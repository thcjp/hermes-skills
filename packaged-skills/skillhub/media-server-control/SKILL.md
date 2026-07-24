---
slug: "media-server-control"
name: "media-server-control"
version: "1.3.0"
displayName: "Jellyfin Control"
summary: "控Jellyfin媒体服务器与TV,搜索/续播/管会话。Control Jellyfin media server and TV。Search content, resume playbac"
license: "Proprietary"
description: |-
  Control Jellyfin media server and TV。Search content, resume playback,
  manage sessions, control T。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写.
tags:
  - Research
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - 创意
  - 图像
  - control
  - json
  - env
  - http
  - jellyfin
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"
---
# Jellyfin Control

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

- Media Server Control 结果导出 - 生成生成内容
- Media Server Control 实时监控 - 遵循专业风格规范
- Media Server Control 错误重试 - 支持多种变体等多种变体
- Media Server Control 多格式支持 - 自动适配多种场景
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 搜索检索 | 关键词与过滤条件 | 匹配结果与相关性排序 |
| 控Jellyfin媒 | 目标数据与配置参数 | 处理结果与执行状态 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### Minimal setup (Jellyfin only, no TV control)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://YOUR_IP:8096",
          "JF_API_KEY": "your-api-key-here",
          "JF_USER": "your-username"
        }
      }
    }
  }
}
```

### With Home Assistant (recommended for TV control)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_API_KEY": "your-jellyfin-api-key",
          "JF_USER": "victor",
          "HA_URL": "http://192.168.1.138:8123",
          "HA_TOKEN": "your-ha-long-lived-token",
          "HA_TV_ENTITY": "media_player.lg_webos_tv_oled48c34la",
          "TV_MAC": "AA:BB:CC:DD:EE:FF"
        }
      }
    }
  }
}
```

### Direct WebOS (LG TV, no Home Assistant needed)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_API_KEY": "your-jellyfin-api-key",
          "JF_USER": "victor",
          "TV_IP": "192.168.1.100",
          "TV_MAC": "AA:BB:CC:DD:EE:FF"
        }
      }
    }
  }
}
```

> **First time with WebOS direct:** The TV will show a pairing prompt. Accept it and save the `TV_CLIENT_KEY` the skill prints — add it to your env to skip the prompt next time.

### Direct ADB (Android TV / Fire TV / Chromecast with Google TV, no HA needed)

```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_API_KEY": "your-jellyfin-api-key",
          "JF_USER": "victor",
          "ADB_DEVICE": "192.168.1.100:5555",
          "TV_MAC": "AA:BB:CC:DD:EE:FF"
        }
      }
    }
  }
}
```

> **First time with ADB:** Enable Developer Options on your TV (Settings → About → tap Build Number 7 times), then enable Network/USB debugging. First connection will show "Allow debugging?" on the TV — accept it. Requires `adb` installed on the Skill平台 host (`sudo apt install adb`).

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | media-server-control处理的内容输入 |,  |
| content | string | 否 | media-server-control处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "control 相关配置参数",
    result: "control 相关配置参数",
    result: "control 相关配置参数",
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

### 示例1：基础用法

```
### Minimal setup (Jellyfin only, no TV control)(补充)
# ...
```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://YOUR_IP:8096",
          "JF_API_KEY": "your-api-key-here",
          "JF_USER": "your-username"
        }
      }
    }
  }
}
```
# ...
### With Home Assistant (recommended for TV control)(补充)
# ...
```json
{
  "skills": {
    "entries": {
      "jellyfin-control": {
        "env": {
          "JF_URL": "http://192.168.1.50:8096",
          "JF_AP
```
# ...
## 常见问题
# ...
### Q1: 如何开始使用Jellyfin Control？
A: 
# ...
### Q2: 遇到错误怎么办？
A: 
# ...
### Q3: Jellyfin Control有什么限制？
A: 
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...