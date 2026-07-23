---
slug: ai-kujiale-design
name: ai-kujiale-design
version: "0.0.6"
displayName: ai-kujiale-design
summary: 室内智能设计skill，分步式对话完成户型确认→风格选择→布局确认→渲染出图。
license: MIT-0
description: |-
  室内智能设计skill，分步式对话完成户型确认→风格选择→布局确认→渲染出图。核心能力:

  - 创意设计领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 内容创作、设计生成、多媒体制作

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Creative
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# ai-kujiale-design

## 说明

必须严格根据本文档流程来执行，不能自作主张发散。

## 初始化配置

首次使用需在项目根目录创建 `.kjlconfig.json` 文件（参考 `.kjlconfig-example.json`），配置 access_token。
若无 token，引导用户访问 <https://www.kujiale.com/skills> 生成并保存 `.kjlconfig.json`，key 是access_token，value
是用户复制的值，`.kjlconfig.json`要保存在`.kjlconfig-example.json`同一目录下。

## Token 读取

所有脚本调用前，先从 `.kjlconfig.json` 读取 access_token字段作为 token：

## 版本校验

每次执行前调用：`node ./scripts/versionCheck.js --token=${token} --version=0.0.6`

* action=1：继续
* action=2：提示"版本已过时，建议更新"
* action=3：终止，提示"版本已废弃，需重新安装"

## 输出规则

* 进度反馈通过 `message(action=send)` 发送
* 最终结果只输出渲染图、全景图和设计亮点，最终结果要严格按照./outputs/result.md输出
* 已发送的消息不重复输出

---

## 分步流程

### 阶段1：户型获取与确认

**触发条件**：用户提到要做室内设计/装修设计

**步骤1.1**：询问户型来源

> "请问您有户型信息吗？
>
> * 输入小区名搜索户型
> * 或直接上传户型图"

**路径A：文字搜索户型**

**步骤1.2a**：询问城市

> "请问房子在哪个城市？"

**步骤1.3a**：询问小区

> "请问是哪个小区？户型信息（几室几厅、面积）也可以一起告诉我。"

**步骤1.4a**：搜索户型

```text
node ./scripts/searchPlan.js --token=<token> --query=<小区名> --areaId=<城市id> --start=0 --num=20
```

展示结果让用户选择：

> "找到以下户型，请回复数字选择：
>
> 1. {小区名} {面积}㎡ {户型结构}
> 2. ..."

用户选择后获得 planId。

**步骤1.5a**：获取户型图并展示给用户确认

```text
node ./scripts/getFloorplanInfo.js --planId=<planId>
```

解析返回结果：

* 若 `floorplanInfos` 为空数组：提示"户型图获取失败，请重新选择或上传户型图"，返回步骤1.4a
* 若有数据：取 `floorplanInfos[0].planImage` 展示给用户，直接展示图片

> "户型已生成，请查看户型图：
> [展示 planImage 图片]
> 面积：{realArea}㎡
> 请确认是否满意？
>
> * 回复「确认」继续创建方案
> * 回复「重新生成」重新搜索户型
> * 回复「上传图片」改为上传户型图"

等待用户回复：

* 若用户确认满意 → 进入步骤1.6创建方案
* 若用户不满意 → 根据用户选择重新执行路径A或路径B

**路径B：上传户型图**

同时监听 `~\.skill-platform\media\inbound` 是否有新图片（每5秒检查）。

**步骤1.2b**：识别户型图
检测到图片后：

> "检测到您上传了图片，正在识别户型..."

**步骤1.3b**：上传图片

```text
node ./scripts/getUploadToken.js --token=<token>
```

按 ./docs/upload.md 执行上传获取 url。

**步骤1.4b**：创建临摹任务

```text
node ./scripts/createBitmapTask.js --token=<token> --bitmap=<url>
```

轮询结果：

```text
node ./scripts/getBitmapTaskResult.js --token=<token> --taskId=<taskId>
```

获得 planId。

**步骤1.5b**：获取户型图并展示给用户确认

```text
node ./scripts/getFloorplanInfo.js --planId=<planId>
```

解析返回结果：

* 若 `floorplanInfos` 为空数组：提示"户型图识别失败，请重新上传或搜索户型"，返回步骤1.2b
* 若有数据：取 `floorplanInfos[0].planImage` 展示给用户

> "户型已识别生成，请查看户型图：
> [展示 planImage 图片]
> 面积：{realArea}㎡
> 请确认是否满意？
>
> * 回复「确认」继续创建方案
> * 回复「重新生成」重新上传户型图
> * 回复「搜索户型」改为文字搜索"

等待用户回复：

* 若用户确认满意 → 进入步骤1.6创建方案
* 若用户不满意 → 根据用户选择重新执行路径A或路径B

**步骤1.6**：创建方案（两种路径合并）

```text
node ./scripts/createDesign.js --token=<token> --planId=<planId>
```

获得 designId。

**步骤1.7**：确认户型

> "已确认户型：{户型信息}，接下来选择您喜欢的风格～"

---

### 阶段2：风格选择（标签+硬装风格）

**触发条件**：户型已确认

**步骤2.1**：获取标签并展示选项

```text
node ./scripts/getTags.js --token=<token>
```

解析返回的标签列表，展示给用户：

> "请选择您的偏好：（单选，回复数字如'1'）
>
> 1. {标签项1名称}
> 2. {标签项2名称}
> 3. ...
>    或直接描述您的喜好"

用户选择后获得 tagItemIds 列表。

**步骤2.2**：查询硬装风格

```text
node ./scripts/getStyles.js --token=<token> --tagItemIds=<id1,id2,...>
```

**步骤2.3**：风格选择

* 若返回多个风格：展示封面图让用户选择

> "以下硬装风格可选，请回复数字选择："
> 展示每个风格的 coverUrl 图片 + styleName，如果非Webchat渠道，直接展示图片

* 若返回单个风格：默认选择

> "已为您匹配{风格名}风格"

获得 styleId，进入下一阶段。

---

### 阶段3：布局生成与确认

**触发条件**：风格已确认。

**步骤3.1**：跟用户确认本次布局会消耗他账号内的智能布局的额度/核豆，需要用户确认知晓后再执行后续步骤

**步骤3.2**：使用 message(action=send) 发送"开始布局，请稍等"

**步骤3.3**：触发智能布局

```text
node ./scripts/triggerLayout.js --token=<token> --designId=<designId> --tagIds=<id1,id2,...> --styleId=<styleId> --applyDecorationStyle=true --buildCeiling=true --autoDesign=true
```

**步骤3.4**：等待并查询布局结果

```text
node ./scripts/getLayoutResult.js --token=<token> --designId=<designId>
```

若 c!=0 则每10秒重复查询。

**步骤3.5**：展示布局结果并等待用户确认
使用 message(action=send) 发送布局信息：

> "布局已生成！以下是各房间的布局情况：
>
> * {房间名1}：{家具列表}
> * {房间名2}：{家具列表}
>   ...
>   直接进入阶段4渲染出图

---

### 阶段4：渲染出图

**触发条件**：布局已确认

**步骤4.1**：使用 message(action=send) 发送："开始渲染，请稍等"

**步骤4.2**：触发渲染

```text
node ./scripts/trigger-render.js --obsDesignId=<designId> --xToken=<token>
```

发送：`"正在生成效果图，预计几分钟..."`

**步骤4.3**：等待10秒后查询渲染结果

```text
node ./scripts/getRenderResult.js --token=<token> --designId=<designId>
```

提取 pictype=0 的 img（渲染图）和 pictype=1 的 panoLink（全景图）。若空则每分钟重试，超5分钟反馈失败。

**步骤4.4**：输出最终结果
发送：`"效果图已生成！"`
严格按 ./outputs/result.md 格式输出：

* 设计亮点（根据第一张渲染图总结）
* 渲染图（按房间优先级：客餐厅→主卧→次卧→其他）
* 全景图链接
* 方案详情链接（[https://www.kujiale.com/pcenter/design/{designId}/setting?from=skills）](https://www.kujiale.com/pcenter/design/%7BdesignId%7D/setting?from=skills%EF%BC%89)

---

## 渠道规则

* Webchat：直接发送图片链接
* 飞书：推送格式 `MEDIA:图片url`，即直接展示图片

## 结果排序

客餐厅 → 主卧 → 次卧 → 其他

## 接口文档

* 户型搜索：./docs/planSearch.md
* 户型图信息：./docs/floorplanInfo.md
* 生成方案：./docs/createDesign.md
* 硬装风格库：./docs/hardStyle.md
* 客户标签：./docs/customTag.md
* 智能布局：./docs/layout.md
* 布局结果：./docs/layoutResult.md
* 布局候选：./docs/layoutCandidates.md
* 渲染结果：./docs/renderResult.md
* 上传：./docs/upload.md
* 临摹导入：./docs/planUrlCreate.md
* 临摹轮询：./docs/planUrlCreateResult.md
* 版本校验：./docs/versionCheck.md

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 室内智能设计skill，分步式对话完成户型确认→风格选择→布局确认→渲染出图
- 触发关键词: 风格选择, skill, 布局确认, 室内智能设计, 成户型确认, kujiale, design, ai-kujiale-design

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用ai-kujiale-design？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: ai-kujiale-design有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
