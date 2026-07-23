---
slug: "stock-filter-skills"
name: "stock-filter-skills"
version: "1.3.0"
displayName: "Stock Filter Skills"
summary: "股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析。提供 17 个 CLI 工具覆盖四大模块。"
license: "Proprietary"
description: |-
  股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析。提供 17 个 CLI 工具覆盖四大模块。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。
tags:
  - Finance
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
---
# Stock Filter Skills

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Stock Filter Skills热门因子管理 | 不支持 | 支持 |
| Stock Filter Skills数据查询 | 不支持 | 支持 |
| Stock Filter Skills和抖音热点分析 | 不支持 | 支持 |
| DCF估值建模与敏感性分析 | 不支持 | 支持 |
| 财务舞弊识别(Beneish M-Score) | 不支持 | 支持 |

## 核心能力

- 股票多条件筛选、热门因子管理、Jiuyan 数据查询和抖音热点分析
- 提供 17 个 CLI 工具覆盖四大模块
#
## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 筛选股票：先 stock_filter_options 获取维度 → 再 stock_filter 执行筛选
2. 查股票：stock_search 搜索 → stock_detail 查详情
3. 批量查询：stock_detail_batch 一次获取多只股票详情
4. 对比股票：stock_compare 对比多只股票的关键指标
5. 分析股票：jiuyan_stock_analysis 获取分析 → jiuyan_stock_theme 查看主题
6. 管理预设：hot_factor_list 查看 → hot_factor_create/update/delete 操作
7. 看热点：douyin_hotspot_list 浏览 → douyin_hotspot_detail 查详情

**结果验证**: 任务完成后,查看输出确认状态。成功时返回摘要和数据;失败时根据错误信息排查,参考恢复章节获取修复步骤。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | stock-filter-skills处理的内容输入 |,  |
| content | string | 否 | stock-filter-skills处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "skills 相关配置参数",
    result: "skills 相关配置参数",
    result: "skills 相关配置参数",
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

所有工具返回 JSON。错误时格式为 `{"error": "描述"}`。常见错误：认证失败（检查 API Key）、连接失败（检查服务是否启动）、参数错误。

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ;确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 对照使用流程章节检查输入格式;参考示例章节修正输入 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述,补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 对照依赖说明章节确认环境配置;检查命令权限设置 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

### 示例1：基础用法

```
1. 筛选股票：先 stock_filter_options 获取维度 → 再 stock_filter 执行筛选
2. 查股票：stock_search 搜索 → stock_detail 查详情
3. 批量查询：stock_detail_batch 一次获取多只股票详情
4. 对比股票：stock_compare 对比多只股票的关键指标
5. 分析股票：jiuyan_stock_analysis 获取分析 → jiuyan_stock_theme 查看主题
6. 管理预设：hot_factor_list 查看 → hot_factor_create/update/delete 操作
7. 看热点：douyin_hotspot_list 浏览 → douyin_hotspot_detail 查详情
```

## 常见问题

### Q1: 如何开始使用Stock Filter Skills？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

