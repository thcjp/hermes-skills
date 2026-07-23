---
slug: "write-a-skill-free"
name: "write-a-skill-free"
version: "1.0.0"
displayName: "技能创建工具(免费版)"
summary: "创建和优化AI技能，支持结构规划、渐进式披露、脚本集成和文件拆分(免费版)"
license: "MIT"
description: |-
  AI技能创建和优化工具。支持技能结构规划、渐进式披露设计、脚本集成和文件
  拆分。技能描述不超过1024字符，SKILL.md不超过100行，超过500行时拆分到
  REFERENCE.md和EXAMPLES.md。引用文件最多1层深度。适用于独立开发者、
  企业团队和自动化工作流场景。不适用于非AI技能的文档创建。
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
tags:
  - 通用办公
---
# 技能创建工具(免费版)

创建和优化AI技能，支持结构规划、渐进式披露、脚本集成和文件拆分。

## 核心能力

### 1. 技能结构规划
规划技能的文件结构，核心文件为 `SKILL.md`，辅助文件包括 `REFERENCE.md` 和 `EXAMPLES.md`。

```
skills/
  my-skill/
    SKILL.md          # 主文件，不超过100行
    REFERENCE.md      # 详细参考，拆分自SKILL.md
    EXAMPLES.md       # 使用示例
    scripts/          # 脚本目录
      helper.py
```

**输入**: 用户提供技能结构规划所需的指令和必要参数。
**处理**: 按照skill规范执行技能结构规划操作,遵循单一意图原则。
**输出**: 返回技能结构规划的执行结果,包含操作状态和输出数据。

### 2. 渐进式披露
技能内容按层次组织：
- 第一层：`SKILL.md`（不超过100行），包含核心能力描述和基本使用
- 第二层：`REFERENCE.md`，包含详细API参考和参数说明
- 第三层：`EXAMPLES.md`，包含完整使用示例
- 引用文件最多1层深度，避免深层嵌套

**处理**: 按照skill规范执行渐进式披露操作,遵循单一意图原则。
**输出**: 返回渐进式披露的执行结果,包含操作状态和输出数据。

### 3. 脚本集成
将可执行脚本放入 `scripts/` 目录，在 `SKILL.md` 中通过路径引用。

```markdown
执行以下命令：
\`\`\`bash
python3 （请参考skill目录中的脚本文件） --input data.json
\`\`\`
```

**输出**: 返回脚本集成的执行结果,包含操作状态和输出数据。
### 4. 文件拆分
当 `SKILL.md` 超过100行时，将详细内容拆分到 `REFERENCE.md`。当总内容超过500行时，进一步拆分到 `EXAMPLES.md`。

**处理**: 按照skill规范执行文件拆分操作,遵循单一意图原则。
**输出**: 返回文件拆分的执行结果,包含操作状态和输出数据。

#
## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 创建新技能 | 技能功能描述 | SKILL.md+REFERENCE.md+EXAMPLES.md |
| 优化现有技能 | 现有SKILL.md | 优化后的技能文件 |

## 使用流程

1. 确定技能范围:支持什么场景、不支持什么场景、需要哪些工具权限
2. 编写SKILL.md(不超过100行):Front matter+核心能力+使用流程+错误处理+常见问题
3. 拆分详细内容:API参考→REFERENCE.md,完整示例→EXAMPLES.md
4. 添加脚本到 `scripts/` 目录
5. 质量检查:行数≤100、描述≤1024字符、引用深度≤1层

#
## 示例

### 示例:SKILL.md模板

```yaml
---
slug: data-validator
name: data-validator
version: "1.0.0"
displayName: 数据验证工具
summary: 验证JSON、CSV数据格式，支持Schema检查和数据清洗
license: MIT
description: |-
  数据验证工具，支持JSON Schema验证、CSV格式检查和数据清洗。
  适用于API响应验证、数据导入预处理和数据质量检查场景。
tools:
  - read
  - exec
---

# 数据验证工具

## 核心能力
### 1. JSON Schema验证
### 2. CSV格式检查
### 3. 数据清洗

## 使用示例
\`\`\`bash
python3 （请参考skill目录中的脚本文件） --input data.json --schema schema.json
\`\`\`

详见 [REFERENCE.md](REFERENCE.md) 获取完整API参考。
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| SKILL.md超过100行 | 内容过多 | 将详细参考拆分到 `REFERENCE.md`，示例拆分到 `EXAMPLES.md` |
| 描述超过1024字符 | description字段过长 | 精简描述，只保留核心功能和场景说明，详细内容移入正文 |
| 引用文件超过1层深度 | REFERENCE.md引用EXAMPLES.md | 合并到同一文件，或直接在SKILL.md中内联关键内容 |
| front matter字段缺失 | 缺少必要字段 | 补全8个字段：slug, name, version, displayName, summary, license, description, tools |

## 常见问题

### Q1: SKILL.md最多多少行？
A: 100行。超过100行时，将详细API参考拆分到 `REFERENCE.md`，完整示例拆分到 `EXAMPLES.md`。SKILL.md只保留核心能力、基本使用和错误处理。

### Q2: description字段最多多少字符？
A: 1024字符。description应包含核心功能一句话说明、支持场景、不支持场景和适用人群。详细内容移入正文。

### Q3: 引用文件的深度限制是什么？
A: 最多1层深度。SKILL.md可以引用 `REFERENCE.md`，但 `REFERENCE.md` 不能再引用其他.md文件。避免深层嵌套导致Agent加载链过长。

## 已知限制

- SKILL.md不超过100行，超出需拆分
- description字段不超过1024字符
- 引用文件最多1层深度，不支持深层嵌套

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 升级提示

本免费版提供基础功能。升级到完整版 write-a-skill 获取全部能力和高级特性。
