---
slug: api-doc-generator-pro
name: api-doc-generator-pro
version: "1.0.0"
displayName: API文档生成器(专业版)
summary: 企业级API文档平台，含代码扫描、多格式导出、版本管理、Mock联动与团队评审。
license: Proprietary
edition: pro
description: |-
  API文档生成器专业版是面向研发团队的全功能API文档平台。在免费版的自然语言→OpenAPI+Markdown双产出基础上，解锁代码仓库自动扫描、多格式导出、文档版本管理、Mock服务器联动、团队评审协作、GraphQL Schema生成、自定义模板引擎、多语言文档八大高级能力，覆盖从代码到文档到 Mock再到评审的完整闭环
tags:
- API文档
- OpenAPI
- 代码扫描
- 团队协作
- 文档治理
tools:
  - - read
- exec
# API文档生成器（专业版）
---
> **从"写文档"到"文档即基础设施"。代码扫描+版本管理+Mock联动+团队评审，企业级API文档平台。**

API文档生成器专业版把免费版的"个人起草工具"升级为"团队级API文档平台"。除了自然语言→OpenAPI+Markdown双产出、RESTful规范校验、状态码模板三大基础能力外，专业版解锁八大高级能力：代码仓库自动扫描、多格式导出、文档版本管理、Mock服务器联动、团队评审协作、GraphQL Schema生成、自定义模板引擎、多语言文档。覆盖从代码到文档到Mock再到评审的完整闭环。

> 详细内容已移至 `references/detail.md` - ## 架构总览
## 快速开始
### 基础搭建（<60秒）：继承免费版能力
专业版完全兼容免费版的所有生成能力。首次使用时，直接对Agent说：

Agent会按免费版的规则生成YAML与Markdown，并额外提示：是否要从代码仓库扫描已有接口？

### 标准搭建（<120秒）：扫描代码仓库生成文档
```bash
api-doc scan --lang go --path ./src --output ./openapi.yaml

api-doc scan --lang java --path ./src/main/java --output ./openapi.yaml

api-doc scan --lang python --path ./app --output ./openapi.yaml

api-doc scan --lang nodejs --path ./routes --output ./openapi.yaml
```

扫描结果自动生成OpenAPI Spec，并标注哪些接口缺注释、哪些字段类型推断不确定需人工确认。

### 完整搭建（<300秒）：启用版本管理与Mock联动
```bash
api-doc init-repo --remote git@your-git-server:team/api-docs.git

api-doc generate --from ./openapi.yaml --tag v1.2.0

api-doc mock start --spec ./openapi.yaml --port 8080

api-doc collab enable --reviewers @zhang,@li
```

## 核心功能
### 功能1：代码仓库自动扫描
**解决痛点**：老项目接口散落在代码各处，手动整理文档既慢又容易漏。

**专业版能力**：支持四种语言的注解扫描，自动提取路由、参数、返回类型。

| 语言 | 框架 | 扫描依据 | 示例注解 |
|------|------|----------|----------|
| Go | gin/echo | 路由注册+struct tag | `@Summary 创建用户` |
| Java | Spring | `@RestController`+`@RequestMapping` | `@ApiOperation` |
| Python | FastAPI/Flask | 装饰器+类型注解 | `@app.route`+Pydantic |
| Node.js | Express/Koa | 路由定义+Joi schema | `router.post` |

**扫描输出**：
- 完整OpenAPI Spec（YAML）
- 扫描报告：已识别接口数、缺注释接口、类型不确定字段
- 建议清单：哪些接口需补注释、哪些字段需显式标注类型

```bash
api-doc scan --lang java --path ./src --output ./openapi.yaml --report ./scan-report.html

SCAN REPORT
===========
Total Endpoints: 47
Documented:      32 (68%)
Undocumented:    15 (32%)
Type Uncertain:  8 fields

Endpoints Needing Comments:
1. POST /api/v1/orders - 缺@ApiOperation
2. GET /api/v1/users/{id} - 缺返回类型说明
...
```

### 功能2：多格式导出
**解决痛点**：不同角色要看不同格式——开发要YAML，产品要HTML，客户要PDF。

**专业版能力**：一键导出五种格式。

```bash
api-doc export --spec ./openapi.yaml --format yaml --output ./openapi.yaml
api-doc export --spec ./openapi.yaml --format json --output ./openapi.json
api-doc export --spec ./openapi.yaml --format html --output ./docs/index.html
api-doc export --spec ./openapi.yaml --format pdf --output ./docs/api.pdf
api-doc export --spec ./openapi.yaml --format swagger-ui --output ./swagger-ui/
```

| 格式 | 用途 | 特点 |
|------|------|------|
| YAML | 开发导入工具 | 结构化，可版本化 |
| JSON | 程序化处理 | 便于脚本解析 |
| HTML | 在线文档门户 | 响应式，可搜索 |
| PDF | 客户交付/归档 | 排版精美，带目录 |
| Swagger UI单页 | 交互式调试 | 可直接发请求测试 |

### 功能3：文档版本管理与diff
**解决痛点**：接口改了字段，文档也改了，但没人记得上次长啥样，无法追溯。

**专业版能力**：文档纳入Git版本化，支持字段级diff。

```bash
api-doc commit --message "新增订单查询接口" --tag v1.3.0

api-doc diff v1.2.0 v1.3.0

DIFF: v1.2.0 → v1.3.0
=====================
[ADDED]   POST /api/v1/orders/search - 订单搜索接口
[MODIFIED] GET /api/v1/users/{id}
  - response.data.phone: type string → string|null (允许空)
  - response.data.avatar: NEW FIELD
[DEPRECATED] GET /api/v1/users/legacy - 将在v2.0移除
[REMOVED]  DELETE /api/v1/users/batch - 批量删除接口已下线
```

### 功能4：Mock服务器联动
**解决痛点**：文档写完了，Mock还得另起一套，两边不同步。

**专业版能力**：文档即Mock，Spec变更Mock自动更新。

```bash
api-doc mock start --spec ./openapi.yaml --port 8080

api-doc mock reload  # 无需重启
curl http://localhost:8080/api/v1/users?mock_scenario=empty    # 空列表
curl http://localhost:8080/api/v1/users?mock_scenario=error    # 错误响应
curl http://localhost:8080/api/v1/users?mock_delay=2000        # 慢响应
```

### 功能5：团队评审与协作
**解决痛点**：接口文档谁都能改，改完没人审，字段命名混乱。

**专业版能力**：PR评审流程，评论与@提及，变更通知。

> 详细代码示例已移至 `references/detail.md`

> 详细内容已移至 `references/detail.md` - ### 功能6：GraphQL Schema生成
### 功能7：自定义模板引擎
**解决痛点**：每个公司的文档模板不同，统一工具产出的格式不合公司规范。

**专业版能力**：基于模板引擎自定义文档结构。

```bash
api-doc generate --spec ./openapi.yaml --template ./templates/company.md.tpl

版本：{{version}}  日期：{{date}}
{% for path in paths %}
**接口**：{{path.method}} {{path.path}}
{% endfor %}
```

### 功能8：多语言文档
**解决痛点**：国际化团队需要中英双语文档，手动维护两份不同步。

**专业版能力**：一次生成，中英双语对照。

```bash
api-doc generate --spec ./openapi.yaml --bilingual --output ./docs/
```

## 使用场景
### 场景一：企业级API文档治理（技术负责人角色）
**痛点**：团队接口文档散落在Confluence、飞书、代码注释各处，版本混乱，新人找不到权威文档。

**专业版方案**：
1. 用 `api-doc scan` 扫描所有微服务代码仓库，统一生成OpenAPI Spec
2. 所有Spec集中纳管到文档版本库，按服务+版本组织
3. 启用团队评审，接口变更必须PR评审通过才能合并
4. 启用Mock联动，前端直接基于文档开发
5. 导出HTML门户，作为团队唯一权威文档入口

**效果**：文档从"散落各处"变为"单一权威源"，新人上手时间从3天降至半天。

### 场景二：前后端并行开发（前端+后端角色）
**痛点**：前端等后端文档才能开工，后端写完代码才想起来写文档。

**专业版方案**：
1. 后端先写OpenAPI Spec（哪怕只有字段定义）并提交PR
2. 评审通过后，前端用 `api-doc mock start` 启动Mock开发
3. 后端实现代码时用 `api-doc scan` 校验实现是否符合Spec
4. 后端代码合入时，CI自动扫描Spec与代码一致性，不一致则拦截
5. 前端切换到真实API时，用文档diff确认无破坏性变更

**效果**：前后端真正并行，整体交付周期缩短约30%。

### 场景三：对外开放API门户（平台/产品角色）
**痛点**：要做对外开放API，需要给客户一套专业文档门户，但维护成本高。

**专业版方案**：
1. 内部Spec作为唯一源，`api-doc export --format html` 生成门户
2. `api-doc export --format pdf` 生成客户交付文档
3. `api-doc export --format swagger-ui` 生成可调试的交互文档
4. 多语言文档支持国际客户（`--bilingual`）
5. 版本管理支持多版本并存（v1/v2同时在线）

**效果**：对外开放API门户从"专人维护"变为"Spec驱动自动生成"，维护成本降低70%。

### 场景四：多语言代码仓库统一文档（架构师角色）
**痛点**：微服务架构下，Go/Java/Python/Node.js服务各写各的，文档格式不统一。

**专业版方案**：
1. 每个服务用对应语言的 `api-doc scan` 扫描生成OpenAPI Spec
2. 所有Spec汇聚到统一文档库
3. 统一导出为HTML门户，按服务模块组织
4. 跨服务接口依赖关系自动绘制调用图
5. 字段命名规范统一校验（如全用snake_case或camelCase）

**效果**：异构技术栈的API文档统一治理，跨服务联调效率提升。

### 场景五：接口评审与规范落地（技术负责人角色）
**痛点**：接口命名规范、状态码规范定了没人执行，评审靠口头。

**专业版方案**：
1. 规范固化为 `api-doc lint` 规则集
2. 接口PR触发自动lint，不规范直接拦截
3. 评审流程要求至少1人approve
4. 评审评论沉淀在文档历史中，可追溯
5. 定期出规范执行报告，识别高频违规项

**效果**：接口规范从"口头约定"变为"工具强制"，规范落地率从30%提升至90%。

## 不适用场景

以下场景API文档生成器(专业版)不适合处理：

- 专业医学法律翻译认证
- 同声传译
- 文学创作翻译


## 触发条件

需要文本翻译、多语言转换、本地化处理时使用。不适用于非本工具能力范围的需求。


## 多角色场景指南
| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 前端开发 | 并行开发、Mock解耦 | Mock联动+多格式导出 | 不等后端即可开发 |
| 后端开发 | 代码即文档 | 代码扫描+版本管理 | 写代码即出文档 |
| 技术负责人 | 文档治理、规范落地 | 代码扫描+团队评审+lint | 单一权威源 |
| 平台/产品 | 对外API门户 | 多格式导出+多语言文档 | 专业门户自动生成 |
| 架构师 | 多语言仓库统一治理 | 代码扫描+版本管理+lint | 异构栈统一文档 |
| 测试工程师 | 文档→测试用例 | Mock联动+测试用例生成 | 文档即测试资产 |
| DevOps | 文档CI/CD | 代码扫描+lint+版本管理 | 文档流水线自动化 |

## 性能优化策略
### 代码扫描优化
1. **增量扫描**：只扫描Git变更文件，大型仓库扫描时间从分钟级降至秒级
2. **并行扫描**：多服务并行扫描，按CPU核数自动并行
3. **缓存机制**：AST解析结果缓存，未变更文件跳过
4. **忽略规则**：`.api-doc-ignore` 文件排除测试代码、mock代码

### 文档生成优化
1. **增量生成**：只重新生成变更的章节，全量文档生成时间减少80%
2. **模板预编译**：模板引擎预编译，生成时零解析开销
3. **按需加载**：大型API文档分章节生成，避免单文件过大
4. **并行导出**：多格式导出并行进行

### Mock服务器优化
1. **Spec缓存**：Mock启动时预生成响应，运行时零延迟
2. **热重载**：Spec变更后增量重载，不中断现有请求
3. **状态分区**：多场景Mock数据隔离
4. **惰性生成**：大响应体按需生成

### 版本管理优化
1. **Git LFS**：大型Spec文件用LFS存储，避免仓库膨胀
2. **差异压缩**：版本diff只存储变更部分
3. **历史归档**：旧版本自动归档，主分支只保留活跃版本
4. **按需拉取**：克隆时只拉取最新版本，历史按需获取

### 成本控制
- 代码扫描在CI Runner本地执行，不消耗云端资源
- Mock服务器本地运行，不消耗云端资源
- 文档门户静态托管，成本极低
- 团队评审按席位计费， inactive成员自动释放

## 多平台集成示例
### 与CI/CD集成

> 详细代码示例已移至 `references/detail.md`

### 与代码仓库集成
```bash
#!/bin/sh
api-doc scan --lang python --path ./app --output ./openapi.yaml
git add openapi.yaml

api-doc verify --spec ./openapi.yaml --path ./app || exit 1
```

### 与API网关集成
```bash
api-doc publish --spec ./openapi.yaml --target gateway --apply
```

### 与团队协作平台集成
```text
1. 文档PR创建 → 自动通知Slack/钉钉/飞书对应频道
2. 评审评论 → @提及对应成员
3. 文档合并 → 自动部署到文档门户
4. 破坏性变更 → 自动通知所有消费方团队
5. 版本发布 → 自动生成changelog并推送
```

## 版本升级迁移指南
### 从免费版升级至专业版
1. **无需迁移**：专业版完全兼容免费版的生成能力
2. **新增功能激活**：
   - 安装CLI：`npm install -g api-doc-generator-pro`
   - 初始化版本库：`api-doc init-repo --remote <git-url>`
   - 启用协作：`api-doc collab enable --reviewers @team`
3. **历史资产导入**：
   - 免费版生成的YAML/Markdown可直接导入版本库
   - 用 `api-doc import --from ./legacy-docs/` 批量导入
4. **指令兼容**：免费版的所有指令在专业版中均可使用

### 版本更新历史
| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含八大高级功能与团队协作 |

## 错误处理
| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| 代码扫描漏接口 | 注解不规范或框架不支持 | 检查注解格式，查看支持框架列表 | 高 |
| 扫描类型推断错误 | 代码缺类型注解 | 补充类型注解，或手动修正Spec | 中 |
| Mock响应与Spec不符 | Spec更新后未reload | 执行 `api-doc mock reload` | 中 |
| 文档导出PDF乱码 | 字体缺失 | 安装中文字体包，或用HTML转PDF | 中 |
| 版本diff误报 | YAML字段顺序变化 | 启用语义化diff（忽略顺序） | 低 |
| 评审通知未送达 | Webhook配置错或成员通知关闭 | 检查Webhook URL，确认成员通知设置 | 高 |
| 多语言文档翻译不准 | 机器翻译质量 | 启用人工校对流程，关键术语人工翻译 | 中 |
| 自定义模板渲染失败 | 模板语法错 | 用 `api-doc template lint` 校验模板 | 中 |
| 代码扫描慢 | 仓库过大或未增量 | 启用增量扫描，配置.ignore文件 | 中 |
| 文档门户访问慢 | 单文件过大 | 启用分章节生成，按需加载 | 低 |

## 即时修复清单
| 问题 | 修复方法 |
|------|----------|
| 扫描漏了新接口 | 检查新接口是否用了支持的注解 |
| Spec字段类型错 | 在代码中补类型注解，重新扫描 |
| Mock响应字段缺 | 检查Spec的response schema是否完整 |
| PDF中文字体丢失 | 安装Noto Sans CJK字体 |
| diff显示全是变化 | 启用语义化diff模式 |
| 评审@提及无效 | 确认成员已在协作空间注册 |
| 模板变量未渲染 | 检查变量名与Spec字段是否一致 |
| 门户搜索失效 | 重新生成索引 `api-doc index rebuild` |

## 维护命令

> 详细代码示例已移至 `references/detail.md`

## FAQ
### Q1：免费版与专业版有什么区别？
免费版聚焦"个人起草文档"，提供自然语言→OpenAPI+Markdown双产出、RESTful规范校验、状态码模板。专业版聚焦"团队级文档平台"，新增八大高级功能：代码扫描、多格式导出、版本管理、Mock联动、团队评审、GraphQL Schema、自定义模板、多语言文档。此外提供多角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。

### Q2：代码扫描支持哪些语言和框架？
支持四种语言的主流框架：
- Go：gin、echo、fiber
- Java：Spring Boot、Spring MVC
- Python：FastAPI、Flask、Django REST
- Node.js：Express、Koa、NestJS

不在列表中的框架可通过自定义扫描插件支持。

### Q3：扫描的准确率怎么样？
对于规范使用注解的代码，准确率约95%。主要误差来源：缺类型注解的动态语言（Python/Node.js）、自定义返回包装、泛型类型。扫描报告会标注"类型不确定"字段，建议人工确认。

### Q4：Mock联动和单独的Mock工具有什么区别？
Mock联动是"文档即Mock"——Spec是唯一源，Mock自动从Spec生成响应，Spec变更Mock热重载。单独Mock工具需要手动维护Mock数据，容易与文档不同步。专业版的Mock联动确保文档、Mock、实现三者一致。

### Q5：版本管理支持多版本并存吗？
支持。可以同时维护v1、v2多个版本的文档，每个版本独立URL访问。适合API升级过渡期，老客户用v1，新客户用v2。版本diff能识别破坏性变更，自动通知消费方。

### Q6：团队评审流程怎么配置？
可配置评审规则：必须评审人数（默认1人）、是否要求tech lead approve、自动分配reviewer策略。评审支持评论、@提及、行级评论。评审通过后自动合并并触发文档部署。

### Q7：多语言文档的翻译质量如何？
基础翻译用机器翻译，关键术语（如字段名、错误码）保留原文。建议启用人工校对流程，重要客户文档由人工翻译。专业版支持术语表，确保翻译一致性。

### Q8：自定义模板引擎用什么语法？
基于Jinja2语法（与Django/Flask模板一致），支持变量替换、条件判断、循环、过滤器。模板可继承，便于维护公司统一模板。提供模板lint工具校验语法。

### Q9：能在CI/CD中完全自动化吗？
可以。专业版CLI支持CI模式，提供GitHub Actions/GitLab CI/Jenkins集成示例。典型流水线：PR触发代码扫描→规范lint→破坏性变更检测→文档生成→部署门户。

### Q10：GraphQL Schema生成能导入到各GraphQL工具吗？
可以。生成的SDL完全符合GraphQL规范，可导入到Apollo Server、GraphiQL、Prisma、Hasura等工具。同时生成GraphQL Markdown文档，便于人工阅读。

### Q11：专业版支持私有化部署吗？
支持。文档版本库、Mock服务器、团队协作空间均可私有化部署到企业内网。代码扫描在本地执行，不上传代码。联系销售获取私有化部署包。

### Q12：文档门户支持搜索吗？
支持。HTML格式文档内置全文搜索，支持按模块、按接口名、按字段名搜索。大型API文档（100+接口）建议启用分章节生成，搜索性能更优。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（用于CLI工具）
- **Git**: 已安装（用于版本管理与团队协作）

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Node.js 18+ | 运行时 | 必需 | 从nodejs.org安装 |
| Git | 工具 | 版本管理必需 | 系统自带或从git-scm.com安装 |
| 中文字体 | 字体 | PDF导出必需 | 安装Noto Sans CJK |
| 代码仓库 | 源码 | 代码扫描必需 | 由团队维护 |

### API Key 配置
- 团队协作空间需配置团队Token：`api-doc collab login`
- 代码扫描在本地执行，不上传代码
- 所有Token通过环境变量配置，禁止硬编码
- 建议将Token存储在 `~/.api-doc/credentials/` 目录（已gitignore）

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成与治理API文档

## License与版权声明
本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：API文档助手（api-doc-writer）
- 原始license：MIT-0
- 改进作品：API文档生成器（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为面向研发团队的API文档平台
- 去除原始项目标识、外部仓库URL与原作者署名
- 新增八大高级功能（代码扫描、多格式导出、版本管理、Mock联动、团队评审、GraphQL Schema、自定义模板、多语言文档）
- 新增分级快速开始指南（基础/标准/完整三档）
- 新增五类真实场景示例（文档治理/并行开发/对外门户/多语言仓库/规范落地）
- 新增多角色场景指南（7种角色×场景映射）
- 新增性能优化策略与多平台集成示例
- 新增版本升级迁移指南
- 新增FAQ章节（12问）与故障排查表（10项）
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT-0 license允许使用、复制、修改和分发，无需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，符合MIT license要求。

## 专业版特性
本专业版相比免费版新增以下能力：

- **代码仓库自动扫描**：支持Go/Java/Python/Node.js四种语言的注解扫描，自动提取接口、参数、返回类型，生成OpenAPI Spec与扫描报告
- **多格式导出**：一键导出YAML/JSON/HTML/PDF/Swagger UI单页五种格式，满足开发、产品、客户、调试多角色需求
- **文档版本管理与diff**：文档纳入Git版本化，支持字段级diff、破坏性变更检测、多版本并存，文档变更可追溯
- **Mock服务器联动**：文档即Mock，Spec变更Mock热重载，支持场景切换与延迟注入，确保文档与Mock一致
- **团队评审与协作**：PR评审流程、评论@提及、变更通知、权限管理，接口规范从口头约定变为工具强制
- **GraphQL Schema生成**：从自然语言或GraphQL代码生成SDL与文档，支持导入到Apollo/Prisma/Hasura等工具
- **自定义模板引擎**：基于Jinja2语法的模板引擎，支持变量替换、条件、循环、继承，适配公司统一文档规范
- **多语言文档**：一次生成中英双语对照文档，支持术语表与人工校对流程，适配国际化团队

此外，专业版还提供：
- 多角色场景指南（前端/后端/技术负责人/平台产品/架构师/测试/DevOps）
- 性能优化策略（扫描/生成/Mock/版本/成本五维度）
- 多平台集成示例（CI-CD/代码仓库/API网关/协作平台）
- 版本升级迁移指南
- 扩展FAQ（12问）与故障排查表（10项）
- 优先支持

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | 自然语言→OpenAPI+Markdown+RESTful校验+状态码模板+基础示例+基础FAQ | 个人试用、轻量文档需求 |
| 收费专业版 | ¥29.9/月 | 全套八大高级功能+多角色指南+性能优化+多平台集成+优先支持 | 团队/企业、文档治理平台 |

专业版通过SkillHub SkillPay发布。

## 已知限制
- 需要API Key，无Key环境无法使用
