---
slug: comfyui-painter-tool-free
name: comfyui-painter-tool-free
version: "1.0.0"
displayName: ComfyUI绘画免费版
summary: 本地ComfyUI图像生成工具，支持文生图基础工作流与默认模型，适合个人创作。
license: MIT
edition: free
description: |-
  ComfyUI绘画免费版 —— 面向个人用户的轻量级本地AI图像生成工具。

  核心能力:
  - 文生图（Text-to-Image）：根据文字描述生成图像
  - 基础工作流：内置默认文生图工作流，开箱即用
  - 默认模型支持：使用SD1.5/SDXL等基础模型
  - 图像保存：自动保存生成结果到本地
  - 参数调整：调整采样步数、CFG、种子等基础参数
  - 提示词优化：基础提示词建议与优化

  适用场景:
  - 个人创作者AI绘画探索
  - 设计师快速生成灵感图
  - 学习AI图像生成技术
  - 社交媒体配图生成

  差异化:免费版提供核心文生图能力与基础工作流，适合个人用户快速上手。PRO版本增加自动调参、CivitAI模型管理、批量生成、图生图、ControlNet等高级能力。

  触发关键词: AI绘画, 图像生成, ComfyUI, 文生图, Stable Diffusion, SD, 提示词, 采样, text-to-image
tags:
- AI绘画
- 图像生成
- ComfyUI
- 个人创作
tools:
- read
- exec
---

# ComfyUI绘画免费版

## 概述

ComfyUI绘画免费版是一款面向个人用户的轻量级本地AI图像生成工具，基于ComfyUI工作流引擎实现。提供文生图核心能力，内置默认工作流与基础模型支持，帮助用户通过文字描述快速生成图像。完全本地运行，无需云端API。

## 核心能力

| 能力 | 说明 |
| --- | --- |
| 文生图 | 根据文字描述生成图像 |
| 默认工作流 | 内置标准文生图工作流 |
| 基础模型 | 支持SD1.5、SDXL等基础模型 |
| 参数调整 | 采样步数、CFG、种子、尺寸 |
| 图像保存 | 自动保存到本地目录 |
| 提示词优化 | 基础提示词建议 |

## 使用场景

### 场景一：文生图基础使用

根据文字描述生成图像。

```bash
# 启动ComfyUI服务
cd ComfyUI
python main.py --listen 0.0.0.0 --port 8188

# 使用默认工作流生成图像
python generate.py --prompt "a beautiful sunset over mountains, golden light, photorealistic" \
  --output ./output/sunset.png
```

```python
# Python API调用ComfyUI
import requests
import json

COMFYUI_URL = "http://127.0.0.1:8188"

def generate_image(prompt, negative_prompt="", seed=-1, steps=20, cfg=7.0, 
                    width=512, height=512, model="v1-5-pruned-emaonly.safetensors"):
    """基础文生图"""
    workflow = {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": seed,
                "steps": steps,
                "cfg": cfg,
                "sampler_name": "euler",
                "scheduler": "normal",
                "denoise": 1.0,
                "model": ["4", 0],
                "positive": ["6", 0],
                "negative": ["7", 0],
                "latent_image": ["5", 0]
            }
        },
        "4": {
            "class_type": "CheckpointLoaderSimple",
            "inputs": {"ckpt_name": model}
        },
        "5": {
            "class_type": "EmptyLatentImage",
            "inputs": {"width": width, "height": height, "batch_size": 1}
        },
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": prompt, "clip": ["4", 1]}
        },
        "7": {
            "class_type": "CLIPTextEncode",
            "inputs": {"text": negative_prompt, "clip": ["4", 1]}
        },
        "8": {
            "class_type": "VAEDecode",
            "inputs": {"samples": ["3", 0], "vae": ["4", 2]}
        },
        "9": {
            "class_type": "SaveImage",
            "inputs": {"filename_prefix": "ComfyUI", "images": ["8", 0]}
        }
    }
    
    # 提交工作流
    response = requests.post(f"{COMFYUI_URL}/prompt", json={"prompt": workflow})
    prompt_id = response.json()["prompt_id"]
    
    # 等待完成并获取结果
    # ... 轮询 /history/{prompt_id} 获取结果
    return prompt_id

# 生成图像
generate_image(
    prompt="a beautiful sunset over mountains, golden light, photorealistic",
    negative_prompt="blurry, low quality, distorted",
    steps=20,
    cfg=7.0,
    width=512,
    height=512
)
```

### 场景二：参数调整生成

调整生成参数获得不同效果。

```bash
# 高质量生成（更多步数）
python generate.py \
  --prompt "portrait of a woman, detailed face, soft lighting" \
  --steps 30 \
  --cfg 8.0 \
  --width 768 \
  --height 768 \
  --output ./output/portrait.png

# 快速预览（少步数）
python generate.py \
  --prompt "landscape, mountains, river" \
  --steps 10 \
  --cfg 5.0 \
  --width 512 \
  --height 512 \
  --output ./output/preview.png
```

### 场景三：固定种子复现

使用固定种子复现相同结果。

```bash
# 固定种子生成
python generate.py \
  --prompt "cyberpunk city, neon lights, rain" \
  --seed 42 \
  --steps 25 \
  --output ./output/cyberpunk.png

# 相同种子相同结果
python generate.py \
  --prompt "cyberpunk city, neon lights, rain" \
  --seed 42 \
  --steps 25 \
  --output ./output/cyberpunk_copy.png
```

## 快速开始

### 1. 安装ComfyUI

```bash
# 克隆ComfyUI
git clone https://github.com/comfyanonymous/ComfyUI
cd ComfyUI

# 安装依赖
pip install -r requirements.txt
```

### 2. 下载基础模型

```bash
# 下载SD1.5模型
cd models/checkpoints
wget https://huggingface.co/runwayml/stable-diffusion-v1-5/resolve/main/v1-5-pruned-emaonly.safetensors
```

### 3. 启动并生成

```bash
# 启动ComfyUI
python main.py --listen 0.0.0.0 --port 8188

# 生成第一张图像
python generate.py --prompt "a cat sitting on a windowsill" --output ./output/cat.png
```

## 配置示例

### 基础生成参数

| 参数 | 默认值 | 说明 | 推荐范围 |
| --- | --- | --- | --- |
| `steps` | 20 | 采样步数 | 10-50 |
| `cfg` | 7.0 | CFG Scale | 5.0-15.0 |
| `seed` | -1 | 随机种子 | -1或正整数 |
| `width` | 512 | 图像宽度 | 512-1024 |
| `height` | 512 | 图像高度 | 512-1024 |
| `sampler` | euler | 采样器 | euler/euler_a/dpmpp_2m |

### 支持的基础模型

| 模型 | 类型 | 显存需求 | 说明 |
| --- | --- | --- | --- |
| SD 1.5 | 基础 | 4GB+ | 经典模型，速度快 |
| SDXL | 基础 | 8GB+ | 高质量，分辨率大 |
| SDXL Turbo | 快速 | 6GB+ | 极速生成 |

### 采样器对比

| 采样器 | 速度 | 质量 | 特点 |
| --- | --- | --- | --- |
| euler | 快 | 中 | 基础采样 |
| euler_a | 快 | 中高 | 带噪声调度 |
| dpmpp_2m | 中 | 高 | 推荐常用 |
| dpmpp_sde | 慢 | 最高 | 质量最佳 |

## 最佳实践

1. **提示词结构**：主体 + 场景 + 风格 + 质量，如"cat, on windowsill, photo, high quality"
2. **负面提示词**：始终添加负面提示词，排除不想要的元素
3. **步数选择**：快速预览用10-15步，高质量用25-35步
4. **CFG调整**：CFG值越高越遵循提示词，但过高会过曝
5. **尺寸控制**：SD1.5推荐512x512，SDXL推荐1024x1024
6. **种子管理**：满意的结果记录种子，便于复现与微调

## 常见问题

### Q1：显存不足怎么办？

降低图像尺寸（如512x512），减少采样步数，或使用SD1.5而非SDXL。关闭其他占显存的程序。

### Q2：生成结果不理想怎么办？

优化提示词，增加细节描述。调整CFG值（7-9通常效果较好）。尝试不同采样器。

### Q3：免费版支持图生图吗？

免费版仅支持文生图。图生图功能需要升级至PRO版本。

### Q4：可以使用自定义模型吗？

免费版支持基础模型。自定义模型（如CivitAI下载的模型）需要升级至PRO版本。

### Q5：生成速度慢怎么办？

减少采样步数，使用SD1.5模型，或使用SDXL Turbo快速模型。确保GPU驱动为最新版本。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上
- **GPU**: NVIDIA GPU（推荐4GB+显存）或CPU（速度较慢）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| ComfyUI | 工作流引擎 | 必需 | ComfyUI项目下载 |
| PyTorch | 深度学习框架 | 必需 | `pip install torch` |
| requests | Python库 | 必需 | `pip install requests` |
| 基础模型 | AI模型 | 必需 | HuggingFace下载 |

### API Key 配置

- 免费版完全本地运行，无需任何API Key
- ComfyUI通过本地HTTP API通信（默认端口8188）

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行AI图像生成任务。核心功能通过Python脚本调用本地ComfyUI API实现，无需云端服务。
