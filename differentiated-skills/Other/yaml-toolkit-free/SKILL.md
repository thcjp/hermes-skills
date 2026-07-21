---
slug: yaml-toolkit-free
name: yaml-toolkit-free
version: "1.0.0"
displayName: YAML处理工具免费版
summary: 解析、生成与校验YAML，正确处理缩进与多文档，适合个人开发者配置管理。
license: Proprietary
edition: free
description: |-
  YAML处理工具免费版，面向个人开发者的轻量级YAML解析与生成工具。核心能力:
  - YAML解析与多文档处理
  - YAML生成与缩进规范
  - 锚点/别名/合并键处理
  - 格式校验与常见陷阱规避

  适用场景:
  - 配置文件解析与生成
  - CI/CD 流水线配置管理
  - 数据序列化与反序列化

  差异化: 免费版聚焦核心解析与生成能力，去除所有外部平台与作者引用，强化中文本地化与触发关键词，适合个人用户零成本上手
tags:
- YAML
- 配置管理
- 数据序列化
- 免费版
tools:
  - - read
- exec
---

# YAML处理工具（免费版）

## 概述

YAML处理工具免费版帮助你解析、生成与校验 YAML，正确处理缩进、多文档、锚点/别名等 YAML 特性。覆盖缩进、引用、类型推断、多文档、流式风格、注释、模式验证七大核心知识域。

## 核心能力

| 能力 | 说明 |
|:-----|:-----|
| 解析 | YAML 文件与字符串解析为对象 |
| 生成 | 对象序列化为规范 YAML |
| 多文档 | `---` 分隔的多文档处理 |
| 锚点/别名 | `&anchor` / `*alias` / `<<: *merge` |
| 类型推断 | 自动识别字符串、数字、布尔、日期、null |
| 格式校验 | 缩进、引号、特殊字符校验 |
| 常见陷阱 | Tab 字符、未引用特殊值、隐式类型转换 |

## 使用场景

### 场景一：解析配置文件

解析 YAML 配置文件为对象。

```python
import yaml

# 解析文件
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 访问配置
print(config['server']['host'])
print(config['server']['port'])
```

### 场景二：生成规范YAML

将对象序列化为规范 YAML。

```python
import yaml

config = {
    'server': {
        'host': 'localhost',
        'port': 8080,
        'timeout': 30
    },
    'database': {
        'url': 'localhost:5432',
        'pool_size': 10
    }
}

# 生成 YAML（不强制排序）
with open('config.yaml', 'w', encoding='utf-8') as f:
    yaml.dump(config, f, default_flow_style=False, allow_unicode=True)

# 输出:
# server:
#   host: localhost
#   port: 8080
#   timeout: 30
# database:
#   url: localhost:5432
#   pool_size: 10
```

### 场景三：处理多文档YAML

处理 `---` 分隔的多文档文件。

```python
import yaml

# 解析多文档
with open('multi-doc.yaml', 'r', encoding='utf-8') as f:
    docs = list(yaml.safe_load_all(f))

for i, doc in enumerate(docs):
    print(f"文档 {i+1}: {doc}")
```

## 快速开始

```python
import yaml

# 1. 解析文件
with open('config.yaml', 'r', encoding='utf-8') as f:
    config = yaml.safe_load(f)

# 2. 解析字符串
config = yaml.safe_load("""
server:
  host: localhost
  port: 8080
""")

# 3. 生成 YAML
yaml_str = yaml.dump(config, default_flow_style=False, allow_unicode=True)

# 4. 多文档解析
docs = list(yaml.safe_load_all(open('multi.yaml', encoding='utf-8')))

# 5. 多文档生成
yaml.dump_all([doc1, doc2], open('output.yaml', 'w', encoding='utf-8'))
```

## 示例

```text
# YAML 规范要点

## 缩进
- 只能用空格，不能用 Tab
- 同一层级缩进必须一致
- 建议每层缩进 2 个空格

## 类型推断
- yes/no/true/false/on/off → 布尔
- null/Null/~ → null
- 数字 → 整数或浮点
- 日期格式 → 日期对象

## 需要引号的特殊值
- 含特殊字符: : # @ ` ! % & * | > ? 
- 以特殊字符开头: - ? : 
- 数字字符串: "123" 避免被解析为数字
- 布尔字符串: "yes" 避免被解析为 true

## 锚点与别名
- &anchor 定义锚点
- *alias 引用锚点
- <<: *anchor 合并键

## 多文档
- --- 分隔文档
- ... 结束文档（可选）
```

## 最佳实践

* 使用 `safe_load` 而非 `load`，避免任意对象实例化的安全风险。
* 缩进统一使用 2 空格，禁止 Tab。
* 含特殊字符的值使用引号（建议双引号）。
* 数字字符串、布尔字符串明确加引号，避免隐式转换。
* 生成时启用 `allow_unicode`，确保中文正确输出。
* 多文档使用 `safe_load_all` 与 `dump_all`。
* 锚点/别名用于减少重复，但不要过度使用降低可读性。
* 配置文件顶部建议添加注释说明用途。

## 常见问题

**Q：免费版支持 YAML 模式验证吗？**
A：免费版提供基础格式校验。如需 JSON Schema 验证，请考虑 PRO 版本。

**Q：免费版支持 YAML 与 JSON 互转吗？**
A：免费版不提供格式互转。如需 YAML/JSON/TOML 互转，请使用 PRO 版本。

**Q：解析失败怎么排查？**
A：常见原因：Tab 缩进、未引号的特殊值、缩进不一致。建议用 `yaml.safe_load` 解析，错误信息会指出行号。

**Q：支持 YAML 1.1 还是 1.2？**
A：免费版基于 PyYAML，兼容 YAML 1.1。如需 1.2 严格模式，请使用 PRO 版本。

**Q：如何避免 yes 被解析为 True？**
A：使用引号：`"yes"` 或 `'yes'`。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.9+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 官方站点下载 |
| PyYAML | 库 | 必需 | pip 安装 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key（除内容中明确标注的外部API）

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + Python脚本执行）
- **说明**: 基于Markdown的AI Skill，通过 PyYAML 处理 YAML

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制

- 本地运行，不支持多设备同步
