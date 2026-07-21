# 详细参考 - card-image-builder-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import json
import subprocess
import os
from pathlib import Path

class BatchCardGenerator:
    """批量卡片图生成器"""

    def __init__(self, template: str, output_dir: str = "tmp/batch/"):
        self.template = template
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)
        self.stats = {"total": 0, "success": 0, "failed": 0}

    def generate_from_json(self, json_path: str) -> dict:
        """从JSON数据文件批量生成

        JSON格式:
        [
          {"text": "文案1", "hl1": "高亮", "out": "card_001.png"},
          {"text": "文案2", "out": "card_002.png"}
        ]
        """
        with open(json_path, 'r', encoding='utf-8') as f:
            items = json.load(f)

        self.stats["total"] = len(items)

        for i, item in enumerate(items, 1):
            output_name = item.get("out", f"card_{i:03d}.png")
            output_path = os.path.join(self.output_dir, output_name)

            cmd = ["python3", "render_card.py",
                   "--template", self.template,
                   "--text", item["text"],
                   "--out", output_path]

            for key in ["hl1", "hl2", "hl3", "footer", "bg", "highlight"]:
                if key in item:
                    cmd.extend([f"--{key}", str(item[key])])

            try:
                result = subprocess.run(cmd, capture_output=True,
                                       text=True, timeout=30)
                if result.returncode == 0:
                    self.stats["success"] += 1
                    print(f"[{i}/{self.stats['total']}] 成功: {output_name}")
                else:
                    self.stats["failed"] += 1
                    print(f"[{i}/{self.stats['total']}] 失败: {output_name} - {result.stderr}")
            except Exception as e:
                self.stats["failed"] += 1
                print(f"[{i}/{self.stats['total']}] 异常: {output_name} - {e}")

        self._print_summary()
        return self.stats

    def generate_from_directory(self, input_dir: str) -> dict:
        """从目录中的文本文件批量生成(文件名作为输出名)"""
        text_files = list(Path(input_dir).glob("*.txt"))
        self.stats["total"] = len(text_files)
        for i, text_file in enumerate(text_files, 1):
            text = text_file.read_text(encoding='utf-8').strip()
            output_path = os.path.join(self.output_dir, f"{text_file.stem}.png")
            cmd = ["python3", "render_card.py", "--template", self.template,
                   "--text", text, "--out", output_path]
            try:
                result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
                if result.returncode == 0:
                    self.stats["success"] += 1
                else:
                    self.stats["failed"] += 1
            except Exception:
                self.stats["failed"] += 1
        self._print_summary()
        return self.stats

    def _print_summary(self):
        """打印批量生成摘要"""
        t, s, f = self.stats["total"], self.stats["success"], self.stats["failed"]
        print(f"\n批量完成: 总计{t} 成功{s}({s/t*100:.1f}%) 失败{f}")

generator = BatchCardGenerator(template="poster-3-4", output_dir="tmp/quotes/")
batch_data = [
    {"text": "保持简单,保持专注", "hl1": "保持简单", "out": "quote_001.png"},
    {"text": "代码是写给人看的", "hl1": "写给人看", "out": "quote_002.png"},
    {"text": "少即是多", "out": "quote_003.png"},
]
with open("batch_quotes.json", "w", encoding="utf-8") as f:
    json.dump(batch_data, f, indent=2, ensure_ascii=False)
generator.generate_from_json("batch_quotes.json")
```

## 代码示例 (python)

```python
import os
import json
from pathlib import Path

class TemplateManager:
    """自定义模板管理器"""

    def __init__(self, templates_dir: str = "assets/templates/"):
        self.templates_dir = templates_dir
        os.makedirs(templates_dir, exist_ok=True)

    def create_template(self, name: str, html_template: str,
                        size: dict, config: dict = None):
        """创建新模板

        Args:
            name: 模板名称
            html_template: HTML模板内容
            size: 尺寸 {"width": 900, "height": 1200}
            config: 额外配置(字数上限、参数定义等)
        """
        html_path = os.path.join(self.templates_dir, f"{name}.html")
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(html_template)

        template_config = {
            "name": name,
            "size": size,
            "max_chars": config.get("max_chars", 500) if config else 500,
            "params": config.get("params", []) if config else [],
            "description": config.get("description", "") if config else ""
        }

        config_path = os.path.join(self.templates_dir, f"{name}.json")
        with open(config_path, 'w', encoding='utf-8') as f:
            json.dump(template_config, f, indent=2, ensure_ascii=False)

        self._register_size(name, size)

        return {
            "template_name": name,
            "html_path": html_path,
            "config_path": config_path,
            "size": size
        }

    def _register_size(self, name: str, size: dict):
        """在渲染器中注册模板尺寸"""
        print(f"已注册模板 '{name}' 尺寸: {size['width']}x{size['height']}")
        print(f"请在 render_card.py 的 size_map 中添加: '{name}': ({size['width']}, {size['height']})")

    def list_templates(self) -> list:
        """列出所有模板"""
        templates = []
        for f in Path(self.templates_dir).glob("*.json"):
            with open(f, 'r', encoding='utf-8') as fh:
                templates.append(json.load(fh))
        return templates

    def delete_template(self, name: str) -> bool:
        """删除模板"""
        html_path = os.path.join(self.templates_dir, f"{name}.html")
        config_path = os.path.join(self.templates_dir, f"{name}.json")

        deleted = False
        for path in [html_path, config_path]:
            if os.path.exists(path):
                os.remove(path)
                deleted = True
        return deleted

manager = TemplateManager()

brand_template_html = """<div class="card" style="width:{{width}}px;height:{{height}}px;background:{{bg_color}};">
  <div class="header" style="padding:40px;"><img src="{{logo_url}}" style="height:60px;"/></div>
  <div class="content" style="padding:0 40px;">
    <h1 style="color:{{text_color}};font-size:36px;">{{title}}</h1>
    <p style="color:{{text_color}};font-size:18px;">{{body_text}}</p>
  </div>
  <div class="footer" style="padding:40px;text-align:center;">
    <span style="color:{{footer_color}};font-size:14px;">{{footer_text}}</span>
  </div>
</div>"""

manager.create_template("brand-poster-3-4", brand_template_html,
    {"width": 900, "height": 1200},
    {"max_chars": 300, "description": "企业品牌海报模板(带logo)",
     "params": ["logo_url", "title", "body_text", "footer_text", "bg_color", "text_color"]})
```

## 代码示例 (python)

```python
class BrandPresetManager:
    """品牌预设管理器"""

    PLATFORM_PRESETS = {
        "公众号": {
            "footer": "公众号 · {brand}",
            "bg": "#e6f5ef",
            "highlight": "#22a854"
        },
        "小红书": {
            "footer": "小红书 · {brand}",
            "bg": "#fdecea",
            "highlight": "#e53935"
        },
        "微博": {
            "footer": "微博 · {brand}",
            "bg": "#e3f2fd",
            "highlight": "#1976d2"
        },
        "抖音": {
            "footer": "抖音 · {brand}",
            "bg": "#1a1a1a",
            "highlight": "#fe2c55"
        },
        "知乎": {
            "footer": "知乎 · {brand}",
            "bg": "#f5f5f5",
            "highlight": "#0066ff"
        },
        "twitter": {
            "footer": "@{brand}",
            "bg": "#ffffff",
            "highlight": "#1da1f2"
        }
    }

    def __init__(self, brand_name: str):
        self.brand_name = brand_name
        self.custom_presets = {}

    def get_preset(self, platform: str) -> dict:
        """获取平台预设"""
        preset = self.PLATFORM_PRESETS.get(platform, self.PLATFORM_PRESETS["公众号"])
        return {
            "footer": preset["footer"].format(brand=self.brand_name),
            "bg": preset["bg"],
            "highlight": preset["highlight"]
        }

    def create_custom_preset(self, name: str, bg: str, highlight: str,
                              footer: str = None):
        """创建自定义品牌预设"""
        self.custom_presets[name] = {
            "footer": footer or f"{name} · {self.brand_name}",
            "bg": bg,
            "highlight": highlight
        }

    def list_platforms(self) -> list:
        """列出所有支持的平台"""
        platforms = list(self.PLATFORM_PRESETS.keys())
        platforms.extend(self.custom_presets.keys())
        return platforms

brand = BrandPresetManager("优品科技")
preset = brand.get_preset("公众号")
print(f"页脚: {preset['footer']}, 背景: {preset['bg']}, 高亮: {preset['highlight']}")

brand.create_custom_preset("品牌主视觉", "#0a0e27", "#00d4ff", "优品科技 · INNOVATE")
```

