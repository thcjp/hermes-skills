---
slug: "anygen-diagram"
name: "anygen-diagram"
version: "1.0.0"
displayName: "AnyGen图表生成-专业版"
summary: "企业级图表生成工具,支持批量生成、自定义模板、团队协作与API集成,适配商业文档生产。"
license: "Proprietary"
edition: "pro"
description: |-
  AnyGen图表生成专业版,面向企业团队与专业用户的高级图表与可视化结构生成工具。核心能力:
  - 批量图表生成,支持多描述队列处理
  - 自定义图表模板库,统一团队风格
  - 团队协作与图表资产管理
  - API 集成,可嵌入文档生成系统
  - 多格式输出(PNG/SVG/PDF/Markdown)
  - 优先渲染队列与企业级技术支持

  适用场景:
  - 技术文档批量配图生产
  - 企业架构图标准化管理
  - 产品文档图表自动生成
  - 团队知识库可视化资产沉淀

  差异化:专业版在免费版基础上扩展批量生成、自定义模板、...
tags:
  - Creative
  - 图表生成
  - 企业版
  - 商业内容
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
---
# AnyGen图表生成-专业版

## 核心能力

| 能力项 | 免费版 | 专业版 | 说明 |
|:-------|:-------|:-------|:-----|
| 自然语言生成图表 | 是 | 是 | 描述即出图 |
| 流程图/架构图/组织图 | 是 | 是 | 多类型支持 |
| 服务端渲染 | 是 | 是 | 高质量输出 |
| 简单认证 | 是 | 是 | 浏览器/Key |
| 批量生成 | 否 | 是 | 多描述队列 |
| 自定义模板 | 否 | 是 | 统一团队风格 |
| 团队协作 | 否 | 是 | 资产共享 |
| API 集成 | 否 | 是 | 程序化调用 |
| 多格式输出 | 限制 | 是 | PNG/SVG/PDF/MD |
| 渲染优先级 | 普通 | 高优先 | 企业级保障 |
| 技术支持 | 社区 | 专属 | 工单响应 |
### 能力项

执行能力项操作,处理用户输入并返回结果。

**输入**: 用户提供能力项所需的参数和指令。

**输出**: 返回能力项的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`能力项`相关配置参数进行设置
### 自然语言生成图表

执行自然语言生成图表操作,处理用户输入并返回结果。

**输入**: 用户提供自然语言生成图表所需的参数和指令。

**输出**: 返回自然语言生成图表的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`自然语言生成图表`相关配置参数进行设置
### 流程图/架构图/组织图

执行流程图/架构图/组织图操作,处理用户输入并返回结果。

**输入**: 用户提供流程图/架构图/组织图所需的参数和指令。

**输出**: 返回流程图/架构图/组织图的处理结果。- 验证执行结果，确认输出符合预期格式
- 参考`流程图/架构图/组织图`相关配置参数进行设置
#
## 适用场景

### 场景一:技术文档批量配图

技术写作团队需为一批文档批量生成架构图与流程图。

```python
# 批量生成图表
python3 scripts/batch_diagram.py \
  --input ./diagram_specs/ \
  --output ./diagrams/ \
  --format svg \
  --parallel 5

# diagram_specs/ 目录下放置多个描述文件(JSON)
# 示例
# {
#   "name": "microservice_arch",
#   "description": "微服务架构图:前端→API网关→[用户/订单/支付]服务→数据库",
#   "template": "enterprise_arch",
#   "format": "svg"
# }
```

### 场景二:企业架构图标准化

企业需统一各部门架构图的视觉风格,使用自定义模板库。

```bash
# 创建自定义模板
python3 scripts/create_template.py \
  --name "enterprise_arch" \
  --style "企业标准风格" \
  --colors "#1a365d,#2b6cb0,#63b3ed" \
  --fonts "Noto Sans CJK SC" \
  --output ./templates/

# 应用模板生成图表
anygen smart_draw "企业IT架构图" \
  --template enterprise_arch \
  --output ./diagrams/it_arch.svg
```

### 场景三:产品文档图表自动生成

产品团队需将 PRD 中的流程描述自动转化为图表。

```bash
# 从 PRD 文档提取描述并生成图表
python3 scripts/prd_to_diagram.py \
  --input ./prd/user_flow.md \
  --extract "流程图描述" \
  --template product_flow \
  --output ./diagrams/user_flow.svg

# API 集成到文档系统
curl -X POST https://api.anygen.io/v1/diagrams \
  -H "Authorization: Bearer $ANYGEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "description": "用户注册流程:填写信息→验证邮箱→完善资料→完成注册",
    "template": "product_flow",
    "format": "svg"
  }'
```

### 场景四:团队图表资产管理

团队需将优质图表沉淀为可复用资产,使用团队协作功能。

```bash
# 提交图表到团队资产库
python3 scripts/diagram_commit.py \
  --file ./diagrams/microservice_arch.svg \
  --description "微服务标准架构图" \
  --tags "架构,微服务,标准" \
  --category "reference"

# 团队成员搜索与复用
python3 scripts/diagram_search.py \
  --query "微服务架构" \
  --category "reference"

# 拉取团队最新模板
python3 scripts/template_pull.py \
  --remote team-repo \
  --branch main
```

## 使用流程

### 优秀步:配置企业 API Key

```bash
# 企业版认证
anygen auth login --api-key sk-pro-详情见说明
export ANYGEN_API_KEY=sk-pro-详情见说明
export ANYGEN_EDITION=pro
```

### 第二步:执行批量生成

```bash
python3 scripts/batch_diagram.py \
  --input ./specs/ \
  --output ./diagrams/ \
  --format svg \
  --parallel 5
```

### 第三步:归档与分发

```bash
# 归档到团队资产库
python3 scripts/diagram_commit.py \
  --input ./diagrams/ \
  --message "批量生成技术文档配图"
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
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
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持 SKILL.md 的任意 AI Agent(Claude Code / Cursor / Codex / Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux
- **运行时**: AnyGen CLI + Python 3.9+

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| AnyGen Pro API | 外部 API | 必需 | 企业服务渠道申请 |
| AnyGen CLI | 命令行工具 | 必需 | 官方安装 |
| Python 3.9+ | 脚本运行 | 必需 | 官方安装 |
| Git | 版本控制 | 必需 | 系统自带 |
| anygen-workflow-generate | 工作流技能 | 必需 | anygen skill install |

### API Key 配置
- **环境变量名**: `ANYGEN_API_KEY`(企业版 Key)
- **附加变量**: `ANYGEN_EDITION=pro`
- **获取方式**: 通过企业服务渠道申请,享有高优先级渲染队列
- **安全建议**: 使用密钥管理服务存储 Key,团队仓库使用 SSH 密钥认证
- **认证方式**: 支持 API Key、浏览器授权两种方式

### 可用性分类
- **分类**: MD+EXEC(纯 Markdown 指令,核心功能需要 exec 命令行执行能力)
- **说明**: 基于Markdown的AI Skill,支持批量生成、自定义模板、团队协作等企业级图表生产场景

## 案例展示

### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```

### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```

## 常见问题

### Q1:专业版与免费版是否兼容?
A:完全兼容。专业版支持免费版所有命令与认证方式,迁移时仅需更换 API Key 并设置 `ANYGEN_EDITION=pro`。

### Q2:批量生成支持多少图表?
A:单批最多 50 个图表,并发数 1-10 可调。大批量建议分批处理。

### Q3:自定义模板如何创建?
A:通过 `create_template` 脚本定义模板名称、风格、颜色、字体等,保存到团队模板库。生成图表时通过 `--template` 参数应用。

### Q4:多格式输出如何选择?
A:网页展示用 SVG(可缩放),文档嵌入用 PNG(通用),印刷归档用 PDF(正式),文档源码用 Markdown(可版本控制)。

### Q5:团队协作支持多少人?
A:License 绑定团队席位,支持 5-50 人团队(视授权规模)。支持资产共享、模板管理与权限控制。

### Q6:能否集成到 CI/CD 流水线?
A:可以。通过 API 可集成到文档构建流水线,实现 PRD/Markdown 文档变更→图表自动重新生成→文档发布的自动化流程。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要API Key，无Key环境无法使用
