---
slug: google-workspace-cli-pro
name: google-workspace-cli-pro
version: "1.0.0"
displayName: 谷歌办公命令行专业版
summary: 全功能Google Workspace命令行工具,覆盖六大服务与批量操作,支持企业级多租户场景与自动化工作流。
license: Proprietary
edition: pro
description: |-
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
tools:
  - - read
- exec
---

# 谷歌办公命令行工具 - 专业版
## 概述
谷歌办公命令行工具专业版是一款面向企业与专业用户的全功能 Google Workspace 命令行解决方案。在完全兼容免费版命令体系的基础上,专业版解锁了 Sheets(表格)、Docs(文档)、Contacts(联系人)三大高级服务,并提供批量操作、自动化工作流模板、企业级多账户管理等进阶能力。

无论是批量发送通知邮件、自动化写入数据报表、批量导出文档归档,还是团队日程协调,专业版都能通过命令行高效完成,无需反复切换浏览器标签,显著降低重复操作成本。

### 免费版与专业版能力对比
| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| Gmail 邮件搜索 | 支持 | 支持 |
| Gmail 邮件发送(纯文本) | 支持 | 支持 |
| Gmail 邮件发送(HTML/附件) | 不支持 | 支持 |
| Gmail 草稿管理 | 不支持 | 支持 |
| Calendar 事件查询 | 支持 | 支持 |
| Calendar 事件创建/更新/删除 | 不支持 | 支持 |
| Drive 文件搜索 | 支持 | 支持 |
| Drive 文件下载 | 不支持 | 支持 |
| Sheets 表格读写 | 不支持 | 支持 |
| Docs 文档导出 | 不支持 | 支持 |
| Contacts 联系人管理 | 不支持 | 支持 |
| 批量操作 | 不支持 | 支持 |
| 自动化工作流模板 | 不支持 | 支持 |
| 多账户企业管理 | 基础 | 高级 |

## 核心能力
### 一、Gmail 高级邮件管理
- 邮件搜索:完整支持 Gmail 搜索语法,含标签、附件、时间范围
- 邮件发送:纯文本 / HTML / 附件发送
- 草稿管理:创建草稿、发送草稿、修改邮件状态
- 标签管理:列出标签、批量打标
- 附件下载:按邮件 ID 下载附件

### 二、Calendar 高级日程管理
- 事件查询:按日历 ID 与时间范围查询
- 事件创建:支持完整事件字段( attendees / 提醒 / 视频会议)
- 事件更新:修改时间、地点、参会人
- 事件删除:批量清理过期事件
- 空闲时间查询:查找参会人共同空闲时段

### 三、Drive 文件管理
- 文件搜索:按关键词、MIME 类型检索
- 文件下载:支持指定本地路径
- 文件夹查找:按名称定位文件夹

### 四、Sheets 表格操作(专业版独有)
- 数据读取:按范围读取单元格数据
- 数据写入:按范围更新单元格
- 数据追加:在指定位置插入新行
- 数据清空:批量清除区域数据
- 元数据查询:获取表格结构信息

### 五、Docs 文档操作(专业版独有)
- 文档导出:支持 txt / pdf / docx 等格式
- 文档内容查看:直接在终端输出文档文本
- 文档复制:创建文档副本

### 六、Contacts 联系人管理(专业版独有)
- 联系人列表:批量获取联系人
- 联系人搜索:按姓名、邮箱检索

## 使用场景
### 场景一:批量发送会议通知邮件
企业行政人员需向 50 位参会者发送会议通知,通过脚本批量处理,自动跳过发送失败项。

```bash
# 批量发送脚本
#!/bin/bash
# batch_notify.sh - 批量会议通知
SUBJECT="2026 Q3 季度总结会议通知"
BODY="各位同事,定于2026年7月25日14:00在3号会议室召开Q3季度总结会议,请准时参加。"

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
每日将销售数据自动写入 Google Sheets,无需手动打开表格录入。

```python
#!/usr/bin/env python3
"""销售数据自动写入 Sheets"""
import subprocess
import json
from datetime import datetime

SHEET_ID = "your_sheet_id_here"
TODAY = datetime.now().strftime("%Y-%m-%d")

# 今日销售数据
sales_data = [
    ["2026-07-18", "华东区", "¥128,500", "32单"],
    ["2026-07-18", "华南区", "¥96,300", "28单"],
    ["2026-07-18", "华北区", "¥152,800", "41单"],
]

# 转为 JSON 格式
values_json = json.dumps(sales_data)

# 追加数据到 Sheets
subprocess.run([
    'gog', 'sheets', 'append', SHEET_ID, '销售数据!A:D',
    '--values-json', values_json,
    '--insert', 'INSERT_ROWS',
    '--no-input'
])

print(f"已写入 {len(sales_data)} 条销售记录")
```

### 场景三:批量导出团队文档归档
项目结束后,将团队 Google Docs 批量导出为 PDF 归档存储。

```bash
# 批量导出文档
#!/bin/bash
# archive_docs.sh - 文档归档
ARCHIVE_DIR="/tmp/project_archive_$(date +%Y%m%d)"
mkdir -p "$ARCHIVE_DIR"

# 文档ID列表
doc_ids=(
    "doc_id_1:需求文档"
    "doc_id_2:设计稿说明"
    "doc_id_3:测试报告"
    "doc_id_4:上线 checklist"
)

for entry in "${doc_ids[@]}"; do
    doc_id="${entry%%:*}"
    name="${entry##*:}"
    output="$ARCHIVE_DIR/${name}.pdf"
    echo "正在导出: $name"
    gog docs export "$doc_id" --format pdf --out "$output" --no-input
done

echo "归档完成,共 ${#doc_ids[@]} 份文档,存储于 $ARCHIVE_DIR"
```

## 快速开始
### 依赖说明
```bash
# 配置 OAuth 凭据
gog auth credentials /path/to/client_secret.json

# 添加账户并授权全部六大服务
gog auth add you@company.com --services gmail,calendar,drive,contacts,sheets,docs

# 验证账户配置
gog auth list
```

### 第二步:设置默认账户
```bash
# 设置企业账户为默认
export GOG_ACCOUNT=you@company.com
```

### 第三步:验证各服务可用性
```bash
# Gmail 验证
gog gmail search 'newer_than:1d' --max 3 --json

# Calendar 验证
gog calendar events primary --from 2026-07-18T00:00:00Z --to 2026-07-18T23:59:59Z --json

# Drive 验证
gog drive search "report" --max 5 --json

# Sheets 验证
gog sheets get <sheetId> "Sheet1!A1:B2" --json

# Docs 验证
gog docs cat <docId>

# Contacts 验证
gog contacts list --max 10
```

## 示例
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

# JSON 输出
export GOG_OUTPUT=json

# 不交互模式
export GOG_NO_INPUT=true

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

class WorkspaceAutomation:
    def __init__(self, account):
        self.account = account
        self.base_cmd = ['gog', '--no-input', '--json', '--account', account]

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

    def get_unread_emails(self, max_count=20):
        """获取未读邮件"""
        result = subprocess.run(
            self.base_cmd + ['gmail', 'search', 'is:unread newer_than:1d',
                           '--max', str(max_count)],
            capture_output=True, text=True
        )
        return json.loads(result.stdout)

    def write_report(self, sheet_id, data):
        """将日报数据写入 Sheets"""
        values_json = json.dumps(data)
        subprocess.run(
            self.base_cmd + ['sheets', 'append', sheet_id, '日报!A:E',
                           '--values-json', values_json, '--insert', 'INSERT_ROWS']
        )

    def generate_daily_brief(self, sheet_id):
        """生成并发送每日简报"""
        events = self.get_today_events()
        emails = self.get_unread_emails()

        brief_data = [[
            datetime.now().strftime('%Y-%m-%d'),
            f'{len(events)} 场会议',
            f'{len(emails)} 封未读邮件',
            '自动生成',
            '待补充'
        ]]
        self.write_report(sheet_id, brief_data)
        return f"日报已生成: {len(events)} 场会议, {len(emails)} 封未读邮件"

# 使用示例
automation = WorkspaceAutomation('you@company.com')
result = automation.generate_daily_brief('your_sheet_id')
print(result)
```

## 最佳实践
### 错误处理
企业级批量操作涉及大量数据,务必对每条记录做错误捕获与重试,避免单点失败导致整体中断。

```bash
# 带重试机制的批量发送
send_with_retry() {
    local email=$1
    local subject=$2
    local body=$3
    local max_retries=3
    local attempt=1

    while [ $attempt -le $max_retries ]; do
        if gog gmail send --to "$email" --subject "$subject" --body "$body" --no-input 2>/dev/null; then
            echo "[成功] $email (第${attempt}次尝试)"
            return 0
        fi
        echo "[重试] $email 第${attempt}次失败,等待${attempt}秒后重试..."
        sleep $attempt
        attempt=$((attempt + 1))
    done
    echo "[失败] $email 已达最大重试次数"
    return 1
}
```

### 2. Sheets 操作优先使用 JSON 传参
写入数据时,优先使用 `--values-json` 传递结构化数据,避免转义问题。

```bash
# 推荐:JSON 格式传参
gog sheets update <sheetId> "Sheet1!A1:B2" \
    --values-json '[["日期","销售额"],["2026-07-18","¥128,500"]]' \
    --input USER_ENTERED --no-input

# 不推荐:内联参数(易出错)
gog sheets update <sheetId> "Sheet1!A1:B2" "日期" "销售额" "2026-07-18" "¥128,500"
```

### 3. 文档导出按需选择格式
不同场景选择不同导出格式,平衡可读性与兼容性:

| 场景 | 推荐格式 | 命令参数 |
|:-----|:---------|:---------|
| 终端快速查看 | txt | `--format txt` |
| 正式归档存档 | pdf | `--format pdf` |
| 后续编辑修改 | docx | `--format docx` |
| 数据提取处理 | txt | `--format txt` 配合 `--json` |

### 4. Calendar 事件创建前先查空闲
避免会议时间冲突,创建事件前先用 `findFreeTime` 查询参会人共同空闲时段。

```bash
# 查询参会人共同空闲时间
gog calendar find-free-time \
    --attendees '["a@company.com","b@company.com","c@company.com"]' \
    --from 2026-07-25T09:00:00Z \
    --to 2026-07-25T18:00:00Z \
    --duration 60 --json
```

### 5. 敏感操作启用审计日志
企业环境下的邮件发送、数据修改等敏感操作,建议记录审计日志:

```bash
# 启用操作日志
log_action() {
    local action=$1
    local detail=$2
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$GOG_ACCOUNT] [$action] $detail" >> /var/log/gog_audit.log
}

log_action "EMAIL_SEND" "发送至 team@company.com,主题:周报提交"
gog gmail send --to team@company.com --subject "周报提交" --body "本周周报已更新" --no-input
```

## 常见问题
### Q1: 如何在多个企业账户间切换?
**A**: 通过 `--account` 参数或 `GOG_ACCOUNT` 环境变量切换。专业版支持账户组管理,可批量操作多账户:

```bash
# 账户 A 操作
gog gmail search 'is:unread' --account admin@company.com --max 10

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
**A**: 确保文档内字体为 Google Docs 支持的中文字体(如 Noto Sans CJK)。导出时指定 `--format pdf`,如仍有问题可先导出为 docx 再本地转换。

### Q5: 如何与企业现有系统集成?
**A**: 专业版所有命令均支持 `--json` 输出,可通过 subprocess 或 HTTP 包装层与 CRM、ERP 等系统集成。参考"自动化工作流模板"章节的 Python 示例。

### Q6: 免费版用户升级后配置是否兼容?
**A**: 完全兼容。专业版沿用免费版的命令体系与配置文件,升级后原有脚本与凭据无需修改,直接获得高级功能权限。

## 依赖说明
### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **网络环境**: 需可访问 Google API 服务
- **Python 环境**: 建议 3.8+(运行自动化脚本模板)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Google OAuth 凭据 | 凭据 | 必需 | Google Cloud Console 创建 |
| gog 命令行工具 | CLI | 必需 | 通过包管理器安装 |
| Google Workspace 账户 | 账户 | 必需 | 企业版或个人版均可 |
| Python 3.8+ | 运行时 | 推荐 | python.org 下载 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 需在 Google Cloud Console 创建 OAuth 2.0 客户端 ID,下载 `client_secret.json`
- 通过 `gog auth credentials /path/to/client_secret.json` 导入凭据
- 需启用以下 API:Gmail API、Google Calendar API、Google Drive API、Google Sheets API、Google Docs API、Google People API(Contacts)
- 首次使用打开浏览器完成 OAuth 授权,凭据本地加密存储

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于命令行的企业级 AI Skill,通过自然语言指令驱动 Agent 执行 Google Workspace 六大服务的深度操作。专业版完全兼容免费版命令体系,额外提供 Sheets/Docs/Contacts 高级操作、批量处理能力与企业级自动化工作流模板,适合团队协作与规模化办公场景。

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
