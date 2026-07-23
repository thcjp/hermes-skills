---
slug: "java-reviewer"
name: "java-reviewer"
version: "1.0.0"
displayName: "Java代码审查专业版"
summary: "企业级 Java 代码审查方案，支持批量审查、自定义规则、HTML 报告与 CI 集成。"
license: "Proprietary"
edition: "pro"
description: |-
  面向企业级 Java 开发团队的代码审查治理工具。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - 开发工具
  - Java
  - 代码审查
  - 企业协作
  - 安全审计
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Java代码审查专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| 能力模块 | 支持 | 支持 |
| 专业版新增 | 不支持 | 支持 |
| 审查范围 | 不支持 | 支持 |
| 批量多文件/多模块/全项目 | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

| 能力模块 | 免费版 | 专业版新增 |
| --- | --- | --- |
| 审查范围 | 单文件/diff | 批量多文件/多模块/全项目 |
| 审查规则 | 内置固定规则 | 自定义规则 + 团队配置 |
| 报告格式 | Markdown | Markdown + HTML + JSON |
| 需求检查 | - | 需求/设计文档一致性检查 |
| 安全审计 | 基础安全检查 | OWASP Top 10 全面审计 |
| CI 集成 | - | 质量门禁 + 合并请求拦截 |
| 趋势追踪 | - | 历史报告对比与质量趋势 |
| 修复建议 | 代码片段 | 批量自动修复脚本 |
### 能力模块

执行能力模块,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供能力模块相关的配置参数、输入数据和处理选项。

**输出**: 返回能力模块的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`能力模块`相关配置参数进行设置
### 审查范围

执行审查范围,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供审查范围相关的配置参数、输入数据和处理选项。

**输出**: 返回审查范围的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`审查范围`相关配置参数进行设置
### 审查规则

执行审查规则,自动处理参数解析、任务调度和结果格式化,返回结构化输出。

**输入**: 用户提供审查规则相关的配置参数、输入数据和处理选项。

**输出**: 返回审查规则的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`审查规则`相关配置参数进行设置
#
## 适用场景

### 场景一：全项目批量审查
团队需要对整个项目进行全面的代码审查。

```bash
#!/bin/bash
PROJECT_DIR=$1
REPORT_DIR="reports/java-review-$(date +%Y%m%d)"
mkdir -p "$REPORT_DIR"

echo "=== Java 批量代码审查 ==="
echo "项目目录: $PROJECT_DIR"
echo "报告目录: $REPORT_DIR"
echo ""

JAVA_FILES=$(find "$PROJECT_DIR" -name "*.java" -not -path "*/test/*")
FILE_COUNT=$(echo "$JAVA_FILES" | wc -l)
echo "审查文件数: $FILE_COUNT"

TOTAL_ISSUES=0
CRITICAL=0
MAJOR=0
MINOR=0
SUGGESTION=0

cat > "$REPORT_DIR/summary.md" << 'EOF'
EOF

echo "| 指标 | 数值 |" >> "$REPORT_DIR/summary.md"
echo "| --- | --- |" >> "$REPORT_DIR/summary.md"
echo "| 审查日期 | $(date) |" >> "$REPORT_DIR/summary.md"
echo "| 审查范围 | $PROJECT_DIR |" >> "$REPORT_DIR/summary.md"
echo "| 文件数量 | $FILE_COUNT |" >> "$REPORT_DIR/summary.md"

echo "$JAVA_FILES" | while read file; do
  REL_PATH=${file#$PROJECT_DIR/}

  SQL_INJECTION=$(grep -n "String sql.*+.*\"" "$file" | head -5)
  if [ -n "$SQL_INJECTION" ]; then
    echo "[Critical] $REL_PATH: 可能的 SQL 注入" >> "$REPORT_DIR/issues.md"
    echo "$SQL_INJECTION" >> "$REPORT_DIR/issues.md"
  fi

  HARDCODED_PWD=$(grep -in "password.*=.*\"\|secret.*=.*\"" "$file" | head -5)
  if [ -n "$HARDCODED_PWD" ]; then
    echo "[Critical] $REL_PATH: 硬编码密码/密钥" >> "$REPORT_DIR/issues.md"
    echo "$HARDCODED_PWD" >> "$REPORT_DIR/issues.md"
  fi

  EMPTY_CATCH=$(awk '/catch.*\{/{flag=1;next}/\}/{if(flag && NR-prev<3) print FILENAME":"prev; flag=0}flag{prev=NR}' "$file")
  if [ -n "$EMPTY_CATCH" ]; then
    echo "[Major] $REL_PATH: 空 catch 块" >> "$REPORT_DIR/issues.md"
    echo "$EMPTY_CATCH" >> "$REPORT_DIR/issues.md"
  fi

  UNCLOSED=$(grep -n "new FileInputStream\|new FileOutputStream\|getConnection" "$file" | grep -v "try.*(" | head -5)
  if [ -n "$UNCLOSED" ]; then
    echo "[Major] $REL_PATH: 资源可能未正确关闭" >> "$REPORT_DIR/issues.md"
    echo "$UNCLOSED" >> "$REPORT_DIR/issues.md"
  fi

  LONG_METHODS=$(awk '/public|private|protected.*\(/{start=NR;name=$0}/^\}/{if(NR-start>50) print FILENAME":"start"-"NR" ("NR-start"行) "name; start=0}' "$file")
  if [ -n "$LONG_METHODS" ]; then
    echo "[Minor] $REL_PATH: 方法过长" >> "$REPORT_DIR/issues.md"
    echo "$LONG_METHODS" >> "$REPORT_DIR/issues.md"
  fi
done

echo ""
echo "=== 审查完成 ==="
echo "报告位置: $REPORT_DIR/"
```

### 场景二：自定义审查规则配置
团队需要根据项目特点自定义审查规则。

```yaml
version: "2.0"
team: "后端开发组"
updated: "2026-07-18"

extends: "default"

rules:
  naming:
    max_method_length: 40        # 比默认 50 更严格
    max_parameter_count: 4       # 方法参数上限
    required_class_suffix:       # 类名后缀要求
      controller: "Controller"
      service: "Service"
      repository: "Repository"
      dto: "DTO"

  security:
    owasp_top_10: true           # 启用 OWASP Top 10 检查
    forbidden_apis:              # 禁止使用的 API
      - "System.out.println"     # 禁止直接控制台输出
      - "Runtime.getRuntime"     # 禁止直接执行命令
      - "ObjectInputStream"      # 禁止反序列化
    required_validation:         # 必须校验的输入
      - "RequestMapping"
      - "PostMapping"
      - "GetMapping"

  performance:
    warn_collection_init: true   # 集合未指定初始容量时告警
    warn_string_concat: true     # 循环内字符串拼接告警
    max_query_count: 5           # 单个请求最大查询数
  design:
    max_cyclomatic_complexity: 10  # 最大圈复杂度
    max_class_length: 500          # 最大类行数
    require_di_pattern: true       # 依赖注入模式
excludes:
  - "**/test/**"
  - "**/generated/**"
  - "**/legacy/**"
  - "**/dto/**"       # DTO 类只检查命名
severity_override:
  empty_catch: critical           # 空 catch 提升为 Critical
  magic_number: minor             # 魔法值降为 Minor
report:
  formats: ["markdown", "html", "json"]
  output_dir: "reports/"
  include_metrics: true
  include_trend: true
```

### 场景三：CI/CD 质量门禁
合并请求需要通过代码审查才能合并。

```yaml
name: Java 代码质量门禁
on:
  pull_request:
    branches: [main, develop]

jobs:
  code-review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
        with:
          fetch-depth: 0  # 获取完整历史用于 diff
      - name: 安装 Java
        uses: actions/setup-java@v4
        with:
          java-version: '17'
          distribution: 'temurin'

      - name: 执行代码审查
        run: |
          （请参考skill目录中的脚本文件） src/

      - name: 检查 Critical 问题数
        run: |
          CRITICAL_COUNT=$(grep -c "\[Critical\]" reports/java-review-*/issues.md || echo 0)
          echo "Critical 问题数: $CRITICAL_COUNT"
          if [ "$CRITICAL_COUNT" -gt 0 ]; then
            echo "::error::发现 $CRITICAL_COUNT 个 Critical 问题，阻止合并"
            exit 1
          fi

      - name: 检查 Major 问题数
        run: |
          MAJOR_COUNT=$(grep -c "\[Major\]" reports/java-review-*/issues.md || echo 0)
          echo "Major 问题数: $MAJOR_COUNT"
          if [ "$MAJOR_COUNT" -gt 5 ]; then
            echo "::warning::Major 问题数超过 5 个，建议修复后再合并"
          fi

      - name: 上传审查报告
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: java-review-report
          path: reports/

      - name: 评论审查结果
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const report = fs.readFileSync('reports/java-review-*/summary.md', 'utf8');
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: `## 代码审查报告\n\n${report}`
            });
```

## 使用流程

### OWASP 安全审计检查清单
| OWASP 类别 | 检查项 | 检测方法 |
| --- | --- | --- |
| 注入 | SQL 注入 | 检查字符串拼接 SQL |
| 注入 | 命令注入 | 检查 Runtime.exec 调用 |
| 认证失效 | 硬编码凭据 | 搜索 password/secret 赋值 |
| 敏感数据暴露 | 明文传输 | 检查 HTTP 连接（非 HTTPS） |
| XML 外部实体 | XXE 漏洞 | 检查 XML 解析器配置 |
| 访问控制失效 | 缺少权限校验 | 检查 Controller 方法注解 |
| 安全配置错误 | 调试信息泄露 | 检查异常信息直接返回前端 |
| XSS | 未转义输出 | 检查响应输出是否转义 |
| 不安全反序列化 | 反序列化漏洞 | 检查 ObjectInputStream |
| 已知漏洞组件 | 依赖漏洞 | 扫描依赖版本 |

### HTML 报告模板
```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>Java 代码审查报告</title>
    <style>
        body { font-family: sans-serif; margin: 20px; }
        .summary { background: #f5f5f5; padding: 15px; border-radius: 5px; }
        .critical { color: #d32f2f; }
        .major { color: #f57c00; }
        .minor { color: #1976d2; }
        .suggestion { color: #388e3c; }
        table { border-collapse: collapse; width: 100%; margin: 10px 0; }
        th, td { border: 1px solid #ddd; padding: 8px; }
        th { background: #f0f0f0; }
        .chart { display: flex; gap: 20px; margin: 20px 0; }
        .chart-bar { display: flex; align-items: end; height: 200px; }
    </style>
</head>
<body>
    <h1>Java 代码审查报告</h1>
    <div class="summary">
        <p><strong>审查日期</strong>: "reviewer_result"</p>
        <p><strong>审查范围</strong>: 全维度</p>
        <p><strong>文件数量</strong>: "reviewer_metadata"</p>
        <p><strong>问题总数</strong>: "reviewer_status"</p>
        <ul>
            <li class="critical">Critical: "reviewer_summary"</li>
            <li class="major">Major: "reviewer_details"</li>
            <li class="minor">Minor: "reviewer_count"</li>
            <li class="suggestion">Suggestion: 建议优化</li>
        </ul>
    </div>

    <h2>问题趋势</h2>
    <div class="chart">
        <!-- 历史趋势图表 -->
    </div>

    <h2>问题详情</h2>
    <table>
        <tr>
            <th>序号</th>
            <th>严重程度</th>
            <th>文件</th>
            <th>行号</th>
            <th>维度</th>
            <th>问题描述</th>
            <th>规则</th>
        </tr>
        相关信息
        <tr>
            <td>"reviewer_timestamp"</td>
            <td class=""reviewer_version"">"reviewer_version"</td>
            <td>"field_9"</td>
            <td>"field_10"</td>
            <td>"field_11"</td>
            <td>reviewer 相关配置参数</td>
            <td>"field_12"</td>
        </tr>
        相关信息
    </table>
</body>
</html>
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | java-reviewer处理的内容输入 |, 默认: 全部维度 |
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


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持读取 SKILL.md 的任意 AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **JDK 版本**: 建议 11 及以上
- **CI/CD 平台**: GitHub Actions / GitLab CI / Jenkins 等

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| JDK | 编译器/运行时 | 推荐 | oracle.com 或 openjdk.net 下载 |
| Git | 命令行工具 | 必需 | 系统包管理器安装 |
| Maven/Gradle | 构建工具 | 可选 | maven.apache.org / gradle.org |
| OWASP Dependency-Check | 安全扫描 | 可选 | `mvn dependency-check:check` |
| jq | JSON 处理 | 可选 | 系统包管理器安装 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令驱动，无需额外 API Key
- CI/CD 集成需要在平台配置对应的访问令牌
- 依赖漏洞扫描需要配置 NVD API Key（免费申请）

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 执行代码审查，专业版功能依赖构建工具和 CI/CD 平台

## 案例展示

### 需求一致性检查
```text
审查时提供需求文档，工具会检查代码实现与需求的一致性

输入：
1. git diff 输出
2. 需求文档（可选）
3. 设计文档（可选）

一致性检查项：
- 需求中的功能点是否都已实现
- 代码改动是否超出需求范围
- 接口设计是否与文档一致
- 数据结构是否与设计匹配

输出：
- [已实现] 用户注册接口（需求 3.1）
- [已实现] 邮箱验证功能（需求 3.2）
- [未实现] 手机号注册（需求 3.3）← 需关注
- [超范围] 修改了登录逻辑（不在需求范围内）
```

### 质量趋势统计
```bash
#!/bin/bash
echo "日期,Critical,Major,Minor,Suggestion,总文件数" > quality-trend.csv

for report in reports/java-review-*/summary.md; do
  date=$(echo $report | grep -o '[0-9]*' | head -1)

  critical=$(grep -c "Critical:" "$report" 2>/dev/null || echo 0)
  major=$(grep -c "Major:" "$report" 2>/dev/null || echo 0)
  minor=$(grep -c "Minor:" "$report" 2>/dev/null || echo 0)
  suggestion=$(grep -c "Suggestion:" "$report" 2>/dev/null || echo 0)
  files=$(grep "文件数量" "$report" | grep -o '[0-9]*')

  echo "$date,$critical,$major,$minor,$suggestion,$files" >> quality-trend.csv
done

echo "趋势数据已保存到 quality-trend.csv"
```

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 常见问题

### Q1：如何减少误报？
```yaml
excludes:
  - "**/test/**"          # 排除测试代码
  - "**/generated/**"     # 排除生成代码
  - "**/migration/**"     # 排除迁移脚本
severity_override:
  magic_number: suggestion  # 魔法值降为建议
```

### Q2：如何处理大量历史问题？
```text
策略：
1. 先生成完整报告，评估问题规模
2. 按严重程度排序，优先修复 Critical
3. 将修复任务拆分到多个迭代
4. 新代码必须完全合规（增量控制）
5. 老代码设定改进目标（如每迭代减少 20%）
```

### Q3：如何集成到 SonarQube？
```bash
（请参考skill目录中的脚本文件） reports/java-review-latest/ > sonar-issues.json

[
  {
    "rule": "java:S2077",
    "severity": "BLOCKER",
    "message": "SQL 注入风险",
    "component": "src/main/java/UserService.java",
    "line": 45
  }
]
```

### Q4：如何统计代码质量指标？
| 指标 | 计算方式 | 目标值 |
| --- | --- | --- |
| Critical 密度 | Critical 数 / 千行 | 0 |
| Major 密度 | Major 数 / 千行 | < 2 |
| 代码合规率 | (1 - 问题文件数 / 总文件数) × 100% | > 95% |
| 平均修复时间 | 问题提出到修复的天数 | < 3 天 |
| 重复代码率 | 重复行数 / 总行数 | < 5% |

### Q5：如何做安全审计？
```bash
echo "=== OWASP 安全审计 ==="

echo "检查 SQL 注入..."
grep -rn "String sql.*+.*\"" src/ --include="*.java"

echo "检查硬编码凭据..."
grep -rn "password.*=.*\"\|secret.*=.*\"" src/ --include="*.java"

echo "检查明文传输..."


## 已知限制

- 每次请求仅处理单一任务,不支持批量并发
- 
- 和网络环境
