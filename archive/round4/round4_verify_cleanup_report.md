# Round 4 - 验证综合治理清理结果报告

> 生成时间: 2026-07-20T09:42:32.433880
> 数据库: `d:\skills\skill-registry.db`
> 验证目标: comprehensive_cleanup.py 执行后是否引入新问题

---

## 一、Task 1 - 验证 license 字段修改

- DB 中 source_license=Proprietary 的记录数: **300**
- 按 source 分布:

| source | 数量 |
|--------|------|
| clawhub | 298 |
| clawhub_differentiated | 2 |

- 抽样数: **10**
- DB与FM一致: **0/10**
- FM为Proprietary: **0/10**
- FM残留开源许可证: **10/10**

### 抽样明细

| slug | source | DB_license | FM_license | DB与FM一致 |
|------|--------|------------|------------|-----------|
| office-task-automator | clawhub | `Proprietary` | `MIT` | 否 |
| mongo-manager-free | clawhub | `Proprietary` | `MIT` | 否 |
| slack-api-toolkit | clawhub | `Proprietary` | `MIT` | 否 |
| canvas-json-handler-free | clawhub | `Proprietary` | `MIT` | 否 |
| knowledge-graph-builder | clawhub | `Proprietary` | `MIT` | 否 |
| jira-flow-skill | clawhub | `Proprietary` | `MIT` | 否 |
| data-analyst-chinese-free | clawhub | `Proprietary` | `MIT` | 否 |
| pg-mcp-skills-free | clawhub | `Proprietary` | `MIT` | 否 |
| whatsapp-master | clawhub | `Proprietary` | `MIT` | 否 |
| graph-query | clawhub | `Proprietary` | `MIT` | 否 |

> **[新发现问题]** comprehensive_cleanup.py 的 `fix_license_fields()` 函数只更新了 DB 的 `source_license` 字段, **未同步更新 SKILL.md frontmatter 的 `license:` 字段**。
> 抽样中 10/10 条的 frontmatter 仍为 MIT/Apache, 与 DB 的 Proprietary 不一致。
> 这是一个**不完整修复** - DB 层面已合规, 但文件层面 (SKILL.md) 仍残留开源许可证。

---

## 二、Task 2 - 验证 tools 字段格式修改

- 全量 tools 格式分布 (PyYAML 解析):

| 格式 | 数量 | 说明 |
|------|------|------|
| `block_array` | 1862 | YAML 块数组 flat list (规范) |
| `block_array_LOT_ERROR` | 43 | YAML 块数组但为 list-of-lists (清理引入的bug!) |
| `string_ERROR` | 2 | 字符串格式 (错误) |
| `file_missing` | 1 | 文件缺失 |
| `missing` | 1 | 缺失 |

- 全量错误格式记录 (含ERROR): **45**
- 其中 list-of-lists bug (LOT_ERROR): **43** 条 (全量)
- 已知被修改记录全量检查: **30** 条
  - 其中 list-of-lists bug: **29** 条
  - 其中格式正确 (flat list): **0** 条

### 已知被修改记录明细 (前15条)

| slug | 格式 | PyYAML解析值 | flat list | LOT bug |
|------|------|-------------|-----------|---------|
| alibaba-quark-scan | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| api-integration | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| auto-workflow | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| automation-workflow-builder | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| azure-ai-transcription-py | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| baoyu-format-markdown | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| book-painter | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| calendar-reminder | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| dlazy-audio-generate | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| dlazy-generate | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| flexible-database-design | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| github-api | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| hugo-blog-publisher | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| humanizer | `block_array_LOT_ERROR` | `[['read', 'exec']]` | 否 | 是 |
| key-guard | `string_ERROR` | `N/A` | 否 | 否 |

> **[新发现问题]** tools 字段修复引入 **list-of-lists bug**!
> comprehensive_cleanup.py 的 `fix_tools_field()` 对 quoted string 格式 `'[read, exec]'` 未先剥离引号再解析数组,
> 导致整个 `[read, exec]` 被作为单个 list item, 产生 `[['read', 'exec']]` 而非 `['read', 'exec']`。
> 全量受影响记录: **43** 条; 已知被修改记录中受影响: **29** 条。

---

## 三、Task 3 - 验证 displayName 字段修改

- DB displayName 长度分布:

| 类别 | 数量 |
|------|------|
| ok(<=20) | 1909 |

- 超长 (>20) 残留: **0** 条 (Round 3 为 154 条)
- 抽样数: **5**
- DB与FM一致率: **4/5**

### 抽样明细

| slug | DB displayName | DB长度 | FM displayName | FM长度 | 一致 |
|------|----------------|--------|---------------|--------|------|
| cashu-emoji | `Cashu Emoji` | 11 | `Cashu Emoji` | 11 | 是 |
| cdp-browser-pilot-free | `Cdp Browser Pilot免费版` | 20 | `CDP浏览器领航(免费版)` | 13 | 否 |
| video-frames | `Video Frames` | 12 | `Video Frames` | 12 | 是 |
| monad-development | `Monad Development` | 17 | `Monad Development` | 17 | 是 |
| compress-pdf | `Compress PDF` | 12 | `Compress PDF` | 12 | 是 |

> **[新发现问题]** DB与FM不一致, 可能是 frontmatter 未同步更新。

---

## 四、Task 4 - 检查 SKILL.md YAML 语法错误

- 总记录数: **1909**
- 文件缺失: 1
- 无 frontmatter: 0
- YAML 解析成功: **1906**
- YAML 解析失败: **2** (Round 3 为 3 条)

### YAML 解析错误明细 (2 条)

| slug | source | edition | error |
|------|--------|---------|-------|
| text-to-speech-heygen | clawhub_download | free | `mapping values are not allowed here   in "<unicode string>", line 6, column 7:       when: (1) Generating stand...'           ^` |
| key-guard | clawhub_download | free | `while parsing a block mapping   in "<unicode string>", line 1, column 1:     slug: key-guard     ^ expected <block end>, but found '<scalar>'   in "<u` |

> **[新发现问题]** 2 条 SKILL.md 存在 YAML 语法错误。

---

## 五、Task 5 - 验证 source 字段修改后的差异化内容

- source=clawhub_download 且 path 在 differentiated-skills 的残留: **0** (Round 3 为 71 条)
- 被修改的 paid orphan 记录数: **500**
- 目录存在: **499/500**
- SKILL.md存在: **499/500**
- 含中文内容: **499/500**
- 含结构化章节: **499/500**
- 差异化信号通过: **499/500**
- DB license=Proprietary: **1/500**

> **[通过]** 71 条 source 误标已全部修复为 clawhub_differentiated, 无残留。
> **[注意]** 1 条记录的差异化信号不足。

---

## 六、Task 6 - 调查孤儿记录标记返回 0 的原因

- 原始 mark_orphan_records 查询返回: **0** 条

### 查询条件逐步分解

| 步骤 | 条件 | 数量 |
|------|------|------|
| A | edition=paid | 649 |
| B | + parent_slug IS NULL | 649 |
| C | + source_slug IS NOT NULL | 649 |
| D | + EXISTS(同source_slug有其他paid且parent_slug非NULL) | 0 <-- 关键断点 |

- round-1 孤立 paid 候选 (edition=paid, parent_slug=NULL, path在differentiated-skills): **649** 条
  - 其中 source_slug IS NULL: **0** 条
  - 其中 source_slug IS NOT NULL: **649** 条
  - 有同source_slug且parent_slug非NULL的paid兄弟: **0**

- 已 deprecated 记录数: **1**
  - 按 edition: {'paid': 1}
  - 按 parent_slug: {'NULL': 1}
  - 按 source: {'clawhub_differentiated': 1}
  - 有 orphan_governance 操作记录: **0** 条

### 根本原因

- 原因B: 649 条有 source_slug 的记录中, 没有找到同 source_slug 且 parent_slug IS NOT NULL 的 round-2 paid 兄弟记录 (EXISTS 子查询失败)
- 原因C: 1 条记录已被标记为 deprecated (可能被早期治理处理, 但查询不检查 workflow_state 所以不应影响)

> **结论**: mark_orphan_records 返回 0 的原因是 EXISTS 子查询条件过于严格 - 要求同 source_slug 存在另一条 parent_slug IS NOT NULL 的 paid 记录。
> 但实际上 round-1 孤立 paid 记录的 round-2 继任者要么不存在, 要么也没有设置 parent_slug, 导致 EXISTS 子查询无法匹配。
> 这些记录可能已在更早期的治理中被标记为 deprecated (通过其他路径), 或从未建立 parent_slug 关联。

---

## 七、综合结论

### 验证结果汇总

| 验证项 | 状态 | 严重度 | 说明 |
|--------|------|--------|------|
| Task 1 (license) | 不完整修复 | 中 | DB source_license 已改为 Proprietary (300 条), 但 frontmatter license 字段未同步更新。抽样中 10/10 条 SKILL.md 仍为 MIT/Apache。comprehensiv |
| Task 2 (tools) | 新发现问题 | 高 | tools 修复引入 list-of-lists bug: 全量 43 条, 已知修改记录中 29/30 条受影响。原因: fix_tools_field() 未先剥离引号再解析数组。 |
| Task 3 (displayName) | 新发现问题 | 中 | DB与FM不一致, frontmatter displayName 未同步更新。 |
| Task 4 (YAML错误) | 新发现问题 | 高 | 2 条 SKILL.md 存在 YAML 语法错误 (可能由清理脚本引入)。 |
| Task 5 (source修复) | 部分通过 | 低 | source 误标已修复, 但 1 条差异化信号不足。 |
| Task 6 (孤儿记录) | 查询逻辑缺陷 | 中 | mark_orphan_records 返回 0, 原因: EXISTS 子查询要求同 source_slug 有 parent_slug IS NOT NULL 的 paid 兄弟, 但实际不存在。1 条记录已通过其他路径标记为 depr |

### 新引入/遗留问题总结

- **[中严重] Task 1 (license)**: DB source_license 已改为 Proprietary (300 条), 但 frontmatter license 字段未同步更新。抽样中 10/10 条 SKILL.md 仍为 MIT/Apache。comprehensive_cleanup.py 的 fix_license_fields() 只更新了 DB, 未写 SKILL.md 文件。
- **[高严重] Task 2 (tools)**: tools 修复引入 list-of-lists bug: 全量 43 条, 已知修改记录中 29/30 条受影响。原因: fix_tools_field() 未先剥离引号再解析数组。
- **[中严重] Task 3 (displayName)**: DB与FM不一致, frontmatter displayName 未同步更新。
- **[高严重] Task 4 (YAML错误)**: 2 条 SKILL.md 存在 YAML 语法错误 (可能由清理脚本引入)。
- **[中严重] Task 6 (孤儿记录)**: mark_orphan_records 返回 0, 原因: EXISTS 子查询要求同 source_slug 有 parent_slug IS NOT NULL 的 paid 兄弟, 但实际不存在。1 条记录已通过其他路径标记为 deprecated。

### 建议修复措施

1. **补充修复 license frontmatter**: 对 300 条 source_license=Proprietary 的记录, 同步更新 SKILL.md frontmatter 的 `license:` 字段为 `Proprietary`。可复用 fix_displayname_anomalies 的文件写入模式。
2. **修复 tools list-of-lists bug**: 对 43 条受影响记录, 将 `tools:\n  - [read, exec]` 修正为 `tools:\n  - read\n  - exec`。根因: fix_tools_field() 应先剥离外层引号, 再判断是否为 `[...]` 数组格式。
3. **修复 YAML 语法错误**: 2 条 SKILL.md 存在 YAML 解析错误, 需逐一修复 (特别是 text-to-speech-heygen 的 summary 字段中的撇号未转义)。
4. **修复孤儿记录查询**: 放宽 EXISTS 子查询条件, 不要求 `s2.parent_slug IS NOT NULL`, 或改为检查 workflow_state 是否已为 deprecated。同时检查 0 条 source_slug=NULL 的记录是否需要补充 source_slug。
