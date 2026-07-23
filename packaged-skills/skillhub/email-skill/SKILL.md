---
slug: "email-skill"
name: "email-skill"
version: "1.0.0"
displayName: "Email"
summary: "SMTP邮件发送自动化,支持多供应商、附件、HTML模板与TLS加密"
license: "Proprietary"
description: |-
  基于SMTP协议的邮件发送自动化Skill,支持Gmail、Outlook、QQ邮箱等主流服务商。
  提供纯文本与HTML双模式、多附件并行上传、CC/BCC收件人编排、测试邮件校验、
  TLS/SSL加密传输与企业级凭据管理。适用于发信通知、报表投递、告警推送、
  营销触达等需要程序化邮件输出的自动化场景。
tags:
  - 通用办公
  - SMTP
  - Automation
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
---
# Email

基于SMTP协议的邮件发送自动化Skill,围绕"配置-校验-投递-追踪"四个环节提供端到端的发信能力。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| **多附件并行投递**:通过`--attachment`参数重复传入多个文件路径,单邮件总附件大小受服务商限制(主流为25MB),超过阈值时自动给出分片建议。 | 支持 | 支持 |
| **收件人编排**:支持`--to`、`--cc`、`--bcc`三组收件人列表,支持逗号分隔批量录入,自动去重并校验邮箱格式。 | 不支持 | 支持 |
| **测试邮件链路**:`--test`标志触发最小化测试邮件,用于在正式发信前验证凭据、端口、网络连通性。 | 不支持 | 支持 |
| **凭据双通道**:支持`email_config.json`配置文件与环境变量两种凭据注入方式,环境变量优先级更高,适配容器化部署。 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 核心能力

- **多供应商适配**:内置Gmail(smtp.gmail.com:587)、Outlook/Office365(smtp.office365.com:587)、Yahoo(smtp.mail.yahoo.com:587)、QQ邮箱(smtp.qq.com:587)及自定义SMTP服务器的连接预设,自动协商TLS/SSL。
- **双内容模式**:支持纯文本(`--body`)与HTML富文本(`--html-file`)两种正文形态,HTML模式可内联CSS样式但不执行JavaScript。
- **多附件并行投递**:通过`--attachment`参数重复传入多个文件路径,单邮件总附件大小受服务商限制(主流为25MB),超过阈值时自动给出分片建议。
- **收件人编排**:支持`--to`、`--cc`、`--bcc`三组收件人列表,支持逗号分隔批量录入,自动去重并校验邮箱格式。
- **测试邮件链路**:`--test`标志触发最小化测试邮件,用于在正式发信前验证凭据、端口、网络连通性。
- **凭据双通道**:支持`email_config.json`配置文件与环境变量两种凭据注入方式,环境变量优先级更高,适配容器化部署。
- **投递结果结构化**:Python API返回`{"success": bool, "message_id": str, "attachments": int, "error": str}`结构,便于上游工作流做条件分支。
### 多供应商适配

执行多供应商适配操作,处理用户输入并返回结果。

**输入**: 用户提供多供应商适配所需的参数和指令。

**输出**: 返回多供应商适配的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`多供应商适配`相关配置参数进行设置
### 双内容模式

执行双内容模式操作,处理用户输入并返回结果。

**输入**: 用户提供双内容模式所需的参数和指令。

**输出**: 返回双内容模式的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`双内容模式`相关配置参数进行设置
### 多附件并行投递

执行多附件并行投递操作,处理用户输入并返回结果。

**输入**: 用户提供多附件并行投递所需的参数和指令。

**输出**: 返回多附件并行投递的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`多附件并行投递`相关配置参数进行设置
#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`email-skill`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 环境准备

### 凭据配置文件

在工作目录创建`email_config.json`:

```json
{
  "smtp_server": "smtp.gmail.com",
  "smtp_port": 587,
  "username": "your-email@gmail.com",
  "password": "your-app-password",
  "sender_name": "自动化助手",
  "use_tls": true,
  "use_ssl": false
}
```

### Gmail应用专用密码

Gmail禁止直接使用账号登录密码,必须使用应用专用密码:

1. 在Google账号开启两步验证(2FA)。
2. 访问`https://myaccount.google.com/security`,进入"应用密码"。
3. 选择"邮件"应用生成16位应用专用密码,填入`password`字段。

### 环境变量注入(推荐用于生产)

```bash
export SMTP_SERVER=smtp.gmail.com
export SMTP_PORT=587
export EMAIL_USERNAME=your-email@gmail.com
export EMAIL_PASSWORD=your-app-password
export EMAIL_SENDER_NAME="自动化助手"
```

## 适用场景

### 场景一:日报报表投递

- **输入**:数据团队产出的`daily_report.xlsx`与收件人列表`team@company.com`。
- **处理**:读取报表文件,以附件形式投递,正文嵌入当日关键指标摘要(HTML表格)。
- **输出**:收件人邮箱收到带附件的HTML邮件,投递结果返回`message_id`用于追踪。

### 场景二:告警通知推送

- **输入**:监控系统触发的告警JSON,包含级别、时间、指标值。
- **处理**:将告警级别映射为邮件主题前缀(`[P0]`/`[P1]`),正文以红色高亮关键指标,投递至值班工程师邮箱。
- **输出**:值班工程师在30秒内收到带优先级标识的告警邮件。

### 场景三:营销批次触达

- **输入**:CSV格式的收件人清单(含姓名、定制化字段)与HTML邮件模板。
- **处理**:逐行解析CSV,变量替换后通过BCC方式批量投递,单批不超过服务商速率限制(如Gmail约100封/分钟)。
- **输出**:完成批次投递统计，返回成功/失败计数与失败明细。

## 案例展示

### 案例1:发送带双附件的项目周报

```bash
python email_sender.py \
  --to "pm@company.com" \
  --cc "dev-leads@company.com" \
  --subject "[周报] 后端服务第28周交付总结" \
  --body "附件为本周交付物与缺陷清单,请于周五前确认。" \
  --attachment "weekly_summary.pdf" \
  --attachment "defects.xlsx"
```

执行成功输出:

```
Email sent successfully
Message-ID: <1894a3b2...@smtp.gmail.com>
Attachments: 2
Recipients: 2 (1 to + 1 cc)
```

### 案例2:HTML格式的产品发布通知

先将HTML正文写入文件`release_notice.html`:

```html
<h2 style="color:#1a73e8;">v2.4.0 已发布</h2>
<p>本次发布包含以下改进:</p>
<ul><li>搜索响应速度提升 35%</li><li>新增批量导出能力</li></ul>
```

随后投递:

```bash
python email_sender.py \
  --to "all-staff@company.com" \
  --subject "[发布通知] v2.4.0" \
  --html-file "release_notice.html"
```

### 案例3:Python API集成到Airflow DAG

```python
from email_sender import EmailSender

sender = EmailSender("email_config.json")
result = sender.send_email(
    to_email="data-ops@company.com",
    subject="ETL 任务失败告警",
    body="task_id=etl_user_dim, duration=1800s, error=connection_timeout",
    attachments=["/opt/airflow/logs/etl_user_dim.log"]
)
if not result["success"]:
    raise RuntimeError(f"告警邮件投递失败: {result['error']}")
```

## 异常处理


### AUTH_001 应用专用密码缺失或失效

- **现象**:`smtplib.SMTPAuthenticationError: 535 Username and Password not accepted`。
- **原因**:Gmail账号未启用2FA,或应用专用密码过期/被撤销。
- **处理**:重新生成16位应用专用密码,确认账号2FA处于开启状态,更新`email_config.json`或环境变量后重投。

### CONN_002 SMTP端口被防火墙拦截

- **现象**:`smtplib.SMTPConnectError: Connection refused`或`socket.timeout`。
- **原因**:587端口被企业出口防火墙拦截,或服务商针对该IP限流。
- **处理**:切换至465(SSL)端口并设置`use_ssl=true`、`use_tls=false`;若仍失败,改用服务商提供的API投递通道(如Gmail API)。

### ATTACH_003 附件超过25MB阈值

- **现象**:`smtplib.SMTPDataError: 552 Message size exceeds fixed limit`。
- **原因**:单邮件总附件体积超过服务商硬限制(Gmail/Outlook为25MB)。
- **处理**:压缩附件或拆分为多封邮件;对超大文件改用云存储链接(OneDrive/Google Drive)放入正文,附件只保留摘要。

### FORMAT_004 收件人邮箱格式非法

- **现象**:`ValueError: Invalid recipient format: user@`。
- **原因**:`--to`参数中存在缺失域名或非法字符的邮箱字符串。
- **处理**:调用前以正则`^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$`校验,剔除空项与重复项后。

### ENCODING_005 主题包含非ASCII字符乱码

- **现象**:收件方主题显示为`=?utf-8?b?...?=`未解码或`???`。
- **原因**:未对Subject做RFC 2047编码,直接传入原始字节。
- **处理**:使用`email.header.Header(subject, 'utf-8').encode()`构造主题,确保多语言字符正确显示。

### RATE_006 触发服务商发信速率限制

- **现象**:`SMTPSenderRefused: 550 5.4.5 Daily user sending quota exceeded`。
- **原因**:短时间投递量超过服务商配额(Gmail普通账号约500封/天)。
- **处理**:引入令牌桶限速(建议50封/分钟),超出配额时切换备用发信账号或队列暂存次日重投。

### SSL_007 TLS握手协商失败

- **现象**:`ssl.SSLError: [SSL: WRONG_VERSION_NUMBER]`。
- **原因**:端口与加密模式错配,如465端口使用了STARTTLS而非隐式SSL。
- **处理**:核对`smtp_port`与`use_tls`/`use_ssl`组合(587配合TLS,465配合SSL),必要时升级Python至3.8以上以支持现代TLS 1.2。

### CONFIG_008 凭据文件路径不可达

- **现象**:`FileNotFoundError: email_config.json`。
- **原因**:工作目录与配置文件不在同一路径,或容器未挂载凭据卷。
- **处理**:使用绝对路径`EmailSender("/etc/secrets/email_config.json")`,或改用环境变量注入,避免依赖相对路径。

## FAQ

### Q1: 是否支持接收与解析邮件(IMAP/POP3)?

不支持。本Skill专注于SMTP发信链路,接收侧请使用`imap-tools`或服务商API单独实现,避免与发信凭据混用。

### Q2: 一封邮件最多能带多少附件?

受服务商总大小限制(Gmail/Outlook为25MB,QQ邮箱为50MB)。附件数量无硬上限,但建议单邮件不超过10个以保证客户端渲染体验。

### Q3: 能否通过代理服务器发信?

可以。在`email_config.json`中新增`proxy_host`与`proxy_port`字段,SMTP连接将通过SOCKS5代理转发,适用于内网隔离环境。

### Q4: HTML邮件为何在Outlook客户端样式错乱?

Outlook使用Word渲染引擎,不支持`flex`、`grid`、`border-radius`等现代CSS。建议使用表格布局与内联样式,避免外部CSS引入。

### Q5: 如何避免邮件被识别为垃圾邮件?

配置SPF、DKIM、DMARC三条DNS记录;使用固定发信域名;正文避免全图片、敏感词与超额链接;逐步预热发信IP而非突发大批量投递。

### Q6: 多账号轮询发信如何实现?

在`email_config.json`中以`accounts`数组提供多组凭据,SDK内部按权重轮询并在单账号触发RATE_006时自动切换至下一个账号。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 仅支持SMTP发信协议,不覆盖IMAP/POP3收信与邮件全文检索。
- 附件大小受服务商硬限制约束,无法绕过;超大文件需改用云链接方案。
- HTML正文中的JavaScript会被所有主流邮箱客户端剥离,无法执行动态逻辑。
- 发信速率与日配额由服务商策略决定,本Skill仅做本地限速建议,无法突破服务商上限。
- 凭据明文存储于配置文件存在风险,生产环境必须改用环境变量或密钥管理服务(如Vault)。
- 国际化邮件头编码依赖Python标准库,低版本Python(3.8以下)对复杂字符集支持有限。
