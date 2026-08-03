# 第45轮提示词 (v45.0) — SkillHub 可见性修复与L9审计集成

> **日期**: 2026-07-24
> **上一轮完成**: V44部分实施 (category修复完成, check_visibility/db.py迁移代码/deep_quality_audit.py L9函数已编写)
> **核心原则**: 严禁新增碎片化代码，必须增强已有流程/功能/代码/配置/数据库

## 复核结论

### 已完成 (V44部分)
- ✅ category推断与修复: 0个NULL/无效category剩余
- ✅ auto_publish.py check-visibility() 函数已编写
- ✅ db.py community_published/download_ready 迁移代码已编写
- ✅ deep_quality_audit.py check_visibility_quality() L9函数已编写并集成到check_skill()
- ✅ fix_missing_fields.py TAG_TO_CATEGORY_MAP + infer_category() 已编写

### 待完成 (V45本轮)
- ❌ db.py迁移未实际执行: community_published/download_ready字段未存在于数据库
- ❌ L9未集成到run_audit()报告: run_audit()不传enable_l9参数, 不收集L9统计, 不输出L9报告
- ❌ L9未集成到main(): 缺少--no-layer9 CLI参数
- ❌ 45个不可见技能未修复: 23个NULL visibility + 22个org_only visibility
- ❌ 8个retry_pending技能未重试上传
- ❌ 7个原始pending_review技能SKILL.md仍有问题: 重复YAML/外部URL/API密钥/营销注入/乱码
- ❌ 增强版community publish JS未生成

## 实施任务

### 任务A: 运行db.py迁移
执行 `python tools/db.py` 添加 community_published/download_ready 字段到实际数据库

### 任务B: 完成L9集成到run_audit()和main()
1. run_audit() 添加 enable_l9 参数
2. check_skill() 调用传入 enable_l9
3. 收集L9统计: l9_score_sum, l9_grades, l9_available_count, l9_issues_list
4. 输出L9报告区块 (与L8格式一致)
5. main() 添加 --no-layer9 CLI参数

### 任务C: 数据库批量修复45个不可见技能
将 platform_uploads 中 23个NULL + 22个org_only 的 visibility 更新为 'public'
同时更新 community_published=1

### 任务D: 生成增强版community publish JS
执行 `python tools/auto_publish.py gen-community-publish-js`

### 任务E: 修复7个pending_review技能SKILL.md
1. version-control-workflows — 删除重复YAML tools/tags, 删除外部URL, 删除API密钥
2. data-analysis-toolkit — 同上
3. trading-strategy-guide — 同上 + 修复日文乱码内容
4. xml-parser-tool — 同上
5. text-rpg-arcade-v3 — 同上
6. video-upload-stream-tool — 同上 + 删除attoaioz.cyou URL和密钥占位符
7. pdf-compressor-tool — 同上

### 任务F: 运行审计验证 + Git提交
1. 运行 `python tools/deep_quality_audit.py` 验证L9正常工作
2. 运行 `python tools/auto_publish.py check-visibility` 验证可见性修复
3. Git add + commit

## 约束
1. 不创建新文件（除计划文件和报告文件外）
2. 不新增独立脚本 — 所有功能集成到现有工具
3. 不模拟/mock — 所有数据库操作必须真实执行
4. 幂等迁移 — ALTER TABLE 必须幂等
5. 向后兼容 — 增强不能破坏现有命令功能
