---
slug: java-development-manual
name: java-development-manual
version: "0.1.0"
displayName: Java Development Manual
summary: Java开发手册规约集合，基于阿里巴巴Java开发手册（嵩山版）。 涵盖7大维度：编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约。
  当用户需要：(1) 编写或审查J...
license: MIT-0
description: |-
  Java开发手册规约集合，基于阿里巴巴Java开发手册（嵩山版）。 涵盖7大维度：编程规约、异常日志、单元测试、安全规约、MySQL数据库、工程结构、设计规约。
  当用户需要：(1) 编写或审查J...

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 嵩山版, 开发手册规约, development, 集合, 基于阿里巴巴, mysql, 开发手册, java
tags:
- Development
tools:
- read
- exec
---

# Java Development Manual

## 概述

本手册基于阿里巴巴Java开发手册（嵩山版），将规约分为7个维度。规约按约束力强弱分为：

| 级别 | 含义 | 说明 |
| --- | --- | --- |
| **【强制】** | 必须遵守 | 违反可能导致严重问题 |
| **【推荐】** | 建议遵守 | 提升代码质量和可维护性 |
| **【参考】** | 可选择性采纳 | 根据实际情况判断 |

## 章节导航

根据需求选择对应章节的详细规约：

| 章节 | 适用场景 | 详细文档 |
| --- | --- | --- |
| **编程规约** | 命名、格式、OOP、并发、集合处理 | [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) |
| **异常日志** | 错误码、异常处理、日志规范 | [exception-log.md](/api/v1/skills/java-development-manual/file?path=references%2Fexception-log.md&ownerHandle=shinelon) |
| **单元测试** | 测试用例、覆盖率、Mock | [unit-test.md](/api/v1/skills/java-development-manual/file?path=references%2Funit-test.md&ownerHandle=shinelon) |
| **安全规约** | SQL注入、XSS、CSRF、脱敏 | [security.md](/api/v1/skills/java-development-manual/file?path=references%2Fsecurity.md&ownerHandle=shinelon) |
| **MySQL数据库** | 建表、索引、SQL、ORM | [mysql.md](/api/v1/skills/java-development-manual/file?path=references%2Fmysql.md&ownerHandle=shinelon) |
| **工程结构** | 分层架构、依赖管理、服务器 | [project-structure.md](/api/v1/skills/java-development-manual/file?path=references%2Fproject-structure.md&ownerHandle=shinelon) |
| **设计规约** | UML、设计模式、设计原则 | [design.md](/api/v1/skills/java-development-manual/file?path=references%2Fdesign.md&ownerHandle=shinelon) |

## 快速参考

### 命名规范速查

```java
// 类名：UpperCamelCase
public class UserService { }
public class UserDO { }      // DO/DTO/VO例外

// 方法名/变量：lowerCamelCase
private String userName;
public void getUserById() { }

// 常量：全大写+下划线
public static final int MAX_RETRY_COUNT = 3;

// 包名：全小写
package com.company.project.service;
```

### 禁止事项速查

| 禁止 | 原因 |
| --- | --- |
| 拼音命名 | 可读性差 |
| 魔法值 | 难以维护 |
| `SELECT *` | 性能和可维护性 |
| Executors创建线程池 | 可能OOM |
| 字符串拼接SQL | 注入风险 |
| finally中return | 丢失try返回值 |
| foreach中remove | ConcurrentModificationException |

### 必须事项速查

| 必须 | 原因 |
| --- | --- |
| 覆写方法加@Override | 避免签名错误 |
| 表必备三字段 | id, create_time, update_time |
| 敏感数据脱敏 | 隐私保护 |
| 参数校验 | 安全防护 |
| ThreadLocal回收 | 避免内存泄漏 |
| 日志用占位符 | 性能优化 |

### 异常处理速查

```java
// 正确的异常处理
try {
    // 业务逻辑
} catch (SpecificException e) {
    logger.error("操作失败, 参数: {}", params, e);
    throw new BusinessException("用户友好提示", e);
} finally {
    // 资源关闭（JDK7+ try-with-resources）
}
```

### 数据库速查

```sql
-- 建表必备
CREATE TABLE example (
    `id` bigint unsigned NOT NULL AUTO_INCREMENT,
    `create_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
    `update_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 索引命名
-- 主键: pk_字段名
-- 唯一: uk_字段名
-- 普通: idx_字段名
```

### 并发处理速查

```java
// 线程池创建
ThreadPoolExecutor executor = new ThreadPoolExecutor(
    corePoolSize,
    maximumPoolSize,
    keepAliveTime,
    TimeUnit.SECONDS,
    new LinkedBlockingQueue<>(queueCapacity),
    new ThreadFactory() {
        private AtomicInteger counter = new AtomicInteger(1);
        public Thread newThread(Runnable r) {
            return new Thread(r, "worker-" + counter.getAndIncrement());
        }
    },
    new ThreadPoolExecutor.CallerRunsPolicy()
);

// ThreadLocal使用
try {
    threadLocal.set(value);
    // 业务逻辑
} finally {
    threadLocal.remove();  // 必须回收
}
```

## 使用指南

### 代码审查场景

1. **命名检查** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"命名风格"章节
2. **并发问题** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"并发处理"章节
3. **异常处理** → 查看 [exception-log.md](/api/v1/skills/java-development-manual/file?path=references%2Fexception-log.md&ownerHandle=shinelon)
4. **安全问题** → 查看 [security.md](/api/v1/skills/java-development-manual/file?path=references%2Fsecurity.md&ownerHandle=shinelon)

### 新项目搭建场景

1. **架构设计** → 查看 [design.md](/api/v1/skills/java-development-manual/file?path=references%2Fdesign.md&ownerHandle=shinelon)
2. **分层结构** → 查看 [project-structure.md](/api/v1/skills/java-development-manual/file?path=references%2Fproject-structure.md&ownerHandle=shinelon)
3. **数据库设计** → 查看 [mysql.md](/api/v1/skills/java-development-manual/file?path=references%2Fmysql.md&ownerHandle=shinelon)
4. **单元测试** → 查看 [unit-test.md](/api/v1/skills/java-development-manual/file?path=references%2Funit-test.md&ownerHandle=shinelon)

### 问题排查场景

1. **NPE问题** → 查看 [exception-log.md](/api/v1/skills/java-development-manual/file?path=references%2Fexception-log.md&ownerHandle=shinelon) 的"NPE防护"
2. **性能问题** → 查看 [mysql.md](/api/v1/skills/java-development-manual/file?path=references%2Fmysql.md&ownerHandle=shinelon) 的"索引规约"
3. **并发问题** → 查看 [coding-convention.md](/api/v1/skills/java-development-manual/file?path=references%2Fcoding-convention.md&ownerHandle=shinelon) 的"并发处理"

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
