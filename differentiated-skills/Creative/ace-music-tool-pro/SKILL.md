---
slug: ace-music-tool-pro
name: ace-music-tool-pro
version: 1.0.0
displayName: ACE音乐生成-专业版
summary: 企业级AI音乐生成工具,支持批量、翻唱、片段重绘、长时长输出,适配商业内容生产。
license: Proprietary
edition: pro
description: 'ACE音乐生成专业版,面向企业团队与专业音乐内容生产者的高级AI音乐工具。核心能力:

  - 批量生成多首歌曲,支持风格矩阵组合

  - 风格翻唱(cover)与片段重绘(repaint)

  - 长时长输出(最高 300 秒),支持完整歌曲结构

  - 音频输入驱动生成,可基于参考素材创作

  - 优先 API 配额与企业级技术支持


  适用场景:

  - 广告/影视配乐批量生产

  - 音乐厂牌快速 demo 生成与迭代

  - 游戏开发商多场景 BGM 批量产出

  - 企业品牌音频资产沉淀


  差异化:专业版在免费版基础上扩展批量生成、...'
tags:
- Creative
- 音乐生成
- 企业版
- 商业内容
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# ACE音乐生成工具 - 专业版

## 概述

ACE音乐生成专业版是一款面向企业团队与专业内容生产者的高级 AI 音乐创作工具。在免费版核心能力之上,扩展了批量生成、风格翻唱(cover)、片段重绘(repaint)、长时长输出与音频输入驱动生成等高级功能,可融入商业音乐生产流水线。

本版本完全兼容免费版所有参数,企业用户可直接迁移既有工作流并获得更高配额与更丰富的创作维度。

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-------|:-------|:-------|:-----|
| 文本生成音乐 | 是 | 是 | 基础 text2music |
| 自定义歌词 | 是 | 是 | 支持 Verse/Chorus 结构 |
| 单曲时长上限 | 60 秒 | 300 秒 | 支持完整歌曲结构 |
| 批量生成 | 否 | 是 | 单任务最多 10 首 |
| 风格翻唱(cover) | 否 | 是 | 基于音频输入翻唱 |
| 片段重绘(repaint) | 否 | 是 | 修改已有音频局部 |
| 音频输入驱动 | 否 | 是 | 参考素材再创作 |
| API 配额优先级 | 普通 | 高优先 | 企业级保障 |
| 技术支持 | 社区 | 专属支持 | 工单响应 |

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：音乐生成工具、支持批量、长时长输出、适配商业内容生产、ACE、音乐生成专业版、面向企业团队与专、业音乐内容生产者、的高级、音乐工具、核心能力、批量生成多首歌曲、支持风格矩阵组合、与片段重绘、音频输入驱动生成、可基于参考素材创、配额与企业级技术等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一:广告配乐批量生成

广告公司需为多个产品线快速产出风格统一的背景音乐,使用批量生成一次性产出多版本候选。

```bash
# 批量生成 5 首电子风格广告配乐
（请参考skill目录中的脚本文件） "electronic dance track, upbeat, brand commercial" \
  --batch 5 \
  --duration 60 \
  --output ad_edm.mp3

# 风格矩阵:不同 BPM 组合
for bpm in 110 120 128 140; do
  （请参考skill目录中的脚本文件） "corporate uplifting pop" \
    --bpm $bpm \
    --duration 30 \
    --output ad_pop_${bpm}.mp3
done
```

### 场景二:歌曲翻唱与片段重绘

音乐厂牌希望对已有 demo 进行风格翻唱,并重绘某一段落以优化听感。

```bash
# 基于原曲翻唱为爵士风格
（请参考skill目录中的脚本文件） "jazz cover, smoky bar, saxophone" \
  --task cover \
  --audio-input original.mp3 \
  --output jazz_cover.mp3

# 重绘副歌部分(30-60秒)
（请参考skill目录中的脚本文件） "more energetic chorus, add brass section" \
  --task repaint \
  --audio-input original.mp3 \
  --start 30 --end 60 \
  --output refined.mp3
```

### 场景三:影视长配乐生成

影视制作公司需要生成 3-5 分钟的背景配乐,使用长时长输出能力。

```bash
# 生成长达 4 分钟的史诗风格配乐
（请参考skill目录中的脚本文件） "epic orchestral, cinematic, emotional build-up, strings and brass" \
  --duration 240 \
  --instrumental \
  --key "D minor" \
  --bpm 90 \
  --output movie_score.mp3
```

## 快速开始

### 第一步:配置企业 API Key

```bash
# 企业版 Key 享有更高配额与优先级
export ACE_MUSIC_API_KEY="your_pro_api_key"
export ACE_MUSIC_EDITION="pro"  # 启用专业版功能
```

### 第二步:执行批量生成

```bash
# 一次生成 3 首不同风格候选
（请参考skill目录中的脚本文件） "summer pop hit" \
  --batch 3 \
  --duration 120 \
  --language en \
  --output summer_pop.mp3
```

### 第三步:结果处理

批量生成会输出多个文件路径,可结合脚本进行自动归档:

```bash
# 自动归档批量生成结果
results=$(（请参考skill目录中的脚本文件） "brand jingle" --batch 5 --output jingle.mp3)
echo "$results" | while read file; do
  mv "$file" ./archive/$(date +%Y%m%d)_$(basename "$file")
done
```

## 示例

专业版完整配置:

```bash
# 环境变量
ACE_MUSIC_API_KEY=your_pro_key
ACE_MUSIC_BASE_URL=https://api.acemusic.ai
ACE_MUSIC_EDITION=pro
ACE_MUSIC_MAX_DURATION=300
ACE_MUSIC_MAX_BATCH=10

# 高级任务参数
--task text2music|cover|repaint   # 任务类型
--audio-input <file>              # 音频输入(cover/repaint 必填)
--start <seconds>                 # 重绘起始位置
--end <seconds>                   # 重绘结束位置
--batch <n>                       # 批量数量(1-10)
--duration <seconds>              # 时长(1-300)
```

## 最佳实践

1. **批量先行筛选**:使用 `--batch` 一次产出多版本,再人工筛选最佳,提升命中率
2. **翻唱保持结构**:使用 cover 时保留原曲段落结构,仅改变风格元素
3. **重绘精确定位**:repaint 时通过 `--start/--end` 精确指定片段,避免整曲重生成
4. **长曲分段生成**:超过 180 秒的曲目建议分段生成后拼接,质量更稳定
5. **风格矩阵组合**:批量生成时组合不同 BPM、调式、语言,形成候选矩阵
6. **企业资产管理**:建议建立命名规范与元数据标签,便于音乐资产归档检索

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有参数,迁移时仅需更换 API Key 并设置 `ACE_MUSIC_EDITION=pro`。

### Q2:批量生成失败的文件如何处理?
A:批量任务中部分失败不影响其他,脚本会返回成功生成的文件列表。失败的可在下次重试。

### Q3:cover 与 repaint 的区别?
A:cover 是对整曲进行风格翻唱(保留旋律改风格),repaint 是对指定片段进行局部修改重绘,两者均可基于音频输入创作。

### Q4:企业版 API 配额如何申请提升?
A:联系企业服务渠道提交配额提升申请,专业版默认享有高优先级队列。

### Q5:长时长生成会不会中途超时?
A:专业版针对长时长任务优化,最长 300 秒歌曲生成约需 3-5 分钟。建议脚本设置合理超时(如 600 秒)。

### Q6:能否集成到 CI/CD 流水线?
A:可以。脚本支持非交互模式,可在自动化流水线中调用,建议结合重试机制与结果校验。

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: Bash shell + curl + jq

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| ACE Music Pro API | 外部 API | 必需 | 企业服务渠道申请 |
| curl | 命令行工具 | 必需 | 系统自带 |
| jq | JSON 处理 | 必需 | 包管理器安装 |
| ffmpeg | 音频处理 | 推荐 | 用于拼接与转码 |
| base64 | 解码工具 | 必需 | 系统自带 |

### API Key 配置
- **环境变量名**: `ACE_MUSIC_API_KEY`(企业版 Key)
- **附加变量**: `ACE_MUSIC_EDITION=pro`
- **获取方式**: 通过企业服务渠道申请,享有高优先级配额
- **安全建议**: 使用密钥管理服务(如 Vault)存储,避免明文写入脚本

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持批量、长时长、翻唱重绘等企业级音乐生产场景

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
