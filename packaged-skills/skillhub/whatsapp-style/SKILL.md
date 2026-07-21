---
slug: whatsapp-style
name: whatsapp-style
version: "1.0.0"
displayName: WhatsApp样式工具-专业版
summary: 企业级WhatsApp格式化平台,支持样式预设/批量转换/团队规范/多平台适配
license: Proprietary
edition: pro
description: |-
  WhatsApp样式工具专业版,面向企业和专业团队的高级消息格式化平台。核心能力:
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
  - 消...
tags:
- 沟通协作
- 消息样式
- WhatsApp
- 企业级
- 批量转换
- 格式规范
tools:
  - - read
- exec
# WhatsApp样式工具(专业版)
## 概述
---
# WhatsApp样式工具-专业版

## 核心能力

### 1. 自定义样式预设
创建和管理可复用的样式预设,团队共享统一的消息风格。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供自定义样式预设所需的指令和必要参数。
**处理**: 按照skill规范执行自定义样式预设操作,遵循单一意图原则。

### 2. 批量格式转换
支持文件级和目录级的批量格式转换,大幅提升运营效率。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供批量格式转换所需的指令和必要参数。
**输出**: 返回批量格式转换的执行结果,包含操作状态和输出数据。

### 3. 多平台格式适配
将同一内容自动适配为不同平台的消息格式。

> 详细代码示例已移至 `references/detail.md`

**输入**: 用户提供多平台格式适配所需的指令和必要参数。
**处理**: 按照skill规范执行多平台格式适配操作,遵循单一意图原则。
**输出**: 返回多平台格式适配的执行结果,包含操作状态和输出数据。

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

        for rule in self.rules["forbidden_patterns"]:
            if re.search(rule["pattern"], message, re.MULTILINE):
                violations.append({
                    "rule": rule["name"],
                    "severity": rule["severity"],
                    "message": rule["message"]
                })

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

guide = TeamStyleGuide("优品商城")

guide.add_rule("required_elements", {
    "name": "company_footer",
    "pattern": r"优品商城",
    "description": "消息须包含公司名称"
})

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

test_message = "*订单通知* 您的订单已确认。- 优品商城"
result = guide.validate(test_message)
print(f"校验结果: {result}")
```

## 适用场景

### 场景一:客服团队统一消息风格
企业客服团队使用样式预设确保所有客服消息风格一致。

```python
manager = StylePresetManager()

manager.create_preset("cs_welcome", "service", """*（根据实际场景填充） 客服中心*

您好 （根据实际场景填充）!

_我是您的专属客服 （根据实际场景填充）_

请问有什么可以帮您?
1. 查询订单
2. 售后服务
3. 产品咨询

manager.create_preset("cs_closing", "service", """*感谢您的咨询*

_希望本次服务对您有帮助_

如有其他问题,随时联系我们。

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
python3 batch_convert.py --input ./campaigns/july/ --output ./campaigns/july_whatsapp/

```

### 场景三:多渠道消息一键适配
同一内容一次编辑,自动适配WhatsApp、Telegram和Slack三个平台。

```python
adapter = MultiPlatformAdapter()

content = """*产品发布会邀请*

我们诚挚邀请您参加新品发布会。

*活动详情*
1. 时间:7月25日 14:00
2. 地点:线上直播
3. 主题:2026年度新品发布

adapted = adapter.adapt_multi(content)

for platform, text in adapted.items():
    print(f"\n{'='*40}")
    print(f"平台: {platform}")
    print(f"{'='*40}")
    print(text)
```

## 使用流程

### 从免费版升级
```bash
skill-platform skills install whatsapp-style-tool-pro
skill-platform gateway restart

```

### 全新安装
```bash
skill-platform skills install whatsapp-style-tool-pro

python3 init_presets.py --org "你的公司名"

python3 validate_whatsapp_style.py --input test_message.txt --pro
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
| strict_level | string | 否 | 审查严格度, 可选: strict/normal/loose, 默认: normal |

## 输出格式

```json
{
  "success": true,
  "data": {
    "overall_grade": "A",
    "total_score": 92,
    "max_score": 100,
    "summary": "处理完成",
    "details": [
      {
        "item": "代码风格",
        "status": "pass",
        "score": 95,
        "comment": "符合规范"
      },
      {
        "item": "安全合规",
        "status": "warn",
        "score": 80,
        "comment": "符合规范"
      }
    ],
    "improvements": [
      {
        "priority": "high",
        "suggestion": "建议优化",
        "expected_gain": "+5分"
      },
      {
        "priority": "medium",
        "suggestion": "建议优化",
        "expected_gain": "+3分"
      }
    ]
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

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
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行文本格式化任务
- **运行模式**: 纯本地处理,支持批量文件操作和预设管理
- **安全等级**: 不涉及敏感数据;审计日志可选开启;预设库支持版本管理
- **兼容性**: 与免费版(whatsapp-style-tool-free)完全兼容,支持无缝升级

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "normal"
}
```
**输出**:
```
评级: B级(良好) - 总分: 85/100

检查详情:
- 代码风格: 通过(95分) - 检查通过
- 安全合规: 警告(75分) - 检查通过
- 无障碍性: 通过(85分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [中优先级] 建议优化
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例内容",
  "strict_level": "strict"
}
```
**输出**:
```
评级: C级(及格) - 总分: 70/100

检查详情:
- 代码风格: 通过(90分) - 检查通过
- 安全合规: 不通过(50分) - 检查通过
- 无障碍性: 警告(70分) - 检查通过

改进建议:
1. [高优先级] 建议优化
2. [高优先级] 建议优化
3. [低优先级] 建议优化
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例内容"
}
```
**输出**:
```
评级: D级(不及格) - 总分: 45/100

检查详情:
- 代码风格: 不通过(40分) - 检查通过
- 安全合规: 不通过(30分) - 检查通过
- 无障碍性: 通过(65分) - 检查通过

改进建议:
1. [紧急] 建议优化
2. [高优先级] 建议优化
```

## 常见问题

### Q1: PRO版的样式预设可以导出共享吗?
**A:** 可以。预设以JSON格式存储,支持导出和导入。团队可以将预设库共享给所有成员,确保消息风格统一。

```bash
python3 export_presets.py --output team_presets.json

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
