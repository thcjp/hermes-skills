---
slug: text-game-arcade-tool-pro
name: text-game-arcade-tool-pro
version: "1.0.0"
displayName: 文字游戏机专业版
summary: 企业级文字游戏平台,支持AI剧情、多人协作、图形界面与商业发布
license: Proprietary
edition: pro
description: |-
  面向游戏工作室、内容平台与教育机构的企业级文字游戏平台。
  核心能力: AI剧情生成、多人协作、图形界面、游戏编辑器、商业发布、多语言
  适用场景: 商业文字游戏开发、教育互动内容、IP衍生、内容平台运营
  差异化: 专业版支持AI剧情与商业化,与免费版游戏格式兼容
  触发关键词: AI剧情, 多人协作, 游戏编辑器, 商业发布, 多语言游戏, 内容平台
tags:
- 文字游戏
- 企业级
- AI剧情
- 游戏编辑器
- 商业发布
- 多人协作
tools:
  - - read
- exec
---
# 文字游戏机 (专业版)
## 概述
专业版面向游戏工作室、内容平台与教育机构,在免费版文字游戏生成之上,扩展 AI 剧情生成、多人协作、图形界面、游戏编辑器、商业发布、多语言等企业级能力。支持构建接近商业品质的文字游戏,适合 IP 衍生、教育互动、内容平台运营等专业场景。

专业版与免费版游戏格式完全兼容,个人创作者升级后现有游戏无缝迁移。

## 核心能力
| 能力模块 | 描述 | 免费版 | 专业版 |
|:--------|:-----|:------:|:------:|
| 多类型游戏 | 冒险、悬疑等 | 支持 | 支持 |
| 剧情分支 | 多结局 | 支持 | 支持 |
| 角色互动 | NPC 对话 | 支持 | 支持 (AI 增强) |
| AI 剧情生成 | 智能 NPC 与动态剧情 | 不支持 | 支持 |
| 多人协作 | 共同创作 | 不支持 | 支持 |
| 图形界面 | GUI 客户端 | 不支持 | 支持 |
| 游戏编辑器 | 可视化编辑 | 不支持 | 支持 |
| 商业发布 | 商业用途 | 个人 | 商业 |
| 多语言 | 多语言游戏 | 不支持 | 支持 |
| 游戏库 | 预设游戏 | 5 款 | 不限 |
| 数据分析 | 玩家行为分析 | 不支持 | 支持 |
| 优先支持 | 专属支持 | 不支持 | 支持 |

## 使用场景
### 场景一: AI 动态剧情
AI 实时生成剧情,玩家自由探索。

```python
import os
import requests
from datetime import datetime

API_BASE = "https://api.text-game-pro.local/v1"
ADMIN_KEY = os.environ["TEXT_GAME_ADMIN_KEY"]

class AIDynamicStory:
    def __init__(self, admin_key):
        self.headers = {"X-API-Key": admin_key, "X-Edition": "pro"}
        self.story_context = {
            "setting": "",
            "characters": [],
            "plot_points": [],
            "player_choices": [],
        }

    def generate_dynamic_scene(self, player_action, current_state):
        """AI 动态生成场景"""
        payload = {
            "player_action": player_action,
            "current_state": current_state,
            "context": self.story_context,
            "generate": [
                "scene_description",
                "npc_dialogue",
                "possible_choices",
                "state_changes",
                "branching_consequences",
            ],
            "tone": "consistent_with_story",
            "language": "zh",
        }
        resp = requests.post(
            f"{API_BASE}/ai/story/generate",
            headers=self.headers,
            json=payload,
            timeout=60,
        )
        return resp.json()

    def ai_npc_dialogue(self, npc_id, player_input, relationship_level):
        """AI NPC 对话"""
        payload = {
            "npc_id": npc_id,
            "player_input": player_input,
            "relationship": relationship_level,
            "personality": "consistent",
            "memory": True,  # 记住之前的对话
            "emotion": True,  # 情感反应
        }
        resp = requests.post(
            f"{API_BASE}/ai/npc/dialogue",
            headers=self.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

story = AIDynamicStory(ADMIN_KEY)
# 玩家自由输入,AI 实时响应
scene = story.generate_dynamic_scene(
    player_action="我决定跳过窗户逃跑",
    current_state={"location": "二楼书房", "pursued": True},
)
```

### 场景二: 多人协作创作
多人共同创作一个大型文字游戏。

```python
class CollaborativeGameProject:
    def create_project(self, name, collaborators, structure):
        """创建协作游戏项目"""
        payload = {
            "name": name,
            "collaborators": collaborators,
            "structure": structure,
            "roles": {
                "writer": ["create_scenes", "edit_dialogue"],
                "designer": ["design_choices", "balance_gameplay"],
                "editor": ["review", "approve", "consistency_check"],
                "publisher": ["publish", "manage_versions"],
            },
            "version_control": True,
            "real_time_editing": True,
        }
        resp = requests.post(
            f"{API_BASE}/projects",
            headers=story.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()

    def assign_scene(self, project_id, scene_id, writer_id):
        """分配场景给作者"""
        payload = {
            "project_id": project_id,
            "scene_id": scene_id,
            "assignee": writer_id,
            "deadline": "2026-08-01",
            "review_required": True,
        }
        resp = requests.post(
            f"{API_BASE}/projects/assign",
            headers=story.headers,
            json=payload,
            timeout=30,
        )
        return resp.json()
```

### 场景三: 商业发布
将文字游戏发布到商业平台。

```python
def publish_game(game_id, platforms, metadata):
    """发布游戏到平台"""
    payload = {
        "game_id": game_id,
        "platforms": platforms,  # [steam, itch_io, app_store, google_play]
        "metadata": metadata,
        "monetization": {
            "model": "premium",  # premium, freemium, episodic
            "price_usd": 9.99,
            "demo_available": True,
        },
        "localization": ["zh", "en", "ja", "ko"],
        "age_rating": "T",
        "achievements": True,
        "cloud_saves": True,
    }
    resp = requests.post(
        f"{API_BASE}/publish",
        headers=story.headers,
        json=payload,
        timeout=300,
    )
    return resp.json()
```

## 不适用场景

以下场景文字游戏机专业版不适合处理：

- 专业医学法律翻译认证
- 同声传译
- 文学创作翻译


## 触发条件

需要文本翻译、多语言转换、本地化处理时使用。不适用于非本工具能力范围的需求。


## 快速开始
### 步骤 1: 申请专业版账户
联系销售开通专业版,获取管理员凭证与租户 ID。

### 步骤 2: 配置凭证
```bash
export TEXT_GAME_ADMIN_KEY="sk_pro_admin_xxx"
export TEXT_GAME_ORG_ID="org_your_id"
export TEXT_GAME_EDITION="pro"
```

### 步骤 3: 创建游戏项目
```bash
curl -X POST -H "X-API-Key: $TEXT_GAME_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"name":"暗夜侦探","type":"mystery","team":["writer1","writer2"]}' \
  "https://api.text-game-pro.local/v1/projects"
```

### 步骤 4: 启用 AI 剧情
```bash
curl -X POST -H "X-API-Key: $TEXT_GAME_ADMIN_KEY" \
  -H "Content-Type: application/json" \
  -d '{"game_id":"g001","ai_features":["dynamic_dialogue","branching_plot","npc_memory"]}' \
  "https://api.text-game-pro.local/v1/ai/enable"
```

## 示例
### 企业级配置
```yaml
# /etc/text-game/pro.yaml
edition: pro
api:
  base_url: https://api.text-game-pro.local/v1
  admin_key: ${TEXT_GAME_ADMIN_KEY}
  org_id: ${TEXT_GAME_ORG_ID}
  timeout: 300

ai_story:
  enabled: true
  features:
    - dynamic_scene_generation
    - npc_dialogue
    - branching_plot
    - emotion_system
    - memory_system
  models:
    story_generator: "gpt-4-class"
    npc_dialogue: "gpt-3.5-class"
  personalization: high

collaboration:
  max_collaborators: 20
  roles: [writer, designer, editor, publisher, tester]
  version_control: git
  real_time_editing: true
  review_workflow: required

editor:
  visual: true
  scene_graph: true
  branching_tree: true
  testing_mode: true
  asset_management: true

publishing:
  platforms: [steam, itch_io, app_store, google_play, web]
  monetization: [premium, freemium, episodic, subscription]
  localization: [zh, en, ja, ko, fr, de, es]
  age_ratings: [esrb, pegi, cero]
  achievements: true
  cloud_saves: true

analytics:
  player_behavior: true
  completion_rate: true
  choice_popularity: true
  drop_off_points: true
  ab_testing: true
```

### AI NPC 系统
```python
def create_ai_npc(npc_config):
    """创建 AI 驱动的 NPC"""
    payload = {
        "name": npc_config["name"],
        "personality": npc_config["personality"],
        "background": npc_config["background"],
        "goals": npc_config["goals"],
        "relationship_system": {
            "initial_level": 0,
            "factors": ["dialogue_choices", "actions", "gifts"],
            "effects_on_dialogue": True,
        },
        "memory": {
            "long_term": True,
            "remembers_player": True,
            "references_past": True,
        },
        "emotion": {
            "enabled": True,
            "visible": True,
            "affects_dialogue": True,
        },
    }
    resp = requests.post(
        f"{API_BASE}/ai/npc/create",
        headers=story.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()
```

### 玩家行为分析
```python
def analyze_player_behavior(game_id, period):
    """分析玩家行为"""
    payload = {
        "game_id": game_id,
        "period": period,
        "metrics": [
            "completion_rate",
            "avg_session_length",
            "choice_distribution",
            "drop_off_points",
            "popular_paths",
            "ending_distribution",
        ],
        "insights": True,
        "recommendations": True,
    }
    resp = requests.post(
        f"{API_BASE}/analytics/players",
        headers=story.headers,
        json=payload,
        timeout=120,
    )
    return resp.json()
```

## 最佳实践
### 1. AI 剧情一致性
```python
def maintain_story_consistency(story_context, new_content):
    """保持剧情一致性"""
    payload = {
        "context": story_context,
        "new_content": new_content,
        "check": [
            "character_consistency",
            "plot_holes",
            "timeline_accuracy",
            "world_building_rules",
            "tone_consistency",
        ],
        "auto_fix": True,
    }
    resp = requests.post(
        f"{API_BASE}/ai/consistency-check",
        headers=story.headers,
        json=payload,
        timeout=60,
    )
    return resp.json()
```

### 2. 协作工作流
```python
def create_writing_workflow(project_id):
    """创作工作流"""
    return {
        "stages": [
            {"name": "剧情大纲", "assignee": "lead_writer", "review": True},
            {"name": "场景撰写", "assignee": "writers", "parallel": True},
            {"name": "对话润色", "assignee": "dialogue_editor"},
            {"name": "一致性检查", "assignee": "continuity_editor", "auto": True},
            {"name": "测试游玩", "assignee": "testers"},
            {"name": "发布准备", "assignee": "publisher"},
        ],
        "version_control": True,
        "feedback_loop": True,
    }
```

### 3. 多语言本地化
```python
def localize_game(game_id, target_languages):
    """游戏多语言本地化"""
    payload = {
        "game_id": game_id,
        "target_languages": target_languages,
        "components": ["story_text", "dialogue", "ui", "achievements"],
        "cultural_adaptation": True,
        "native_review": True,
    }
    resp = requests.post(
        f"{API_BASE}/localize",
        headers=story.headers,
        json=payload,
        timeout=600,
    )
    return resp.json()
```

## 常见问题
### Q1: 专业版与免费版游戏格式兼容吗?
完全兼容。专业版在免费版基础上扩展,现有游戏可直接迁移。

### Q2: AI 剧情质量如何?
AI 实时生成剧情接近人工创作水准,但建议关键节点人工把关。

### Q3: 商业发布的版权归属?
专业版生成的游戏版权归用户所有,可用于商业发布。

### Q4: 多人协作支持多少人?
支持 20 人同时协作,实时同步编辑。

### Q5: 发布到哪些平台?
Steam、itch.io、App Store、Google Play、Web 等主流平台。

## 依赖说明
### 运行环境
- **Agent 平台**: 支持 SKILL.md 规范的任意 AI Agent (Claude Code、Cursor、Codex、Gemini CLI 等)
- **操作系统**: Windows / macOS / Linux (生产环境推荐 Linux)
- **网络**: 需访问专业版服务
- **Python**: 3.9+ (用于脚本化操作)

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Text Game Pro API | 在线 API | 必需 | 联系销售开通专业版 |
| LLM API | 推理服务 | 必需 | 由 Agent 内置 LLM 提供 |
| Python 3.9+ | 运行时 | 推荐 | python.org 下载 |
| requests 库 | Python 库 | 推荐 | `pip install requests` |
| 数据库 | 数据存储 | 可选 | 兼容主流关系型数据库 (使用 `数据库` 上下文) |

### API Key 配置
```bash
# 专业版凭证
export TEXT_GAME_ADMIN_KEY="sk_pro_admin_xxx"
export TEXT_GAME_ORG_ID="org_your_id"
export TEXT_GAME_EDITION="pro"

# 可选: 发布平台
export STEAM_API_KEY="..."
export APPLE_APP_STORE_KEY="..."
export GOOGLE_PLAY_KEY="..."

# 可选: AI 模型
export OPENAI_API_KEY="..."
export ANTHROPIC_API_KEY="..."
```

### 可用性分类
- **分类**: MD+EXEC (Markdown 指令 + 命令行执行)
- **说明**: 本 Skill 面向游戏工作室与内容平台,通过自然语言指令驱动 Agent 调用 Pro API,完成 AI 剧情、协作创作、商业发布
- **专业版特性**: AI 剧情、多人协作、图形界面、游戏编辑器、商业发布、多语言、数据分析
- **兼容性**: 与免费版游戏格式完全兼容,支持平滑升级

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 已知限制
- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
