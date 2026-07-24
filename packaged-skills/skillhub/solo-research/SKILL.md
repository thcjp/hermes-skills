---
slug: "solo-research"
name: "solo-research"
version: 1.7.2
displayName: "独立研究工具"
summary: "多策略研究工具，支持GitHub库发现、WebFetch、MCP搜索、内容回退与Product Hunt调研。"
license: "Proprietary"
description: |-
  独立研究工具，通过多搜索策略获取全面准确的研究结果.
  支持GitHub Library Discovery、WebFetch、MCP web_search、Blocked Content Fallback.
  覆盖Product Hunt调研、技术选型、库发现等多种研究场景.
  提供来源验证、交叉验证与结构化结果输出，适用于深度研究与决策支持.
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
tags:
  - 信息检索
  - 搜索
  - 检索
  - 工具
category: "Knowledge"
---
# 独立研究工具

多策略研究工具，支持GitHub库发现、WebFetch、MCP搜索、内容回退与Product Hunt调研.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 独立研究工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### GitHub Library Discovery
在GitHub上发现与评估开源库：

- **关键词搜索**：按技术栈、功能描述搜索相关仓库
- **排序评估**：按stars、最近更新、活跃度排序
- **质量评估**：检查README完整性、文档质量、issue处理速度
- **依赖分析**：分析库的依赖关系与兼容性
- **社区评估**：检查贡献者数量、fork数、release频率

**输入**: 用户提供GitHub Library Discovery所需的指令和必要参数.
**输出**: 返回GitHub Library Discovery的处理结果,包含执行状态码、结果数据和执行日志。### WebFetch
获取指定URL的网页内容并进行结构化提取：

- **内容获取**：获取网页全文内容
- **结构化提取**：从网页中提取关键信息（标题、正文、表格等）
- **多格式支持**：支持HTML、Markdown、JSON等格式
- **重试机制**：网络失败时自动重试
- **内容清洗**：去除广告、导航等无关内容

**输入**: 用户提供WebFetch所需的指令和必要参数.
**处理**: 解析WebFetch的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回WebFetch的处理结果,包含执行状态码、结果数据和执行日志。### MCP web_search

通过MCP（Model Context Protocol）web_search服务进行网络搜索：

- **并行搜索**：同时发起多个搜索查询，提高效率
- **多源搜索**：从多个搜索引擎获取结果
- **结果聚合**：聚合不同来源的搜索结果，去重排序
- **语义搜索**：支持自然语言查询，而非仅关键词匹配
- **实时结果**：获取最新的网络信息

### Blocked Content Fallback

当内容被阻止或无法访问时的回退策略：

- **缓存回退**：尝试从缓存服务（如Wayback Machine）获取内容
- **替代来源**：寻找相同内容的替代URL
- **摘要回退**：从搜索结果摘要中提取关键信息
- **API回退**：使用API替代网页抓取（如Reddit API替代网页爬取）
- **用户提示**：当所有回退策略失败时，提示用户提供内容或替代来源

### Product Hunt Research
在Product Hunt上进行产品调研：

- **产品搜索**：按类别、关键词搜索Product Hunt上的产品
- **趋势分析**：分析产品的upvotes、评论数与排名趋势
- **竞品对比**：对比同类产品的功能、定价与用户评价
- **发布时间**：查看产品发布时间与更新历史
- **用户反馈**：提取用户评论中的优缺点分析

**输出**: 返回Product Hunt Research的处理结果,包含执行状态码、结果数据和执行日志.
### 研究方法论（Research Methodology）

系统化的研究流程确保结果全面准确：

- **并发查询（Concurrent queries）**：同时发起多个搜索，覆盖不同角度
- **引用追踪（Citation tracking）**：追踪与验证信息来源
- **来源验证（Source verification）**：验证来源的权威性与时效性
- **交叉验证（Cross-validation）**：通过多个来源验证同一信息
- **综合与差距分析（Synthesis & gaps）**：综合研究发现，识别知识差距

### 结构化结果输出（Result Format）

以标准格式输出研究结果：

- **SOLO Answer**：直接回答用户问题的核心结论
- **Search Process Summary**：搜索过程摘要（使用的工具与查询）
- **Key Findings**：关键发现，按重要性排序
- **Citation Table**：引用表格（来源、URL、访问日期）
- **Gaps & Limitations**：知识差距与研究局限性

#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 明确研究问题与目标
3. Agent根据问题类型选择搜索策略（GitHub、WebFetch、MCP等）
4. 并发执行多个搜索查询，覆盖不同角度
5. 对搜索结果进行来源验证与交叉验证
6. 尝试获取完整内容，如遇阻止使用回退策略
7. 综合研究发现，识别知识差距
8. 以标准格式输出结构化研究结果

#
## 示例

### 示例1：发现React状态管理库

```
用户: 帮我找找2026年最流行的React状态管理库
# ...
Agent: 研究完成
# ...
## SOLO Answer
2026年最流行的React状态管理库依次为：Zustand、Jotai、Redux Toolkit、TanStack Query.
# ...
## Search Process Summary
- GitHub Library Discovery: 搜索 "react state management"，按stars排序
- MCP web_search: "best react state management 2026"
- WebFetch: 获取npm trends对比页面
# ...
## Key Findings
1. Zustand - 42k stars，轻量级，API简洁，2025年增长最快
2. Jotai - 18k stars，原子化状态管理，适合细粒度状态
3. Redux Toolkit - 60k stars，企业级首选，DevTools生态完善
4. TanStack Query - 38k stars，服务端状态管理，替代Redux场景
# ...
## Citation Table
| 来源 | URL | 访问日期 |
|:---:|:---:|:---:|
| GitHub | 相关技术文档 | 2026-02-16 |
| npm trends | npmtrends.com/zustand-vs-jotai | 2026-02-16 |
```

### 示例2：Product Hunt产品调研

```
用户: 调研Product Hunt上最近的热门AI写作工具
# ...
Agent: 研究完成
# ...
## SOLO Answer(续1)
近期Product Hunt上热门的AI写作工具包括：Jasper AI、Copy.ai、Writesonic、Rytr.
# ...
## Key Findings(续1)
1. Jasper AI - 1,245 upvotes，企业级AI写作，支持品牌语调
2. Copy.ai - 980 upvotes，营销文案专用，模板丰富
3. Writesonic - 856 upvotes，支持长文写作，SEO优化
4. Rytr - 720 upvotes，性价比高，适合个人使用
# ...
## Gaps & Limitations
- 未包含最新一周发布的产品（Product Hunt API延迟）
- 用户评价基于Product Hunt评论，可能存在偏差
```

### 示例3：技术选型研究

```
用户: 对比PostgreSQL和MongoDB在2026年的优劣
# ...
Agent: 研究完成
# ...
## SOLO Answer(续2)
PostgreSQL适合需要ACID事务与复杂查询的场景，MongoDB适合灵活schema与水平扩展的场景.
# ...
## Key Findings(续2)
1. PostgreSQL: SQL标准兼容，ACID事务，JSON支持，扩展性强
2. MongoDB: 文档模型灵活，水平扩展原生支持，聚合管道强大
3. 性能对比: PostgreSQL在复杂查询上更优，MongoDB在写入吞吐量上更优
4. 生态: 两者均有成熟的ORM/ODM支持与云服务
# ...
## Cross-validation
- DB-Engines排名: PostgreSQL第4，MongoDB第5（2026年2月）
- Stack Overflow Survey: PostgreSQL使用率持续上升
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| WebFetch获取失败 | 网页不可访问或超时 | 使用Blocked Content Fallback；尝试缓存或替代URL |
| MCP web_search不可用 | MCP服务未配置 | 降级为WebFetch直接获取；提示用户配置MCP |
| GitHub API限流 | API调用频率超限 | 等待限流重置；使用未认证API（低频率）；提示用户配置Token |
| 搜索结果为空 | 关键词过于具体 | 扩大搜索范围；使用同义词；调整搜索策略 |
| 来源不可靠 | 信息来源缺乏权威性 | 标记来源可靠性；寻找权威替代来源；交叉验证 |
| Product Hunt API不可用 | API未配置或过期 | 降级为WebFetch抓取Product Hunt网页；提示用户配置API |

## 常见问题

### Q1: 支持哪些搜索策略？
A: 支持五种搜索策略：GitHub Library Discovery（开源库发现）、WebFetch（网页内容获取）、MCP web_search（网络搜索）、Blocked Content Fallback（内容回退）、Product Hunt Research（产品调研）。根据问题类型自动选择或组合使用.
### Q2: 如何处理被阻止的内容？
A: 使用Blocked Content Fallback策略：1）尝试缓存服务（Wayback Machine）；2）寻找替代URL；3）从搜索摘要提取关键信息；4）使用API替代网页抓取；5）提示用户提供内容.
### Q3: 研究结果如何保证准确性？
A: 通过研究方法论确保准确性：并发查询覆盖多角度、引用追踪验证来源、来源验证检查权威性、交叉验证通过多源验证同一信息、综合与差距分析识别知识差距.
### Q4: 结果输出格式是什么样的？
A: 标准输出包含五部分：SOLO Answer（核心结论）、Search Process Summary（搜索过程）、Key Findings（关键发现）、Citation Table（引用表格）、Gaps & Limitations（知识差距与局限性）.
### Q5: MCP web_search必须配置吗？
A: 不是必须的。MCP web_search为可选依赖，未配置时可降级为WebFetch直接获取网页内容。但配置MCP可获得更好的搜索体验与更全面的结果.
### Q6: 如何提高搜索效率？
A: 1）使用并发查询同时发起多个搜索；2）按问题类型选择最优策略；3）先用MCP搜索获取概览，再用WebFetch获取详情；4）对GitHub项目优先使用GitHub API；5）设置合理的超时与重试机制.
## 已知限制

- 需要网络访问，无网络环境无法执行搜索
- MCP web_search为可选依赖，未配置时搜索能力受限
- GitHub API有速率限制，未认证时限制更严格
- 部分网站可能阻止WebFetch访问，需依赖回退策略
- 搜索结果的时效性取决于搜索引擎索引更新频率
- 研究深度受LLM上下文窗口限制，超长内容需分批处理
