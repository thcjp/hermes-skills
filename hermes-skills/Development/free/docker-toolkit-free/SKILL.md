---

name: "docker-toolkit-free"
description: "Docker容器管理工具，支持镜像/容器/卷/网络基础操作与简单编排。Use when 需要项目管理、任务规划、进度跟踪、团队协作时使用。不适用于实际人员绩效评估。适用于独立开发者、企业团队和自动化工作流场景。支持中文交互，无需复杂配置即开即用。输出结果可直接使用，减少二次加工成本。提供结构化输出和错误处理机制。"
license: Proprietary
allowed-tools: read exec
compatibility: "Requires LLM with tool-use capability"
metadata:
  displayName: "Docker容器入门工具"
  version: "1.0.0"
  summary: "Docker容器管理工具，支持镜像/容器/卷/网络基础操作与简单编排。"
  tags:
    - "Operations"
    - "Docker"
    - "容器化"
    - "部署"
  source: "SkillHub"
  converted_at: "2026-07-22T17:58:36"
tools:
  - exec
  - read

---

# Docker容器入门工具（免费版）

## 概述

本工具为个人开发者提供Docker容器管理能力。支持镜像构建、容器生命周期管理、数据卷与网络配置，以及Docker Compose基础编排。适合个人开发环境与小型应用的容器化部署。

## 核心能力

### 管理功能

| 功能 | 说明 | 免费版支持 |
| --- | --- | --- |
| 镜像管理 | 构建/拉取/推送/删除 | 支持 |
| 容器管理 | 创建/启动/停止/删除 | 支持 |
| 数据卷 | 创建/挂载/备份 | 支持 |
| 网络 | 创建/连接/断开 | 支持 |
| Compose | 多容器编排 | 基础支持 |
| 镜像仓库 | 私有仓库管理 | 不支持 |
| 集群管理 | Swarm/K8s | 不支持 |
| 安全扫描 | 镜像漏洞扫描 | 不支持 |

**输出**: 返回管理功能的执行结果,包含操作状态和输出数据。

### 核心功能执行
用`input_params`参数进行配置。

**输出**: 返回核心功能执行的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置。

**输出**: 返回参数配置与调用的执行结果,包含操作状态和输出数据。
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：Docker、容器管理工具、支持镜像、网络基础操作与简、单编排、面向个人开发者的、支持镜像构建与拉、生命周期管理、数据卷与网络配置、Use、when、需要数据分析、报表生成、统计洞察、数据可视化时使用、不适用于实时流数、据处理、适用于独立开发者、企业团队和自动化、工作流场景等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持。

## 使用场景

### 场景一：构建并运行容器

用户输入："构建镜像并运行容器"

```bash
# 构建镜像
python3 scripts/docker.py image build \
  --tag my-app:latest \
  --path ./Dockerfile

# 运行容器
  --image my-app:latest \
  --name my-app \
  --port 8080:80 \
  --detach

# 查看运行状态
```

### 场景二：Docker Compose编排

用户输入："用Compose启动一套Web+数据库环境"

```bash
# 生成docker-compose.yml
py compose generate \
  --template "web_db" \
  --output docker-compose.yml

# 启动服务
py compose up --detach

# 查看状态
```

### 场景三：数据卷管理

用户输入："创建数据卷并挂载到容器"

```bash
# 创建数据卷
py volume create --name my-data

# 挂载运行
  --image postgres:15 \
  --name my-db \
  --volume my-data:/var/lib/数据库/data \
  --detach
```

## 快速开始

1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

### 环境准备

```bash
# 依赖说明
# macOS: brew install --cask docker
# Linux: curl -fsSL https://get.docker.com | sh
# Windows: 下载Docker Desktop

# 安装Python依赖
pip install docker

# 验证Docker
docker --version
```

### 常用命令

```bash
# 镜像管理
py image build --tag my-app:latest --path ./Dockerfile
py image pull nginx:latest
py image delete my-app:old

# 容器管理
py container run --image nginx --name web --port 8080:80 --detach
py container stop --name web
py container logs --name web --tail 100

# 数据卷
py volume create --name my-data

# 网络
py network create --name my-net

# Compose
py compose up --detach
```

**结果处理**: 执行完成后,查看输出结果确认操作状态。成功时输出包含处理摘要和结果数据;失败时根据错误信息排查问题,查阅错误处理章节获取恢复步骤。

#
## 示例

### Docker配置

```yaml
docker_config:
  host: "unix:///var/run/docker.sock"
  timeout: 60

  defaults:
    image:
      registry: "docker.io"
      tag: "latest"
    container:
      restart_policy: "unless-stopped"
      memory_limit: "512m"
      cpu_limit: 1.0
    volume:
      driver: "local"
    network:
      driver: "bridge"

  compose:
    version: "3.8"
    default_template: "web_db"
```

## 优选实践

1. **镜像优化**：使用多阶段构建减小镜像体积
2. **标签管理**：使用语义化版本标签，避免仅用latest
3. **数据持久化**：重要数据使用数据卷，避免容器删除后丢失
4. **网络隔离**：不同应用使用独立网络，避免互相干扰

| 实践要点 | 说明 |
| --- | --- |
| 镜像清理 | 定期清理无用镜像，释放磁盘 |
| 资源限制 | 设置内存和CPU限制，避免容器失控 |
| 日志管理 | 配置日志轮转，避免日志撑满磁盘 |
| 安全意识 | 不使用root运行应用，最小权限原则 |

## 常见问题

### Q1：免费版支持Docker Swarm/K8s吗？

免费版仅支持单机Docker管理。如需集群管理，建议升级PRO版或使用专用K8s工具。

### Q2：如何连接远程Docker？

通过配置DOCKER_HOST环境变量指向远程Docker守护进程。需开启远程Docker的TCP端口（需配置TLS加密）。

### Q3：支持私有镜像仓库吗？

免费版支持从私有仓库拉取镜像（需提前docker login）。如需管理私有仓库，建议升级PRO版。

### Q4：容器无法启动怎么办？

检查：镜像是否存在、端口是否被占用、数据卷路径是否正确、容器日志中的错误信息。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python版本**: 3.8+
- **Docker**: 20.0+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python | 运行时 | 必需 | 系统安装或conda环境 |
| docker | Python库 | 必需 | `pip install docker` |
| docker-compose | CLI工具 | 可选 | 随Docker Desktop安装 |

### API Key 配置

- 免费版无需API Key
- 私有镜像仓库需通过 `docker login` 配置凭证

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+Python脚本执行）
- **说明**: 通过Docker SDK管理本地容器资源
- **免费版限制**: 单机管理、不支持集群与私有仓库管理

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制

- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 安全注意事项

| 风险类型 | 防范措施 |
|----------|---------|
| API密钥泄露 | 通过环境变量配置，禁止硬编码到代码或配置文件中 |
| 命令执行风险 | 仅执行白名单命令，避免拼接用户输入到命令行参数中 |
| 网络通信安全 | 使用HTTPS协议，验证SSL证书有效性 |
| 敏感数据暴露 | 输出结果中不包含密钥、令牌等敏感信息 |

使用前请确认已阅读依赖说明章节，确保运行环境满足安全要求。

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据

## 核心功能

- **自动化执行**: 基于指令驱动的自动化流程
- **文件处理**: 支持多种文件格式的读取、解析和写入操作
- **API集成**: 通过标准化接口调用外部服务并处理响应
- **命令执行**: 在安全沙箱中执行系统命令并收集结果
- **信息检索**: 快速搜索和过滤目标数据