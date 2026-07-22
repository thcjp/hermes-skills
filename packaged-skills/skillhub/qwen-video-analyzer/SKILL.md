---
slug: "qwen-video-analyzer"
name: "qwen-video-analyzer"
version: "1.0.0"
displayName: "通义千问视频分析-专业版"
summary: "企业级视频分析工具,支持批量处理、自定义模型、结构化报告,适配商业内容审核与生产。"
license: "Proprietary"
edition: "pro"
description: |-
  通义千问视频分析专业版,面向企业团队与专业用户的高级AI视频内容理解工具。核心能力:
  - 批量视频分析,支持目录扫描与队列处理
  - 自定义模型选择(Qwen 系列多版本)
  - 结构化分析报告(JSON/Markdown/Excel)
  - 视频内容审核(违规/敏感内容检测)
  - 多维度分析(场景/物体/动作/情绪/字幕)
  - 优先 API 配额与企业级技术支持

  适用场景:
  - 视频平台内容批量审核
  - 媒体机构视频素材标注归档
  - 企业培训视频内容结构化
  - 安防监控视频智能分析

  差异化:专业版在免...
tags:
  - Creative
  - 视频分析
  - 企业版
  - 商业内容
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# 通义千问视频分析-专业版

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-------|:-------|:-------|:-----|
| 本地视频分析 | 是 | 是 | 支持常见格式 |
| 远程 URL 分析 | 是 | 是 | http/https 直链 |
| 自定义提示词 | 是 | 是 | 灵活提问 |
| 抽帧频率调节 | 是 | 是 | FPS 1-10 |
| 场景描述 | 是 | 是 | 逐场景描述 |
| 物体识别 | 是 | 是 | 检测画面物体 |
| 视频摘要 | 是 | 是 | 内容概要 |
| 批量分析 | 否 | 是 | 目录/队列处理 |
| 自定义模型 | 否 | 是 | 多版本选择 |
| 结构化报告 | 否 | 是 | JSON/MD/Excel |
| 内容审核 | 否 | 是 | 违规检测 |
| 多维度分析 | 否 | 是 | 场景/物体/动作/情绪 |
| API 配额优先级 | 普通 | 高优先 | 企业级保障 |
| 技术支持 | 社区 | 专属 | 工单响应 |
### 能力项

执行能力项操作,处理用户输入并返回结果。

**输入**: 用户提供能力项所需的参数和指令。

**输出**: 返回能力项的处理结果。

- 执行`能力项`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力项`相关配置参数进行设置
### 本地视频分析

执行本地视频分析操作,处理用户输入并返回结果。

**输入**: 用户提供本地视频分析所需的参数和指令。

**输出**: 返回本地视频分析的处理结果。

- 执行`本地视频分析`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`本地视频分析`相关配置参数进行设置
### 远程 URL 分析

执行远程 URL 分析操作,处理用户输入并返回结果。

**输入**: 用户提供远程 URL 分析所需的参数和指令。

**输出**: 返回远程 URL 分析的处理结果。

- 执行`远程 URL 分析`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`远程 URL 分析`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级视频分析工、支持批量处理、适配商业内容审核、与生产、通义千问视频分析、面向企业团队与专、业用户的高级、视频内容理解工具、核心能力、批量视频分析、支持目录扫描与队、自定义模型选择、Qwen、系列多版本、结构化分析报告、Markdown、视频内容审核、敏感内容检测、配额与企业级技术。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:视频平台批量内容审核

视频平台需对一批上传视频进行内容审核,检测违规或敏感内容。

```python
# 批量审核视频内容
python3 scripts/batch_analyze.py \
  --input ./uploads/ \
  --model qwen-vl-max \
  --prompt "请审核这段视频是否包含违规、暴力、色情等敏感内容,输出审核结论与风险等级" \
  --output ./audit_reports/ \
  --format json \
  --parallel 5

# 生成审核汇总报告
python3 scripts/audit_summary.py \
  --input ./audit_reports/ \
  --output audit_summary.xlsx
```

### 场景二:媒体机构素材标注归档

媒体机构需对一批视频素材进行内容标注,便于后续检索与复用。

```bash
# 批量生成视频标注
python3 scripts/batch_analyze.py \
  --input ./footage/ \
  --model qwen-vl-plus \
  --prompt "请为这段视频生成:1.内容摘要(50字内)2.场景标签(5个)3.人物/物体清单4.情绪基调" \
  --output ./annotations/ \
  --format markdown \
  --parallel 8

# 导出为 Excel 索引表
python3 scripts/export_index.py \
  --input ./annotations/ \
  --output footage_index.xlsx \
  --columns "文件名,摘要,标签,物体,情绪"
```

### 场景三:安防监控视频分析

安防团队需对监控视频进行智能分析,识别异常事件。

```bash
# 多维度分析监控视频
python3 scripts/batch_analyze.py \
  --input ./surveillance/ \
  --model qwen-vl-max \
  --prompt "请分析这段监控视频:1.出现的人物数量与行为2.是否有异常事件(闯入/打斗/聚集)3.时间轴事件记录" \
  --output ./security_reports/ \
  --format json \
  --fps 4 \
  --parallel 3

# 异常事件告警
python3 scripts/alert_anomalies.py \
  --input ./security_reports/ \
  --threshold "high" \
  --notify webhook_url
```

### 场景四:企业培训视频结构化

企业培训部门需将培训视频内容结构化,生成章节目录与知识点。

```bash
# 生成视频章节与知识点
python3 scripts/batch_analyze.py \
  --input ./training_videos/ \
  --model qwen-vl-max \
  --prompt "请为这段培训视频生成:1.章节目录(带时间戳)2.每章核心知识点3.适合的考核问题(3个)" \
  --output ./training_outlines/ \
  --format markdown \
  --parallel 5
```

## 使用流程

### 优秀步:配置企业 API Key

```json
// ~/.skill-platform/skill-platform.json
{
  "skills": {
    "dashscope": {
      "apiKey": "your_pro_api_key",
      "edition": "pro",
      "default_model": "qwen-vl-max"
    }
  }
}
```

### 第二步:执行批量分析

```bash
python3 scripts/batch_analyze.py \
  --input ./videos/ \
  --model qwen-vl-max \
  --prompt "请详细描述视频内容" \
  --output ./reports/ \
  --format json \
  --parallel 5
```

### 第三步:生成汇总报告

```bash
python3 scripts/summary_report.py \
  --input ./reports/ \
  --output summary.xlsx \
  --format excel
```

### 命令参数说明

- `--prompt`: 命令参数,用于指定操作选项
- `--notify`: 命令参数,用于指定操作选项
- `--format`: 命令参数,用于指定操作选项
- `--parallel`: 命令参数,用于指定操作选项
- `--model`: 命令参数,用于指定操作选项

### 命令参数说明

- `--threshold`: 命令参数,用于指定操作选项
- `--columns`: 命令参数,用于指定操作选项
- `--input`: 命令参数,用于指定操作选项

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
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Python 3.9+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| DashScope Pro API | 外部 API | 必需 | 企业服务渠道申请 |
| Python 3.9+ | 运行时 | 必需 | 官方安装 |
| dashscope | Python SDK | 必需 | pip install dashscope |
| ffmpeg | 视频处理 | 必需 | 包管理器安装 |
| openpyxl | Excel 生成 | 推荐 | pip install openpyxl |
| aiohttp | 异步 HTTP | 推荐 | pip install aiohttp |

### API Key 配置
- **配置文件**: `~/.skill-platform/skill-platform.json`
- **字段路径**: `skills.dashscope.apiKey`(企业版 Key)
- **附加字段**: `skills.dashscope.edition=pro`
- **获取方式**: 通过企业服务渠道申请,享有高优先级配额
- **安全建议**: 配置文件设置权限 600,使用密钥管理服务存储

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持批量分析、自定义模型、结构化报告等企业级视频内容分析场景

## 案例展示

专业版完整配置:

```bash
# 配置文件
~/.skill-platform/skill-platform.json

# 环境变量
DASHSCOPE_API_KEY=your_pro_key
DASHSCOPE_EDITION=pro
DASHSCOPE_DEFAULT_MODEL=qwen-vl-max
DASHSCOPE_MAX_BATCH=50
DASHSCOPE_DEFAULT_PARALLEL=5

# 可选模型
# qwen-vl-max: 优秀能力,适合复杂分析
# qwen-vl-plus: 均衡能力,性价比高
# qwen-vl-base: 基础能力,成本最低

# 批量分析参数
--input <dir>                  # 输入目录
--output <dir>                 # 输出目录
--model <model>                # 模型选择
--prompt <text>                # 分析提示词
--fps <n>                      # 抽帧频率(1-10)
--parallel <n>                 # 并发数(1-20)
--format json|markdown|excel   # 报告格式
```

### 多维度分析配置

```bash
# 综合分析(场景+物体+动作+情绪)
--prompt "请从以下维度分析视频:1.场景描述 2.物体识别 3.动作分析 4.情绪基调 5.内容摘要"

# 内容审核专用
--prompt "请审核视频是否包含:1.暴力内容 2.色情内容 3.违规广告 4.敏感政治内容,输出风险等级(低/中/高)"

# 时间轴事件
--prompt "请按时间顺序记录视频中的关键事件,格式:[时间] 事件描述"
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有参数与命令,迁移时仅需更换 API Key 并设置 `edition=pro`。

### Q2:批量分析支持多少视频?
A:单批最多 50 个视频,并发数 1-20 可调。大批量建议分批处理。

### Q3:模型之间有什么区别?
A:qwen-vl-max 能力优秀但成本最高,适合复杂分析;qwen-vl-plus 均衡性价比;qwen-vl-base 成本最低,适合简单标注。

### Q4:结构化报告包含哪些内容?
A:根据提示词输出,支持 JSON(程序处理)、Markdown(人工阅读)、Excel(数据统计)三种格式,可自定义字段。

### Q5:内容审核准确率如何?
A:Qwen 多模态模型对常见违规内容(暴力、色情、敏感)有较高识别率,但建议结合人工复核,不能完全替代人工审核。

### Q6:能否集成到视频处理流水线?
A:可以。通过 API 可集成到视频上传、转码、审核一体化流水线,实现自动化内容分析。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
