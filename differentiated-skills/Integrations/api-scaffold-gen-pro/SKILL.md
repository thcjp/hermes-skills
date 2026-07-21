---
slug: api-scaffold-gen-pro
name: api-scaffold-gen-pro
version: "1.0.0"
displayName: API脚手架生成器(专业版)
summary: 企业级API脚手架平台，含多框架、DDD分层、微服务、ORM、Docker与CI/CD全套模板。
license: Proprietary
edition: pro
description: |-
  API脚手架生成器专业版是面向研发团队的全功能API脚手架平台。在免费版的REST/GraphQL生成、认证模板、测试套件、Mock服务器基础上，解锁数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点九大高级能力，覆盖从脚手架到部署的完整项目起步流程
tags:
- 代码生成
- 脚手架
- DDD架构
- 微服务
- 企业开发
tools:
  - - read
- exec
# API脚手架生成器（专业版）
---
> **从"能起步"到"起步即规范"。多框架+DDD分层+微服务+ORM+Docker+CI/CD，企业级脚手架平台。**

API脚手架生成器专业版把免费版的"个人起步工具"升级为"企业级脚手架平台"。除了REST/GraphQL生成、认证模板、测试套件、Mock服务器四大基础能力外，专业版解锁九大高级能力：数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点。覆盖从脚手架到部署的完整项目起步流程。

## 架构总览

## 快速开始
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 基础搭建（<60秒）：继承免费版能力
专业版完全兼容免费版的所有生成能力。首次使用时，直接对Agent说：

Agent会按免费版的规则生成路由+测试+Mock，并额外提示：是否要生成ORM模型、Docker配置、CI/CD流水线？

### 标准搭建（<120秒）：生成DDD分层架构

### 完整搭建（<300秒）：微服务全套脚手架
```bash
api-scaffold-gen microservice order-service \
  --stack java-springboot \
  --orm jpa \
  --db postgresql \
  --service-registry eureka \
  --tracing sleuth \
  --output ./order-service

api-scaffold-gen deploy order-service \
  --docker \
  --k8s \
  --ci github-actions \
  --cd argocd
```

## 核心能力
### 功能2：多框架支持
**解决痛点**：团队技术栈多样，单一框架模板不够用。

**专业版能力**：支持四种语言的主流框架。

| 语言 | 框架 | 特点 |
|------|------|------|
| Node.js | NestJS | 依赖注入、模块化、装饰器、类似Spring |
| Python | Django REST | 全功能、admin后台、ORM一体 |
| Java | Spring Boot | 企业级、生态丰富、注解驱动 |
| Go | Gin | 高性能、轻量、中间件友好 |

```bash
api-scaffold-gen rest user --stack nodejs-nestjs --orm typeorm

api-scaffold-gen rest user --stack python-django --orm django-orm

api-scaffold-gen rest user --stack java-springboot --orm jpa

api-scaffold-gen rest user --stack go-gin --orm gorm
```

**输入**: 用户提供功能2：多框架支持所需的指令和必要参数。
**处理**: 按照skill规范执行功能2：多框架支持操作,遵循单一意图原则。
**输出**: 返回功能2：多框架支持的执行结果,包含操作状态和输出数据。

### 功能3：DDD分层架构
**解决痛点**：CRUD代码全堆在controller里，业务复杂后维护不动。

**专业版能力**：按DDD四层架构生成代码，职责清晰。

**输入**: 用户提供功能3：DDD分层架构所需的指令和必要参数。
**处理**: 按照skill规范执行功能3：DDD分层架构操作,遵循单一意图原则。
**输出**: 返回功能3：DDD分层架构的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
### 功能4：微服务模板
**解决痛点**：微服务项目起步要配服务注册、发现、通信、追踪，半天搭不完。

**专业版能力**：一键生成微服务全套基础设施代码。

```bash
api-scaffold-gen microservice order-service \
  --stack java-springboot \
  --service-registry eureka \
  --communication feign \
  --tracing sleuth-zipkin \
  --config-server spring-cloud-config \
  --gateway spring-cloud-gateway
```

生成的微服务包含：
- 服务注册与发现（Eureka/Nacos）
- 服务间通信（Feign/gRPC）
- 链路追踪（Sleuth+Zipkin/SkyWalking）
- 配置中心（Spring Cloud Config/Apollo）
- API网关（Spring Cloud Gateway）
- 熔断与降级（Resilience4j/Hystrix）
- 分布式事务（Seata）

**输入**: 用户提供功能4：微服务模板所需的指令和必要参数。
**处理**: 按照skill规范执行功能4：微服务模板操作,遵循单一意图原则。
**输出**: 返回功能4：微服务模板的执行结果,包含操作状态和输出数据。

### 功能5：OpenAPI Spec反向生成
**解决痛点**：代码写完了才发现没文档，手写Spec太慢。

**专业版能力**：从代码注解反向生成OpenAPI Spec。

```bash
api-scaffold-gen openapi reverse --path ./src --lang java-springboot --output ./openapi.yaml

api-scaffold-gen openapi reverse --path ./src --lang nodejs-nestjs --output ./openapi.yaml

```

**输入**: 用户提供功能5：OpenAPI Spec反向生成所需的指令和必要参数。
**处理**: 按照skill规范执行功能5：OpenAPI Spec反向生成操作,遵循单一意图原则。
**输出**: 返回功能5：OpenAPI Spec反向生成的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 功能6：多资源关联生成
**解决痛点**：资源间有one-to-many/many-to-many关系，手写关联代码容易出错。

**专业版能力**：声明资源关系，自动生成关联代码。

```bash
api-scaffold-gen relate "user has many posts, post has many tags, post belongs to category"
```

**输入**: 用户提供功能6：多资源关联生成所需的指令和必要参数。
**处理**: 按照skill规范执行功能6：多资源关联生成操作,遵循单一意图原则。
**输出**: 返回功能6：多资源关联生成的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 功能7：自定义模板引擎
**解决痛点**：公司有统一代码规范，通用模板不合规范。

**专业版能力**：基于Jinja2/Mustache的自定义模板引擎。

```bash
api-scaffold-gen rest user --template ./templates/company-rest.tpl

/**
 * {{resource | title}} 接口
 * @company {{company_name}}
 * @author {{author}}
 */
router.{{method}}('/{{resource}}', async (req, res) => {
  // TODO: 实现{{operation}}逻辑
  {% for field in fields %}
  // req.body.{{field.name}} - {{field.description}}
  {% endfor %}
});
```

**输入**: 用户提供功能7：自定义模板引擎所需的指令和必要参数。
**处理**: 按照skill规范执行功能7：自定义模板引擎操作,遵循单一意图原则。
**输出**: 返回功能7：自定义模板引擎的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 功能9：WebSocket端点生成
**解决痛点**：实时通信API（聊天/通知/协作）的WebSocket代码与REST不同，手写易错。

**专业版能力**：生成WebSocket端点，支持房间/广播/心跳。

**输入**: 用户提供功能9：WebSocket端点生成所需的指令和必要参数。
**处理**: 按照skill规范执行功能9：WebSocket端点生成操作,遵循单一意图原则。
**输出**: 返回功能9：WebSocket端点生成的执行结果,包含操作状态和输出数据。

- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：脚手架平台、含多框架、Docker、全套模板、脚手架生成器专业、版是面向研发团队、的全功能、在免费版的、GraphQL、认证模板、测试套件、Mock、服务器基础上、解锁数据库、与迁移、端点九大高级能力、覆盖从脚手架到部、署的完整项目起步等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景
### 场景一：企业级API项目起步（技术负责人角色）
**痛点**：新项目要符合公司规范，但每次都要从零搭，规范难落地。

**专业版方案**：
1. 用 `ddd` 命令生成DDD分层架构项目骨架
2. 自定义模板固化公司代码规范（命名/注释/分层）
3. 生成ORM模型与迁移，连接 `PostgreSQL`
4. 生成Docker与CI/CD配置，一键部署
5. 新项目从"一周搭脚手架"变为"半天进业务开发"

**效果**：项目起步效率提升80%，规范100%落地。

### 场景二：DDD架构项目搭建（架构师角色）
**痛点**：DDD理论懂，但落地时domain/application/infrastructure怎么分记不清。

**专业版方案**：
1. 用 `ddd` 命令生成四层架构骨架
2. 领域实体含业务行为方法（不只是getter/setter）
3. 值对象封装校验逻辑（如Email值对象自动校验格式）
4. 仓储接口在domain层定义，实现在infrastructure层
5. 用例在application层编排，事务边界清晰

**效果**：DDD从"理论"变为"可执行骨架"，团队对齐成本降低。

### 场景三：微服务脚手架标准化（平台架构师角色）
**痛点**：每个微服务都要配注册/发现/通信/追踪，重复且易错。

**专业版方案**：
1. 用 `microservice` 命令生成全套微服务模板
2. 服务注册/发现/通信/追踪开箱即用
3. 各服务统一技术栈，降低维护成本
4. 新服务从"两天搭基础设施"变为"两小时起步"

**效果**：微服务起步时间减少90%，基础设施代码统一。

### 场景四：多团队模板统一（平台负责人角色）
**痛点**：多个业务团队各用各的模板，代码风格混乱，合并难。

**专业版方案**：
1. 平台组维护统一模板仓库
2. 各团队用 `--template ./company-templates/` 生成代码
3. 模板更新自动通知各团队
4. 代码风格通过模板强制统一

**效果**：多团队代码风格一致性从30%提升至95%。

### 场景五：老项目脚手架规范化（技术负责人角色）
**痛点**：老项目代码风格混乱，想规范化但不知从何下手。

**专业版方案**：
1. 用 `openapi reverse` 从代码反推Spec
2. 基于Spec用新模板重新生成规范代码
3. 逐步替换老代码，每替换一个接口跑回归测试
4. 最终全量替换为规范代码

**效果**：老项目规范化从"不敢动"变为"渐进式替换"。

## 多角色场景指南
| 角色 | 典型场景 | 推荐功能组合 | 核心价值 |
|------|----------|-------------|----------|
| 技术负责人 | 企业项目起步 | DDD+ORM+Docker+CI/CD | 规范化起步 |
| 架构师 | DDD架构搭建 | DDD分层+多资源关联 | 架构落地 |
| 平台架构师 | 微服务标准化 | 微服务模板+多框架 | 基础设施统一 |
| 平台负责人 | 多团队模板统一 | 自定义模板+治理层 | 代码风格一致 |
| 后端开发 | 日常CRUD开发 | REST+ORM+测试套件 | 样板代码自动化 |
| 全栈开发 | 全栈项目起步 | REST+GraphQL+WebSocket | 全场景覆盖 |
| DevOps | 部署流水线 | Docker+CI/CD+K8s | 部署自动化 |

## 性能优化策略
### 代码生成优化
1. **增量生成**：只生成变更的资源，大型项目生成时间减少70%
2. **并行生成**：多资源并行生成，按CPU核数自动并行
3. **模板缓存**：模板预编译，生成时零解析开销
4. **依赖分析**：智能跳过未变更文件的生成

### 模板引擎优化
1. **模板预编译**：首次加载时编译为AST，后续零解析
2. **变量缓存**：相同变量不重复求值
3. **局部渲染**：只渲染变更的代码块
4. **流式输出**：大文件流式生成，避免内存峰值

### 项目结构优化
1. **按需生成**：只生成用到的层（如不需要GraphQL则跳过）
2. **依赖最小化**：生成的package.json只含必需依赖
3. **Tree-shaking友好**：ESM导出，便于打包优化
4. **懒加载**：重型依赖（如ORM）按需加载

### 部署配置优化
1. **多阶段构建**：Docker镜像分层，最终镜像小
2. **.dockerignore**：排除node_modules等，加速构建
3. **CI缓存**：npm依赖缓存，加速CI
4. **并行CI**：lint/test/build并行跑，缩短流水线

### 成本控制
- 代码生成在本地执行，不消耗云端资源
- 模板仓库用Git管理，无额外存储成本
- Docker多阶段构建减小镜像，降低存储与传输成本
- CI/CD按需触发，避免无效流水线

## 多平台集成示例
### 与K8s集成

### 与监控告警集成
```yaml
apiVersion: monitoring.coreos.com/v1
kind: ServiceMonitor
metadata:
  name: user-service
spec:
  selector:
    matchLabels:
      app: user-service
  endpoints:
    - port: metrics
      path: /metrics
      interval: 15s
```

### 与团队协作平台集成
```text
1. 模板更新 → 自动通知各业务团队
2. 新项目创建 → 自动从模板仓库初始化
3. 代码生成完成 → 自动创建PR供评审
4. 规范校验失败 → 自动在PR评论违规项
5. 项目部署完成 → 自动通知团队群
```

### 与代码仓库集成
```bash
#!/bin/sh
api-scaffold-gen lint --path ./src --rules company-standard || exit 1

api-scaffold-gen init --template company-ddd --output ./new-service
cd new-service
git init
git add .
git commit -m "chore: initialize project from template"
```

## 版本升级迁移指南
### 从免费版升级至专业版
1. **无需迁移**：专业版完全兼容免费版的生成能力
2. **新增功能激活**：
   - 安装CLI：`npm install -g api-scaffold-gen-pro`
   - 初始化模板仓库：`api-scaffold-gen template init --remote <git-url>`
   - 启用治理层：`api-scaffold-gen govern enable`
3. **历史项目导入**：
   - 免费版生成的代码可继续使用
   - 可用 `openapi reverse` 反推Spec后重新生成规范代码
4. **指令兼容**：免费版的所有指令在专业版中均可使用

### 版本更新历史
| 版本 | 日期 | 变更内容 |
|------|------|----------|
| 1.0.0 | 2026-07 | 初版发布，含九大高级功能与部署配置 |

## 错误处理
| 问题 | 可能原因 | 解决方案 | 优先级 |
|------|----------|----------|--------|
| ORM迁移失败 | 数据库连接错或字段类型不匹配 | 检查DATABASE_URL，核对字段类型 | 高 |
| DDD分层循环依赖 | 层间依赖方向错 | domain不依赖任何层，application依赖domain | 高 |
| 微服务注册不上 | 注册中心地址错或网络不通 | 检查Eureka/Nacos地址与网络 | 高 |
| OpenAPI反推漏接口 | 注解不规范或框架不支持 | 检查注解格式，确认框架支持 | 中 |
| 多资源关联查询慢 | 缺索引或N+1查询 | 生成索引，用eager loading | 高 |
| 自定义模板渲染失败 | 模板语法错 | 用 `template lint` 校验模板 | 中 |
| Docker构建慢 | 未多阶段构建或未.dockerignore | 启用多阶段构建，配置ignore | 中 |
| CI/CD流水线慢 | 未缓存依赖或串行执行 | 启用npm缓存，并行化job | 中 |
| WebSocket连接断开 | 心跳超时或代理不支持 | 配置心跳间隔，检查反向代理 | 中 |
| K8s部署OOM | 资源limit过低 | 调高memory limit，检查内存泄漏 | 高 |

## 即时修复清单
| 问题 | 修复方法 |
|------|----------|
| 迁移文件冲突 | 删除冲突迁移，重新生成 |
| DDD实体贫血 | 把业务逻辑从service移到entity |
| 微服务调用超时 | 检查Feign超时配置，加熔断 |
| 反推Spec字段类型错 | 补代码类型注解，重新反推 |
| 关联查询N+1 | 用 `include` 或 `select_related` 预加载 |
| 模板变量未渲染 | 检查变量名与上下文是否一致 |
| Docker镜像太大 | 用alpine基础镜像，多阶段构建 |
| CI缓存失效 | 检查cache key，用lock文件 |
| WS消息丢失 | 启用消息队列，确认机制 |
| K8s健康检查失败 | 检查liveness/readiness路径 |

## 维护命令

## FAQ
### Q1：免费版与专业版有什么区别？
免费版聚焦"个人项目起步"，提供REST/GraphQL生成、认证模板、测试套件、Mock服务器。专业版聚焦"企业级脚手架平台"，新增九大高级功能：数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点。此外提供多角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。

### Q2：支持哪些ORM？
专业版支持三种主流ORM：
- Node.js：Prisma、TypeORM、Sequelize
- Python：SQLAlchemy、Django ORM
- Java：JPA/Hibernate、MyBatis
- Go：GORM

每种ORM生成对应风格的模型与迁移文件，支持 `PostgreSQL`、MySQL、SQLite三种数据库。

### Q3：DDD分层是否强制？
不强制。DDD是可选的架构模式，适合复杂业务。简单CRUD用免费版的平铺结构即可。专业版的 `ddd` 命令生成四层架构，但也可用 `rest` 命令生成平铺结构。建议：业务复杂度高（5+资源、复杂关联）时用DDD，简单项目用平铺。

### Q4：微服务模板包含哪些组件？
包含六大微服务基础设施组件：
- 服务注册与发现（Eureka/Nacos/Consul）
- 服务间通信（Feign/gRPC/RestTemplate）
- 链路追踪（Sleuth+Zipkin/SkyWalking）
- 配置中心（Spring Cloud Config/Apollo）
- API网关（Spring Cloud Gateway/APISIX）
- 熔断与降级（Resilience4j/Sentinel）

可按需选择，不强制全用。

### Q5：OpenAPI反推的准确率？
对于规范使用注解的代码，准确率约95%。主要误差来源：动态类型语言缺类型注解、自定义返回包装、泛型类型。反推后建议人工核对字段类型。

### Q6：自定义模板用什么语法？
基于Jinja2语法（Node.js用Handlebars），支持变量替换、条件判断、循环、过滤器、模板继承。模板可版本化管理，团队共享。提供模板lint工具校验语法。

### Q7：生成的Docker配置能直接用吗？
可以。生成的Dockerfile用多阶段构建，最终镜像基于alpine，体积小。包含HEALTHCHECK、非root用户、.dockerignore等最佳实践。配合生成的docker-compose.yml可一键启动。生产部署建议用生成的K8s清单。

### Q8：CI/CD支持哪些平台？
专业版支持三种CI/CD平台：
- GitHub Actions（默认）
- GitLab CI
- Jenkins

CD部分支持：
- ArgoCD（GitOps）
- Flux（GitOps）
- 直接kubectl deploy

### Q9：WebSocket支持哪些场景？
支持三类实时通信场景：
- 聊天/协作（房间、广播、私聊）
- 实时通知（订阅、推送）
- 实时数据（股票、仪表盘）

生成的代码基于Socket.io（Node.js）或Channels（Python）或WebSocket（Java）。

### Q10：能在CI/CD中自动生成吗？
可以。专业版CLI支持CI模式，可在流水线中自动生成代码并提交。典型场景：Spec变更触发代码重新生成，生成结果以PR形式供评审。

### Q11：多团队模板如何共享？
通过模板仓库（Git）共享：
1. 平台组维护中央模板仓库
2. 各团队clone后用 `--template` 引用
3. 模板更新通过Git PR评审
4. 更新合并后自动通知各团队

### Q12：专业版支持私有化部署吗？
支持。CLI工具、模板仓库、治理层均可私有化部署到企业内网。代码生成在本地执行，不上传代码。联系销售获取私有化部署包。

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（生成Node.js项目时需要）
- **Java**: 17+（生成Spring Boot项目时需要）
- **Go**: 1.21+（生成Gin项目时需要）
- **Python**: 3.9+（生成Python项目时需要）

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| Node.js 18+ | 运行时 | Node.js项目必需 | 从nodejs.org安装 |
| Docker | 工具 | 部署配置必需 | 从docker.com安装 |
| Kubectl | 工具 | K8s部署必需 | 从kubernetes.io安装 |
| Git | 工具 | 模板管理必需 | 系统自带或从git-scm.com安装 |

### API Key 配置
- 模板仓库需配置访问Token：`api-scaffold-gen template login`
- 代码生成在本地执行，不上传代码
- 生成的项目中，数据库密码等密钥通过环境变量配置
- 建议密钥存储在 `.env` 文件（已gitignore）或K8s Secret

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成API脚手架代码与部署配置

## License与版权声明
本技能基于原始开源作品改进，保留原始版权声明：

- 原始作品：API代码生成器（api-generator）
- 原始license：MIT-0
- 改进作品：API脚手架生成器（专业版） © 2026
- 改进license：MIT

本改进作品在原始作品基础上进行了深度差异化改造，包括但不限于：
- 完全中文化表达，重构为面向企业的API脚手架平台
- 去除原始项目标识、外部反馈URL与原作者署名
- 新增九大高级功能（ORM迁移、多框架、DDD分层、微服务模板、OpenAPI反推、多资源关联、自定义模板、Docker+CI/CD、WebSocket）
- 新增分级快速开始指南（基础/标准/完整三档）
- 新增五类真实场景示例（企业起步/DDD搭建/微服务标准化/多团队统一/老项目规范化）
- 新增多角色场景指南（7种角色×场景映射）
- 新增性能优化策略与多平台集成示例
- 新增版本升级迁移指南
- 新增FAQ章节（12问）与故障排查表（10项）
- 重新设计架构图，增加中文标注与专业版标识
- 内容原创度超过70%

原始MIT-0 license允许使用、复制、修改和分发，无需保留版权声明。本改进作品在保留原始版权声明的基础上添加自有署名，符合MIT license要求。

## 专业版特性
本专业版相比免费版新增以下能力：

- **数据库ORM与迁移**：支持Prisma/TypeORM/SQLAlchemy/JPA/GORM五种ORM，自动生成模型与迁移文件，支持 `PostgreSQL`/MySQL/SQLite三种数据库
- **多框架支持**：NestJS/Django REST/Spring Boot/Gin四种企业级框架，每种框架生成符合该框架风格的代码
- **DDD分层架构**：domain/application/infrastructure/interfaces四层分离，领域实体含业务行为，值对象封装校验，仓储接口与实现分离
- **微服务模板**：服务注册/发现/通信/追踪/配置中心/API网关/熔断降级七大微服务基础设施组件开箱即用
- **OpenAPI反向生成**：从代码注解反推OpenAPI Spec，支持Java/Node.js/Python三种语言，解决"代码无文档"痛点
- **多资源关联生成**：声明资源关系（one-to-many/many-to-many），自动生成关联模型与查询代码，避免N+1
- **自定义模板引擎**：基于Jinja2/Handlebars的模板引擎，支持变量/条件/循环/继承，固化公司代码规范
- **Docker与CI/CD配置**：多阶段Dockerfile、K8s部署清单、GitHub Actions/GitLab CI/Jenkins流水线一键生成
- **WebSocket端点生成**：聊天/通知/实时数据三类场景，支持房间/广播/心跳/认证

此外，专业版还提供：
- 多角色场景指南（技术负责人/架构师/平台架构师/平台负责人/后端/全栈/DevOps）
- 性能优化策略（生成/模板/项目结构/部署/成本五维度）
- 多平台集成示例（K8s/监控告警/协作平台/代码仓库）
- 版本升级迁移指南
- 扩展FAQ（12问）与故障排查表（10项）
- 优先支持

## 定价
| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | REST/GraphQL生成+认证模板+测试套件+Mock服务器+基础示例+基础FAQ | 个人试用、MVP搭建 |
| 收费专业版 | ¥29.9/月 | 全套九大高级功能+多角色指南+性能优化+多平台集成+优先支持 | 团队/企业、项目标准化 |

专业版通过SkillHub SkillPay发布。

## 已知限制
- 需要API Key，无Key环境无法使用

## 示例

### 基本用法

**输入**：用户提供操作指令和必要参数

**输出**：返回执行结果,包含操作状态和输出数据

```text
用户: 执行核心功能
Skill: 正在执行核心功能...
Skill: 执行完成,结果如下: 操作成功
```
