---
slug: graph-knowledge-base
name: graph-knowledge-base
version: "1.0.0"
displayName: 知识图谱库(专业版)
summary: 全功能知识图谱工具，支持图谱关系查询、知识分析、跨实体关联与多格式导出
license: Proprietary
edition: pro
description: |-
  知识图谱库(专业版)是面向团队与知识工作者的全功能知识图谱管理工具，在免费版基础上新增图谱关系查询、知识分析、跨实体关联与多格式导出等高级能力。核心能力：
  - 完整的实体管理、事实添加与版本替代能力
  - 图谱关系查询，发现跨实体隐含关联
  - 知识分析，事实聚类与主题识别
  - 跨实体关联，构建知识网络视图
  - 多格式导出...
tags:
- 集成工具
- 知识管理
- 知识图谱
- 专业版
tools:
  - - read
- exec
---
# 知识图谱库(专业版)

## 核心能力

| 能力 | 说明 | 专业版增强 |
|------|------|-----------|
| 实体与事实管理 | 原子化事实添加与替代 | 批量导入与迁移 |
| 图谱关系查询 | 跨实体关联发现 | 语义相似度+共现分析 |
| 知识分析 | 事实主题聚类 | 热点识别与盲区检测 |
| 跨实体关联 | 知识网络可视化 | 交互式图谱浏览 |
| 多格式导出 | JSON/CSV/Markdown | GraphML/Gephi/Neo4j |
| 版本对比 | 事实演进时间线 | 差异分析与回溯 |
| 批量操作 | 批量导入导出 | CSV/JSON/API同步 |
| 优先支持 | SLA保障 | 专属技术支持通道 |
### 实体与事实管理

执行实体与事实管理操作,处理用户输入并返回结果。

**输入**: 用户提供实体与事实管理所需的参数和指令。

**输出**: 返回实体与事实管理的处理结果。
### 图谱关系查询

执行图谱关系查询操作,处理用户输入并返回结果。

**输入**: 用户提供图谱关系查询所需的参数和指令。

**输出**: 返回图谱关系查询的处理结果。
### 知识分析

执行知识分析操作,处理用户输入并返回结果。

**输入**: 用户提供知识分析所需的参数和指令。

**输出**: 返回知识分析的处理结果。


## 适用场景

### 场景一：企业专家网络构建
HR部门希望构建企业内部的专家网络图谱。为每位员工创建实体，记录技能、项目、认证等事实。通过图谱关系查询发现跨部门的技能重叠与互补，通过知识分析识别技能热点与稀缺领域，辅助人才调配与团队组建。

### 场景二：研究文献关联发现
研究团队管理大量文献笔记，每篇文献作为实体，关键发现作为事实。通过跨实体关联发现不同研究间的隐含联系，通过知识分析识别研究主题的演进趋势，为新的研究方向提供数据支撑。

### 场景三：项目知识资产导出
项目结项时需要将知识资产导出归档。专业版支持多格式导出，将项目实体与事实导出为JSON(结构化存档)、Markdown(可读报告)、GraphML(图谱工具导入)等格式，确保知识资产可移植与可复用。

### 场景四：跨项目知识复用
新项目启动时，通过图谱关系查询在历史项目知识库中搜索相关事实。跨实体关联功能展示与新项目主题相关的历史决策、经验教训与技术选型，避免重复探索，加速项目启动。

### 场景五：知识盲区检测
知识管理负责人希望评估团队知识覆盖度。通过知识分析模块的事实聚类与主题识别，生成知识覆盖热力图，识别事实稀疏的"盲区"领域，指导后续知识补充方向。

## 使用流程

本工具属于复杂工具，预计180秒内可完成图谱查询与分析。

### 步骤1：批量导入事实
```bash
python3 scripts/kg.py import \
  --file knowledge.csv \
  --format csv \
  --dry-run
```

### 步骤2：执行图谱关系查询
```bash
python3 scripts/kg.py graph \
  --entity people/zhangsan \
  --depth 2 \
  --relation similarity \
  --threshold 0.6
```

### 步骤3：知识主题分析
```bash
python3 scripts/kg.py analyze \
  --scope all \
  --cluster-themes \
  --report markdown \
  --output analysis-report.md
```

### 步骤4：跨实体关联可视化
```bash
python3 scripts/kg.py network \
  --entities people/zhangsan,projects/alpha,technologies/react \
  --format graphml \
  --output knowledge-network.graphml
```

### 步骤5：多格式导出
```bash
python3 scripts/kg.py export \
  --entity projects/alpha \
  --formats json,markdown,graphml \
  --output-dir ./export
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理

| 现象 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 图谱查询无结果 | 关联阈值过高 | 降低threshold值重新查询 | 中 |
| 分析超时 | 事实数量过大 | 缩小scope范围或分批分析 | 中 |
| 导出格式错误 | 格式参数不支持 | 确认格式在支持列表中 | 低 |
| 批量导入失败 | CSV格式不规范 | 检查列名与数据类型 | 高 |
| GraphML打开乱码 | 编码问题 | 确认使用UTF-8编码导出 | 低 |
| 关联深度过大卡顿 | depth设置过高 | 降低depth值(建议≤3) | 中 |
| 主题聚类不准 | 事实数量不足 | 积累更多事实后重新分析 | 低 |
| 版本快照缺失 | 时间戳不完整 | 检查事实的created_at字段 | 中 |

## 依赖说明

### 运行环境
- **Agent平台**：支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**：Windows / macOS / Linux
- **Python**：3.9+(用于运行kg.py脚本及分析模块)

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| Python | 运行时 | 必需 | python.org官方下载 |
| 标准库(json/os/csv) | Python内置 | 必需 | Python自带 |
| scikit-learn | Python包 | 推荐 | `pip install scikit-learn`(聚类分析) |
| networkx | Python包 | 推荐 | `pip install networkx`(图谱算法) |
| numpy | Python包 | 推荐 | `pip install numpy`(数值计算) |

### API Key 配置
- **本工具特点**：纯本地运行，无需外部API Key
- **数据存储**：所有知识数据存储在本地文件系统
- **安全要求**：建议将知识库目录加入版本控制或定期备份
- **团队协作**：通过Git等版本控制工具实现团队协作与冲突管理

### 可用性分类
- **分类**：MD+EXEC()
- **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行知识图谱管理与关联分析任务，数据完全本地化

## 案例展示

### 批量导入CSV格式
```csv
entity,category,fact,source
people/zhangsan,status,担任前端开发工程师,doc
people/zhangsan,skill,精通React框架,conversation
projects/alpha,status,已完成优秀阶段交付,meeting
technologies/react,status,采用v18版本,doc
```

### 图谱查询参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| --entity | string | - | 起始实体 |
| --depth | int | 2 | 关联深度 |
| --relation | enum | similarity | 关系类型(similarity/cooccurrence/manual) |
| --threshold | float | 0.5 | 关联强度阈值 |
| --format | enum | json | 输出格式(json/graphml/dot) |

### 知识分析参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| --scope | enum | all | 分析范围(all/entity/category) |
| --cluster-themes | bool | true | 启用主题聚类 |
| --heatmap | bool | false | 生成覆盖热力图 |
| --gap-detection | bool | true | 盲区检测 |
| --report | enum | markdown | 报告格式(markdown/html/json) |

### 导出格式说明

| 格式 | 用途 | 特点 |
|------|------|------|
| JSON | 结构化存档 | 完整保留事实与关系 |
| CSV | 表格分析 | 便于Excel处理 |
| Markdown | 可读报告 | 适合文档归档 |
| GraphML | 图谱工具 | 兼容Gephi/yEd |
| Neo4j | 图数据库 | Cypher导入脚本 |
| Dot | 图形渲染 | Graphviz可视化 |

## 常见问题

### Q1：图谱关系查询的关联强度如何计算？
A：专业版支持两种关联算法。语义相似度(similarity)基于事实文本的向量相似度计算；共现分析(cooccurrence)基于实体在相同来源中共同出现的频率。两种算法可组合使用，阈值默认0.5，可根据需要调整。

### Q2：知识分析的主题聚类准确吗？
A：主题聚类质量依赖事实数量与质量。建议对事实数超过50条的实体集合进行分析。通过`--cluster-themes`预设主题类别可提升准确性。聚类结果会标注置信度，低于0.6的建议人工复核。

### Q3：批量导入支持哪些格式？
A：支持CSV与JSON格式导入。CSV适合从Excel导出的结构化数据；JSON适合从其他系统迁移的嵌套数据。建议先用`--dry-run`预览导入结果，确认无误后正式执行。

### Q4：GraphML文件如何在Gephi中打开？
A：专业版导出的GraphML文件完全兼容Gephi。在Gephi中选择"打开GraphML文件"，导入后可使用Gephi的布局算法与可视化功能进行交互式探索。

### Q5：导出的Neo4j格式如何使用？
A：专业版导出的Neo4j格式包含Cypher导入脚本。在Neo4j浏览器中执行该脚本即可将知识图谱导入图数据库，支持后续的Cypher查询与图算法分析。

### Q6：跨实体关联的深度如何设置？
A：深度(depth)控制关联遍历的层级。深度1仅显示直接关联，深度2显示二度关联(关联的关联)。建议从深度1开始探索，逐步增加深度。深度过大会导致结果过于复杂，建议不超过3。

### Q7：知识盲区检测的原理是什么？
A：盲区检测通过分析事实在各类别与实体间的分布密度识别稀疏区域。若某类别下的事实数显著低于平均值，或某实体仅有少量事实，会被标记为盲区。结合热力图可直观识别知识覆盖薄弱处。

### Q8：版本对比能回溯到任意时间点吗？
A：可以。专业版基于事实的`created_at`与`superseded_at`时间戳，可重建任意时间点的知识快照。通过`snapshot --date 2026-03-01`命令查看指定日期的知识状态。

### Q9：专业版是否支持团队协作？
A：专业版支持通过文件同步(如Git)实现团队协作。知识库以文件形式存储，适合版本控制。建议为不同成员分配独立的实体管理范围，通过合并策略解决冲突。

### Q10：如何获取优先技术支持？
A：专业版用户可通过专属支持通道提交工单，享受SLA保障的响应时效。图谱构建与分析相关问题建议附带实体规模与分析参数，便于快速定位问题。

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
