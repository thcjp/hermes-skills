---
slug: "write-a-skill"
name: "write-a-skill"
version: "2.0.0"
displayName: "技能创建工具"
summary: "创建和优化AI技能，支持结构规划、渐进式披露、脚本集成和文件拆分"
license: "Proprietary"
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
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
---
# 技能创建工具

创建和优化AI技能，支持结构规划、渐进式披露、脚本集成和文件拆分。

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 技能创建工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
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
**处理**: 解析技能结构规划的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回技能结构规划的处理结果,包含执行状态码、结果数据和执行日志。

### 2. 渐进式披露
技能内容按层次组织：
- 第一层：`SKILL.md`（不超过100行），包含核心能力描述和基本使用
- 第二层：`REFERENCE.md`，包含详细API参考和参数说明
- 第三层：`EXAMPLES.md`，包含完整使用示例
- 引用文件最多1层深度，避免深层嵌套

**处理**: 解析渐进式披露的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回渐进式披露的处理结果,包含执行状态码、结果数据和执行日志。

### 3. 脚本集成
将可执行脚本放入 `scripts/` 目录，在 `SKILL.md` 中通过路径引用。

```markdown
执行以下命令：
\`\`\`bash
python3 （请参考skill目录中的脚本文件） --input data.json
\`\`\`
```

**输出**: 返回脚本集成的处理结果,包含执行状态码、结果数据和执行日志。
### 4. 文件拆分
当 `SKILL.md` 超过100行时，将详细内容拆分到 `REFERENCE.md`。当总内容超过500行时，进一步拆分到 `EXAMPLES.md`。

**处理**: 解析文件拆分的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回文件拆分的处理结果,包含执行状态码、结果数据和执行日志。

### 5. 技能描述编写
技能描述不超过1024字符，需包含：
- 核心功能一句话说明
- 支持的场景列表
- 不支持的场景说明
- 适用人群

**输入**: 用户提供技能描述编写所需的指令和必要参数。
**处理**: 解析技能描述编写的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。
**输出**: 返回技能描述编写的处理结果,包含执行状态码、结果数据和执行日志。

### 6. Front Matter生成
自动生成符合规范的front matter：

```yaml
---
slug: my-skill
name: my-skill
version: "1.0.0"
displayName: 技能名称
summary: 一句话描述
license: "Proprietary"
description: |-
  详细描述...
tools:
  - read
  - exec
---
```

**输入**: 用户提供Front Matter生成所需的指令和必要参数。
**处理**: 解析Front Matter生成的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `front_matter生成` 选项

### 7. 质量检查
检查技能文件的质量：
- `SKILL.md` 行数 ≤ 100
- 描述字符数 ≤ 1024
- 引用文件深度 ≤ 1层
- 术语一致性检查
- 示例完整性检查

**输入**: 用户提供质量检查所需的指令和必要参数。
**输出**: 返回质量检查的处理结果,包含执行状态码、结果数据和执行日志。

#
## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`write-a-skill`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 创建流程

### 第一步：确定技能范围

明确技能的核心功能和边界：
- 支持什么场景
- 不支持什么场景
- 需要哪些工具权限

### 第二步：编写SKILL.md

核心文件，不超过100行：
1. Front matter（slug, name, version, displayName, summary, license, description, tools）
2. 核心能力列表
3. 基本使用流程
4. 错误处理表
5. 常见问题

### 第三步：拆分详细内容

如果SKILL.md超过100行：
- API详细参考 → `REFERENCE.md`
- 完整示例 → `EXAMPLES.md`

### 第四步：添加脚本

可执行脚本放入 `scripts/` 目录，在SKILL.md中引用路径。

### 第五步：质量检查

```bash
# 检查行数
wc -l SKILL.md
# ...
# 检查描述字符数
head -20 SKILL.md | grep "description" | wc -c
# ...
# 检查引用文件深度
grep -r "\[.*\](.*\.md)" SKILL.md
```

## 真实示例

### 示例1：创建技能目录结构

```bash
mkdir -p my-skill/scripts
touch my-skill/SKILL.md
touch my-skill/REFERENCE.md
touch my-skill/EXAMPLES.md
```

### 示例2：SKILL.md模板

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
# ...
# 数据验证工具
# ...
## 环境依赖补充
# ...
| 依赖项 | 类型 | 必需 | 说明 |
|:---:|:---:|:---:|:---:|
| LLM API (用于AI推理和内容生成) | 外部服务 | 是 | 见核心能力章节 |
| Shell环境 (用于执行命令行操作) | 运行环境 | 否 | 见核心能力章节 |
| Python 3.8+ | 运行环境 | 否 | 见核心能力章节 |
# ...
## 能力速查
### 1. JSON Schema验证
### 2. CSV格式检查
### 3. 数据清洗
# ...
## 使用示例
\`\`\`bash
python3 （请参考skill目录中的脚本文件） --input data.json --schema schema.json
\`\`\`
# ...
详见 [REFERENCE.md](REFERENCE.md) 获取完整API参考。
```

### 示例3：拆分到REFERENCE.md

当SKILL.md超过100行时：

```markdown
# 数据验证工具 - 详细参考
# ...
## JSON Schema验证
# ...
### 支持的Schema类型
- type: string, number, integer, boolean, array, object, null
- format: date-time, email, uri, uuid
- constraints: minLength, maxLength, pattern, minimum, maximum
# ...
### 验证命令
\`\`\`bash
python3 （请参考skill目录中的脚本文件） --input data.json --schema user-schema.json
\`\`\`
# ...
### 输出格式
\`\`\`json
{"valid": true, "errors": [], "warnings": []}
\`\`\`
```

### 示例4：质量检查

```bash
# 检查SKILL.md行数
wc -l my-skill/SKILL.md
# 输出: 85 my-skill/SKILL.md
# ...
# 检查描述字符数
sed -n '/^description:/,/^---/p' my-skill/SKILL.md | wc -c
# 输出: 456
# ...
# 检查引用文件深度
grep -oP '\[.*?\]\(.*?\.md\)' my-skill/SKILL.md
# 输出: [REFERENCE.md](REFERENCE.md)
# 深度: 1层 (符合要求)
```

### 示例5：脚本集成

```bash
# （请参考skill目录中的脚本文件）
#!/usr/bin/env python3
import json, sys, argparse
# ...
parser = argparse.ArgumentParser()
parser.add_argument("--input", required=True)
parser.add_argument("--schema", required=True)
args = parser.parse_args()
# ...
with open(args.input) as f:
    data = json.load(f)
with open(args.schema) as f:
    schema = json.load(f)
# ...
# 验证逻辑...
print(json.dumps({"valid": True, "errors": []}))
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| SKILL.md超过100行 | 内容过多 | 将详细参考拆分到 `REFERENCE.md`，示例拆分到 `EXAMPLES.md` |
| 描述超过1024字符 | description字段过长 | 精简描述，只保留核心功能和场景说明，详细内容移入正文 |
| 引用文件超过1层深度 | REFERENCE.md引用EXAMPLES.md | 合并到同一文件，或直接在SKILL.md中内联关键内容 |
| 术语不一致 | 同一概念使用不同名称 | 统一术语表，在SKILL.md中定义关键术语 |
| 缺少使用示例 | 仅有描述无示例 | 在 `EXAMPLES.md` 中添加至少3个完整示例，包含输入和输出 |
| front matter字段缺失 | 缺少必要字段 | 补全8个字段：slug, name, version, displayName, summary, license, description, tools |
| slug与name不一致 | slug和name值不同 | 确保slug等于name等于文件夹名 |

## 常见问题

### Q1: SKILL.md最多多少行？
A: 100行。超过100行时，将详细API参考拆分到 `REFERENCE.md`，完整示例拆分到 `EXAMPLES.md`。SKILL.md只保留核心能力、基本使用和错误处理。

### Q2: description字段最多多少字符？
A: 1024字符。description应包含核心功能一句话说明、支持场景、不支持场景和适用人群。详细内容移入正文。

### Q3: 引用文件的深度限制是什么？
A: 最多1层深度。SKILL.md可以引用 `REFERENCE.md`，但 `REFERENCE.md` 不能再引用其他.md文件。避免深层嵌套导致Agent加载链过长。

### Q4: 如何决定内容拆分到哪个文件？
A: 核心能力和基本使用保留在 `SKILL.md`（≤100行）。API详细参考、参数说明和配置选项放入 `REFERENCE.md`。完整的使用示例（包含输入输出）放入 `EXAMPLES.md`。

### Q5: 脚本文件应该放在哪里？
A: 放入 `scripts/` 目录。在SKILL.md中通过路径引用（如 `python3 （请参考skill目录中的脚本文件）`）。脚本文件不计入SKILL.md的行数限制。

### Q6: front matter有哪些必填字段？
A: 8个字段：`slug`（等于文件夹名）、`name`（等于slug）、`version`、`displayName`（≤20字符）、`summary`（≤100字符）、`license`、`description`、`tools`（YAML数组格式）。

### Q7: 如何确保术语一致性？
A: 在SKILL.md开头定义关键术语表。全文使用统一的术语，不混用同义词。例如统一使用"技能"而非"skill"和"技能"混用。质量检查时通过 `grep` 验证术语使用频率。

## 已知限制

- SKILL.md不超过100行，超出需拆分
- description字段不超过1024字符
- 引用文件最多1层深度，不支持深层嵌套
- `tools` 字段必须为YAML数组格式（如 `- read`，非 `- - read`）
- `displayName` 不超过20字符
- `summary` 不超过100字符
- `slug` 必须等于 `name` 必须等于文件夹名
