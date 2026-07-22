# SkillHub Platform Review 处理方案

## 问题描述
60个企业版技能（org 862）卡在platform_review状态，admin API无法干预。

## 已执行操作
- test-paid-skill 已删除 ✅

## 待执行操作
### 联系平台支持
- **邮箱**: skillhub_ipr@tencent.com
- **邮件主题**: 【技能审核】团队版(org 862) 60个技能卡在platform_review状态，请求协助审核
- **邮件内容模板**:

```
您好，

我们是SkillHub团队版用户（org ID: 862），有60个技能自上传后一直处于platform_review状态，
长时间未完成审核。这些技能均已通过本地pre-check验证，frontmatter格式规范，
无违规内容。请协助审核以下技能：

[附60个技能slug列表]

如需补充材料或有任何问题，请随时联系。

谢谢！
```

### 备选策略
如平台支持无响应，考虑：
1. 删除卡在platform_review的技能
2. 重新上传（新slug或相同slug）
3. 等待平台批量审核处理

## 60个platform_review技能slug列表
（需从SkillHub admin API获取完整列表，可通过以下命令查询）
```
GET https://api.skillhub.cn/api/v1/orgs/862/admin/skills?status=platform_review&page=1&pageSize=100
```
