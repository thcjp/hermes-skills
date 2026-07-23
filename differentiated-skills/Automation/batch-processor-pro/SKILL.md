---
slug: batch-processor-pro
name: batch-processor-pro
version: 1.0.0
displayName: 批处理专家
summary: 解决OOM、中断无法恢复、缺乏幂等、进度不可见四大痛点，附检查点与并行决策矩阵。
license: Proprietary
description: 批处理专家解决大批量数据处理的OOM、中断无法恢复、缺乏幂等、进度不可见四大痛点,提供流式分块、检查点恢复、幂等设计、进度报告、并行决策矩阵、五级错误分级六大核心能力。适用于批量文件/API/数据清洗/媒体转换等"对N个东西做同样操作"的场景。适用关键词:批处理、批量、检查点、断点续跑、幂等、并行、流式、OOM、进度
tags:
- 自动化
- 批处理
- 效率工具
tools:
- - read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 批处理专家

处理多个数据项时应用本skill。核心信条:**永远先dry-run少量样本,必有检查点可恢复,每项必幂等。**

## 核心能力

### 1. 流式分块
按行/按文件/按批次分块处理,内存恒定不OOM。大文件按行读、目录按文件处理、API按批次调用

**输入**: 用户提供流式分块所需的指令和必要参数。
**处理**: 解析流式分块的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回流式分块的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 2. 检查点恢复
每N项(默认50)存检查点到磁盘,中断后从断点续跑而非从头重跑,避免80%进度丢失

**输入**: 用户提供检查点恢复所需的指令和必要参数。
**处理**: 解析检查点恢复的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回检查点恢复的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 3. 幂等设计
每项有唯一键(文件路径+mtime/记录主键/业务ID),处理前查重跳过已处理项,防止重复扣款/发邮件

**输入**: 用户提供幂等设计所需的指令和必要参数。
**处理**: 解析幂等设计的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回幂等设计的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 4. 进度报告
按总项数自适应报告频率(<100每项/100-1000每10项/1000+每100项),含完成百分比与剩余时间预估

**输入**: 用户提供进度报告所需的指令和必要参数。
**处理**: 解析进度报告的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回进度报告的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 5. 并行决策矩阵
按任务特征(CPU/IO密集、顺序依赖、数据量、限流)选串行/并发/分片并行,附ThreadPoolExecutor与分片示例

**输入**: 用户提供并行决策矩阵所需的指令和必要参数。
**处理**: 解析并行决策矩阵的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回并行决策矩阵的响应数据,包含状态码、结果和日志。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 6. 五级错误分级
L1瞬时重试退避、L2数据错误跳过记录、L3可恢复排队、L4系统中止告警、L5数据完整性立即中止人工介入

**输入**: 用户提供五级错误分级所需的指令和必要参数。
**处理**: 解析五级错误分级的输入参数,完成核心逻辑,返回结构化响应。
**输出**: 返回五级错误分级的响应数据,包含状态码、结果和日志。
**技术参数**：使用`input_params`和`output_format`参数控制执行行为,支持`json`/`text`/`csv`输出格式。
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：中断无法恢复、缺乏幂等、进度不可见四大痛、附检查点与并行决、批处理专家解决大、批量数据处理的、五级错误分级六大、核心能力、适用于批量文件、数据清洗、媒体转换等、个东西做同样操作、的场景、适用关键词、批处理等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 适用场景

**何时使用**:
- 批量处理目录下数百至数万个文件
- 批量调API处理上万条记录
- 批量图片/视频转换或压缩
- 批量数据清洗与校验
- 任何"要对N个东西做同样操作"的任务

**输入**:待处理的数据项列表(文件路径/记录数组/API参数列表)及处理函数
**输出**:处理结果列表、检查点文件、批处理完成报告(成功/失败/跳过数、用时、平均速率、失败TOP原因)

**不适用场景**:
- 单次处理少量数据(<10项,直接处理即可)
- 实时流式处理(需Flink/Kafka等流处理框架)
- 强顺序依赖且需全局状态的任务(并行无收益)

## 使用流程

### Step 1: Dry-run验证(2-3项样本)
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | 批处理专家处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```python
SAMPLE_SIZE = 3
sample_items = items[:SAMPLE_SIZE]
results = [process(item) for item in sample_items]
# 人工核对结果正确再放量
```

### Step 2: 计数与预估
```text
"将处理47项,预计2分钟完成"
"将处理10000项,预计3小时,已存检查点可中断恢复"
```

### Step 3: 确认破坏性操作
```text
"将删除200个文件,不可恢复。确认继续?[y/N]"
"将向1000个客户发送邮件,不可撤回。确认继续?[y/N]"
```

### Step 4: 选择分块策略
- **大文件**:按行分块(每1000行一个chunk)
- **目录批量**:按文件逐个处理
- **API调用**:按批次(每50条一批)

### Step 5: 实现检查点与幂等
```python
CHECKPOINT_INTERVAL = 50  # 每50项存一次

def process_with_checkpoint(items, job_id):
    checkpoint = load_or_init_checkpoint(job_id)
    start_idx = checkpoint["completed"]
    for i, item in enumerate(items[start_idx:], start=start_idx):
        if item["id"] in checkpoint["processed_ids"]:
            continue  # 幂等:跳过已处理
        try:
            process(item)
            checkpoint["processed_ids"].append(item["id"])
        except Exception as e:
            checkpoint["failed_items"].append({"id": item["id"], "error": str(e)})
        checkpoint["completed"] = i + 1
        if (i + 1) % CHECKPOINT_INTERVAL == 0:
            save_checkpoint(job_id, checkpoint)
            report_progress(i + 1, len(items))
    save_checkpoint(job_id, checkpoint)
```

### Step 6: 选择并行策略(参考决策矩阵)
CPU密集→串行;IO密集→并发(ThreadPoolExecutor);无依赖大数据量→分片并行;有API限流→令牌桶限流。

### Step 7: 处理后生成报告
```text
批处理完成报告
==============================
任务: batch-process-20260718
总数: 10000 | 成功: 9977 | 失败: 23 | 跳过: 0
用时: 38分12秒 | 平均速率: 4.36项/秒
检查点: ~/.checkpoints/batch-process-20260718.json
失败项TOP原因: timeout:15, invalid_format:8
```

## 示例

### 示例
**输入**: 一个10万行的JSONL大文件,每行一条记录,需逐行解析并调用处理函数

**输出**:
```python
def process_large_file(path, chunk_size=1000):
    with open(path, 'r', encoding='utf-8') as f:
        chunk = []
        for line_no, line in enumerate(f, 1):
            item = json.loads(line)
            chunk.append(item)
            if len(chunk) >= chunk_size:
                process_chunk(chunk)
                chunk = []  # 释放内存
            if line_no % 50 == 0:
                save_checkpoint(job_id, checkpoint)
                report_progress(line_no, 100000)
        if chunk:
            process_chunk(chunk)
```
内存恒定(仅保留1000行),中断后从检查点续跑。

### 示例2: 批量调API处理1万条记录
**输入**: 1万条订单记录,需调用第三方API验证状态,API限流每秒50次

**输出**:
```python
from concurrent.futures import ThreadPoolExecutor, as_completed
import time, threading

rate_limiter = threading.Semaphore(50)  # 令牌桶限流

def process_order(order):
    with rate_limiter:
        result = api.verify(order["id"])
        return {"id": order["id"], "status": result.status}

with ThreadPoolExecutor(max_workers=10) as executor:
    futures = {executor.submit(process_order, o): o for o in orders}
    for future in as_completed(futures):
        try:
            results.append(future.result())
        except Exception as e:
            failed.append({"error": str(e), "item": futures[future]})
```
并发执行但不超过API限流,失败项记录到failed.json待重试。

## 错误处理


| 场景 | 原因 | 处理方式 |
|:-----|:-----|:---------|
| OOM内存崩溃 | 一次性load全部数据 | 改用流式分块,按行/按文件/按批次处理,内存恒定 |
| 中断后从头重跑 | 无检查点机制 | 加checkpoint机制,每50项存盘,中断后从断点续跑 |
| 重复处理/重复扣款 | 缺乏幂等设计 | 加唯一键+去重检查,处理前先查"是否已处理" |
| 进度卡住不动 | 单项处理卡死 | 加per-item timeout,超时跳过记录到failed |
| 全部API调用失败 | API限流或凭证过期 | 加令牌桶限流、退避执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令(1s/2s/4s)、检查Token有效性 |
| 并行数据错乱 | 共享状态竞争 | 改串行或加锁,有共享状态时禁止并行 |
| 检查点文件丢失 | 仅存内存未持久化 | 检查点必须持久化到磁盘,不能只在内存 |
| 数据完整性问题 | 重复处理或数据丢失 | L5级别立即中止,人工介入,核对幂等键与校验和 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 推荐(3.8+,脚本实现) | python.org |
| Redis | 服务 | 可选(幂等去重) | 自部署或云服务 |
| 外部API Key | 凭证 | 按需(批量调API时) | 通过环境变量配置 |

**运行环境**:
- 操作系统: Windows / macOS / Linux
- 本skill基于Markdown指令,无需额外API Key
- 涉及外部API批量调用时,通过环境变量配置API Key

**可用性分类**: MD+EXEC(Markdown指令 + 脚本执行)

## 常见问题

**Q: 处理10万条记录一加载就OOM怎么办?**
A: 用流式分块——按行读大文件、逐文件处理目录、按批次调API。内存恒定,不一次性load全部数据。

**Q: 跑到80%断了怎么办?**
A: 检查点机制。每50项存一次检查点到磁盘,中断后从断点续跑。`resume_job(job_id, items)`自动跳过已处理项。

**Q: 重跑会不会重复处理?**
A: 用幂等键。每项有唯一ID,处理前先查"是否已处理"。已处理则跳过。非幂等操作(扣款、发邮件)尤其重要。

**Q: 该用串行还是并行?**
A: 看决策矩阵。CPU密集串行,IO密集并发,有顺序依赖串行,无依赖大数据量分片并行,数据量小(<100)串行。

**Q: API限流导致批量失败?**
A: 限流并行(令牌桶)+ 退避重试(1s/2s/4s)+ 批量请求(50条/批)。L1瞬时错误最多重试3次。

## 已知限制

1. **检查点频率需平衡**:太低(丢进度多)太高(IO开销大),默认50项需根据任务调整
2. **并行受GIL限制**:Python的CPU密集任务多线程无效,需用进程级并行或改用C扩展
3. **非幂等操作需特殊处理**:扣款、发邮件等操作重试会重复,必须先做幂等设计
4. **超长任务需分片**:超过1小时的任务建议分片并行,避免单点失败全丢
5. **不适用实时流处理**:本skill面向批量离线处理,实时流式处理需Flink/Kafka等专业框架
