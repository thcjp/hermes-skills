# 详细参考 - api-scaffold-gen-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (yaml)

```yaml
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

## 代码示例 (typescript)

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

## 代码示例 (bash)

```bash
api-scaffold-gen ddd user-service \
  --stack nodejs-nestjs \
  --orm prisma \
  --db postgresql \
  --output ./user-service

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

## 代码示例 (yaml)

```yaml
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

## 代码示例 (text)

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

## 代码示例 (typescript)

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

## 代码示例 (prisma)

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

## 代码示例 (prisma)

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

## 代码示例 (bash)

```bash
api-scaffold-gen rest <resource> --stack <stack> --orm <orm>
api-scaffold-gen graphql <resource> --stack <stack>
api-scaffold-gen ddd <service> --stack <stack> --orm <orm>
api-scaffold-gen microservice <service> --stack <stack> [options]

api-scaffold-gen orm <resource> --orm <orm> --db <db>
api-scaffold-gen migrate create --name <name>
api-scaffold-gen migrate apply
api-scaffold-gen migrate rollback

api-scaffold-gen openapi reverse --path <dir> --lang <lang> --output <file>

api-scaffold-gen relate "<relation_description>"

api-scaffold-gen template lint <file>
api-scaffold-gen template list
api-scaffold-gen template add <name> --path <file>

api-scaffold-gen deploy <service> --docker --k8s --ci <ci> --cd <cd>

api-scaffold-gen websocket <namespace> --stack <stack>

api-scaffold-gen govern enable
api-scaffold-gen govern lint --path <dir> --rules <ruleset>
api-scaffold-gen govern template update
```

## 代码示例 (python)

```python
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

## 代码示例 (text)

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

## 代码示例 (dockerfile)

```dockerfile
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

### 功能1：数据库ORM与迁移
**解决痛点**：CRUD生成了但用内存Map，接数据库还要手写模型与迁移。

**专业版能力**：支持三种主流ORM，自动生成模型与迁移文件。

```bash
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
api-scaffold-gen orm user --orm sqlalchemy --db postgresql
```

```python
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



### 功能8：Docker与CI/CD配置
**解决痛点**：项目写完了，Dockerfile和CI/CD还要手写，又是一个工程。

**专业版能力**：一键生成部署配置。

```dockerfile
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



