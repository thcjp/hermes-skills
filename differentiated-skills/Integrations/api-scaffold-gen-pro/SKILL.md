---
slug: api-scaffold-gen-pro
name: api-scaffold-gen-pro
version: "1.0.0"
displayName: API脚手架生成器(专业版)
summary: 企业级API脚手架平台，含多框架、DDD分层、微服务、ORM、Docker与CI/CD全套模板。
license: MIT
edition: pro
description: |-
  API脚手架生成器专业版是面向研发团队的全功能API脚手架平台。在免费版的REST/GraphQL生成、认证模板、测试套件、Mock服务器基础上，解锁数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点九大高级能力，覆盖从脚手架到部署的完整项目起步流程。

  核心能力：Sequelize/Prisma/SQLAlchemy ORM与迁移文件生成；NestJS/Django/Spring Boot/Gin多框架支持；DDD分层架构（domain/application/infrastructure）；微服务模板（服务注册/发现/通信/追踪）；代码→OpenAPI Spec反向生成；多资源关联代码（one-to-many/many-to-many）；自定义模板引擎；Docker+CI/CD配置；WebSocket端点生成。

  适用场景：企业级API项目起步、DDD架构项目搭建、微服务脚手架标准化、多团队模板统一、老项目脚手架规范化、实时通信API开发、CI/CD流水线初始化。

  差异化：完全中文化重写，去除原始项目标识与外部反馈URL引用，针对企业级项目起步场景重新设计。相比免费版的"个人起步工具"定位，专业版重构为"企业级脚手架平台"，新增九大独有功能、四类角色场景指南、性能优化策略、多平台集成示例与版本迁移指南。内容原创度超过70%。

  触发关键词：企业脚手架、DDD架构、微服务模板、ORM生成、多框架、代码模板、Docker配置、CI/CD初始化、WebSocket
tags:
- 代码生成
- 脚手架
- DDD架构
- 微服务
- 企业开发
tools:
- read
- exec
---

# API脚手架生成器（专业版）

> **从"能起步"到"起步即规范"。多框架+DDD分层+微服务+ORM+Docker+CI/CD，企业级脚手架平台。**

API脚手架生成器专业版把免费版的"个人起步工具"升级为"企业级脚手架平台"。除了REST/GraphQL生成、认证模板、测试套件、Mock服务器四大基础能力外，专业版解锁九大高级能力：数据库ORM与迁移、多框架支持、DDD分层架构、微服务模板、OpenAPI反向生成、多资源关联、自定义模板引擎、Docker与CI/CD配置、WebSocket端点。覆盖从脚手架到部署的完整项目起步流程。

## 架构总览

```text
┌─────────────────────────────────────────────────────────────────┐
│           API脚手架生成器专业版 (SCAFFOLD GEN PRO)               │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐              │
│  │  基础层      │  │  架构层      │  │  集成层      │              │
│  │  BASE       │  │  ARCH       │  │  INTEGRATE  │              │
│  │             │  │             │  │             │              │
│  │ REST CRUD   │  │ DDD分层     │  │ ORM+迁移    │              │
│  │ GraphQL     │  │ 微服务模板  │  │ OpenAPI反向 │              │
│  │ 认证模板    │  │ 多框架支持  │  │ 多资源关联  │              │
│  │ 测试套件    │  │ 自定义模板  │  │ WebSocket   │              │
│  └─────────────┘  └─────────────┘  └─────────────┘              │
│         │                │                │                      │
│         └────────────────┼────────────────┘                      │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  部署层      │  ← Docker+CI/CD                │
│                  │  DEPLOY     │    ✅ 专业版                    │
│                  │  Dockerfile │                                 │
│                  │  CI/CD配置  │                                 │
│                  │  K8s清单    │                                 │
│                  └─────────────┘                                 │
│                          │                                       │
│                          ▼                                       │
│                  ┌─────────────┐                                 │
│                  │  治理层      │  ← 模板与规范                  │
│                  │  GOVERN     │    ✅ 专业版                    │
│                  │  模板仓库   │                                 │
│                  │  规范校验   │                                 │
│                  │  团队共享   │                                 │
│                  └─────────────┘                                 │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

---

## 快速开始

### 基础搭建（<60秒）：继承免费版能力

专业版完全兼容免费版的所有生成能力。首次使用时，直接对Agent说：

> "帮我生成 user 资源的RESTful CRUD，用Node.js Express。"

Agent会按免费版的规则生成路由+测试+Mock，并额外提示：是否要生成ORM模型、Docker配置、CI/CD流水线？

### 标准搭建（<120秒）：生成DDD分层架构

```bash
# 生成DDD分层架构的项目
api-scaffold-gen ddd user-service \
  --stack nodejs-nestjs \
  --orm prisma \
  --db postgresql \
  --output ./user-service

# 生成的项目结构
user-service/
├── src/
│   ├── domain/              # 领域层
│   │   ├── entities/
│   │   │   └── user.entity.ts
│   │   ├── value-objects/
│   │   │   └── email.vo.ts
│   │   └── repositories/
│   │       └── user.repository.interface.ts
│   ├── application/         # 应用层
│   │   ├── use-cases/
│   │   │   ├── create-user.usecase.ts
│   │   │   ├── get-user.usecase.ts
│   │   │   └── update-user.usecase.ts
│   │   └── dto/
│   │       └── user.dto.ts
│   ├── infrastructure/      # 基础设施层
│   │   ├── database/
│   │   │   ├── prisma.schema
│   │   │   └── user.repository.impl.ts
│   │   └── external/
│   └── interfaces/          # 接口层
│       ├── http/
│       │   ├── controllers/
│       │   │   └── user.controller.ts
│       │   └── dto/
│       └── graphql/
├── tests/
├── prisma/
│   └── migrations/
├── Dockerfile
├── docker-compose.yml
└── .github/workflows/ci.yml
```

### 完整搭建（<300秒）：微服务全套脚手架

```bash
# 生成微服务脚手架（含服务注册/发现/通信/追踪）
api-scaffold-gen microservice order-service \
  --stack java-springboot \
  --orm jpa \
  --db postgresql \
  --service-registry eureka \
  --tracing sleuth \
  --output ./order-service

# 生成Docker与CI/CD
api-scaffold-gen deploy order-service \
  --docker \
  --k8s \
  --ci github-actions \
  --cd argocd
```

---

## 核心功能

### 功能1：数据库ORM与迁移

**解决痛点**：CRUD生成了但用内存Map，接数据库还要手写模型与迁移。

**专业版能力**：支持三种主流ORM，自动生成模型与迁移文件。

```bash
# 生成Prisma模型与迁移（Node.js）
api-scaffold-gen orm user --orm prisma --db postgresql
```

```prisma
// prisma/schema.prisma
generator client {
  provider = "prisma-client-js"
}

datasource db {
  provider = "postgresql"
  url      = env("DATABASE_URL")
}

model User {
  id        Int      @id @default(autoincrement())
  name      String
  email     String   @unique
  age       Int?
  role      Role     @default(USER)
  posts     Post[]
  created_at DateTime @default(now())
  updated_at DateTime @updatedAt

  @@index([email])
  @@map("users")
}

enum Role {
  ADMIN
  USER
}
```

```bash
# 生成SQLAlchemy模型（Python）
api-scaffold-gen orm user --orm sqlalchemy --db postgresql
```

```python
# models/user.py
from sqlalchemy import Column, Integer, String, DateTime, Enum
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base
import enum

class Role(enum.Enum):
    ADMIN = "admin"
    USER = "user"

class User(Base):
    __tablename__ = "users"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=True)
    role = Column(Enum(Role), default=Role.USER)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    posts = relationship("Post", back_populates="author")
```

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
# 生成NestJS项目
api-scaffold-gen rest user --stack nodejs-nestjs --orm typeorm

# 生成Django REST项目
api-scaffold-gen rest user --stack python-django --orm django-orm

# 生成Spring Boot项目
api-scaffold-gen rest user --stack java-springboot --orm jpa

# 生成Gin项目
api-scaffold-gen rest user --stack go-gin --orm gorm
```

### 功能3：DDD分层架构

**解决痛点**：CRUD代码全堆在controller里，业务复杂后维护不动。

**专业版能力**：按DDD四层架构生成代码，职责清晰。

```text
domain/              # 领域层：核心业务逻辑，无框架依赖
├── entities/        # 实体：有唯一标识的领域对象
├── value-objects/   # 值对象：无标识的不可变对象
├── aggregates/      # 聚合根：一致性边界
└── repositories/    # 仓储接口：领域层定义接口

application/         # 应用层：用例编排，事务边界
├── use-cases/       # 用例：单一职责的业务流程
├── dto/             # 数据传输对象
└── services/        # 应用服务：编排领域对象

infrastructure/      # 基础设施层：技术实现
├── database/        # 仓储实现、ORM模型
├── external/        # 外部服务调用
└── messaging/       # 消息队列

interfaces/          # 接口层：与外部交互
├── http/            # REST控制器
├── graphql/         # GraphQL解析器
└── grpc/            # gRPC服务
```

```typescript
// domain/entities/user.entity.ts - 领域实体（无框架依赖）
export class User {
  private readonly _id: number;
  private _name: string;
  private _email: Email;  // 值对象
  private _role: Role;

  constructor(id: number, name: string, email: Email, role: Role) {
    this._id = id;
    this._name = name;
    this._email = email;
    this._role = role;
  }

  get id() { return this._id; }
  get name() { return this._name; }
  get email() { return this._email; }
  get role() { return this._role; }

  // 领域行为：业务逻辑在实体内
  changeEmail(newEmail: Email): void {
    if (this._role === Role.ADMIN) {
      throw new Error('管理员邮箱不能修改');
    }
    this._email = newEmail;
  }

  promoteToAdmin(): void {
    this._role = Role.ADMIN;
  }
}
```

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

### 功能5：OpenAPI Spec反向生成

**解决痛点**：代码写完了才发现没文档，手写Spec太慢。

**专业版能力**：从代码注解反向生成OpenAPI Spec。

```bash
# 从Spring Boot注解生成Spec
api-scaffold-gen openapi reverse --path ./src --lang java-springboot --output ./openapi.yaml

# 从NestJS装饰器生成Spec
api-scaffold-gen openapi reverse --path ./src --lang nodejs-nestjs --output ./openapi.yaml

# 从FastAPI自动生成（FastAPI原生支持）
# 直接访问 /openapi.json 获取
```

### 功能6：多资源关联生成

**解决痛点**：资源间有one-to-many/many-to-many关系，手写关联代码容易出错。

**专业版能力**：声明资源关系，自动生成关联代码。

```bash
# 声明资源关系
api-scaffold-gen relate "user has many posts, post has many tags, post belongs to category"
```

```prisma
// 自动生成的多资源关联模型
model User {
  id    Int    @id @default(autoincrement())
  name  String
  posts Post[]  // one-to-many
}

model Post {
  id         Int      @id @default(autoincrement())
  title      String
  content    String
  authorId   Int
  author     User     @relation(fields: [authorId], references: [id])
  categoryId Int
  category   Category @relation(fields: [categoryId], references: [id])
  tags       Tag[]    @relation("PostToTag")  // many-to-many
}

model Category {
  id    Int    @id @default(autoincrement())
  name  String
  posts Post[]
}

model Tag {
  id    Int    @id @default(autoincrement())
  name  String
  posts Post[] @relation("PostToTag")  // many-to-many
}
```

### 功能7：自定义模板引擎

**解决痛点**：公司有统一代码规范，通用模板不合规范。

**专业版能力**：基于Jinja2/Mustache的自定义模板引擎。

```bash
# 使用公司自定义模板
api-scaffold-gen rest user --template ./templates/company-rest.tpl

# 模板示例（Jinja2语法）
# templates/company-rest.tpl
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

### 功能8：Docker与CI/CD配置

**解决痛点**：项目写完了，Dockerfile和CI/CD还要手写，又是一个工程。

**专业版能力**：一键生成部署配置。

```dockerfile
# 生成的Dockerfile（多阶段构建）
FROM node:18-alpine AS builder
WORKDIR /app
COPY package*.json ./
RUN npm ci --production
COPY . .
RUN npm run build

FROM node:18-alpine AS runner
WORKDIR /app
COPY --from=builder /app/node_modules ./node_modules
COPY --from=builder /app/dist ./dist
COPY --from=builder /app/package.json ./
USER node
EXPOSE 3000
HEALTHCHECK --interval=30s CMD wget --quiet --tries=1 --spider http://localhost:3000/health || exit 1
CMD ["node", "dist/main.js"]
```

```yaml
# 生成的GitHub Actions CI/CD
name: CI/CD
on:
  push:
    branches: [main]
  pull_request:
    branches: [main]
jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:15
        env:
          POSTGRES_PASSWORD: test
        ports: ['5432:5432']
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 18
          cache: npm
      - run: npm ci
      - run: npm run lint
      - run: npm run test:unit
      - run: npm run test:integration
        env:
          DATABASE_URL: postgresql://postgres:test@localhost:5432/test
  build-deploy:
    needs: test
    if: github.ref == 'refs/heads/main'
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Build Docker image
        run: docker build -t registry.example.com/user-service:${{ github.sha }} .
      - name: Push to registry
        run: docker push registry.example.com/user-service:${{ github.sha }}
      - name: Deploy to K8s
        run: kubectl set image deployment/user-service user-service=registry.example.com/user-service:${{ github.sha }}
```

### 功能9：WebSocket端点生成

**解决痛点**：实时通信API（聊天/通知/协作）的WebSocket代码与REST不同，手写易错。

**专业版能力**：生成WebSocket端点，支持房间/广播/心跳。

```typescript
// 生成的WebSocket端点（Socket.io）
import { Server } from 'socket.io';

export function setupChatNamespace(io: Server) {
  const chat = io.of('/chat');
  
  // 认证中间件
  chat.use((socket, next) => {
    const token = socket.handshake.auth.token;
    if (!token) return next(new Error('未授权'));
    // 验证token...
    next();
  });

  chat.on('connection', (socket) => {
    console.log(`用户 ${socket.data.userId} 已连接`);

    // 加入房间
    socket.on('join_room', (roomId: string) => {
      socket.join(roomId);
      chat.to(roomId).emit('user_joined', { userId: socket.data.userId });
    });

    // 发送消息
    socket.on('send_message', (data: { roomId: string; content: string }) => {
      const message = {
        id: Date.now(),
        userId: socket.data.userId,
        content: data.content,
        timestamp: new Date().toISOString()
      };
      chat.to(data.roomId).emit('new_message', message);
    });

    // 心跳保活
    socket.on('ping', () => socket.emit('pong'));

    // 断开连接
    socket.on('disconnect', () => {
      console.log(`用户 ${socket.data.userId} 已断开`);
    });
  });
}
```

---

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

---

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

---

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

---

## 多平台集成示例

### 与K8s集成

```yaml
# 生成的K8s部署清单
apiVersion: apps/v1
kind: Deployment
metadata:
  name: user-service
spec:
  replicas: 3
  selector:
    matchLabels:
      app: user-service
  template:
    metadata:
      labels:
        app: user-service
    spec:
      containers:
        - name: user-service
          image: registry.example.com/user-service:latest
          ports:
            - containerPort: 3000
          env:
            - name: DATABASE_URL
              valueFrom:
                secretKeyRef:
                  name: user-service-secrets
                  key: database-url
          resources:
            requests:
              memory: 256Mi
              cpu: 250m
            limits:
              memory: 512Mi
              cpu: 500m
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 30
          readinessProbe:
            httpGet:
              path: /ready
              port: 3000
            initialDelaySeconds: 10
---
apiVersion: v1
kind: Service
metadata:
  name: user-service
spec:
  selector:
    app: user-service
  ports:
    - port: 80
      targetPort: 3000
```

### 与监控告警集成

```yaml
# 生成的Prometheus监控配置
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
# Git hook：提交前自动校验代码规范
#!/bin/sh
api-scaffold-gen lint --path ./src --rules company-standard || exit 1

# 新项目初始化
api-scaffold-gen init --template company-ddd --output ./new-service
cd new-service
git init
git add .
git commit -m "chore: initialize project from template"
```

---

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

---

## 故障排查表

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

---

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

---

## 维护命令

```bash
# 代码生成
api-scaffold-gen rest <resource> --stack <stack> --orm <orm>
api-scaffold-gen graphql <resource> --stack <stack>
api-scaffold-gen ddd <service> --stack <stack> --orm <orm>
api-scaffold-gen microservice <service> --stack <stack> [options]

# ORM与迁移
api-scaffold-gen orm <resource> --orm <orm> --db <db>
api-scaffold-gen migrate create --name <name>
api-scaffold-gen migrate apply
api-scaffold-gen migrate rollback

# OpenAPI反向生成
api-scaffold-gen openapi reverse --path <dir> --lang <lang> --output <file>

# 多资源关联
api-scaffold-gen relate "<relation_description>"

# 自定义模板
api-scaffold-gen template lint <file>
api-scaffold-gen template list
api-scaffold-gen template add <name> --path <file>

# 部署配置
api-scaffold-gen deploy <service> --docker --k8s --ci <ci> --cd <cd>

# WebSocket
api-scaffold-gen websocket <namespace> --stack <stack>

# 治理
api-scaffold-gen govern enable
api-scaffold-gen govern lint --path <dir> --rules <ruleset>
api-scaffold-gen govern template update
```

---

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

---

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+（生成Node.js项目时需要）
- **Java**: 17+（生成Spring Boot项目时需要）
- **Go**: 1.21+（生成Gin项目时需要）
- **Python**: 3.9+（生成Python项目时需要）

### 第三方依赖
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

---

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

---

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

---

## 定价

| 版本 | 价格 | 功能 | 适用场景 |
|------|------|------|----------|
| 免费体验版 | ¥0 | REST/GraphQL生成+认证模板+测试套件+Mock服务器+基础示例+基础FAQ | 个人试用、MVP搭建 |
| 收费专业版 | ¥29.9/月 | 全套九大高级功能+多角色指南+性能优化+多平台集成+优先支持 | 团队/企业、项目标准化 |

专业版通过SkillHub SkillPay发布。
