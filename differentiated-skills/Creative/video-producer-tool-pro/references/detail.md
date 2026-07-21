# 详细参考 - video-producer-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
batch:
  parallel_workers: 8              # 并行生产数
  max_retries: 3                    # 失败重试次数
  retry_delay: 10                   # 重试间隔（秒）
  queue_file: /tmp/render-queue.json

production:
  default_resolution: "1080p"       # 默认分辨率
  default_fps: 30                   # 默认帧率
  default_language: "zh"            # 默认语言
  max_scenes: 50                    # 单视频最大场景数
brand:
  logo: /assets/logo.png
  watermark:
    enabled: true
    image: /assets/watermark.png
    position: bottom-right
    opacity: 0.7
  color_scheme:
    primary: "#1a73e8"
    secondary: "#ffffff"
    accent: "#ff6b35"
  fonts:
    title: "Noto Sans SC Bold"
    body: "Noto Sans SC Regular"
    subtitle: "Noto Sans SC Light"

templates:
  intro: /templates/intro-3s.json
  outro: /templates/outro-5s.json
  transitions: /templates/transitions/

tts:
  default_voice: "female-professional"
  voice_map:
    zh: "female-professional"
    en: "male-business"
    ja: "female-friendly"
  speed: 1.0
  pitch: 0

render:
  parallel: 8
  gpu_acceleration: true           # GPU 加速
  crf: 18                            # 视频质量（18-28，越小越好）
  preset: "medium"                   # 编码速度
report:
  enabled: true
  output: /tmp/reports/produce-report.json
  include_thumbnails: true
  include_metadata: true
```

## 代码示例 (yaml)

```yaml
project: 产品视频本地化
source_topic: "智能办公解决方案"
output_dir: /videos/localized/

base_script:
  - text: "智能办公 让效率翻倍"
    emoji: "⚡"
    title: "智能办公"
  - text: "一键协同 团队高效"
    emoji: "👥"
    title: "团队协同"
  - text: "数据驱动 决策更准"
    emoji: "📊"
    title: "数据驱动"

languages:
  - code: zh
    voice: female-professional
  - code: en
    voice: male-business
  - code: ja
    voice: female-friendly
  - code: ko
    voice: male-casual
  - code: fr
    voice: female-elegant
  - code: de
    voice: male-formal

brand:
  logo: /assets/company-logo.png
  intro_template: /templates/intro-3s.json
  outro_template: /templates/outro-5s.json
```

## 代码示例 (json)

```json
{
  "project": "MCN 日更批量",
  "output_dir": "/videos/mcn-daily/",
  "brand": {
    "logo": "/assets/logo.png",
    "watermark": true,
    "color_scheme": "tech-blue"
  },
  "videos": [
    {
      "account": "tech-account",
      "topic": "AI 新突破",
      "script": [
        {"text": "AI 又一次突破极限", "emoji": "🚀", "title": "AI 突破"},
        {"text": "这次改变了什么", "emoji": "💡", "title": "变革"}
      ],
      "language": "zh",
      "resolution": "1080p"
    },
    {
      "account": "edu-account",
      "topic": "高效学习法",
      "script": [
        {"text": "学霸都在用的方法", "emoji": "📚", "title": "学习方法"},
        {"text": "三步提升效率", "emoji": "⚡", "title": "效率提升"}
      ],
      "language": "zh",
      "resolution": "1080p"
    }
  ]
}
```

## 代码示例 (json)

```json
{
  "project": "新品发布 A/B 测试",
  "output_dir": "/videos/ab-test/",
  "base_topic": "智能手表新品",
  "variants": [
    {
      "name": "variant-A-question",
      "hook": {"text": "你还在用传统手表吗", "emoji": "❓", "title": "传统 vs 智能"},
      "script": [
        {"text": "智能手表时代已来", "emoji": "⌚", "title": "智能时代"}
      ]
    },
    {
      "name": "variant-B-data",
      "hook": {"text": "销量突破 100 万", "emoji": "📊", "title": "销量神话"},
      "script": [
        {"text": "智能手表时代已来", "emoji": "⌚", "title": "智能时代"}
      ]
    },
    {
      "name": "variant-C-scene",
      "hook": {"text": "想象一下未来的生活", "emoji": "🌟", "title": "未来生活"},
      "script": [
        {"text": "智能手表时代已来", "emoji": "⌚", "title": "智能时代"}
      ]
    }
  ]
}
```

### 场景 1：MCN 矩阵账号批量出片
某 MCN 机构运营 10 个垂类账号，每天需要为每个账号生产 3-5 条短视频。

**批量生产配置 `batch-produce.json`：**

```json
{
  "project": "MCN 日更批量",
  "output_dir": "/videos/mcn-daily/",
  "brand": {
    "logo": "/assets/logo.png",
    "watermark": true,
    "color_scheme": "tech-blue"
  },
  "videos": [
    {
      "account": "tech-account",
      "topic": "AI 新突破",
      "script": [
        {"text": "AI 又一次突破极限", "emoji": "🚀", "title": "AI 突破"},
        {"text": "这次改变了什么", "emoji": "💡", "title": "变革"}
      ],
      "language": "zh",
      "resolution": "1080p"
    },
    {
      "account": "edu-account",
      "topic": "高效学习法",
      "script": [
        {"text": "学霸都在用的方法", "emoji": "📚", "title": "学习方法"},
        {"text": "三步提升效率", "emoji": "⚡", "title": "效率提升"}
      ],
      "language": "zh",
      "resolution": "1080p"
    }
  ]
}
```

**执行命令：**

```bash
node batch-produce.js --config /path/to/batch-produce.json --parallel 8
```

**输出报告：**

```text
/videos/mcn-daily/
├── tech-account/
│   ├── ai-new-breakthrough.mp4
│   └── report.json
├── edu-account/
│   ├── study-method.mp4
│   └── report.json
└── batch-report.json   # 批量生产总报告
```



