---
slug: "jellyfin-control"
name: "jellyfin-control"
version: "1.3.0"
displayName: "Jellyfin Control"
summary: "Control Jellyfin media server and TV. Search content, resume playback, manage"
license: "MIT"
description: |-
  Control Jellyfin media server and TV。Search content, resume playback,
  manage sessions, control T。Use when 需要生成营销文案、写作内容、标题优化、内容创作时使用。不适用于纯技术文档撰写。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Research
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# Jellyfin Control

## 核心能力

- （根据实际场景填充） - 生成生成内容
- （根据实际场景填充） - 遵循专业风格规范
- （根据实际场景填充） - 支持多种变体等多种变体
- （根据实际场景填充） - 自动适配多种场景
### 指令解析与执行

解析用户指令,执行核心操作并返回处理结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`指令解析与执行`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`指令解析与执行`相关配置参数进行设置
### 数据处理与转换

处理输入数据,执行转换操作并输出结果。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`数据处理与转换`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`数据处理与转换`相关配置参数进行设置
### 结果验证与输出

验证处理结果的正确性,格式化输出并返回给用户。

**输入**: 用户提供操作指令和必要参数。

**输出**: 返回操作执行的结果。

- 执行`结果验证与输出`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`结果验证与输出`相关配置参数进行设置
### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: Control、Jellyfin、media、server、Search、content、resume、playback、manage、sessions、Use、需要生成营销文案、写作内容、标题优化、内容创作时使用、不适用于纯技术文、档撰写、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

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

### 命令参数说明

1. `-ha-long-lived-token`: 命令参数,用于指定操作选项
2. `-jellyfin-api-key`: 命令参数,用于指定操作选项

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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
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
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法

```
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
          "JF_AP
```

## 常见问题

### Q1: 如何开始使用Jellyfin Control？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Jellyfin Control有什么限制？
A: 

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
