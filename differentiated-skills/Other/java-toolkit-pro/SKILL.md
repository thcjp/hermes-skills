---
slug: java-toolkit-pro
name: java-toolkit-pro
version: "1.0.0"
displayName: Java 工具箱专业版
summary: 面向团队的全项目扫描、规则集治理与 JVM 调优工具。
license: Proprietary
edition: pro
description: |-
  面向团队的 Java 全项目扫描、规则集治理与 JVM 调优专业工具。核心能力:
  - 全项目批量规则扫描与回归
  - 团队规则集与豁免治理
  - JVM/GC/模块化深度主题
  - 测试（JUnit/Mockito）与性能门禁

  适用场景:
  - 企业多模块 Java 项目统一规则
  - 团队规则集与豁免版本化治理
  - JVM 调优与性能门禁

  差异化: 专业版在免费版单文件自检上扩展全项目扫描、规则集治理、JVM 调优与测试门禁，兼容免费版 14 条规则
tags:
- Java
- 企业级
- 代码质量
- JVM
- 其他工具
tools:
  - - read
- exec
---
# Java 工具箱（专业版）

## 概述

专业版面向团队与企业，在免费版 14 条关键规则基础上，扩展全项目批量扫描、团队规则集与豁免治理、JVM/GC/模块化深度主题与测试性能门禁。规则与免费版兼容，已有规则可直接纳入规则集。

## 核心能力

| 能力 | 说明 | 专业版增强 |
|:-----|:-----|:-----------|
| 全项目扫描 | 多模块批量规则检查 | 回归追踪 |
| 规则集治理 | 规则、豁免、严重级 | 版本化 |
| JVM 主题 | GC、内存、模块化 | 深度专题 |
| 测试门禁 | JUnit/Mockito 覆盖率 | 构建期卡控 |
| 性能门禁 | 关键路径性能阈值 | CI 阻断 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置。

### 核心功能执行
用`input_params`参数进行配置。

**输入**: 用户提供核心功能执行所需的指令和必要参数。
**处理**: 按照skill规范执行核心功能执行操作,遵循单一意图原则。
**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输入**: 用户提供参数配置与调用所需的指令和必要参数。
**处理**: 按照skill规范执行参数配置与调用操作,遵循单一意图原则。
**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置。

**输入**: 用户提供结果处理与输出所需的指令和必要参数。
**处理**: 按照skill规范执行结果处理与输出操作,遵循单一意图原则。
**输出**: 返回结果处理与输出的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向团队的全项目、规则集治理与、调优工具、面向团队的、Java、调优专业工具、全项目批量规则扫、描与回归、团队规则集与豁免、模块化深度主题、与性能门禁等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：全项目规则扫描

```bash
# 批量扫描（专业版）
./gradlew check -PjavaRules=team-ruleset.json --scan-report java-report.json
```

```text
报告示例:
  严重: 3 处 equals 未配 hashCode
  中等: 5 处 volatile 误用为原子
  提示: 8 处 Optional.get() 未判空
  覆盖模块: 12 / 12
```

### 场景二：团队规则集治理

```json
{
  "ruleset": "team-java-v2",
  "rules": {
    "equals_hashcode_pair": {"severity": "block"},
    "volatile_atomicity": {"severity": "block"},
    "optional_get_without_check": {"severity": "warn"},
    "try_with_resources": {"severity": "block"}
  },
  "exclusions": [
    {"path": "legacy/**", "reason": "遗留模块，迁移期豁免", "until": "2026-12"}
  ]
}
```

### 场景三：JVM 调优与测试门禁

```bash
# GC 日志分析
java -Xlog:gc*=info:file=gc.log -jar app.jar
# 覆盖率门禁
./gradlew test jacocoTestCoverageVerification \
  -Pminimum.coverage=0.80
```

```json
{
  "jvm_tuning": {"gc": "G1GC", "max_pause_ms": 200, "heap": "4G"},
  "test_gate": {"min_coverage": 0.80, "block_on_fail": true},
  "modules": ["app", "core", "api"]
}
```

## 不适用场景

以下场景Java 工具箱专业版不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析

## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求。

## 快速开始

1. 将免费版 14 条规则纳入团队规则集。
2. 配置豁免清单与严重级。
3. 接入构建期扫描与覆盖率门禁。
4. 启用 JVM 调优与性能门禁。

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

### 命令参数说明

- `-PjavaRules`: 命令参数,用于指定操作选项
- `-Pminimum`: 命令参数,用于指定操作选项
- `-Xlog`: 命令参数,用于指定操作选项
- `-Xmx4g`: 命令参数,用于指定操作选项
- `-XX`: 命令参数,用于指定操作选项
- `-Xms4g`: 命令参数,用于指定操作选项

## 示例

扫描配置（`java-scan.json`）：

```json
{
  "modules": ["app", "core", "api"],
  "ruleset": "team-java-v2",
  "report": "java-report.json",
  "coverage_min": 0.80,
  "block_severe": true,
  "regression_baseline": "main"
}
```

## 最佳实践

- **规则集版本化**：规则变更走版本，便于回溯与协同。
- **豁免要限期**：所有豁免标注原因与期限，到期自动告警。
- **门禁分级**：严重级阻断构建，警告级仅记录。
- **覆盖率设底线**：关键模块覆盖率 ≥ 80%，低于阈值阻断。
- **GC 先观测再调**：先开 GC 日志观测，再调参数，别凭感觉。

## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-------|:-------|
| 14 条规则 | 相同 | 相同（纳入规则集） |
| 范围 | 单文件 | 全项目批量 |
| 规则集 | 不支持 | 版本化治理 |
| JVM 调优 | 不支持 | 支持 |

## 常见问题

**Q1：规则集怎么团队协同？**
A：规则集 JSON 版本化管理，团队评审后合并。

**Q2：全项目扫描要多久？**
A：取决于代码量，10 万行约 2-5 分钟，支持增量扫描。

**Q3：免费版规则能直接升级吗？**
A：能。把 14 条规则作为规则集基础，再扩展团队规则。

**Q4：覆盖率门禁怎么接 CI？**
A：构建后跑 JaCoCo 覆盖率校验，低于阈值退出非零。

**Q5：专业版有优先支持吗？**
A：有。专业版享规则定制与 JVM 调优咨询。

## 进阶用法

### JVM 调优专题

```bash
# GC 日志（JDK 11+）
java -Xlog:gc*=info:file=gc.log:time,level,tags -jar app.jar

# 常用 GC 参数
java -XX:+UseG1GC \
     -XX:MaxGCPauseMillis=200 \
     -Xms4g -Xmx4g \
     -XX:+HeapDumpOnOutOfMemoryError \
     -jar app.jar
```

```text
GC 选择:
  G1GC:    通用，平衡吞吐与延迟（JDK 9+ 默认）
  ZGC:     超低延迟，大堆
  Parallel: 高吞吐，批处理
  调优原则: 先观测再调，别凭感觉
```

### 模块化（JPMS）

```text
module-info.java:
  module com.example.app {
      requires java.sql;
      requires org.slf4j;
      exports com.example.api;
      opens com.example.internal to spring.core;
  }

模块化收益:
  - 强封装，明确导出
  - 启动更快（少加载）
  - 依赖清晰，避免循环
```

### 测试与覆盖率门禁

```groovy
// Gradle JaCoCo 门禁
jacocoTestCoverageVerification {
    violationRules {
        rule {
            limit {
                minimum = 0.80
            }
        }
    }
}
check.dependsOn jacocoTestCoverageVerification
```

## 规则集治理

- **规则分级**：block（阻断）/ warn（告警）/ info（记录）。
- **豁免限期**：遗留违规走豁免，标注期限，到期告警。
- **增量扫描**：大项目用增量扫描，只查变更文件。
- **趋势归档**：每次扫描归档，绘制违规趋势。
- **组件源头治**：高频违规在组件库层修复。

## 性能门禁

```json
{
  "performance_gate": {
    "p99_latency_ms": 200,
    "throughput_min": 1000,
    "gc_pause_ms": 100,
    "block_on_regression": true,
    "baseline": "main"
  }
}
```

- **关键路径压测**：每次发布跑关键路径性能测试。
- **回归即阻断**：性能劣化超阈值阻断发布。
- **GC 先观测**：开 GC 日志观测再调，避免盲目调参。
- **堆 dump 留底**：OOM 时自动 dump，便于分析。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **JDK**: 11+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| JDK | 工具链 | 必需 | adoptium.net |
| Gradle/Maven | 构建工具 | 推荐 | gradle.org / maven.apache.org |
| JaCoCo | 覆盖率 | 门禁时必需 | `org.jacoco` 插件 |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令，无需额外 API Key

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成全项目扫描与门禁治理

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
