---
slug: smart-light-controller-pro
name: smart-light-controller-pro
version: "1.0.0"
displayName: 智能灯控(专业版)
summary: 全功能智能灯控方案，支持多灯同步、灯光秀、场景预设与定时计划。
license: Proprietary
edition: pro
description: |-
  智能灯控专业版是一款面向局域网智能灯泡的全功能控制方案，兼容 TP-Link Kasa 协议设备，覆盖单灯控制、多灯同步、灯光秀编排、场景预设、定时计划与日出日落联动等完整能力。核心能力：
  - 多灯批量同步控制，支持分组与级联编排
  - 灯光秀序列引擎，支持渐变、闪烁、节拍同步等过渡效果
  - 场景预设保存与一键切换，支持 JSON 配置导入导出
  - 定时计划任务与日出日落联动，自动适配地理位置
  - 设备健康监控与异常告警...
tags:
- 智能家居
- 灯光控制
- 自动化
- 场景编排
tools:
  - - read
- exec
---
# 智能灯控工具（专业版）

## 概述

专业版在免费版单灯核心操作基础上，扩展为全屋灯光管理平台。支持多灯批量同步、灯光秀序列编排、场景预设保存、定时计划任务与日出日落联动，适合智能家居爱好者、商业空间运营者与自动化开发者使用。所有指令均在局域网内完成，零云端依赖，隐私与延迟表现优异。

专业版新增并行指令调度引擎，可同时对数十盏灯泡下发指令并将延迟控制在 500 毫秒以内；内置设备健康监控，灯泡离线时自动告警并触发重连流程；提供 JSON 格式的场景配置文件，便于团队协作与版本管理。

## 核心能力

| 能力项 | 说明 | 专业版独有 |
|--------|------|-----------|
| 多灯批量同步 | 一条指令控制多盏灯泡 | 是 |
| 灯光秀编排 | 渐变、闪烁、节拍同步序列 | 是 |
| 场景预设管理 | 保存/切换/导入导出场景 | 是 |
| 定时计划任务 | Cron 表达式驱动灯光调度 | 是 |
| 日出日落联动 | 基于经纬度自动调整 | 是 |
| 设备健康监控 | 离线告警与自动重连 | 是 |
| 并行指令调度 | 多灯并行下发，延迟可控 | 是 |
| 单灯基础控制 | 开关、亮度、HSV、色温 | 否（免费版可用） |

## 使用场景

### 场景一：全屋观影模式（家庭用户）

用户一键将客厅、走廊、卧室灯光切换至观影场景：客厅灯调至 10% 暖色、走廊灯关闭、卧室灯调至 20% 蓝色。

```bash
uv run light_scene.py --apply movie-night
```

场景配置文件 `movie-night.json` 示例：

```json
{
  "name": "观影模式",
  "lights": [
    {"ip": "192.168.1.50", "on": true, "brightness": 10, "hsv": [30, 80, 40]},
    {"ip": "192.168.1.51", "on": false},
    {"ip": "192.168.1.52", "on": true, "brightness": 20, "hsv": [240, 80, 50]}
  ],
  "transition": 2.0
}
```

### 场景二：商业空间节庆灯光秀（运营者）

商场节日需要编排一段 60 秒的灯光秀，包含红绿交替闪烁与渐变过渡。运营者通过序列文件定义关键帧，引擎自动插值生成平滑过渡。

```bash
uv run light_show.py --ip 192.168.1.50,192.168.1.51,192.168.1.52 \
  --sequence festival.json --duration 60 --transition 1.5 --loop
```

序列文件 `festival.json` 示例：

```json
{
  "name": "节庆灯光秀",
  "steps": [
    {"time": 0, "hsv": [0, 100, 80], "brightness": 80},
    {"time": 3, "hsv": [120, 100, 80], "brightness": 80},
    {"time": 6, "hsv": [0, 100, 80], "brightness": 80, "off_flash": true}
  ]
}
```

### 场景三：日出唤醒自动化（开发者）

开发者利用定时计划与日出日落联动，实现每天日出前 30 分钟自动渐亮唤醒。系统根据本机经纬度自动计算日出时间，无需手动维护日期表。

```bash
uv run light_schedule.py --rule sunrise-wake --offset -30 --duration 20 \
  --target-brightness 80 --hsv 30 60 80
```

### 场景四：团队协作场景管理（团队用户）

团队成员通过 Git 共享场景配置仓库，新增场景后提交 Pull Request，审核合并后自动同步至所有执行节点。配置文件采用 JSON 格式，支持 Diff 对比与版本回滚。

## 不适用场景

以下场景智能灯控(专业版)不适合处理：

- 实际人员绩效评估
- 财务预算审批
- 合同法务审核


## 触发条件

需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于非本工具能力范围的需求。


## 快速开始

### 前置条件

- Python 3.11 及以上版本
- 已安装 uv 包管理器
- 灯泡与执行机器处于同一局域网
- 已知所有灯泡 IP 地址（建议在路由器绑定固定 IP）

### 120 秒上手

第一步，安装依赖：

```bash
uv pip install python-kasa>=0.10.2 astral>=3.2
```

第二步，批量发现并登记设备：

```bash
uv run light_registry.py --discover --save devices.json
```

第三步，创建第一个场景并应用：

```bash
uv run light_scene.py --create evening --template warm-dim
uv run light_scene.py --apply evening
```

第四步，设置定时计划：

```bash
uv run light_schedule.py --add "0 22 * * *" --scene evening
```

## 示例

### 多灯批量控制

```bash
# 同时控制三盏灯
uv run control_multi.py --ips 192.168.1.50,192.168.1.51,192.168.1.52 \
  --on --brightness 60 --hsv 200 50 60
```

### 灯光秀过渡效果

```bash
# 蓝红交替闪烁，忽略白色步骤以避免乒乓切换
uv run light_show.py --ip 192.168.1.50 \
  --duration 30 --transition 1 --off-flash --verbose
```

### 日出日落联动

```bash
# 日落时自动开灯
uv run light_schedule.py --rule sunset-on --offset 0 --scene evening

# 日出前 30 分钟渐亮唤醒
uv run light_schedule.py --rule sunrise-wake --offset -30 --duration 20
```

### 设备健康监控

```bash
# 启动后台监控守护进程
uv run light_monitor.py --interval 60 --alert-webhook https://your-hook.example/notify
```

## 最佳实践

### 1. 并行指令优化

多灯控制时启用并行调度，将延迟从串行的 N×200ms 降至并行的 200ms+N×10ms：

```bash
uv run control_multi.py --ips 192.168.1.50,192.168.1.51,192.168.1.52 \
  --on --parallel --max-concurrency 5
```

### 2. 场景配置版本管理

将场景配置文件纳入 Git 仓库，每次修改提交 Commit，便于回滚与审计：

```bash
git add scenes/*.json
git commit -m "feat: 新增观影模式场景"
```

### 3. 熔断与降级策略

当某盏灯泡连续 3 次无响应时，自动触发熔断跳过该设备，避免阻塞整批指令。熔断后每 5 分钟尝试一次恢复探测：

```bash
uv run control_multi.py --ips 192.168.1.50,192.168.1.51 \
  --on --circuit-breaker --threshold 3 --recovery-interval 300
```

### 4. 批量检查点与幂等

灯光秀执行过程中每 5 秒写入检查点，中断后可从断点恢复，避免从头重放：

```bash
uv run light_show.py --sequence festival.json --checkpoint --resume
```

### 5. 增量状态同步

定期拉取所有灯泡当前状态并与预期对比，发现漂移时自动校正，保持场景一致性。

## 常见问题

### Q1：多灯同步时部分灯泡延迟明显？

排查步骤：
1. 确认所有灯泡固件版本一致（旧固件响应较慢）
2. 检查路由器是否启用 QoS 限制了 9999 端口带宽
3. 启用并行调度并调高 `--max-concurrency`
4. 将灯泡与执行机器接入同一交换机，减少路由跳数

### Q2：灯光秀过渡出现卡顿？

过渡卡顿通常由指令间隔过短导致。建议：单灯过渡间隔不小于 100 毫秒；多灯序列使用 `--transition` 参数控制插值步长；避免在 1 秒内发送超过 10 条指令。

### Q3：日出日落时间不准？

专业版使用 astral 库根据经纬度计算日出日落。首次使用时需配置本机经纬度：

```bash
uv run light_config.py --set-location --lat 39.9 --lon 116.4
```

### Q4：场景配置文件如何分享？

场景配置为标准 JSON 格式，可直接分享文件或通过 Git 仓库协作。导入他人场景时建议先用 `--dry-run` 预览效果：

```bash
uv run light_scene.py --import friend-scene.json --dry-run
```

### Q5：设备离线后如何自动恢复？

启动 `light_monitor.py` 守护进程后，离线设备每 5 分钟自动探测一次。恢复在线后自动同步当前场景状态。告警可通过 Webhook 推送至飞书、钉钉等渠道。

### Q6：能否与智能家居平台联动？

专业版支持通过 Webhook 与 Home Assistant、开源自动化平台等集成。灯光事件可触发外部联动，外部事件也可通过 HTTP 接口触发灯光场景切换。

### Q7：如何备份全部场景与计划？

```bash
uv run light_config.py --export backup.tar.gz --include scenes schedules devices
```

### Q8：专业版是否支持 IKEA TRADFRI？

专业版通过适配层支持 IKEA TRADFRI 设备（需配合 DIRIGERA 网关），使用 `--protocol tradfri` 参数指定。注意 TRADFRI 的响应延迟略高于 Kasa。

### Q9：多用户同时控制会冲突吗？

专业版内置指令锁机制，同一灯泡的指令按时间戳排队执行，避免冲突。团队协作时建议按区域划分控制权限。

### Q10：如何监控灯光使用统计？

```bash
uv run light_stats.py --range 30d --output usage-report.html
```

## 依赖说明

### 运行环境

- **Agent 平台**：支持 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**：Windows / macOS / Linux
- **Python**：3.11 及以上版本
- **网络**：执行机器与灯泡处于同一局域网

### 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 | 版本兼容性 |
|:-------|:-----|:---------|:---------|:-----------|
| python-kasa | Python 库 | 必需 | `uv pip install python-kasa>=0.10.2` | 兼容 0.10.x - 0.13.x |
| astral | Python 库 | 日出日落功能必需 | `uv pip install astral>=3.2` | 兼容 3.x |
| uv | 包管理器 | 推荐 | `pip install uv` | 兼容 0.4+ |
| LLM API | API | 必需 | 由 Agent 平台内置 LLM 提供 | 不限 |

### API Key 配置

- 本工具基于局域网直连，无需云端 API Key
- 日出日落计算使用本地 astral 库，无需在线服务
- 告警 Webhook 地址存储于环境变量 `LIGHT_ALERT_WEBHOOK`
- 场景配置中的设备 IP 建议通过 `devices.json` 统一管理
- 禁止在脚本中硬编码设备凭据或 Webhook 密钥

### 可用性分类

- **分类**：MD+EXEC（纯 Markdown 指令，核心功能需 exec 命令行执行能力）
- **说明**：基于 Markdown 的 AI Skill，通过自然语言指令驱动 Agent 执行多灯编排与场景管理任务

## 专业版特性

本专业版相比免费版新增以下能力：

- 多灯批量同步控制：一条指令管理全屋灯光，并行调度延迟低于 500 毫秒
- 灯光秀序列引擎：支持渐变、闪烁、节拍同步、关键帧插值等过渡效果
- 场景预设管理：保存/切换/导入导出场景配置，支持 Git 版本管理
- 定时计划任务：Cron 表达式驱动灯光调度，支持复杂时间规则
- 日出日落联动：基于经纬度自动计算日出日落时间，无需手动维护
- 设备健康监控：离线告警、自动重连、熔断降级、增量状态同步
- IKEA TRADFRI 适配：通过 DIRIGERA 网关支持 TRADFRI 设备
- 优先技术支持：工作日 4 小时内响应，提供 SLA 保障

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | 0 元 | 单灯核心控制 + 基础示例 | 个人试用 |
| 收费专业版 | 29.9 元/月 | 全功能 + 高级特性 + 优先支持 | 团队/企业 |

专业版通过 Skill 平台付费发布，支持按月订阅与一次性买断（999 元）。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
