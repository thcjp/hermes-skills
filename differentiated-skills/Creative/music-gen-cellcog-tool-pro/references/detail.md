# 详细参考 - music-gen-cellcog-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
project:
  name: "企业音乐资产管理"
  version: "1.0.0"

api:
  provider: "cellcog"
  api_key: "${CELLCOG_API_KEY}"
  endpoint: "https://api.cellcog.com/v1"
  rate_limit: "100/hour"

generation:
  default_format: "flac"
  default_quality: "lossless"
  default_sample_rate: 48000
  default_bit_depth: 24
  parallel: 5
  auto_validate: true

license_management:
  track_usage: true
  expiry_alerts: true
  compliance_check: true
  auto_renew: false

library:
  categories:
    - background
    - brand
    - content
    - emotional
    - genre
  search:
    by_mood: true
    by_bpm: true
    by_genre: true
    by_duration: true
    by_license: true
  auto_tag: true
  fingerprint: true
  waveform: true

audit:
  audio_quality: true
  loudness: -16
  standard: "EBU R128"
  spectrum_analysis: true
  style_matching: true
  report: "html"
```

## 代码示例 (python)

```python
quality_audit = {
    "checks": [
        {
            "name": "音质检查",
            "test": "audio_quality",
            "min_bitrate": "128kbps",
            "min_sample_rate": "44100Hz",
            "check_clipping": True,
            "check_noise": True
        },
        {
            "name": "时长验证",
            "test": "duration_check",
            "expected_range": [15, 300]
        },
        {
            "name": "响度规范",
            "test": "loudness_normalization",
            "target_loudness": -16,
            "tolerance": 2,
            "standard": "EBU R128"
        },
        {
            "name": "频谱分析",
            "test": "spectrum_analysis",
            "check_frequency_response": True,
            "check_dynamic_range": True
        },
        {
            "name": "风格匹配",
            "test": "style_matching",
            "compare_with_prompt": True,
            "confidence_threshold": 0.8
        }
    ],
    "auto_fix": {
        "loudness_normalize": True,
        "trim_silence": True,
        "remove_clipping": True,
        "noise_reduction": True
    },
    "report_format": "html"
}
```

## 代码示例 (python)

```python
batch_config = {
    "project": "电商配乐批量生产",
    "tasks": [
        {
            "id": "bgm_001",
            "type": "text_to_music",
            "prompt": "欢快的电子音乐,适合产品展示,128 BPM",
            "duration": 30,
            "style": "electronic",
            "format": "wav",
            "quality": "high"
        },
        {
            "id": "bgm_002",
            "type": "lyrics_to_music",
            "lyrics": "歌词内容...",
            "style": "pop",
            "voice": "female",
            "duration": 90,
            "format": "wav",
            "quality": "high"
        },
        {
            "id": "bgm_003",
            "type": "text_to_music",
            "prompt": "轻松的lo-fi音乐,适合学习背景,80 BPM",
            "duration": 120,
            "style": "lo-fi",
            "instrumental": True,
            "format": "flac",
            "quality": "lossless"
        }
    ],
    "parallel": 5,
    "auto_validate": True,
    "license_tracking": True,
    "output_dir": "./music-library/"
}

python3 batch_music_gen.py --config batch_config
```

