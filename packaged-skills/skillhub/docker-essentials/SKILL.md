---
slug: docker-essentials
name: docker-essentials
version: "1.0.0"
displayName: Docker核心操作指南
summary: 涵盖容器生命周期、镜像管理、Compose、网络、数据卷、系统管理等Docker核心操作。
license: Proprietary
description: |-
  Docker核心操作指南，覆盖容器生命周期的完整管理流程。
  包含容器调试、镜像构建与管理、Docker Compose多容器编排。
  涵盖网络配置、数据卷管理、系统管理与常见工作流。
  适用于开发、测试、生产环境的Docker容器化部署与运维。
tools:
  - read
  - exec
---

# Docker核心操作指南

涵盖容器生命周期、镜像管理、Compose、网络、数据卷、系统管理等Docker核心操作。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Docker环境**: Docker Engine 20.10+ 及 Docker Compose v1/v2

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Docker Engine | 运行时 | 必需 | https://docs.docker.com/engine/install/ |
| Docker Compose | 工具 | 必需 | https://docs.docker.com/compose/install/ |
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| 终端/Shell | CLI | 必需 | 操作系统自带 |

### 可用性分类
- **分类**: MD+EXEC（纯Markdown指令，需要exec命令行执行能力运行Docker命令）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成与执行Docker命令

## 核心能力

### 容器生命周期管理（Container Lifecycle）

完整的容器创建、启动、停止、删除管理：

**运行容器（Running containers）：**

```bash
docker run nginx                              # 前台运行
docker run -d nginx                           # 后台运行
docker run --name my-nginx -d nginx           # 指定名称
docker run -p 8080:80 -d nginx                # 端口映射
docker run -e MY_VAR=value -d app             # 环境变量
docker run -v /host/path:/container/path -d app  # 卷挂载
docker run --rm alpine echo "Hello"           # 退出后自动删除
docker run -it ubuntu bash                    # 交互式终端
```

**管理容器（Managing containers）：**

```bash
docker ps                # 查看运行中容器
docker ps -a             # 查看所有容器（含已停止）
docker stop container_name    # 停止容器
docker start container_name   # 启动容器
docker restart container_name # 重启容器
docker rm container_name      # 删除已停止容器
docker rm -f container_name   # 强制删除容器
docker container prune        # 清理所有已停止容器
```

### 容器检查与调试（Container Inspection & Debugging）
查看日志、执行命令、检查容器状态：

**查看日志（Viewing logs）：**

```bash
docker logs container_name           # 查看全部日志
docker logs -f container_name        # 跟踪日志
docker logs --tail 100 container_name  # 最后100行
docker logs -t container_name        # 显示时间戳
```

**执行命令（Executing commands）：**

```bash
docker exec container_name ls -la              # 执行单条命令
docker exec -it container_name bash            # 交互式shell
docker exec -u root -it container_name bash    # 以root执行
docker exec -e VAR=value container_name env    # 带环境变量
```

**检查（Inspection）：**

```bash
docker inspect container_name                          # 完整信息
docker inspect -f '{{.NetworkSettings.IPAddress}}' container_name  # 提取IP
docker stats                  # 所有容器资源使用
docker stats container_name   # 指定容器资源使用
docker top container_name     # 容器内进程
```

**输入**: 用户提供容器检查与调试（Container Inspection & Debugging）所需的指令和必要参数。
**输出**: 返回容器检查与调试（Container Inspection & Debugging）的执行结果,包含操作状态和输出数据。### 镜像管理（Image Management）

构建、拉取、推送、清理镜像：

**构建镜像（Building images）：**

```bash
docker build -t myapp:1.0 .                          # 基本构建
docker build -f Dockerfile.dev -t myapp:dev .        # 指定Dockerfile
docker build --build-arg VERSION=1.0 -t myapp .      # 构建参数
docker build --no-cache -t myapp .                   # 不使用缓存
```

**管理镜像（Managing images）：**

```bash
docker images                # 列出镜像
docker pull nginx:latest     # 拉取镜像
docker tag myapp:1.0 myapp:latest  # 打标签
docker push myrepo/myapp:1.0      # 推送镜像
docker rmi image_name        # 删除镜像
docker image prune           # 清理悬空镜像
docker image prune -a        # 清理所有未使用镜像
```

### Docker Compose
多容器应用编排与服务管理：

**基本操作（Basic operations）：**

```bash
docker-compose up            # 启动（前台）
docker-compose up -d         # 启动（后台）
docker-compose down          # 停止并删除
docker-compose down -v       # 同时删除卷
docker-compose logs          # 查看所有服务日志
docker-compose logs -f web   # 跟踪指定服务日志
docker-compose up -d --scale web=3  # 扩展服务实例数
```

**服务管理（Service management）：**

```bash
docker-compose ps            # 查看服务状态
docker-compose exec web bash # 在服务中执行命令
docker-compose restart web   # 重启服务
docker-compose build web     # 重新构建服务
docker-compose up -d --build # 重新构建并启动
```

**输入**: 用户提供Docker Compose所需的指令和必要参数。
**输出**: 返回Docker Compose的执行结果,包含操作状态和输出数据。### 网络配置（Networking）
管理Docker网络与容器互联：

```bash
docker network ls                            # 列出网络
docker network create mynetwork              # 创建网络
docker network connect mynetwork container_name   # 连接容器到网络
docker network disconnect mynetwork container_name  # 断开连接
docker network inspect mynetwork             # 查看网络详情
docker network rm mynetwork                  # 删除网络
```

**输入**: 用户提供网络配置（Networking）所需的指令和必要参数。
**处理**: 按照skill规范执行网络配置（Networking）操作,遵循单一意图原则。### 数据卷管理（Volumes）

持久化数据存储管理：

```bash
docker volume ls                # 列出卷
docker volume create myvolume   # 创建卷
docker volume inspect myvolume  # 查看卷详情
docker volume rm myvolume       # 删除卷
docker volume prune             # 清理未使用卷
docker run -v myvolume:/data -d app  # 使用卷
```

### 系统管理（System Management）
Docker系统级清理与信息查看：

```bash
docker system df                # 查看磁盘使用
docker system prune             # 清理未使用资源
docker system prune -a          # 清理所有未使用（含镜像）
docker system prune --volumes   # 同时清理卷
docker info                     # 系统信息
docker version                  # 版本信息
```

**输入**: 用户提供系统管理（System Management）所需的指令和必要参数。
**输出**: 返回系统管理（System Management）的执行结果,包含操作状态和输出数据。### 常见工作流（Common Workflows）
预置开发、数据库、调试与构建工作流：

**开发容器（Development container）：**

```bash
docker run -it --rm \
  -v $(pwd):/app \
  -w /app \
  -p 3000:3000 \
  node:18 \
  npm run dev
```

**数据库容器（Database container）：**

```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15
```

**快速调试（Quick debugging）：**

```bash
docker exec -it container_name sh
docker cp container_name:/path/to/file ./local/path
docker cp ./local/file container_name:/path/in/container
```

**多阶段构建（Multi-stage build）：**

```dockerfile
FROM node:18 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:alpine
COPY --from=builder /app/dist /usr/share/nginx/html
```

**输入**: 用户提供常见工作流（Common Workflows）所需的指令和必要参数。
**输出**: 返回常见工作流（Common Workflows）的执行结果,包含操作状态和输出数据。
## 使用流程

1. 确认Docker Engine与Docker Compose已安装并运行
2. 根据需求选择操作类型（容器管理、镜像构建、Compose编排等）
3. 使用自然语言描述需求，Agent生成对应的Docker命令
4. Agent执行命令并检查输出结果
5. 如遇错误，参考错误处理章节进行排查

## 示例

### 示例1：启动一个带端口的Nginx容器

```
用户: 帮我启动一个Nginx容器，端口映射8080到80

Agent: docker run -d --name my-nginx -p 8080:80 nginx
- 容器已在后台启动
- 访问 http://localhost:8080 即可查看Nginx欢迎页
- 使用 docker logs -f my-nginx 查看日志
```

### 示例2：使用Docker Compose启动多服务

```
用户: 用docker-compose启动一个web+redis的应用

Agent: 以下是docker-compose.yml配置：
version: '3'
services:
  web:
    build: .
    ports:
      - "3000:3000"
    depends_on:
      - redis
  redis:
    image: redis:alpine

执行: docker-compose up -d
- 两个服务已在后台启动
- 使用 docker-compose ps 查看状态
- 使用 docker-compose logs -f 查看日志
```

### 示例3：调试运行中的容器

```
用户: 我的app容器有问题，帮我进去看看

Agent: 执行调试命令：
1. docker logs --tail 50 app  # 查看最近日志
2. docker exec -it app sh     # 进入容器shell
3. docker stats app           # 查看资源使用

如需复制文件：
docker cp app:/var/log/app.log ./app.log
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| `Cannot connect to the Docker daemon` | Docker服务未启动 | 执行 `systemctl start docker`（Linux）或启动Docker Desktop（Win/Mac） |
| `port is already allocated` | 端口被占用 | 使用 `docker ps` 查看占用端口的容器；更换映射端口或停止占用容器 |
| `Conflict. The container name is already in use` | 容器名冲突 | 执行 `docker rm -f <name>` 删除旧容器，或使用新名称 |
| `no space left on device` | 磁盘空间不足 | 执行 `docker system prune -a --volumes` 清理未使用资源 |
| `image not found locally` | 镜像不存在 | 执行 `docker pull <image>` 拉取镜像，或检查镜像名拼写 |
| `permission denied` | 用户无Docker权限 | 将用户加入docker组：`sudo usermod -aG docker $USER`，重新登录 |
| Compose服务启动失败 | 配置文件错误 | 检查docker-compose.yml语法；执行 `docker-compose config` 验证配置 |

## 常见问题

### Q1: 如何查看容器内发生了什么？
A: 使用 `docker logs -f <container>` 跟踪日志，使用 `docker exec -it <container> sh` 进入容器shell，使用 `docker stats <container>` 查看资源使用情况。

### Q2: 如何清理Docker释放空间？
A: 使用 `docker system prune -a --volumes` 清理所有未使用的镜像、容器、网络和卷。注意此操作不可逆，确保没有需要保留的资源。

### Q3: 如何在容器间通信？
A: 创建自定义网络 `docker network create mynet`，启动容器时使用 `--network mynet`，容器间可通过容器名互相访问。

### Q4: 数据卷和绑定挂载有什么区别？
A: 数据卷（volume）由Docker管理，存储在Docker目录，适合持久化数据。绑定挂载（bind mount）直接映射主机路径，适合开发时挂载代码。

### Q5: 如何构建更小的镜像？
A: 使用多阶段构建（multi-stage build），合并RUN命令减少层，使用Alpine等基础镜像，添加 `.dockerignore` 排除不必要文件。

### Q6: docker-compose up和docker-compose up -d有什么区别？
A: `docker-compose up` 在前台运行，日志直接输出到终端，Ctrl+C停止。`docker-compose up -d` 在后台运行，需要用 `docker-compose logs` 查看日志。

## 已知限制

- 需要Docker Engine运行环境，无Docker环境无法执行命令
- 部分命令在Windows上语法不同（如 `$(pwd)` 需改为 `${PWD}`）
- Docker Compose v1使用 `docker-compose`，v2使用 `docker compose`（无连字符）
- 容器内GPU支持需要额外配置NVIDIA Container Toolkit
- 复杂网络拓扑（如overlay网络）需要Swarm模式支持
- 镜像构建性能受网络影响，拉取基础镜像可能较慢
