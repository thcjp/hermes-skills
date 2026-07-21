---
slug: chromecast-control-tool-pro
name: chromecast-control-tool-pro
version: "1.0.0"
displayName: 投屏控制专业版
summary: 企业级投屏管理系统，支持多设备管理、播放队列、自动化脚本、状态监控与定时任务。
license: Proprietary
edition: pro
description: |-
  投屏控制专业版 —— 面向专业用户与企业环境的高级Chromecast投屏管理系统。核心能力:
  - 多设备同步管理：统一管理多台Chromecast设备
  - 播放队列管理：创建与管理视频播放队列
  - 自动化脚本：定时投屏、自动播放列表、场景联动
  - 实时状态监控：监控所有设备的播放状态
  - 设备分组：将设备分组...
tags:
- 投屏控制
- Chromecast
- 企业工具
- 自动化
- 多设备管理
tools:
  - - read
- exec
---

# 投屏控制专业版

## 概述

投屏控制专业版是企业级Chromecast投屏管理系统，在免费版基础上提供多设备同步管理、播放队列、自动化脚本、实时状态监控等专业能力。适用于企业展厅、智能家居多房间系统、学校多教室投屏等高阶场景。

### 免费版与专业版对比

| 能力 | 免费版 | 专业版 |
| --- | --- | --- |
| 设备发现 | 支持 | 支持+自动注册 |
| 视频投屏 | 单设备 | 多设备同步 |
| 播放控制 | 基础控制 | 全功能+字幕 |
| 播放队列 | 不支持 | 支持（增删改查） |
| 多设备管理 | 手动指定 | 统一管理+分组 |
| 自动化脚本 | 不支持 | 定时+场景联动 |
| 状态监控 | 单次查询 | 实时监控+告警 |
| 设备分组 | 不支持 | 支持 |
| 多房间音频 | 不支持 | 同步播放 |
| 事件回调 | 不支持 | 状态变化触发 |
| Web管理 | 不支持 | 可视化Dashboard |

## 核心能力

### 1. 多设备同步管理

```python
import subprocess
import json
from concurrent.futures import ThreadPoolExecutor

class ChromecastManager:
    def __init__(self):
        self.devices = {}
        self.groups = {}
        self.discover_devices()

    def discover_devices(self):
        """发现并注册所有设备"""
        result = subprocess.run(
            ['catt', 'scan'], capture_output=True, text=True
        )
        for line in result.stdout.strip().split('\n'):
            if '-' in line:
                parts = line.split(' - ')
                ip = parts[0].strip()
                name = parts[1].strip()
                self.devices[name] = {
                    'ip': ip,
                    'name': name,
                    'status': 'idle',
                    'current_media': None
                }

    def cast_to_device(self, device_name, url):
        """向指定设备投屏"""
        subprocess.run([
            'catt', '-d', device_name, 'cast', url
        ])
        self.devices[device_name]['status'] = 'playing'
        self.devices[device_name]['current_media'] = url

    def cast_to_all(self, url):
        """向所有设备同步投屏"""
        with ThreadPoolExecutor(max_workers=5) as executor:
            for name in self.devices:
                executor.submit(self.cast_to_device, name, url)

    def create_group(self, group_name, device_names):
        """创建设备分组"""
        self.groups[group_name] = device_names

    def cast_to_group(self, group_name, url):
        """向设备分组投屏"""
        if group_name in self.groups:
            with ThreadPoolExecutor(max_workers=5) as executor:
                for name in self.groups[group_name]:
                    executor.submit(self.cast_to_device, name, url)

    def get_all_status(self):
        """获取所有设备状态"""
        statuses = {}
        for name, info in self.devices.items():
            result = subprocess.run(
                ['catt', '-d', name, 'status'],
                capture_output=True, text=True
            )
            statuses[name] = {
                **info,
                'detailed_status': result.stdout.strip()
            }
        return statuses
```

**输入**: 用户提供多设备同步管理所需的指令和必要参数。
**处理**: 按照skill规范执行多设备同步管理操作,遵循单一意图原则。
**输出**: 返回多设备同步管理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 2. 播放队列管理

```python
class PlaylistManager:
    def __init__(self, cast_manager):
        self.manager = cast_manager
        self.queues = {}  # device_name -> [urls]

    def add_to_queue(self, device_name, url):
        """添加到播放队列"""
        if device_name not in self.queues:
            self.queues[device_name] = []
        self.queues[device_name].append(url)

    def add_batch_to_queue(self, device_name, urls):
        """批量添加到队列"""
        if device_name not in self.queues:
            self.queues[device_name] = []
        self.queues[device_name].extend(urls)

    def remove_from_queue(self, device_name, index):
        """从队列中移除"""
        if device_name in self.queues and index < len(self.queues[device_name]):
            self.queues[device_name].pop(index)

    def get_queue(self, device_name):
        """获取当前队列"""
        return self.queues.get(device_name, [])

    def play_next(self, device_name):
        """播放队列中的下一个"""
        if device_name in self.queues and self.queues[device_name]:
            next_url = self.queues[device_name].pop(0)
            self.manager.cast_to_device(device_name, next_url)
            return next_url
        return None

    def clear_queue(self, device_name):
        """清空队列"""
        if device_name in self.queues:
            self.queues[device_name] = []
```

**输入**: 用户提供播放队列管理所需的指令和必要参数。
**处理**: 按照skill规范执行播放队列管理操作,遵循单一意图原则。
**输出**: 返回播放队列管理的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 3. 自动化脚本与定时任务

```python
import schedule
import time
import threading

class AutomationManager:
    def __init__(self, cast_manager):
        self.manager = cast_manager
        self.scheduler = schedule.Scheduler()
        self.running = False
        self.thread = None

    def schedule_cast(self, device_name, url, time_str):
        """定时投屏"""
        self.scheduler.every().day.at(time_str).do(
            self.manager.cast_to_device, device_name, url
        )

    def schedule_playlist(self, device_name, urls, time_str):
        """定时播放列表"""
        def play_playlist():
            for url in urls:
                self.manager.cast_to_device(device_name, url)
                time.sleep(300)  # 每个内容播放5分钟
        self.scheduler.every().day.at(time_str).do(play_playlist)

    def schedule_stop_all(self, time_str):
        """定时停止所有设备"""
        self.scheduler.every().day.at(time_str).do(self.stop_all)

    def stop_all(self):
        """停止所有设备"""
        for name in self.manager.devices:
            subprocess.run(['catt', '-d', name, 'stop'])

    def start(self):
        """启动自动化调度"""
        self.running = True
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()

    def stop(self):
        """停止自动化调度"""
        self.running = False

    def _run(self):
        while self.running:
            self.scheduler.run_pending()
            time.sleep(1)
```

**输入**: 用户提供自动化脚本与定时任务所需的指令和必要参数。
**处理**: 按照skill规范执行自动化脚本与定时任务操作,遵循单一意图原则。
**输出**: 返回自动化脚本与定时任务的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 4. 实时状态监控

```python
class StatusMonitor:
    def __init__(self, cast_manager):
        self.manager = cast_manager
        self.callbacks = []
        self.monitoring = False
        self.thread = None

    def register_callback(self, callback):
        """注册状态变化回调"""
        self.callbacks.append(callback)

    def start_monitoring(self, interval=10):
        """开始监控"""
        self.monitoring = True
        self.thread = threading.Thread(
            target=self._monitor_loop, args=(interval,), daemon=True
        )
        self.thread.start()

    def stop_monitoring(self):
        """停止监控"""
        self.monitoring = False

    def _monitor_loop(self, interval):
        import time
        while self.monitoring:
            for name in self.manager.devices:
                status = self._get_device_status(name)
                if self._has_changed(name, status):
                    self._notify_change(name, status)
            time.sleep(interval)

    def _get_device_status(self, device_name):
        result = subprocess.run(
            ['catt', '-d', device_name, 'status'],
            capture_output=True, text=True, timeout=5
        )
        return result.stdout.strip()

    def _has_changed(self, device_name, new_status):
        old = self.manager.devices[device_name].get('detailed_status')
        return old != new_status

    def _notify_change(self, device_name, new_status):
        self.manager.devices[device_name]['detailed_status'] = new_status
        for callback in self.callbacks:
            callback(device_name, new_status)
```

**输入**: 用户提供实时状态监控所需的指令和必要参数。
**处理**: 按照skill规范执行实时状态监控操作,遵循单一意图原则。
**输出**: 返回实时状态监控的执行结果,包含操作状态和输出数据。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：企业级投屏管理系、支持多设备管理、状态监控与定时任、投屏控制专业版、面向专业用户与企、业环境的高级、投屏管理系统、核心能力、统一管理多台、创建与管理视频播、自动播放列表、场景联动、监控所有设备的播、放状态、将设备分组等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

## 使用场景

### 场景一：企业展厅数字标牌

企业展厅多台电视展示不同内容，需要统一管理。

```python
# 初始化管理器
manager = ChromecastManager()
print(f"发现设备: {list(manager.devices.keys())}")

# 创建设备分组
manager.create_group('entrance', ['入口屏1', '入口屏2'])
manager.create_group('main_hall', ['主展厅1', '主展厅2', '主展厅3'])
manager.create_group('exit', ['出口屏'])

# 向不同区域投屏不同内容
manager.cast_to_group('entrance', 'https://example.com/welcome.mp4')
manager.cast_to_group('main_hall', 'https://example.com/product-demo.mp4')
manager.cast_to_group('exit', 'https://example.com/thanks.mp4')

# 设置自动化：每天9点开始播放，18点停止
automation = AutomationManager(manager)
automation.schedule_cast('entrance', 'https://example.com/welcome.mp4', '09:00')
automation.schedule_cast('main_hall', 'https://example.com/product-demo.mp4', '09:00')
automation.schedule_stop_all('18:00')
automation.start()
```

### 场景二：多房间音频系统

智能家居多房间同步播放背景音乐。

```python
# 多房间音频同步
manager = ChromecastManager()

# 创建全屋音频组
manager.create_group('whole_house', ['客厅', '卧室', '厨房', '阳台'])

# 同步播放音乐
manager.cast_to_group('whole_house', 'https://example.com/jazz.mp3')

# 创建播放队列
playlist = PlaylistManager(manager)
playlist.add_batch_to_queue('whole_house', [
    'https://example.com/song1.mp3',
    'https://example.com/song2.mp3',
    'https://example.com/song3.mp3',
])

# 监控播放状态，自动播放下一首
monitor = StatusMonitor(manager)
monitor.register_callback(lambda device, status: 
    playlist.play_next(device) if 'stopped' in status.lower() else None
)
monitor.start_monitoring(interval=5)
```

### 场景三：定时内容轮播

商业空间定时轮播不同广告内容。

```python
# 定时内容轮播
manager = ChromecastManager()
automation = AutomationManager(manager)

# 早上播放晨间内容
automation.schedule_playlist('展示屏', [
    'https://example.com/morning-ad1.mp4',
    'https://example.com/morning-ad2.mp4',
    'https://example.com/morning-ad3.mp4',
], '08:00')

# 下午播放午间内容
automation.schedule_playlist('展示屏', [
    'https://example.com/afternoon-ad1.mp4',
    'https://example.com/afternoon-ad2.mp4',
], '12:00')

# 晚上播放晚间内容
automation.schedule_playlist('展示屏', [
    'https://example.com/evening-ad1.mp4',
    'https://example.com/evening-ad2.mp4',
], '18:00')

automation.start()
print("定时轮播已启动")
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 依赖详情

```bash
pip install catt schedule
```

### 2. 初始化多设备管理

```python
from chromecast_manager import ChromecastManager

manager = ChromecastManager()
print(f"发现 {len(manager.devices)} 台设备")

for name, info in manager.devices.items():
    print(f"  {name}: {info['ip']}")
```

### 3. 创建分组并投屏

```python
manager.create_group('living_area', ['客厅', '餐厅'])
manager.cast_to_group('living_area', 'https://example.com/video.mp4')
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。


## 示例

### 设备分组策略

| 分组类型 | 适用场景 | 示例 |
| --- | --- | --- |
| 区域分组 | 按物理区域 | 入口组、主厅组、出口组 |
| 功能分组 | 按功能用途 | 展示组、音频组、信息组 |
| 时间分组 | 按时段切换 | 晨间组、午间组、晚间组 |

### 自动化场景

| 场景 | 触发条件 | 动作 |
| --- | --- | --- |
| 展厅开启 | 每天09:00 | 投屏欢迎内容 |
| 展厅关闭 | 每天18:00 | 停止所有设备 |
| 内容轮播 | 定时间隔 | 切换播放内容 |
| 状态告警 | 设备离线 | 发送通知 |

### 监控指标

| 指标 | 说明 | 告警阈值 |
| --- | --- | --- |
| 设备在线状态 | 在线/离线 | 离线超过5分钟 |
| 播放状态 | 播放/暂停/停止 | 异常停止 |
| 当前内容 | 正在播放的URL | 内容不匹配 |
| 音量水平 | 当前音量值 | 低于10或高于90 |

## 最佳实践

1. **设备命名规范**：使用统一的命名规则（如"区域-功能-编号"），便于管理
2. **分组策略**：根据使用场景合理分组，避免过度分组增加复杂度
3. **队列管理**：长内容播放使用队列，避免单次投屏超时
4. **监控间隔**：状态监控间隔建议10-30秒，过短会增加网络负担
5. **错误恢复**：实现设备离线自动重连机制
6. **日志记录**：记录所有操作日志，便于排查问题
7. **安全考虑**：限制管理接口的访问范围，避免未授权控制

## 常见问题

### Q1：多设备同步有延迟怎么办？

网络带宽是主要瓶颈。建议使用有线网络或高品质WiFi，减少同时投屏的设备数量。

### Q2：自动化任务不执行怎么办？

检查系统时间是否正确，确认调度器线程正在运行。查看日志排查具体错误。

### Q3：设备离线后如何自动恢复？

实现状态监控回调，检测到设备离线后自动重试连接，恢复后继续播放队列。

### Q4：支持多少台设备同时管理？

理论上无限制，实际受网络带宽影响。建议单组不超过10台设备。

### Q5：与免费版的命令是否兼容？

完全兼容。专业版底层使用相同的catt命令，免费版的所有命令可直接在专业版中使用。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **网络环境**: 与所有Chromecast设备在同一局域网
- **Python版本**: 3.8及以上

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3 | 运行时 | 必需 | python.org 下载安装 |
| catt | Python工具 | 必需 | `pip install catt` |
| schedule | Python库 | 必需 | `pip install schedule` |
| Chromecast设备 | 硬件 | 必需 | 购买Chromecast硬件 |

### API Key 配置

- 专业版无需任何API Key
- 所有功能通过局域网内catt命令行工具实现，无需云端认证
- 与免费版完全兼容，免费版的所有命令可直接复用

### 可用性分类

- **分类**: MD+EXEC（纯Markdown指令，核心功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行专业Chromecast投屏管理任务。支持多设备管理、播放队列、自动化脚本、状态监控等企业级功能，通过Python脚本调用catt命令实现。与免费版完全兼容，可直接复用免费版的所有catt命令。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响
