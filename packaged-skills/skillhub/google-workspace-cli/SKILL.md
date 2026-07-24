---

slug: "google-workspace-cli"
name: "google-workspace-cli"
version: 1.0.1
displayName: "谷歌办公命令行专业版"
summary: "全功能Google Workspace命令行工具,覆盖六大服务与批量操作,支持企业级多租户场景与自动化工作流。"
license: "Proprietary"
edition: "pro"
description: |-，可处理提升工作效率
  谷歌办公命令行工具专业版,面向企业与专业用户提供 Gmail、Calendar、Drive、Contacts、Sheets、Docs 全六大服务的深度操作能力。核心能力:
  - 六大服务全覆盖:Gmail / Calendar / Drive / Contacts / Sheets / Docs
  - 批量邮件发送与草稿管理
  - Sheets 读写、追加、清空与元数据查询
  - Docs 导出、内容查看与文档复制
  - Contacts 联系人批量管理
  - 企业级多账户与自动化工作流支持

  适用场景:
  - 企业批量邮件通知与...
tags:
  - 沟通协作
  - 邮件管理
  - 谷歌办公
  - 命令行工具
  - 企业效率
  - 自动化
  - 数据处理
  - 工具
  - 效率
  - 写作
  - 电商
  - 知识
  - 文档
  - 研究
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"

---

# 谷歌办公命令行专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 核心能力

### 一、Gmail 高级邮件管理
- 邮件搜索:完整支持 Gmail 搜索语法,含标签、附件、时间范围
- 邮件发送:纯文本 / HTML / 附件发送
- 草稿管理:创建草稿、发送草稿、修改邮件状态
- 标签管理:列出标签、批量打标
- 附件下载:按邮件 ID 下载附件

**输入**: 用户提供一、Gmail 高级邮件管理所需的指令和必要参数.
### 二、Calendar 高级日程管理
- 事件查询:按日历 ID 与时间范围查询
- 事件创建:支持完整事件字段( attendees / 提醒 / 视频会议)
- 事件更新:修改时间、地点、参会人
- 事件删除:批量清理过期事件
- 空闲时间查询:查找参会人共同空闲时段

**输入**: 用户提供二、Calendar 高级日程管理所需的指令和必要参数.
**处理**: 解析二、Calendar 高级日程管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。### 三、Drive 文件管理
- 文件搜索:按关键词、MIME 类型检索
- 文件下载:支持指定本地路径
- 文件夹查找:按名称定位文件夹

**输入**: 用户提供三、Drive 文件管理所需的指令和必要参数.
**输出**: 返回三、Drive 文件管理的解析响应,包含完成状态码、响应数据和完成日志。### 四、Sheets 表格任务(专业版独有)
- 数据读取:按范围读取单元格数据
- 数据写入:按范围更新单元格
- 数据追加:在指定位置插入新行
- 数据清空:批量清除区域数据
- 元数据查询:获取表格结构信息

**输入**: 用户提供四、Sheets 表格操作(专业版独有)所需的指令和必要参数.
**解析**: 解析四、Sheets 表格任务(专业版独有)的输入参数,完成核心解析逻辑,返回结构化响应和完成状态.
**输出**: 返回四、Sheets 表格任务(专业版独有)的解析响应,包含完成状态码、响应数据和完成日志。### 五、Docs 文档任务(专业版独有)
- 文档导出:支持 txt / pdf / docx 等格式
- 文档内容查看:直接在终端输出文档文本
- 文档复制:创建文档副本

**输入**: 用户提供五、Docs 文档操作(专业版独有)所需的指令和必要参数.
**解析**: 解析五、Docs 文档任务(专业版独有)的输入参数,完成核心解析逻辑,返回结构化响应和完成状态。### 六、Contacts 联系人管理(专业版独有)
- 联系人列表:批量获取联系人
- 联系人搜索:按姓名、邮箱检索

**输入**: 用户提供六、Contacts 联系人管理(专业版独有)所需的指令和必要参数.
**输出**: 返回六、Contacts 联系人管理(专业版独有)的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:批量发送会议通知邮件
企业行政人员需向 50 位参会者发送会议通知,通过脚本批量处理,自动跳过发送失败项.
```bash
# 批量发送脚本
#!/bin/bash
# batch_notify.sh - 批量会议通知
SUBJECT="2026 Q3 季度总结会议通知"
BODY="各位同事,定于2026年7月25日14:00在3号会议室召开Q3季度总结会议,请准时参加。"
# ...
while IFS=, read -r name email; do
    echo "正在发送给: $name <$email>"
    if gog gmail send --to "$email" --subject "$SUBJECT" --body "$BODY" --no-input; then
        echo "  [成功] $name"
    else
        echo "  [失败] $name - 请手动重试"
    fi
done < attendees.csv
```

**attendees.csv 示例**:

```text
张三,zhangsan@company.com
李四,lisi@company.com
王五,wangwu@company.com
```

### 场景二:自动化写入销售数据报表
每日将销售数据自动写入 Google Sheets,无需手动打开表格录入.
```python
#!/usr/bin/env python3
"""销售数据自动写入 Sheets"""
import subprocess
import json
from datetime import datetime
# ...
SHEET_ID = "your_sheet_id_here"
TODAY = datetime.now().strftime("%Y-%m-%d")
# ...
# 今日销售数据
sales_data = [
    ["2026-07-18", "华东区", "¥128,500", "32单"],
    ["2026-07-18", "华南区", "¥96,300", "28单"],
    ["2026-07-18", "华北区", "¥152,800", "41单"],
]
# ...
# 转为 JSON 格式
values_json = json.dumps(sales_data)
# ...
# 追加数据到 Sheets
subprocess.run([
    'gog', 'sheets', 'append', SHEET_ID, '销售数据!A:D',
    '--values-json', values_json,
    '--insert', 'INSERT_ROWS',
    '--no-input'
])
# ...
print(f"已写入 {len(sales_data)} 条销售记录")
```

### 场景三:批量导出团队文档归档
项目结束后,将团队 Google Docs 批量导出为 PDF 归档存储.
```bash
# 批量导出文档
#!/bin/bash
# archive_docs.sh - 文档归档
ARCHIVE_DIR="/tmp/project_archive_$(date +%Y%m%d)"
mkdir -p "$ARCHIVE_DIR"
# ...
# 文档ID列表
doc_ids=(
    "doc_id_1:需求文档"
    "doc_id_2:设计稿说明"
    "doc_id_3:测试报告"
    "doc_id_4:上线 checklist"
)
# ...
for entry in "${doc_ids[@]}"; do
    doc_id="${entry%%:*}"
    name="${entry##*:}"
    output="$ARCHIVE_DIR/${name}.pdf"
    echo "正在导出: $name"
    gog docs export "$doc_id" --format pdf --out "$output" --no-input
done
# ...
echo "归档完成,共 ${#doc_ids[@]} 份文档,存储于 $ARCHIVE_DIR"
```

## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
2. **操作系统**: Windows / macOS / Linux
3. **网络环境**: 需可访问 Google API 服务
4. **Python 环境**: 建议 3.8+(运行自动化脚本模板)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| Google OAuth 凭据 | 凭据 | 必需 | Google Cloud Console 创建 |
| gog 命令行工具 | CLI | 必需 | 通过包管理器安装 |
| Google Workspace 账户 | 账户 | 必需 | 企业版或个人版均可 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
5. 需在 Google Cloud Console 创建 OAuth 2.0 客户端 ID,下载 `client_secret.json`
6. 通过 `gog auth credentials /path/to/client_secret.json` 导入凭据
7. 需启用以下 API:Gmail API、Google Calendar API、Google Drive API、Google Sheets API、Google Docs API、Google People API(Contacts)
8. 首次使用打开浏览器完成 OAuth 授权,凭据本地加密存储

### 可用性分类
9. **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
10. **说明**: 基于命令行的企业级 AI Skill,通过自然语言指令驱动 Agent 执行 Google Workspace 六大服务的深度操作。专业版完全兼容免费版命令体系,额外提供 Sheets/Docs/Contacts 高级操作、批量处理能力与企业级自动化工作流模板,适合团队协作与规模化办公场景.
**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | google-workspace-cli处理的内容输入 |,  |
| content | string | 否 | google-workspace-cli处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
    result: "cli 相关配置参数",
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
| 输入content为空 | 用户未提供必要信息 | 提示用户提供content, 并给出示例格式 |
| 输入内容过长(>5000字) | 超出单次处理能力 | 建议分段处理, 每段不超过2000字 |
| 风格参数不识别 | 传入不支持的风格 | 列出支持的风格选项, 使用默认风格 |
| 生成内容不达标 | 质量校验未通过 | 自动1次, 仍不达标则标注问题返回 |
| 其他异常 | 内部处理异常 | 检查输入后 |

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|:------|------:|:------|:------|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 企业级多账户配置
```bash
# ~/.gog/config 企业配置示例
default_account: admin@company.com
output_format: json
no_input: true
retry_count: 3
retry_interval: 5
```

### 环境变量配置
```bash
# 默认账户
export GOG_ACCOUNT=you@company.com
# ...
# JSON 输出
export GOG_OUTPUT=json
# ...
# 不交互模式
export GOG_NO_INPUT=true
# ...
# 重试策略
export GOG_RETRY_COUNT=3
export GOG_RETRY_INTERVAL=5
```

### 自动化工作流模板
```python
#!/usr/bin/env python3
"""企业日报自动化工作流"""
import subprocess
import json
from datetime import datetime, timedelta
# ...
class WorkspaceAutomation:
    def __init__(self, account):
        self.account = account
        self.base_cmd = ['gog', '--no-input', '--json', '--account', account]
# ...
    def get_today_events(self):
        """获取今日日历事件"""
        today = datetime.now().strftime('%Y-%m-%d')
        result = subprocess.run(
            self.base_cmd + ['calendar', 'events', 'primary',
                           '--from', f'{today}T00:00:00Z',
                           '--to', f'{today}T23:59:59Z'],
            capture_output=True, text=True
        )
        return json.loads(result.stdout)
# ...
    def get_unread_emails(self, max_count=20):
        """获取未读邮件"""
        result = subprocess.run(
            self.base_cmd + ['gmail', 'search', 'is:unread newer_than:1d',
                           '--max', str(max_count)],
            capture_output=True, text=True
        )
        return json.loads(result.stdout)
# ...
    def write_report(self, sheet_id, data):
        """将日报数据写入 Sheets"""
        values_json = json.dumps(data)
        subprocess.run(
            self.base_cmd + ['sheets', 'append', sheet_id, '日报!A:E',
                           '--values-json', values_json, '--insert', 'INSERT_ROWS']
        )
# ...
    def generate_daily_brief(self, sheet_id):
        """生成并发送每日简报"""
        events = self.get_today_events()
        emails = self.get_unread_emails()
# ...
        brief_data = [[
            datetime.now().strftime('%Y-%m-%d'),
            f'{len(events)} 场会议',
            f'{len(emails)} 封未读邮件',
            '自动生成',
            '详情见说明'
        ]]
        self.write_report(sheet_id, brief_data)
        return f"日报已生成: {len(events)} 场会议, {len(emails)} 封未读邮件"
# ...
# 使用示例
automation = WorkspaceAutomation('you@company.com')
result = automation.generate_daily_brief('your_sheet_id')
print(result)
```

## 常见问题

### Q1: 如何在多个企业账户间切换?
**A**: 通过 `--account` 参数或 `GOG_ACCOUNT` 环境变量切换。专业版支持账户组管理,可批量操作多账户:

```bash
# 账户 A 操作
gog gmail search 'is:unread' --account admin@company.com --max 10
# ...
# 切换到账户 B
export GOG_ACCOUNT=hr@company.com
gog gmail search 'is:unread' --max 10
```

### Q2: Sheets 写入数据时格式丢失怎么办?
**A**: 使用 `--input USER_ENTERED` 参数,确保数据按用户输入方式解析(如日期、货币格式自动识别):

```bash
gog sheets update <sheetId> "Sheet1!A1" \
    --values-json '[["2026-07-18"]]' \
    --input USER_ENTERED --no-input
```

### Q3: 批量发送邮件触发 Gmail 限额怎么办?
**A**: Gmail 每日发送限额为 2000 封(普通账户)或 20000 封(Workspace 账户)。建议:
- 控制单批次发送量在 100 封以内
- 间隔 1-2 秒发送,避免触发速率限制
- 超限时分多日发送或使用草稿模式分批处理

### Q4: Docs 导出 PDF 中文乱码?
**A**: 确保文档内字体为 Google Docs 支持的中文字体(如 Noto Sans CJK)。导出时指定 `--format pdf`,如仍有问题可先导出为 docx 再本地转换.
### Q5: 如何与企业现有系统集成?
**A**: 专业版所有命令均支持 `--json` 输出,可通过 subprocess 或 HTTP 包装层与 CRM、ERP 等系统集成。参考"自动化工作流模板"章节的 Python 示例.
### Q6: 免费版用户升级后配置是否兼容?
**A**: 完全兼容。专业版沿用免费版的命令体系与配置文件,升级后原有脚本与凭据无需修改,直接获得高级功能权限.
## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

