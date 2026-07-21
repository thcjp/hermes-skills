# 详细参考 - whatsapp-style-guide-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
from datetime import datetime

class ComplianceAuditor:
    """WhatsApp格式合规审计器"""

    def __init__(self, org_name: str):
        self.org_name = org_name
        self.audit_log = []

    def audit_message(self, message: str, context: dict = None) -> dict:
        """审计单条消息的格式合规性"""
        import re

        checks = {
            "no_double_asterisk": {
                "pattern": r'\*\*',
                "severity": "error",
                "message": "禁止使用双星号加粗"
            },
            "no_markdown_headers": {
                "pattern": r'^#{1,6}\s',
                "severity": "error",
                "message": "禁止使用Markdown标题"
            },
            "no_markdown_tables": {
                "pattern": r'\|.*\|.*\|',
                "severity": "error",
                "message": "禁止使用Markdown表格"
            },
            "no_horizontal_rules": {
                "pattern": r'^---+$',
                "severity": "warning",
                "message": "不建议使用水平线"
            },
            "has_company_name": {
                "pattern": re.escape(self.org_name),
                "severity": "info",
                "message": f"消息包含公司名称({self.org_name})",
                "required": True
            },
        }

        results = []
        for check_name, rule in checks.items():
            found = bool(re.search(rule["pattern"], message, re.MULTILINE))
            if rule.get("required"):
                status = "pass" if found else "fail"
            else:
                status = "fail" if found else "pass"

            results.append({
                "check": check_name,
                "status": status,
                "severity": rule["severity"],
                "message": rule["message"]
            })

        audit_entry = {
            "timestamp": datetime.now().isoformat(),
            "message_preview": message[:100],
            "context": context or {},
            "results": results,
            "overall": "pass" if all(r["status"] == "pass" for r in results) else "fail"
        }
        self.audit_log.append(audit_entry)
        return audit_entry

    def generate_report(self) -> dict:
        """生成合规审计报告"""
        total = len(self.audit_log)
        passed = sum(1 for e in self.audit_log if e["overall"] == "pass")
        failed = total - passed

        return {
            "organization": self.org_name,
            "report_date": datetime.now().isoformat(),
            "summary": {
                "total_audited": total,
                "passed": passed,
                "failed": failed,
                "pass_rate": f"{passed/total*100:.1f}%" if total > 0 else "N/A"
            },
            "audit_log": self.audit_log
        }

auditor = ComplianceAuditor("优品商城")

auditor.audit_message("*订单通知* 优品商城 - 订单已确认")
auditor.audit_message("## 标题 **加粗** 内容")  # 不合规
report = auditor.generate_report()
print(f"合规率: {report['summary']['pass_rate']}")
```

## 代码示例 (python)

```python
class InteractiveFormatTester:
    """交互式WhatsApp格式测试器"""

    def __init__(self):
        self.test_cases = []

    def test_format(self, text: str) -> dict:
        """测试文本格式并返回分析结果"""
        import re

        formats_found = {
            "bold": re.findall(r'\*[^*\n]+\*', text),
            "italic": re.findall(r'_[^_\n]+_', text),
            "strikethrough": re.findall(r'~[^~\n]+~', text),
            "monospace": re.findall(r'`[^`\n]+`', text),
            "list_items": re.findall(r'^\*\s+.+$', text, re.MULTILINE),
            "numbered_items": re.findall(r'^\d+\.\s+.+$', text, re.MULTILINE),
            "quotes": re.findall(r'^>\s+.+$', text, re.MULTILINE),
        }

        issues = self._check_issues(text)

        return {
            "text": text,
            "formats": {k: v for k, v in formats_found.items() if v},
            "issues": issues,
            "char_count": len(text),
            "line_count": text.count('\n') + 1,
            "estimated_render": self._estimate_render(text, formats_found)
        }

    def _check_issues(self, text: str) -> list:
        """检查潜在格式问题"""
        issues = []
        import re

        if re.search(r'\*\*', text):
            issues.append({"type": "double_asterisk", "severity": "error",
                          "message": "检测到双星号,WhatsApp使用单星号加粗"})
        if re.search(r'^#{1,6}\s', text, re.MULTILINE):
            issues.append({"type": "markdown_header", "severity": "error",
                          "message": "检测到Markdown标题,请用加粗代替"})
        if re.search(r'\|.*\|.*\|', text):
            issues.append({"type": "markdown_table", "severity": "error",
                          "message": "检测到Markdown表格,请用列表代替"})
        if re.search(r'^---+$', text, re.MULTILINE):
            issues.append({"type": "horizontal_rule", "severity": "warning",
                          "message": "检测到水平线,请用下划线代替"})

        return issues

    def _estimate_render(self, text: str, formats: dict) -> str:
        """估算渲染效果"""
        render = text
        import re
        render = re.sub(r'\*([^*\n]+)\*', r'【加粗:\1】', render)
        render = re.sub(r'_([^_\n]+)_', r'【斜体:\1】', render)
        render = re.sub(r'~([^~\n]+)~', r'【删除:\1】', render)
        render = re.sub(r'`([^`\n]+)`', r'【代码:\1】', render)
        return render

tester = InteractiveFormatTester()

result = tester.test_format("""*订单通知*
订单号: `ORD-001`
* 合品A
* 商品B

print(f"发现格式: {result['formats']}")
print(f"问题: {result['issues']}")
print(f"渲染预估: {result['estimated_render']}")
```

## 代码示例 (python)

```python
class MultilingualStyleGuide:
    """多语言WhatsApp格式指南"""

    GUIDES = {
        "zh_CN": {
            "name": "中文格式指南",
            "bold_example": "*重要通知*",
            "list_style": "* 项目",  # 中文习惯用星号
            "quote_style": "> 引用",
            "notes": [
                "中文字符与格式符号之间不留空格",
                "中文标点符号(。、!)不影响格式",
                "全角符号不会触发格式渲染",
            ]
        },
        "en_US": {
            "name": "English Style Guide",
            "bold_example": "*Important Notice*",
            "list_style": "* Item",
            "quote_style": "> Quote",
            "notes": [
                "No space between format symbols and text",
                "English punctuation does not affect formatting",
                "Use single asterisks, never double",
            ]
        },
        "ja_JP": {
            "name": "日本語スタイルガイド",
            "bold_example": "*重要なお知らせ*",
            "list_style": "* 項目",
            "quote_style": "> 引用",
            "notes": [
                "日本語文字とフォーマット記号の間にスペースを入れない",
                "全角記号はフォーマット渲染に影響しない",
                "日本語の句読点はフォーマットに影響しない",
            ]
        }
    }

    def get_guide(self, lang: str) -> dict:
        """获取指定语言的格式指南"""
        return self.GUIDES.get(lang, self.GUIDES["zh_CN"])

    def list_languages(self) -> list:
        """列出所有支持的语言"""
        return [{"code": k, "name": v["name"]} for k, v in self.GUIDES.items()]
```

## 代码示例 (python)

```python
class WhatsAppEscapeHandler:
    """WhatsApp特殊字符转义处理器"""

    ESCAPE_MAP = {
        '*': '\\*',
        '_': '\\_',
        '~': '\\~',
        '`': '\\`',
        '>': '\\>',
    }

    def escape_text(self, text: str) -> str:
        """转义文本中的格式符号"""
        result = text
        for char, escaped in self.ESCAPE_MAP.items():
            result = result.replace(char, escaped)
        return result

    def escape_only_outside_format(self, text: str) -> str:
        """仅转义格式区域外的符号(保留已有格式)"""
        import re
        format_pattern = r'(\*[^*\n]+\*|_[^_\n]+_|~[^~\n]+~|`[^`\n]+`)'

        parts = re.split(format_pattern, text)
        result = []
        for i, part in enumerate(parts):
            if i % 2 == 0:
                result.append(self.escape_text(part))
            else:
                result.append(part)
        return ''.join(result)

handler = WhatsAppEscapeHandler()

raw = "计算结果: 3 * 4 = 12"
escaped = handler.escape_text(raw)
print(f"转义后: {escaped}")
```

## 代码示例 (text)

```text
*商务通知模式*

适用于:正式通知、公告、商务沟通

*结构规范:*
* 标题:加粗,不超过20字
* 正文:普通文本,段落间空行
* 要点:加粗标题 + 列表详情
* 落款:引用块格式

*示例:*
*关于系统维护的通知*

尊敬的用户:

我们将于本周六凌晨进行系统维护。

*维护详情*
1. 时间:7月20日 02:00-06:00
2. 影响:服务暂停约4小时
3. 范围:全部在线服务

> 如有紧急事务,请联系客服热线
> 感谢您的理解与支持
```

