---
slug: "file-auto-organizer"
name: "file-auto-organizer"
version: 1.0.1
displayName: "File Auto Organizer"
summary: "文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。。文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。Use when 需要文件处理、文档"
license: "Proprietary"
description: |-
  文件自动整理工具。按文件类型、日期自动归类下载文件夹，适合整理控和洁癖用户。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解.
tags:
  - Other
  - 工具
  - 效率
  - bash
  - python3
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# File Auto Organizer

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

* 📂 按文件类型自动归类（图片、文档、视频、压缩包等）
* 📅 按日期整理（今天、昨天、本周等）
* 🔍 支持自定义规则
* 🗑️ 可选：删除重复文件
* 📊 整理报告
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文件操作 | 文件路径与操作参数 | 操作结果与文件元信息 |
| 文件自动整理工具 | 目标数据与配置参数 | 处理结果与执行状态 |
| 按文件类型 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 整理下载文件夹

```bash
python3 （请参考skill目录中的脚本文件） organize ~/Downloads
```

### 按类型整理

```bash
python3 （请参考skill目录中的脚本文件） by-type ~/Downloads
```

### 按日期整理

```bash
python3 （请参考skill目录中的脚本文件） by-date ~/Downloads
```

### 查看统计

```bash
python3 （请参考skill目录中的脚本文件） stats ~/Downloads
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | file-auto-organizer处理的内容输入 |,  |
| content | string | 否 | file-auto-organizer处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "organizer 相关配置参数",
    result: "organizer 相关配置参数",
    result: "organizer 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 案例展示

```bash
python3 （请参考skill目录中的脚本文件） organize ~/Desktop
# ...
python3 （请参考skill目录中的脚本文件） organize ~/Downloads --report
```

## 常见问题

### Q1: 如何开始使用File Auto Organizer？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

