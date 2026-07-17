---
slug: api-integration
name: api-integration
version: "1.0.0"
displayName: "api-integration - API é\x9B\x86æ\x88\x90"
summary: API 集成技能 - 掌握 RESTful API 调用、GraphQL 支持、API 认证管理等核心能力
license: MIT-0
description: |-
  API 集成技能 - 掌握 RESTful API 调用、GraphQL 支持、API 认证管理等核心能力\n\n核心能力:\n- 集成工具领域的专业化AI辅助工具\n\
  - 基于高人气开源Skill深度优化升级\n- 移除风险代码,增强安全性和稳定性\n\n适用场景:\n- 第三方API集成、平台对接、数据同步\n- 独立开发者与一人公司效率提升\n\
  - 自动化工作流与智能决策辅助\n\n差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。\n\n\
  触发关键词: é\x9B\x86æ\x88\x90, api, api-integration, 掌握, restful, 调用, 支持, 集成技能
tags: '[''Integrations'']'
tools: '[read, exec]'
---

# api-integration - API éæ

**Slogan：** 连接世界，集成万物

---

## 📋 技能描述

**提供完整的 API 集成能力，从 RESTful 到 GraphQL，**
**帮助 AI Agent 快速接入第三方服务，扩展能力边界。**

---

## 🎯 核心知识

### 1. RESTful API

```text
HTTP 方法：
- GET - 获取资源
- POST - 创建资源
- PUT - 更新资源
- DELETE - 删除资源

状态码：
- 200 - 成功
- 201 - 创建成功
- 400 - 请求错误
- 401 - 未授权
- 404 - 资源不存在
- 500 - 服务器错误
```

---

### 2. 认证方式

| 方式 | 说明 | 安全性 |
| --- | --- | --- |
| **API Key** | 简单密钥 | 中 |
| **OAuth2** | 授权框架 | 高 |
| **JWT** | Token 认证 | 高 |
| **Basic Auth** | 基础认证 | 低 |

---

### 3. GraphQL

```text
特点：
- 按需查询
- 强类型
- 单一端点
- 实时订阅
```

---

## 🛠️ 应用能力

### 能力 1：RESTful 调用

```python
import requests

def call_api(endpoint, method='GET', data=None, headers=None):
    response = requests.request(
        method=method,
        url=endpoint,
        json=data,
        headers=headers
    )
    response.raise_for_status()
    return response.json()
```

### 能力 2：认证管理

```python
def get_oauth_token(client_id, client_secret):
    response = requests.post(
        'https://api.example.com/oauth/token',
        data={
            'grant_type': 'client_credentials',
            'client_id': client_id,
            'client_secret': client_secret
        }
    )
    return response.json()['access_token']
```

### 能力 3：错误处理

```python
def safe_api_call(endpoint):
    try:
        return call_api(endpoint)
    except requests.exceptions.HTTPError as e:
        if e.response.status_code == 404:
            return {'error': 'Resource not found'}
        elif e.response.status_code == 401:
            return {'error': 'Unauthorized'}
        else:
            return {'error': str(e)}
```

---

## 💚 滚滚的话

**好的 API 集成，**
**稳定、安全、高效。**

**滚滚陪你一起，**
**连接更多服务！** 🔌💚

---

**创建人：** 滚滚 & 地球人
**创建时间：** 2026-03-15
**状态：** ✅ 学习完成

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
