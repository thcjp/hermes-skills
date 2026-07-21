# 详细参考 - whatsapp-style-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

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

manager = StylePresetManager()

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

)

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

## 代码示例 (python)

```python
import os
import re
from pathlib import Path

class BatchStyleConverter:
    """批量WhatsApp格式转换器"""

    CONVERSION_RULES = [
        (r'\*\*(.+?)\*\*', r'*\1*'),        # 双星号->单星号
        (r'__(.+?)__', r'*\1*'),              # 双下划线->单星号
        (r'^#{1,6}\s+(.+)$', r'*\1*'),       # 标题->加粗
        (r'^---+$', '__________'),            # 水平线->下划线
        (r'~~(.+?)~~', r'~\1*'),             # 双波浪线->单波浪线
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

converter = BatchStyleConverter()

result = converter.convert_file("messages/order_template.md")
print(f"转换完成: {result}")

batch_result = converter.convert_directory("messages/", "messages_whatsapp/")
print(f"批量统计: {batch_result['stats']}")
```

## 代码示例 (python)

```python
class MultiPlatformAdapter:
    """多平台消息格式适配器"""

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

        import re

        bold_pattern = r'\*{1,2}([^*\n]+)\*{1,2}'
        bold_texts = re.findall(bold_pattern, result)
        result = re.sub(bold_pattern, '\x00BOLD_START\x00\\1\x00BOLD_END\x00', result)

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

adapter = MultiPlatformAdapter()

content = "*重要通知* 本周会议时间调整为周五下午2点。"

adapted = adapter.adapt_multi(content)
for platform, text in adapted.items():
    print(f"\n[{platform}]")
    print(text)
```

