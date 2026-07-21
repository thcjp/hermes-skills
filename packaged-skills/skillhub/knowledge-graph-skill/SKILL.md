---
slug: knowledge-graph-skill
name: knowledge-graph-skill
version: "1.2.0"
displayName: 知识图谱技能
summary: 嵌入式知识图谱,持久化存储结构化知识,支持查询、合并、可视化与配置
license: MIT
description: |-
  嵌入式知识图谱,以JSON存储持久化结构化知识,通过CLI脚本查询,生成KGML摘要供会话上下文使用。核心能力包括KGML格式知识表示、高级查询(子节点/类型/孤儿/统计/时间线)、实体合并(absorb/nest)、密钥保管库、深度启发式提取、可视化、配置管理、跨助手只读访问与记忆导入。
tools:
  - read
  - exec
---

# 知识图谱技能

个人知识图谱以JSON存储,通过CLI脚本查询,生成紧凑的KGML摘要供会话上下文使用。

## 首次安装

```bash
node scripts/install.mjs [--workspace /path/to/workspace] [--platform agent]
```

自动检测平台并修补助手指令文件,注入知识图谱指令和图摘要。操作幂等,可重复执行。

## KGML格式参考

```text
#KGML v2 | <count>e <count>r | depth:<N> | <date>
[category]
Label(Alias):type — attr1,attr2
  ChildLabel(CA):type — attrs    ← 缩进 = 父>子
%rels
A>verb>B C>verb>D                ← 跨分支关系(使用别名)
%vault key1,key2                 ← 保管库键名(不含值)
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD（纯Markdown指令，无需exec命令行能力）

## 核心能力

- **KGML格式知识表示**: 以 `#KGML v2` 头部声明实体数和关系数,通过缩进表示父子层级,`%rels` 标记跨分支关系,`%vault` 标注密钥键名
- **高级查询命令**: 支持 `children`/`type`/`cat`/`orphans`/`stats`/`recent`/`timeline`/`changed`/`uncertain` 等查询,覆盖子节点、类型、分类、孤立实体、统计、时间线、变更和低置信度实体
- **实体合并**: 通过 `merge.mjs --mode absorb|nest` 合并相似实体,absorb模式吸收源实体属性,nest模式将源实体嵌套为目标实体子节点
- **密钥保管库**: 使用 `vault.mjs set/get/list/del` 管理加密密钥,密钥值永不打印到对话或日志,仅通过 `get` 管道传递
- **深度启发式提取**: 通过 `depth-check.mjs` 评估知识项复杂度,得分 ≥ 4 时提取所有命名组织、事件、策略和交叉关系
- **知识图谱可视化**: 通过 `visualize.mjs` 生成自包含离线HTML,父边渲染为蓝色虚线箭头(60%不透明度),常规边为红色实线箭头
- **配置管理**: 通过 `config.mjs get/set/reset` 管理 `tokenBudget`(5000)、`maxAttrLen`(40)、`minEntities`(30)、`levenshteinThreshold`(2)等参数
- **跨助手只读访问**: 通过 `reader.mjs` 的 `createReader()` 或 `export.mjs --format json` 提供只读访问,其他助手无写入权限
- **记忆导入**: 通过 `import-memory.mjs --apply` 以置信度 0.5 导入记忆,使用 `query.mjs uncertain` 审查自动导入的实体
- **知识整合**: 当实体数 > 80 时运行 `consolidate.mjs` 整合,自动嵌套单关系孤儿、建议相似标签合并、修剪空属性
### KGML格式知识表示

执行KGML格式知识表示操作,处理用户输入并返回结果。

**输入**: 用户提供KGML格式知识表示所需的参数和指令。

**输出**: 返回KGML格式知识表示的处理结果。

- 执行`KGML格式知识表示`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`KGML格式知识表示`相关配置参数进行设置
### 高级查询命令

执行高级查询命令操作,处理用户输入并返回结果。

**输入**: 用户提供高级查询命令所需的参数和指令。

**输出**: 返回高级查询命令的处理结果。

- 执行`高级查询命令`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`高级查询命令`相关配置参数进行设置
### 实体合并

执行实体合并操作,处理用户输入并返回结果。

**输入**: 用户提供实体合并所需的参数和指令。

**输出**: 返回实体合并的处理结果。

- 执行`实体合并`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`实体合并`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 嵌入式知识图谱、持久化存储结构化、支持查询、可视化与配置、存储持久化结构化、CLI、脚本查询、摘要供会话上下文、核心能力包括、跨助手只读访问与。这些能力在上述核心功能中均有对应处理逻辑。
## 高级查询命令

```bash
node scripts/query.mjs children <id>      # 直接子节点
node scripts/query.mjs type <type>         # 指定类型的所有实体
node scripts/query.mjs cat <category>      # 分类下所有实体
node scripts/query.mjs orphans             # 未链接的孤立实体
node scripts/query.mjs stats               # 图谱统计
node scripts/query.mjs recent [--days 7]   # 最近创建/更新的实体
node scripts/query.mjs timeline [--from YYYY-MM-DD] [--to YYYY-MM-DD]
node scripts/query.mjs changed             # 创建后修改过的实体
node scripts/query.mjs uncertain           # 置信度 < 0.5 的实体
```

## 实体合并

```bash
node scripts/merge.mjs --target <id> --source <id> --mode absorb|nest
```

- `absorb`: 源实体属性合并到目标实体,源实体删除
- `nest`: 源实体成为目标实体的子节点,保留独立属性

## 保管库(密钥)

```bash
node scripts/vault.mjs set <key> <value> --note "description"
node scripts/vault.mjs get <key>          # 原始值(用于管道传递)
node scripts/vault.mjs list               # 仅显示键名
node scripts/vault.mjs del <key>
```

## 深度启发式

添加复杂知识项(文章、论文、报告、系统描述)前,先评估复杂度:

```bash
node scripts/depth-check.mjs "粘贴文本或摘要"
echo "article text" | node scripts/depth-check.mjs
node scripts/depth-check.mjs --file /path/to/article.txt
node scripts/depth-check.mjs --json    # 机器可读输出
```

**关键规则:** 复杂内容永不在2层停止。若得分 ≥ 4,提取所有命名组织、事件、策略和交叉关系,而非仅顶层主题。

## 可视化

```bash
node scripts/visualize.mjs                # → data/kg-viz.html
node scripts/visualize.mjs --output /tmp/graph.html
```

始终使用此脚本,不要编写自定义HTML。输出自包含、离线、无CDN依赖。

父边渲染为**蓝色虚线箭头**(60%不透明度)。常规边为红色实线箭头。

## 配置

所有设置有合理默认值。仅覆盖需要的项,配置仅存储变更。

```bash
node scripts/config.mjs                       # 列出所有设置及当前值
node scripts/config.mjs get <key>              # 获取值(如 summary.tokenBudget)
node scripts/config.mjs set <key> <value>      # 设置值
node scripts/config.mjs reset <key>            # 重置单个键到默认
node scripts/config.mjs reset --all            # 重置全部
node scripts/config.mjs --json                 # 完整配置为JSON
```

### 可用设置

| 区块 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| **summary** | `tokenBudget` | 5000 | kg-summary.md最大token数 |
| | `maxAttrLen` | 40 | 属性值最大字符数 |
| | `maxPerRoot` | 4 | 每个根子树显示的最大关系数 |
| | `compactThreshold` | 400 | 紧凑模式实体数阈值 |
| | `mediumThreshold` | 200 | 中等深度实体数阈值 |
| **validation** | `minEntities` | 30 | 提取PASS的最小实体数 |
| | `minRelationRatio` | 0.5 | 每实体关系比 |
| | `minDepth` | 3 | PASS的最小层级深度 |
| | `minEvents` | 3 | PASS的最小事件节点数 |
| **consolidation** | `autoNest` | true | 自动嵌套单关系孤儿 |
| | `mergeSuggestions` | true | 建议相似标签合并 |
| | `levenshteinThreshold` | 2 | 合并建议最大编辑距离 |
| **visualization** | `repulsion` | 5000 | 物理排斥力 |
| | `edgeRestLength` | 160 | 默认边静止长度 |
| | `simulationSteps` | 500 | 物理模拟迭代次数 |

配置文件: `data/kg-config.json`(每个助手独立,gitignore排除)。

## 跨助手访问(只读)

```javascript
import { createReader } from '<path-to-skill>/lib/reader.mjs';
const kg = createReader();
kg.search("query"); kg.traverse("id", { depth: 2 }); kg.stats();
```

或CLI: `node scripts/export.mjs --format json --target /path/to/output.json`

## 记忆导入

```bash
node scripts/import-memory.mjs            # 试运行
node scripts/import-memory.mjs --apply    # 以置信度 0.5 添加
```

然后: `node scripts/query.mjs uncertain` 审查自动导入的实体。

## 知识实体指南

`knowledge` 类型涵盖声明性和程序性知识。使用属性和标签区分:

| 类型 | 标签 | 关键属性 | 示例 |
| --- | --- | --- | --- |
| 事实/发现 | `#fact`, `#til` | `source`, `field`, `summary` | "大语言模型每token约4字符" |
| 研究/论文 | `#paper`, `#research` | `source`, `field`, `summary`, `author` | AI对齐论文发现 |
| 想法 | `#idea` | `summary`, `status` | "构建知识图谱查询CLI" |
| 操作流程 | `#howto`, `#procedure` | `steps`, `context`, `summary` | "如何在树莓派部署" |
| 心智模型 | `#mental-model`, `#framework` | `steps`, `context`, `summary` | "调试网络: ping→DNS→防火墙" |
| 工作流 | `#workflow` | `steps`, `context`, `summary` | "代码审查: 先测试再实现" |

**程序性知识属性:**

* `steps`: 有序流程字符串(使用 `→` 或编号: `"1. 检查日志 → 2. 复现 → 3. 修复 → 4. 测试"`)
* `context`: 何时/何地应用此知识(如 `"网络断开时"`, `"代码审查期间"`)
* `summary`: 知识内容的简短描述

## 整合

每周或实体数 > 80 时运行 `node scripts/consolidate.mjs`。然后运行 `summarize.mjs`。

## 安全

* 永不在对话中打印保管库值或记录到 memory/ 文件
* `vault.enc.json` 和 `.vault-key` 不得出现在上下文中
* 其他助手: 通过 `reader.mjs` 只读访问,无写入权限

## 使用流程

1. 执行 `node scripts/install.mjs` 安装并修补助手指令文件
2. 使用 `node scripts/depth-check.mjs` 评估知识项复杂度,得分 ≥ 4 时提取完整层级
3. 添加知识实体,使用属性和标签区分声明性/程序性知识
4. 通过 `node scripts/query.mjs` 查询图谱(children/type/cat/orphans/stats/recent/uncertain)
5. 使用 `node scripts/merge.mjs --mode absorb|nest` 合并相似实体
6. 通过 `node scripts/vault.mjs` 管理加密密钥,永不在对话中暴露密钥值
7. 使用 `node scripts/visualize.mjs` 生成自包含可视化HTML
8. 通过 `node scripts/config.mjs set` 调整 `tokenBudget`、`minEntities`、`levenshteinThreshold` 等参数
9. 实体数 > 80 时运行 `node scripts/consolidate.mjs` 整合图谱

## 示例

### 示例1:查询孤立实体与统计

```bash
node scripts/query.mjs orphans
# 输出:
# Orphan entities (3):
#   - [e042] DebugTip(调试技巧):howto — steps,context
#   - [e089] OldIdea(旧想法):idea — summary,status
#   - [e103] Note(笔记):note — summary

node scripts/query.mjs stats
# 输出:
# Graph Statistics:
#   Total entities: 127
#   Total relations: 89
#   Relation ratio: 0.70
#   Max depth: 4
#   Categories: 6
#   Orphan entities: 3
#   Uncertain entities: 12
```

### 示例2:合并相似实体

```bash
node scripts/merge.mjs --target e042 --source e103 --mode absorb
# 输出:
# Merged e103 → e042 (absorb)
#   Transferred attributes: summary
#   Source e103 deleted
#   3 relations updated

node scripts/merge.mjs --target e042 --source e089 --mode nest
# 输出:
# Nested e089 under e042
#   e089 is now child of e042
#   Relations preserved
```

### 示例3:保管库操作

```bash
node scripts/vault.mjs set API_KEY "sk-abc123" --note "外部API访问密钥"
# 输出: Stored key 'API_KEY' with note

node scripts/vault.mjs list
# 输出:
# Vault keys:
#   - API_KEY (外部API访问密钥)
#   - DB_PASSWORD (数据库密码)

node scripts/vault.mjs get API_KEY
# 输出: sk-abc123 (仅用于管道传递,不在对话中显示)
```

### 示例4:深度启发式评估

```bash
node scripts/depth-check.mjs --file /path/to/article.txt --json
# 输出:
# {
#   "score": 5,
#   "recommendation": "extract_all",
#   "estimatedEntities": 45,
#   "estimatedDepth": 4,
#   "namedEntities": ["OrgA", "OrgB", "PolicyX", "EventY"],
#   "reason": "Complex content with multiple organizations, policies, and cross-references"
# }
```

### 示例5:可视化生成

```bash
node scripts/visualize.mjs --output /tmp/kg-graph.html
# 输出:
# Visualization generated: /tmp/kg-graph.html
# Entities: 127, Relations: 89
# Parent edges: 34 (blue dashed)
# Regular edges: 55 (red solid)
# Self-contained, offline, no CDN dependencies
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 保管库键不存在 | `vault.mjs get <key>` 查询未设置的键 | 先使用 `vault.mjs set <key> <value>` 存储键值,使用 `vault.mjs list` 查看已有键名 |
| 置信度过低实体堆积 | `import-memory.mjs --apply` 导入大量置信度 < 0.5 的实体 | 运行 `query.mjs uncertain` 审查,手动确认或删除低置信度实体 |
| 合并目标不存在 | `merge.mjs --target <id>` 指定的实体ID已被删除 | 使用 `query.mjs` 确认实体ID有效,合并前检查目标实体存在 |
| KGML格式错误 | 实体缩进不一致或 `%rels`/`%vault` 标记位置错误 | 遵循KGML v2格式: 头部声明、缩进表示层级、`%rels` 前空行分隔 |
| 可视化渲染空白 | 实体数过多导致物理模拟不收敛 | 调整 `config.mjs set visualization.repulsion 3000` 降低排斥力,增加 `simulationSteps` 到 800 |
| 记忆导入冲突 | 导入的实体与已有实体标签相似但属性不同 | 先 `import-memory.mjs` 试运行检查,使用 `consolidate.mjs` 合并相似实体,`levenshteinThreshold` 控制合并灵敏度 |
| 跨助手写入被拒绝 | 其他助手尝试通过非 `reader.mjs` 方式写入图谱 | 跨助手访问仅通过 `reader.mjs` 只读,写入操作必须在本助手内执行 |
| 配置验证失败 | `config.mjs set` 设置了非法值(如 `minEntities` 为负数) | 检查设置项的值范围,`minEntities` ≥ 0,`minRelationRatio` 在 0-1 之间,使用 `reset <key>` 恢复默认 |
| 整合后数据丢失 | `consolidate.mjs` 的 `autoNest` 错误嵌套了不应合并的实体 | 整合前备份 `data/kg-config.json`,设置 `autoNest: false` 禁用自动嵌套,手动审查合并建议 |
| token预算超限 | kg-summary.md超过 `tokenBudget`(5000) | 调整 `config.mjs set summary.tokenBudget 8000`,或减小 `maxAttrLen` 和 `maxPerRoot` 压缩摘要 |

## 常见问题

### Q1: 如何选择 `absorb` 和 `nest` 合并模式?
A: `absorb` 将源实体的属性合并到目标实体,源实体被删除,适合两个实体描述同一概念的情况。`nest` 将源实体作为目标实体的子节点,保留独立性,适合源实体是目标实体的子类别或细节的情况。合并前使用 `query.mjs` 查看两个实体的属性和关系,判断是否应完全吸收或保持层级。

### Q2: 保管库的密钥如何安全使用?
A: 使用 `vault.mjs set <key> <value>` 存储密钥,密钥值经加密存储在 `vault.enc.json` 中。使用 `vault.mjs get <key>` 获取原始值,仅用于管道传递给其他命令(如 `vault.mjs get API_KEY | curl -H "Authorization: Bearer $(cat)"`)。永不在对话中打印密钥值,`vault.enc.json` 和 `.vault-key` 不得出现在助手上下文中。

### Q3: `depth-check.mjs` 得分 ≥ 4 意味着什么?
A: 得分 ≥ 4 表示知识内容复杂度高,包含多个命名组织、事件、策略和交叉关系。此时不应仅在2层提取顶层主题,而应提取所有命名的组织、事件、政策和跨分支关系。这确保知识图谱捕获内容的完整结构,而非仅表面主题。得分 < 4 的简单内容可适当减少提取深度。

### Q4: 何时需要运行 `consolidate.mjs` 整合?
A: 每周定期运行一次,或当实体数 > 80 时运行。整合操作包括: 自动嵌套单关系孤儿(`autoNest`)、建议编辑距离 ≤ `levenshteinThreshold`(默认2)的相似标签合并、修剪空属性。整合后运行 `summarize.mjs` 更新摘要。建议整合前备份 `data/kg-config.json`,以防错误合并。

### Q5: 如何让其他助手访问知识图谱?
A: 其他助手通过 `reader.mjs` 的 `createReader()` 函数只读访问,支持 `search()`、`traverse()`、`stats()` 方法。或通过CLI `node scripts/export.mjs --format json --target /path/to/output.json` 导出为JSON文件。其他助手无写入权限,写入操作必须在本助手内执行。这确保知识图谱的数据完整性。

### Q6: `uncertain` 查询返回的实体如何处理?
A: `query.mjs uncertain` 返回置信度 < 0.5 的实体,通常是 `import-memory.mjs --apply` 自动导入的。逐个审查这些实体: 确认正确的补充属性并提升置信度,或删除不准确的实体。建议导入记忆后立即运行 `uncertain` 查询审查,避免低质量实体积累影响图谱准确性。

### Q7: 可视化中蓝色虚线和红色实线分别代表什么?
A: 蓝色虚线箭头(60%不透明度)表示父子层级关系(parent edge),即实体间的树状结构关系。红色实线箭头表示常规关系(regular edge),即通过 `%rels` 定义的跨分支关系。通过颜色和线型区分,可以直观识别哪些是层级结构、哪些是交叉引用。可视化使用 `visualize.mjs` 生成,自包含离线HTML,无CDN依赖。

## 已知限制

- 知识图谱以JSON存储,超大图谱(实体数 > 1000)可能影响查询性能
- 跨助手访问仅限只读,其他助手无法直接写入图谱
- 保管库密钥依赖 `.vault-key` 文件,丢失该文件将无法解密密钥
- `depth-check.mjs` 的复杂度评估基于启发式规则,可能对某些领域内容判断不准确
- 可视化的物理模拟在实体数过多时可能不收敛,需调整 `repulsion` 和 `simulationSteps` 参数
