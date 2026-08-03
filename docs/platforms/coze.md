# Coze 平台规则文档

> 适配器: `tools/coze_adapter.py` | 注册表: `platform_registry['coze']`

## 平台概述

Coze(扣子)是字节跳动旗下的 AI Bot 开发平台，支持将 skill 转换为 Coze plugin 并发布。创作者可获得 70% 收入分成。当前需要官方邀请才能上传，处于 pending 状态。

**关键属性**:
- 可变现: 是(70% 创作者分成)
- 适配器模块: `coze_adapter`
- 同步函数: `coze_adapter.CozeAdapter.check_eligibility`(资格检查)
- 上传状态: pending(需官方邀请)
- 分成比例: 70%(创作者) / 30%(平台)

## 认证要求

### 当前状态
- **上传需要官方邀请**: Coze 平台目前需要官方邀请才能开通上传权限
- `CozeAdapter.upload_skill()` 返回 `{'status': 'pending', 'reason': 'coze_invite_required'}`
- 获取邀请后，需实现实际的上传逻辑

### 认证凭证(预期)
- Coze 开发者平台 API Token
- 环境变量: `COZE_API_TOKEN`
- 配置文件: `~/.coze/config.json`

## 速率限制

| 参数 | 值 | 说明 |
|------|-----|------|
| cooldown | 10s | 最小请求间隔(预期，需官方确认) |
| max_per_hour | 20 | 每小时最大上传数(预期) |
| max_per_day | 50 | 每天最大上传数(预期) |

**注意**: 速率限制为预期值，实际限制需在获得上传权限后确认。

## 预上传检查项

| 检查项 | 阻断级别 | 说明 |
|--------|---------|------|
| dedup | 阻断(fail-safe) | 内容指纹去重 |
| quality_gate | 非阻断 | 质量门控 |
| security_scan | 非阻断 | 安全风险扫描 |

**来源**: `pre_upload_checks.run_pre_checks()` + `platform_registry['coze'].pre_checks`

## 资格检查(6类标准)

Coze 使用 6 类评估标准判断 skill 是否符合上架要求:

| 评估项 | 权重 | 检查内容 |
|--------|------|---------|
| 案例完整性 | 20 | SKILL.md 包含使用案例/示例 |
| 名称规范 | 15 | slug 和 displayName 符合命名规范 |
| 描述准确 | 20 | summary 准确描述功能，无夸大 |
| 安全合规 | 20 | 无硬编码密钥/无危险代码，需 SkillHub 已发布 |
| 定价合理 | 10 | 定价符合市场区间(0-199.9) |
| 质量达标 | 15 | 通过 quality_gate 检查 |

**总分**: 100 分，全部通过即为 eligible

**分类**:
- `paid_eligible`: 全部通过 + 付费 skill → 可上架 + 收入预估
- `free_eligible`: 全部通过 + 免费 skill → 可上架
- `not_eligible`: 有未通过项 → 不可上架

**来源**: `coze_adapter.COZE_CRITERIA` + `CozeAdapter.check_eligibility()`

## 格式转换

SKILL.md → Coze plugin.json:
```json
{
  "name": "slug",
  "display_name": "displayName",
  "description": "summary",
  "tools": [...],
  "version": "1.0.0",
  "license": "MIT",
  "homepage": "",
  "config": {
    "price_model": "per_call",
    "price_amount": 0
  }
}
```

**来源**: `coze_adapter.CozeAdapter.convert_format()`

## 发布流程

```
1. 资格检查 → CozeAdapter.check_eligibility(skill_data)
2. 格式转换 → CozeAdapter.convert_format(skill_md_content)
3. 上传(待实现) → CozeAdapter.upload_skill(skill_path, slug)
   └─ 当前返回 pending(coze_invite_required)
4. 收入预估 → price * 0.70(创作者分成)
```

## 收入分成

| 项目 | 比例 |
|------|------|
| 创作者 | 70% |
| 平台 | 30% |

**计算**: `estimated_revenue = price * COZE_CREATOR_SHARE`

**来源**: `coze_adapter.COZE_CREATOR_SHARE = 0.70`

## 常见问题

### Q: 为什么 Coze 上传返回 pending
A: Coze 平台需要官方邀请才能上传。当前 `upload_skill()` 返回 pending 状态。获得邀请后需实现实际的上传逻辑。

### Q: Coze 资格检查中安全合规项需要什么
A: 需要 skill 已在 SkillHub 发布(review_status 为 published/approved/public_published)。未在 SkillHub 发布的 skill 不通过安全合规检查。

### Q: Coze 和 SkillHub 的收入分成有什么区别
A: SkillHub 通过 SkillPay 机制变现(企业认证 + 微信支付)，Coze 提供 70% 创作者分成。

## 封禁风险点

| 风险 | 严重度 | 描述 | 缓解措施 |
|------|--------|------|---------|
| 资格不满足 | 低 | 未通过 6 类评估标准 | 资格检查前置 |
| 未在 SkillHub 发布 | 中 | 安全合规项要求 SkillHub 已发布 | 先完成 SkillHub 同步 |
| 定价异常 | 低 | 定价超出 0-199.9 区间 | 定价合理性检查 |

## 与其他平台的差异

| 维度 | SkillHub | ClawHub | Coze |
|------|---------|---------|------|
| 变现 | SkillPay | 无 | 70% 分成 |
| 上传状态 | 可用(API+CLI) | 可用(CLI) | pending(需邀请) |
| 评估标准 | 质量门控 | 无 | 6类标准(100分) |
| 安全合规 | security_scan | 跳过 | 需 SkillHub 已发布 |
| 格式转换 | 原生SKILL.md | 原生SKILL.md | plugin.json |
