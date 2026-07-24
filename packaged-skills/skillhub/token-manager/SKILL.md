---

slug: "token-manager"
name: "token-manager"
version: 1.2.1
displayName: "Token用量管理"
summary: "监控API Token使用量和费用，提供定时提醒、余额预警和跨会话分析。API Token使用量和费用监控工具。实时跟踪Token消耗和余额，支持定时提醒、 余额预警、工具集成和跨会话分析。"
license: "Proprietary"
description: |-，可自动提升工作效率
  API Token使用量和费用监控工具。实时跟踪Token消耗和余额，支持定时提醒、
  余额预警、工具集成和跨会话分析。按¥12/1M tokens计费，80%上下文阈值
  触发提醒，50k会话Token触发预警。适用于独立开发者、企业团队和自动化
  工作流场景。不适用于无API计费的场景.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - 研究
  - 分析
  - AI代理
category: "Automation"

---

# Token用量管理

监控API Token使用量和费用，提供定时提醒、余额预警和跨会话分析.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Token用量管理处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| Token用量管理余额预警和跨会话分析 | 不支持 | 支持 |
| 大数据集流式处理 | 不支持 | 支持 |
| 多数据源关联查询 | 不支持 | 支持 |
| 可视化图表自动生成 | 不支持 | 支持 |
| 定时数据同步与增量更新 | 不支持 | 支持 |

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

### 1. 使用量监控
通过 `manager.js report` 实时查看当前会话和累计的Token使用量、费用和余额.
```bash
node （请参考skill目录中的脚本文件） report
```

**处理**: 解析使用量监控的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回使用量监控的处理结果,包含执行状态码、结果数据和执行日志.
### 2. 定时提醒
通过 `scheduler.js check` 定时检查Token使用情况，在达到阈值时触发提醒.
- 80%上下文阈值：上下文窗口使用超过80%时提醒
- 50k会话Token：单次会话消耗超过50k tokens时提醒
- ¥5余额阈值：余额低于¥5时预警

```bash
node （请参考skill目录中的脚本文件） check --interval 300
```

**输出**: 返回定时提醒的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 工具集成
通过 `session-tracker.js record` 记录每次API调用的Token消耗，自动分类和统计.
```bash
node （请参考skill目录中的脚本文件） record --input 1200 --output 800 --model "moonshot-v1-8k"
```- 验证返回数据的完整性和格式正确性
- 参考`工具集成`的配置文档进行参数调优
### 4. 跨会话分析
汇总多个会话的Token使用数据，分析使用趋势和费用分布.
```bash
node （请参考skill目录中的脚本文件） report --range 7d --format table
```

**输入**: 用户提供跨会话分析所需的指令和必要参数.
**输出**: 返回跨会话分析的处理结果,包含执行状态码、结果数据和执行日志.
### 5. 余额查询
通过API实时查询账户余额，按¥12/1M tokens计费.
```bash
curl -s https://api.moonshot.cn/v1/users/me/balance \
  -H "Authorization: Bearer ${MOONSHOT_API_KEY}"
```

**处理**: 解析余额查询的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回余额查询的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 费用估算
根据Token使用量和模型单价估算费用：
- 输入Token：¥12/1M tokens
- 输出Token：¥12/1M tokens
- 缓存Token：¥6/1M tokens

- 参考`费用估算`的配置文档进行参数调优

**处理**: 解析费用估算的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 7. 提供商管理
支持多API提供商配置，通过环境变量切换：
- `MOONSHOT_API_KEY`：月之暗面API密钥
- `OPENAI_API_KEY`：OpenAI API密钥
- `ANTHROPIC_API_KEY`：Anthropic API密钥

**处理**: 解析提供商管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回提供商管理的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`token-manager`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 真实示例

### 示例1：查看使用报告

```bash
node （请参考skill目录中的脚本文件） report
```

输出：
```
=== Token使用报告 ===
当前会话:
  输入Token:  12,450
  输出Token:  3,820
  总Token:    16,270
  预估费用:   ¥0.195
# ...
累计（本月）:
  总Token:    1,245,000
  预估费用:   ¥14.94
  剩余余额:   ¥85.06
# ...
上下文使用: 62% (49,600/80,000)
状态: 正常
```

### 示例2：记录API调用

```bash
node （请参考skill目录中的脚本文件） record \
  --input 1200 \
  --output 800 \
  --model "moonshot-v1-8k" \
  --provider "moonshot"
```

输出：
```json
{
  "recorded": true,
  "session_id": "sess-abc123",
  "input_tokens": 1200,
  "output_tokens": 800,
  "total_tokens": 2000,
  "cost_cny": 0.024,
  "model": "moonshot-v1-8k",
  "provider": "moonshot",
  "timestamp": "2026-07-21T10:30:00Z"
}
```

### 示例3：余额预警

```bash
node （请参考skill目录中的脚本文件） check --interval 300
```

输出：
```
[2026-07-21 10:35:00] 检查Token使用情况...
  余额: ¥4.82
  警告: 余额低于¥5阈值！请及时充值.
  上下文: 78% (62,400/80,000)
  会话Token: 38,200 / 50,000
```

### 示例4：7天使用趋势

```bash
node （请参考skill目录中的脚本文件） report --range 7d --format table
```

输出：
```
=== 7天Token使用趋势 ===
日期         输入Token  输出Token  总Token    费用(¥)
2026-07-15   45,200     12,300     57,500     0.69
2026-07-16   52,800     15,200     68,000     0.82
2026-07-17   38,100     10,500     48,600     0.58
2026-07-18   61,300     18,700     80,000     0.96
2026-07-19   72,500     22,100     94,600     1.14
2026-07-20   55,200     16,800     72,000     0.86
2026-07-21   48,900     14,200     63,100     0.76
────────────────────────────────────────────────────
合计         374,000    109,800    483,800    5.81
日均         53,429     15,686     69,114     0.83
```

### 示例5：查询余额

```bash
curl -s https://api.moonshot.cn/v1/users/me/balance \
  -H "Authorization: Bearer ${MOONSHOT_API_KEY}" | jq .
```

输出：
```json
{
  "code": 0,
  "data": {
    "available_balance": 85.06,
    "balance": 100.00,
    "used": 14.94
  }
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| `MOONSHOT_API_KEY`未配置 | 环境变量缺失 | 通过 `export MOONSHOT_API_KEY="your_key"` 设置 |
| 余额查询返回401 | API密钥无效或过期 | 检查密钥是否正确，重新生成API密钥 |
| 余额查询返回429 | 速率限制 | 等待60秒后降低查询频率 |
| 余额低于¥5阈值 | 账户余额不足 | 及时充值，scheduler发出预警 |
| 上下文使用超过80% | 上下文窗口即将满 | 清理历史消息，开启新会话 |
| 会话Token超过50k | 单次会话消耗过大 | 检查是否有循环调用，优化提示词 |
| 定时任务未执行 | cron配置错误 | 检查 `scheduler.js` 的interval参数，确认为300秒 |

## 常见问题

### Q1: Token费用如何计算？
A: 按¥12/1M tokens计费。输入Token和输出Token分别计算。例如：输入1200 tokens + 输出800 tokens = 2000 tokens，费用 = 2000 / 1000000 * 12 = ¥0.024。缓存Token价格为¥6/1M tokens.
### Q2: 80%上下文阈值是什么意思？
A: 上下文窗口（如80,000 tokens）使用超过80%（64,000 tokens）时触发提醒。建议清理历史消息或开启新会话，避免上下文溢出导致性能下降.
### Q3: 50k会话Token预警意味着什么？
A: 单次会话消耗超过50,000 tokens时触发预警。通常意味着对话过长或存在循环调用。建议检查是否有不必要的重复请求.
### Q4: 如何配置多个API提供商？
A: 通过环境变量配置：`MOONSHOT_API_KEY`、`OPENAI_API_KEY`、`ANTHROPIC_API_KEY`。`session-tracker.js` 的 `--provider` 参数指定当前使用的提供商.
### Q5: 定时检查间隔应该是多少？
A: 建议300秒（5分钟）。通过 `scheduler.js check --interval 300` 设置。过短间隔会增加API调用消耗，过长间隔可能错过预警时机.
### Q6: 余额预警后怎么办？
A: 余额低于¥5时系统发出预警。建议立即充值。余额耗尽后API调用将返回402 Payment Required错误，所有依赖API的功能将中断.
### Q7: 跨会话分析支持哪些时间范围？
A: 支持 `--range` 参数：`1d`（1天）、`7d`（7天）、`30d`（30天）、`90d`（90天）。输出格式可选 `table`（表格）或 `json`（JSON）.
## 已知限制

- 计费标准为¥12/1M tokens，不同模型价格可能不同
- 80%上下文阈值为默认值，不可自定义
- 50k会话Token预警为固定阈值
- ¥5余额预警为固定阈值
- 余额查询依赖API可用性，网络不可达时无法获取实时余额
- 定时任务间隔建议300秒，过短会增加Token消耗
- 跨会话分析需要历史数据积累，首次使用时数据有限
