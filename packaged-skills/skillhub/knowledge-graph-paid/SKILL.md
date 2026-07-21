---
slug: knowledge-graph-paid
name: knowledge-graph-paid
version: "1.0.0"
displayName: 知识图谱工具(专业版)
summary: 团队级嵌入式知识图谱,含加密保险库、可视化、多Agent协作与内存导入。
license: Proprietary
edition: pro
description: |-
  知识图谱工具(专业版)面向团队与企业,提供完整的嵌入式知识图谱能力,含加密保险库、离线可视化、跨Agent协作与内存自动导入。核心能力:
  - 全量查询、合并、嵌套、整理能力
  - 加密保险库:密钥/令牌加密存储,权限隔离
  - 离线HTML可视化:自包含图谱交互页面
  - 跨Agent只读+写入:多Agent共享知识
  - 内存自动导入:从会话历史提取并审查
  - 高级配置:物理参数、阈值、压缩策略

  适用场景:
  - 团队知识库与决策记录沉淀
  - 研究项目多源知识整合
  - 多Agent协作共享长期记忆
  - 敏感配置...
tags:
- Development
- Knowledge
- 团队知识库
- 企业级
- 可视化
- 安全
tools:
  - - read
- exec
---
# 知识图谱工具(专业版)

## 核心能力

| 能力模块 | 说明 | 与免费版差异 |
| --- | --- | --- |
| 全量查询 | 子节点、类型、分类、孤立、统计、时间线、变更、低置信度 | 与免费版一致 |
| 实体合并 | absorb/nest两种合并模式 | 免费版仅基础整理 |
| 加密保险库 | 密钥/令牌加密存储,权限隔离,绝不泄露明文 | 免费版无 |
| 离线可视化 | 自包含HTML交互页面,物理引擎布局 | 免费版无 |
| 跨Agent协作 | reader.mjs只读 + 受控写入 | 免费版仅单Agent |
| 内存导入 | 从会话历史自动提取实体,低置信度审查 | 免费版无 |
| 高级配置 | 物理参数、验证阈值、压缩策略、整理自动化 | 免费版仅基础设置 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。

- 执行`能力模块`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 全量查询

执行全量查询操作,处理用户输入并返回结果。

**输入**: 用户提供全量查询所需的参数和指令。

**输出**: 返回全量查询的处理结果。

- 执行`全量查询`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`全量查询`相关配置参数进行设置
### 实体合并

执行实体合并操作,处理用户输入并返回结果。

**输入**: 用户提供实体合并所需的参数和指令。

**输出**: 返回实体合并的处理结果。

- 执行`实体合并`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`实体合并`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 团队级嵌入式知识、含加密保险库、协作与内存导入、知识图谱工具、专业版、面向团队与企业、提供完整的嵌入式、知识图谱能力、协作与内存自动导、核心能力、整理能力、自包含图谱交互页、共享知识、内存自动导入、从会话历史提取并。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:团队决策记录沉淀

团队完成一次架构评审,希望把决策、备选方案与权衡沉淀为可检索的知识。

```bash
# 查看当前图谱规模
node scripts/query.mjs stats

# 评估决策文档复杂度
node scripts/depth-check.mjs --file /path/to/adr.md

# 提取后写入,Agent 会自动建议合并相似实体
node scripts/consolidate.mjs
```

Agent 会读取决策文档,提取实体(方案、约束、风险)、关系(权衡、依赖、替代),并在 KGML 中标注置信度,便于后续审查。

```text
#KGML v2 | 28e 15r | depth:4 | 2026-07-18
[决策]
微服务拆分(ADR-007):decision — 按业务能力拆分,独立部署
  服务边界:principle — 限界上下文驱动
  数据一致性:constraint — 最终一致+Saga
%rels
微服务拆分>权衡>单体部署 微服务拆分>依赖>服务网格
```

### 场景二:加密存储团队密钥

团队需要把API密钥、数据库连接串等敏感信息加密存储,且不让明文进入上下文。

```bash
# 设置加密键值(带备注)
node scripts/vault.mjs set db_password 'S3cret!' --note "生产数据库主密码"

# 获取原始值(用于管道传递,不在聊天显示)
node scripts/vault.mjs get db_password | xargs -I{} apply-config {}

# 列出键名(不显示值)
node scripts/vault.mjs list

# 删除
node scripts/vault.mjs del db_password
```

安全原则:

- 绝不在聊天或日志中打印保险库值
- `vault.enc.json` 与 `.vault-key` 永不进入上下文
- 其他Agent通过 reader.mjs 只读访问,无写入权限

### 场景三:多Agent共享知识

团队有多个Agent各司其职,希望共享同一份知识图谱。

```javascript
// Agent A 写入知识
import { createReader } from '<path-to-skill>/lib/reader.mjs';
const kg = createReader();
kg.search("微服务");
kg.traverse("id-微服务拆分", { depth: 2 });
kg.stats();
```

```bash
# 导出为JSON供其他Agent消费
node scripts/export.mjs --format json --target /shared/kg-export.json
```

跨Agent访问规则:

- 只读访问:通过 reader.mjs,任何Agent可用
- 写入访问:仅授权Agent,通过权限配置控制
- 数据隔离:每个Agent的配置独立,互不污染

## 使用流程

### 1. 团队初始化

```bash
# 在团队共享目录初始化
node scripts/install.mjs --workspace /shared/team-kg --platform skill-platform

# 配置团队默认token预算
node scripts/config.mjs set summary.tokenBudget 8000
node scripts/config.mjs set validation.minEntities 50
```

### 2. 可视化生成

```bash
# 默认输出到 data/kg-viz.html
node scripts/visualize.mjs

# 自定义输出路径
node scripts/visualize.mjs --output /tmp/team-graph.html
```

可视化页面特性:

1. 自包含,离线可用,无CDN依赖
2. 父子边渲染为蓝色虚线箭头(60%透明度)
3. 普通关系为红色实线箭头
4. 物理引擎布局,可拖拽与缩放

### 3. 内存导入

```bash
# 先空跑预览
node scripts/import-memory.mjs

# 确认后正式导入(置信度0.5)
node scripts/import-memory.mjs --apply

# 审查自动导入的低置信度实体
node scripts/query.mjs uncertain
```

### 4. 高级合并

```bash
# absorb模式:源实体被目标吸收,属性合并
node scripts/merge.mjs --target <目标id> --source <源id> --mode absorb

# nest模式:源实体作为目标子节点嵌套
node scripts/merge.mjs --target <目标id> --source <源id> --mode nest
```

### 命令参数说明

5. `-config`: 命令参数,用于指定操作选项
6. `-I`: 命令参数,用于指定操作选项
7. `--format`: 命令参数,用于指定操作选项
8. `--output`: 命令参数,用于指定操作选项
9. `--target`: 命令参数,用于指定操作选项

### 命令参数说明

- `--mode`: 命令参数,用于指定操作选项
- `-platform`: 命令参数,用于指定操作选项
- `--platform`: 命令参数,用于指定操作选项
- `--apply`: 命令参数,用于指定操作选项
- `-export`: 命令参数,用于指定操作选项

### 命令参数说明

- `-to-skill`: 命令参数,用于指定操作选项
- `-I`: 命令参数,用于指定操作选项
- `--file`: 命令参数,用于指定操作选项
- `-memory`: 命令参数,用于指定操作选项
- `--source`: 命令参数,用于指定操作选项

### 命令参数说明

- `-I`: 命令参数,用于指定操作选项
- `-viz`: 命令参数,用于指定操作选项
- `--note`: 命令参数,用于指定操作选项

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 建议 20 LTS 及以上(用于加密与多Agent模块)
- **浏览器**: 现代浏览器(用于查看可视化HTML)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js | 运行时 | 必需 | nodejs.org 下载 |
| npm | 包管理器 | 必需 | 随Node.js安装 |
| 团队密码管理器 | 工具 | 推荐 | 用于保管 .vault-key |

### API Key 配置

- 。
- 加密保险库的密钥由本地 `.vault-key` 文件管理,不依赖外部API。
- 多Agent协作时,各Agent的鉴权由所在平台处理。

### 可用性分类

- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。PRO版面向团队与企业,提供加密保险库、可视化、多Agent协作与内存导入能力,完全兼容免费版查询与KGML格式。


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 完整配置项参考

| 模块 | 键 | 默认值 | 说明 |
| --- | --- | --- | --- |
| summary | tokenBudget | 5000 | kg-summary.md 最大token |
| summary | maxChildDepth | auto | 树深度(null=自动:<100取3,100-400取2,>400取1) |
| summary | maxAttrLen | 40 | 属性值最大字符 |
| summary | maxPerRoot | 4 | 每根子树最大关系 |
| summary | compactThreshold | 400 | 紧凑模式实体阈值 |
| summary | mediumThreshold | 200 | 中等深度阈值 |
| validation | minEntities | 30 | 提取通过最小实体 |
| validation | minRelationRatio | 0.5 | 每实体最小关系比 |
| validation | minDepth | 3 | 通过最小层级 |
| validation | minEvents | 3 | 通过最小事件节点 |
| depthCheck | entityCapForEstimate | 50 | 目标估算NER上限 |
| depthCheck | minEntitiesMultiplier | 1.0 | 命名实体→最小目标乘数 |
| depthCheck | extraEntities | 30 | 加到最小实体的额外值 |
| consolidation | autoNest | true | 自动嵌套单关系孤儿 |
| consolidation | mergeSuggestions | true | 相似标签合并建议 |
| consolidation | pruneEmptyAttrs | true | 删除空/null属性 |
| consolidation | levenshteinThreshold | 2 | 合并建议最大编辑距离 |
| visualization | repulsion | 5000 | 物理斥力 |
| visualization | edgeRestLength | 160 | 默认边静止长度 |
| visualization | overlapPenalty | 3 | 重叠斥力乘数 |
| visualization | simulationSteps | 500 | 物理仿真迭代 |
| visualization | initialSpread | 1.5 | 初始节点扩散乘数 |
| visualization | zoomAnimationMs | 400 | 缩放到节点动画时长 |

### 团队治理配置示例

```bash
# 团队高标准:要求更多实体与关系
node scripts/config.mjs set validation.minEntities 50
node scripts/config.mjs set validation.minRelationRatio 0.6
node scripts/config.mjs set validation.minEvents 5

# 大图谱压缩策略
node scripts/config.mjs set summary.compactThreshold 300
node scripts/config.mjs set summary.tokenBudget 8000

# 可视化调整(大图谱需要更大斥力)
node scripts/config.mjs set visualization.repulsion 8000
node scripts/config.mjs set visualization.simulationSteps 800
```

## 常见问题

### Q1:PRO版与免费版如何共存?

两者 KGML 格式与查询命令完全兼容,PRO版包含免费版全部能力。团队升级时直接替换Skill文件,已有 `data/` 目录的图谱数据无需迁移。

### Q2:加密保险库的密钥如何管理?

保险库使用本地加密文件 `vault.enc.json` 与密钥文件 `.vault-key`。两者必须一起备份,且永不进入版本控制或聊天上下文。建议将 `.vault-key` 单独存放在团队密码管理器中。

### Q3:可视化页面能否离线使用?

可以。`visualize.mjs` 生成的HTML完全自包含,无任何CDN或外部依赖,可直接双击在浏览器打开,适合内网或离线环境分享。

### Q4:多Agent写入如何避免冲突?

建议采用"单写入者"模式:只授权一个 curator Agent 拥有写入权限,其他Agent通过 reader.mjs 只读访问,如需新增知识则提交给 curator 审核后写入。这样可避免并发写入冲突。

### Q5:内存导入会污染图谱吗?

内存导入默认以0.5低置信度写入,并标记为 `uncertain`。导入后必须运行 `node scripts/query.mjs uncertain` 逐个审查,人工确认的提升置信度,拒绝的删除,避免低质量内容污染图谱。

### Q6:支持多租户隔离吗?

支持。通过不同 `--workspace` 路径初始化多个独立图谱实例,各自拥有独立的 `data/` 与配置。租户间数据物理隔离,互不影响。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
