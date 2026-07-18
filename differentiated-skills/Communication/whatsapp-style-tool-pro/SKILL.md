---
slug: whatsapp-style-tool-pro
name: whatsapp-style-tool-pro
version: "1.0.0"
displayName: WhatsApp样式工具-专业版
summary: 企业级WhatsApp格式化平台,支持样式预设/批量转换/团队规范/多平台适配
license: MIT
edition: pro
description: |-
  WhatsApp样式工具专业版,面向企业和专业团队的高级消息格式化平台。

  核心能力:
  - 全部WhatsApp格式语法支持(加粗/斜体/删除线/等宽体/列表/引用)
  - 自定义样式预设与消息模板管理
  - 批量格式转换,支持文件级处理
  - 团队样式规范与一致性校验
  - 多平台格式适配(WhatsApp/Telegram/Slack)
  - 实时格式预览与智能修复
  - 格式审计日志与版本管理

  适用场景:
  - 企业客服团队的统一消息样式规范
  - 营销消息批量格式化与质量管控
  - 多渠道消息格式自动适配
  - 消息模板版本管理与审批流程

  差异化:
  - 与免费版完全兼容,无缝升级不丢失已有配置
  - 支持自定义样式预设,团队共享统一规范
  - 批量格式转换能力,大幅提升运营效率
  - 多平台格式智能适配,一次编辑多渠道发布
  - 提供格式审计日志,支持合规追溯

  触发关键词: whatsapp, 样式, 格式, 预设, 批量, 转换, 团队, 规范, 模板, 审计, 多平台, 适配, styler, preset, batch, format, template
tags:
- 沟通协作
- 消息样式
- WhatsApp
- 企业级
- 批量转换
- 格式规范
tools:
- read
- exec
---

# WhatsApp样式工具(专业版)

## 概述

WhatsApp样式工具专业版是一款面向企业和专业团队的高级消息格式化平台。在免费版基础格式能力之上,PRO版提供自定义样式预设、批量格式转换、团队样式规范、多平台格式适配等企业级功能,帮助团队实现消息样式的一致性管理和高效生产。

PRO版与免费版完全兼容,升级后原有格式规则和清理逻辑继续生效。适合企业客服团队统一消息风格、营销团队批量格式化内容、多渠道发布场景下的格式自动适配等复杂需求。

### PRO版增强能力总览

| 能力分类 | 具体功能 | 免费版 | PRO版 |
|:---------|:---------|:-------|:------|
| 基础样式 | 加粗/斜体/删除线/等宽体 | 支持 | 支持 |
| 基础样式 | 列表/引用 | 支持 | 支持 |
| 格式清理 | Markdown符号自动清理 | 支持 | 支持 |
| 格式校验 | 基础校验 | 支持 | 支持 |
| 样式预设 | 自定义样式模板 | - | 支持 |
| 样式预设 | 预设库管理 | - | 支持 |
| 批量处理 | 文件级批量转换 | - | 支持 |
| 批量处理 | 目录递归处理 | - | 支持 |
| 团队协作 | 样式规范定义 | - | 支持 |
| 团队协作 | 一致性校验 | - | 支持 |
| 多平台 | 格式智能适配 | - | 支持 |
| 多平台 | WhatsApp/Telegram/Slack | - | 支持 |
| 预览能力 | 实时格式预览 | 基础 | 实时 |
| 审计 | 格式审计日志 | - | 支持 |
| 审计 | 版本管理 | - | 支持 |

## 核心能力

### 1. 自定义样式预设

创建和管理可复用的样式预设,团队共享统一的消息风格。

```python
import json
from datetime import datetime

class StylePresetManager:
    """WhatsApp样式预设管理器"""

    def __init__(self):
        self.presets = {}

    def create_preset(self, name: str, template: str, category: str = "general"):
        """创建样式预设

        Args:
            name: 预设名称
            template: 消息模板(使用 {{变量}} 占位符)
            category: 分类(general/marketing/service/notification)
        """
        preset = {
            "name": name,
            "template": template,
            "category": category,
            "created_at": datetime.now().isoformat(),
            "version": "1.0"
        }
        self.presets[name] = preset
        return preset

    def apply_preset(self, name: str, variables: dict) -> str:
        """应用样式预设,填充变量"""
        preset = self.presets.get(name)
        if not preset:
            raise ValueError(f"预设 '{name}' 不存在")

        result = preset["template"]
        for key, value in variables.items():
            result = result.replace(f"{{{{{key}}}}}", str(value))
        return result

    def list_presets(self, category: str = None) -> list:
        """列出所有预设"""
        if category:
            return [p for p in self.presets.values() if p["category"] == category]
        return list(self.presets.values())


# 使用示例:创建企业样式预设
manager = StylePresetManager()

# 创建订单通知预设
manager.create_preset(
    name="order_notification",
    category="notification",
    template="""*{{company}} 订单通知*

订单号: `{{order_id}}`
收件人: {{customer_name}}

*商品明细*
{{items_list}}

*合计: {{total}}元*

> {{footer_note}}"""
)

# 创建营销活动预设
manager.create_preset(
    name="marketing_promo",
    category="marketing",
    template="""*{{title}}*

_{{subtitle}}_

*活动详情*
* 时间: {{period}}
* 优惠: {{discount}}
* 优惠码: `{{code}}`

~原价{{original_price}}元~ *现价{{sale_price}}元*

> {{urgency_note}}"""
)

# 应用预设
message = manager.apply_preset("order_notification", {
    "company": "优品商城",
    "order_id": "ORD-20260718-001",
    "customer_name": "张三",
    "items_list": "1. 蓝牙耳机 x1 - 199元\n2. 保护壳 x1 - 30元",
    "total": "229",
    "footer_note": "预计3个工作日内发货,请留意物流通知。"
})
print(message)
```

### 2. 批量格式转换

支持文件级和目录级的批量格式转换,大幅提升运营效率。

```python
import os
import re
from pathlib import Path

class BatchStyleConverter:
    """批量WhatsApp格式转换器"""

    # 格式转换规则
    CONVERSION_RULES = [
        (r'\*\*(.+?)\*\*', r'*\1*'),        # 双星号->单星号
        (r'__(.+?)__', r'*\1*'),              # 双下划线->单星号
        (r'^#{1,6}\s+(.+)$', r'*\1*'),       # 标题->加粗
        (r'^---+$', '__________'),            # 水平线->下划线
        (r'~~(.+?)~~', r'~\1*'),             # 双波浪线->单波浪线
        # 表格转列表
        (r'\|(.+)\|', r'* \1'),              # 表格行->列表项
    ]

    def __init__(self):
        self.stats = {"processed": 0, "converted": 0, "errors": 0}

    def convert_text(self, text: str) -> str:
        """转换单段文本"""
        result = text
        for pattern, replacement in self.CONVERSION_RULES:
            result = re.sub(pattern, replacement, result, flags=re.MULTILINE)
        return result

    def convert_file(self, input_path: str, output_path: str = None) -> dict:
        """转换单个文件"""
        if output_path is None:
            path = Path(input_path)
            output_path = str(path.parent / f"{path.stem}_whatsapp{path.suffix}")

        try:
            with open(input_path, 'r', encoding='utf-8') as f:
                content = f.read()

            converted = self.convert_text(content)

            with open(output_path, 'w', encoding='utf-8') as f:
                f.write(converted)

            self.stats["processed"] += 1
            if content != converted:
                self.stats["converted"] += 1

            return {
                "input": input_path,
                "output": output_path,
                "changed": content != converted,
                "char_count": len(converted)
            }
        except Exception as e:
            self.stats["errors"] += 1
            return {"input": input_path, "error": str(e)}

    def convert_directory(self, input_dir: str, output_dir: str = None) -> dict:
        """批量转换目录下所有文本文件"""
        if output_dir is None:
            output_dir = f"{input_dir}_whatsapp"
        os.makedirs(output_dir, exist_ok=True)

        results = []
        supported_extensions = ['.txt', '.md', '.text']

        for root, dirs, files in os.walk(input_dir):
            for filename in files:
                if Path(filename).suffix in supported_extensions:
                    input_path = os.path.join(root, filename)
                    rel_path = os.path.relpath(input_path, input_dir)
                    output_path = os.path.join(output_dir, rel_path)
                    os.makedirs(os.path.dirname(output_path), exist_ok=True)
                    result = self.convert_file(input_path, output_path)
                    results.append(result)

        return {
            "stats": self.stats,
            "results": results
        }


# 使用示例
converter = BatchStyleConverter()

# 转换单个文件
result = converter.convert_file("messages/order_template.md")
print(f"转换完成: {result}")

# 批量转换目录
batch_result = converter.convert_directory("messages/", "messages_whatsapp/")
print(f"批量统计: {batch_result['stats']}")
```

### 3. 多平台格式适配

将同一内容自动适配为不同平台的消息格式。

```python
class MultiPlatformAdapter:
    """多平台消息格式适配器"""

    # 各平台格式规则
    PLATFORM_RULES = {
        "whatsapp": {
            "bold": ("*", "*"),
            "italic": ("_", "_"),
            "strikethrough": ("~", "~"),
            "code": ("`", "`"),
            "list_item": "* ",
            "quote": "> ",
            "forbid_headers": True,
            "forbid_tables": True,
        },
        "telegram": {
            "bold": ("**", "**"),
            "italic": ("__", "__"),
            "strikethrough": ("~~", "~~"),
            "code": ("`", "`"),
            "list_item": "- ",
            "quote": "> ",
            "forbid_headers": False,
            "forbid_tables": True,
        },
        "slack": {
            "bold": ("*", "*"),
            "italic": ("_", "_"),
            "strikethrough": ("~", "~"),
            "code": ("`", "`"),
            "list_item": "- ",
            "quote": "> ",
            "forbid_headers": True,
            "forbid_tables": False,
        }
    }

    def adapt(self, content: str, target_platform: str) -> str:
        """将内容适配到目标平台格式"""
        rules = self.PLATFORM_RULES.get(target_platform)
        if not rules:
            raise ValueError(f"不支持的平台: {target_platform}")

        result = content

        # 统一转换为中间格式再适配
        # 先提取已有格式
        import re

        # 提取加粗内容
        bold_pattern = r'\*{1,2}([^*\n]+)\*{1,2}'
        bold_texts = re.findall(bold_pattern, result)
        result = re.sub(bold_pattern, '\x00BOLD_START\x00\\1\x00BOLD_END\x00', result)

        # 重新应用目标平台格式
        b_start, b_end = rules["bold"]
        result = result.replace('\x00BOLD_START\x00', b_start)
        result = result.replace('\x00BOLD_END\x00', b_end)

        return result

    def adapt_multi(self, content: str) -> dict:
        """一次性适配所有支持的平台"""
        return {
            platform: self.adapt(content, platform)
            for platform in self.PLATFORM_RULES
        }


# 使用示例
adapter = MultiPlatformAdapter()

content = "*重要通知* 本周会议时间调整为周五下午2点。"

# 适配到各平台
adapted = adapter.adapt_multi(content)
for platform, text in adapted.items():
    print(f"\n[{platform}]")
    print(text)
```

### 4. 团队样式规范

定义团队统一的消息样式规范,自动校验消息一致性。

```python
class TeamStyleGuide:
    """团队样式规范管理器"""

    def __init__(self, org_name: str):
        self.org_name = org_name
        self.rules = {
            "required_elements": [],
            "forbidden_patterns": [],
            "style_guidelines": []
        }

    def add_rule(self, category: str, rule: dict):
        """添加样式规则"""
        self.rules[category].append(rule)

    def validate(self, message: str) -> dict:
        """校验消息是否符合团队规范"""
        violations = []
        import re

        # 检查禁止模式
        for rule in self.rules["forbidden_patterns"]:
            if re.search(rule["pattern"], message, re.MULTILINE):
                violations.append({
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "message": rule["message"]
                })

        # 检查必需元素
        for rule in self.rules["required_elements"]:
            if not re.search(rule["pattern"], message):
                violations.append({
                    "rule": rule["name"],
                    "severity": "warning",
                    "message": f"缺少必需元素: {rule['description']}"
                })

        return {
            "compliant": len(violations) == 0,
            "violations": violations,
            "message_length": len(message)
        }


# 使用示例:定义企业样式规范
guide = TeamStyleGuide("优品商城")

# 添加必需元素规则
guide.add_rule("required_elements", {
    "name": "company_footer",
    "pattern": r"优品商城",
    "description": "消息须包含公司名称"
})

# 添加禁止模式
guide.add_rule("forbidden_patterns", {
    "name": "no_double_asterisk",
    "pattern": r'\*\*',
    "severity": "error",
    "message": "禁止使用双星号加粗,请用单星号"
})

guide.add_rule("forbidden_patterns", {
    "name": "no_markdown_headers",
    "pattern": r'^#{1,6}\s',
    "severity": "error",
    "message": "禁止使用Markdown标题"
})

# 校验消息
test_message = "*订单通知* 您的订单已确认。- 优品商城"
result = guide.validate(test_message)
print(f"校验结果: {result}")
```

## 使用场景

### 场景一:客服团队统一消息风格

企业客服团队使用样式预设确保所有客服消息风格一致。

```python
# 初始化预设管理器并加载团队预设
manager = StylePresetManager()

# 预设:客服欢迎语
manager.create_preset("cs_welcome", "service", """*{{company}} 客服中心*

您好 {{customer_name}}!

_我是您的专属客服 {{agent_name}}_

请问有什么可以帮您?
1. 查询订单
2. 售后服务
3. 产品咨询

> 服务时间: 周一至周日 9:00-21:00""")

# 预设:客服结束语
manager.create_preset("cs_closing", "service", """*感谢您的咨询*

_希望本次服务对您有帮助_

如有其他问题,随时联系我们。

> {{company}} 致力于为您提供优质服务""")

# 客服使用预设生成消息
welcome_msg = manager.apply_preset("cs_welcome", {
    "company": "优品商城",
    "customer_name": "张三",
    "agent_name": "小李"
})
print(welcome_msg)
```

### 场景二:营销内容批量格式化

营销团队将一批Markdown格式的活动文案批量转换为WhatsApp格式。

```bash
# 批量转换目录下所有文案
python3 batch_convert.py --input ./campaigns/july/ --output ./campaigns/july_whatsapp/

# 输出示例:
# 处理完成: 共 15 个文件
#   已转换: 12 个
#   无需转换: 3 个
#   错误: 0 个
# 输出目录: ./campaigns/july_whatsapp/
```

### 场景三:多渠道消息一键适配

同一内容一次编辑,自动适配WhatsApp、Telegram和Slack三个平台。

```python
# 多平台适配
adapter = MultiPlatformAdapter()

content = """*产品发布会邀请*

我们诚挚邀请您参加新品发布会。

*活动详情*
1. 时间:7月25日 14:00
2. 地点:线上直播
3. 主题:2026年度新品发布

> 敬请准时参加,期待您的到来!"""

# 一键适配所有平台
adapted = adapter.adapt_multi(content)

# 分别发送到各平台
for platform, text in adapted.items():
    print(f"\n{'='*40}")
    print(f"平台: {platform}")
    print(f"{'='*40}")
    print(text)
```

## 快速开始

### 从免费版升级

```bash
# PRO版继承免费版全部配置,直接安装即可
skill-platform skills install whatsapp-style-tool-pro
skill-platform gateway restart

# 发送 /new 开始新会话
```

### 全新安装

```bash
# 1. 安装PRO版Skill
skill-platform skills install whatsapp-style-tool-pro

# 2. 初始化预设库
python3 init_presets.py --org "你的公司名"

# 3. 验证安装
python3 validate_whatsapp_style.py --input test_message.txt --pro
```

## 配置示例

### PRO版企业级配置

```yaml
# config-pro.yaml - WhatsApp样式工具PRO版配置
whatsapp_style:
  # 预设管理
  presets:
    storage_path: "./presets/"
    auto_save: true
    version_control: true

  # 批量转换
  batch:
    supported_extensions: [".txt", ".md", ".text"]
    parallel_workers: 4
    output_suffix: "_whatsapp"

  # 多平台适配
  multi_platform:
    enabled: true
    platforms: ["whatsapp", "telegram", "slack"]
    default_platform: "whatsapp"

  # 团队规范
  team_guide:
    enabled: true
    org_name: "你的公司名"
    strict_mode: false
    log_violations: true

  # 审计日志
  audit:
    enabled: true
    log_path: "./logs/style-audit.log"
    retain_days: 90
```

### 样式预设库结构

```
presets/
├── notification/
│   ├── order_confirmation.json
│   ├── shipping_notice.json
│   └── payment_reminder.json
├── marketing/
│   ├── promo_general.json
│   ├── flash_sale.json
│   └── member_offer.json
├── service/
│   ├── cs_welcome.json
│   ├── cs_closing.json
│   └── faq_response.json
└── _shared/
    ├── header.json
    └── footer.json
```

## 最佳实践

### 1. 预设命名规范

采用 `类别_场景_语言` 命名规范,便于管理和检索。

```python
# 推荐命名
PRESET_NAMING_CONVENTION = {
    "notification_order_zh": "中文订单通知",
    "marketing_promo_zh": "中文营销推广",
    "service_welcome_zh": "中文客服欢迎语",
    "notification_order_en": "英文订单通知",
}
```

### 2. 多平台适配优先级

| 步骤 | 操作 | 说明 |
|:-----|:-----|:-----|
| 1 | 编辑原始内容 | 使用中间格式编写 |
| 2 | WhatsApp适配 | 转换为WhatsApp格式 |
| 3 | 多平台扩展 | 自动适配其他平台 |
| 4 | 逐平台校验 | 确认各平台显示正常 |
| 5 | 审计记录 | 记录格式转换日志 |

### 3. 批量转换性能优化

```python
# 大批量文件转换的性能建议
PERFORMANCE_TIPS = {
    "parallel_workers": "使用多线程并行处理,建议4-8个worker",
    "file_size_limit": "单文件超过1MB时分块处理",
    "memory_mode": "大目录使用流式处理,避免全量加载",
    "cache_rules": "缓存编译后的正则表达式,避免重复编译",
}
```

## 常见问题

### Q1: PRO版的样式预设可以导出共享吗?

**A:** 可以。预设以JSON格式存储,支持导出和导入。团队可以将预设库共享给所有成员,确保消息风格统一。

```bash
# 导出预设
python3 export_presets.py --output team_presets.json

# 导入预设
python3 import_presets.py --input team_presets.json
```

### Q2: 批量转换支持哪些文件格式?

**A:** 支持所有文本格式文件,包括 `.txt`、`.md`、`.text`。对于 `.docx` 等富文本格式,建议先导出为纯文本再进行转换。

### Q3: 多平台适配会改变消息内容吗?

**A:** 不会。多平台适配仅调整格式符号(如加粗符号、列表符号等),不修改消息的文字内容。各平台的消息文本保持一致,仅格式语法有所不同。

### Q4: 团队样式规范可以设置强制执行吗?

**A:** 可以。在配置中设置 `strict_mode: true` 后,不符合规范的消息将被拦截并提示修正。违规记录会写入审计日志,便于追溯。

### Q5: 预设模板支持版本管理吗?

**A:** PRO版支持预设版本管理。每次修改预设时自动保存历史版本,可随时回滚到之前的版本。

### Q6: 如何与免费版用户协作?

**A:** PRO版与免费版完全兼容。PRO版用户创建的预设可以导出为标准格式,免费版用户可以通过手动方式应用。免费版的格式规则在PRO版中继续生效。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(批量转换和预设管理脚本需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| pathlib | 标准库 | 必需 | Python内置 |
| re | 标准库 | 必需 | Python内置 |
| json | 标准库 | 必需 | Python内置 |

### API Key 配置

- 本Skill为纯Markdown指令型工具,无需额外API Key
- 所有格式处理在本地完成,不依赖外部服务
- 预设库存储在本地文件系统,无需云端凭证

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行文本格式化任务
- **运行模式**: 纯本地处理,支持批量文件操作和预设管理
- **安全等级**: 不涉及敏感数据;审计日志可选开启;预设库支持版本管理
- **兼容性**: 与免费版(whatsapp-style-tool-free)完全兼容,支持无缝升级
