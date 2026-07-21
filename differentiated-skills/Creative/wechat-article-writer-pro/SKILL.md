---
slug: wechat-article-writer-pro
name: wechat-article-writer-pro
version: "1.0.0"
displayName: 公众号写作专业版
summary: 企业级公众号写作引擎，支持多模型切换、业务资料库、发布流程、配图管理与团队协作。
license: Proprietary
edition: pro
description: |-
  公众号写作专业版 —— 面向专业内容团队与企业运营的高级公众号写作引擎。核心能力:
  - 多模型切换：支持DeepSeek、GPT、Claude等模型，按场景灵活选择
  - 业务资料库集成：自动关联产品/服务资料，实现增量改写
  - 完整发布流程：从选题到发布一条龙，支持草稿箱与直接发布
  - 智能配图管理：自动生成配图占位，支持用户供图与AI生成
  - 多草稿管理：支持续写、多版本对比、历史草稿追踪
  - 自定义预设：结构预设、文末区块、禁用词等深度定制
  - 内容审查集成：自动剥离引用标注...
tags:
- 内容创作
- 公众号
- 企业工具
- 多模型
- 发布流程
tools:
  - - read
- exec
---
# 公众号写作专业版

## 概述

公众号写作专业版是企业级公众号写作引擎，在免费版基础上提供多模型切换、业务资料库集成、完整发布流程、智能配图管理、多草稿管理等专业能力。支持从选题到发布的完整工作流，适用于企业公众号矩阵运营、专业自媒体团队等高阶内容生产场景。

### 免费版与专业版对比

| 能力 | 免费版 | 专业版 |
| --- | --- | --- |
| 话题生成初稿 | 支持 | 支持 |
| 基础润色改写 | 支持 | 支持 |
| 多模型切换 | 不支持 | DeepSeek/GPT/Claude等 |
| 业务资料库 | 不支持 | 自动关联产品资料 |
| 发布流程 | 仅草稿 | 草稿箱+直接发布 |
| 配图管理 | 不支持 | 自动占位+用户供图+AI生成 |
| 多草稿管理 | 不支持 | 续写/多版本对比 |
| 自定义预设 | 基础模板 | 结构/文末/禁用词深度定制 |
| 内容审查 | 不支持 | 引用标注剥离+敏感词检测 |
| 团队协作 | 不支持 | 多草稿追踪与版本管理 |

## 核心能力

### 1. 多模型切换

```yaml
# .article/config.yaml 写作模型配置
writing_model:
  provider: "deepseek"  # deepseek / openai / anthropic
  base_url: "https://api.deepseek.com/v1"
  model: "deepseek-chat"
```

```bash
# 多模型写作脚本调用
python3 write.py draft \
  --input topic-card.md \
  --model deepseek \
  -o draft.md

# 仅输出提示词JSON，不调用LLM（由Agent代写）
python3 write.py prompt draft --input topic-card.md

# 改写模式
python3 write.py rewrite \
  --input draft.md \
  --instruction "优化开头吸引力" \
  -o draft_revised.md

# 续写模式
python3 write.py continue \
  --input draft.md \
  -o draft_extended.md
```

### 2. 业务资料库集成

```bash
# 查看业务资料库
ls .article/products/

# 写作时引用业务资料（最多5个）
python3 write.py draft \
  --input topic-card.md \
  --reference .article/products/product_a/intro.md \
  --reference .article/products/product_a/tutorial.md \
  -o draft.md
```

```python
# 业务资料库结构
products_structure = """
.article/products/
├── product_a/
│   ├── intro.md           # 产品介绍
│   ├── tutorial.md        # 使用教程
│   ├── case_study.md      # 客户案例
│   └── images/            # 业务配图
├── product_b/
│   ├── intro.md
│   └── faq.md
└── service_c/
    └── overview.md
"""

# 写作时自动关联业务资料
# Agent会先 ls .article/products/，判断是否有相关产品的业务介绍
# 有相关文档 → 传入 --reference 参数
# 无相关文档 → 仅靠选题卡与合并配置写稿
```

### 3. 完整发布流程

```yaml
# publish_method 配置选项
# draft: 定稿后写入公众号草稿箱（默认）
# published: 创建草稿后自动提交发布
# none: 跳过微信上传，仅本地处理

publish_method: "draft"
```

```bash
# 完整发布流程
python3 publish.py full \
  --article draft.md \
  --method draft

# 强制直接发布
python3 publish.py full \
  --article draft.md \
  --publish
```

### 4. 智能配图管理

```python
# 配图占位生成（默认模式）
# 写作时自动在合适位置插入配图占位
# 格式: ![类型名：画面内容](placeholder)

# 配图密度配置
image_config = {
    "image_source": "generated",  # generated / user
    "image_density": "每节一图",  # 每节一图 / 每段一图 / 自定义
}

# 用户供图模式
user_image_config = {
    "image_source": "user",
    "img_analysis": "img_analysis.md"  # 图片分析文件
}
```

### 5. 多草稿管理

```bash
# 草稿目录结构
drafts/
├── 20260118-time-management/
│   ├── article.yaml        # 文章配置
│   ├── topic-card.md       # 选题卡
│   ├── draft.md            # 当前草稿
│   └── imgs/               # 图片目录
├── 20260119-fitness-tips/
│   ├── article.yaml
│   ├── topic-card.md
│   └── draft.md
```

## 使用场景

### 场景一：企业产品软文写作

企业需要撰写产品介绍软文，自动关联业务资料库中的产品信息。

```bash
# 1. 检查业务资料库
ls .article/products/smart_speaker/

# 2. 使用DeepSeek模型写作，引用产品资料
python3 write.py draft \
  --input topic-card.md \
  --model deepseek \
  --reference .article/products/smart_speaker/intro.md \
  --reference .article/products/smart_speaker/features.md \
  -o draft.md

# 3. 审查并剥离引用标注
python3 write.py strip-citations draft.md -o article_temp.md

# 4. 发布到公众号草稿箱
python3 publish.py full --article article.md --method draft
```

### 场景二：内容矩阵批量生产

运营团队管理多个公众号，需要批量生产不同风格的内容。

```python
# 多账号配置管理
accounts = [
    {
        "name": "科技前沿号",
        "config": ".article/tech/config.yaml",
        "model": "deepseek",
        "style": "严谨专业"
    },
    {
        "name": "生活美学号",
        "config": ".article/life/config.yaml",
        "model": "openai",
        "style": "温暖文艺"
    },
    {
        "name": "商业洞察号",
        "config": ".article/biz/config.yaml",
        "model": "anthropic",
        "style": "深度分析"
    }
]

# 批量生成
for account in accounts:
    subprocess.run([
        "python3", "write.py", "draft",
        "--input", f"{account['config']}/topic-card.md",
        "--model", account["model"],
        "-o", f"{account['config']}/draft.md"
    ])
```

### 场景三：用户供图写作流程

用户提供自有图片，Agent读图分析后按图编排文章结构。

```bash
# 1. 用户图片放入 imgs/ 目录
cp ~/photos/product_demo.png drafts/20260118-product/imgs/

# 2. 生成图片分析模板
python3 user_image_prepare.py --draft-dir drafts/20260118-product/

# 3. 填写 img_analysis.md（Agent读图后自动填写）
# 示例
# - 图片: imgs/product_demo.png
#   推荐用途: 封面
#   建议章节: 产品展示
#   画面描述: 产品外观特写，白色背景

# 4. 使用用户供图模式写作
# article.yaml 中设置 image_source: user
python3 write.py draft --input topic-card.md -o draft.md
```

## 不适用场景

以下场景公众号写作专业版不适合处理：

- 需要100%确定性的关键决策
- 医疗诊断
- 法律判决


## 触发条件

需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 1. 完整环境配置

```bash
# 依赖说明
pip install pyyaml requests

# 配置写作模型API Key
cat > aws.env << 'EOF'
WRITING_MODEL_API_KEY=your_deepseek_api_key
EOF

# 配置微信发布凭证（可选）
cat >> aws.env << 'EOF'
WECHAT_APP_ID=your_app_id
WECHAT_APP_SECRET=your_app_secret
EOF
```

### 2. 创建业务资料库

```bash
mkdir -p .article/products/your_product/
# 创建产品介绍文档
cat > .article/products/your_product/intro.md << 'EOF'
# 产品介绍
产品名称、核心功能、目标用户、竞争优势...
EOF
```

### 3. 完整写作流程

```bash
# 步骤1：创建选题卡
cat > topic-card.md << 'EOF'
# 选题卡
主题: 你的文章主题
目标读者: 读者画像
核心观点: 文章要传达的核心信息
EOF

# 步骤2：生成初稿（引用业务资料）
python3 write.py draft \
  --input topic-card.md \
  --reference .article/products/your_product/intro.md \
  -o draft.md

# 步骤3：审查与修正
python3 write.py strip-citations draft.md -o article_temp.md

# 步骤4：发布
python3 publish.py full --article article.md --method draft
```

## 配置示例

### 完整配置文件

```yaml
# .article/config.yaml
article_category: "科技互联网"
target_reader: "产品经理与开发者"
default_author: "公众号名称"
tone: "专业深度"
writing_style: "方法论"
target_word_count: 3000
heading_density: "较高"
forbidden_words: ["竞品名A", "竞品名B"]

# 写作模型配置
writing_model:
  provider: "deepseek"
  base_url: "https://api.deepseek.com/v1"
  model: "deepseek-chat"

# 配图配置
image_source: "generated"
image_density: "每节一图"

# 发布配置
publish_method: "draft"

# 结构预设
default_structure: ["方法论型"]
default_closing_block: ["standard_closing"]
```

### 退出码处理

| 退出码 | 含义 | 处理方式 |
| --- | --- | --- |
| 0 | 成功 | 正常流程 |
| 1 | 调用失败 | 检查网络/凭证/配置 |
| 2 | 模型未配置 | 自动降级为Agent代写 |

## 最佳实践

1. **模型选择策略**：深度分析类用DeepSeek，创意文案类用GPT，长文推理类用Claude
2. **业务资料管理**：保持资料库更新，过时资料会导致内容不准确
3. **配图规划**：写作前规划配图位置与内容，提升文章视觉质量
4. **多草稿协作**：不同团队成员可在不同草稿目录工作，避免冲突
5. **发布前审查**：始终先发布到草稿箱，预览确认后再正式发布
6. **引用标注管理**：写作阶段保留引用路径用于溯源，发布前自动剥离
7. **预设定制化**：为不同内容类型创建专属结构预设，提升写作效率

## 常见问题

### Q1：如何切换写作模型？

修改 `.article/config.yaml` 中的 `writing_model` 配置，或运行脚本时通过 `--model` 参数指定。

### Q2：业务资料库的文档格式有什么要求？

使用Markdown格式，文档直接放在产品根目录下（如 `.article/products/产品名/intro.md`）。

### Q3：发布失败提示微信凭证错误怎么办？

检查 `aws.env` 中的 `WECHAT_APP_ID` 和 `WECHAT_APP_SECRET` 是否正确，确认公众号API权限已开启。

### Q4：如何实现Agent代写（不调用外部API）？

使用 `write.py prompt` 子命令获取提示词JSON，由Agent按相同约束直接写稿。模型未配置时会自动降级为此模式。

### Q5：与免费版的配置文件是否兼容？

完全兼容。专业版在免费版配置基础上扩展，免费版的 `config.yaml` 和 `article.yaml` 可直接在专业版中使用。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8及以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| PyYAML | Python库 | 必需 | `pip install pyyaml` |
| requests | Python库 | 必需 | `pip install requests` |
| DeepSeek API | 外部API | 可选 | DeepSeek平台注册获取 |
| 微信公众号API | 外部API | 可选 | 微信公众平台获取 |

### API Key 配置

- `WRITING_MODEL_API_KEY`：写作模型API密钥，存储在 `aws.env` 文件中
- `WECHAT_APP_ID` / `WECHAT_APP_SECRET`：微信公众号API凭证（发布功能需要）
- 与免费版配置文件完全兼容，可无缝升级

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业写作任务。支持多模型切换、业务资料库、发布流程等企业级功能，通过Python脚本实现复杂工作流。与免费版完全兼容，可直接复用免费版的配置文件与写作约束。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要API Key，无Key环境无法使用
- 性能取决于底层模型能力
