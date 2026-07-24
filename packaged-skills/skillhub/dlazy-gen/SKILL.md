---
slug: "dlazy-gen"
name: "dlazy-gen"
version: 1.0.1
displayName: "综合生成工具-专业版"
summary: "全模态生成引擎，覆盖40+模型，支持图片/视频/音频生成与管道链接批量工作流。"
license: "Proprietary"
edition: "pro"
description: |-
  综合生成工具专业版，面向专业团队的全模态AI生成平台。核心能力：
  - 40+ 模型全覆盖（图片、视频、音频三大模态）
  - 高质量图片生成（seedream-4。Use when 需要视频处理、音频编辑、媒体转换、配音生成时使用。不适用于版权受保护的媒体内容处理.
tags:
  - Creative
  - ImageGeneration
  - VideoGeneration
  - Enterprise
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 综合生成工具-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 综合生成工具-专业版全模态生成 | 不支持 | 支持 |
| 综合生成工具-专业版音频生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

### 模态覆盖对比

| 模态 | 免费版 | 专业版 | 代表模型 |
|:-----|:-----|:-----|:-----|
| 基础文生图 | 4个 | 19个 | banana2, seedream-4.5, recraft-v4-pro, qwen-image-2-pro |
| 矢量图生成 | 不支持 | 2个 | recraft-v4-vector, recraft-v4-pro-vector |
| 图片处理 | 2个 | 4个 | imageseg, superres, image-replicate, video-replicate |
| 视频生成 | 不支持 | 17个 | veo-3.1, seedance-2.0, kling-v3, pixverse-c1, wan2.7 |
| 音频生成 | 不支持 | 15个 | doubao-tts, suno-music, elevenlabs-dialogue |
| 管道链接 | 不支持 | 支持 | 多步骤串联 |- 验证返回数据的完整性和格式正确性
- 参考`核心能力`的配置文档进行参数调优
### 核心能力(补充)
```text
图片生成（19个模型）:
  - 高质量: seedream-4.5, qwen-image-2-pro, recraft-v4-pro
  - 通用型: banana-pro, banana2, gpt-image-2, grok-4.2
  - 风格化: mj-imagine, jimeng-t2i, kling-image-o1, viduq2-t2i
  - 矢量图: recraft-v4-vector, recraft-v4-pro-vector (SVG输出)
  - 轻量级: seedream-5.0-lite
# ...
视频生成（17个模型）:
  - 文生视频: veo-3.1, seedance-2.0, kling-v3, pixverse-c1, wan2.7
  - 图生视频: jimeng-i2v-first, viduq2-i2v, kling-v3-omni
  - 首尾帧: jimeng-i2v-first-tail
  - 数字人: jimeng-omnihuman-1.5, jimeng-dream-actor
  - 视频编辑: happyhorse-1.0, video-replicate
  - 唇形同步: heygen-lipsync-speed, sync-lipsync-3, videoretalk
  - 视频处理: videoseg
音频生成（15个模型）:
  - 详见 dlazy-audio-tool-pro
高级功能:
  - 管道链接（Pipe Chaining）
  - 批量生成
  - 风格复刻（image-replicate, video-replicate）
  - 矢量图输出（SVG）
```

**输入**: 用户提供核心能力所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `核心能力` 选项
- 处理流程: 接收输入 -> 执行核心能力 -> 返回结果
- 输入: 用户提供核心能力所需的参数和指令
- 输出: 返回核心能力的处理结果,包含执行状态码、结果数据和执行日志

### 基础文生图

针对基础文生图,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供基础文生图相关的配置参数、输入数据和处理选项.
**输出**: 返回基础文生图的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`基础文生图`的配置文档进行参数调优
#
## 适用场景

### 场景一：广告素材全流程制作

从文案到视频广告的完整制作流程.
```bash
# 第1步: 生成产品主视觉图
dlazy seedream-4.5 \
  --prompt "高端无线耳机产品图，深色背景，戏剧性灯光，超写实" \
  --ratio "16:9" \
  --quality "4K"
# ...
# 第2步: 图片转视频（图生视频）
dlazy kling-v3 \
  --image @0.url \
  --prompt "耳机缓缓旋转，光影流动，产品展示动效" \
  --duration 5
# ...
# 第3步: 生成背景音乐
dlazy suno-music \
  --mode "custom" \
  --style "electronic ambient premium" \
  --title "Product Showcase BGM" \
  --instrumental true \
  --duration 5
# ...
# 第4步: 生成配音旁白
dlazy doubao-tts \
  --text "全新无线耳机，聆听非凡。" \
  --voice "male-magnetic"
# ...
# 管道链接一键完成:
dlazy seedream-4.5 --prompt "高端无线耳机，深色背景" --ratio "16:9" \
  | dlazy kling-v3 --image @0.url --prompt "耳机旋转展示" --duration 5
```

### 场景二：短视频内容批量生产

批量生成短视频素材.
```python
# 短视频批量生产脚本
import subprocess
import json
# ...
class VideoBatchProducer:
    """短视频批量生产器"""
# ...
    def __init__(self):
        self.pipeline = []
# ...
    def add_image_step(self, prompt, model="seedream-5.0-lite", ratio="9:16"):
        """添加图片生成步骤"""
        self.pipeline.append({
            "type": "image",
            "model": model,
            "prompt": prompt,
            "ratio": ratio
        })
        return self
# ...
    def add_video_step(self, prompt, model="kling-v3", duration=5):
        """添加视频生成步骤"""
        self.pipeline.append({
            "type": "video",
            "model": model,
            "prompt": prompt,
            "duration": duration
        })
        return self
# ...
    def add_audio_step(self, text, model="doubao-tts"):
        """添加配音步骤"""
        self.pipeline.append({
            "type": "audio",
            "model": model,
            "text": text
        })
        return self
# ...
    def execute_batch(self, scenarios):
        """批量执行生产流程"""
        results = []
        for scenario in scenarios:
            steps = []
            for step in self.pipeline:
                cmd = self._build_command(step, scenario)
                result = subprocess.run(cmd, capture_output=True, text=True)
                try:
                    output = json.loads(result.stdout)
                    steps.append({"step": step["type"], "output": output})
                except:
                    steps.append({"step": step["type"], "error": "failed"})
            results.append({"scenario": scenario, "steps": steps})
        return results
# ...
    def _build_command(self, step, scenario):
        cmd = ["dlazy", step["model"]]
        if step["type"] == "image":
            cmd += ["--prompt", step["prompt"].format(**scenario),
                    "--ratio", step["ratio"]]
        elif step["type"] == "video":
            cmd += ["--prompt", step["prompt"].format(**scenario),
                    "--duration", str(step["duration"])]
        elif step["type"] == "audio":
            cmd += ["--text", step["text"].format(**scenario)]
        return cmd
# ...
# 批量生产
producer = VideoBatchProducer()
producer.add_image_step("美食特写：{dish}，暖色调，诱人", "9:16") \
        .add_video_step("{dish}冒热气，缓慢推进", duration=5) \
        .add_audio_step("今天推荐：{dish}，色香味俱全！")
# ...
scenarios = [
    {"dish": "红烧肉"},
    {"dish": "清蒸鱼"},
    {"dish": "麻婆豆腐"},
    {"dish": "糖醋排骨"},
    {"dish": "宫保鸡丁"}
]
results = producer.execute_batch(scenarios)
```

### 场景三：矢量图与Logo生成

生成可缩放的矢量图资产.
```bash
# 生成SVG矢量Logo
dlazy recraft-v4-vector \
  --prompt "极简风格科技公司Logo，几何图形，蓝色主调" \
  --output "logo.svg"
# ...
# 高保真矢量插画（4MP级别）
dlazy recraft-v4-pro-vector \
  --prompt "详细的等距插画，城市俯视图，扁平风格" \
  --output "city-illustration.svg"
```

### 管道引用速查

| 引用 | 解析为 |
|---:|---:|
| `-` | 上游输出的自然值 |
| `@N` | 第N个输出的主值 |
| `@N.path` | 深入第N个输出 |
| `@*` | 所有输出的主值数组 |
| `@stdin` | 完整上游JSON信封 |

## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
2. **操作系统**: Windows / macOS / Linux
3. **Node.js**: 16+（dlazy CLI 运行需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Node.js 16+ | 运行时 | 必需 | nodejs.org 官方下载 |
| @dlazy/cli | CLI工具 | 必需 | `npm install -g @dlazy/cli@latest` |
| dlazy API Key | 认证 | 必需 | dlazy.com/dashboard 获取 |
| FFmpeg（可选） | 工具 | 推荐 | 视频拼接与格式转换 |

### API Key 配置
4. **必需**: dlazy API Key（与免费版共用）
5. **获取方式**: 访问 dlazy.com/dashboard/organization/api-key
6. **配置方式**: `dlazy auth set YOUR_API_KEY` 或环境变量 `DLAZY_API_KEY`
7. **安全说明**: Key 可随时轮换或撤销；配置文件权限限制为当前用户
8. **余额说明**: 视频生成消耗较高，建议定期检查余额

### 可用性分类
9. **分类**: MD+EXEC+API（Markdown指令 + 命令行 + 外部API调用）
10. **说明**: 企业级AI Skill，支持全模态40+模型、管道链接与批量处理
11. **适用规模**: 专业内容团队，多媒体批量生产
12. **兼容性**: 与免费版完全兼容，API Key 和配置无缝共用

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:------|------:|:------|:------|
| content | string | 否 | dlazy-gen处理的内容输入 |,  |
| mode | string | 否 | 处理模式, 可选: json/text/markdown,  |
| max_retries | integer | 否 | 单步最大重试次数, 默认: 2 |
| skip_steps | array | 否 | 跳过的步骤编号(用于断点续传), 默认: [] |

## 输出格式

```json
{
  "success": true,
  "data": {
    "final_result": {
      "gen_result": "gen_result_value",
      "gen_metadata": "gen_metadata_value",
      "gen_status": "gen_status_value"
    },
    "execution_log": [
      {
        "step": 1,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 1200,
        "output_summary": "按流程执行"
      },
      {
        "step": 2,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 3500,
        "output_summary": "按流程执行"
      },
      {
        "step": 3,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 2100,
        "output_summary": "按流程执行"
      },
      {
        "step": 4,
        "name": "按流程执行",
        "status": "completed",
        "duration_ms": 800,
        "output_summary": "按流程执行"
      }
    ],
    "total_duration_ms": 7600,
    "gates_passed": 3,
    "gates_total": 3
  },
  "error": null
}
```

中间产物模板参考: `assets/dlazy-gen_template`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|:------:|--------|:-------|:------:|
| LLM | 模型 | 是 | 需要LLM执行各步骤的智能处理, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 高质量图片生成

```bash
# seedream-4.5 高质量文生图
dlazy seedream-4.5 \
  --prompt "描述文本" \
  --ref-images "ref1.jpg,ref2.jpg" \  # 参考图（可选）
  --quality "4K"                       # 2K 或 4K
  --ratio "16:9"
# ...
# recraft-v4-pro 4MP高分辨率
dlazy recraft-v4-pro \
  --prompt "描述文本" \
  --resolution "4MP"   # 适合印刷品
```

### 视频生成配置

```bash
# veo-3.1 高质量视频
dlazy veo-3.1 \
  --prompt "描述文本" \
  --mode "t2v"          # t2v 或 i2v
  --image "input.jpg"   # i2v模式需要
  --duration 5
# ...
# seedance-2.0 多模态参考
dlazy seedance-2.0 \
  --prompt "描述文本" \
  --ref-images "img1.jpg" \
  --ref-video "ref.mp4" \  # 视频参考
  --first-frame "start.jpg" \
  --last-frame "end.jpg"
```

### 管道链接配置

```bash
# 多步骤管道链接
dlazy seedream-4.5 --prompt "城市夜景" --n 4 \
  | dlazy superres --images @* \
  | dlazy kling-v3 --image @0.url --prompt "城市灯火流动"
# ...
# 管道引用说明:
# @0.url  = 上游优秀个输出的URL
# @*      = 上游所有输出数组
# -       = 上游自然值（单值场景）
```

## 常见问题

### Q: 视频生成支持多长？

A: 多数视频模型支持 5-10 秒。veo-3.1 支持更长时长但生成时间相应增加。建议短视频 5 秒起步.
### Q: 管道链接中某一步失败怎么办？

A: 管道中断，已完成的步骤输出仍可使用。检查失败步骤的错误信息，修正后从失败步骤重新执行.
### Q: 矢量图输出什么格式？

A: recraft-v4-vector 和 recraft-v4-pro-vector 输出 SVG 格式，可在任意分辨率下缩放，适合 Logo、图标和插画.
### Q: 如何从免费版升级？

A: API Key 和 CLI 配置无需变更，直接使用专业版的全部 40+ 模型即可.
### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

A: 单批建议不超过 50 个任务。超大批量请分批执行，避免 API 限流.
### Q: 视频生成消耗大吗？

A: 视频生成的消耗显著高于图片。建议先用图片确认创意方向，再生成视频.
## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|----------|----------|----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 图像处理能力受限于本地硬件与内存
- 大尺寸图片处理可能较慢或失败
