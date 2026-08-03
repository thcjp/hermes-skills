# 第57轮提示词 (v57.0) — 企业Cookie获取 + 批量审核通过2,706版本 + DELETE重传38被拒skill + description批量优化

> **日期**: 2026-07-25
> **上一轮完成**: V54/V55/V56 — 994/995 skills上传 + category_mapping.json重建 + enterprise_uploader.py增强(iconUrl/tags/summary_zh/category/subCategories/changelog/MIT-0修正) + batch_operations_v2.py创建 + v6可见性分析报告
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 获取企业账号Cookie → 批量审核通过2,706个待审版本 → DELETE+重传38个被拒skill

## V54-V56完成总结

| 任务 | 版本 | 状态 | 结果 |
|------|------|------|------|
| 830个SKILL.md license修复(Proprietary→MIT) | V52 | ✅ | commit 611a1acc0 |
| 53个source_missing修复 | V53 | ✅ | commit 4b6da3d5d |
| 994/995 skills上传SkillHub | V54 | ✅ | 仅dashboard因保留slug失败 |
| category_mapping.json重建(平台12分类字符串键) | V54 | ✅ | education键已修正 |
| enterprise_uploader.py增强 | V54 | ✅ | iconUrl/tags/summary_zh/category/subCategories/changelog/MIT-0修正 |
| batch_operations_v2.py创建 | V55 | ✅ | check-auth/approve-all/delete-rejected/reupload |
| batch_approve_v2.js创建 | V55 | ✅ | localStorage进度持久化+自动翻页 |
| v6可见性分析报告 | V56 | ✅ | 12因素排名+字段审计+P0/P1/P2行动计划 |
| 批量审核通过2,706版本 | V55-V56 | ❌ | **阻断: 企业Cookie缺失** |
| DELETE+重传38个被拒skill | V55-V56 | ❌ | **阻断: 企业Cookie缺失** |
| 4个org_only skill对外发布 | V55-V56 | ❌ | **阻断: 企业Cookie缺失** |

## 本地已完成审计（无需API）

| P0/P1任务 | 审计结果 | 状态 |
|-----------|----------|------|
| P0-3: enterprise_uploader.py iconUrl字段 | line 410: `'iconUrl': CATEGORY_ICONS.get(platform_category, DEFAULT_ICON)` | ✅ 已完成 |
| P0-4: 107个tags格式(string→list) | 全目录扫描: 0个string格式tags | ✅ 已完成 |
| P0-5: MIT-0 license修正 | 全目录扫描: 0个MIT-0 license | ✅ 已完成 |
| P1-9: 12个分类差异化图标 | enterprise_uploader.py line 61-74: SVG data URI, 12分类+默认 | ✅ 已完成 |
| P1-10: summary_zh补全 | 1035/1035 skills已有summary_zh (100%) | ✅ 已完成 |
| P1-11: description长度(150-280字符) | 25/1035合格, 1010个过短 | ❌ 需执行 |

## 核心阻断: 企业账号Cookie

### 问题诊断

当前cookie文件 `~/.skillhub_cookies.txt` (112字节) 为**个人账号**session:
```
sid=bs2eg6b3e9acc4963ad370b36117555bdc5c7; language=zh; dp.sess=97fdc4ddd2dbd7fb
```

Admin API返回: `"enterprise authentication required"`

### 根因分析

| 编号 | 发现 | 影响 |
|------|------|------|
| 1 | 所有995个skill上传到了个人账号(user_cb75122a)而非企业团队账号(org 862) | skill归属错误 |
| 2 | 个人账号无Admin API权限 | 无法批量审核/删除/发布 |
| 3 | 企业团队已通过认证+绑定微信商户号 | 具备Admin API权限条件 |
| 4 | 浏览器MCP连接超时 | 无法自动获取企业Cookie |

### 解决方案

**用户需手动操作**:
1. 在浏览器中打开 https://www.skillhub.cn
2. 确认登录的是**企业团队账号**(非个人账号)
   - 检查右上角用户名是否显示企业团队名
   - 检查是否能访问 https://www.skillhub.cn/admin 页面
3. 打开浏览器开发者工具 (F12) → Application → Cookies → www.skillhub.cn
4. 复制完整的cookie字符串(至少包含 `sid` 和 `dp.sess` 字段)
5. 保存到 `~/.skillhub_cookies.txt` 文件中
6. 或通过对话提供cookie值，由助手写入文件

**验证命令**:
```bash
cd D:\skills\tools
python batch_operations_v2.py check-auth
```
预期输出: `✅ 认证成功! Skill总数: XXX`

## 实施任务

### 任务1: 获取企业账号Cookie (P0 — 最高优先级，用户操作)

**执行方案**:
1. 用户在浏览器登录企业团队账号
2. 导出完整cookie字符串
3. 保存到 `~/.skillhub_cookies.txt`
4. 运行 `python batch_operations_v2.py check-auth` 验证

**验证标准**:
- `check-auth` 返回 `✅ 认证成功`
- Admin API可正常返回skill列表

### 任务2: 批量审核通过2,706个待审版本 (P0)

**前置条件**: 任务1完成(企业Cookie可用)

**执行方案**:
1. 运行 `python batch_operations_v2.py approve-all` 生成批量审核JS脚本
2. 在浏览器中打开 https://www.skillhub.cn/admin/skill-reviews
3. 在控制台执行 `batch_approve_v2.js`
4. 脚本自动: 遍历271页 × 每页10个 = 2,710个审核项
5. 每批50个保存进度到localStorage，失败自动重试

**备选方案**(如果Admin API支持直接审核):
```bash
# 检查API审核接口
curl -X POST "https://api.skillhub.cn/api/v1/orgs/862/admin/skills/{slug}/approve" \
  -H "Cookie: $(cat ~/.skillhub_cookies.txt)"
```

**验证标准**:
- 2,706个待审版本全部审核通过(剩余<50需人工处理)
- 抽样10个skill在 https://www.skillhub.cn/skills 前台可搜索

### 任务3: DELETE+重传38个被拒skill (P0)

**前置条件**: 任务1完成(企业Cookie可用)

**被拒skill列表(38个)**:
```
ai-writing-style-cloner, api-design-architect, auth-security-architect,
azure-cloud-automator, brand-identity-creator, c-suite-advisor,
canvas-art-designer, clickhouse-olap-expert, cloudflare-edge-developer,
code-review-sentinel, competitive-ad-spy, compliance-manager,
content-cms-architect, content-refiner, copywriting-master,
csv-insight-miner, drama-hit-producer, ebook-factory,
ecommerce-pricing-strategist, geo-rank-architect, hook-retention-master,
intel-sentinel, novel-autopilot, poetry-craftsman, requirement-explorer-pro,
sales-copy-writer, seo-doctor, seo-rank-monopolizer, stealth-browser-assistant,
title-hook-factory, topic-hunter, viral-decoder, viral-prophet,
ai-artist-workstation-pro, lead-research-hunter, duckdb-analytics-engine,
docx-document-master, debug-doctor
```

**执行方案**:
```bash
cd D:\skills\tools
python batch_operations_v2.py reupload-rejected
```
脚本自动: DELETE旧版本 → 等待1秒 → POST重传(含完整字段: MIT license, tags, summary_zh, category, subCategories, iconUrl, changelog)

**验证标准**:
- 38个被拒skill全部DELETE+重传成功
- 重新上传后进入审核队列
- 历史拒绝通知不再出现

### 任务4: 4个org_only skill对外发布 (P0)

**前置条件**: 任务1完成(企业Cookie可用)

**4个org_only skill**:
```
ai-artist-workstation-pro, clickhouse-olap-expert,
requirement-explorer-pro, lead-research-hunter
```

**执行方案**:
```bash
cd D:\skills\tools
python batch_operations_v2.py publish-org-only
```

**验证标准**:
- 4个skill从org_only切换为public
- 前台可搜索

### 任务5: 优化1010个skill的description长度 (P1 — 可本地执行)

**问题**: 1010/1035个skill的description长度<150字符，影响详情页质量和搜索权重。目标: 150-280字符。

**执行方案**:
1. 编写批量优化脚本 `batch_optimize_description.py`:
   - 读取每个SKILL.md的frontmatter
   - 提取displayName, summary, summary_zh, tags
   - 基于已有内容扩写description至150-280字符
   - 保持原有语义不变，不添加虚假功能
2. 批量处理1010个skill
3. 每批50个验证一次，确保格式正确
4. 处理完后需要DELETE+重传(因PUT不可用)

**description扩写策略**:
- 基于summary_zh扩展功能描述
- 添加使用场景说明
- 添加目标用户群体
- 添加核心价值主张
- 确保中文描述自然流畅

**验证标准**:
- 1010个skill的description长度达到150-280字符
- 内容语义与原有description一致
- 无虚假功能描述

### 任务6: 处理5个VPN被封禁skill (P1)

**被封禁skill列表**:
```
v2ray-proxy-tool-free, v2ray-proxy-tool-pro, universal-proxy-pro,
vpn-toolkit-free, vpn-toolkit-pro
```

**执行方案**:
1. 评估每个skill的可修改性
2. 移除VPN/翻墙相关内容
3. 转型为网络安全/隐私保护工具
4. 重新上传触发审核

**验证标准**:
- 可修改的skill重新上传成功
- 通过安全审核

### 任务7: 重新上传memory-orchestrator-sk (P1)

**前置条件**: 任务1完成(企业Cookie可用)

**执行方案**:
```bash
cd D:\skills\tools
python batch_operations_v2.py reupload-deleted
```

**验证标准**:
- memory-orchestrator-sk重新上传成功
- 公开API可查

### 任务8: Git提交与下一轮提示词生成

**执行方案**:
1. 提交V54-V57变更到本地git:
   - docs/plans/next-round-prompt-v55.0.md ~ v57.0.md
   - docs/skillhub-visibility-analysis-v6.html
   - docs/skillhub-visibility-analysis-v4/ ~ v5/
   - data/category_mapping.json (修正education键)
   - data/reports/batch_approve_v3.js
   - data/reports/skill_field_audit_report.json
   - data/reports/skillhub_field_analysis.json
   - tools/enterprise_uploader.py (iconUrl/tags/summary_zh增强)
   - tools/batch_operations_v2.py (新增)
   - tools/batch_field_fix.py (新增)
   - config/project_config.py (如有修改)
   - 1010个SKILL.md description优化(如任务5完成)
2. 推送到origin和hermes-skills
3. 生成 next-round-prompt-v58.0.md

## 任务执行顺序

```
任务1 (获取企业Cookie) ──────────────────────────────┐
                                                      │
任务2 (批量审核通过2,706版本) ── 需要任务1 ──────────┤
                                                      │
任务3 (DELETE+重传38个被拒skill) ── 需要任务1 ──────┤
                                    → 触发任务2审批 ──┤
                                                      ├──→ 任务8 (Git提交)
任务4 (4个org_only对外发布) ── 需要任务1 ────────────┤
                                                      │
任务5 (优化1010个description) ── 可并行执行 ─────────┤
                                    → 需要重传 ──────┤
                                                      │
任务6 (处理5个VPN skill) ── 可并行执行 ──────────────┤
                                                      │
任务7 (重传memory-orchestrator-sk) ── 需要任务1 ─────┘
```

**说明**:
- 任务1是所有API操作的前置条件(用户手动操作)
- 任务5可立即并行执行(不依赖API)
- 任务6可立即并行执行(本地内容修改)
- 任务2/3/4/7需要任务1完成后执行

## 验证检查清单

- [ ] 企业账号Cookie获取成功(check-auth返回✅)
- [ ] 2,706个待审版本批量审核通过(剩余<50)
- [ ] 38个被拒skill DELETE并重新上传成功
- [ ] 4个org_only skill切换为public
- [ ] 1010个skill的description长度达到150-280字符
- [ ] 5个VPN skill内容修改完成
- [ ] memory-orchestrator-sk重新上传成功
- [ ] 抽样10个skill在前台可搜索
- [ ] Git提交并推送
- [ ] 下一轮提示词v58.0生成

## 约束

1. **增强已有代码** — 不创建碎片化新文件，所有修复功能集成到现有工具脚本
2. **不模拟/mock** — 所有操作必须真实执行，审核/删除/上传/生成均实际发生
3. **幂等操作** — 修复函数必须可重复执行不产生副作用
4. **向后兼容** — 增强不能破坏enterprise_uploader.py现有功能
5. **内容保真** — description扩写不得改变技能原有语义，不添加虚假功能
6. **网络容错** — API失败不应阻塞其他任务
7. **质量底线** — 不得引入降低审计等级的修改
8. **SkillHub优先** — 审核通过是最高优先级
9. **分类统一** — 本地分类=skillhub分类=clawhub分类
10. **版本同步** — 本地skill版本升级后必须同步到全部3个平台
11. **企业账号** — 所有API操作必须使用企业团队账号Cookie，不使用个人账号
