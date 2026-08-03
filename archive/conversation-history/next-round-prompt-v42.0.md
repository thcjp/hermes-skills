# 第42轮提示词 (v42.0)

> **日期**: 2026-07-24
> **上一轮完成**: Phase 1-7 架构治理全部完成，44项验证全部通过
> **Git 提交**: 2e604e81 (94 files, +5410/-1960), cdae7300 (凭证安全修复)

## 上一轮完成情况

### Phase 1: 统一配置存取消费 ✅
- 创建 `config/` 目录（`project_config.py`, `platform_config.py`, `github_repo_strategy.py`）
- 修改 37 个脚本的硬编码路径为统一配置导入
- 修复 SQL 操作符优先级 bug
- 统一 `TRACE_PASS_THRESHOLD = 42`

### Phase 2: 工具/产品物理分离 ✅
- `skill-registry/` → `tools/`（69 个 .py 文件）
- 986 个 JSON 数据文件 → `data/`
- 19 个 MD 文档 → `docs/`
- 6 个顶层脚本 → `tools/scripts/`
- 删除 3 个冗余数据库文件
- 更新 43 个脚本的路径引用

### Phase 3: 数据库清理和增强 ✅
- 删除 3 个冗余 DB 文件
- 添加 `free_slug`、`paid_slug` 字段
- 迁移 `skill_type` 到三轨模型：source=600, free=1675, paid=599, tool=8
- 规范化 `pricing_tier`：L1-入门级(597), L2-标准级(807), L3-专业级(967), L4-企业级(511)
- 修复 `is_paid` NULL 值（0 个剩余）
- 修复 `edition` 空值（0 个剩余）
- 重建 FTS：2121 条记录 + 3 个触发器（INSERT/UPDATE/DELETE）
- 创建 3 个看板视图：`v_skill_lifecycle`、`v_platform_summary`、`v_three_track_overview`

### Phase 4: 文档统一 ✅
- 创建 `docs/ARCHITECTURE.md` 作为唯一权威架构文档
- 重写 `README.md` 含目录导航
- 归档 57 个历史计划文档到 `docs/plans/archive/`
- 移动 12 个报告文件到 `docs/reports/`
- 删除 4 个 v1 审核报告和 3 个触发文档（合并到 ARCHITECTURE.md）

### Phase 5: 顶层文件清理 ✅
- 移动 `upload-packaged.ps1` 到 `tools/scripts/`
- 删除 4 个空目录（agent-ai, coze, failed-temp, promptbase）
- 更新 `.gitignore`

### Phase 6: 每日同步实现 ✅
- 创建 `tools/daily_sync.py` 统一同步入口
- 更新 `dashboard_server.py` 使用三轨模型视图和 `v_platform_summary`

### Phase 7: 全量验证 ✅
- 44 项验证全部通过
- 0 个硬编码路径
- 数据库完整性验证通过
- 目录结构验证通过

### 待处理
- GitHub 推送因网络超时失败，需重试 `git push origin main` 和 `git push hermes-skills main`

## 当前项目状态

| 维度 | 数据 |
|------|------|
| 总 Skill 数 | 2882 |
| 三轨分布 | source=600, free=1675, paid=599, tool=8 |
| 定价分层 | L1-入门级=597, L2-标准级=807, L3-专业级=967, L4-企业级=511 |
| SkillHub | success=1126, retry_pending=16, blocked=1 |
| ClawHub | success=1152, fail=2, retry_pending=1 |
| GitHub | success=1159 |
| FTS 记录 | 2121 |
| 看板视图 | 3 个（v_skill_lifecycle, v_platform_summary, v_three_track_overview） |

## 第42轮任务清单

### 任务1: GitHub 推送重试
- `git push origin main`（私有备份仓库）
- `git push hermes-skills main`（公开引流仓库）
- 验证两个仓库的提交状态一致

### 任务2: ClawHub 定时上传监控
- 检查 ClawHub 定时任务（ID: 5f5e0baf）运行状态
- 查看已上传数量和剩余数量
- 如果定时任务失败，手动执行上传

### 任务3: SkillHub 待审 skill 处理
- 16 个 retry_pending 状态的 skill 需要处理
- 1 个 blocked_by_quality_gate 的 skill 需要修复后重提
- 检查是否有新的 pending_review 状态

### 任务4: 看板服务更新验证
- 启动 `dashboard_server.py` 验证三轨模型数据正确显示
- 验证 `v_skill_lifecycle`、`v_platform_summary`、`v_three_track_overview` 视图数据
- 确认 pricing_tiers 分层显示正确

### 任务5: daily_sync.py 集成测试
- 运行 `python tools/daily_sync.py --report` 验证报告生成
- 验证报告数据与数据库一致
- 考虑将 daily_sync.py 配置为定时任务

### 任务6: 源 skill 发现与增强
- 运行 `auto_discover.py` 检查是否有新的优秀 skill 可下载
- 对已有 source 类型 skill 检查是否有版本更新
- 下载新 skill 后执行差异化增强流程

### 任务7: 三轨模型完整性检查
- 检查 source 类型 skill 是否都有对应的 free 版
- 检查 free 类型 skill 是否都有对应的 paid 版
- 识别缺失的轨道并生成增强计划
- 验证 `free_slug`、`paid_slug`、`source_slug` 关联正确性

## 验证检查清单

- [ ] GitHub origin 推送成功
- [ ] GitHub hermes-skills 推送成功
- [ ] ClawHub 定时任务正常运行
- [ ] SkillHub 16 个 retry_pending 已处理
- [ ] 看板服务正确显示三轨模型
- [ ] daily_sync.py --report 正常运行
- [ ] 三轨模型关联完整性验证通过
- [ ] 新发现的 skill 已下载并入库
