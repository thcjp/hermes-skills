---
slug: "plugin-architecture"
name: "plugin-architecture"
version: 1.0.2
displayName: "插件UI架构"
summary: "为SkillHub安装UI插件架构，使插件可注册自定义视图与导航标签。"
license: "Proprietary"
description: |-
  插件UI架构为SkillHub（OpenClaw）安装UI插件注册支持，使插件可在Control仪表板侧边栏
  注册自定义UI视图/标签。支持registerView API注册，包含id、label、subtitle、icon、
  group、position等配置项，可指定Chat、Control、Agent、Settings导航分组.
  提供Installation安装指令与Reference参考代码文件.
tags:
  - Other
  - 插件
  - UI架构
  - 通用办公
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# Plugin Architecture — 插件UI架构

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 插件UI架构处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |
| 商用版权授权 | 不支持 | 支持 |
| 多版本对比与A/B优选 | 不支持 | 支持 |

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

### UI视图注册（registerView API）

插件可通过 `api.registerView()` 函数在Control仪表板侧边栏注册自定义UI视图/标签。注册时需提供id（唯一标识）、label（显示名称）、subtitle（描述文字）、icon（图标名称）、group（导航分组）、position（组内排序）.
```typescript
// 在插件的 register() 函数中：
if (typeof api.registerView === "function") {
  api.registerView({
    id: "my-view",
    label: "My View",
    subtitle: "Description here",
    icon: "database",
    group: "Agent",
    position: 5,
  });
}
```- 验证返回数据的完整性和格式正确性
- 参考`UI视图注册（registerView API）`的配置文档进行参数调优
### 导航分组集成（Navigation Group Integration）
注册的视图通过group字段指定所属导航分组，支持四个分组：Chat（聊天）、Control（控制）、Agent（代理）、Settings（设置）。position字段控制视图在组内的显示顺序.
**输入**: 用户提供导航分组集成（Navigation Group Integration）所需的指令和必要参数.
**处理**: 解析导航分组集成（Navigation Group Integration）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回导航分组集成（Navigation Group Integration）的处理结果,包含执行状态码、结果数据和执行日志。### 图标系统配置（Icon System）
通过icon字段指定视图图标，使用图标集中的图标名称（如 `database`、`settings`、`chat` 等）。图标名称需匹配Control仪表板内置图标集.
**输入**: 用户提供图标系统配置（Icon System）所需的指令和必要参数.
**输出**: 返回图标系统配置（Icon System）的处理结果,包含执行状态码、结果数据和执行日志。### 安装流程（Installation Process）
此技能需要由SkillHub agent手动安装。安装步骤：

1. 将技能解压到skills文件夹
2. 给agent发送安装指令，引用 `INSTALL_INSTRUCTIONS.md`
3. agent读取 `INSTALL_INSTRUCTIONS.md` 并逐步执行安装

```text
Please install the plugin-architecture skill. Read the INSTALL_INSTRUCTIONS.md file in the skill folder and follow it step by step.
```

**输入**: 用户提供安装流程（Installation Process）所需的指令和必要参数.
**输出**: 返回安装流程（Installation Process）的处理结果,包含执行状态码、结果数据和执行日志。### 参考代码文件（Reference Files）
技能包含以下文件供参考：
- `SKILL.md` — 技能说明文件
- `INSTALL_INSTRUCTIONS.md` — agent逐步安装指令
- `reference/` — 参考代码文件，展示需要添加的代码

**输入**: 用户提供参考代码文件（Reference Files）所需的指令和必要参数.
**处理**: 解析参考代码文件（Reference Files）的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回参考代码文件（Reference Files）的处理结果,包含执行状态码、结果数据和执行日志.
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`plugin-architecture`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

## 示例

### 基本用法

向Agent发送指令:

```
使用 插件UI架构 处理以下任务:
[具体任务描述]
```

### 输出说明

Agent将根据指令调用对应能力,返回响应数据。响应格式取决于具体能力点的输出定义.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| `api.registerView` 未定义 | 插件架构未安装 | 先安装plugin-architecture技能，确认 `INSTALL_INSTRUCTIONS.md` 已执行 |
| `registerView` 参数缺失 | 必填字段未提供 | 确保提供id、label、group等必填字段 |
| 视图未显示在侧边栏 | group值无效 | 使用Chat/Control/Agent/Settings之一 |
| 图标不显示 | icon名称不匹配 | 使用Control仪表板内置图标集中的有效名称 |
| 安装后视图重复 | 重复注册相同id | 确保每个视图使用唯一id |
| `INSTALL_INSTRUCTIONS.md` 未找到 | 技能文件不完整 | 重新解压技能，确认所有文件存在 |
| `reference/` 目录缺失 | 技能包损坏 | 重新下载或解压技能包 |
| TypeScript类型错误 | api类型定义未导入 | 参考 `reference/` 中的类型定义文件 |

## FAQ

### 如何开始使用？

阅读使用流程章节,按步骤配置环境和参数后即可开始使用。首次使用建议先阅读依赖说明章节确认环境就绪.
### 遇到错误怎么办？

查看错误处理章节,对照错误场景找到对应的处理方式。如错误处理章节未覆盖,收集错误信息后通过已知限制章节了解skill能力边界.
## 已知限制

- 仅支持在SkillHub Control仪表板中注册UI视图
- 需要手动安装，不支持自动安装
- 图标仅限Control仪表板内置图标集
- 导航分组固定为Chat/Control/Agent/Settings四个
- 依赖agent正确执行 `INSTALL_INSTRUCTIONS.md` 中的步骤
