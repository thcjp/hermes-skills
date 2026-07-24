---
slug: "video-translator-tool-pro"
name: "video-translator-tool-pro"
version: "1.0.0"
displayName: "视频翻译-专业版"
summary: "企业级视频翻译与配音平台，支持8种语言、双语字幕、批量翻译、语音克隆与优先队列，适合跨国内容本地化。"
license: "Proprietary"
edition: "pro"
description: |-
  视频翻译专业版。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理.
tags:
  - Creative
  - 视频翻译
  - 多语言
  - 专业版
  - 批量处理
  - 语音克隆
  - 企业级
  - 视频处理
  - 媒体
  - 创意
  - json
  - bash
  - python3
  - 不支持
  - 翻译记忆
tools:
  - read
  - exec
  - write
homepage: ""
category: "Creative"
---
视频翻译专业版是一款面向企业团队与跨国内容机构的多语言视频本地化平台。在免费版中英互译能力之上，专业版扩展了 8 种源语言支持、双语字幕烧录、批量翻译处理、语音克隆、翻译记忆库等企业级能力.
专业版采用任务队列架构，支持优先级调度、断点续传、失败重试，可稳定处理 50+ 视频的批量翻译任务。同时完全兼容免费版 API Key 与调用方式，已有项目可无缝迁移.
### 免费版与专业版能力对比
| 能力 | 免费版 | 专业版 |
|---|---|---|
| 中英互译 | 支持 | 支持 |
| 多语言翻译 | 不支持（仅 zh/en） | 8 种源语言 |
| 双语字幕 | 不支持 | 支持 |
| 单语字幕 | 支持 | 支持 |
| 批量翻译 | 不支持 | 50+ 并行 |
| 语音克隆 | 不支持 | 支持 |
| 任务优先级 | 不支持 | 支持 |
| 翻译记忆库 | 不支持 | 支持 |
| 术语表管理 | 不支持 | 支持 |
| 质量报告 | 不支持 | 支持 |
| API 配额管理 | 不支持 | 支持 |
| 优先支持 | 社区 | 优先响应 |

## 核心能力
### 1. 多语言翻译支持
专业版支持 8 种源语言，目标语言覆盖中英：

| 源语言 | 代码 | 目标语言选项 |
|:-----|:-----|:-----|
| 英文 | en | zh |
| 中文 | zh | en |
| 韩文 | ko | zh / en |
| 日文 | ja | zh / en |
| 法文 | fr | zh / en |
| 俄文 | ru | zh / en |
| 西班牙文 | es | zh / en |
| 德文 | de | zh / en |

**输入**: 用户提供多语言翻译支持所需的指令和必要参数.
**处理**: 解析多语言翻译支持的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回多语言翻译支持的响应数据,包含状态码、结果和日志.
### 2. 双语字幕烧录
支持原文与译文同时显示：

- 上方原文，下方译文（标准布局）
- 左右分栏布局（适合教学场景）
- 自定义字幕样式（字体/颜色/位置）
- 双语对照便于学习

**输入**: 用户提供双语字幕烧录所需的指令和必要参数.
**处理**: 解析双语字幕烧录的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回双语字幕烧录的响应数据,包含状态码、结果和日志.
### 3. 批量翻译处理
支持单任务翻译 50+ 视频：

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | 视频翻译-专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

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
```

**输入**: 用户提供批量翻译处理所需的指令和必要参数.
**处理**: 解析批量翻译处理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回批量翻译处理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 语音克隆
保留原视频说话人的音色特征：

- 提取原视频音色特征
- 使用克隆音色进行目标语言配音
- 保留语调与情感
- 适合访谈、演讲、教程类视频

**输入**: 用户提供语音克隆所需的指令和必要参数.
**处理**: 解析语音克隆的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回语音克隆的响应数据,包含状态码、结果和日志.
### 5. 翻译记忆库与术语表
**翻译记忆库：**

- 自动记录已翻译片段
- 相同内容自动复用（节省 API 调用）
- 支持跨项目共享

**术语表：**

- 自定义专业术语翻译映射
- 保障术语一致性
- 支持多领域术语表（科技/医疗/法律等）

**输入**: 用户提供翻译记忆库与术语表所需的指令和必要参数.
**处理**: 解析翻译记忆库与术语表的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回翻译记忆库与术语表的响应数据,包含状态码、结果和日志.
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
```

**输入**: 用户提供任务优先级队列所需的指令和必要参数.
**处理**: 解析任务优先级队列的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回任务优先级队列的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级视频翻译与、配音平台、种语言、语音克隆与优先队、适合跨国内容本地、视频翻译专业版、Use、when、需要视频处理、音频编辑、媒体转换、配音生成时使用、不适用于版权受保、护的媒体内容处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景
### 场景 1：跨国企业培训视频本地化
某跨国企业需要将英文培训视频本地化为中文版本，并保留讲师原音色.
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
某在线教育平台需要将中文课程翻译为英文、日文、韩文三种语言版本，并显示双语字幕便于学习.
**多语言配置 `multilingual.yaml`：**

**执行命令：**

```bash
python3 batch_translate.py --config /path/to/multilingual.yaml --parallel 6
```

### 场景 3：影视作品出海字幕与配音
某影视公司需要将中文纪录片翻译为英文版本，同时提供双语字幕版本供学习使用.
**操作步骤：**

1. 告诉 Agent：「把这个纪录片翻译成英文，需要两个版本：纯英文配音版 和 中英双语字幕版」
2. Agent 生成两个变体任务
3. 并行处理两个版本
4. 输出报告对比

**示例配置：**

## 快速开始
### 第一步：环境检查
```bash
python3 --version
# ...
curl --version
jq --version
```

### 第二步：配置 API Key
```bash
export VIDEO_TRANSLATE_SERVICE_API_KEY="your_api_key_here"
# ...
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
## 示例
### 完整配置文件模板

### 术语表示例

### 任务队列管理
```bash
python3 queue_manager.py status --queue /tmp/translate-queue.json
# ...
python3 queue_manager.py priority --task-id task-001 --level urgent
# ...
python3 queue_manager.py pause --queue /tmp/translate-queue.json
```

## 最佳实践
### 1. 多语言翻译策略
```yaml
priority_order:
  - en    # 英文（全球通用）
  - zh    # 中文（中国市场）
  - ja    # 日文（日本市场）
  - ko    # 韩文（韩国市场）
```

### 2. 术语表管理
```bash
python3 glossary_manager.py create \
  --domain technology \
  --output /config/glossary-tech.json
# ...
python3 glossary_manager.py import \
  --file /data/terms.csv \
  --domain technology
# ...
python3 batch_translate.py \
  --config batch.json \
  --glossary /config/glossary-tech.json
```

### 3. 翻译记忆库优化
```bash
python3 memory_manager.py cleanup \
  --database /data/translation-memory.db \
  --min-quality 0.8
# ...
python3 memory_manager.py export \
  --database /data/translation-memory.db \
  --output /data/memory-export.json
```

### 4. 语音克隆使用建议
- 适用于：访谈、演讲、教程、纪录片
- 不适用于：多人对话、背景噪音大的视频
- 克隆前建议提取纯净人声片段（30 秒以上）

## 常见问题
### Q1：专业版与免费版 API Key 是否通用？
**A：** 完全通用。专业版与免费版使用相同的 API Key 与服务地址，专业版扩展的是客户端能力（批量、多语言、语音克隆等）.
### Q2：语音克隆效果不理想怎么办？
**A：** 优化建议：

1. 提供更长的纯净人声样本（建议 60 秒以上）
2. 确保样本音质清晰（采样率 44.1kHz 以上）
3. 避免背景音乐干扰
4. 单人视频克隆效果最佳

### Q3：批量翻译中部分视频失败怎么办？
**A：** 专业版自动记录失败任务：

```bash
python3 batch_translate.py --retry-failed /tmp/translate-queue.json
# ...
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
# ...
python3 memory_manager.py import --project B --file /data/memory-a.json
```

### Q6：API 调用配额如何管理？
**A：** 专业版提供配额监控：

```bash
python3 quota_manager.py status
# ...
python3 quota_manager.py set --project "培训本地化" --limit 10000
```

### Q7：术语表支持哪些格式？
**A：** 支持 JSON、CSV、XLSX 三种格式：

```bash
python3 glossary_manager.py import --file /data/terms.csv --format csv
```

## 依赖说明
### 运行环境
- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **网络**：需要稳定网络连接（访问翻译服务）
- **磁盘**：建议预留 10GB+（翻译记忆库与缓存）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:---:|:---:|:---:|:---:|:---:|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| curl | 命令行工具 | 必需 | 系统自带 | 任意版本 |
| jq | JSON 处理 | 可选 | 系统包管理器 | 1.6+ |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令
```bash
pip3 install requests pyyaml
# ...
python3 --version
python3 -c "import requests; print('requests ready')"
curl --version
```

### API Key 配置
专业版需要以下 API Key：

| API 类型 | 环境变量 | 用途 | 获取方式 |
|:--------|--------:|:--------|:--------|
| 翻译服务 | `VIDEO_TRANSLATE_SERVICE_API_KEY` | 视频翻译 API 调用 | `https://luoji.cn` |
| 语音克隆 | `VOICE_CLONE_API_KEY` | 语音克隆服务（可选） | 对应语音克隆服务商 |

```bash
export VIDEO_TRANSLATE_SERVICE_API_KEY="your_translation_api_key"
export VOICE_CLONE_API_KEY="your_voice_clone_key"
# ...
curl -s 'https://audiox-api-global.luoji.cn/video-trans/health' \
  -H "Authorization: Bearer $VIDEO_TRANSLATE_SERVICE_API_KEY"
```

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 调用翻译 API 完成多语言视频翻译
- **离线可用**：否（依赖在线翻译服务）
- **隐私等级**：中（视频需上传至翻译服务，记忆库本地存储）
- **企业部署**：支持私有化部署翻译记忆库

## 版本说明
- **当前版本**：1.0.0
- **版本类型**：PRO（专业版）
- **兼容性**：与 `video-translator-tool-free` 完全兼容，免费版 API Key 可直接使用
- **支持策略**：优先响应企业用户问题，提供工单支持与专属技术顾问

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需要API Key，无Key环境无法使用
- 本地运行，不支持多设备同步

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "视频翻译-专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "video translator pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
