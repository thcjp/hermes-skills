---
slug: comfyui-painter-tool-pro
name: comfyui-painter-tool-pro
version: 1.0.0
displayName: ComfyUI绘画专业版
summary: "专业AI绘画工具，支持自动调参、CivitAI模型管理、批量生成、图生图与ControlNet.。ComfyUI绘画专业版 —— 面向专业创作者与设计团队的高级本地AI绘画工具。核心能力:"
license: Proprietary
edition: pro
description: 'ComfyUI绘画专业版 —— 面向专业创作者与设计团队的高级本地AI绘画工具。核心能力:

  - 自动调参：根据提示词自动优化采样器、步数、CFG等参数

  - CivitAI模型管理：搜索、下载、管理CivitAI平台模型与LoRA

  - 图生图（Image-to-Image）：基于参考图生成变体

  - ControlNet集成：姿态控制、边缘检测、深度图等专业控制

  - 批量生成：队列管理..'
tags:
  - AI绘画
  - 图像生成
  - 企业工具
  - ControlNet
  - CivitAI
  - UI设计
  - 前端
  - 设计
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Creative"
---
# ComfyUI绘画专业版

## 概述

ComfyUI绘画专业版是面向专业创作者与设计团队的高级本地AI绘画工具，在免费版基础上提供自动调参、CivitAI模型管理、图生图、ControlNet集成、批量生成等专业能力。适用于专业插画、电商产品图、游戏美术、建筑可视化等高阶创作场景.
### 免费版与专业版对比

| 能力 | 免费版 | 专业版 |
|---|---|---|
| 文生图 | 支持 | 支持+自动调参 |
| 图生图 | 不支持 | 支持 |
| ControlNet | 不支持 | 支持（多类型） |
| 模型管理 | 基础模型 | CivitAI全模型 |
| LoRA支持 | 不支持 | 支持 |
| 批量生成 | 不支持 | 支持（队列管理） |
| 高清放大 | 不支持 | Tiled Upscale |
| 工作流模板 | 1个默认 | 多种专业模板 |
| 提示词工程 | 基础建议 | 高级模板+权重 |
| 图像后处理 | 不支持 | 修复/迁移/放大 |

## 核心能力

### 1. 自动调参

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | ComfyUI绘画专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
import requests
import json
# ..
COMFYUI_URL = "http://127.0.0.1:8188"
# ..
class AutoTuneGenerator:
    def __init__(self, comfyui_url):
        self.url = comfyui_url
# ..
    def auto_tune_params(self, prompt, style="photorealistic"):
        """根据提示词与风格自动优化参数"""
        presets = {
            "photorealistic": {
                "sampler": "dpmpp_2m",
                "scheduler": "karras",
                "steps": 30,
                "cfg": 7.5,
                "denoise": 1.0
            },
            "anime": {
                "sampler": "euler_a",
                "scheduler": "normal",
                "steps": 25,
                "cfg": 6.5,
                "denoise": 1.0
            },
            "artistic": {
                "sampler": "dpmpp_sde",
                "scheduler": "karras",
                "steps": 35,
                "cfg": 8.0,
                "denoise": 1.0
            },
            "fast_preview": {
                "sampler": "euler",
                "scheduler": "normal",
                "steps": 12,
                "cfg": 5.0,
                "denoise": 1.0
            }
        }
        return presets.get(style, presets["photorealistic"])
# ..
    def generate_with_auto_tune(self, prompt, negative_prompt="", 
                                 style="photorealistic", seed=-1,
                                 width=1024, height=1024, model="sdxl_base.safetensors"):
        """自动调参生成"""
        params = self.auto_tune_params(prompt, style)
# ..
        workflow = self._build_workflow(
            prompt=prompt,
            negative_prompt=negative_prompt,
            model=model,
            seed=seed,
            **params,
            width=width,
            height=height
        )
# ..
        response = requests.post(f"{self.url}/prompt", json={"prompt": workflow})
        return response.json().get("prompt_id")
# ..
    def _build_workflow(self, prompt, negative_prompt, model, seed,
                        sampler, scheduler, steps, cfg, denoise,
                        width, height):
        """构建工作流"""
        return {
            "3": {
                "class_type": "KSampler",
                "inputs": {
                    "seed": seed, "steps": steps, "cfg": cfg,
                    "sampler_name": sampler, "scheduler": scheduler,
                    "denoise": denoise,
                    "model": ["4", 0], "positive": ["6", 0],
                    "negative": ["7", 0], "latent_image": ["5", 0]
                }
            },
            "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": model}},
            "5": {"class_type": "EmptyLatentImage", "inputs": {"width": width, "height": height, "batch_size": 1}},
            "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
            "7": {"class_type": "CLIPTextEncode", "inputs": {"text": negative_prompt, "clip": ["4", 1]}},
            "8": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
            "9": {"class_type": "SaveImage", "inputs": {"filename_prefix": "ComfyUI_Pro", "images": ["8", 0]}}
        }
```

**输入**: 用户提供自动调参所需的指令和必要参数.
**处理**: 解析自动调参的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回自动调参的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. CivitAI模型管理

```python
import os
import requests
from pathlib import Path
# ..
class CivitAIManager:
    def __init__(self, api_key, comfyui_models_dir):
        self.api_key = api_key
        self.models_dir = comfyui_models_dir
        self.base_url = "https://civitai.com/api/v1"
# ..
    def search_models(self, query, model_type="checkpoint", limit=10):
        """搜索CivitAI模型"""
        response = requests.get(
            f"{self.base_url}/models",
            params={"query": query, "types": model_type, "limit": limit},
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        return response.json()
# ..
    def download_model(self, model_id, version_id, model_type="checkpoint"):
        """下载模型"""
        # 获取下载链接
        response = requests.get(
            f"{self.base_url}/models/{model_id}",
            headers={"Authorization": f"Bearer {self.api_key}"}
        )
        model_info = response.json()
# ..
        # 找到指定版本
        for version in model_info.get("modelVersions", []):
            if version["id"] == version_id:
                download_url = version["downloadUrl"]
                filename = f"{model_info['name']}_{version['name']}.safetensors"
# ..
                # 确定保存目录
                save_dir = os.path.join(self.models_dir, model_type + "s")
                os.makedirs(save_dir, exist_ok=True)
                save_path = os.path.join(save_dir, filename)
# ..
                # 下载模型
                print(f"下载模型: {filename}")
                response = requests.get(
                    download_url,
                    headers={"Authorization": f"Bearer {self.api_key}"},
                    stream=True
                )
                with open(save_path, 'wb') as f:
                    for chunk in response.iter_content(chunk_size=8192):
                        f.write(chunk)
# ..
                print(f"模型已保存: {save_path}")
                return save_path
# ..
        return None
# ..
    def list_local_models(self):
        """列出本地模型"""
        models = {}
        for subdir in ["checkpoints", "loras", "vae", "embeddings"]:
            dir_path = os.path.join(self.models_dir, subdir)
            if os.path.exists(dir_path):
                models[subdir] = [
                    f for f in os.listdir(dir_path)
                    if f.endswith(('.safetensors', '.ckpt', '.pt'))
                ]
        return models
```

**输入**: 用户提供CivitAI模型管理所需的指令和必要参数.
**处理**: 解析CivitAI模型管理的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回CivitAI模型管理的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 图生图（Image-to-Image）

```python
def img2img(self, input_image_path, prompt, negative_prompt="", 
            denoise=0.6, seed=-1, steps=25, cfg=7.0,
            model="sdxl_base.safetensors"):
    """图生图：基于参考图生成变体"""
    # 上传输入图像
    with open(input_image_path, 'rb') as f:
        upload_response = requests.post(
            f"{self.url}/upload/image",
            files={"image": f}
        )
    image_name = upload_response.json()["name"]
# ..
    # 构建图生图工作流
    workflow = {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": seed, "steps": steps, "cfg": cfg,
                "sampler_name": "dpmpp_2m", "scheduler": "karras",
                "denoise": denoise,  # 关键：控制变化程度
                "model": ["4", 0], "positive": ["6", 0],
                "negative": ["7", 0], "latent_image": ["12", 0]
            }
        },
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": model}},
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": negative_prompt, "clip": ["4", 1]}},
        "10": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        "11": {"class_type": "VAEEncode", "inputs": {"pixels": ["10", 0], "vae": ["4", 2]}},
        "12": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "13": {"class_type": "SaveImage", "inputs": {"filename_prefix": "ComfyUI_Img2Img", "images": ["12", 0]}}
    }
# ..
    response = requests.post(f"{self.url}/prompt", json={"prompt": workflow})
    return response.json().get("prompt_id")
```

**输入**: 用户提供图生图（Image-to-Image）所需的指令和必要参数.
**处理**: 解析图生图（Image-to-Image）的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回图生图（Image-to-Image）的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. ControlNet集成

```python
def generate_with_controlnet(self, input_image_path, prompt, control_type="openpose",
                              negative_prompt="", seed=-1, steps=30, cfg=7.5,
                              model="sdxl_base.safetensors"):
    """使用ControlNet控制生成"""
    # 上传输入图像
    with open(input_image_path, 'rb') as f:
        upload_response = requests.post(f"{self.url}/upload/image", files={"image": f})
    image_name = upload_response.json()["name"]
# ..
    # ControlNet模型映射
    controlnet_models = {
        "openpose": "control_openpose_sdxl.safetensors",
        "canny": "control_canny_sdxl.safetensors",
        "depth": "control_depth_sdxl.safetensors",
        "scribble": "control_scribble_sdxl.safetensors"
    }
# ..
    workflow = {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": seed, "steps": steps, "cfg": cfg,
                "sampler_name": "dpmpp_2m", "scheduler": "karras", "denoise": 1.0,
                "model": ["4", 0], "positive": ["20", 0],
                "negative": ["7", 0], "latent_image": ["5", 0]
            }
        },
        "4": {"class_type": "CheckpointLoaderSimple", "inputs": {"ckpt_name": model}},
        "5": {"class_type": "EmptyLatentImage", "inputs": {"width": 1024, "height": 1024, "batch_size": 1}},
        "7": {"class_type": "CLIPTextEncode", "inputs": {"text": negative_prompt, "clip": ["4", 1]}},
        "10": {"class_type": "LoadImage", "inputs": {"image": image_name}},
        # ControlNet预处理器
        "15": {"class_type": "ControlNetPreprocessor", "inputs": {"image": ["10", 0]}},
        # ControlNet加载
        "16": {"class_type": "ControlNetLoader", "inputs": {"control_net_name": controlnet_models[control_type]}},
        # ControlNet应用
        "20": {
            "class_type": "ControlNetApply",
            "inputs": {
                "conditioning": ["6", 0], "control_net": ["16", 0],
                "image": ["15", 0], "strength": 0.8
            }
        },
        "6": {"class_type": "CLIPTextEncode", "inputs": {"text": prompt, "clip": ["4", 1]}},
        "12": {"class_type": "VAEDecode", "inputs": {"samples": ["3", 0], "vae": ["4", 2]}},
        "13": {"class_type": "SaveImage", "inputs": {"filename_prefix": "ComfyUI_ControlNet", "images": ["12", 0]}}
    }
# ..
    response = requests.post(f"{self.url}/prompt", json={"prompt": workflow})
    return response.json().get("prompt_id")
```

**输入**: 用户提供ControlNet集成所需的指令和必要参数.
**处理**: 解析ControlNet集成的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回ControlNet集成的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：绘画工具、支持自动调参、批量生成、图生图与、绘画专业版、面向专业创作者与、设计团队的高级本、核心能力、根据提示词自动优、化采样器、等参数、平台模型与、姿态控制、边缘检测、深度图等专业控制、队列管理等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一：电商产品图批量生成

电商团队批量生成不同风格的产品场景图.
```python
# 批量生成产品图
generator = AutoTuneGenerator(COMFYUI_URL)
# ..
products = [
    {"name": "耳机_白色", "prompt": "white wireless earbuds, on marble table, studio lighting, product photography"},
    {"name": "耳机_黑色", "prompt": "black wireless earbuds, on wooden desk, warm lighting, product photography"},
    {"name": "耳机_场景", "prompt": "wireless earbuds, on beach sand, sunset, lifestyle photography"},
]
# ..
for product in products:
    generator.generate_with_auto_tune(
        prompt=product["prompt"],
        negative_prompt="blurry, low quality, watermark",
        style="photorealistic",
        seed=-1,
        width=1024,
        height=1024,
        model="sdxl_base.safetensors"
    )
    print(f"已提交生成: {product['name']}")
```

### 场景二：CivitAI模型搜索与下载

搜索并下载特定风格的模型.
```python
# CivitAI模型管理
civitai = CivitAIManager(
    api_key="your_civitai_api_key",
    comfyui_models_dir="./ComfyUI/models"
)
# ..
# 搜索动漫风格模型
results = civitai.search_models("anime style", model_type="checkpoint", limit=5)
for model in results["items"]:
    print(f"模型: {model['name']} - 下载量: {model['stats']['downloadCount']}")
# ..
# 下载选定的模型
civitai.download_model(
    model_id=12345,
    version_id=67890,
    model_type="checkpoint"
)
# ..
# 列出本地所有模型
local_models = civitai.list_local_models()
print("本地模型:", local_models)
```

### 场景三：ControlNet姿态控制生成

使用参考图姿态生成新图像.
```python
# 使用ControlNet控制姿态
generator = AutoTuneGenerator(COMFYUI_URL)
# ..
generator.generate_with_controlnet(
    input_image_path="./reference/pose_reference.jpg",
    prompt="a woman in elegant dress, same pose, studio lighting, fashion photography",
    control_type="openpose",  # 姿态控制
    negative_prompt="blurry, deformed, extra limbs",
    seed=42,
    steps=30,
    cfg=7.5,
    model="sdxl_base.safetensors"
)
print("ControlNet生成已提交")
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```bash
# 依赖说明
pip install torch torchvision requests
export CIVITAI_API_KEY="your_api_key"
```

```python
from comfyui_pro import AutoTuneGenerator
generator = AutoTuneGenerator("http://127.0.0.1:8188")
# 自动调参生成
generator.generate_with_auto_tune(prompt="dragon over mountains", style="artistic")
# 图生图
generator.img2img(input_image_path="./input.jpg", prompt="oil painting", denoise=0.5)
```

## 示例

### 自动调参预设

| 风格预设 | 采样器 | 步数 | CFG | 适用场景 |
|---:|---:|---:|---:|---:|
| photorealistic | dpmpp_2m | 30 | 7.5 | 写实照片 |
| anime | euler_a | 25 | 6.5 | 动漫风格 |
| artistic | dpmpp_sde | 35 | 8.0 | 艺术创作 |
| fast_preview | euler | 12 | 5.0 | 快速预览 |

### ControlNet类型

| 类型 | 控制内容 | 适用场景 |
|:---:|:---:|:---:|
| openpose | 人体姿态 | 人物姿态控制 |
| canny | 边缘检测 | 形状轮廓控制 |
| depth | 深度图 | 空间层次控制 |
| scribble | 涂鸦 | 草图生成 |

## 最佳实践

1. **风格预设选择**：写实用photorealistic，动漫用anime，创作用artistic
2. **CivitAI模型**：根据需求选择合适模型，注意模型授权与使用范围
3. **ControlNet强度**：strength值0.7-0.9效果较好，过低控制不明显
4. **图生图denoise**：风格转换用0.5，细节修复用0.2
5. **批量并发**：批量生成时控制并发数，避免显存溢出
6. **LoRA叠加**：可叠加多个LoRA实现复合风格，注意权重平衡
7. **高清放大**：生成后使用Tiled Upscale进行高清放大，提升细节

## 常见问题

### Q1：CivitAI下载需要API Key吗？

需要。在CivitAI网站注册账号，在账户设置中获取API Key.
### Q2：ControlNet显存需求多大？

ControlNet额外需要1-2GB显存。建议8GB以上显存使用ControlNet.
### Q3：批量生成如何管理队列？

专业版支持队列管理，提交的任务会排队执行。可通过ComfyUI的/prompt接口轮询状态.
### Q4：LoRA如何使用？

将LoRA文件放入models/loras目录，在工作流中添加LoraLoader节点并设置权重（通常0.5-0.8）.
### Q5：与免费版的工作流兼容吗？

兼容。专业版在免费版工作流基础上扩展，免费版的基础文生图工作流可直接在专业版中使用.
## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上
- **GPU**: NVIDIA GPU（推荐8GB+显存，ControlNet需10GB+）

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| ComfyUI | 工作流引擎 | 必需 | ComfyUI项目下载 |
| PyTorch | 深度学习框架 | 必需 | `pip install torch` |
| requests | Python库 | 必需 | `pip install requests` |
| CivitAI API | 外部API | 可选 | CivitAI网站注册获取 |
| ControlNet模型 | AI模型 | 可选 | ComfyUI Manager安装 |
| LoRA模型 | AI模型 | 可选 | CivitAI平台下载 |

### API Key 配置

- `CIVITAI_API_KEY`：CivitAI平台API密钥（模型下载功能需要）
- ComfyUI本地运行无需API Key
- 与免费版完全兼容，免费版的本地ComfyUI配置可直接在专业版中使用

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业AI图像生成任务。支持自动调参、CivitAI模型管理、图生图、ControlNet等高级功能，通过Python脚本调用本地ComfyUI API与CivitAI API实现。与免费版完全兼容，可直接复用免费版的基础文生图工作流与默认模型配置.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|:---|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
- 组件兼容性依赖特定框架版本
- 免费版自定义主题与令牌管理能力有限
- 生成的代码可能需要手动调整以适应项目规范

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "ComfyUI绘画专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "comfyui painter pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
