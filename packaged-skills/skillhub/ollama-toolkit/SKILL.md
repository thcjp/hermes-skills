---
slug: "ollama-toolkit"
name: "ollama-toolkit"
version: "1.0.0"
displayName: "Ollama工具箱(专业版)"
summary: "全功能本地Ollama AI模型管理工具，支持多轮对话、自定义模型、批量推理与API集成"
license: "Proprietary"
edition: "pro"
description: |-
  Ollama工具箱专业版是面向团队和高级用户的完整本地AI模型管理方案，在免费版基础上解锁多轮对话会话管理、Modelfile自定义模型创建、批量文件推理处理、REST API集成、性能资源监控和模型对比评估等全部高级能力。核心能力：多轮上下文对话、自定义模型构建与微调、批量文件推理与结果聚合、HTTP API服务集成、GPU/CPU/内存实时监控、多模型横向对比评估、提示词模板管理、流式输出处理
tags:
  - 本地AI
  - 模型管理
  - 批量推理
  - 高级集成
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Ollama工具箱(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| :--------- | 不支持 | 支持 |
| :----- | 不支持 | 支持 |
| 模型管理 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 专业版支持 | 说明 |
|:---------|:-----------|:-----|
| 模型管理 | 支持 | 列表、拉取、删除、详情查看 |
| 单轮推理 | 支持 | 命令行直接推理、管道输入、文件输入 |
| 多轮对话 | 支持 | 交互式会话、上下文保持、历史管理 |
| 自定义模型 | 支持 | Modelfile创建、参数微调、系统提示词设置 |
| 批量推理 | 支持 | 文件批量处理、结果聚合、并行执行 |
| REST API | 支持 | HTTP接口调用、流式输出、JSON响应 |
| 参数配置 | 支持 | 温度、上下文、GPU层、停止词等全参数 |
| 性能监控 | 支持 | GPU/CPU/内存使用率、推理耗时统计 |
| 模型对比 | 支持 | 多模型同任务横向对比评估 |
| 提示词模板 | 支持 | 预设模板管理和复用 |
### 能力模块

执行能力模块操作,处理用户输入并返回结果。

**输入**: 用户提供能力模块所需的参数和指令。

**输出**: 返回能力模块的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 模型管理

执行模型管理操作,处理用户输入并返回结果。

**输入**: 用户提供模型管理所需的参数和指令。

**输出**: 返回模型管理的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`模型管理`相关配置参数进行设置
### 单轮推理

执行单轮推理操作,处理用户输入并返回结果。

**输入**: 用户提供单轮推理所需的参数和指令。

**输出**: 返回单轮推理的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`单轮推理`相关配置参数进行设置
#
## 适用场景

### 开发者场景：API集成与流式输出

将Ollama作为后端AI服务集成到应用中，通过REST API实现流式对话和结构化输出：

```bash
# 启动API服务
ollama serve

# 通过API调用模型（流式输出）
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:7b",
  "prompt": "用Python实现快速排序",
  "stream": true
}'

# 通过API进行对话（带上下文）
curl http://localhost:11434/api/chat -d '{
  "model": "qwen2.5:7b",
  "messages": [
    {"role": "user", "content": "什么是设计模式？"},
    {"role": "assistant", "content": "设计模式是..."},
    {"role": "user", "content": "举例说明工厂模式"}
  ],
  "stream": false
}'
```

### 运维场景：批量文档处理

对大量文档执行批量摘要或分类，结果自动聚合输出：

```bash
# 批量处理目录下的所有文本文件
for file in docs/*.txt; do
  echo "=== 处理: $file ==="
  cat "$file" | ollama run qwen2.5:7b "提取关键要点，用JSON格式输出" --format json
  echo ""
done > results.json

# 并行处理（利用后台任务）
for file in docs/*.txt; do
  (cat "$file" | ollama run qwen2.5:7b "一句话摘要" > "summaries/$(basename $file).summary") &
done
wait
echo "批量处理完成"
```

### 研究场景：模型对比评估

对同一任务使用不同模型进行推理，横向对比输出质量：

```bash
# 定义测试提示词
PROMPT="解释什么是RESTful API，给出三个设计原则"

# 使用不同模型执行同一任务
echo "=== Qwen2.5 7B ===" 
ollama run qwen2.5:7b "$PROMPT" --temperature 0.3

echo "=== LLaMA3.2 ==="
ollama run llama3.2 "$PROMPT" --temperature 0.3

echo "=== Gemma2 ==="
ollama run gemma2 "$PROMPT" --temperature 0.3
```

### 定制场景：自定义模型构建

通过Modelfile创建具有预设系统提示词和参数的定制模型：

```bash
# 创建Modelfile
cat > MyAssistant.modelfile << 'EOF'
FROM qwen2.5:7b

# 系统提示词
SYSTEM """
你是一个专业的技术文档助手。回答时遵循以下规则：
1. 使用中文回答
2. 代码示例附带注释
3. 结构化输出，使用标题和列表
"""

# 参数配置
PARAMETER temperature 0.3
PARAMETER num_ctx 8192
PARAMETER top_p 0.9
PARAMETER stop "<|im_end|>"
EOF

# 从Modelfile创建自定义模型
ollama create my-assistant -f MyAssistant.modelfile

# 运行自定义模型
ollama run my-assistant "解释微服务架构"
```

## 使用流程

### 前置条件

1. 已安装Ollama（从官网下载安装包）
2. Ollama服务正在运行
3. 建议配备独立GPU（NVIDIA 8GB+显存或Apple Silicon）

### 依赖说明

### 运行环境

4. **Agent平台**：支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
5. **操作系统**：Windows / macOS / Linux
6. **硬件要求**：8GB+内存（3b模型），16GB+内存（7b模型），推荐独立GPU
7. **GPU驱动**：NVIDIA CUDA 11+（NVIDIA显卡）/ Metal（Apple Silicon）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Ollama | 运行时 | 必需 | 从Ollama官网下载安装 |
| 开源模型 | 模型文件 | 必需 | 通过`ollama pull`从仓库下载 |
| curl | 命令行工具 | 可选 | API调用场景需要，系统通常自带 |
| NVIDIA驱动 | 驱动程序 | 可选 | GPU加速需要，从NVIDIA官网安装 |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

8. 本Skill基于Ollama本地运行，无需任何API Key
9. Ollama服务默认监听`localhost:11434`，无需认证
10. 局域网部署时建议通过防火墙限制访问来源，Ollama本身不提供内置认证机制
11. 如需认证层，建议在反向代理（如Nginx）中配置API Key验证

### 可用性分类

12. **分类**：MD+EXEC（纯Markdown指令，需要exec命令行执行能力）
13. **说明**：基于Markdown的AI Skill，通过自然语言指令驱动Agent执行Ollama全量命令行和API操作

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
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


| 症状 | 可能原因 | 解决方案 | 优先级 |
|:-----|:---------|:---------|:-------|
| 模型拉取失败 | 网络问题或仓库不可达 | ，或使用镜像源 | 高 |
| 推理时显存溢出 | 模型过大或并发过多 | 换小模型或降低并发数 | 高 |
| API连接拒绝 | Ollama服务未启动 | 执行`ollama serve`启动服务 | 高 |
| 输出乱码 | 模板或停止词配置错误 | 检查Modelfile的TEMPLATE和stop参数 | 中 |
| 响应缓慢 | GPU层设置过低或CPU推理 | 增加`--num-gpu`值或换用更小模型 | 中 |
| 自定义模型创建失败 | Modelfile语法错误 | 检查FROM、SYSTEM、PARAMETER格式 | 中 |
| 批量处理结果缺失 | 部分请求超时或失败 | 记录失败项，降低并发后 | 中 |
| 多轮对话上下文断裂 | messages数组不完整 | 确保传递完整对话历史 | 低 |
| JSON输出格式错误 | 模型未严格遵循格式 | 在提示词中强调JSON结构要求 | 低 |
| 模型删除后磁盘未释放 | 模型文件残留 | 检查`~/.ollama/models`目录手动清理 | 低 |

## 依赖说明

| 依赖项 | 类型 | 必需 | 说明 |
|--------|------|------|------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 多轮对话管理

```bash
# 启动交互式会话（支持多轮对话）
ollama run qwen2.5:7b

# 会话内使用 / 命令
# /bye        退出会话
# /show info  显示模型信息
# /show system 显示系统提示词
# /set parameter temperature 0.5  调整参数
# /save session.json  保存会话

# 通过API实现多轮对话（保留上下文）
curl http://localhost:11434/api/chat -d '{
  "model": "qwen2.5:7b",
  "messages": [
    {"role": "system", "content": "你是一个Python专家"},
    {"role": "user", "content": "如何读取CSV文件？"}
  ],
  "stream": false,
  "options": {"temperature": 0.3}
}'
```

### 自定义模型进阶

```bash
# 带模板和参数的完整Modelfile
cat > CodeReviewer.modelfile << 'EOF'
FROM qwen2.5:7b

PARAMETER temperature 0.2
PARAMETER num_ctx 8192
PARAMETER top_p 0.9
PARAMETER top_k 40
PARAMETER repeat_penalty 1.1

SYSTEM """
你是一个严格的代码审查专家。对提供的代码进行以下分析：
1. 安全漏洞检查
2. 性能问题识别
3. 代码风格建议
4. 改进方案提供
输出格式使用Markdown，每个问题标注严重程度（高/中/低）。
"""

TEMPLATE """相关信息<|im_start|>system
相关信息<|im_end|>
相关信息相关信息<|im_start|>user
相关信息<|im_end|>
相关信息<|im_start|>assistant
处理结果<|im_end|>
"""
EOF

# 创建模型
ollama create code-reviewer -f CodeReviewer.modelfile

# 使用自定义模型审查代码
cat app.py | ollama run code-reviewer
```

### REST API完整集成

```bash
# 生成文本（非流式）
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:7b",
  "prompt": "写一首关于编程的诗",
  "stream": false,
  "options": {
    "temperature": 0.8,
    "num_predict": 200
  }
}'

# 对话接口（流式）
curl http://localhost:11434/api/chat -d '{
  "model": "qwen2.5:7b",
  "messages": [{"role": "user", "content": "你好"}],
  "stream": true
}'

# 列出所有模型（API方式）
curl http://localhost:11434/api/tags

# 获取模型信息
curl http://localhost:11434/api/show -d '{"name":"qwen2.5:7b"}'

# 创建模型（API方式）
curl http://localhost:11434/api/create -d '{
  "name": "my-model",
  "modelfile": "FROM qwen2.5:7b\nSYSTEM \"你是助手\""
}'

# 删除模型（API方式）
curl -X DELETE http://localhost:11434/api/delete -d '{"name":"my-model"}'
```

### 批量推理与结果聚合

```bash
# 批量分类处理
for file in emails/*.txt; do
  result=$(cat "$file" | ollama run qwen2.5:7b "将此邮件分类为：咨询/投诉/建议/其他，只输出分类名称")
  echo "$(basename $file)|$result" >> classification.csv
done

# 批量摘要并生成报告
echo "# 文档摘要报告" > summary.md
echo "" >> summary.md
for file in docs/*.md; do
  echo "## $(basename $file)" >> summary.md
  cat "$file" | ollama run qwen2.5:7b "用3句话总结核心内容" >> summary.md
  echo "" >> summary.md
done

# 并行批量处理（控制并发数）
find docs/ -name "*.txt" | xargs -P 4 -I {} sh -c 'cat "{}" | ollama run qwen2.5:7b "摘要" > "{}.summary"'
```

### 全参数配置

```bash
# 完整参数列表
ollama run qwen2.5:7b \
  --temperature 0.3 \
  --num-ctx 8192 \
  --num-predict 500 \
  --top-p 0.9 \
  --top-k 40 \
  --repeat-penalty 1.1 \
  --num-gpu 35 \
  --seed 42 \
  "回答问题"

# 通过API传递参数
curl http://localhost:11434/api/generate -d '{
  "model": "qwen2.5:7b",
  "prompt": "生成随机数",
  "options": {
    "temperature": 0.3,
    "num_ctx": 8192,
    "num_predict": 500,
    "top_p": 0.9,
    "top_k": 40,
    "repeat_penalty": 1.1,
    "seed": 42
  }
}'
```

### 性能监控

```bash
# 查看正在运行的模型及资源占用
ollama ps

# 监控GPU使用率（NVIDIA）
nvidia-smi -l 1

# 监控Ollama进程资源
top -p $(pgrep ollama)

# 统计推理耗时
time ollama run qwen2.5:7b "生成100字摘要" > /dev/null

# 测量不同模型的响应延迟
for model in qwen2.5:0.5b qwen2.5:3b qwen2.5:7b; do
  echo -n "$model: "
  { time ollama run $model "你好" > /dev/null; } 2>&1 | grep real
done
```

### 提示词模板管理

```bash
# 创建提示词模板目录
mkdir -p ~/.ollama/templates

# 保存常用提示词模板
cat > ~/.ollama/templates/summary.txt << 'EOF'
请总结以下文本的核心要点，按重要性排序输出：
1. 提取3-5个关键信息
2. 每个信息用一句话概括
3. 标注信息来源段落

文本内容：
（根据实际场景填充）
EOF

# 使用模板进行推理
cat 文档.txt | ollama run qwen2.5:7b "$(cat ~/.ollama/templates/summary.txt)"
```

## 常见问题

### Q1: 多轮对话时上下文丢失？

确保通过API的`messages`数组传递完整对话历史，或在交互模式中保持在同一会话内。`/save`命令可保存当前会话上下文。

### Q2: Modelfile创建模型失败？

检查Modelfile语法：`FROM`行指定基础模型（需已拉取），`SYSTEM`和`TEMPLATE`使用三引号包裹多行内容，`PARAMETER`使用`键 值`格式。

### Q3: 批量推理时部分请求失败？

通常是显存不足导致。降低并发数（`xargs -P 2`），或使用`--num-gpu`限制GPU层数。失败的请求可记录后重试。

### Q4: API调用返回连接拒绝？

确保Ollama服务正在运行（`ollama serve`）。默认监听`localhost:11434`，如需远程访问设置`OLLAMA_HOST=0.0.0.0:11434`。

### Q5: 流式输出如何在前端处理？

API返回的是逐行JSON（每行一个`{"response":"字","done":false}`对象），前端按行解析并追加显示，直到`"done":true`。

### Q6: 自定义模型的TEMPLATE参数怎么写？

TEMPLATE使用Go模板语法，`相关信息`插入系统提示词，`相关信息`插入用户输入，`处理结果`插入模型输出。不同基础模型的模板格式不同，建议先`ollama show --template 基础模型名`查看默认模板。

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

使用`--format json`参数（命令行）或在API中设置`"format": "json"`。模型会尝试输出合法JSON，但建议在提示词中也明确要求JSON格式并描述结构。

### Q8: 不同模型的停止词不同？

各模型的停止词（stop token）不同。通过`ollama show 模型名`查看默认配置，在Modelfile中用`PARAMETER stop "停止词"`自定义。

### Q9: 如何评估模型在特定任务上的表现？

设计标准化测试集，对每个模型执行相同任务，比较输出的准确性、完整性和耗时。建议使用固定`seed`和低`temperature`确保评估公平性。

### Q10: GPU显存如何优化分配？

通过`--num-gpu`控制加载到GPU的层数。显存充足时全部加载（速度快），显存不足时部分加载到CPU（速度慢但不溢出）。7b模型约需5GB显存全量加载。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

