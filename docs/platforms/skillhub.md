# SkillHub 平台规则文档

> 适配器: `tools/skillhub_adapter.py` | 上传: `tools/enterprise_uploader.py` | 注册表: `platform_registry['skillhub']`

## 平台概述

SkillHub 是本项目唯一可变现平台，通过 SkillPay 机制实现 skill 付费使用。支持三种定价模式：按次付费(per_call)、月度订阅(monthly)、一次性购买(one_time)。

**关键属性**:
- 可变现: 是(SkillPay)
- 适配器模块: `skillhub_adapter`
- 同步函数: `enterprise_uploader.upload_skill`
- 上传通道: API(含 WAF 重试) / CLI(fallback)
- 组织ID: 862

## 认证要求

### 凭证优先级
1. **API Key**(推荐): `~/.skillhub/credentials.json` 中的 org API Key
2. **Cookie 文件**: `~/.skillhub_cookies.txt`(UTF-8-sig 编码，自动去 BOM)
3. **环境变量**: `SKILLHUB_SESSION_COOKIE`

### 企业认证
- **Proprietary license 必须企业认证**: 个人账号使用 Proprietary 会触发 Pay Skill 审核(需企业认证 + 微信支付商户绑定)
- 个人账号仅可使用: MIT, Apache-2.0, BSD-3-Clause, ISC
- 检查函数: `skillhub_adapter.check_enterprise_certification()`

### 凭证配置
```
文件: config/platform_config.py → SKILLHUB_CREDENTIALS_FILE
环境: SKILLHUB_COOKIE, SKILLHUB_API_KEY
```

## 速率限制

| 参数 | 值 | 说明 |
|------|-----|------|
| rpm | 2 | 每分钟最大请求数 |
| cooldown | 60s | 最小请求间隔(V138 S1: 12s→60s) |
| max_per_hour | 10 | 每小时最大上传数 |
| max_per_day | 20 | 每天最大上传数(V138 S1: 100→20) |

**来源**: `skillhub_adapter.SKILLHUB_RATE_LIMIT`(收口自 `rate_limiter.py` + `daily_sync.py`)

**根因**: 2026-07-24 单日上传 1098 个 skill 导致账号被封禁。原配置(12s 间隔 / 100 日限)过于宽松。

## 预上传检查项

| 检查项 | 阻断级别 | 说明 |
|--------|---------|------|
| dedup | 阻断(fail-safe) | 内容指纹去重(SHA-256 + SimHash)，模块不可用时阻断 |
| quality_gate | 非阻断 | 质量门控(评分 + 删除状态)，不可用时跳过 |
| security_scan | 非阻断 | 安全风险扫描，高危阻断，中低危警告 |
| proprietary_check | 阻断 | Proprietary license + 企业认证检查(SkillHub 专用) |

**来源**: `pre_upload_checks.run_pre_checks()` + `platform_registry['skillhub'].pre_checks`

## 发布流程

### 上传流程(V139 S4: 统一上传通道)
```
sync_to_skillhub()
  ├─ should_use_api() = True → enterprise_uploader.upload_skill(skip_publish=True)
  │    ├─ 门控检查(get_gate_status)
  │    ├─ 质量门控(marketing + security + anti-hallucination + rating)
  │    ├─ Proprietary 前置拦截
  │    ├─ 速率限制预检
  │    ├─ 内容去重预检(fail-safe)
  │    ├─ 构建 payload(分类 + 图标 + tags + summary_zh)
  │    ├─ API 上传(_upload_with_waf_retry: 两级 WAF 重试)
  │    └─ record_rate_limit_upload
  └─ should_use_api() = False → _skillhub_cli_fallback(CLI, 缺 WAF 重试)
```

### WAF 重试策略
| 级别 | 触发条件 | 策略 |
|------|---------|------|
| 1 | HTTP 566(腾讯 EdgeOne WAF 拦截) | 截断 files 内容为仅 frontmatter |
| 2 | 第 1 级仍 566 | base64 编码 files 内容 |

**来源**: `skillhub_adapter.WAF_RETRY_CONFIG` + `enterprise_uploader._upload_with_waf_retry`

### 发布后流程(approve → publish → star)
```
post_upload_publish(slug, skill_id)
  ├─ Step 1: approve (pending → published)
  ├─ Step 2: publish_to_community (visibility=public)
  └─ Step 3: star_skill (提升搜索排名)
```

**每步间隔**: 60s(rate_limit 控制，V138 S3 修复)

## 审核状态机

```
pending ──approve──→ published ──unlist──→ unlisted
   │                    │                     │
   │                    ├──delete──→deleted   ├──delete──→deleted
   │                    │                     │
   └──reject──→rejected ┘                   relist
                    │                         │
                  resubmit                    ↓
                    │                      published
                    └──→ pending
```

**来源**: `skillhub_adapter.REVIEW_STATES` + `can_transition()` + `get_valid_actions()`

## 封禁风险点

| 风险 | 严重度 | 描述 | 缓解措施 | 根因来源 |
|------|--------|------|---------|---------|
| 速率过快 | 高 | 上传间隔 <30s 或每日 >20 个 | cooldown=60s, max_per_day=20 | 2026-07-24 封禁(单日 1098 个) |
| 近似重复内容 | 高 | summary/core features 量化词相同 | _QUANT_POOL 轮选 + 11 分类差异化 | 2026-07-24 封禁(990 个近似重复) |
| Proprietary + 个人账号 | 中 | 个人账号使用 Proprietary 触发 Pay Skill 审核 | enterprise_uploader 前置拦截 | V138 S5 修复 |
| 发布后三步连发 | 中 | approve/publish/star 间隔 <1s | 每步纳入 rate_limit，间隔 60s | V138 S3 修复 |
| 去重模块不可用时放行 | 高 | ImportError 时 pass 放行 | fail-safe 阻断(dedup_blocked=True) | V138 S2 修复 |

## 团队分类映射

| 平台分类键 | 团队分类名 | 数字ID |
|-----------|----------|--------|
| office-efficiency | 通用办公 | 11039 |
| content-creation | 内容创作 | 11040 |
| dev-programming | 研发工具 | 11041 |
| data-analysis | 数据分析 | 11042 |
| design-media | 设计多媒体 | 11043 |
| ai-agent | AI Agent | 11044 |
| knowledge-management | 知识管理 | 11045 |
| business-ops | 商业运营 | 11046 |
| it-ops-security | IT运维安全 | 11047 |
| education | 教育学习 | 11048 |

**来源**: `enterprise_uploader.TEAM_CATEGORY_IDS` + `category_mapping.json`

## 常见问题

### Q: 上传返回 566 错误
A: 腾讯 EdgeOne WAF 拦截，通常因 SKILL.md 内容含 SQL 代码或特殊字符。系统已自动两级重试(截断 → base64 编码)。

### Q: skill 停留在 pending 状态
A: 上传后未执行发布流程(approve → publish → star)。检查 `platform_ops.post_upload_publish` 是否被调用。

### Q: Proprietary license 被拦截
A: 个人账号不能使用 Proprietary。需要企业认证 + 微信支付商户绑定，或改用 MIT license。

### Q: 上传被速率限制
A: 检查 `daily_sync` 的速率限制计数。cooldown=60s, max_per_day=20。等待 cooldown 过期后重试。
