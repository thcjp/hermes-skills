---
slug: "token-manager-free"
name: "token-manager-free"
version: "1.0.0"
displayName: "Token用量管理(免费版)"
summary: "监控API Token使用量和费用，提供定时提醒、余额预警和跨会话分析(免费版)"
license: "MIT"
description: |-
  API Token使用量和费用监控工具。实时跟踪Token消耗和余额，支持定时提醒、
  余额预警、工具集成和跨会话分析。按¥12/1M tokens计费，80%上下文阈值
  触发提醒，50k会话Token触发预警。适用于独立开发者、企业团队和自动化
  工作流场景。不适用于无API计费的场景.
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
pricing_tier: "L2-标准级"
suggested_price: "19.9 CNY/per_use"

---
# Token用量管理(免费版)

监控API Token使用量和费用，提供定时提醒、余额预警和跨会话分析.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | Token用量管理(免费版)处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

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
### 输出格式

完成响应以Markdown格式返回,包含任务状态(成功/失败)、解析摘要和具体输出数据。失败时返回错误码和错误信息,便于定位问题。- 验证返回数据的完整性和格式正确性
- 参考`输出格式`的配置文档进行参数调优
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 使用量查看 | 无 | 当前会话+累计Token使用报告 |
| 余额预警 | 定时检查 | 余额状态+预警通知 |
| 跨会话分析 | 时间范围 | 使用趋势+费用分布 |

## 使用流程

1. 配置API密钥环境变量(如 `MOONSHOT_API_KEY`)
2. 用 `session-tracker.js record` 记录每次API调用
3. 用 `manager.js report` 查看使用报告
4. 用 `scheduler.js check --interval 300` 设置定时检查
5. 用 `manager.js report --range 7d` 查看跨会话趋势

#
## 示例

### 示例:查看使用报告

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

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| `MOONSHOT_API_KEY`未配置 | 环境变量缺失 | 通过 `export MOONSHOT_API_KEY="your_key"` 设置 |
| 余额查询返回401 | API密钥无效或过期 | 检查密钥是否正确，重新生成API密钥 |
| 余额查询返回429 | 速率限制 | 等待60秒后检查网络连接和配置后重试，降低查询频率 |
| 余额低于¥5阈值 | 账户余额不足 | 及时充值，scheduler发出预警 |

## 常见问题

### Q1: Token费用如何计算？
A: 按¥12/1M tokens计费。输入Token和输出Token分别计算。例如：输入1200 tokens + 输出800 tokens = 2000 tokens，费用 = 2000 / 1000000 * 12 = ¥0.024。缓存Token价格为¥6/1M tokens.
### Q2: 80%上下文阈值是什么意思？
A: 上下文窗口（如80,000 tokens）使用超过80%（64,000 tokens）时触发提醒。建议清理历史消息或开启新会话，避免上下文溢出导致性能下降.
### Q3: 50k会话Token预警意味着什么？
A: 单次会话消耗超过50,000 tokens时触发预警。通常意味着对话过长或存在循环调用。建议检查是否有不必要的重复请求.
## 已知限制

- 计费标准为¥12/1M tokens，不同模型价格可能不同
- 80%上下文阈值为默认值，不可自定义
- 50k会话Token预警为固定阈值

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
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
## 升级提示

本免费版提供基础功能。升级到完整版 token-manager 获取全部能力和高级特性.