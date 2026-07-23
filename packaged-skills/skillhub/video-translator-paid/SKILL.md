---
slug: "video-translator-paid"
name: "video-translator-paid"
version: "1.0.0"
displayName: "视频翻译-专业版"
summary: "企业级视频翻译与配音平台，支持8种语言、双语字幕、批量翻译、语音克隆与优先队列，适合跨国内容本地化。"
license: "Proprietary"
edition: "pro"
description: |-
  视频翻译专业版。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Creative
  - 视频翻译
  - 多语言
  - 专业版
  - 批量处理
  - 语音克隆
  - 企业级
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# 视频翻译-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 基础功能 | 支持 | 支持 |
| 高级配置 | 不支持 | 支持 |
| 自动化处理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

### 1. 多语言翻译支持
专业版支持 8 种源语言，目标语言覆盖中英：

| 源语言 | 代码 | 目标语言选项 |
|:-------|:-----|:-------------|
| 英文 | en | zh |
| 中文 | zh | en |
| 韩文 | ko | zh / en |
| 日文 | ja | zh / en |
| 法文 | fr | zh / en |
| 俄文 | ru | zh / en |
| 西班牙文 | es | zh / en |
| 德文 | de | zh / en |

**输入**: 用户提供多语言翻译支持所需的指令和必要参数。
**处理**: 按照skill规范执行多语言翻译支持操作,遵循单一意图原则。
**输出**: 返回多语言翻译支持的执行结果,包含操作状态和输出数据。- 验证执行结果，确认输出符合预期格式
- 参考`任务优先级队列`相关配置参数进行设置
### 2. 双语字幕烧录
支持原文与译文同时显示：

- 上方原文，下方译文（标准布局）
- 左右分栏布局（适合教学场景）
- 自定义字幕样式（字体/颜色/位置）
- 双语对照便于学习

**输入**: 用户提供双语字幕烧录所需的指令和必要参数。
**处理**: 按照skill规范执行双语字幕烧录操作,遵循单一意图原则。
**输出**: 返回双语字幕烧录的执行结果,包含操作状态和输出数据。

### 3. 批量翻译处理
支持单任务翻译 50+ 视频：

```text
输入视频清单（CSV/JSON）
      ↓
任务调度器分配并行翻译
      ↓
多翻译进程并行执行
      ↓
翻译队列管理（优先级调度）
      ↓
失败重试 + 结果聚合
      ↓
生成翻译报告
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量翻译处理` 选项
- 处理流程: 接收输入 -> 执行批量翻译处理 -> 返回结果
- 输入: 用户提供批量翻译处理所需的参数和指令
- 输出: 返回批量翻译处理的执行结果,包含操作状态和输出数据

### 4. 语音克隆
保留原视频说话人的音色特征：

- 提取原视频音色特征
- 使用克隆音色进行目标语言配音
- 保留语调与情感
- 适合访谈、演讲、教程类视频

**输入**: 用户提供语音克隆所需的指令和必要参数。
**处理**: 按照skill规范执行语音克隆操作,遵循单一意图原则。
**输出**: 返回语音克隆的执行结果,包含操作状态和输出数据。

### 5. 翻译记忆库与术语表
**翻译记忆库：**

- 自动记录已翻译片段
- 相同内容自动复用（节省 API 调用）
- 支持跨项目共享

**术语表：**

- 自定义专业术语翻译映射
- 保障术语一致性
- 支持多领域术语表（科技/医疗/法律等）

**输入**: 用户提供翻译记忆库与术语表所需的指令和必要参数。
**输出**: 返回翻译记忆库与术语表的执行结果,包含操作状态和输出数据。

### 6. 任务优先级队列
```text
任务提交
   ↓
优先级评估（紧急/高/中/低）
   ↓
翻译队列排序
   ↓
并行翻译（按配额限制）
   ↓
进度监控 + 失败重试
   ↓
结果通知
```- 验证执行结果，确认输出符合预期格式
- 参考`任务优先级队列`相关配置参数进行设置
#
## 适用场景

### 场景 1：跨国企业培训视频本地化
某跨国企业需要将英文培训视频本地化为中文版本，并保留讲师原音色。

**操作步骤：**

1. 告诉 Agent：「把这批英文培训视频翻译成中文，使用语音克隆保留讲师音色」
2. 提供视频清单与术语表
3. Agent 提交批量翻译任务，开启语音克隆
4. 任务完成后返回预览链接与质量报告

**示例配置 `batch-translate.json`：**

> 详细代码示例已移至 `references/detail.md`

**执行命令：**

```bash
python3 batch_translate.py --config /path/to/batch-translate.json --parallel 8
```

### 场景 2：教育平台多语言课程制作
某在线教育平台需要将中文课程翻译为英文、日文、韩文三种语言版本，并显示双语字幕便于学习。

**多语言配置 `multilingual.yaml`：**

> 详细代码示例已移至 `references/detail.md`

**执行命令：**

```bash
python3 batch_translate.py --config /path/to/multilingual.yaml --parallel 6
```

### 场景 3：影视作品出海字幕与配音
某影视公司需要将中文纪录片翻译为英文版本，同时提供双语字幕版本供学习使用。

**操作步骤：**

1. 告诉 Agent：「把这个纪录片翻译成英文，需要两个版本：纯英文配音版 和 中英双语字幕版」
2. Agent 生成两个变体任务
3. 并行处理两个版本
4. 输出报告对比

**示例配置：**

> 详细代码示例已移至 `references/detail.md`

## 使用流程

### 优秀步：环境检查
```bash
python3 --version

curl --version
jq --version
```

### 第二步：配置 API Key
```bash
export VIDEO_TRANSLATE_SERVICE_API_KEY="your_api_key_here"

curl -s 'https://audiox-api-global.luoji.cn/video-trans/health' \
  -H "Authorization: Bearer $VIDEO_TRANSLATE_SERVICE_API_KEY"
```

### 第三步：提交多语言翻译任务
```bash
curl -s -X POST 'https://audiox-api-global.luoji.cn/video-trans/orchestrate' \
  -H "Authorization: Bearer $VIDEO_TRANSLATE_SERVICE_API_KEY" \
  -F 'video=@/path/to/korean-video.mp4' \
  -F 'sourceLanguage=ko' \
  -F 'targetLanguage=zh' \
  -F 'show=true' \
  -F 'bilingual=false'
```

### 第四步：提交双语字幕任务
```bash
curl -s -X POST 'https://audiox-api-global.luoji.cn/video-trans/orchestrate' \
  -H "Authorization: Bearer $VIDEO_TRANSLATE_SERVICE_API_KEY" \
  -F 'video=@/path/to/japanese-video.mp4' \
  -F 'sourceLanguage=ja' \
  -F 'targetLanguage=en' \
  -F 'show=true' \
  -F 'bilingual=true'
```

### 第五步：批量翻译
```bash
python3 batch_translate.py \
  --config /tmp/batch-translate.json \
  --parallel 8 \
  --voice-clone \
  --report /tmp/translation-report.json
```

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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要稳定网络连接（访问翻译服务）
- **磁盘**：建议预留 10GB+（翻译记忆库与缓存）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:-------|:-----|:---------|:---------|:---------|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| curl | 命令行工具 | 必需 | 系统自带 | 任意版本 |
| jq | JSON 处理 | 可选 | 系统包管理器 | 1.6+ |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令
```bash
pip3 install requests pyyaml

python3 --version
python3 -c "import requests; print('requests ready')"
curl --version
```

### API Key 配置
专业版需要以下 API Key：

| API 类型 | 环境变量 | 用途 | 获取方式 |
|:---------|:---------|:-----|:---------|
| 翻译服务 | `VIDEO_TRANSLATE_SERVICE_API_KEY` | 视频翻译 API 调用 | `https://luoji.cn` |
| 语音克隆 | `VOICE_CLONE_API_KEY` | 语音克隆服务（可选） | 对应语音克隆服务商 |

```bash
export VIDEO_TRANSLATE_SERVICE_API_KEY="your_translation_api_key"
export VOICE_CLONE_API_KEY="your_voice_clone_key"

curl -s 'https://audiox-api-global.luoji.cn/video-trans/health' \
  -H "Authorization: Bearer $VIDEO_TRANSLATE_SERVICE_API_KEY"
```

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用翻译 API 完成多语言视频翻译
- **离线可用**：否（依赖在线翻译服务）
- **隐私等级**：中（视频需上传至翻译服务，记忆库本地存储）
- **企业部署**：支持私有化部署翻译记忆库

## 案例展示

### 完整配置文件模板

> 详细代码示例已移至 `references/detail.md`

### 术语表示例

> 详细代码示例已移至 `references/detail.md`

### 任务队列管理
```bash
python3 queue_manager.py status --queue /tmp/translate-queue.json

python3 queue_manager.py priority --task-id task-001 --level urgent

python3 queue_manager.py pause --queue /tmp/translate-queue.json
```

## 常见问题

### Q1：专业版与免费版 API Key 是否通用？
**A：** 完全通用。专业版与免费版使用相同的 API Key 与服务地址，专业版扩展的是客户端能力（批量、多语言、语音克隆等）。

### Q2：语音克隆效果不理想怎么办？
**A：** 优化建议：

1. 提供更长的纯净人声样本（建议 60 秒以上）
2. 确保样本音质清晰（采样率 44.1kHz 以上）
3. 避免背景音乐干扰
4. 单人视频克隆效果优秀

### Q3：批量翻译中部分视频失败怎么办？
**A：** 专业版自动记录失败任务：

```bash
python3 batch_translate.py --retry-failed /tmp/translate-queue.json

python3 batch_translate.py --resume /tmp/translate-queue.json
```

### Q4：双语字幕布局如何自定义？
**A：** 通过配置文件自定义：

```yaml
subtitle:
  bilingual: true
  layout: "stacked"    # stacked（上下）/ side-by-side（左右）
  original_position: "top"
  translated_position: "bottom"
```

### Q5：翻译记忆库如何跨项目共享？
**A：** 专业版支持记忆库导入导出：

```bash
python3 memory_manager.py export --project A --output /data/memory-a.json

python3 memory_manager.py import --project B --file /data/memory-a.json
```

### Q6：API 调用配额如何管理？
**A：** 专业版提供配额监控：

```bash
python3 quota_manager.py status

python3 quota_manager.py set --project "培训本地化" --limit 10000
```

### Q7：术语表支持哪些格式？
**A：** 支持 JSON、CSV、XLSX 三种格式：

```bash
python3 glossary_manager.py import --file /data/terms.csv --format csv
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步
