# Round 38 执行提示词 v38.0

## 上下文
- **上一轮**: Round 37 (Git: 081cf7f0, 2105 files, +60051/-89044)
- **当前日期**: 2026-07-24
- **数据库**: 2097 skills, 0 NULL pricing_tier, 0 'free' tier
- **平台状态**: SkillHub 2068 published/12 pending_review, ClawHub 855 published/502 pending, Hermes 1067 published

## Round 37 完成情况

### Task 1 (P0): 修复2个CRITICAL frontmatter问题 - 完成 ✅
- 修复 logo-brand-identity-cellcog 和 ui-ux 的缺失 `---` 分隔符
- 补充 homepage、任务定义、输入输出、使用指南、依赖说明等缺失section
- 修复错位 `---` 分隔符和空Q1回答
- 审计结果: critical=0 ✅

### Task 2 (P0): 修复20个L7a B级模板块 - 完成 ✅
- 20个skill的"基础使用"表格行从通用模板替换为各自特有的具体功能描述
- 涉及skill: clawprint, elite-frontend-design, figma-design, finance-accounting, finance-report-analyzer, free-web-search, frontend-design, html-designer, javascript-skills, live-stream-script, magic-api-generate, manage-liquidity, minimalist-design-system, molted-work, pandoc-convert-openclaw, rss-fetcher, shadcn-ui, telegram, ui-ux-developer-tool, ux
- 审计结果: L7a A=2097, B=0, template_blocks=0 ✅

### Task 3 (P0): 修复L6 EMPTY_LIMITATIONS - 完成 ✅
- 修复41个skill的已知限制段落(3个新增段落 + 3个替换占位符 + 35个填充空段落)
- 4个skill已有充分内容无需修改
- 涉及packaged(18个)和differentiated(23个)两个目录
- 审计结果: L6 avg_score=100.0, A=2097 ✅

### Task 4 (P0): 修复tools/tags回归 - 完成 ✅
- 842个文件的tools字段格式修复("- - read" → "- read")
- 审计脚本frontmatter解析器增强: 支持非缩进列表项("- item")
- 审计结果: MISSING_TOOLS=0, MISSING_TAGS=0 ✅

### Task 5 (P1): L7a审计启用状态修复 - 完成 ✅
- 修改 deep_quality_audit.py: L7a从opt-in改为opt-out(默认启用, --no-layer7关闭)
- 审计结果: L7a enabled=true, avg_score=100.0 ✅

### Task 6 (P1): L8安全审计层实现 - 完成 ✅
- 实现8类安全检查: EXTERNAL_URL, INJECTED_MARKETING_TEXT, API_KEY_EXPOSURE, SLUG_CONTENT_MISMATCH, DUPLICATE_YAML_FIELDS, TAG_MISMATCH, GARBLED_TEXT, DEPENDENCY_CONTRADICTION
- URL白名单添加 skillhub.ai
- 任务定义pattern添加"任务定义"
- 审计结果: L8 avg_score=100.0, A=2097, pass_rate=100% ✅

### Task 7 (P1): 数据库platform_uploads同步 - 完成 ✅
- ClawHub: 159→530条记录(+371)
- SkillHub: 29→1126条记录(+1097)
- 总计新增1468条记录

### Task 8 (P2): ClawHub上传 - 部分完成 ⚠️
- 本轮上传82个成功(855 vs 773), 限流窗口200/24h
- 剩余502个待上传, 限流重置约2026-07-24T21:01 UTC
- 22个VERSION_EXISTS已通过版本递增修复

### Task 9 (P2): SkillHub重新提交 - 阻塞 ⚠️
- skillhub CLI v0.4.1 不支持publish命令
- 需要通过Trae Work对话命令或Web界面提交
- 认证token已过期, 需要用户重新登录
- 12个pending_review skills待重新提交

## 交叉验证发现的遗留问题

### 1. ClawHub 502个待上传
- 限流: 200/24h, 下次重置约2026-07-24T21:01 UTC (北京时间约2026-07-25 05:01)
- 上传脚本: `python clawhub_batch_uploader.py --resume --limit 200`
- 需要至少3轮(502/200≈3)才能完成全部上传

### 2. SkillHub 12个pending_review需重新提交
- CLI不支持publish, 需Trae Work或Web界面
- 12个skill: version-control-workflows, data-analysis-toolkit, trading-strategy-guide, xml-parser-tool, baoyu-md-formatter, file-browser-tool, markdown-converter-tool, podcast-downloader-tool, rho-telegram-alerts-tool, text-rpg-arcade-v3, video-upload-stream-tool, pdf-compressor-tool
- 需要用户重新登录获取新token

### 3. L5可销售性: 27个B级skill
- L5 avg_score=89.9, A=2070, B=27
- B级skill可通过增加内容深度、使用指南等提升至A级
- 不影响销售(L5 A+B=100%), 但可优化

### 4. L7b可执行性审计未在主审计中运行
- L7b需要 --layer7b 标志显式启用
- 上次单独运行结果: A=2097/2097 (100%)
- 可考虑将L7b也改为默认启用

### 5. L6/L7a各有2个skill有轻微问题(低于INFO阈值)
- 不影响severity级别(info=0, ok=2097)
- 可进一步优化至0问题

## Round 38 任务清单

### Task 1 (P0): ClawHub剩余502个skill上传
**目标**: 完成ClawHub全量上传

1. 检查ClawHub限流是否已重置(距上次上传>24h)
2. 运行 `python clawhub_batch_uploader.py --resume --limit 200` 上传200个
3. 如仍有剩余,等待24h后继续上传
4. 上传完成后同步clawhub_published_slugs.json和数据库platform_uploads表
5. 验证ClawHub published count = 855 + 502 = 1357

**验证标准**:
- ClawHub published count >= 1357
- 0个VERSION_EXISTS失败
- platform_uploads表clawhub记录数 >= 1357

### Task 2 (P0): SkillHub 12个pending_review重新提交
**目标**: 将修复后的12个skill重新提交到SkillHub

1. 检查skillhub CLI是否有新版本支持publish命令
2. 如CLI不支持,通过Trae Work对话命令提交
3. 对每个skill执行publish操作
4. 检查提交后状态是否从pending变为reviewing
5. 如果仍被拒绝,分析新的失败原因并修复

**验证标准**:
- 12个skill已重新提交
- 提交结果已记录
- pending_review数量从12降至0(或记录新原因)

### Task 3 (P1): L5可销售性优化(27个B级→A级)
**目标**: 将27个B级skill提升至A级

1. 从审计报告获取27个B级skill列表
2. 分析每个B级skill的扣分原因
3. 针对性补充: 使用指南、代码示例、错误处理详情、依赖说明等
4. 重新运行审计验证L5 avg_score提升

**验证标准**:
- L5 A级从2070提升至2090+
- L5 B级从27降至5以下
- L5 avg_score从89.9提升至92+

### Task 4 (P1): L7b默认启用
**目标**: 将L7b改为默认启用,与L7a一致

1. 修改 deep_quality_audit.py: L7b从opt-in改为opt-out(默认启用, --no-layer7b关闭)
2. 运行完整审计(不带--layer7b参数)验证L7b正确运行
3. 验证L7b结果与上次单独运行一致

**验证标准**:
- L7b enabled = true (不带--layer7b参数时)
- L7b avg_score = 100.0
- L7b A=2097, B=0

### Task 5 (P2): L6/L7a剩余2个轻微问题修复
**目标**: 消除L6和L7a中最后的2个轻微问题

1. 从审计报告获取2个有问题的skill详情
2. 针对性修复(可能是section格式或内容细节)
3. 重新运行审计验证0问题

**验证标准**:
- L6 total_with_issues = 0
- L7a total_with_issues = 0

### Task 6 (P2): 审计脚本L7b默认启用后的性能评估
**目标**: 确保L7b默认启用后审计性能可接受

1. 测量L7b启用后的审计总耗时
2. 如耗时过长(>10分钟),优化L7b检查逻辑
3. 考虑并行化或缓存机制

**验证标准**:
- 审计总耗时 < 10分钟
- L7b检查不影响其他层级审计

## 执行规则
1. 遵循`修复提示词.md`的R1-R78规则
2. 每个任务完成后进行代码级验证(非文档声明)
3. 禁止任何形式的mock/fallback/todo/pass
4. 修复必须覆盖全部3个目录(packaged-skills/skillhub, opensource-skills/packaged, differentiated-skills)
5. 完成后生成下一轮提示词v39.0

## 平台统计速览
| 平台 | 已发布 | 待审核/待上传 | 总计 |
|------|--------|---------------|------|
| SkillHub | 2068 | 12 pending | 2080 |
| ClawHub | 855 | 502 pending | 1357 |
| Hermes | 1067 | 0 | 1067 |

## 审计质量速览
| 层级 | 状态 | A级 | B级 | C+D+F级 | avg_score |
|------|------|-----|-----|---------|-----------|
| L4 功能质量 | ✅ | 2097 | 0 | 0 | 93.4 |
| L5 可销售性 | ✅ | 2070 | 27 | 0 | 89.9 |
| L6 内容真实性 | ✅ | 2097 | 0 | 0 | 100.0 |
| L7a 语义模板 | ✅ | 2097 | 0 | 0 | 100.0 |
| L7b 可执行性 | ⚠️ 未启用 | - | - | - | - |
| L8 安全审计 | ✅ | 2097 | 0 | 0 | 100.0 |
| Critical | ✅ | 0 critical, 0 warning, 0 info, 2097 OK | | | |

## 定价分布速览
| 定价层级 | 数量 | 占比 | 目标 |
|----------|------|------|------|
| L1-入门级 | 443 | 23.1% | - |
| L2-标准级 | 686 | 35.8% | - |
| L3-专业级 | 527 | 27.5% | <40% ✅ |
| L4-企业级 | 261 | 13.6% | - |
| L1+L2合计 | 1129 | 58.9% | >30% ✅ |
| NULL/free | 0 | 0% | 0 ✅ |

## Git提交记录
| 轮次 | Commit | 文件数 | 变更行数 |
|------|--------|--------|----------|
| Round 36 | 58542b46 | 63 | +1705/-24084 |
| Round 36 | d8e61e8d | 1 | +192 |
| Round 37 | 081cf7f0 | 2105 | +60051/-89044 |
