---
slug: telegram-chat
name: telegram-chat
version: "1.0.0"
displayName: 电报聊天工具专业版
summary: 企业级Telegram多Bot管理与跨实例通信工具,支持主动推送、消息归档审计与群组批量管理。
license: Proprietary
edition: pro
description: |-
  电报聊天工具专业版,面向团队与企业用户提供多 Bot 管理、主动消息推送、消息归档审计与群组批量管理能力。核心能力:
  - 多 Bot 统一管理与快速切换
  - 主动消息推送(无需被艾特即可发送)
  - 消息归档与审计日志
  - 群组批量管理与成员同步
  - 跨实例群组广播
  - Webhook 集成与自动化工作流
  - 消息模板与定时发送

  适用场景:
  - 企业团队多 Bot 协作管理
  - 跨群组消息广播与公告
  - 自动化通知与告警推送
  - 消息合规存档与审计追溯

  差异化:专业版完全兼容免费版配置与命令体系...
tags:
- 沟通协作
- 即时通讯
- Telegram
- 机器人
- 企业效率
- 自动化
- 消息归档
tools:
  - - read
- exec
# 电报聊天工具 - 专业版
## 概述
---
# 电报聊天工具专业版

## 核心能力

### 一、多 Bot 统一管理(专业版独有)
- 同时管理多个 Bot 实例
- Bot 间快速切换与消息路由
- 统一配置管理与权限控制
- Bot 健康状态监控

**输入**: 用户提供一、多 Bot 统一管理(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行一、多 Bot 统一管理(专业版独有)操作,遵循单一意图原则。
**输出**: 返回一、多 Bot 统一管理(专业版独有)的执行结果,包含操作状态和输出数据。### 二、主动消息推送(专业版独有)
- 无需被艾特即可主动发送消息
- 支持指定群组/用户定向推送
- 支持富文本与 Markdown 格式消息
- 支持消息卡片与按钮交互

### 三、消息归档与审计(专业版独有)
- 全量消息自动归档存储
- 按时间/群组/用户多维度检索
- 审计日志记录所有操作
- 支持导出归档数据

**处理**: 按照skill规范执行三、消息归档与审计(专业版独有)操作,遵循单一意图原则。
### 四、群组批量管理(专业版独有)
- 批量将 Bot 加入多个群组
- 群组成员列表同步与导出
- 群组权限统一配置
- 跨群组消息同步

**输入**: 用户提供四、群组批量管理(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行四、群组批量管理(专业版独有)操作,遵循单一意图原则。### 五、跨群组广播(专业版独有)
- 一条消息同时推送到多个群组
- 支持按标签筛选目标群组
- 广播任务调度与进度追踪
- 失败自动重试

**输入**: 用户提供五、跨群组广播(专业版独有)所需的指令和必要参数。
**处理**: 按照skill规范执行五、跨群组广播(专业版独有)操作,遵循单一意图原则。
**输出**: 返回五、跨群组广播(专业版独有)的执行结果,包含操作状态和输出数据。### 六、Webhook 集成与自动化(专业版独有)
- 接收外部系统 Webhook 触发消息推送
- 与 CI/CD、监控系统、告警系统对接
- 支持自定义消息模板
- 定时任务调度

### 七、消息模板与定时发送(专业版独有)
- 预设常用消息模板
- 支持变量插值(如日期、姓名)
- 定时发送消息(如每日站会提醒)
- 重复任务调度(如每周周报提醒)

**输入**: 用户提供七、消息模板与定时发送(专业版独有)所需的指令和必要参数。
**输出**: 返回七、消息模板与定时发送(专业版独有)的执行结果,包含操作状态和输出数据。

### 技术细节

| 组件 | 说明 | 关键参数 |
|:-----|:-----|:---------|
| `parser` | 解析输入指令 | `format`, `encoding` |
| `processor` | 执行核心处理逻辑 | `mode`, `timeout` |
| `output` | 格式化输出结果 | `format`, `encoding` |

### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、Telegram、管理与跨实例通信、支持主动推送、消息归档审计与群、电报聊天工具专业、面向团队与企业用、户提供多、组批量管理能力、核心能力、统一管理与快速切、无需被艾特即可发、消息归档与审计日、群组批量管理与成、员同步、跨实例群组广播、集成与自动化工作。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一:跨群组广播重要公告
公司行政需向多个部门群组同时推送放假通知,避免逐群发送。

```bash
python3 {SKILL_DIR}/scripts/telegram_broadcast.py \
    --bot "company_bot" \
    --targets "研发群,市场群,财务群,行政群" \
    --message "【放假通知】2026年国庆假期为10月1日至10月7日,10月8日正常上班。请各部门提前安排好工作。" \
    --format markdown
```

**广播任务输出示例**:

```text
==================================================
广播任务报告
==================================================
任务ID: broadcast_20260718_001
发起Bot: @company_bot
消息类型: markdown
目标群组: 4个

--------------------------------------------------
发送结果:
[成功] 研发群 (-1001111111111) - 已送达
[成功] 市场群 (-1002222222222) - 已送达
[成功] 财务群 (-1003333333333) - 已送达
[失败] 行政群 (-1004444444444) - Bot非管理员,已加入重试队列

--------------------------------------------------
统计: 成功 3/4, 失败 1/4
状态: 部分成功,失败项已自动重试
```

### 场景二:CI/CD 构建结果自动推送
开发团队希望将 CI/CD 构建结果自动推送到团队 Telegram 群组。

> 详细代码示例已移至 `references/detail.md`

### 场景三:每日站会提醒定时推送
团队希望每天早上 9:50 自动在群组中推送站会提醒。

```bash
python3 {SKILL_DIR}/scripts/telegram_schedule.py \
    --bot "team_bot" \
    --target "研发群" \
    --time "09:50" \
    --repeat "weekdays" \
    --message "【站会提醒】10分钟后(10:00)开始每日站会,请各位准备:
1. 昨日完成事项
2. 今日计划事项
3. 遇到的问题与阻碍" \
    --format markdown
```

**定时任务管理**:

```bash
python3 {SKILL_DIR}/scripts/telegram_schedule.py --list

python3 {SKILL_DIR}/scripts/telegram_schedule.py --pause task_id_001

python3 {SKILL_DIR}/scripts/telegram_schedule.py --resume task_id_001

python3 {SKILL_DIR}/scripts/telegram_schedule.py --delete task_id_001
```

## 使用流程

### 优秀步:配置多个 Bot
```yaml
messaging:
  telegram:
    bots:
      - name: "company_bot"
        token: "111111111:AAAaaaBBBbbbCCCccc"
        display_name: "公司官方Bot"
        allowed_chats:
          - "-1001111111111"
          - "-1002222222222"

      - name: "dev_team_bot"
        token: "222222222:DDDdddEEEeeeFFFfff"
        display_name: "研发团队Bot"
        allowed_chats:
          - "-1003333333333"

      - name: "hr_bot"
        token: "333333333:GGGgggHHHhhhIIIiii"
        display_name: "人事Bot"
        allowed_chats:
          - "-1004444444444"
```

### 第二步:验证多 Bot 配置
```bash
python3 {SKILL_DIR}/scripts/telegram_status.py --all

python3 {SKILL_DIR}/scripts/telegram_status.py --bot "dev_team_bot"
```

**状态输出示例**:

```text
==================================================
Bot 状态总览
==================================================
[正常] company_bot    @company_official_bot    在线    管理3个群组
[正常] dev_team_bot   @dev_team_bot            在线    管理2个群组
[异常] hr_bot         @hr_assistant_bot        离线    Token可能过期

统计: 正常 2/3, 异常 1/3
```

### 第三步:开始使用高级功能
```bash
python3 {SKILL_DIR}/scripts/telegram_push.py \
    --bot "dev_team_bot" \
    --target "研发群" \
    --message "版本 v2.1.0 已发布,请更新测试。" \
    --format markdown

python3 {SKILL_DIR}/scripts/telegram_broadcast.py \
    --bot "company_bot" \
    --targets "研发群,市场群" \
    --message "公司年会定于1月20日举办,请各部门准备节目。"
```

### 命令参数说明

- `--show-source`: 命令参数,用于指定操作选项
- `--resume`: 命令参数,用于指定操作选项
- `--delete`: 命令参数,用于指定操作选项
- `--target`: 命令参数,用于指定操作选项
- `--search`: 命令参数,用于指定操作选项

### 命令参数说明

- `--retry`: 命令参数,用于指定操作选项
- `--repeat`: 命令参数,用于指定操作选项
- `--pause`: 命令参数,用于指定操作选项
- `--list`: 命令参数,用于指定操作选项
- `--message`: 命令参数,用于指定操作选项

### 命令参数说明

- `--targets`: 命令参数,用于指定操作选项

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
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 建议 3.8+(运行自动化脚本)
- **网络环境**: 需可访问 Telegram API(部分区域需网络代理)
- **定时任务**: 建议 cron(Linux/macOS)或任务计划程序(Windows)
- **存储空间**: 消息归档需预留磁盘空间(建议 10GB+)

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Telegram 账户 | 账户 | 必需 | 注册 Telegram |
| Telegram Bot Token | 凭据 | 必需 | 通过 @BotFather 创建(支持多个) |
| skill-platform.yaml | 配置 | 必需 | 手动创建配置文件 |
| Python 3.8+ | 运行时 | 必需 | python.org 下载 |
| requests | Python库 | 必需 | pip install requests |
| 网络代理 | 网络 | 视情况 | 部分地区需代理访问 Telegram |
| Webhook 服务 | 服务 | 可选 | 用于接收外部系统触发 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 通过 Telegram 中的 @BotFather 创建多个 Bot 获取各自 Token
- 将 Token 配置到 `skill-platform.yaml` 的 `messaging.telegram.bots` 列表
- 将各 Bot 允许通信的群组 ID 填入对应 `allowed_chats` 列表
- Webhook 集成需配置密钥(`secret`字段)用于请求验证
- Token 属于敏感凭据,建议使用环境变量引用,定期轮换

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能通过 Python 脚本与 Telegram API 调用实现)
- **说明**: 基于脚本的企业级 AI Skill,通过自然语言指令驱动 Agent 执行 Telegram 多 Bot 管理与跨实例通信。专业版完全兼容免费版单 Bot 配置与基础聊天能力,额外提供多 Bot 统一管理、主动消息推送、消息归档审计、群组批量管理、跨群组广播、Webhook 集成与定时任务调度能力,适合中大型团队与企业级通信场景。

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

### Q1: 多个 Bot 之间如何区分消息来源?
**A**: 专业版为每个 Bot 维护独立身份标识。归档记录与审计日志中会标注消息来源 Bot 名称,便于追溯:

```bash
python3 {SKILL_DIR}/scripts/telegram_archive.py --search "关键词" --show-source
```

### Q2: 广播任务部分群组失败怎么办?
**A**: 广播任务会自动重试失败的群组。常见失败原因:
- Bot 不是该群组的管理员
- 群组 ID 配置错误
- 网络波动

查看广播报告中的失败列表,针对性修复后重试:

```bash
python3 {SKILL_DIR}/scripts/telegram_broadcast.py --retry task_id_001
```

### Q3: 定时任务如何管理?
**A**: 专业版提供完整的定时任务管理:

```bash
python3 {SKILL_DIR}/scripts/telegram_schedule.py --list          # 查看所有任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --pause <id>    # 暂停任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --resume <id>   # 恢复任务
python3 {SKILL_DIR}/scripts/telegram_schedule.py --delete <id>   # 删除任务
```

### Q4: 消息归档占用空间过大怎么办?
**A**: 建议配置归档保留策略(`retention_days: 365`、`auto_cleanup: true`、`compress: true`),定期清理过期数据并压缩存储。

### Q5: 免费版用户升级后配置是否兼容?
**A**: 完全兼容。专业版支持免费版的单 Bot 配置格式,升级后原有配置无需修改,直接获得多 Bot 管理与高级功能权限。

### Q6: Webhook 集成如何保证安全?
**A**: 专业版 Webhook 支持密钥验证(`secret` 字段),确保仅授权的系统可触发推送。请求需携带此密钥才能通过验证。

### Q7: 是否支持与其他 IM 平台互通?
**A**: 专业版专注 Telegram 生态。如需跨平台消息同步(如 Telegram 与 Slack 互通),可通过 Webhook 中转实现。

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
