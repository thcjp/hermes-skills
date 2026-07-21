---
slug: pro-comm-toolkit
name: pro-comm-toolkit
version: "1.0.0"
displayName: 职场沟通工具箱专业版
summary: 企业级职场沟通助手，支持批量邮件生成、多语言翻译、自定义模板、跨文化沟通与团队协作场景。
license: Proprietary
edition: pro
description: |-
  职场沟通工具箱（专业版）—— 面向团队和企业的全功能写作辅助工具。核心能力:
  - 批量邮件生成与多收件人个性化定制
  - 多语言翻译与跨文化沟通指导
  - 自定义模板库与团队共享
  - 危机公关与高敏感场景沟通
  - 会议全流程管理（议程、纪要、跟进）
  - 沟通效果分析与优化建议

  适用场景:
  - 企业级邮件批量处理与个性化发送
  - 跨国团队多语言沟通
  - 危机公关与舆情应对
  - 高管汇报与董事会沟通
  - 跨部门协作与冲突调解

  差异化: 在免费版基础上增加批量处理、多语言支持、自定义模板、危机沟通等高级...
tags:
- 沟通协作
- 企业级
- 写作助手
- 多语言
- 批量处理
tools:
  - - read
- exec
---
# 职场沟通工具箱专业版

## 核心能力

### 1. 批量邮件生成与个性化
支持从数据源（CSV、JSON）批量生成个性化邮件，每封邮件根据收件人信息自动调整内容。

**输入**: 用户提供批量邮件生成与个性化所需的指令和必要参数。
**处理**: 按照skill规范执行批量邮件生成与个性化操作,遵循单一意图原则。

### 2. 多语言翻译与跨文化沟通
内置中、英、日、韩、法、德等多种语言的沟通模板，并提供跨文化沟通的注意事项指导。

**处理**: 按照skill规范执行多语言翻译与跨文化沟通操作,遵循单一意图原则。
**输出**: 返回多语言翻译与跨文化沟通的执行结果,包含操作状态和输出数据。

### 3. 自定义模板库
支持创建、编辑、分类管理自定义模板，并支持团队内共享与版本控制。

**输入**: 用户提供自定义模板库所需的指令和必要参数。
**处理**: 按照skill规范执行自定义模板库操作,遵循单一意图原则。

### 4. 危机公关与高敏感场景
针对突发事件、舆情危机、客户投诉等高敏感场景，提供专门的沟通框架与措辞指导。

**处理**: 按照skill规范执行危机公关与高敏感场景操作,遵循单一意图原则。
**输出**: 返回危机公关与高敏感场景的执行结果,包含操作状态和输出数据。

### 5. 会议全流程管理
从议程制定、会中记录到会后跟进，提供完整的会议管理工具链。

**处理**: 按照skill规范执行会议全流程管理操作,遵循单一意图原则。
**输出**: 返回会议全流程管理的执行结果,包含操作状态和输出数据。

### 6. 沟通效果分析
基于消息结构、语气、长度等维度，提供写作质量评分与优化建议。

**处理**: 按照skill规范执行沟通效果分析操作,遵循单一意图原则。
**输出**: 返回沟通效果分析的执行结果,包含操作状态和输出数据。
## 适用场景

### 场景一：批量发送个性化客户通知邮件

从客户数据文件批量生成个性化邮件，每封邮件根据客户名称、产品使用情况自动调整内容。

```python
# batch_email_generator.py
import csv
import json

def generate_batch_emails(template, data_file, output_dir):
    """
    批量生成个性化邮件
    :param template: 邮件模板字符串，支持 {name} {product} 等占位符
    :param data_file: CSV 数据文件路径
    :param output_dir: 输出目录
    """
    with open(data_file, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            email_content = template.format(**row)
            filename = f"{output_dir}/email_{row['customer_id']}.txt"
            with open(filename, 'w', encoding='utf-8') as out:
                out.write(email_content)
            print(f"已生成: {filename}")

# 示例
template = """主题: 【{product}】重要服务更新通知

尊敬的 {name} 先生/女士：

您好！感谢您使用我们的 {product} 服务。
我们将于 {date} 进行系统升级，届时服务将暂停约2小时。

升级内容：
- 性能优化，响应速度提升30%
- 新增 {feature} 功能
- 安全补丁更新

如有疑问，请随时联系您的专属客户经理。

此致
敬礼
"""
generate_batch_emails(template, "customers.csv", "./output_emails")
```

### 场景二：跨国团队多语言会议通知

```text
多语言会议通知模板
=====================================

[中文版]
主题: 季度产品评审会议通知
各位同事，我们将于本周五14:00召开季度产品评审会议，
请提前准备各自负责模块的进展汇报。

[English Version]
Subject: Quarterly Product Review Meeting
Dear colleagues, we will hold the quarterly product review
meeting this Friday at 14:00. Please prepare progress reports
for your respective modules in advance.

[日本語版]
件名: 四半期製品レビュー会議のお知らせ
皆様、今週金曜日14:00に四半期製品レビュー会議を開催します。
それぞれの担当モジュールの進捗報告を事前にご準備ください。

跨文化注意事项:
- 日本团队: 注意使用敬语，会议开始前5分钟接入
- 欧美团队: 直接切入主题，避免过多寒暄
- 中国团队: 会前分发材料，会上聚焦讨论
```

### 场景三：危机公关沟通框架

```text
危机公关沟通五步法
=====================================

优秀步: 快速响应（1小时内）
- 确认事实，不猜测原因
- 表达关注与歉意
- 承诺调查并公布结果

第二步: 信息披露（4小时内）
- 公开已知事实
- 说明正在采取的措施
- 提供客户支持渠道

第三步: 原因说明（24小时内）
- 公布调查结果
- 说明根本原因
- 公布改进方案

第四步: 补救措施
- 受影响客户的补偿方案
- 流程改进计划
- 防止复发的措施

第五步: 后续跟进
- 定期更新整改进展
- 总结经验教训
- 恢复客户信任

邮件模板:
主题: 【重要】关于 {event} 的说明与致歉

尊敬的 {name}：

关于 {date} 发生的 {event}，我们向您致以诚挚的歉意。
经调查，事件原因为 {cause}。
我们已采取以下措施：{actions}。
为表达歉意，我们将 {compensation}。

如您有任何疑问，请通过以下方式联系我们：
- 专属热线: {phone}
- 邮箱: {email}

此致
敬礼
{company} 团队
```

## 使用流程

### 安装

```bash
npx skillhub@latest install pro-comm-toolkit-pro
```

### 批量生成邮件

```bash
# 从CSV批量生成个性化邮件
python batch_email_generator.py --template templates/notice.txt \
  --data customers.csv --output ./output_emails

# 查看生成统计
python batch_email_generator.py --stats
```

### 多语言翻译

```bash
# 将邮件翻译为多语言版本
python translate_communication.py \
  --input email_zh.txt \
  --languages en,ja,ko,fr,de \
  --output ./multilingual_emails/
```

### 自定义模板管理

```bash
# 创建新模板
python template_manager.py create --name "项目周报" --category "report"

# 列出所有模板
python template_manager.py list --category "report"

# 团队共享模板
python template_manager.py share --template-id 12 --team "engineering"
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
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境

- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python 版本**: 3.8+（批量处理与多语言功能需要）
- **运行时**: Node.js 16+（模板管理工具需要）

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3.8+ | 运行时 | 必需 | python.org 官方下载 |
| pandas | Python库 | 推荐 | `pip install pandas` |
| jinja2 | Python库 | 推荐 | `pip install jinja2` |
| Markdown 渲染器 | 工具 | 可选 | 系统自带或第三方编辑器 |

### API Key 配置

```bash
# 多语言翻译功能（可选）
export TRANSLATION_API_KEY="your_translation_api_key"

# 邮件发送功能（可选）
export SMTP_HOST="smtp.company.com"
export SMTP_PORT="587"
export SMTP_USER="noreply@company.com"
export SMTP_PASSWORD="your_password"
```

本工具核心功能基于 Markdown 指令驱动，无需额外 API Key 即可使用。批量发送与多语言翻译功能需要对应服务的 API Key。

### 可用性分类

- **分类**: MD+EXEC+SCRIPT（Markdown指令 + 可执行脚本 + 批量处理能力）
- **说明**: 基于Markdown的AI Skill，，专业版支持脚本化批量处理
- **适用人群**: 企业团队、项目经理、公关团队、跨国组织
- **兼容性**: 完全兼容免费版，支持无缝升级
- **支持级别**: 优先技术支持，工作日24小时内响应

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

### 示例2: 进阶用法
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

### Q: 专业版与免费版如何兼容？

专业版完全兼容免费版的模板格式与写作规则。免费版创建的内容可直接在专业版中使用，升级无需迁移数据。

### Q: 批量邮件一次最多支持多少收件人？

专业版单次批量最大支持 1000 个收件人，建议分批发送并控制频率（每秒不超过 10 封），避免触发邮件服务商的限制。

### Q: 多语言翻译的准确度如何保证？

专业版建议对关键沟通内容采用"AI翻译 + 母语者审核"的双保险模式。AI 负责初翻，母语者负责文化适配与润色。

### Q: 自定义模板支持哪些变量？

支持以下变量类型：
- `{name}`: 收件人姓名
- `{company}`: 公司名
- `{product}`: 产品名
- `{date}`: 日期
- `{custom_field}`: 自定义字段（从数据源读取）

### Q: 危机公关模板可以预先准备吗？

可以且强烈建议。专业版支持预先创建常见危机场景（数据泄露、服务中断、产品缺陷等）的沟通模板，事件发生时只需填充具体信息即可快速响应。

### Q: 团队共享模板如何管理权限？

```bash
# 设置模板权限
python template_manager.py set-permission \
  --template-id 12 \
  --team "engineering" \
  --role "editor"    # editor / viewer / admin
```

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
