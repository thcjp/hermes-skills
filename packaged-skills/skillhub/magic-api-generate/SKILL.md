---
slug: "magic-api-generate"
name: "magic-api-generate"
version: 1.0.1
displayName: "magic-api-generate"
summary: "magic-api 国产接口快速开发框架。通过 Web UI 编写脚本自动映射为 HTTP 接口，无需 Controller/Service/Dao。当用户提到"
license: "Proprietary"
description: |-
  magic-api 国产接口快速开发框架。通过 Web UI 编写脚本自动映射为 HTTP 接口，无需 Controller/Service/Dao。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API.
tags:
  - Integrations
  - API
  - 接口
  - 开发工具
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Development"
---
# magic-api-generate

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |
| 代码复杂度可视化与重构建议 | 不支持 | 支持 |

## 核心能力

详见参考文档：

* **[语法参考](/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)** - 完整语法、内置函数、模块导入
* **[数据库操作](/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)** - 多数据源、分页、事务
* **[业务示例](/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)** - 登录认证、文件上传、导出等
### 语法参考(/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)

针对语法参考(/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32),自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供语法参考(/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)相关的配置参数、输入数据和处理选项.
**输出**: 返回语法参考(/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)的处理结果.
- 针对`语法参考(/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)`,解析输入数据并返回响应
- 验证返回数据的完整性和格式正确性
- 参考`语法参考(/api/v1/skills/magic-api-generate/file?path=references%2Fsyntax.md&ownerHandle=webx32)`的配置文档进行参数调优
### 数据库操作(/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)

针对数据库操作(/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32),自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供数据库操作(/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)相关的配置参数、输入数据和处理选项.
**输出**: 返回数据库操作(/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)的处理结果.
- 针对`数据库操作(/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)`,解析输入数据并返回响应
- 验证返回数据的完整性和格式正确性
- 参考`数据库操作(/api/v1/skills/magic-api-generate/file?path=references%2Fdatabase.md&ownerHandle=webx32)`的配置文档进行参数调优
### 业务示例(/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)

针对业务示例(/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32),自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供业务示例(/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)相关的配置参数、输入数据和处理选项.
**输出**: 返回业务示例(/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)的处理结果.
- 针对`业务示例(/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)`,解析输入数据并返回响应
- 验证返回数据的完整性和格式正确性
- 参考`业务示例(/api/v1/skills/magic-api-generate/file?path=references%2Fexamples.md&ownerHandle=webx32)`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 接口开发 | 接口路径与业务逻辑脚本 | 自动映射的HTTP接口 |
| 数据库操作 | SQL与数据源配置 | 多数据源查询/分页/事务结果 |
| 业务实现 | 登录认证/文件上传/导出需求 | 可运行的magic-api脚本 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

### 依赖说明

### 运行环境
1. **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
2. **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
3. ### 可用性分类
4. **分类**: MD+EXEC()
5. **说明**: 基于Markdown的AI Skill,

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|:---:|:---:|:---:|:---:|
| content | string | 否 | magic-api-generate处理的内容输入 |,  |
| content | string | 否 | magic-api-generate处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "generate 相关配置参数",
    result: "generate 相关配置参数",
    result: "generate 相关配置参数",
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

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明(补充)

| 依赖项 | 类型 | 必需 | 说明 |
|---:|:---|---:|---:|
| LLM | 模型 | 是 | 需要LLM进行内容生成, 推荐GPT-4/智谱GLM-4/DeepSeek |
| API Key | 凭证 | 否 | 使用云端LLM时需要, 本地LLM不需要 |

**国内替代方案**:
- OpenAI GPT → 智谱GLM-4 / 百度文心一言 / 通义千问 / DeepSeek
- OpenAI Embedding → 智谱embedding-2 / 百度embedding

## 案例展示

### 示例1：基础用法

```
### 依赖说明(补充)(补充)
# ...
```xml
<dependency>
    <groupId>org.ssssssss</groupId>
    <artifactId>magic-api-spring-boot-starter</artifactId>
    <version>2.2.2</version>
</dependency>
```
# ...
### application.yml 配置
# ...
```yaml
server:
  port: 9999

magic-api:
  web: /magic/web              # Web UI 入口
  resource:
    location: /data/magic-api  # 脚本存储位置（可改为 classpath: 只读模式）
```
# ...
### 访问 Web UI
# ...
```text
http://localhost:9999/magic/web
```
```

## 常见问题

### Q1: 如何开始使用magic-api-generate？
A: 

## 错误处理

| 错误场景(续)| 原因 | 处理方式 |
|:---------:|-----------|:----------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **安全性** - 生产环境关闭 Web UI 或限制 IP 访问
2. **版本控制** - 脚本目录建议 Git 管理
3. **密码加密** - 使用 MD5/BCrypt，不要明文存储
4. **SQL 注入** - 使用参数化查询 `?` 占位符
5. **性能** - 复杂逻辑拆分多个接口，避免单脚本过长
