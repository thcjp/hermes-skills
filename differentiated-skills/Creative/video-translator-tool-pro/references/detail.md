# 详细参考 - video-translator-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
batch:
  parallel_workers: 8              # 并行翻译数
  max_retries: 3                    # 失败重试次数
  retry_delay: 10                   # 重试间隔（秒）
  queue_file: /tmp/translate-queue.json

translation:
  default_source: "en"              # 默认源语言
  default_target: "zh"              # 默认目标语言
  supported_sources:                # 支持的源语言
    - en
    - zh
    - ko
    - ja
    - fr
    - ru
    - es
    - de
  supported_targets:                # 支持的目标语言
    - zh
    - en

subtitle:
  show: true                         # 默认显示字幕
  bilingual: false                  # 默认非双语
  style:
    font: "Noto Sans SC"
    size: 24
    color: "#ffffff"
    background: "rgba(0,0,0,0.7)"
    position: "bottom"

voice_clone:
  enabled: true                     # 启用语音克隆
  model: "advanced"                 # 克隆模型版本
  preserve_emotion: true            # 保留情感
glossary:
  file: /config/glossary-default.json
  domain: "general"
  custom_terms:
    "AI": "人工智能"
    "API": "应用程序接口"

memory:
  enabled: true                     # 启用翻译记忆库
  database: /data/translation-memory.db
  similarity_threshold: 0.9        # 复用相似度阈值
report:
  enabled: true
  output: /tmp/reports/translate-report.json
  include_quality_score: true
  include_cost_analysis: true
```

## 代码示例 (yaml)

```yaml
project: 课程多语言版本
output_dir: /videos/course-multilingual/

videos:
  - file: /videos/course-01.mp4
    source: zh

targets:
  - language: en
    voice_clone: false
    show_subtitles: true
    bilingual: true
  - language: ja
    voice_clone: true
    show_subtitles: true
    bilingual: true
  - language: ko
    voice_clone: true
    show_subtitles: true
    bilingual: true

glossary:
  file: /config/glossary-edu.json
  domain: education
```

## 代码示例 (json)

```json
{
  "project": "纪录片出海",
  "source_video": "/videos/documentary.mp4",
  "source_language": "zh",
  "variants": [
    {
      "name": "english-dubbed",
      "target_language": "en",
      "voice_clone": true,
      "show_subtitles": false,
      "bilingual": false
    },
    {
      "name": "bilingual-subtitle",
      "target_language": "en",
      "voice_clone": false,
      "show_subtitles": true,
      "bilingual": true
    }
  ]
}
```

## 代码示例 (json)

```json
{
  "domain": "technology",
  "terms": [
    {
      "source": "AI",
      "translations": {
        "zh": "人工智能",
        "en": "Artificial Intelligence"
      }
    },
    {
      "source": "machine learning",
      "translations": {
        "zh": "机器学习",
        "en": "Machine Learning"
      }
    }
  ]
}
```

## 代码示例 (json)

```json
{
  "project": "企业培训本地化",
  "output_dir": "/videos/training-localized/",
  "videos": [
    {"url": "/videos/training-01.mp4", "source": "en", "target": "zh"},
    {"url": "/videos/training-02.mp4", "source": "en", "target": "zh"},
    {"url": "/videos/training-03.mp4", "source": "en", "target": "zh"}
  ],
  "options": {
    "voice_clone": true,
    "show_subtitles": true,
    "bilingual": false,
    "glossary": "/config/glossary-tech.json"
  }
}
```

