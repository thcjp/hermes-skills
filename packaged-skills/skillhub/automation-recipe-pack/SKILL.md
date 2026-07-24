---
slug: "automation-recipe-pack"
name: "automation-recipe-pack"
version: 1.1.2
displayName: "自动化配方"
summary: "10个实用自动化场景配方，覆盖文件处理、数据转换、批量操作等高频任务，可自动化提升工作效率。10个实用自动化场景配方，覆盖文件处理、数据转换、批量操作等高频任务。适用于效率工具爱好者、自动化"
license: "MIT"
description: "10个实用自动化场景配方，覆盖文件处理、数据转换、批量操作等高频任务。适用于效率工具爱好者、自动化新手，可自动化提升工作效率。支持批量处理、工作流优化、定时触发等场景。"
tags:
  - Automation
  - 自动化
  - 工作流
  - 效率
  - agent
  - string
  - llm
tools:
  - read
  - exec
  - write
homepage: ""
category: "Automation"
---
# 自动化配方

10个实用自动化场景配方，覆盖文件处理、数据转换、批量操作等高频任务。

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |

## 核心能力

本技能提供10个实用自动化场景配方,覆盖文件处理、数据转换、批量操作等高频任务:

### 文件处理配方
- **批量文件重命名**: 按规则(日期/序号/正则)批量重命名目录下文件,支持预览与回滚
- **文件格式转换**: 支持CSV/JSON/Excel/TXT等格式互转,保留数据结构完整性
- **重复文件清理**: 基于文件哈希(MD5/SHA256)识别并清理重复文件,释放存储空间
- **目录结构同步**: 增量同步源目录到目标目录,支持过滤规则与删除策略

### 数据转换配方
- **数据清洗与结构化**: 去除空行/空格/特殊字符,统一日期与数字格式,输出标准化结构数据
- **多源数据合并**: 按主键合并多个CSV/Excel数据源,处理冲突字段与缺失值
- **模板数据填充**: 基于模板文件批量生成个性化文档(邮件/合同/报告),支持变量替换

### 工作流编排配方
- **定时任务编排**: 基于cron表达式定时触发数据处理流水线,支持失败重试与通知
- **条件分支流程**: 根据数据内容自动选择处理分支(IF-ELSE/SWITCH模式),实现智能路由
- **多步骤管道编排**: 将多个处理步骤串联为管道,前一步输出作为后一步输入,支持中间结果缓存

每个配方均可独立调用,也可组合编排为复杂工作流。付费版支持可视化编排界面、执行日志审计与异常重试机制。

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

## 适用场景

| 场景 | 典型输入 | 输出内容 |
|:-----|:-----|:-----|
| 文件批量处理 | 文件路径列表+重命名规则 | 处理结果摘要+变更明细 |
| 数据格式转换 | 源格式数据(CSV/JSON/Excel) | 目标格式数据文件 |
| 重复文件清理 | 目标目录路径 | 重复文件清单+释放空间统计 |
| 多源数据合并 | 多个CSV文件+合并主键 | 合并后数据文件+冲突报告 |
| 模板批量生成 | 模板文件+变量数据源 | 批量生成的个性化文档 |
| 定时数据处理 | cron表达式+处理流程 | 定时执行日志+结果通知 |
| 目录结构同步 | 源目录+目标目录+过滤规则 | 同步操作日志+差异报告 |

**不适用于**：需要人工判断的复杂决策场景、实时性要求极高的在线服务

## 使用流程

1. **定义自动化任务**: 解析用户需求,构建任务执行计划与触发条件
2. **编排执行流程**: 按依赖顺序执行各步骤,处理条件分支与异常重试
3. **监控与报告**: 记录执行日志,输出任务状态与结果摘要
4. **异常处理**: 如遇错误,参考错误处理章节中对应场景的处理方式

## 示例代码

### 1. 批量文件重命名配方（PowerShell）

按日期前缀批量重命名指定目录下的图片文件:

```powershell
# 批量重命名配方：按 YYYYMMDD_序号 格式重命名图片
$targetDir = "C:\Photos\2024"
$files = Get-ChildItem -Path $targetDir -Include *.jpg,*.png -File | Sort-Object Name
$datePrefix = Get-Date -Format "yyyyMMdd"
$counter = 1

foreach ($file in $files) {
    $newName = "${datePrefix}_{0:D3}{1}" -f $counter, $file.Extension
    $newPath = Join-Path $targetDir $newName
    Rename-Item -Path $file.FullName -NewName $newPath
    Write-Host "已重命名: $($file.Name) -> $newName"
    $counter++
}
Write-Host "完成! 共重命名 $($counter - 1) 个文件"
```

### 2. CSV数据清洗与格式转换配方（Python）

清洗CSV数据并转换为JSON格式:

```python
import csv
import json
from datetime import datetime

def clean_and_convert(input_csv, output_json):
    """数据清洗配方：去空行、统一日期格式、转JSON"""
    cleaned = []
    with open(input_csv, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            # 去除首尾空格
            row = {k.strip(): v.strip() for k, v in row.items() if k}
            # 跳过空行
            if not any(row.values()):
                continue
            # 统一日期格式为 YYYY-MM-DD
            for key, val in row.items():
                if 'date' in key.lower() and val:
                    try:
                        row[key] = datetime.strptime(val, '%m/%d/%Y').strftime('%Y-%m-%d')
                    except ValueError:
                        pass
            cleaned.append(row)

    with open(output_json, 'w', encoding='utf-8') as f:
        json.dump(cleaned, f, ensure_ascii=False, indent=2)

    print(f"清洗完成: 输入 {len(cleaned)} 条记录 -> {output_json}")

# 示例：清洗销售数据CSV并输出JSON
clean_and_convert('sales_raw.csv', 'sales_clean.json')
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | 处理的内容输入 |
| format | string | 否 | 可选值: json/text/markdown |
| style | string | 否 | 输出风格 |

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "处理结果",
    "metadata": {
      "template_used": "automation",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试 |

## 依赖说明

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Agent LLM | API | 必需 | 由Agent内置LLM提供 |
| Agent平台 | 运行时 | 必需 | 支持SKILL.md的任意AI Agent |

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI等
- **操作系统**: Windows / macOS / Linux

## 常见问题

### Q1: 如何开始使用自动化配方？
A: 在AI Agent对话中直接调用本技能,提供需要自动化处理的任务描述即可。

## 已知限制

1. 不适用于需要人工创意判断的任务
2. 复杂工作流编排需付费版支持
3. 依赖Agent平台的LLM能力执行
