---
slug: "tts-whatsapp-paid"
name: "tts-whatsapp-paid"
version: 1.0.1
displayName: "WhatsApp语音消息专业版"
summary: "企业级WhatsApp语音消息工具,支持群发广播、定时发送、批量处理与消息模板,适配团队协作。。面向团队与企业用户的 WhatsApp 语音消息工具(专业版)。核心能力: - 涵盖免费版全部"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与企业用户的 WhatsApp 语音消息工具(专业版)。核心能力:
  - 涵盖免费版全部能力(Piper TTS、40+ 语言、单条发送)
  - 群组广播:发送到 WhatsApp 群组
  - 批量发送:联系人列表群发
  - 定时发送:cron 任务自动发送
  - 消息模板:变量替换与个性化
  - 多语言批量:一次任务多语言消息
  - 发送队列与并发控制
  - 发送报告与状态追踪
  - API 服务化:FastAPI 封装
  - 联系人管理(CRM)集成

  适用场景:
  - 企业客服语音消息群发
  - 营销活动语...
tags:
  - 创意设计
  - 语音合成
  - WhatsApp
  - 企业级
  - 群发广播
  - 自动化
  - 社交
  - 通信
  - self
  - target
  - 不支持
  - lang
  - message
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Communication"
---
# WhatsApp语音消息专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| WhatsApp语音消息专业版定时发送 | 不支持 | 支持 |
| WhatsApp语音消息专业版批量处理 | 不支持 | 支持 |
| 多渠道消息批量发送 | 不支持 | 支持 |
| 消息模板与变量注入 | 不支持 | 支持 |
| 送达状态实时回调 | 不支持 | 支持 |

## 核心能力

### 免费版 vs 专业版对比
| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-----|:-----|:-----|
| TTS 合成 | 支持 | 支持 | - |
| 多语言 | 40+ | 40+ | - |
| 单人发送 | 支持 | 支持 | - |
| 音质/语速 | 支持 | 支持 | - |
| 自动清理 | 支持 | 支持 | - |
| 群组发送 | 不支持 | 支持 | 群广播 |
| 批量发送 | 不支持 | 联系人列表群发 | 生产力 |
| 定时发送 | 不支持 | cron 任务 | 自动化 |
| 消息模板 | 不支持 | 变量替换 | 个性化 |
| 多语言批量 | 不支持 | 一次任务多语言 | 国际化 |
| 发送队列 | 不支持 | 并发控制 | 高吞吐 |
| 发送报告 | 不支持 | 状态追踪 | 审计 |
| API 服务 | 不支持 | FastAPI | 远程调用 |
| CRM 集成 | 不支持 | 联系人管理 | 客户运营 |

**输入**: 用户提供免费版 vs 专业版对比所需的指令和必要参数.
**输出**: 返回免费版 vs 专业版对比的处理结果,包含执行状态码、结果数据和执行日志.
### TTS 合成

针对TTS 合成,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供TTS 合成相关的配置参数、输入数据和处理选项.
**输出**: 返回TTS 合成的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`TTS 合成`的配置文档进行参数调优
### 多语言

针对多语言,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供多语言相关的配置参数、输入数据和处理选项.
**输出**: 返回多语言的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`多语言`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一:群组广播
发送语音消息到 WhatsApp 群组.
```bash
# 发送到群组(使用群组 ID)
tts-whatsapp "各位同事,明天上午十点有团队会议,请准时参加。" \
    --lang zh_CN \
    --voice zh_CN-huayan-medium \
    --target "120363257357161211@g.us"
# ...
# 群组通知(多语言版本)
tts-whatsapp "Team, reminder: meeting tomorrow at 10 AM." \
    --lang en_US \
    --target "group-id@g.us"
```

### 场景二:批量个性化发送
基于联系人列表批量发送个性化语音消息.
```python
import csv
import subprocess
import os
# ...
class BatchWhatsAppSender:
    """批量 WhatsApp 语音发送器"""
# ...
    def __init__(self, default_lang="zh_CN", voice="zh_CN-huayan-medium"):
        self.default_lang = default_lang
        self.voice = voice
        self.results = []
# ...
    def send_from_csv(self, csv_path, template):
        """从 CSV 批量发送
# ...
        Args:
            csv_path: 联系人 CSV 文件路径
            template: 消息模板,用 {name} 等占位符
        """
        with open(csv_path, "r", encoding="utf-8") as f:
            readers = csv.DictReader(f)
            for row in readers:
                # 变量替换
                message = template.format(**row)
                target = row["phone"]
# ...
                # 根据联系人语言选择
                lang = row.get("language", self.default_lang)
                voice = row.get("voice", self.voice)
# ...
                # 发送
                result = self.send_one(message, target, lang, voice)
                self.results.append({
                    "name": row.get("name", ""),
                    "phone": target,
                    "status": "success" if result else "failed",
                    "message": message[:50]
                })
# ...
        self.generate_report()
# ...
    def send_one(self, text, target, lang, voice):
        """发送单条"""
        try:
            cmd = [
                "tts-whatsapp", text,
                "--lang", lang,
                "--voice", voice,
                "--target", target,
                "--quality", "medium"
            ]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
            return result.returncode == 0
        except Exception as e:
            print(f"发送失败 {target}: {e}")
            return False
# ...
    def generate_report(self):
        """生成发送报告"""
        success = sum(1 for r in self.results if r["status"] == "success")
        failed = len(self.results) - success
# ...
        print(f"\n发送报告")
        print(f"成功: {success}")
        print(f"失败: {failed}")
        print(f"总计: {len(self.results)}")
# ...
        # 保存详细报告
        with open("send_report.csv", "w", encoding="utf-8") as f:
            f.write("name,phone,status,message\n")
            for r in self.results:
                f.write(f"{r['name']},{r['phone']},{r['status']},{r['message']}\n")
# ...
# 使用
sender = BatchWhatsAppSender()
sender.send_from_csv(
    "contacts.csv",
    "你好 {name},提醒您:{event} 将于 {time} 开始。"
)
```

```csv
# contacts.csv
name,phone,language,event,time
张三,+8613800138000,zh_CN,产品评审会,2026-07-20 14:00
李四,+8613800138001,zh_CN,产品评审会,2026-07-20 14:00
John,+15555550123,en_US,Product Review,2026-07-20 14:00
```

### 场景三:定时发送
配置定时任务自动发送语音消息.
```python
import schedule
import time
import subprocess
# ...
class ScheduledSender:
    """定时语音消息发送器"""
# ...
    def __init__(self):
        self.jobs = []
# ...
    def add_daily(self, time_str, message, target, lang="zh_CN"):
        """添加每日定时任务"""
        schedule.every().day.at(time_str).do(
            self._send, message=message, target=target, lang=lang
        )
        self.jobs.append({"type": "daily", "time": time_str, "target": target})
# ...
    def add_weekly(self, day, time_str, message, target, lang="zh_CN"):
        """添加每周定时任务"""
        getattr(schedule.every(), day).at(time_str).do(
            self._send, message=message, target=target, lang=lang
        )
        self.jobs.append({"type": "weekly", "day": day, "time": time_str})
# ...
    def _send(self, message, target, lang):
        """执行发送"""
        cmd = ["tts-whatsapp", message, "--lang", lang, "--target", target]
        result = subprocess.run(cmd, capture_output=True, text=True)
        status = "成功" if result.returncode == 0 else "失败"
        print(f"[{time.strftime('%H:%M:%S')}] {status}: {message[:30]}")
# ...
    def run(self):
        """启动调度器"""
        print(f"已加载 {len(self.jobs)} 个定时任务")
        for job in self.jobs:
            print(f"  - {job}")
        while True:
            schedule.run_pending()
            time.sleep(60)
# ...
# 使用
scheduler = ScheduledSender()
# ...
# 每天早上 9 点发送提醒
scheduler.add_daily("09:00", "早上好!记得查看今日待办事项。", "+8613800138000")
# ...
# 每周一发送周报提醒
scheduler.add_weekly("monday", "10:00",
    "各位同事,请记得提交本周工作周报。", "group-id@g.us")
# ...
scheduler.run()
```

### 场景四:API 服务化
将语音消息发送封装为 API 服务.
```python
from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import JSONResponse
import subprocess
# ...
app = FastAPI(title="WhatsApp TTS 服务", version="1.0.0")
# ...
@app.post("/api/v1/send")
async def send_voice(
    text: str,
    target: str,
    lang: str = "zh_CN",
    voice: str = None,
    quality: str = "medium",
    speed: float = 1.0,
    background_tasks: BackgroundTasks = None
):
    """发送单条语音消息"""
    cmd = ["tts-whatsapp", text, "--lang", lang, "--target", target,
           "--quality", quality, "--speed", str(speed)]
    if voice:
        cmd.extend(["--voice", voice])
# ...
    result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
# ...
    if result.returncode == 0:
        return JSONResponse({"status": "success", "target": target})
    return JSONResponse({"status": "failed", "error": result.stderr}, status_code=500)
# ...
@app.post("/api/v1/broadcast")
async def broadcast(
    text: str,
    targets: list,
    lang: str = "zh_CN",
    background_tasks: BackgroundTasks = None
):
    """批量群发(异步)"""
    def send_batch():
        for target in targets:
            subprocess.run(
                ["tts-whatsapp", text, "--lang", lang, "--target", target],
                capture_output=True, timeout=30
            )
# ...
    background_tasks.add_task(send_batch)
    return {"status": "accepted", "count": len(targets)}
# ...
@app.post("/api/v1/schedule")
async def schedule_send(
    text: str,
    target: str,
    send_at: str,
    lang: str = "zh_CN"
):
    """定时发送(需配合调度器)"""
    # 写入调度队列
    with open("schedule_queue.json", "a", encoding="utf-8") as f:
        import json
        json.dump({"text": text, "target": target, "time": send_at, "lang": lang}, f)
        f.write("\n")
    return {"status": "scheduled", "send_at": send_at}
# ...
# 启动: uvicorn server:app --host 0.0.0.0 --port 8000
```

## 使用流程

### 依赖说明

### 运行环境
1. **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux
3. **Python**: 3.9 及以上
4. **网络**: 需访问 WhatsApp(发送消息时)

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| piper-tts | Python 库 | 必需 | `pip install piper-tts` |
| ffmpeg | 系统工具 | 必需 | `brew install ffmpeg` / `apt install ffmpeg` |
| schedule | Python 库 | 可选(定时) | `pip install schedule` |
| fastapi | Python 库 | 可选(API) | `pip install fastapi uvicorn` |
| WhatsApp 连接 | 服务 | 必需 | 本地配置或桥接服务 |
| Python 3.9+ | 运行时 | 必需 | `python.org` 下载 |
| 语音模型 | 数据文件 | 必需 | 从 Piper 仓库下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
5. TTS 合成**无需任何 API Key**(Piper 本地运行)
6. WhatsApp 发送需配置连接(通过本地桥接服务)
7. API 服务化建议配置鉴权 Token 保护接口
8. 企业部署建议通过密钥管理服务统一托管认证凭据

### 可用性分类
9. **分类**: MD+EXEC()
10. **说明**: 基于Markdown的AI Skill,。专业版支持群发广播、定时发送与 API 服务化,适合企业级语音消息触达场景.
#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | tts-whatsapp处理的内容输入 |,  |
| content | string | 否 | tts-whatsapp处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "whatsapp 相关配置参数",
    result: "whatsapp 相关配置参数",
    result: "whatsapp 相关配置参数",
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
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|---:|:---|---:|---:|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 批量发送配置
```yaml
# broadcast-config.yaml
broadcast:
  contacts_file: "contacts.csv"
  template: "你好 {name},{message}"
  default_lang: "zh_CN"
  default_voice: "zh_CN-huayan-medium"
  quality: "medium"
  speed: 1.0
  max_concurrent: 3
  retry: 2
  delay_between: 2  # 秒
  report_file: "send_report.csv"
```

### 定时任务配置
```yaml
# schedule-config.yaml
schedules:
  - name: "每日提醒"
    time: "09:00"
    message: "早上好!记得查看今日待办。"
    target: "+8613800138000"
    lang: "zh_CN"
# ...
  - name: "周报提醒"
    day: "monday"
    time: "10:00"
    message: "请记得提交本周工作周报。"
    target: "group-id@g.us"
    lang: "zh_CN"
```

### 消息模板变量
| 变量 | 说明 | 示例 |
|:------:|--------|:-------|
| `{name}` | 联系人姓名 | 张三 |
| `{phone}` | 手机号 | +86138... |
| `{event}` | 事件名称 | 产品评审会 |
| `{time}` | 时间 | 14:00 |
| `{date}` | 日期 | 2026-07-20 |
| 自定义 | CSV 任意字段 | 任何列名 |

## 常见问题

### 错误恢复步骤
| 错误场景(续)| 原因 | 处理方式 |
|----|:--:|---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制
是的。WhatsApp 对批量消息有限制。建议:
- 控制发送频率(每条间隔 2-5 秒)
- 每日不超过 1000 条
- 使用 WhatsApp Business API 获得更高配额
- 获得接收者明确同意

### Q2: 定时发送如何保证执行?
- 使用系统 cron(最可靠)
- 或 Python schedule + 后台进程
- 任务持久化到文件,重启后恢复
- 监控进程存活,异常时告警

### Q3: 消息模板如何定制?
使用 Python 字符串格式化,`{name}` 等占位符在发送时替换为 CSV 中的实际值。支持任意字段名.
### Q4: 多语言批量如何实现?
在 CSV 中为每个联系人指定 `language` 和 `voice` 字段,发送时自动选择对应语言的语音模型.
### Q5: 专业版与免费版的迁移?
零迁移成本。专业版是免费版的超集,命令行完全兼容。升级后原有单条发送继续可用,新特性按需启用.
### Q6: API 服务的并发能力?
单实例支持 5-10 并发(受 TTS 合成速度限制)。大批量建议使用任务队列异步处理。可通过多实例部署线性扩展.
## 错误处理

| 错误场景(续)(续)| 原因 | 处理方式 |
|----------|----------|----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 补充限制说明

- 需要LLM支持
- 依赖Agent平台的LLM能力与运行环境配置
- 免费版功能受限，高级能力需升级专业版
