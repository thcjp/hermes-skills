---
slug: "doubao-image-gen"
name: "doubao-image-gen"
version: 1.0.1
displayName: "豆包图片生成-专业版"
summary: "企业级AI图片生成平台，支持批量生成、多比例输出、风格预设、提示词增强与工作流自动化。"
license: "Proprietary"
edition: "pro"
description: |-
  豆包图片生成专业版。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务。Use when 需要提升效率、自动化流程、批量处理、工作流优化时使用。不适用于需要人工创意判断的任务.
tags:
  - Creative
  - AI绘图
  - 图片生成
  - 专业版
  - 批量处理
  - 企业级
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "图像处理,AI绘图,创意"
category: "Creative"
---
# 豆包图片生成-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 豆包图片生成-专业版企业级AI图片生成 | 不支持 | 支持 |
| 豆包图片生成-专业版支持批量生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

### 1. 批量图片生成
支持单任务生成 50+ 图片：

```text
输入生成清单（CSV/JSON）
      ↓
任务调度器分配并行生成
      ↓
多浏览器实例并行执行
      ↓
失败重试 + 结果聚合
      ↓
生成批量报告
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `批量图片生成` 选项
- 处理流程: 接收输入 -> 执行批量图片生成 -> 返回结果
- 输入: 用户提供批量图片生成所需的参数和指令
- 输出: 返回批量图片生成的处理结果,包含执行状态码、结果数据和执行日志

### 2. 多比例同时输出
一次提示词生成多种比例版本：

| 比例 | 适用场景 |
|:-----|:-----|
| 3:4 | 竖版社交媒体 |
| 1:1 | 方形头像/商品图 |
| 4:3 | 横版配图 |
| 16:9 | 宽屏壁纸 |
| 9:16 | 手机壁纸/故事 |
| 2:3 | 海报 |
| 3:2 | 横版海报 |

**输入**: 用户提供多比例同时输出所需的指令和必要参数.
**处理**: 解析多比例同时输出的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 3. 风格预设管理
预设风格模板，保障视觉一致性：

- 预设风格库（写实/卡通/油画/水彩等）
- 品牌专属风格模板
- 风格参数自定义
- 跨项目风格复用

**处理**: 解析风格预设管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回风格预设管理的处理结果,包含执行状态码、结果数据和执行日志.
### 4. 提示词增强
AI 自动优化提示词：

- 自动补充细节描述
- 风格关键词增强
- 负面提示词生成
- 多语言提示词支持

**输入**: 用户提供提示词增强所需的指令和必要参数.
**处理**: 解析提示词增强的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 5. 参考图生成
基于参考图进行风格迁移：

- 上传参考图
- 提取风格特征
- 应用到新内容生成
- 保留参考图风格一致性

**输入**: 用户提供参考图生成所需的指令和必要参数.
**处理**: 解析参考图生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 6. 工作流自动化
完整自动化生产流程：

```text
需求输入 → 提示词增强 → 批量生成 → 多比例输出 → 质量评估 → 自动归档
```

#
## 适用场景

> 详细内容已移至 `references/detail.md` - ### 场景 1：电商商品图批量生成
### 场景 2：品牌营销素材规模化生产
某品牌需要为营销活动生成一系列风格统一的素材图.
**风格预设配置 `brand-style.json`：**

```json
{
  "name": "品牌统一风格",
  "description": "科技感 暖色调 简约风",
  "style_keywords": ["科技感", "暖色调", "简约", "高级感"],
  "negative_keywords": ["复杂背景", "低质感"],
  "default_ratio": "3:4",
  "quality": "high"
}
```

**批量生成配置：**

> 详细代码示例已移至 `references/detail.md`

### 场景 3：参考图风格迁移
某设计师希望基于一张参考图的风格，生成新的设计图.
**操作步骤：**

1. 上传参考图
2. 描述新内容需求
3. 系统提取参考图风格
4. 生成风格一致的新图

**示例配置：**

```json
{
  "project": "风格迁移设计",
  "reference_image": "/images/style-reference.jpg",
  "items": [
    {"prompt": "客厅场景", "preserve_style": true},
    {"prompt": "卧室场景", "preserve_style": true},
    {"prompt": "厨房场景", "preserve_style": true}
  ]
}
```

### 场景 4：提示词增强与优化
用户输入简单提示词，AI 自动增强为详细描述.
**操作步骤：**

1. 用户输入：「一只猫」
2. AI 增强提示词
3. 用户确认增强后的提示词
4. 生成图片

**示例流程：**

```bash
python3 prompt_enhancer.py \
  --input "一只猫" \
  --style-preset "photorealistic" \
  --output /tmp/enhanced-prompt.txt
# ...
```

## 使用流程

### 优秀步：环境检查
```bash
python3 --version
# ...
google-chrome --version
# ...
ls ~/.skill-platform/workspace/
```

### 第二步：批量生成示例
创建生成清单：

```json
[
  {"id": "img-1", "prompt": "现代客厅 3:4", "ratios": ["3:4"]},
  {"id": "img-2", "prompt": "极简卧室 1:1", "ratios": ["1:1"]}
]
```

执行批量生成：

```bash
python3 batch_generate.py \
  --config /tmp/items.json \
  --output-dir /tmp/generated/ \
  --parallel 8 \
  --enhance-prompt
```

### 第三步：多比例输出
```bash
python3 batch_generate.py \
  --config /tmp/items.json \
  --ratios "3:4,1:1,16:9" \
  --output-dir /tmp/multi-ratio/
```

### 第四步：使用风格预设
```bash
python3 batch_generate.py \
  --config /tmp/items.json \
  --style-preset /config/brand-style.json \
  --output-dir /tmp/branded/
```

### 第五步：提示词增强
```bash
python3 prompt_enhancer.py \
  --input "咖啡店" \
  --output /tmp/enhanced.txt
# ...
python3 prompt_enhancer.py \
  --batch /tmp/prompts.txt \
  --output-dir /tmp/enhanced/
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | doubao-image-gen处理的内容输入 |,  |
| content | string | 否 | doubao-image-gen处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
    result: "gen 相关配置参数",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**：支持 SKILL.md 规范的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.8+（批量脚本依赖）
- **浏览器**：需要浏览器访问豆包 AI 创作页面（支持多实例）
- **网络**：需要网络连接（访问豆包服务）
- **内存**：建议 16GB+（多浏览器实例并行）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本要求 |
|:------|------:|:------|:------|------:|
| Python | 运行时 | 必需 | python.org | 3.8+ |
| Chrome | 浏览器 | 必需 | google.com | 100+ |
| message | 平台工具 | 必需 | Skill 平台安装 | - |
| requests | Python 库 | 必需 | `pip install requests` | 2.25+ |
| PyYAML | Python 库 | 可选 | `pip install pyyaml` | 5.4+ |
| Pillow | Python 库 | 可选 | `pip install Pillow` | 9.0+（质量评估） |
| 豆包账号 | 服务 | 必需 | 豆包平台注册 | - |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 | - |

#### 完整安装命令
```bash
pip3 install requests pyyaml Pillow
# ...
python3 --version
google-chrome --version
which message
python3 -c "import requests; print('requests ready')"
```

### API Key 配置
专业版需要以下配置：

| 配置项 | 环境变量 | 用途 | 获取方式 |
|---:|:---|---:|---:|
| 豆包账号 | 浏览器登录 | 访问豆包 AI 服务 | 豆包平台注册 |
| Skill 平台 Token | 平台配置 | 平台认证 | Skill 平台控制台 |
| 提示词增强 API | `PROMPT_ENHANCE_API_KEY` | AI 提示词增强（可选） | 对应 AI 服务商 |

```bash
export PROMPT_ENHANCE_API_KEY="your_enhance_key"
# ...
```

### 可用性分类
- **分类**：MD+EXEC（Markdown 指令 + 命令行执行 + 浏览器自动化 + Python 脚本）
- **说明**：通过自然语言指令驱动 Agent 操作浏览器与 Python 脚本完成批量图片生成
- **离线可用**：否（需要网络访问豆包服务）
- **隐私等级**：中（提示词与参考图需上传至豆包服务）
- **企业部署**：支持私有化部署客户端，支持多浏览器实例并行

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1：专业版与免费版工作流是否兼容？
**A：** 完全兼容。专业版包含免费版所有工作流，单图生成流程可直接运行。专业版扩展的是批量、多比例、风格预设等能力.
### Q2：批量生成中部分图片失败怎么办？
**A：** 专业版自动记录失败任务：

```bash
python3 batch_generate.py --retry-failed /tmp/generate-queue.json
# ...
python3 batch_generate.py --resume /tmp/generate-queue.json
```

### Q3：多比例输出如何工作？
**A：** 一次提示词同时生成多种比例版本：

```bash
python3 batch_generate.py \
  --config items.json \
  --ratios "3:4,1:1,16:9"
```

每个比例版本保存到独立子目录.
### Q4：风格预设如何创建？
**A：** 通过风格管理器创建：

```bash
python3 style_manager.py create \
  --name "我的风格" \
  --keywords "简约,高质感" \
  --negative "复杂,模糊"
```

### Q5：参考图风格迁移效果如何？
**A：** 参考图风格迁移效果取决于：

- 参考图风格特征明显程度
- `style_strength` 参数（建议 0.7-0.9）
- 提示词与参考图的兼容性

### Q6：提示词增强是否支持英文？
**A：** 支持。提示词增强支持中英文输入与输出：

```bash
python3 prompt_enhancer.py \
  --input "a cat" \
  --language "en" \
  --output /tmp/enhanced-en.txt
```

### Q7：生成结果如何自动归档？
**A：** 启用自动归档：

```bash
python3 batch_generate.py \
  --config items.json \
  --auto-archive \
  --archive-dir /images/archive/
```

按项目与时间自动组织目录结构.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

