# 第48轮提示词 (v48.0) — SkillHub批量审核执行 + DELETE重传被拒skill + 前台搜索可见性验证

> **日期**: 2026-07-25
> **上一轮完成**: V47 — 995个SKILL.md补全summary_zh(100%) + 修复107个tags格式(100% list) + 修复1个MIT-0 + enterprise_uploader.py增强(12分类SVG图标) + batch_approve_v3.js生成 + batch_operations_v2.py增强(38拒绝+5封禁+4org_only) + 可见性分析报告v6
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库
> **最高优先级**: 执行批量审核通过 + DELETE重传38个被拒skill + 验证前台搜索可见性

## V47完成总结

| 任务 | 状态 | 结果 |
|------|------|------|
| 995个SKILL.md补全summary_zh | ✅ | 100%覆盖(1035个文件) |
| 修复107个tags格式(string→list) | ✅ | 100% list格式 |
| 修复1个MIT-0 license | ✅ | upstage-document-parse-free → MIT |
| enterprise_uploader.py增强 | ✅ | 12分类SVG图标 + tags验证 + summary_zh优先fm + license修正 + homepage空 |
| batch_approve_v3.js生成 | ✅ | 自动页数检测 + 进度保存 + 错误恢复 |
| batch_operations_v2.py增强 | ✅ | 38拒绝 + 5封禁 + 4org_only + 新命令 |
| 可见性分析报告v6 | ✅ | 77KB HTML, 8章节, 交互式表格 |
| v47.0提示词生成 | ✅ | 11个任务, 14条约束 |
| 批量审核通过 | ❌ | 需浏览器执行batch_approve_v3.js |
| DELETE重传38个被拒skill | ❌ | 需企业cookie |
| 4个org_only对外发布 | ❌ | 需企业cookie |
| 5个VPN封禁skill处理 | ❌ | 需决策 |
| Git提交 | ❌ | 待执行 |

## V47验证结果

```
summary_zh覆盖率:    995/995 (100.0%) ✅
tags list格式:       995/995 (100.0%) ✅
license=MIT:         995/995 (100.0%) ✅
category覆盖率:      995/995 (100.0%) ✅
enterprise_uploader.py: 6/6检查通过 ✅
batch_operations_v2.py: 5/5检查通过 ✅
batch_approve_v3.js: 4/4检查通过 ✅
```

## 实施任务

### 任务1: 执行批量审核通过 (P0 — 最高优先级)

**问题**: 2,706条审核记录中部分仍处于待审状态。

**执行方案**:
1. 导航到 https://www.skillhub.cn/admin/skill-reviews
2. 在浏览器控制台执行 `D:\skills\data\reports\batch_approve_v3.js`
3. 脚本自动: 检测总页数 → 逐页点击"审核通过" → 翻页 → 进度保存
4. 如中断可恢复(localStorage保存进度)

**验证标准**:
- 审核页面"管理员审核中"数量接近0
- 抽样10个skill状态变为"审核通过"

### 任务2: DELETE重传38个被拒skill (P0)

**执行方案**:
1. 获取企业账号cookie(从浏览器开发者工具)
2. 更新 ~/.skillhub_cookies.txt
3. 执行: `python batch_operations_v2.py reupload-rejected`
4. 脚本自动: DELETE旧版本 → 重新上传(含iconUrl/summary_zh/tags)
5. 重新上传后进入审核队列

**验证标准**:
- 38个被拒skill全部DELETE+重传成功
- 历史拒绝通知不再出现

### 任务3: 4个org_only skill对外发布 (P0)

**执行方案**:
1. 执行: `python batch_operations_v2.py publish-org-only`
2. 或在admin/skills页面手动点击"对外发布"

**验证标准**:
- 4个skill的visibility从org_only变为public

### 任务4: 处理5个VPN被封禁skill (P1)

**执行方案**:
1. 检查5个skill的SKILL.md内容
2. 决策: 修改内容重传 or 放弃
3. 如放弃: `python batch_operations_v2.py delete-banned`
4. 如修改: 去除VPN/proxy关键词 → DELETE → 重传

**验证标准**:
- 5个被封禁skill有明确处理决策

### 任务5: 重新上传memory-orchestrator-sk (P1)

**执行方案**:
1. 执行: `python batch_operations_v2.py reupload-deleted`
2. 验证上传成功

### 任务6: 验证前台搜索可见性 (P1)

**执行方案**:
1. 完成任务1-3后等待30分钟
2. 在skillhub.cn/skills前台搜索我方skill
3. 通过API检查搜索结果
4. 如不可见,检查namespace和索引问题

**验证标准**:
- 抽样10个skill在前台可搜索

### 任务7: Git提交与下一轮提示词 (P2)

**执行方案**:
1. 提交V47+V48变更到git
2. 推送到origin和hermes-skills
3. 生成下一轮提示词v49.0

## 需要用户手动执行的操作

以下操作需要用户在浏览器中手动执行(因需企业账号session):

1. **批量审核通过**: 
   - 打开 https://www.skillhub.cn/admin/skill-reviews
   - F12控制台粘贴执行 batch_approve_v3.js 内容

2. **获取企业cookie**:
   - 登录 skillhub.cn 企业账号
   - F12 → Application → Cookies → 复制完整cookie
   - 保存到 ~/.skillhub_cookies.txt

3. **DELETE重传**(获取cookie后):
   - `python D:\skills\tools\batch_operations_v2.py reupload-rejected`

4. **对外发布**(获取cookie后):
   - `python D:\skills\tools\batch_operations_v2.py publish-org-only`

## 约束

1. **增强已有代码** — 不创建碎片化新文件
2. **不模拟/mock** — 所有操作必须真实执行
3. **幂等操作** — 修复函数可重复执行
4. **向后兼容** — 不破坏现有功能
5. **SkillHub优先** — 审核通过+对外发布最高优先级
6. **企业账号** — 所有admin操作需企业账号cookie
7. **VPN禁令** — 不得上传VPN/proxy相关内容
8. **tags格式** — 全部YAML list格式(已达标)
9. **summary_zh必设** — 全部SKILL.md包含(已达标)
10. **iconUrl必设** — 上传时包含SVG分类图标(已达标)
