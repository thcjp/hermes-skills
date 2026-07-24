---

slug: "email-daily-summary"
name: "email-daily-summary"
version: 0.1.1
displayName: "Email Daily Summary"
summary: "基于 browser-use 自动登录邮箱并生成每日邮件摘要与统计日报。基于 browser-use CLI 自动化登录 Gmail、Outlook、QQ 邮箱、163/126 邮箱及企业微"
license: "Proprietary"
description: |-，可自动提升工作效率
  基于 browser-use CLI 自动化登录 Gmail、Outlook、QQ 邮箱、163/126 邮箱及企业微信邮箱,
  抓取收件箱列表,提取发件人、主题、摘要片段与时间戳,生成结构化每日邮件日报.
  支持未读统计、按重要性/发件人/主题分类、AI 智能摘要、截图归档与定时任务调度.
  适用于独立开发者每日邮件梳理、团队晨会邮件同步、企业高管 inbox 分诊等场景.
tags:
  - 通用办公
  - Email
  - Automation
  - 邮件
  - 通信
  - 工具
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Communication"

---

# Email Daily Summary

通过 `browser-use` CLI 驱动浏览器自动化登录 Web 邮箱,抓取当日邮件并生成结构化日报。优先复用本机 Chrome 已登录会话(`--browser real`),避免在脚本中存储明文密码.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Email Daily Summary处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Email Daily Summary自动登录邮箱并生成 | 不支持 | 支持 |
| 多标签页并行抓取 | 不支持 | 支持 |
| 反爬虫策略自动绕过 | 不支持 | 支持 |
| 页面结构变化自适应 | 不支持 | 支持 |
| 批量导出结构化数据 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

- **多邮箱自动登录**:复用 Chrome 已登录会话(`--browser real`)或 `--headed` 手动登录,覆盖 Gmail、Outlook、QQ 邮箱、163/126 邮箱、企业微信邮箱
- **邮件列表抓取**:通过 DOM 选择器提取收件箱行(`tr.zA` 等),获取发件人、主题、摘要片段、时间戳四元组
- **统计聚合**:实时计算未读数(`.zE`)、可见总数、按发件人域名/主题关键词分类
- **AI 智能摘要**:`browser-use extract` 用自然语言指令提取前 N 封邮件并按重要性排序
- **截图归档**:每日 inbox 快照保存为 PNG,按日期归档到本地目录
- **定时调度**:提供 crontab(Linux/macOS)与 launchd(macOS)两种调度模板,每日定时触发
- **跨账号汇总**:顺序遍历多个邮箱 URL,合并生成统一的跨账号日报
- **关键词监控**:命中白名单发件人或主题关键词时,在日报中高亮并加入"建议操作"区块
### 多邮箱自动登录

针对多邮箱自动登录,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供多邮箱自动登录相关的配置参数、输入数据和处理选项.
**输出**: 返回多邮箱自动登录的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`多邮箱自动登录`的配置文档进行参数调优
### 邮件列表抓取

针对邮件列表抓取,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供邮件列表抓取相关的配置参数、输入数据和处理选项.
**输出**: 返回邮件列表抓取的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`邮件列表抓取`的配置文档进行参数调优
### 统计聚合

针对统计聚合,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供统计聚合相关的配置参数、输入数据和处理选项.
**输出**: 返回统计聚合的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`统计聚合`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 前置依赖

1. 安装 browser-use CLI:

```bash
uv pip install browser-use[cli]
browser-use install
```

2. 在本机 Chrome 中至少登录过一次目标邮箱(用于 `--browser real` 复用会话)
3. 操作系统:Windows / macOS / Linux 均可,定时任务依赖 crontab 或 launchd

## 支持的邮箱服务

| 邮箱服务 | 登录 URL | 收件箱 URL |
|:---:|:---:|:---:|
| Gmail | https://accounts.google.com | https://mail.google.com |
| Outlook | https://login.live.com | https://outlook.live.com |
| QQ 邮箱 | https://mail.qq.com | https://mail.qq.com |
| 163 邮箱 | https://mail.163.com | https://mail.163.com |
| 126 邮箱 | https://mail.126.com | https://mail.126.com |
| 企业微信邮箱 | https://exmail.qq.com | https://exmail.qq.com |

## 使用流程

1. 确认 `browser-use --version` 可正常输出,否则按前置依赖安装
2. 选择登录方式:已登录 Chrome 用 `--browser real`,首次登录用 `--headed`
3. 打开收件箱 URL,`browser-use state` 探测当前 DOM 结构
4. 执行 `eval` 脚本提取邮件四元组,或 `extract` 让 AI 自然语言提取
5. 聚合统计、生成 Markdown 日报,`screenshot` 归档快照
6. `browser-use close` 释放浏览器会话

## 适用场景

### 场景 1:每日晨间邮件简报

- **输入**:Gmail 收件箱 URL + 当日日期(如 `2026-07-20`)
- **输出**:Markdown 日报,含未读数、Top 5 重要邮件、分类统计、建议操作;附 `inbox_2026-07-20.png` 截图
- **触发**:`crontab` 每日 09:00 自动执行

### 场景 2:多账号跨邮箱汇总

- **输入**:多个邮箱配置(Gmail + QQ 邮箱 + 企业微信邮箱)
- **输出**:合并日报,按邮箱分节展示,统一统计未读总数与重要邮件清单
- **触发**:用户主动请求或每日定时

### 场景 3:重要发件人监控告警

- **输入**:发件人白名单(如 `boss@company.com`、`finance@bank.com`)
- **输出**:命中邮件列表,含主题、时间、摘要片段;若命中则在日报顶部加红标记
- **触发**:每小时轮询或事件驱动

### 场景 4:周报邮件统计

- **输入**:周起止日期(如 `2026-07-14` 至 `2026-07-20`)
- **输出**:周邮件量趋势、Top 10 发件人、分类占比、未处理邮件清单
- **触发**:每周一 09:00 自动执行

## 案例展示

### 案例 1:生成今日 Gmail 日报

```bash
DATE=$(date +%Y-%m-%d)
OUTPUT_DIR="./email_summaries"
mkdir -p "$OUTPUT_DIR"
# ...
browser-use --browser real open https://mail.google.com
sleep 3
# ...
# 探测页面状态
browser-use state
# ...
# 截图归档
browser-use screenshot "$OUTPUT_DIR/inbox_$DATE.png"
# ...
# 提取前 20 封邮件四元组
browser-use eval "
  const emails = [];
  document.querySelectorAll('tr.zA').forEach((row, i) => {
    if (i < 20) {
      const sender = row.querySelector('.yX.xY span')?.innerText || '';
      const subject = row.querySelector('.y6 span')?.innerText || '';
      const snippet = row.querySelector('.y2')?.innerText || '';
      const time = row.querySelector('.xW.xY span')?.innerText || '';
      emails.push({ sender, subject, snippet, time });
    }
  });
  JSON.stringify(emails, null, 2);
"
# ...
# 未读统计
browser-use eval "
(() => {
  const unread = document.querySelectorAll('.zE').length;
  const visible = document.querySelectorAll('tr.zA').length;
  return JSON.stringify({ unread, visible, timestamp: new Date().toISOString() });
})()
"
# ...
browser-use close
```

输出示例:

```text
==========================================
邮件日报 - 2026-07-20
==========================================
统计概览:
- 未读邮件: 12 封
- 可见邮件: 50 封
- 命中白名单: 2 封
# ...
重要邮件:
1. boss@company.com | 项目进度汇报 - 紧急 | 09:30
2. finance@bank.com | 账单提醒 | 08:15
# ...
建议操作:
- 回复 boss@company.com
- 处理 3 封审批邮件
==========================================
```

### 案例 2:监控 boss@company.com 邮件

```bash
browser-use --browser real open https://mail.google.com
sleep 3
# ...
browser-use eval "
  const hits = [];
  document.querySelectorAll('tr.zA').forEach(row => {
    const sender = row.querySelector('.yX.xY span')?.innerText || '';
    if (sender.toLowerCase().includes('boss@company.com')) {
      hits.push({
        sender,
        subject: row.querySelector('.y6 span')?.innerText || '',
        time: row.querySelector('.xW.xY span')?.innerText || ''
      });
    }
  });
  JSON.stringify(hits, null, 2);
"
```

输出示例:

```json
[
  { "sender": "boss@company.com", "subject": "项目进度汇报 - 紧急", "time": "09:30" },
  { "sender": "boss@company.com", "subject": "周一晨会议程", "time": "07:45" }
]
```

### 案例 3:多账号(Gmail + QQ 邮箱)合并日报

```bash
DATE=$(date +%Y-%m-%d)
REPORT="$OUTPUT_DIR/daily_$DATE.md"
echo "# 跨邮箱日报 $DATE" > "$REPORT"
# ...
# Gmail 分节
browser-use --browser real open https://mail.google.com
sleep 3
echo "## Gmail" >> "$REPORT"
browser-use extract "提取前 10 封邮件的发件人、主题、时间,按重要性排序" >> "$REPORT"
browser-use close
# ...
# QQ 邮箱分节
browser-use --browser real open https://mail.qq.com
sleep 3
echo "## QQ 邮箱" >> "$REPORT"
browser-use extract "提取前 10 封邮件的发件人、主题、时间,按重要性排序" >> "$REPORT"
browser-use close
# ...
echo "报告已生成: $REPORT"
```

## 定时任务

### Linux/macOS (crontab)

```bash
crontab -e
# 每日 09:00 执行
0 9 * * * /path/to/email_daily_summary.sh >> /path/to/logs/email_summary.log 2>&1
```

### macOS (launchd)

创建 `~/Library/LaunchAgents/com.email.dailysummary.plist`,设置 `StartCalendarInterval` 为 Hour=9, Minute=0,ProgramArguments 指向脚本路径,然后:

```bash
launchctl load ~/Library/LaunchAgents/com.email.dailysummary.plist
```

## 异常处理

### 1. browser-use CLI 未安装或不可用

- **现象**:执行 `browser-use` 报 `command not found`
- **处理**:`uv pip install browser-use[cli]` 后再执行 `browser-use install` 安装浏览器依赖

### 2. Chrome 会话过期或未登录

- **现象**:`--browser real` 打开邮箱后跳转到登录页
- **处理**:切换 `--headed` 模式手动登录一次,或在本机 Chrome 中重新登录目标邮箱后

### 3. CSS 选择器失效(DOM 改版)

- **现象**:`eval` 返回空数组或 `unread: 0` 但页面明显有未读邮件
- **处理**:`browser-use state` 重新探测当前 DOM,更新选择器(如 Gmail 由 `tr.zA` 改为 `tr.zB`),并将新选择器写入配置

### 4. 登录遇到二次验证或验证码

- **现象**:登录流程卡在 SMS 验证码或图形验证码页面
- **处理**:必须使用 `--headed` 模式由人工完成验证;自动化流程不可绕过验证码

### 5. 邮件列表加载缓慢

- **现象**:`state` 显示页面已加载但 `tr.zA` 数量为 0
- **处理**:在 `open` 与 `eval` 之间插入 `sleep 5`,或循环 `browser.scroll('down')` 触发懒加载

### 6. screenshot 写入失败

- **现象**:`browser-use screenshot` 报权限错误或路径不存在
- **处理**:执行前 `mkdir -p "$OUTPUT_DIR"` 创建目录,确认运行用户对目录有写权限

### 7. eval 脚本执行超时

- **现象**:邮件量大(>100 封)时 `eval` 单次执行超过浏览器脚本超时阈值
- **处理**:分批抓取,每次 `i < 20`,滚动后再抓取下一批,合并结果

### 8. crontab 环境变量缺失

- **现象**:手动执行正常,crontab 触发时报 `browser-use: command not found`
- **处理**:在脚本顶部显式 `export PATH=/usr/local/bin:/opt/homebrew/bin:$PATH`,或使用 `browser-use` 绝对路径

## FAQ

### Q1:如何避免在脚本中保存邮箱密码?

优先使用 `--browser real` 模式复用本机 Chrome 已登录会话,凭证由 Chrome 管理,脚本不接触密码。必须登录时,密码从系统环境变量或 keyring 读取,不硬编码.
### Q2:如何同时汇总多个邮箱?

顺序执行多个 `browser-use --browser real open <url>` 块,每个邮箱独立 `extract` 后追加到同一份 Markdown 报告,按邮箱分节展示。参考案例 3.
### Q3:AI 摘要功能(`extract`)需要什么配置?

`extract` 依赖 browser-use 内置 LLM,需配置 `OPENAI_API_KEY` 或同等 LLM 凭证。未配置时降级为纯 `eval` 抓取四元组,不生成 AI 摘要.
### Q4:如何切换到无头模式?

将 `--browser real` 替换为 `--headless`,但无头模式无法复用 Chrome 已登录会话,需改用 token 或手动登录流程。生产环境定时任务推荐保持 `--browser real` 并锁定屏幕.
### Q5:截图保存路径如何自定义?

通过 `OUTPUT_DIR` 环境变量控制,默认 `./email_summaries`。建议设置为绝对路径(如 `/var/log/email_summaries`)以便定时任务稳定写入.
### Q6:邮件量很大(>100 封)时如何处理?

分页抓取:每次 `eval` 取 20 封,`browser.scroll('down')` 触发加载,`sleep 1` 等待渲染,循环至 `tr.zA` 数量不再增长。合并所有批次后生成日报.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- CSS 选择器依赖邮箱 Web 版 DOM 结构,Gmail/Outlook 改版可能导致 `tr.zA`、`.zE` 等选择器失效,需定期校验
- `--browser real` 需要本机 Chrome 已登录目标邮箱,服务器或无 GUI 环境不适用
- 验证码、二次验证、风险控制验证必须人工干预,无法全自动绕过
- 仅支持 Web 邮箱自动化,不支持 IMAP/POP/SMTP 协议直连
- 单次抓取受浏览器渲染性能限制,超大量邮箱(>500 封/日)建议改用 IMAP 方案
- QQ 邮箱、163 邮箱的 Web 版反自动化策略可能导致 `--browser real` 失效,需 `--headed` 人工辅助
- 截图为整页快照,长收件箱可能被截断,需配合滚动分页截图

## 安全提示

1. 不在脚本中明文保存密码,优先 `--browser real` 复用会话
2. 敏感凭证使用环境变量或系统 keyring 存储
3. 定期检查邮箱授权应用列表,移除不需要的第三方访问
4. 启用邮箱两步验证,自动化仅复用已登录会话不绕过验证
5. 日志文件不记录邮件正文,仅记录发件人、主题、时间元数据
