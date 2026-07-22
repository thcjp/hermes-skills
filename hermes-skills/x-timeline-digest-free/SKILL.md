---
name: "x-timeline-digest-free"
description: "使用 bird 读取 X/Twitter 时间线,增量去重后输出结构化 JSON,不含中文分类简报"
license: MIT
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "X 时间线摘要免费版"
  version: "1.0.0"
  summary: "使用 bird 读取 X/Twitter 时间线,增量去重后输出结构化 JSON,不含中文分类简报"
  tags:
    - "通用办公"
    - "Social Media"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
---

# X Timeline Digest Free

## 概述

本 Skill 通过 bird 命令行工具读取 X/Twitter 的 For You 与 Following 两条时间线,
对推文进行增量过滤与去重,输出结构化 JSON。
免费版聚焦于基础的数据拉取与去重,不包含中文简报、排序修剪与启发式降噪。

本 Skill 仅负责数据生成,不处理投递通道。

---

## 配置

配置从 `skills.entries["x-timeline-digest-free"].config` 读取。

| 名称 | 类型 | 默认值 | 说明 |
| --- | --- | --- | --- |
| intervalHours | number | 6 | 增量窗口小时数 |
| fetchLimitForYou | number | 100 | For You 拉取条数 |
| fetchLimitFollowing | number | 60 | Following 拉取条数 |
| similarityThreshold | number | 0.9 | 近重复相似度阈值 |
| statePath | string | ~/.skill-platform/state/x-timeline-digest-free.json | 状态文件路径 |

---

## 依赖

- bird 已安装并可在 PATH 中调用
- bird 已通过 cookie 完成登录认证
- Node.js 运行时
- 只读使用

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

### 时间线拉取
- For You:`bird home -n 100 --json`
- Following:`bird home --following -n 60 --json`

**输入**: 用户提供时间线拉取所需的指令和必要参数。
**处理**: 按照skill规范执行时间线拉取操作,遵循单一意图原则。
**输出**: 返回时间线拉取的执行结果,包含操作状态和输出数据。### 增量过滤
读取 statePath 中的 lastRunAt,仅保留该时间点之后发布的推文。

**输入**: 用户提供增量过滤所需的指令和必要参数。
**输出**: 返回增量过滤的执行结果,包含操作状态和输出数据。### 去重
- 硬去重:按推文 ID 唯一化
- 近重复合并:基于文本相似度合并内容相近的推文

---

**输入**: 用户提供去重所需的指令和必要参数。
**处理**: 按照skill规范执行去重操作,遵循单一意图原则。
**输出**: 返回去重的执行结果,包含操作状态和输出数据。
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`x-timeline-digest-free`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 使用方式

执行摘要生成脚本,获得去重后的 JSON:

```bash
node skills/x-timeline-digest-free/digest.js
```

输出可直接落盘供下游脚本或工具二次处理。

---

## 输出结构

```json
{
  "window": {
    "start": "2026-02-01T00:00:00+08:00",
    "end": "2026-02-01T06:00:00+08:00",
    "intervalHours": 6
  },
  "counts": {
    "forYouFetched": 100,
    "followingFetched": 60,
    "afterIncremental": 34,
    "afterDedup": 26
  },
  "items": [
    {
      "id": "123456",
      "author": "@handle",
      "createdAt": "2026-02-01T02:15:00+08:00",
      "text": "推文正文",
      "url": "https://x.com/handle/status/123456",
      "sources": ["following"]
    }
  ]
}
```

---

## 案例

### 案例:定时拉取与归档

将脚本接入定时任务,每 6 小时执行一次,
把输出的 items 数组追加到本地归档文件,
作为 X 动态的原始数据沉淀,供后续按需检索与分析。

### 案例:降噪阅读

手动执行脚本获取去重后的 JSON,
按 createdAt 排序后集中阅读,
避免 For You 与 Following 的重叠内容反复出现。

---

## 异常处理


### bird 未安装

执行报 command not found。
执行 `which bird` 检查路径,未安装时先完成安装。

### bird 登录态过期

返回认证失败或空结果。
执行 bird 登录子命令重新完成 cookie 认证后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令。

### statePath 不可写

无法写入状态文件导致 lastRunAt 不更新,下次运行会重复处理。
检查 statePath 所在目录是否存在且有写权限。

### 拉取条数为 0

forYouFetched 与 followingFetched 均为 0。
确认 bird 登录态有效,执行ping命令测试网络连通性,检查防火墙和代理设置连通性,
账号被限流时拉长 intervalHours 后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令。

### 近重复阈值过高

similarityThreshold 过高导致内容相近的转发各自保留。
下调阈值到 0.8 观察合并效果。

---

## 常见问题

### 免费版包含中文简报吗?

不包含。免费版仅输出基础去重 JSON,
中文分类简报、排序修剪与启发式降噪属于付费版能力。

### 状态文件被删除会怎样?

sentTweetIds 丢失后,已推送过的推文会在下次运行时再次进入结果。
建议将 statePath 设置在有备份的目录。

### intervalHours 可以设得很小吗?

默认 6 小时适合多数节奏。
低于 2 小时会导致增量过滤效果减弱、重复率上升。

### 支持列表与搜索吗?

不支持。本 Skill 仅处理 For You 与 Following 两条时间线。

---

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 依赖 bird 命令行工具
- 不包含中文分类简报,需下游自行处理
- 不包含排序修剪与启发式降噪
- 仅处理 For You 与 Following 两条时间线
- 投递通道不在范围内
- bird 登录态过期需要人工重新认证

---

## 升级提示

需要中文分类简报、排序修剪与启发式降噪?
需要按 AI、加密、观点等主题分组的高信号阅读体验?
升级到付费版 x-timeline-digest,获得完整的智能简报能力与多阶段过滤管道。
