---
slug: "generate-mindmap"
name: "generate-mindmap"
version: 1.0.4
displayName: "Generate Mindmap"
summary: "生成基于认知科学方法论的交互式思维导图。支持 Markdown 大纲或 JSON 输入，一条命令同时导出 HTML（可交互编辑、8 种布局、深浅双主题）、PNG、JPG、SVG、PDF、XMin..."
license: "MIT"
description: |-
  生成基于认知科学方法论的交互式思维导图。支持 Markdown 大纲或 JSON 输入，一条命令同时导出 HTML（可交互编辑、8 种布局、深浅双主题）、PNG、JPG、SVG、PDF、XMin。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解.
tags:
  - Knowledge
  - 工具
  - 效率
  - 知识
  - mindmap
  - json
  - generate
  - markdown
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# Generate Mindmap

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Generate Mindmap一条命令同时导出 | 不支持 | 支持 |
| Generate Mindmap可交互编辑 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

- 生成基于认知科学方法论的交互式思维导图
- 支持 Markdown 大纲或 JSON 输入，一条命令同时导出 HTML（可交互编辑、8 种布局、深浅双主题）、PNG、JPG、SVG、PDF、XMin
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 交互响应 | 事件与回调数据 | 响应状态与交互结果 |
| 命令执行 | 指令名与参数 | 执行结果与输出日志 |
| PDF处理 | PDF文件与操作类型 | 提取文本或生成文档 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

**优秀步**：按 [内容设计方法](#%E5%86%85%E5%AE%B9%E8%AE%BE%E8%AE%A1%E5%9B%9B%E6%AD%A5%E6%B3%95) 提炼结构，写入一个 Markdown 大纲文件（避免把内容塞进 shell 参数——引号和特殊字符会出问题）：

```bash
cat > /tmp/mindmap_outline.md << 'EOF'
# ...
#
## 输入格式
# ...
**Markdown 大纲**（首选，见上）。**JSON**（需要精确控制时）：
# ...
```json
{
  "central": "核心洞见",
  "branches": [
    {"label": "🔬 维度一", "color": "#4A90D9",
     "children": ["证据A", {"label": "证据B", "children": ["事实1", "事实2"]}]}
  ]
}
```
# ...
JSON 也通过 `--data-file` 传入（自动识别 JSON / Markdown）；`--data-file -` 读 stdin；`--data '...'` 仅限极短内容。主分支若缺 emoji，脚本会按语义关键词自动补充.
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    result: "mindmap 相关配置参数",
    result: "mindmap 相关配置参数",
    result: "mindmap 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```
# ...
输出模板参考: `assets/output.json`
# ...
## 异常处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 
# ...
## 依赖说明
# ...
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
# ...
### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
# ...
### API Key 配置
- 
# ...
### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,
# ...
# ...
**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示
# ...
`{baseDir}/examples/`：`ai_trends.html`、`product_launch.html`、`python_learning.html`（可直接用浏览器打开体验交互与主题切换），以及对应 `.json` 数据和 `outline_example.md` 大纲示例.
# ...
## 常见问题
# ...
### Q1: 如何开始使用Generate Mindmap？
A: 
# ...
### Q2: 遇到错误怎么办？
A: 
# ...
### Q3: Generate Mindmap有什么限制？
A: 
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|:---------|---------:|:---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...