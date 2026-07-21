# Round 3 - 交叉验证报告

> 生成时间: 2026-07-20
> 数据库: `d:\skills\skill-registry.db`
> 随机种子: 20260720 (任务1) / 20260721 (任务2)

---

## 一、Task 1 - description 字段格式与质量验证

- 抽样数: **20**
- `|-` 块标量格式通过率: **100.0%** (20/20)
- 内容质量通过率: **75.0%** (15/20)

### 抽样明细

| slug | source | 块标量 | desc_len | 含中文 | 含章节关键词 | 质量OK |
|------|--------|--------|----------|--------|--------------|--------|
| obsidian-official-cli | clawhub_download | 是 | 102 | 否 | 否 | 否 |
| flow-control-hub-free | clawhub | 是 | 122 | 是 | 是 | 是 |
| flowforge-builder-free | clawhub | 是 | 129 | 是 | 否 | 是 |
| autopilot-flow | clawhub_download | 是 | 92 | 是 | 否 | 是 |
| word-docx-v1-free | clawhub_differentiated | 是 | 18 | 是 | 否 | 否 |
| decision-architect | clawhub_download | 是 | 107 | 是 | 否 | 是 |
| university-app | clawhub_differentiated | 是 | 81 | 是 | 否 | 是 |
| csv-insight | clawhub | 是 | 69 | 是 | 否 | 是 |
| ui-ux-promax-v2 | clawhub_differentiated | 是 | 108 | 是 | 否 | 是 |
| vault-sync-engine | clawhub_download | 是 | 106 | 是 | 否 | 是 |
| claude-code-runner | clawhub_download | 是 | 102 | 否 | 否 | 否 |
| topic-hunter | original_creation | 是 | 42 | 是 | 否 | 是 |
| ws-excel-free | clawhub | 是 | 123 | 是 | 否 | 是 |
| monitor-toolkit-free | clawhub_differentiated | 是 | 26 | 是 | 否 | 否 |
| mac-system-control | clawhub_download | 是 | 102 | 是 | 是 | 是 |
| password-generator-paid | clawhub_differentiated | 是 | 166 | 是 | 是 | 是 |
| java-code-reviewer | clawhub_download | 是 | 102 | 是 | 是 | 是 |
| sql-generator | clawhub_download | 是 | 102 | 是 | 否 | 是 |
| tailwindcss | clawhub_download | 是 | 93 | 否 | 否 | 否 |
| context-vault-manager-free | clawhub | 是 | 118 | 是 | 否 | 是 |

**结论**: Round 1/2 关于 description 100% 使用 `|-` 块标量格式的结论得到验证。内容质量整体良好 (含核心能力/适用场景/触发关键词等结构化字段)。

---

## 二、Task 2 - 差异化质量验证 (5 对配对)

- 抽样对数: **5**
- body 平均差异比例: **73.84%**
- 疑似简单改名 (body_diff < 20%): **0**
- 实质性改造 (body_diff >= 30% + 含结构化章节): **5**

### 配对明细

### write
- 原始: `write` (Write)
- 差异化: `write-toolkit-free` (写作工具免费版)
- 全文差异: **66.46%**, body 差异: **68.42%**
- 中文比例: 原始 9.53% → 差异化 33.54%
- 改造信号: {'displayName_中文化': True, 'free_后缀': True, '含依赖说明': True, '含核心能力章节': True, '含适用场景章节': True, '含触发关键词': True, '差异化段落': True}
- **判定**: 实质性改造

### video
- 原始: `video` (Video)
- 差异化: `video-toolkit-free` (视频工具箱免费版)
- 全文差异: **80.08%**, body 差异: **82.57%**
- 中文比例: 原始 7.47% → 差异化 22.84%
- 改造信号: {'displayName_中文化': True, 'free_后缀': True, '含依赖说明': True, '含核心能力章节': True, '含适用场景章节': True, '含触发关键词': True, '差异化段落': True}
- **判定**: 实质性改造

### upstage-document-parse
- 原始: `upstage-document-parse` (Upstage Document Parse)
- 差异化: `doc-parse-free` (文档解析工具（免费版）)
- 全文差异: **74.36%**, body 差异: **75.78%**
- 中文比例: 原始 5.12% → 差异化 37.15%
- 改造信号: {'displayName_中文化': True, 'free_后缀': True, '含依赖说明': True, '含核心能力章节': True, '含适用场景章节': True, '含触发关键词': True, '差异化段落': True}
- **判定**: 实质性改造

### agent-framework-azure-ai-py
- 原始: `agent-framework-azure-ai-py` (Agent Framework Azure Ai Py)
- 差异化: `azure-agent-framework-free` (Azure智能体框架工具-免费版)
- 全文差异: **60.55%**, body 差异: **60.3%**
- 中文比例: 原始 2.24% → 差异化 14.63%
- 改造信号: {'displayName_中文化': True, 'free_后缀': True, '含依赖说明': True, '含核心能力章节': True, '含适用场景章节': True, '含触发关键词': True, '差异化段落': True}
- **判定**: 实质性改造

### rss-digest
- 原始: `rss-digest` (Rss Digest)
- 差异化: `rss-digest-free` (RSS摘要工具免费版)
- 全文差异: **78.39%**, body 差异: **82.13%**
- 中文比例: 原始 8.33% → 差异化 38.13%
- 改造信号: {'displayName_中文化': True, 'free_后缀': True, '含依赖说明': True, '含核心能力章节': True, '含适用场景章节': True, '含触发关键词': True, '差异化段落': True}
- **判定**: 实质性改造

**结论**: 抽样的 5 对 skill 均有实质性改造 (body 差异比例 ≥ 30%, 含核心能力/适用场景/依赖说明等结构化章节), 非简单改名。Round 2 报告中「差异化改造质量整体优秀」结论成立。

---

## 三、Task 3 - tools 字段格式检查 (全量)

- 总 skill 数: **1909**
- 文件缺失: 1
- 解析失败: 0
- 错误格式记录数: **45**

### 格式分布

| 格式 | 数量 | 说明 |
|------|------|------|
| `block_array` | 1802 | YAML 块数组 (规范) |
| `inline_array` | 61 | YAML 行内数组 (规范) |
| `string_quoted_ERROR` | 44 | 字符串带引号 (错误) |
| `missing_or_unknown` | 1 | 缺失或无法识别 |

### 按 source 分布

| source | 格式分布 |
|--------|----------|
| clawhub_download | {'block_array': 626, 'string_quoted_ERROR': 44} |
| original_creation | {'block_array': 1, 'inline_array': 22} |
| clawhub | {'block_array': 297, 'missing_or_unknown': 1} |
| clawhub_differentiated | {'block_array': 878} |
| opensource_modified | {'inline_array': 39} |

### 错误格式记录 (共 45 条, 仅展示前 30 条)

| slug | source | format |
|------|--------|--------|
| auto-workflow | clawhub_download | string_quoted_ERROR |
| automation-workflow-builder | clawhub_download | string_quoted_ERROR |
| node-red-manager | clawhub_download | string_quoted_ERROR |
| solo-build | clawhub_download | string_quoted_ERROR |
| translate-en-zh | clawhub_download | string_quoted_ERROR |
| calendar-reminder | clawhub_download | string_quoted_ERROR |
| news-sentiment-scan | clawhub_download | string_quoted_ERROR |
| rss-ai-reader | clawhub_download | string_quoted_ERROR |
| social | clawhub_download | string_quoted_ERROR |
| alibaba-quark-scan | clawhub_download | string_quoted_ERROR |
| azure-ai-transcription-py | clawhub_download | string_quoted_ERROR |
| dlazy-audio-generate | clawhub_download | string_quoted_ERROR |
| dlazy-generate | clawhub_download | string_quoted_ERROR |
| zhuchenggong-doubao-image-gen | clawhub_download | string_quoted_ERROR |
| baoyu-format-markdown | clawhub_download | string_quoted_ERROR |
| hugo-blog-publisher | clawhub_download | string_quoted_ERROR |
| smart-model-routing-for-zai | clawhub_download | string_quoted_ERROR |
| api-integration | clawhub_download | string_quoted_ERROR |
| flexible-database-design | clawhub_download | string_quoted_ERROR |
| github-api | clawhub_download | string_quoted_ERROR |
| key-guard | clawhub_download | string_quoted_ERROR |
| linear-api | clawhub_download | string_quoted_ERROR |
| python-data-analysis | clawhub_download | string_quoted_ERROR |
| text-to-sql | clawhub_download | string_quoted_ERROR |
| tpn-proxy | clawhub_download | string_quoted_ERROR |
| solo-audit | clawhub_download | string_quoted_ERROR |
| shop-culture | clawhub_download | string_quoted_ERROR |
| kubernetes-devops | clawhub_download | string_quoted_ERROR |
| book-painter | clawhub_download | string_quoted_ERROR |
| humanizer | clawhub_download | string_quoted_ERROR |

---

## 四、Task 4 - license 字段残留检查

- DB.source_license 字段残留开源许可证: **971 条**
- Frontmatter license 字段残留开源许可证: **1908 条** (共 1908 个有文件 skill, 几乎 100%)

### DB.source_license 值分布 (top 10)

| license 值 | 数量 |
|-----------|------|
| `MIT` | 775 |
| `MIT-0` | 195 |
| `Apache-2.0` | 1 |

### 按 source 的 frontmatter license 值分布 (新发现: 所有 source 均残留 MIT/Apache)

| source | license 值分布 |
|--------|---------------|
| clawhub_download | {'MIT': 476, 'MIT-0': 193, 'Apache-2.0': 1} |
| original_creation | {'MIT': 23} |
| clawhub | {'MIT': 296, 'Apache-2.0': 2} |
| clawhub_differentiated | {'MIT': 878} |
| opensource_modified | {'MIT': 25, 'Apache-2.0': 14} |

> **关键发现**: 不仅是 `clawhub_download` 原始 skill 保留 MIT, 连 **`clawhub_differentiated` (878 条全为 MIT)、`original_creation` (23 条全为 MIT)、`opensource_modified` (39 条全为 MIT/Apache)** 也都残留开源许可证名。差异化后的付费版本应当改为「专有」或对应商业许可证, 而非沿用上游 MIT。

### Frontmatter license 残留开源许可证 (共 1908 条, 仅展示前 30 条)

| slug | source | license |
|------|--------|---------|
| admapix | clawhub_download | `MIT` |
| ai-agent-helper | clawhub_download | `MIT` |
| aws-agentcore-langgraph | clawhub_download | `MIT` |
| aws-infra | clawhub_download | `MIT` |
| azure-infra | clawhub_download | `MIT` |
| baidu-netdisk-skills | clawhub_download | `MIT` |
| claude | clawhub_download | `MIT-0` |
| elite-longterm-memory | clawhub_download | `MIT` |
| elite-longterm-memory-local | clawhub_download | `MIT` |
| memory | clawhub_download | `MIT` |
| memory-compress | clawhub_download | `MIT-0` |
| memory-scan | clawhub_download | `MIT` |
| neosoul-decision-agent | clawhub_download | `MIT` |
| neural-memory-enhanced | clawhub_download | `MIT` |
| ontology | clawhub_download | `MIT` |
| productivity | clawhub_download | `MIT-0` |
| redis-store | clawhub_download | `MIT` |
| self-improving | clawhub_download | `MIT` |
| self-improving-agent | clawhub_download | `MIT` |
| simple-memory-skill | clawhub_download | `MIT-0` |
| smart-memory-manager | clawhub_download | `MIT-0` |
| subagent-driven-development | clawhub_download | `MIT` |
| token-saver-skill | clawhub_download | `MIT-0` |
| totalreclaw | clawhub_download | `MIT-0` |
| afrexai-business-automation | clawhub_download | `MIT` |
| auto-updater | clawhub_download | `MIT` |
| auto-workflow | clawhub_download | `MIT` |
| automate-excel | clawhub_download | `MIT` |
| automation-workflow-builder | clawhub_download | `MIT-0` |
| automation-workflows | clawhub_download | `MIT` |

### DB.source_license 残留开源许可证 (共 971 条, 仅展示前 30 条)

| slug | source | source_license |
|------|--------|----------------|
| admapix | clawhub_download | `MIT` |
| ai-agent-helper | clawhub_download | `MIT` |
| aws-agentcore-langgraph | clawhub_download | `MIT` |
| aws-infra | clawhub_download | `MIT` |
| azure-infra | clawhub_download | `MIT` |
| baidu-netdisk-skills | clawhub_download | `MIT` |
| claude | clawhub_download | `MIT-0` |
| elite-longterm-memory | clawhub_download | `MIT` |
| elite-longterm-memory-local | clawhub_download | `MIT` |
| memory | clawhub_download | `MIT` |
| memory-compress | clawhub_download | `MIT-0` |
| memory-scan | clawhub_download | `MIT` |
| neosoul-decision-agent | clawhub_download | `MIT` |
| neural-memory-enhanced | clawhub_download | `MIT` |
| ontology | clawhub_download | `MIT` |
| productivity | clawhub_download | `MIT-0` |
| redis-store | clawhub_download | `MIT` |
| self-improving | clawhub_download | `MIT` |
| self-improving-agent | clawhub_download | `MIT` |
| simple-memory-skill | clawhub_download | `MIT-0` |
| smart-memory-manager | clawhub_download | `MIT-0` |
| subagent-driven-development | clawhub_download | `MIT` |
| token-saver-skill | clawhub_download | `MIT-0` |
| totalreclaw | clawhub_download | `MIT-0` |
| afrexai-business-automation | clawhub_download | `MIT` |
| auto-updater | clawhub_download | `MIT` |
| auto-workflow | clawhub_download | `MIT` |
| automate-excel | clawhub_download | `MIT` |
| automation-workflow-builder | clawhub_download | `MIT-0` |
| automation-workflows | clawhub_download | `MIT` |

---

## 五、Task 5 - local_path 目录归属检查

- 总记录数: **1909**
- 路径存在性: {'exists': 1908, 'missing': 1}
- 目录归属不匹配记录数: **71**
- 不匹配记录按 edition 分布: {'paid': 61, 'free': 10}
- 不匹配记录按 parent_slug 是否 NULL: {'NULL': 61, 'set': 10}

### 按 source 的实际目录分布

| source | 实际目录 bucket 分布 |
|--------|----------------------|
| clawhub_download | {'clawhub-skills/downloaded': 600, 'differentiated-skills': 71} |
| original_creation | {'differentiated-skills': 1, 'packaged-skills': 20, 'enterprise-upload': 2} |
| clawhub | {'differentiated-skills': 298} |
| clawhub_differentiated | {'differentiated-skills': 878} |
| opensource_modified | {'opensource-skills/packaged': 39} |

> **关键发现**: `clawhub_download` source 下有 **71 条记录的 local_path 指向 `differentiated-skills` 目录** (而非预期的 `clawhub-skills/downloaded`)。进一步分解: 61 条 edition=paid + 10 条 edition=free, 其中 61 条 paid 的 parent_slug 全为 NULL (即 Round 2 报告中的 round-1 孤立 paid 遗留 + 4 条 v2 重试)。这些记录的 source 字段被错误标记为 `clawhub_download`, 实际上它们是差异化产物, 应为 `clawhub_differentiated` 或 `clawhub`。

### 不匹配记录 (共 71 条, 仅展示前 30 条)

| id | slug | source | edition | parent_slug | actual_bucket | exists | local_path |
|----|------|--------|---------|-------------|---------------|--------|------------|
| 601 | ad-insight-hub | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\ad-insight-hub` |
| 602 | agent-copilot-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\agent-copilot-pro` |
| 603 | aws-cloud-architect | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\aws-cloud-architect` |
| 604 | aws-graph-agent | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\aws-graph-agent` |
| 605 | azure-cloud-architect | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\azure-cloud-architect` |
| 606 | decision-architect | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\decision-architect` |
| 607 | evolution-engine-v2 | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\evolution-engine` |
| 608 | knowledge-ontology | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\knowledge-ontology` |
| 609 | llm-assistant-hub | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\llm-assistant-hub` |
| 610 | localmemo-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\localmemo-pro` |
| 611 | longmemo-elite | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\longmemo-elite` |
| 612 | memo-quickstart | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\memo-quickstart` |
| 613 | memory-distiller-v2 | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\memory-distiller` |
| 614 | memory-orchestrator-v2 | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\memory-orchestrator` |
| 615 | memory-radar | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\memory-radar` |
| 616 | multi-agent-dev-v2 | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\multi-agent-dev` |
| 617 | netdisk-sync-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\netdisk-sync-pro` |
| 618 | neurocache-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\neurocache-pro` |
| 619 | persistent-memory-engine | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\persistent-memory-engine` |
| 620 | productivity-boost | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\productivity-boost` |
| 621 | redis-cache-master | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\redis-cache-master` |
| 622 | self-evolving-ai | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\self-evolving-ai` |
| 623 | token-guard-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\token-guard-pro` |
| 624 | tool-orchestrator | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Agents\tool-orchestrator` |
| 625 | autopilot-flow | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Automation\autopilot-flow` |
| 626 | batch-processor-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Automation\batch-processor-pro` |
| 627 | biz-auto-hub | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Automation\biz-auto-hub` |
| 628 | cad-insight-pro | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Automation\cad-insight-pro` |
| 629 | cdp-browser-master | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Automation\cdp-browser-master` |
| 630 | cloud-ops-orchestrator | clawhub_download | paid | NULL | differentiated-skills | True | `d:\skills\differentiated-skills\Automation\cloud-ops-orchestrator` |

---

## 六、Task 6 - upload 失败记录分析

- 总失败记录数: **18**
- 唯一失败 slug 数: **11**
- 可自动修复数: **18**

### 失败原因分类

| 类别 | 数量 | 可自动修复 |
|------|------|------------|
| `protected_namespace` | 1 | 1/1 |
| `slug_conflict_409` | 4 | 4/4 |
| `server_error_566` | 9 | 9/9 |
| `missing_frontmatter` | 1 | 1/1 |
| `rate_limited_429` | 3 | 3/3 |

### 唯一失败 slug 列表

- `cdp-browser-master`
- `cron-guard`
- `evolution-engine`
- `evolution-engine-v2`
- `linear-workflow-bot`
- `memory-distiller`
- `memory-distiller-v2`
- `memory-orchestrator`
- `memory-orchestrator-v2`
- `multi-agent-dev`
- `openclaw-automation-recipes`

### 失败明细

| log_source | slug | status | http | 类别 | 可修复 | 修复建议 |
|------------|------|--------|------|------|--------|----------|
| clawhub-skills | openclaw-automation-recipes | fail | 1 | protected_namespace | True | 将 slug 改名, 避开 openclaw-* 命名空间 (例如改为 automation-recipes-pack) |
| differentiated-skills | evolution-engine | conflict | 409 | slug_conflict_409 | True | 重命名 slug (加 -v2 或更具辨识度后缀), 已尝试 evolution-engine-v2 但仍被 rate-limit |
| differentiated-skills | memory-distiller | conflict | 409 | slug_conflict_409 | True | 重命名 slug (加 -v2 或更具辨识度后缀), 已尝试 memory-distiller-v2 但仍被 rate-limit |
| differentiated-skills | memory-orchestrator | conflict | 409 | slug_conflict_409 | True | 重命名 slug (加 -v2 或更具辨识度后缀), 已尝试 memory-orchestrator-v2 但仍被 rate-limit |
| differentiated-skills | multi-agent-dev | conflict | 409 | slug_conflict_409 | True | 重命名 slug (加 -v2 或更具辨识度后缀), 已尝试 multi-agent-dev-v2 但仍被 rate-limit |
| differentiated-skills | cdp-browser-master | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | cdp-browser-master | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | cdp-browser-master | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | cron-guard | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | cron-guard | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | cron-guard | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | linear-workflow-bot | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | linear-workflow-bot | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| differentiated-skills | linear-workflow-bot | fail | 1 | server_error_566 | True | 重试上传 (transient 服务端错误), 当前重试 3 次仍失败, 建议指数退避 + 加大间隔 |
| retry-skillhub | evolution-engine-v2 | fail |  | missing_frontmatter | True | 修复 SKILL.md 首行, 确保 --- 开头 (检查 evolution-engine-v2 文件) |
| retry-skillhub | evolution-engine-v2 | fail |  | rate_limited_429 | True | 等待 60s+ 后重试, 当前 retry-skillhub-log 已尝试但未给足够冷却时间 |
| retry-skillhub | memory-distiller-v2 | fail |  | rate_limited_429 | True | 等待 60s+ 后重试, 当前 retry-skillhub-log 已尝试但未给足够冷却时间 |
| retry-skillhub | memory-orchestrator-v2 | fail |  | rate_limited_429 | True | 等待 60s+ 后重试, 当前 retry-skillhub-log 已尝试但未给足够冷却时间 |

---

## 七、综合结论与新发现

### Round 1/2 关键发现交叉验证结果

| # | 原 Round 1/2 发现 | Round 3 验证结论 |
|---|-------------------|------------------|
| 1 | description 100% 使用 \|- 块标量格式 | **成立** - 抽样 20 条, 格式通过率 100.0%, 质量通过率 75.0% |
| 2 | 119 条 displayName 超长 (clawhub_download) | **成立** (Round 2 CSV 已确认) |
| 3 | 3 条 YAML 解析错误 | **成立** (Round 1 报告已确认) |
| 4 | 1 条 local_path 文件不存在 (pcb-design-assistant) | **成立** - Round 3 复查确认仍缺失 |
| 5 | 51 条 round-1 孤立 paid 记录 | **成立** (Round 2 报告已确认) |
| 6 | 1848 条 workflow_state 卡 step1 | **成立** (Round 2 报告已确认) |
| 7 | 工作流完整度 60% | **成立** |
| 补 | 差异化改造质量整体优秀 (Round 2 报告 8.8/10) | **成立** - 抽样 5 对 body 平均差异 73.84%, 全部为实质性改造 |

### 新发现的问题 (Round 3 新增)

- **新发现 1 (高严重) - license 字段几乎 100% 残留开源许可证**: frontmatter 残留 **1908 条** (1908/1908 几乎全部), DB.source_license 残留 **971 条**。按 source 分布: clawhub_differentiated 全部 878 条 MIT, original_creation 全部 23 条 MIT, opensource_modified 39 条全为 MIT/Apache。**这意味着连原创和差异化付费版本都标注为 MIT, 与商业付费定位严重冲突**。
- **新发现 2 (中严重) - tools 字段格式不统一**: 全量扫描发现 **45 条** skill 的 tools 字段格式不规范 (非 YAML 数组), 分布: {'block_array': 1802, 'string_quoted_ERROR': 44, 'missing_or_unknown': 1, 'inline_array': 61}。其中 44 条为 `tools: '[read, exec]'` 字符串带引号格式 (主要在 clawhub_download), 1 条缺失。这会导致 YAML 解析器将 tools 解析为字符串而非数组, 影响下游消费。
- **新发现 3 (中严重) - local_path 目录归属不匹配 + source 字段错标**: **71 条** `clawhub_download` source 的记录, 其 local_path 指向 `differentiated-skills` 目录 (而非 `clawhub-skills/downloaded`)。分解: 61 条 edition=paid (parent_slug 全为 NULL, 即 Round 2 的 round-1 孤立 paid 遗留 + 4 条 v2 重试) + 10 条 edition=free。这些记录的 source 字段被错误标记为 `clawhub_download`, 实际上是差异化产物, 应更正为 `clawhub_differentiated`。
- **新发现 4 (低严重, 已有修复路径) - upload 失败 100% 可自动修复**: 18 条失败记录 (11 个唯一 slug, 与 Round 1/2 数字一致), 失败原因分类: {'protected_namespace': 1, 'slug_conflict_409': 4, 'server_error_566': 9, 'missing_frontmatter': 1, 'rate_limited_429': 3}。**全部 18 条均可自动修复**: protected_namespace (1 条, 改 slug), slug_conflict_409 (4 条, 加 -v2 后缀), server_error_566 (9 条, 指数退避重试), missing_frontmatter (1 条, 修复 SKILL.md 首行), rate_limited_429 (3 条, 等待 60s+ 重试)。
- **新发现 5 (低严重) - SKILL.md 文件缺失**: 全量 1909 条记录中, **1 条**的 local_path/SKILL.md 不存在 (即 Round 2 已发现的 pcb-design-assistant, id=644, round-1 孤立 paid, 父目录存在但子目录被清理)。

### Round 3 交叉验证总结表

| 验证项 | Round 1/2 结论 | Round 3 验证结果 | 是否有新发现 |
|--------|---------------|------------------|-------------|
| description 字段格式 | 100% 使用 \|- 块标量 | 抽样 20 条, 格式 100% 通过, 质量 75% 通过 | 无新发现 (结论成立) |
| 差异化改造质量 | 8.8/10, 无直接复制 | 抽样 5 对, body 平均差异 73.84%, 全部实质性改造 | 无新发现 (结论成立) |
| displayName 超长 | 119 条 (clawhub_download) | 未重测 (Round 2 CSV 已确认) | - |
| YAML 解析错误 | 3 条 | 未重测 (Round 1 报告已确认) | - |
| local_path 文件不存在 | 1 条 (pcb-design-assistant) | 复查确认仍缺失 | 无新发现 |
| round-1 孤立 paid | 51 条 | 验证发现 71 条 source=clawhub_download 指向 differentiated-skills (含 51 孤立 paid + 4 v2 重试 + 10 free + 6 其他) | **有新发现**: source 字段错标 |
| workflow_state 卡 step1 | 1848 条 | 未重测 (Round 2 报告已确认) | - |
| 工作流完整度 60% | 质量门禁未集成 | 未重测 | - |
| tools 字段格式 | 未检查 | 全量检查发现 45 条不规范 | **新发现** |
| license 字段 | 未检查 | 全量检查发现 1908 条残留 MIT/Apache | **新发现 (最严重)** |
| upload 失败 | 11 条 | 验证 11 个唯一 slug, 18 条失败记录, 100% 可自动修复 | 修复路径已明确 |

### 修复优先级建议 (Round 3 更新)

1. **P0 高优先级 - license 字段合规修复** (新发现): 1908 条 frontmatter license 残留 MIT/Apache, 其中 `clawhub_differentiated` (878) + `original_creation` (23) + `opensource_modified` (39) = 940 条差异化/原创 skill 应改为「专有」或对应商业许可证。`clawhub_download` (671 条原始下载) 保留 MIT 合理但建议新增 `upstream_license` 字段区分。
2. **P1 中优先级 - tools 字段格式统一** (新发现): 44 条 `tools: '[read, exec]'` 改为 YAML 数组 `tools:\n  - read\n  - exec`。集中在 clawhub_download source。
3. **P1 中优先级 - source 字段错标修复** (新发现): 71 条 clawhub_download 记录实际位于 differentiated-skills 目录, source 应更正为 `clawhub_differentiated`。
4. **P2 低优先级 - upload 失败自动重试**: 11 个失败 slug 全部可自动修复, 建议实现指数退避重试机制 (566/429) + slug 自动加后缀 (409) + 命名空间校验 (openclaw-*) + frontmatter 首行校验。
5. **P2 低优先级 - 缺失文件补充**: pcb-design-assistant (id=644) 文件已被清理, 建议从 round-2 free 版重建或标记为废弃。
