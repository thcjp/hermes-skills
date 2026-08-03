# ClawHub 平台规则文档

> 适配器: `tools/clawhub_adapter.py` | 上传: `tools/clawhub_batch_uploader.py` | 注册表: `platform_registry['clawhub']`

## 平台概述

ClawHub 是海外开源 skill 生态平台，无支付机制。主要用于开源 skill 的分发和社区贡献。所有上传的 skill 默认 MIT license，面向全球开发者社区。

**关键属性**:
- 可变现: 否(无支付机制)
- 适配器模块: `clawhub_adapter`
- 同步函数: `clawhub_batch_uploader.upload_skill`
- 上传通道: clawhub CLI
- 开源生态: 是

## 认证要求

### 凭证配置
- **CLI 认证**: 通过 `clawhub` CLI 工具登录(交互式)
- **API Token**: 环境变量 `CLAWHUB_API_TOKEN`
- **配置文件**: `~/.clawhub/config.json`

### License 要求
- 必须为开源 license: MIT, Apache-2.0, BSD-3-Clause, ISC
- **不支持 Proprietary**(开源生态平台)
- 上传前自动检查 license 合规性

## 速率限制

| 参数 | 值 | 说明 |
|------|-----|------|
| cooldown | 5s | 最小请求间隔(海外平台限制较宽松) |
| max_per_hour | 30 | 每小时最大上传数 |
| max_per_day | 100 | 每天最大上传数 |

**注意**: ClawHub 速率限制比 SkillHub 宽松，因为海外平台无反垃圾系统触发风险。但仍需控制频率避免 API 限流。

## 预上传检查项

| 检查项 | 阻断级别 | 说明 |
|--------|---------|------|
| dedup | 阻断(fail-safe) | 内容指纹去重(SHA-256 + SimHash) |
| quality_gate | 非阻断 | 质量门控(评分 + 删除状态) |

**来源**: `pre_upload_checks.run_pre_checks()` + `platform_registry['clawhub'].pre_checks`

**注意**: ClawHub 不执行 security_scan 和 proprietary_check(开源平台无安全审核流程)。

## 发布流程

```
sync_to_clawhub(slug, skill_md, new_version, skill_id)
  ├─ 1. 读取 SKILL.md 内容
  ├─ 2. 解析 frontmatter(slug, version, license, tags)
  ├─ 3. 验证 license 为开源类型
  ├─ 4. 构建 ClawHub 上传 payload
  ├─ 5. 调用 clawhub CLI 上传
  │    └─ clawhub upload <skill_dir> --version <version>
  ├─ 6. 记录 platform_upload 结果
  └─ 7. 返回同步结果
```

### 批量上传
```bash
python tools/clawhub_batch_uploader.py upload-all
```

### 单个上传
```bash
python tools/clawhub_batch_uploader.py upload <slug>
```

### 上传结果状态
| 状态 | 说明 |
|------|------|
| success | 上传成功 |
| failed | 上传失败(CLI 错误或网络问题) |
| version_exists | 版本已存在(无需重复上传) |
| rate_limited | API 限流(等待后重试) |
| license_blocked | License 不合规(非开源 license) |

## 深度差异化要求

从 clawhub 下载的 600 个 skill 必须经过深度差异化后才能上传：
- **质量增强**: 基于用户评价和在线痛点改进功能
- **成本优化**: 降低 LLM 调用成本，提升效率
- **性能提升**: 优化执行速度和资源消耗
- **去重检查**: 确保差异化后内容与源 skill 不高度相似(SimHash 阈值 3)

差异化后的 skill 同时上传到 SkillHub 和 ClawHub(双平台策略)。

## 适配器接口

ClawHub 适配器(`clawhub_adapter.py`)对标 `coze_adapter.py` 组织模式：

```python
from clawhub_adapter import ClawHubAdapter

adapter = ClawHubAdapter()
# 资格检查
result = adapter.check_eligibility(skill_data)
# 格式转换
plugin = adapter.convert_format(skill_md_content)
# 上传
result = adapter.upload_skill(skill_path, slug)
```

## 常见问题

### Q: clawhub CLI 未安装
A: ClawHub CLI 需单独安装。运行 `npm install -g clawhub` 或从 ClawHub 官网下载。

### Q: 上传返回 license 错误
A: ClawHub 仅接受开源 license。检查 SKILL.md frontmatter 中 license 字段是否为 MIT/Apache-2.0/BSD/ISC。

### Q: ClawHub 与 SkillHub 的区别
A:
- ClawHub: 海外开源生态，无支付，宽松速率限制，无 WAF 拦截
- SkillHub: 国内企业平台，SkillPay 变现，严格速率限制，WAF 重试

## 封禁风险点

| 风险 | 严重度 | 描述 | 缓解措施 |
|------|--------|------|---------|
| 重复内容上传 | 低 | 相同内容以不同 slug 上传 | dedup 预检查(fail-safe) |
| License 不合规 | 中 | 使用非开源 license | 上传前 license 验证 |
| API 限流 | 低 | 短时间大量上传 | cooldown=5s, max_per_day=100 |

## 与 SkillHub 的差异对比

| 维度 | SkillHub | ClawHub |
|------|---------|---------|
| 变现 | SkillPay(按次/月度/买断) | 无 |
| 速率限制 | cooldown=60s, 20/day | cooldown=5s, 100/day |
| WAF 重试 | 两级(截断+base64) | 无 |
| 安全审核 | security_scan | 跳过 |
| License 限制 | MIT~Proprietary(企业认证) | 仅开源(MIT/Apache/BSD/ISC) |
| 发布后流程 | approve→publish→star | 无(直接发布) |
| 审核状态机 | pending→published→unlisted | 无审核状态 |
