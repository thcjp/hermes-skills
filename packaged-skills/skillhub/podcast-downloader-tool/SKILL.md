---
slug: "podcast-downloader-tool"
name: "podcast-downloader-tool"
version: "1.0.0"
displayName: "Podcast Downloader"
summary: "小宇宙播客下载工具。从小宇宙(xiaoyuzhoufm.com)下载播客音频和Show Notes。自动转换为MP3格式（兼容Sanag、小游等骨传导蓝牙耳机、水下游泳时离线播放）。当用户需要下..."
license: "Proprietary"
description: |-
  小宇宙播客下载工具。从小宇宙(xiaoyuzhoufm
tags:
  - Creative
  - 播客
  - 音频
  - 媒体
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# Podcast Downloader

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Podcast Downloader自动转换 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |

## 核心能力

- 从小宇宙(xiaoyuzhoufm
- com)下载播客音频和Show Notes
- 自动转换为MP3格式（兼容Sanag、小游等骨传导蓝牙耳机、水下游泳时离线播放）
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 音频生成 | 文本与语音参数 | 音频文件与时长信息 |
| 小宇宙播客下载工具 | 目标数据与配置参数 | 处理结果与执行状态 |
| 从小宇宙 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

```bash
（请参考skill目录中的脚本文件） "https://www.xiaoyuzhoufm.com/episode/abc123def456ghi789jklmno"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | podcast-downloader-tool处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```text
/Users/zym/Documents/podcast/  # Baidu cloud sync directory
└── PodcastName-EpisodeTitle/
    ├── EpisodeTitle.mp3
    └── EpisodeTitle.md
```

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

### 示例1：基础用法

```
```bash
（请参考skill目录中的脚本文件） "https://www.xiaoyuzhoufm.com/episode/abc123def456ghi789jklmno"
```
```

## 常见问题

### Q1: 如何开始使用Podcast Downloader？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

