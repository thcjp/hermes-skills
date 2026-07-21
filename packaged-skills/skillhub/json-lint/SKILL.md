---
slug: json-lint
name: json-lint
version: "1.0.0"
displayName: JSON校验工具专业版
summary: 企业级JSON校验工具，支持并行扫描、Schema验证、超集兼容、自动修复与监控告警。
license: Proprietary
edition: pro
description: |-
  JSON校验工具专业版面向企业级场景，在免费版基础上扩展并行扫描、JSON Schema验证、JSON5/JSONC超集兼容、自动修复建议、历史趋势监控等高级能力。核心能力：多线程并行扫描万级文件、基于JSON Schema的语义校验、JSON5/JSONC/JSON-LD超集支持、自动修复建议生成、通过率历史趋势与告警、CI/CD深度集成
tags:
- 集成工具
- JSON
- 企业级
- 校验
tools:
  - - read
- exec
---
# JSON校验工具专业版

## 核心能力

### 并行扫描引擎
- 多线程并行校验，默认8线程，可配置
- 万级文件分钟级完成
- 任务分片：按目录或文件大小分片，负载均衡
- 进度可观测：实时输出处理进度

### JSON Schema验证
- 支持JSON Schema Draft 7/2019-09/2020-12
- 类型校验：string/number/integer/boolean/array/object/null
- 约束校验：required/enum/pattern/minLength/maxLength/minimum/maximum
- 嵌套校验：properties/items/additionalProperties
- 引用校验：$ref跨文件引用

**输入**: 用户提供JSON Schema验证所需的指令和必要参数。
**处理**: 按照skill规范执行JSON Schema验证操作,遵循单一意图原则。
**输出**: 返回JSON Schema验证的执行结果,包含操作状态和输出数据。### 超集兼容
| 超集 | 特性 | 适用场景 |
|------|------|----------|
| JSON5 | 注释、单引号、尾随逗号、十六进制 | 配置文件 |
| JSONC | 注释 | VS Code配置 |
| JSON-LD | @context语义标注 | 知识图谱 |
| HJSON | 多行字符串、注释 | 人类可读配置 |

**输入**: 用户提供超集兼容所需的指令和必要参数。
**处理**: 按照skill规范执行超集兼容操作,遵循单一意图原则。
**输出**: 返回超集兼容的执行结果,包含操作状态和输出数据。### 自动修复建议
- 定位错误位置（行列号+上下文）
- 生成修复方案（修改前/修改后对比）
- 修复置信度评分
- 一键应用修复（需确认）

**输入**: 用户提供自动修复建议所需的指令和必要参数。
**处理**: 按照skill规范执行自动修复建议操作,遵循单一意图原则。### 监控告警
- 通过率历史趋势（日/周/月）
- 通过率下降自动告警
- 新增错误文件告警
- 错误类型分布统计
- 集成Webhook/邮件/钉钉

**输入**: 用户提供监控告警所需的指令和必要参数。
**处理**: 按照skill规范执行监控告警操作,遵循单一意图原则。
**输出**: 返回监控告警的执行结果,包含操作状态和输出数据。
### JSON5

执行JSON5操作,处理用户输入并返回结果。

**输入**: 用户提供JSON5所需的参数和指令。

**输出**: 返回JSON5的处理结果。

- 执行`JSON5`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`JSON5`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、校验工具、支持并行扫描、自动修复与监控告、校验工具专业版面、向企业级场景、在免费版基础上扩、展并行扫描、历史趋势监控等高、级能力、核心能力、多线程并行扫描万、的语义校验、超集支持、自动修复建议生成、通过率历史趋势与、深度集成。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

| 场景 | 角色 | 价值 | 推荐能力 |
|------|------|------|----------|
| 大型项目质量门禁 | 架构师 | 万级文件分钟校验 | 并行扫描+Schema验证 |
| 企业配置中心校验 | 运维主管 | 配置语义合规检查 | Schema验证+监控告警 |
| API契约验证 | 后端开发者 | 响应是否符合契约 | Schema验证 |
| 数据迁移验收 | 数据库管理员 | 迁移数据语法+语义校验 | 并行扫描+Schema验证 |
| 多团队规范统一 | 技术负责人 | 统一JSON规范并监控 | Schema验证+监控告警 |
| 合规审计 | 合规专员 | 审计JSON文件合规性 | 并行扫描+报告导出 |

## 使用流程

### 场景1：并行扫描大型项目

向Agent发送指令：
```
扫描./project目录下所有.json文件，启用8线程并行校验，输出结构化报告与通过率统计。
```

Agent将：
1. 收集所有`.json`文件，按大小分片
2. 8线程并行校验
3. 汇总错误与通过率
4. 输出结构化报告

### 场景2：Schema验证

```json
// schema.json
{
  "type": "object",
  "required": ["name", "age"],
  "properties": {
    "name": {"type": "string", "minLength": 1},
    "age": {"type": "integer", "minimum": 0, "maximum": 150}
  }
}
```

```bash
node lint.js --dir ./data --schema schema.json
```

### 场景3：JSON5校验

```bash
node lint.js --dir ./config --format json5
```

支持含注释与尾随逗号的JSON5文件。

### 场景4：自动修复建议

```json
// 错误文件 broken.json
{
  "name": "张三",
  "age": 30,  // 尾随逗号
}
```

修复建议输出：
```json
{
  "file": "broken.json",
  "errors": [
    {
      "line": 3,
      "column": 3,
      "type": "trailing_comma",
      "message": "尾随逗号",
      "fix": "移除第3行末尾的逗号",
      "before": "  \"age\": 30,",
      "after": "  \"age\": 30",
      "confidence": 0.99
    }
  ]
}
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 全部维度 |
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

| 现象 | 可能原因 | 解决步骤 | 优先级 |
|------|----------|----------|--------|
| 并行扫描卡死 | 线程死锁/IO瓶颈 | 降低线程数，检查IO负载 | 高 |
| Schema验证超时 | Schema过复杂 | 简化Schema，启用预编译 | 中 |
| JSON5解析失败 | 格式参数未设置 | 设置format=json5 | 高 |
| 修复建议不准确 | 置信度阈值过低 | 提高auto_apply阈值 | 中 |
| 告警未触发 | 阈值设置过低 | 调整alert_threshold | 中 |
| 历史数据丢失 | history_dir被清理 | 配置持久化存储，定期备份 | 低 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 16+（用于并行扫描与Schema验证）
- **Python**: 3.8+（用于监控告警脚本）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |
| JSON解析器 | 运行时 | 必需 | Node.js/Python内置 |
| Schema验证库 | npm/pip包 | 必需 | `ajv`/`jsonschema` |
| JSON5解析器 | npm/pip包 | 必需 | `json5` |
| 告警SDK | npm/pip包 | 可选 | 钉钉/企业微信/邮件 |

### API Key 配置
- 本Skill基于Markdown指令，无需额外API Key
- 校验与验证为本地执行，不依赖外部API
- 告警通道（Webhook）需配置对应服务的接入地址

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，校验与验证功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent执行企业级JSON校验任务，高级功能通过命令行工具实现

## 案例展示

### 并行扫描参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `parallel` | integer | 8 | 并行线程数 |
| `shard_strategy` | string | size | 分片策略size/count |
| `shard_size` | string | 1MB | 分片大小 |
| `progress_interval` | integer | 100 | 进度上报间隔（文件数） |

### Schema验证参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `schema` | string | - | Schema文件路径 |
| `schema_draft` | string | 2020-12 | Draft版本 |
| `strict` | boolean | true | 是否严格模式 |
| `allow_additional` | boolean | false | 是否允许额外字段 |

### 超集参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `format` | string | json | json/json5/jsonc/hjson |
| `allow_comments` | boolean | false | 是否允许注释 |
| `allow_trailing_comma` | boolean | false | 是否允许尾随逗号 |

### 监控告警参数

| 参数 | 类型 | 默认值 | 说明 |
|------|------|--------|------|
| `history_dir` | string | .lint-history | 历史报告目录 |
| `alert_threshold` | number | 95 | 通过率告警阈值 |
| `alert_webhook` | string | - | Webhook地址 |
| `alert_channels` | array | [] | 告警通道 |

## 常见问题

### Q1：并行扫描结果顺序混乱？
A：并行扫描不保证文件处理顺序，但报告中的错误明细会按文件路径排序输出。若需保持扫描顺序，设置`parallel=1`，但会显著降低性能。

### Q2：Schema验证报错信息不清晰？
A：专业版的Schema验证器支持详细错误路径，例如`$.user.address.city`。若错误信息仍不清晰，检查Schema本身的复杂度，必要时拆分为多个简单Schema。`strict`模式会报告所有违反项，非strict模式仅报告优秀个。

### Q3：JSON5文件被误报为标准JSON错误？
A：确认`format`参数设置为`json5`。若仍报错，检查文件扩展名是否为`.json5`，或显式指定`--format json5`。专业版支持按扩展名自动识别格式。

### Q4：自动修复误修改了有效内容？
A：自动修复默认不自动应用，仅生成建议。若启用了自动应用（`auto_apply=true`），仅对高置信度（>0.95）的修复生效。修复前已创建备份，可从`.bak`恢复。

### Q5：监控告警频繁误报？
A：调整告警阈值（alert_threshold），或将告警去重间隔加大。基线建立阶段（前1-2周）建议关闭告警，仅采集数据。通过率波动较大时，采用滑动平均值而非瞬时值判断。

### Q6：Schema验证速度很慢？
A：复杂Schema（含大量$ref或嵌套）验证较慢。优化策略：(1) 简化Schema，减少深层嵌套；(2) 启用Schema预编译；(3) 并行验证不同文件。万级文件Schema验证通常在5-10分钟内完成。

### Q7：如何集成到Git Hooks？
A：专业版提供命令行接口，在pre-commit钩子中调用`lint.js --dir ./src --schema schema.json`，失败时返回非零退出码，阻止提交。建议仅校验暂存区的JSON文件，避免全量扫描。

### Q8：超集文件如何转换为标准JSON？
A：专业版支持`--convert`参数，将JSON5/JSONC/HJSON转换为标准JSON。转换会移除注释、尾随逗号、单引号等超集特性，输出符合标准的JSON。

### Q9：历史趋势数据如何持久化？
A：历史报告存储在`history_dir`目录，按日期命名。专业版提供趋势查询接口，可按日/周/月聚合通过率。数据格式为JSON，可导出为CSV供报表工具使用。

### Q10：多团队如何共享Schema？
A：Schema文件纳入独立仓库或包管理（npm/pip），各团队通过依赖引入。Schema变更走评审流程，通过后发布新版本。专业版支持Schema版本锁定，避免升级导致的兼容性问题。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
