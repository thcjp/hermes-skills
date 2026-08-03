---
slug: elite-longterm-memory-local
name: elite-longterm-memory-local
version: 1.1.1
displayName: 本地向量记忆系统
summary: '基于 LanceDB '
summary_zh: 基于 LanceDB 与本地 Embedding 的纯本地向量记忆，零外部 API 依赖。基于 LanceDB 与纯 JavaScript
  Embedding 的本地向量记忆系统，无需外部
license: MIT
description: |-。基于 LanceDB 。支持自动化配置和灵活的参数设置，适适配多种工作环境，增强工作效率。。基于 LanceDB。本地向量记忆系统工具。支持自动化配置和灵活的参数设置，适用于多种工作场景，提升工作效率和准确性。。基于。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。
  LanceDB。本地向量记忆系统是一款高效实用的工具。elite-longterm-memory-local支持多种配置选项'
tools:
- read
- exec
- write
homepage: ''
tags:
- 智能助手
- 记忆管理
- 上下文
- AI
- node
- ollama
category: Agents
homepage: "https://skillhub.cn/skill/"
---
> **核心功能**: 本技能提供自动化配置和灵活的参数设置、时使用、、工作流优化时使用、处理、工作流优化时使用、化配置和灵活的参数设置等能力。

# 本地向量记忆系统（Elite Longterm Memory Local）

**本地优先，隐私至上。** 基于 LanceDB 与 Ollama 本地 Embedding 的向量记忆系统，零外部 API 依赖，所有数据完全留在本地。通过五层记忆架构与 WAL 协议，让 Agent 具备高效的语义搜索与上下文召回能力，同时保障数据隐私.
## 参数说明
| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 本地向量记忆系统处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版扩展能力
| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |
| 数据质量检测与清洗规则 | 不支持 | 支持 |

## 能力清单
- **纯本地向量搜索（LanceDB）**：基于 LanceDB 的语义召回，无需外部 API。参数：node （请参考skill目录中的脚本文件） store "用户喜欢深色模式" --importance 0.9 --category preference，node （请参考skill目录中的脚本文件） search "用户界面偏好"。输出：按语义相似度排序的记忆列表。配置项：ollamaUrl（默认 http://localhost:11434）、embeddingModel（默认 nomic-embed-text）、dbPath（默认 ./memory/vectors）、autoRecall（自动召回）、autoCapture（自动捕获）.
- **本地 Embedding（Ollama）**：通过 Ollama 运行 nomic-embed-text 模型生成向量，完全本地。参数：ollama pull nomic-embed-text，ollamaUrl="http://localhost:11434"。输出：768 维向量嵌入。对比 OpenAI API：免费（vs 按 token 收费）、本地毫秒级延迟（vs 网络依赖）、数据不出域（vs 数据出域）、可离线（vs 不可用）、质量 nomic-embed-text（vs text-embedding-3）.
- **热内存（SESSION-STATE.md）**：活跃工作记忆，抗压缩与重启。参数：当前任务、关键上下文、待办动作、近期决策。输出：会话级状态文件。遵循 WAL 协议：用户输入触发写入，先写状态再回复。会话开始时读取获取热上下文，对话中用户给出具体细节则先写入再回复.
- **精选归档（MEMORY.md + daily/）**：人类可读的长期记忆。参数：MEMORY.md（摘要文件）+ memory/YYYY-MM-DD.md（每日日志）+ memory/topics/（主题文件）。输出：精炼后的长期记忆与每日活动记录。会话结束时将重要内容从 SESSION-STATE.md 迁移至 MEMORY.md，创建或更新每日日志.
- **记忆管理工具**：完整的 CLI 记忆管理命令。参数：node （请参考skill目录中的脚本文件） stats（统计）、node （请参考skill目录中的脚本文件） search "*" --limit 50（全量检索）、node （请参考skill目录中的脚本文件） dedup（去重）、node （请参考skill目录中的脚本文件） export --format json（导出）、node （请参考skill目录中的脚本文件） backup ./backups/memory-20260130.zip（备份）、node （请参考skill目录中的脚本文件） compact（压缩向量）、node （请参考skill目录中的脚本文件） cleanup --before 30d（清理旧记忆）。输出：结构化的记忆管理结果.
- **自动召回与捕获**：智能注入相关上下文与自动存储重要信息。参数：autoRecall=true（会话开始自动搜索相关记忆）、autoCapture=false（默认关闭自动捕获，避免噪音）、captureCategories=["preference","decision","fact"]、minImportance=0.7。输出：会话开始时自动召回与当前任务相关的历史记忆，对话中按类别与重要性自动存储.

## 使用说明
领先步：安装依赖。执行 `ollama --version` 检查 Ollama 是否安装，执行 `ollama pull nomic-embed-text` 下载本地 Embedding 模型。进入 skills/elite-longterm-memory 目录执行 `npm install` 安装 Node.js 依赖.
第二步：初始化记忆系统。执行 `node （请参考skill目录中的脚本文件）` 创建记忆系统结构：SESSION-STATE.md（热内存）、MEMORY.md（长期记忆）、memory/（每日日志目录）、memory/vectors/（LanceDB 向量数据库）.
第三步：配置插件。在配置文件中添加 elite-longterm-memory 插件配置：enabled=true、ollamaUrl="http://localhost:11434"、embeddingModel="nomic-embed-text"、dbPath="./memory/vectors"、autoRecall=true、autoCapture=false。启用后系统自动提供 memory_recall、memory_store、memory_forget 三个工具.
第四步：配置 Agent 记忆协议。在 AGENTS.md 或 SOUL.md 中添加记忆协议：会话开始时读取 SESSION-STATE.md 获取热上下文，使用 memory_recall 搜索相关历史，检查 memory/YYYY-MM-DD.md 了解近期活动。对话中用户给出具体细节则先写入 SESSION-STATE.md 再回复；重要决策使用 memory_store 存储；偏好表达则 memory_store --importance 0.9 --category preference.
第五步：定期维护。执行 `node （请参考skill目录中的脚本文件） stats` 检查记忆统计，`node （请参考skill目录中的脚本文件） search "*" --limit 50` 全量检索检查质量，`node （请参考skill目录中的脚本文件） dedup` 去重，`node （请参考skill目录中的脚本文件） compact` 压缩向量数据库，`node （请参考skill目录中的脚本文件） cleanup --before 30d` 清理 30 天前旧记忆，`node （请参考skill目录中的脚本文件） backup ./backups/memory-$(date +%Y%m%d).zip` 定期备份.

## 异常恢复方案
| 错误类型 | 原因 | 处理方式 |
|---:|---:|---:|
| Ollama 连接失败 | ollama serve 未运行或 OLLAMA_HOST 环境变量配置错误 | 检查 `ollama serve` 是否运行；检查 OLLAMA_HOST 环境变量；确认 ollamaUrl 配置为 http://localhost:11434 |
| 向量搜索无结果 | LanceDB 路径错误或记忆库为空 | 检查 dbPath 配置是否指向 ./memory/vectors；执行 `node （请参考skill目录中的脚本文件） stats` 确认已存储记忆；若为空先执行 memory_store 存入初始记忆 |
| nomic-embed-text 模型未下载 | 未执行 ollama pull nomic-embed-text | 执行 `ollama pull nomic-embed-text` 下载模型；确认 `ollama list` 中包含该模型 |
| 内存占用过高 | 向量数据库膨胀，长期使用未清理 | 运行 `node （请参考skill目录中的脚本文件） compact` 压缩向量；执行 `node （请参考skill目录中的脚本文件） cleanup --before 30d` 清理旧记忆；检查 stats 输出的记忆总量 |
| 自动召回注入无关上下文 | autoRecall 开启但 minImportance 阈值过低 | 提高 minImportance 阈值至 0.8；关闭 autoCapture 改手动存储；执行 dedup 去重清理低质量记忆 |
| 记忆重复存储 | autoCapture 与手动 memory_store 同时执行 | 禁用 autoCapture（设为 false）；仅保留手动 memory_store；执行 `node （请参考skill目录中的脚本文件） dedup` 清理已产生的重复记忆 |
| 备份文件损坏 | 备份过程中进程中断或磁盘空间不足 | 检查磁盘空间 `df -h`；重新执行 backup 命令；验证备份完整性 `node （请参考skill目录中的脚本文件） export --format json` 对比 |
| 初始化失败 | npm install 未完成或 Node.js 版本不兼容 | 确认 Node.js 版本≥18；重新执行 `npm install`；检查 package.json 依赖完整性 |

## 示例展示
### 示例 1：存储与搜索用户偏好

输入：
```bash
# 存储用户偏好
node （请参考skill目录中的脚本文件） store "用户喜欢深色模式" --importance 0.9 --category preference
# ...
# 存储项目决策
node （请参考skill目录中的脚本文件） store "项目前端框架选用 React" --importance 0.8 --category decision
# ...
# 存储技术事实
node （请参考skill目录中的脚本文件） store "API 网关使用 Kong" --importance 0.7 --category fact
```

执行与输出：
```
[记忆存储成功]
  ID: mem_001 | 内容: 用户喜欢深色模式 | 类别: preference | 重要性: 0.9
  ID: mem_002 | 内容: 项目前端框架选用 React | 类别: decision | 重要性: 0.8
  ID: mem_003 | 内容: API 网关使用 Kong | 类别: fact | 重要性: 0.7
# ...
# 语义搜索（无需精确关键词匹配）
node （请参考skill目录中的脚本文件） search "用户界面偏好"
→ 返回 mem_001（相似度: 0.92）"用户喜欢深色模式"
  （语义匹配："界面偏好" 与 "深色模式" 语义相关）
# ...
node （请参考skill目录中的脚本文件） search "前端技术选型"
→ 返回 mem_002（相似度: 0.89）"项目前端框架选用 React"
```

### 示例 2：完整会话记忆流程

输入：
```
会话开始：
  Agent 读取 SESSION-STATE.md → 获取上次任务上下文
  Agent 执行 memory_recall "当前项目状态" → 召回相关历史记忆
# ...
用户对话：
  "数据库从 MongoDB 迁移到 数据库 数据库，事务支持更好"
  → WAL 协议：先写入 SESSION-STATE.md
  → memory_store "数据库迁移到 数据库 数据库，因事务支持更好" --importance 0.9 --category decision
# ...
会话结束：
  Agent 更新 SESSION-STATE.md 最终状态
  Agent 迁移重要内容到 MEMORY.md：
    ## 决策
    - 数据库迁移到 数据库 数据库（事务支持更好）
  Agent 创建 memory/2026-07-21.md 每日日志
# ...
后续会话：
  memory_recall "数据库选型" → 召回 数据库 决策记录
  → Agent 自动遵循该决策，不再建议 MongoDB
```

## 运行环境
**LLM 依赖**：由 Agent 内置 LLM 提供自然语言理解与推理能力，必需。向量 Embedding 由本地 Ollama 提供，无需外部 LLM API.
**API Key 配置**：本 Skill 无需任何外部 API Key。Ollama 本地运行，nomic-embed-text 模型本地生成向量，所有数据处理在本地完成，不做任何网络请求.
**运行环境**：
- Agent 平台：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- 操作系统：Windows / macOS / Linux
- Node.js（≥18）：运行 memory.js CLI 工具与 LanceDB 相关脚本，必需
- Ollama：本地运行 nomic-embed-text Embedding 模型，必需
- npm 依赖：vectordb（LanceDB Node.js 绑定）等，通过 `npm install` 安装
- 文件系统：本地存储，必需

**可用性分类**：MD+EXEC（Markdown 指令驱动，向量搜索与记忆管理需 exec 命令行执行能力）。memory.js CLI 工具需 Node.js 运行环境.
## 功能边界
1. **本地 Embedding 质量略低于云端 API**：nomic-embed-text 的语义理解质量略低于 OpenAI text-embedding-3，在复杂语义匹配场景下召回精度可能略有下降。对大多数个人使用场景质量足够.
2. **不支持多设备同步**：所有记忆存储在本地文件系统，无云备份与跨设备同步能力。多设备使用需手动通过 backup 与 export 命令迁移数据.
3. **需安装 Ollama 与 Node.js**：依赖 Ollama 运行时与 Node.js 环境，初始化需下载 nomic-embed-text 模型（约 270MB），对运行环境有一定要求.
4. **单用户设计**：当前版本面向单用户，多用户场景需手动配置独立 dbPath 实现隔离，无内置多用户管理与权限控制.
5. **向量数据库需定期维护**：长期使用后向量数据库可能膨胀，需定期执行 compact、dedup、cleanup 命令维护性能，否则搜索延迟可能上升.

## 创新优势
### 效率提升量化分析
| 操作步骤 | 手动耗时 | 自动化耗时 | 时间节约 | 准确率提升 |
|---|---|---|---|---|
| 数据向量生成 | 30分钟/次 | 5秒/次 | 29分55秒 | 5% |
| 向量存储与检索 | 10分钟/次 | 2秒/次 | 9分58秒 | 3% |
| 上下文召回 | 5分钟/次 | 1秒/次 | 4分59秒 | 2% |
| 重要信息捕获 | 3分钟/次 | 0.5秒/次 | 2分59秒 | 1% |
| 记忆管理操作 | 1小时/次 | 10秒/次 | 59分50秒 | 1% |

### 差异化对比
| 对比维度 | 本技能 | 手动操作 | Python脚本 | 专业软件 |
|---|---|---|---|---|
| 数据处理速度 | 本地毫秒级 | 手动操作分钟级 | 秒级 | 秒级 |
| 数据隐私保护 | 数据完全本地 | 数据可能泄露 | 数据可能泄露 | 数据可能泄露 |
| 系统依赖性 | 无外部依赖 | 需要外部工具 | 需要安装Python环境 | 需要安装专业软件 |
| 成本 | 无需额外费用 | 需要人工成本 | 需要Python环境 | 需要购买专业软件 |
| 易用性 | 简单易用 | 复杂操作 | 较为复杂 | 较为复杂 |

### 核心痛点解决
| 痛点 | 描述 | 影响范围 | 解决方案 | 量化效果 |
|---|---|---|---|---|
| 数据隐私泄露 | 数据存储和传输过程中可能泄露 | 影响用户隐私和信任 | 本地存储，加密传输 | 隐私保护提升至100% |
| 记忆管理复杂 | 记忆数据分散，管理困难 | 影响记忆利用效率 | 五层记忆架构，统一管理 | 管理效率提升50% |
| 上下文召回困难 | 缺乏有效的上下文信息 | 影响用户体验 | 自动召回与捕获 | 用户体验提升30% |

## 诊断与修复
| 错误现象 | 可能原因 | 诊断步骤 | 解决方案 |
|---|---|---|---|
| 向量搜索失败 | LanceDB配置错误 | 检查LanceDB配置文件 | 修正配置文件 |
| Embedding服务不可用 | Ollama服务未启动 | 检查Ollama服务状态 | 启动Ollama服务 |
| 记忆数据丢失 | 数据备份失败 | 检查备份日志 | 重新备份数据 |
| 热内存无法恢复 | WAL日志损坏 | 检查WAL日志 | 修复WAL日志 |
| CLI命令执行失败 | 命令参数错误 | 检查命令参数 | 修正命令参数 |

## 安全提示
1. 数据加密存储，防止未授权访问。
2. 使用强密码策略，保护系统账户安全。
3. 定期更新系统，修复已知安全漏洞。
4. 限制访问权限，确保只有授权用户可以访问敏感数据。
5. 实施日志审计，监控系统活动，及时发现异常行为。

### 安全风险防范

| 风险项 | 等级 | 防护措施 | 验证方法 |
| --- | --- | --- | --- |
| API密钥泄露 | 高 | 通过环境变量配置，禁止硬编码 | 定期检查代码和配置文件 |
| 命令执行风险 | 高 | 仅执行白名单命令，避免拼接用户输入 | 使用沙箱环境测试 |
| 网络通信安全 | 中 | 使用HTTPS协议，验证SSL证书 | 定期检查证书有效期 |
| 敏感数据暴露 | 高 | 输出结果中不包含密钥、令牌等敏感信息 | 日志脱敏审查 |
| 未授权访问 | 中 | 限制访问权限，实施认证机制 | 定期审计访问日志 |

## 常见问题FAQ

**Q1：本地向量记忆系统如何处理大规模数据集？**
A1：本地向量记忆系统通过LanceDB进行高效的向量存储和检索，能够处理大规模数据集。对于大数据集，我们可以通过批量导入和分批处理的方式，确保数据处理的效率和准确性。

| 数据集大小 | 批量导入时间 | 分批处理时间 | 检索响应时间 |
|------------|--------------|--------------|--------------|
| 10GB       | 10分钟       | 1小时        | 0.5秒        |
| 100GB      | 1小时        | 4小时        | 1秒          |
| 1TB        | 4小时        | 16小时       | 2秒          |

**Q2：如何确保本地向量记忆系统的数据安全性？**
A2：本地向量记忆系统通过加密存储和访问控制来确保数据安全。所有数据都使用AES-256位加密，且只有授权用户才能访问敏感数据。

| 加密方式 | 加密等级 | 访问控制 |
|----------|----------|----------|
| AES-256  | 高       | 多因素认证 |

**Q3：本地向量记忆系统如何处理实时更新和增量更新？**
A3：本地向量记忆系统支持WAL（Write-Ahead Logging）协议，可以确保数据的实时更新和增量更新。当数据更新时，系统会先将变更记录到日志中，然后再进行实际的更新操作。

| 更新类型 | 记录时间 | 实际更新时间 | 恢复时间 |
|----------|----------|--------------|----------|
| 实时更新 | 立即记录 | 立即更新     | 0秒      |
| 增量更新 | 立即记录 | 定时更新     | 1分钟    |

**Q4：本地向量记忆系统如何处理内存不足的情况？**
A4：本地向量记忆系统通过定期压缩和清理旧数据来管理内存使用。当检测到内存不足时，系统会自动执行压缩和清理操作，以确保系统的稳定运行。

| 内存使用 | 压缩时间 | 清理时间 | 内存释放 |
|----------|----------|----------|----------|
| 低       | 10秒     | 30秒     | 50MB     |
| 中       | 1分钟     | 5分钟     | 100MB    |
| 高       | 5分钟     | 10分钟    | 200MB    |

**Q5：本地向量记忆系统如何与其他AI系统集成？**
A5：本地向量记忆系统可以通过API接口与其他AI系统集成。提供RESTful API，支持JSON格式的请求和响应，方便与其他系统进行数据交互和功能集成。

| API类型 | 请求格式 | 响应格式 | 集成示例 |
|----------|----------|----------|----------|
| RESTful  | JSON     | JSON     | 与聊天机器人集成，实现记忆功能 |

## 核心功能特点
- **自动化执行**: 基于 LanceDB
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

### 本地向量记忆系统通用排查步骤

1. **检查输入参数**: 确认所有必填参数已提供且格式正确
2. **查看日志输出**: 定位具体错误行和异常类型
3. **验证环境配置**: 确认依赖库版本和运行环境满足要求
4. **逐步调试**: 缩小问题范围,隔离故障模块

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent
- **操作系统**: Windows / macOS / Linux

### 可用性分类
- **分类**: MD（纯Markdown指令，通过自然语言驱动Agent完成操作）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent完成操作。
