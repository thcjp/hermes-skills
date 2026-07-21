---
slug: grok-image
name: grok-image
version: "1.0.0"
displayName: Grok图片生成-专业版
summary: 批量AI图片生成引擎，支持多格式导出、消息平台集成与自动化工作流。
license: Proprietary
edition: pro
description: |-
  Grok图片生成工具专业版。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
- ImageGeneration
- Enterprise
- Automation
tools:
  - - read
- exec
---
# Grok图片生成-专业版

## 核心能力

### 能力对比

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 生成模式 | 单张 | 批量队列 |
| 输出格式 | JPG（默认） | PNG/JPG/WebP |
| 保存路径 | Downloads | 自定义路径 |
| 文件命名 | 随机 | 规则化命名 |
| 消息集成 | 不支持 | 飞书等平台发送 |
| 提示词管理 | 无 | 模板库 |
| 工作流 | 手动 | 自动化编排 |
| 后处理 | 无 | 压缩/裁剪/水印 |

### 核心能力

```text
批量生成:
  - 提示词队列自动处理
  - 生成间隔控制（避免限流）
  - 失败重试机制
  - 进度追踪与日志

多格式导出:
  - PNG（无损，透明背景）
  - JPG（压缩，小体积）
  - WebP（现代格式，高质量低体积）
  - 格式自动转换

消息平台集成:
  - 飞书即时发送
  - 自定义消息描述
  - 批量发送多张图片
  - 发送状态追踪

提示词管理:
  - 模板库（主题/风格/氛围）
  - 变量替换（（根据实际场景填充） （根据实际场景填充））
  - 历史记录
  - 收藏与复用

工作流自动化:
  - 生成 → 保存 → 后处理 → 发送
  - 条件分支
  - 定时执行
  - Webhook 触发

图片后处理:
  - 压缩优化
  - 自动裁剪
  - 水印添加
  - 尺寸调整
```

## 适用场景

### 场景一：批量社交媒体配图

为社交媒体批量生成配图并自动分发。

```python
# 批量图片生成工作流
import time
from pathlib import Path

class BatchImageWorkflow:
    """批量图片生成工作流"""

    def __init__(self, output_dir="./generated-images"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.results = []

    def process_batch(self, prompt_queue, interval=15):
        """批量处理提示词队列"""
        for i, prompt_data in enumerate(prompt_queue):
            print(f"[{i+1}/{len(prompt_queue)}] 生成: {prompt_data['name']}")

            result = self._generate_single(prompt_data)
            self.results.append(result)

            # 生成间隔（避免限流）
            if i < len(prompt_queue) - 1:
                print(f"等待 {interval} 秒...")
                time.sleep(interval)

        return self.results

    def _generate_single(self, prompt_data):
        """生成单张图片"""
        # 第1步: 打开 Grok Imagine
        # playwright: open https://grok.com/imagine

        # 第2步: 输入提示词
        prompt = self._build_prompt(prompt_data)
        # playwright: type prompt into input

        # 第3步: 点击生成
        # playwright: click generate button

        # 第4步: 等待生成
        time.sleep(10)

        # 第5步: 保存图片
        # desktop-agent: right-click → save as

        # 第6步: 重命名文件
        filename = f"{prompt_data['name']}.jpg"
        # rename downloaded file to custom path

        return {
            "id": f"img-{prompt_data['name']}",
            "name": prompt_data["name"],
            "prompt": prompt,
            "file_path": str(self.output_dir / filename),
            "status": "completed"
        }

    def _build_prompt(self, data):
        """构建提示词"""
        template = data.get("template", "{subject}，{style}风格，{mood}氛围")
        return template.format(
            subject=data.get("subject", ""),
            style=data.get("style", ""),
            mood=data.get("mood", "")
        )

    def send_to_feishu(self, image_paths, message=""):
        """发送图片到飞书"""
        for path in image_paths:
            # message tool: send image to feishu
            print(f"已发送: {path}")

# 批量生成配置
queue = [
    {"name": "spring-landscape", "subject": "春天的山水风景",
     "style": "水彩", "mood": "清新"},
    {"name": "summer-beach", "subject": "夏日海滩",
     "style": "印象派", "mood": "热烈"},
    {"name": "autumn-forest", "subject": "秋天森林",
     "style": "油画", "mood": "温暖"},
    {"name": "winter-city", "subject": "冬日城市",
     "style": "赛博朋克", "mood": "冷峻"},
]

workflow = BatchImageWorkflow("./social-media-images")
results = workflow.process_batch(queue, interval=15)

# 发送到飞书
image_paths = [r["file_path"] for r in results]
workflow.send_to_feishu(image_paths, "本季四景配图已生成")
```

### 场景二：提示词模板管理

使用模板库管理和复用提示词。

```python
# 提示词模板管理系统
class PromptTemplateManager:
    """提示词模板管理器"""

    def __init__(self):
        self.templates = {
            "product-shot": {
                "template": "{product}产品特写，{background}背景，{lighting}灯光，超写实",
                "variables": ["product", "background", "lighting"]
            },
            "landscape": {
                "template": "{season}的{scene}，{style}风格，{mood}氛围",
                "variables": ["season", "scene", "style", "mood"]
            },
            "character-portrait": {
                "template": "{character}肖像，{art_style}风格，{expression}表情，{background}背景",
                "variables": ["character", "art_style", "expression", "background"]
            },
            "abstract-art": {
                "template": "抽象艺术：{concept}，{color_scheme}配色，{technique}技法",
                "variables": ["concept", "color_scheme", "technique"]
            }
        }
        self.history = []

    def generate_from_template(self, template_name, variables):
        """从模板生成提示词"""
        template = self.templates[template_name]["template"]
        prompt = template.format(**variables)
        self.history.append({
            "template": template_name,
            "variables": variables,
            "prompt": prompt
        })
        return prompt

    def batch_from_template(self, template_name, variable_sets):
        """从模板批量生成提示词"""
        prompts = []
        for variables in variable_sets:
            prompt = self.generate_from_template(template_name, variables)
            prompts.append(prompt)
        return prompts

# 使用模板批量生成
manager = PromptTemplateManager()

# 产品图模板批量
product_prompts = manager.batch_from_template("product-shot", [
    {"product": "无线耳机", "background": "深色", "lighting": "戏剧性"},
    {"product": "智能手表", "background": "白色", "lighting": "柔和"},
    {"product": "机械键盘", "background": "木质", "lighting": "暖色"},
    {"product": "游戏鼠标", "background": "霓虹", "lighting": "RGB"},
])

for p in product_prompts:
    print(f"提示词: {p}")
```

### 场景三：自动化工作流编排

完整的生成→保存→后处理→发送工作流。

```bash
#!/bin/bash
# 完整自动化工作流脚本

OUTPUT_DIR="./workflow-output"
WATERMARK="./watermark.png"

mkdir -p "$OUTPUT_DIR"

# 第1步: 批量生成图片
echo "=== 第1步: 批量生成图片 ==="
PROMPTS=("夏日海滩日落" "秋日森林小径" "冬日雪景城市" "春日樱花公园")

for i in "${!PROMPTS[@]}"; do
    echo "生成第 $((i+1)) 张: ${PROMPTS[$i]}"
    # 浏览器自动化: 打开Grok → 输入提示词 → 生成 → 保存
    # ... (浏览器操作代码)
    sleep 12  # 等待生成

    # 重命名文件
    mv ~/Downloads/latest.jpg "$OUTPUT_DIR/season-$((i+1)).jpg"
    echo "已保存: $OUTPUT_DIR/season-$((i+1)).jpg"

    # 生成间隔
    sleep 5
done

# 第2步: 图片后处理
echo "=== 第2步: 图片后处理 ==="
for img in "$OUTPUT_DIR"/*.jpg; do
    # 添加水印（如有ImageMagick）
    if command -v convert &> /dev/null; then
        convert "$img" "$WATERMARK" -gravity bottom-right -composite "$img"
        echo "已添加水印: $img"
    fi
done

# 第3步: 发送到飞书
echo "=== 第3步: 发送到飞书 ==="
for img in "$OUTPUT_DIR"/*.jpg; do
    # message工具发送
    echo "已发送: $img"
done

echo "=== 工作流完成 ==="
ls -la "$OUTPUT_DIR/"
```

## 使用流程

### 优秀步：配置输出目录

```bash
# 创建自定义输出目录
mkdir -p ./generated-images
mkdir -p ./generated-images/png
mkdir -p ./generated-images/jpg
mkdir -p ./generated-images/webp
```

### 第二步：准备提示词队列

```python
# 准备批量提示词
prompts = [
    {"name": "img-001", "prompt": "描述文本1"},
    {"name": "img-002", "prompt": "描述文本2"},
    {"name": "img-003", "prompt": "描述文本3"},
]
```

### 第三步：执行批量工作流

```bash
# 运行批量生成工作流
python3 batch_workflow.py --queue prompts.json --output ./generated-images --interval 15
```

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
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **浏览器**: Chrome/Edge（浏览器自动化需要）
- **Python**: 3.8+（批量工作流脚本需要）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Playwright/浏览器工具 | 工具 | 必需 | Agent内置或插件安装 |
| desktop-agent | 工具 | 必需 | `uvx desktop-agent`（自动安装） |
| Grok 账号 | 服务 | 必需 | grok.com 注册 |
| ImageMagick（可选） | 工具 | 可选 | 用于图片后处理（水印/压缩） |
| Python 3.8+ | 运行时 | 推荐 | 批量工作流脚本运行 |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- 需要已登录的 Grok 账号（浏览器会话）
- 飞书发送需要配置消息工具（如需）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令 + 命令行 + 浏览器自动化）
- **说明**: 企业级AI Skill，支持批量图片生成、多格式导出与消息平台集成
- **适用规模**: 内容团队，批量图片生产与分发
- **兼容性**: 与免费版单张生成完全兼容，支持无缝升级

## 案例展示

### 批量生成配置

```json
{
  "batch_config": {
    "output_dir": "./generated-images",
    "interval_seconds": 15,
    "max_retries": 3,
    "format": "jpg",
    "naming_rule": "{template}-{index:03d}"
  },
  "prompt_queue": [
    {"name": "spring", "template": "landscape", "variables": {"season": "春天", "scene": "花园", "style": "水彩", "mood": "清新"}},
    {"name": "summer", "template": "landscape", "variables": {"season": "夏天", "scene": "海滩", "style": "印象派", "mood": "热烈"}}
  ]
}
```

### 飞书发送配置

```json
{
  "feishu_config": {
    "enabled": true,
    "message_template": "图片描述: {description}",
    "batch_send": true,
    "send_interval": 2,
    "image_path": "./generated-images"
  }
}
```

### 提示词模板库

```json
{
  "templates": {
    "product-shot": "{product}产品特写，{background}背景，{lighting}灯光",
    "landscape": "{season}的{scene}，{style}风格，{mood}氛围",
    "character-portrait": "{character}肖像，{art_style}风格，{expression}表情",
    "social-media": "{subject}，{style}风格，{mood}氛围，适合{platform}分享"
  }
}
```

## 常见问题

### Q: 批量生成间隔多少合适？

A: 建议 15 秒以上，避免触发 Grok Imagine 的频率限制。如果遇到限流，增加到 30 秒。

### Q: 如何发送图片到飞书？

A: 先将图片保存到本地目录，然后使用消息工具发送。支持自定义消息描述和批量发送。

### Q: 支持哪些输出格式？

A: 支持 PNG（无损透明）、JPG（压缩小体积）和 WebP（现代格式）。可在配置中指定，默认 JPG。

### Q: 如何从免费版升级？

A: 免费版的单张生成和保存流程在专业版中完整保留。专业版新增批量队列、模板管理和消息集成，无需迁移已有配置。

### Q: 生成失败怎么办？

A: 专业版内置失败重试机制（默认 3 次）。如果重试仍失败，检查网络连接、Grok 账号状态和页面 DOM 是否变化。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 
- 
- 
