---
slug: docker-essentials-1-0-0
name: docker-essentials-1-0-0
version: "1.0.0"
displayName: Docker Essentials 1.0.0
summary: Essential Docker commands and workflows for container management, image operations,
  and debugging.
license: MIT
description: |-
  Essential Docker commands and workflows for container management, image
  operations, and debugging.

  核心能力:

  - 开发工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 代码审查、开发规范、项目管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 1.0.0, workflows, docker, essentials, container, commands, essential
tags:
- Development
- Operations
tools:
- read
- exec
---

# Docker Essentials 1.0.0

Essential Docker commands for container and image management.

## Container Lifecycle

### Running containers

```bash
docker run nginx

docker run -d nginx

docker run --name my-nginx -d nginx

docker run -p 8080:80 -d nginx

docker run -e MY_VAR=value -d app

docker run -v /host/path:/container/path -d app

docker run --rm alpine echo "Hello"

docker run -it ubuntu bash
```

### Managing containers

```bash
docker ps

docker ps -a

docker stop container_name

docker start container_name

docker restart container_name

docker rm container_name

docker rm -f container_name

docker container prune
```

## Container Inspection & Debugging

### Viewing logs

```bash
docker logs container_name

docker logs -f container_name

docker logs --tail 100 container_name

docker logs -t container_name
```

### Executing commands

```bash
docker exec container_name ls -la

docker exec -it container_name bash

docker exec -u root -it container_name bash

docker exec -e VAR=value container_name env
```

### Inspection

```bash
docker inspect container_name

docker inspect -f '{{.NetworkSettings.IPAddress}}' container_name

docker stats

docker stats container_name

docker top container_name
```

## Image Management

### Building images

```bash
docker build -t myapp:1.0 .

docker build -f Dockerfile.dev -t myapp:dev .

docker build --build-arg VERSION=1.0 -t myapp .

docker build --no-cache -t myapp .
```

### Managing images

```bash
docker images

docker pull nginx:latest

docker tag myapp:1.0 myapp:latest

docker push myrepo/myapp:1.0

docker rmi image_name

docker image prune

docker image prune -a
```

## Docker Compose

### Basic operations

```bash
docker-compose up

docker-compose up -d

docker-compose down

docker-compose down -v

docker-compose logs

docker-compose logs -f web

docker-compose up -d --scale web=3
```

### Service management

```bash
docker-compose ps

docker-compose exec web bash

docker-compose restart web

docker-compose build web

docker-compose up -d --build
```

## Networking

```bash
docker network ls

docker network create mynetwork

docker network connect mynetwork container_name

docker network disconnect mynetwork container_name

docker network inspect mynetwork

docker network rm mynetwork
```

## Volumes

```bash
docker volume ls

docker volume create myvolume

docker volume inspect myvolume

docker volume rm myvolume

docker volume prune

docker run -v myvolume:/data -d app
```

## System Management

```bash
docker system df

docker system prune

docker system prune -a

docker system prune --volumes

docker info

docker version
```

## Common Workflows

**Development container:**

```bash
docker run -it --rm \
  -v $(pwd):/app \
  -w /app \
  -p 3000:3000 \
  node:18 \
  npm run dev
```

**Database container:**

```bash
docker run -d \
  --name postgres \
  -e POSTGRES_PASSWORD=secret \
  -e POSTGRES_DB=mydb \
  -v postgres-data:/var/lib/postgresql/data \
  -p 5432:5432 \
  postgres:15
```

**Quick debugging:**

```bash
docker exec -it container_name sh

docker cp container_name:/path/to/file ./local/path

docker cp ./local/file container_name:/path/in/container
```

**Multi-stage build:**

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

## Useful Flags

**`docker run` flags:**

* `-d`: Detached mode (background)
* `-it`: Interactive terminal
* `-p`: Port mapping (host:container)
* `-v`: Volume mount
* `-e`: Environment variable
* `--name`: Container name
* `--rm`: Auto-remove on exit
* `--network`: Connect to network

**`docker exec` flags:**

* `-it`: Interactive terminal
* `-u`: User
* `-w`: Working directory

## Tips

* Use `.dockerignore` to exclude files from build context
* Combine `RUN` commands in Dockerfile to reduce layers
* Use multi-stage builds to reduce image size
* Always tag your images with versions
* Use `--rm` for one-off containers
* Use `docker-compose` for multi-container apps
* Clean up regularly with `docker system prune`

## Documentation

Official docs: <https://docs.docker.com/>
Dockerfile reference: <https://docs.docker.com/engine/reference/builder/>
Compose file reference: <https://docs.docker.com/compose/compose-file/>

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
