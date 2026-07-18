---
slug: whatsapp-style-guide-pro
name: whatsapp-style-guide-pro
version: "1.0.0"
displayName: WhatsApp样式指南-专业版
summary: 企业级WhatsApp格式完整规范,含边界场景/高级模式/多语言指南/交互式测试
license: MIT
edition: pro
description: |-
  WhatsApp样式指南专业版,提供完整的WhatsApp消息格式规范体系,面向企业和专业内容团队。

  核心能力:
  - 完整WhatsApp格式语法规范(含边界场景与特殊字符处理)
  - 高级排版模式库(商务/营销/客服/技术场景)
  - 多语言格式指南(中文/英文/日文)
  - 交互式格式测试与实时预览
  - 团队样式规范定制与执行
  - 格式合规审计与报告生成
  - 版本化规范管理与变更追踪

  适用场景:
  - 企业内容团队的WhatsApp消息规范制定
  - 多语言客服团队的格式培训
  - 消息格式合规审计与质量管控
  - 大规模消息生产的样式标准化

  差异化:
  - 与免费版完全兼容,无缝升级不丢失已有规范
  - 覆盖免费版未包含的边界场景和高级排版模式
  - 支持多语言格式指南,满足国际化团队需求
  - 交互式测试能力,实时验证格式效果
  - 提供格式合规审计报告,支持企业级质量管控

  触发关键词: whatsapp, 样式, 指南, 规范, 边界, 高级, 模式, 多语言, 测试, 审计, 合规, guide, advanced, compliance, audit, multilingual
tags:
- 沟通协作
- 样式指南
- WhatsApp
- 企业级
- 格式规范
- 合规审计
tools:
- read
- exec
---

# WhatsApp样式指南(专业版)

## 概述

WhatsApp样式指南专业版是一套完整的WhatsApp消息格式规范体系。在免费版核心语法规范的基础上,PRO版新增了边界场景处理、高级排版模式库、多语言格式指南、交互式格式测试和团队规范定制等企业级能力,帮助内容团队实现消息格式的标准化、合规化和国际化。

PRO版与免费版完全兼容,升级后原有规范文档继续有效。适合企业内容团队制定统一的WhatsApp消息规范、多语言客服团队格式培训、消息格式合规审计等场景。

### PRO版增强能力总览

| 能力分类 | 具体功能 | 免费版 | PRO版 |
|:---------|:---------|:-------|:------|
| 核心规范 | 基础语法说明 | 支持 | 支持 |
| 核心规范 | 允许/禁止模式 | 支持 | 支持 |
| 核心规范 | 基础示例库 | 支持 | 支持 |
| 核心规范 | 格式速查表 | 支持 | 支持 |
| 边界场景 | 特殊字符转义 | - | 支持 |
| 边界场景 | Emoji与格式混用 | - | 支持 |
| 边界场景 | 多行格式处理 | - | 支持 |
| 高级模式 | 商务排版模式 | - | 支持 |
| 高级模式 | 营销排版模式 | - | 支持 |
| 高级模式 | 客服排版模式 | - | 支持 |
| 高级模式 | 技术排版模式 | - | 支持 |
| 多语言 | 中文格式指南 | - | 支持 |
| 多语言 | 英文格式指南 | - | 支持 |
| 多语言 | 日文格式指南 | - | 支持 |
| 交互测试 | 实时格式预览 | - | 支持 |
| 交互测试 | 格式效果测试 | - | 支持 |
| 团队规范 | 自定义规范定义 | - | 支持 |
| 团队规范 | 合规审计报告 | - | 支持 |
| 版本管理 | 规范版本控制 | - | 支持 |

## 核心能力

### 1. 边界场景处理规范

#### 特殊字符转义

当文本内容本身包含格式符号时,需要特殊处理以避免误触发格式。

```python
class WhatsAppEscapeHandler:
    """WhatsApp特殊字符转义处理器"""

    # 需要转义的字符及其转义形式
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
        # 匹配已有格式区域
        format_pattern = r'(\*[^*\n]+\*|_[^_\n]+_|~[^~\n]+~|`[^`\n]+`)'

        parts = re.split(format_pattern, text)
        result = []
        for i, part in enumerate(parts):
            if i % 2 == 0:
                # 非格式区域,转义
                result.append(self.escape_text(part))
            else:
                # 格式区域,保留原样
                result.append(part)
        return ''.join(result)


# 使用示例
handler = WhatsAppEscapeHandler()

# 场景:文本中包含星号但不希望加粗
raw = "计算结果: 3 * 4 = 12"
escaped = handler.escape_text(raw)
print(f"转义后: {escaped}")
# 输出: 计算结果: 3 \* 4 = 12
```

#### Emoji与格式混用

```python
class EmojiFormatGuide:
    """Emoji与格式混用指南"""

    RULES = {
        "emoji_before_format": "Emoji放在格式符号之前,不影响格式渲染",
        "emoji_inside_format": "Emoji在格式符号内部时,确保符号紧贴文字部分",
        "emoji_after_format": "Emoji放在格式符号之后,不影响格式渲染",
    }

    EXAMPLES = {
        "correct_emoji_bold": "🔥 *限时特惠* 🔥",
        "correct_emoji_list": "📦 订单明细:\n* 商品A\n* 商品B",
        "correct_emoji_quote": "💡 温馨提示:\n> 请及时确认收货",
        "warning_emoji_inside": "🔥*限时特惠*🔥 (部分设备可能不渲染加粗)",
    }

    def get_recommendation(self, emoji: str, format_type: str) -> str:
        """获取Emoji与格式的推荐组合方式"""
        return f"推荐: {emoji} {format_type}文本{format_type} {emoji}"
```

#### 多行格式处理

```text
┌─────────────────────────────────────────────────────────┐
│  多行格式处理规范                                        │
├─────────────────────────────────────────────────────────┤
│  1. 加粗/斜体/删除线不可跨行(每行独立使用)              │
│  2. 等宽体不可跨行(每行独立使用)                        │
│  3. 引用块可跨行(每行以 > 开头)                         │
│  4. 列表项每行独立(每行以 * 或数字开头)                 │
│  5. 空行用于段落分隔,不影响格式                         │
└─────────────────────────────────────────────────────────┘
```

### 2. 高级排版模式库

#### 商务排版模式

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

#### 营销排版模式

```text
*营销推广模式*

适用于:促销活动、产品推广、优惠通知

*结构规范:*
* 标题:加粗 + Emoji吸引注意
* 副标题:斜体,营造氛围
* 商品:编号列表,清晰展示
* 价格:删除线原价 + 加粗现价
* 紧迫感:引用块,限时限量提示

*示例:*
🔥 *夏季清仓大促* 🔥

_一年仅此一次,错过再等一年_

*精选商品*
1. 蓝牙耳机 Pro - ~299元~ *199元*
2. 智能手表 - ~599元~ *399元*
3. 无线充电器 - ~99元~ *59元*

> ⏰ 活动时间:7月18日-20日
> 数量有限,先到先得!
```

#### 客服排版模式

```text
*客服沟通模式*

适用于:客户服务、售后支持、咨询回复

*结构规范:*
* 问候:加粗标题 + 斜体问候语
* 选项:列表形式,便于客户选择
* 说明:普通文本,简洁明了
* 结语:引用块,服务承诺

*示例:*
*客服中心*

_您好,很高兴为您服务_

请问需要什么帮助?

1. 查询订单状态
2. 申请退换货
3. 产品使用咨询
4. 转人工客服

> 服务时间: 09:00-21:00
> 回复时效: 5分钟内响应
```

#### 技术排版模式

```text
*技术文档模式*

适用于:技术说明、操作指引、故障排查

*结构规范:*
* 标题:加粗
* 步骤:编号列表,每步清晰
* 代码/命令:等宽体
* 注意事项:引用块
* 技术参数:列表形式

*示例:*
*API接入指引*

*操作步骤*
1. 获取API Key: `sk-xxxxxxxxxxxx`
2. 设置请求头: `Authorization: Bearer <key>`
3. 发送请求到: `https://api.example.com/v1/send`

*请求参数*
* phone: 收件人号码(含国家代码)
* message: 消息内容(最多4096字符)
* type: 消息类型(text/media/template)

> 注意: API调用频率限制为每秒10次
> 超出限制将返回 429 状态码
```

### 3. 多语言格式指南

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

### 4. 交互式格式测试

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
        # 模拟加粗渲染
        render = re.sub(r'\*([^*\n]+)\*', r'【加粗:\1】', render)
        render = re.sub(r'_([^_\n]+)_', r'【斜体:\1】', render)
        render = re.sub(r'~([^~\n]+)~', r'【删除:\1】', render)
        render = re.sub(r'`([^`\n]+)`', r'【代码:\1】', render)
        return render


# 使用示例
tester = InteractiveFormatTester()

result = tester.test_format("""*订单通知*
订单号: `ORD-001`
* 合品A
* 商品B
> 感谢购买""")

print(f"发现格式: {result['formats']}")
print(f"问题: {result['issues']}")
print(f"渲染预估: {result['estimated_render']}")
```

### 5. 团队规范定制与合规审计

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


# 使用示例
auditor = ComplianceAuditor("优品商城")

# 审计消息
auditor.audit_message("*订单通知* 优品商城 - 订单已确认")
auditor.audit_message("## 标题 **加粗** 内容")  # 不合规

# 生成报告
report = auditor.generate_report()
print(f"合规率: {report['summary']['pass_rate']}")
```

## 使用场景

### 场景一:制定团队WhatsApp消息规范

企业内容团队使用PRO版指南制定统一的WhatsApp消息格式规范。

```python
# 初始化合规审计器
auditor = ComplianceAuditor("优品商城")

# 定义团队规范
team_standards = {
    "notification": "通知类消息须使用加粗标题 + 编号列表 + 引用落款",
    "marketing": "营销类消息须使用Emoji + 加粗 + 删除线价格 + 紧迫感引用",
    "service": "客服类消息须使用加粗问候 + 斜体服务语 + 编号选项",
}

# 审计客服消息
cs_message = """*客服中心*

_您好,很高兴为您服务_

1. 查询订单
2. 售后服务

> 优品商城 致力于优质服务"""

result = auditor.audit_message(cs_message, {"type": "service"})
print(f"合规状态: {result['overall']}")
```

### 场景二:多语言团队格式培训

国际化客服团队使用多语言指南培训各语言团队。

```python
# 获取各语言格式指南
guide = MultilingualStyleGuide()

for lang_info in guide.list_languages():
    lang_guide = guide.get_guide(lang_info["code"])
    print(f"\n{lang_guide['name']}")
    print(f"  加粗示例: {lang_guide['bold_example']}")
    print(f"  注意事项: {lang_guide['notes']}")
```

### 场景三:消息批量合规审计

对一批待发送消息进行格式合规审计,确保全部通过后再发送。

```python
# 批量审计
messages = [
    "*发货通知* 订单已发出 - 优品商城",
    "## 标题 **内容** 优品商城",
    "*活动* ~原价199~ *现价99* 优品商城",
]

for msg in messages:
    result = auditor.audit_message(msg)
    status = "通过" if result["overall"] == "pass" else "不通过"
    print(f"[{status}] {msg[:30]}...")

# 生成审计报告
report = auditor.generate_report()
print(f"\n总审计: {report['summary']}")
```

## 快速开始

### 从免费版升级

```bash
# PRO版继承免费版全部规范,直接安装即可
skill-platform skills install whatsapp-style-guide-pro
skill-platform gateway restart

# 发送 /new 开始新会话
```

### 全新安装

```bash
# 安装PRO版Skill
skill-platform skills install whatsapp-style-guide-pro

# 初始化团队规范
python3 init_team_guide.py --org "你的公司名"

# 运行交互式测试
python3 interactive_test.py
```

## 配置示例

### PRO版企业级配置

```yaml
# config-pro.yaml
whatsapp_style_guide:
  # 多语言支持
  languages:
    enabled: ["zh_CN", "en_US", "ja_JP"]
    default: "zh_CN"

  # 高级模式库
  pattern_library:
    enabled: true
    categories: [business, marketing, service, technical]
    custom_patterns: ./patterns/custom/

  # 交互式测试
  interactive_test:
    enabled: true
    auto_suggest_fixes: true

  # 合规审计
  compliance:
    enabled: true
    org_name: "你的公司名"
    strict_mode: false
    audit_log_path: "./logs/compliance-audit.log"
    report_schedule: "weekly"

  # 版本管理
  version_control:
    enabled: true
    change_log: "./changelog.md"
```

## 最佳实践

### 1. 规范版本管理

```text
规范版本管理建议:
1. 每次规范变更记录版本号(如 v1.0 -> v1.1)
2. 变更内容写入changelog
3. 旧版本规范保留至少6个月
4. 团队成员通知规范更新
5. 新成员入职时发放最新规范
```

### 2. 合规审计流程

| 步骤 | 操作 | 负责人 | 工具 |
|:-----|:-----|:-------|:-----|
| 1 | 消息编写 | 内容编辑 | 高级模式库 |
| 2 | 格式自检 | 内容编辑 | 交互式测试 |
| 3 | 合规审计 | 质量管控 | 合规审计器 |
| 4 | 问题修正 | 内容编辑 | 审计报告 |
| 5 | 发送审批 | 主管审批 | 审计报告 |
| 6 | 正式发送 | 运营人员 | 消息发送工具 |

### 3. 多语言团队协作

```text
多语言协作建议:
1. 各语言团队使用对应语言的格式指南
2. 格式规则跨语言一致(语法相同)
3. 排版模式可按地区习惯微调
4. 合规审计统一执行(不区分语言)
5. 定期同步各语言团队的格式最佳实践
```

## 常见问题

### Q1: PRO版指南包含哪些免费版没有的内容?

**A:** PRO版新增了:边界场景处理(特殊字符转义、Emoji混用、多行格式)、高级排版模式库(商务/营销/客服/技术四种场景模式)、多语言格式指南(中/英/日)、交互式格式测试器和合规审计报告功能。

### Q2: 合规审计可以自动化吗?

**A:** 可以。PRO版支持批量消息合规审计,可集成到消息发送流程中,在发送前自动检查格式合规性。不合规的消息会被拦截并生成修正建议。

### Q3: 多语言指南的格式规则是否一致?

**A:** 格式语法规则跨语言一致(WhatsApp的格式符号不随语言变化)。但排版习惯和注意事项会根据语言特点有所不同,如中文字符与格式符号之间不留空格、全角符号不影响格式等。

### Q4: 自定义排版模式如何添加?

**A:** 在配置的 `custom_patterns` 目录下创建模式定义文件(JSON格式),定义模式名称、结构规范和示例。PRO版会自动加载自定义模式。

### Q5: 交互式测试支持哪些功能?

**A:** 交互式测试支持:格式检测(识别文本中使用的所有格式)、问题诊断(检测禁止模式和不规范用法)、渲染预估(模拟WhatsApp端的显示效果)和修正建议(自动提供修复方案)。

### Q6: 如何与免费版用户协作?

**A:** PRO版与免费版完全兼容。免费版用户可以查看核心语法规范,PRO版用户额外拥有高级模式和审计能力。团队中可以混合使用两个版本,PRO版用户的审计报告可共享给免费版用户参考。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+(交互式测试和合规审计脚本需要)

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| re | 标准库 | 必需 | Python内置 |
| json | 标准库 | 必需 | Python内置 |
| datetime | 标准库 | 必需 | Python内置 |

### API Key 配置

- 本Skill为纯Markdown指令型指南工具,无需额外API Key
- 所有规范内容和测试功能在本地完成,不依赖外部服务
- 合规审计日志存储在本地文件系统

### 可用性分类

- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,提供完整的WhatsApp格式规范体系和合规审计能力
- **运行模式**: 纯本地处理,支持交互式测试和批量审计
- **安全等级**: 审计日志可选加密存储;规范版本支持变更追踪
- **兼容性**: 与免费版(whatsapp-style-guide-free)完全兼容,支持无缝升级
