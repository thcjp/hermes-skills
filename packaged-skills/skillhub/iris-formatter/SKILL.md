---
slug: "iris-formatter"
name: "iris-formatter"
version: 1.0.1
displayName: "IRIS代码格式化专业版"
summary: "企业级 IRIS ObjectScript 代码审查方案，含批量处理、自定义规则与报告导出。。面向企业级 IRIS 开发团队的 ObjectScript 代码审查与治理工具。核心能力: -"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业级 IRIS 开发团队的 ObjectScript 代码审查与治理工具。核心能力:
  - 批量代码审查与格式化（多文件/多类）
  - 自定义规范规则与团队级配置
  - 结构化审查报告导出（Markdown/HTML）
  - SQL 格式规范与性能检查
  - 陷阱（Trap）深度分析与安全审计
  - 代码复杂度与重复度分析

  适用场景:
  - 企业级 IRIS 项目的代码质量管控
  - 团队协作中的代码审查标准化
  - 遗留系统的代码重构与规范化
  - 上线前的安全审计与合规检查

  差异化: 专业版兼容免费版所有规...
tags:
  - 开发工具
  - IRIS
  - ObjectScript
  - 企业协作
  - 代码质量
  - 工具
  - 效率
  - 自动化
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
# 定价元数据
category: "Automation"
---
# IRIS代码格式化专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| IRIS代码格式化专业版含批量处理 | 不支持 | 支持 |
| IRIS代码格式化专业版自定义规则与报告导出 | 不支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
|:-----|:-----|:-----|
| 代码审查 | 单文件审查 | 批量多文件/多类审查 |
| 规范规则 | 内置固定规则 | 自定义规则 + 团队配置 |
| 报告输出 | 文本报告 | Markdown/HTML 结构化报告 |
| SQL 检查 | 基础格式 | SQL 格式 + 性能检查 |
| 陷阱分析 | 基础陷阱检查 | 深度安全审计 |
| 代码度量 | - | 复杂度 + 重复度分析 |
| 格式化 | 单文件格式化 | 批量格式化 + 自动修正 |
### 能力模块

针对能力模块,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项.
**输出**: 返回能力模块的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力模块`的配置文档进行参数调优
### 代码审查

针对代码审查,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供代码审查相关的配置参数、输入数据和处理选项.
**输出**: 返回代码审查的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`代码审查`的配置文档进行参数调优
### 规范规则

针对规范规则,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供规范规则相关的配置参数、输入数据和处理选项.
**输出**: 返回规范规则的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`规范规则`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景
- 不适用: 需要人工判断的复杂决策场景

### 场景一：批量代码审查
团队需要对整个模块的代码进行批量审查.
```bash
#!/bin/bash
# （请参考skill目录中的脚本文件） - 批量审查 IRIS 代码
MODULE_DIR=$1
REPORT_FILE="iris-review-report-$(date +%Y%m%d).md"
# ...
echo "# IRIS 代码审查报告" > "$REPORT_FILE"
echo "**审查时间**: $(date)" >> "$REPORT_FILE"
echo "**审查范围**: $MODULE_DIR" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
# ...
# 统计文件数
FILE_COUNT=$(find "$MODULE_DIR" -name "*.cls" -o -name "*.mac" -o -name "*.inc" | wc -l)
echo "**文件数量**: $FILE_COUNT" >> "$REPORT_FILE"
echo "" >> "$REPORT_FILE"
# ...
echo "=== 开始批量审查 $FILE_COUNT 个文件 ==="
# ...
# 批量审查
TOTAL_ISSUES=0
CRITICAL_COUNT=0
WARNING_COUNT=0
# ...
find "$MODULE_DIR" -name "*.cls" -o -name "*.mac" | while read file; do
  echo "审查: $file"
# ...
  # 检查命名规范
  ISSUES=$(grep -n "yonghu\|dingdan\|zhifu" "$file" | wc -l)
  if [ "$ISSUES" -gt 0 ]; then
    echo "- [严重] $file: 发现拼音命名" >> "$REPORT_FILE"
  fi
# ...
  # 检查锁规范
  LOCK_ISSUES=$(grep -n "l +\^" "$file" | grep -v ":3\|:5\|:10" | wc -l)
  if [ "$LOCK_ISSUES" -gt 0 ]; then
    echo "- [警告] $file: 锁未设置超时" >> "$REPORT_FILE"
  fi
# ...
  # 检查事务规范
  TS_COUNT=$(grep -c "ts\b" "$file")
  TC_COUNT=$(grep -c "tc\b" "$file")
  TRO_COUNT=$(grep -c "tro\b" "$file")
  if [ "$TS_COUNT" -ne "$((TC_COUNT + TRO_COUNT))" ]; then
    echo "- [严重] $file: 事务不闭合 (ts:$TS_COUNT tc:$TC_COUNT tro:$TRO_COUNT)" >> "$REPORT_FILE"
  fi
# ...
  # 检查后置表达式格式
  POSTFIX_ISSUES=$(grep -n ") && (\|) || (" "$file" | wc -l)
  if [ "$POSTFIX_ISSUES" -gt 0 ]; then
    echo "- [严重] $file: 后置表达式格式错误（括号与&&间有空格）" >> "$REPORT_FILE"
  fi
done
# ...
echo "" >> "$REPORT_FILE"
echo "## 审查完成" >> "$REPORT_FILE"
echo "详细报告: $REPORT_FILE"
```

### 场景二：自定义规范规则配置
团队需要根据项目特点自定义规范规则.
```yaml
# .iris-rules.yml - 自定义规范规则配置
rules:
  # 命名规范
  naming:
    variable_case: lowerCamelCase
    method_case: UpperCamelCase
    constant_case: UPPER_SNAKE
    max_variable_length: 31
    max_method_length: 30
    forbidden_prefixes: ["is", "arr", "str"]
    required_boolean_suffix: "Flag"
# ...
  # 锁规范
  lock:
    require_timeout: true
    default_timeout: 3
    require_paired: true
    forbid_table_global_lock: true
    require_subscript: true
# ...
  # 事务规范
  transaction:
    require_closure: true
    forbid_cross_method: true
    require_blank_line: true
    max_distance: 20  # ts/tc/tro 之间最大行数
  # 格式规范
  format:
    indent: "tab"
    space_around_operator: true
    command_case: "lower"
    use_abbreviation: true
    full_spell_commands: ["for", "while", "if", "elseif", "else", "continue"]
    max_line_length: 120
    max_method_lines: 50
# ...
  # SQL 规范
  sql:
    fields_per_line: 5
    indent_after_newline: 3
    comma_at_end: true
    command_case: "lower"
# ...
  # 陷阱规范
  trap:
    require_error_handler: true
    default_trap_name: "Error"
    require_zt_reset: true
    require_tl_check: true
    require_lock_release: true
# ...
# 严重程度映射
severity:
  naming_pinyin: critical
  naming_case: warning
  lock_no_timeout: critical
  lock_unpaired: critical
  transaction_unclosed: critical
  format_spacing: minor
  format_abbreviation: warning
  postfix_format: critical
```

### 场景三：代码复杂度分析
团队需要分析代码的复杂度和重复度，识别需要重构的代码.
```bash
#!/bin/bash
# （请参考skill目录中的脚本文件） - 代码复杂度分析
TARGET=$1
# ...
echo "=== IRIS 代码复杂度分析 ==="
echo "目标: $TARGET"
echo ""
# ...
# 方法行数统计
echo "## 方法行数统计（超过 50 行需重构）"
echo "| 文件 | 方法 | 行数 | 状态 |"
echo "| --- | --- | --- | --- |"
# ...
find "$TARGET" -name "*.cls" | while read file; do
  # 提取方法及其行数
  awk '
    /ClassMethod|Method/ {
      method_name = $0
      method_start = NR
    }
    /^}/ {
      if (method_name != "") {
        lines = NR - method_start
        if (lines > 50) {
          status = "需重构"
        } else if (lines > 30) {
          status = "建议优化"
        } else {
          status = "正常"
        }
        if (lines > 30) {
          printf "| %s | %s | %d | %s |\n", FILENAME, method_name, lines, status
        }
        method_name = ""
      }
    }
  ' "$file"
done
# ...
echo ""
echo "## 重复代码检测"
# 查找重复的代码块（5 行以上相同）
find "$TARGET" -name "*.cls" -exec cat {} \; | \
  awk 'BEGIN{block=""} {
    block = block $0 "\n"
    if (NF == 0) {
      if (length(block) > 100) {
        print block
      }
      block = ""
    }
  }' | sort | uniq -d | head -10
```

## 使用流程

### HTML 报告模板
```html
<!-- 生成结构化 HTML 审查报告 -->
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>IRIS 代码审查报告</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        .critical { color: #d32f2f; font-weight: bold; }
        .warning { color: #f57c00; }
        .minor { color: #1976d2; }
        .suggestion { color: #388e3c; }
        table { border-collapse: collapse; width: 100%; }
        th, td { border: 1px solid #ddd; padding: 8px; text-align: left; }
        th { background-color: #f5f5f5; }
    </style>
</head>
<body>
    <h1>IRIS 代码审查报告</h1>
    <table>
        <tr>
            <th>审查时间</th>
            <td>"formatter_result"</td>
        </tr>
        <tr>
            <th>审查范围</th>
            <td>全维度</td>
        </tr>
        <tr>
            <th>文件数量</th>
            <td>"formatter_metadata"</td>
        </tr>
        <tr>
            <th>问题总数</th>
            <td>"formatter_status"</td>
        </tr>
    </table>
# ...
    <h2>问题详情</h2>
    <table>
        <tr>
            <th>序号</th>
            <th>严重程度</th>
            <th>文件</th>
            <th>行号</th>
            <th>问题描述</th>
            <th>规范依据</th>
        </tr>
        相关信息
        <tr>
            <td>"formatter_summary"</td>
            <td class=""formatter_details"">"formatter_details"</td>
            <td>"formatter_count"</td>
            <td>"formatter_timestamp"</td>
            <td>formatter 相关配置参数</td>
            <td>"formatter_version"</td>
        </tr>
        相关信息
    </table>
</body>
</html>
```

### SQL 格式规范检查
```objectscript
// SQL 格式规范
// 1. 每行 5 个字段
// 2. 换行后 3 个 Tab 缩进
// 3. 逗号在行末
// 4. 每行不超过 120 字符
// 5. SQL 命令统一小写
# ...
// 正确格式
&sql(
   select id, name, age, email, phone
         into :id, :name, :age, :email, :phone
         from user_table
         where id = :userId
)
# ...
// 错误格式
&sql(SELECT ID,NAME,AGE,EMAIL,PHONE,ADDRESS,STATUS FROM USER_TABLE WHERE ID=:userId)
// 问题：字段过多、命令大写、单行过长
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | iris-formatter处理的内容输入 |, 默认: 全部维度 |
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

- 边界输入处理: 空输入返回提示信息, 超长输入自动截断
- 降级策略: 异常时返回默认值, 确保流程不中断

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **IRIS/Cache 版本**: 建议 2018 及以上
- **CI/CD 平台**: GitLab CI / GitHub Actions / Jenkins 等

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| InterSystems IRIS | 运行时 | 推荐 | InterSystems 官方获取 |
| Git | 命令行工具 | 推荐 | 系统包管理器安装 |
| YAML 解析器 | 工具 | 可选 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- IRIS 服务器连接需要配置访问凭据
- CI/CD 集成需要在平台配置对应的访问令牌

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行批量代码审查与格式化，专业版功能依赖命令行脚本和 CI/CD 平台

## 案例展示

### 审查规则配置文件
```yaml
# team-iris-standards.yml
version: "2.0"
team: "后端开发组"
updated: "2026-07-18"
# ...
# 继承基础规则
extends: "default"
# ...
# 团队自定义覆盖
overrides:
  naming:
    # 团队特有前缀要求
    service_prefix: "Svc"
    controller_prefix: "Ctrl"
    dao_prefix: "DAO"
# ...
  format:
    # 团队约定的方法最大行数
    max_method_lines: 40  # 比默认 50 更严格
  sql:
    # 禁止在循环内写 SQL
    forbid_sql_in_loop: true
    # 必须使用参数化查询
    require_parameterized: true
# ...
# 排除规则
excludes:
  - "**/test/**"
  - "**/legacy/**"
  - "**/*.inc"  # include 文件单独审查
# 报告配置
report:
  format: ["markdown", "html"]
  output_dir: "reports/"
  include_source: true
  max_suggestions: 5
```

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 常见问题

### Q1：如何处理遗留代码的大量违规？
```text
策略：
1. 先生成完整审查报告，评估违规规模
2. 按严重程度排序，优先修复 critical 级别
3. 使用批量格式化处理格式类问题
4. 命名和结构问题分批重构
5. 新代码必须完全合规，老代码逐步改进
```

### Q2：自定义规则和内置规则冲突怎么办？
```yaml
# 自定义规则会覆盖同名的内置规则
# 使用 extends 继承基础规则后，用 overrides 覆盖
extends: "default"
overrides:
  format:
    max_method_lines: 40  # 覆盖默认的 50
```

### Q3：如何排除特定文件不被审查？
```yaml
# 在规则配置中设置排除
excludes:
  - "**/legacy/**"      # 排除 legacy 目录
  - "**/*_old.cls"      # 排除旧文件
  - "**/test/**"        # 排除测试代码
```

### Q4：如何将审查集成到 CI/CD？
```yaml
# .gitlab-ci.yml
iris-code-review:
  stage: quality
  script:
    - （请参考skill目录中的脚本文件） src/
    - |
      CRITICAL_COUNT=$(grep -c "\[严重\]" iris-review-report-*.md)
      if [ "$CRITICAL_COUNT" -gt 0 ]; then
        echo "发现 $CRITICAL_COUNT 个严重问题，阻止合并"
        exit 1
      fi
  artifacts:
    reports:
# ...
## 已知限制
# ...
- 每次请求仅处理单一任务,不支持批量并发
- 
- 和网络环境
# ...