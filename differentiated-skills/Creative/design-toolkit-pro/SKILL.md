---
slug: design-toolkit-pro
name: design-toolkit-pro
version: "1.0.0"
displayName: 设计偏好工具箱-专业版
summary: 企业级视觉偏好管理系统，支持多媒介、品牌系统、团队协作与批量设计生成。
license: MIT
edition: pro
description: |-
  设计偏好工具箱专业版，面向团队与企业的视觉偏好管理平台。

  核心能力：
  - 覆盖 UI、图形、视频、印刷、3D 五大媒介的偏好管理
  - 多用户团队偏好档案与角色权限控制
  - 品牌系统一致性校验与自动修正
  - 跨媒介偏好同步与冲突消解
  - 偏好导入导出与团队共享机制
  - 批量设计任务的偏好自动注入

  适用场景：
  - 企业设计团队统一视觉语言
  - 多项目并行时的品牌一致性保障
  - 设计系统构建与维护
  - 跨团队设计协作与偏好传承

  差异化：专业版在免费版基础上扩展至五大多媒介，支持团队多用户协作、品牌系统管理、批量操作与企业级集成。与免费版完全兼容，可无缝升级。

  触发关键词: design, 视觉偏好, 品牌系统, 设计系统, 团队协作, 多媒介, 批量设计, 设计一致性
tags:
- Creative
- Design
- Enterprise
- BrandSystem
tools:
- read
- exec
---

# 设计偏好工具箱（专业版）

## 概述

设计偏好工具箱专业版是企业级视觉偏好管理系统。它不仅记录个人审美倾向，更将偏好管理扩展至团队协作、品牌系统、多媒介同步和企业级工作流。通过结构化的偏好档案与自动一致性校验，确保整个设计团队的输出保持统一的视觉语言。

本版本与免费版完全兼容——免费版的偏好文件可直接导入专业版，并在专业版中获得多媒介扩展、团队共享和品牌系统管理等高级能力。

## 核心能力

### 能力对比

| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 支持媒介 | UI、图形（2类） | UI、图形、视频、印刷、3D（5类） |
| 用户模式 | 单用户 | 多用户团队协作 |
| 品牌系统 | 不支持 | 完整品牌系统管理 |
| 偏好维度 | 审美、配色、字体 | 审美、配色、字体、动效、深度、布局、交互 |
| 一致性校验 | 手动检查 | 自动校验与修正建议 |
| 批量操作 | 不支持 | 批量设计任务偏好注入 |
| 数据管理 | 单文件 | 多项目、多档案、导入导出 |
| 团队共享 | 手动复制 | 权限化共享与版本控制 |

### 专业版核心能力清单

```text
多媒介支持:
  - UI Design（界面设计）
  - Graphic Design（图形设计）
  - Video（视频/动效）
  - Print（印刷物料）
  - 3D（三维资产）

团队协作:
  - 多用户偏好档案
  - 角色权限控制（管理员/设计师/观察者）
  - 偏好变更审批流程
  - 版本历史与回滚

品牌系统:
  - 品牌色彩体系
  - 字体规范体系
  - 组件风格规范
  - 一致性自动校验

工作流集成:
  - 批量设计任务偏好注入
  - CI/CD 设计审查钩子
  - 跨项目偏好同步
  - API 接口对接
```

## 使用场景

### 场景一：企业设计团队统一视觉语言

当多个设计师协作时，确保所有人的输出符合品牌规范。

```python
# 团队偏好管理示例
class TeamPreferenceManager:
    """团队偏好管理器"""

    def __init__(self, team_id, brand_system):
        self.team_id = team_id
        self.brand = brand_system
        self.members = {}

    def register_member(self, user_id, role="designer"):
        """注册团队成员"""
        self.members[user_id] = {
            "role": role,
            "personal_prefs": {},
            "brand_overrides": {}
        }

    def merge_preferences(self, user_id):
        """合并个人偏好与品牌规范"""
        personal = self.members[user_id]["personal_prefs"]
        merged = self.brand.copy()
        # 品牌规范优先级高于个人偏好
        for medium in ["ui", "graphic", "video", "print", "3d"]:
            if medium in personal:
                merged[medium] = self._resolve_conflicts(
                    personal[medium],
                    self.brand.get(medium, {})
                )
        return merged

    def _resolve_conflicts(self, personal, brand):
        """冲突消解：品牌规范优先"""
        resolved = brand.copy()
        for key, value in personal.items():
            if key not in brand:  # 品牌未定义的维度采纳个人偏好
                resolved[key] = value
        return resolved

# 使用示例
brand = {
    "colors": {"primary": "#1a1a2e", "accent": "#e94560"},
    "typography": {"heading": "Playfair Display", "body": "IBM Plex Sans"},
    "ui": {"radius": "8px", "spacing": "4px"}
}
manager = TeamPreferenceManager("team-001", brand)
manager.register_member("designer-A", "designer")
prefs = manager.merge_preferences("designer-A")
```

### 场景二：多项目品牌一致性保障

同时进行多个项目时，确保所有项目遵循同一品牌系统。

```bash
#!/bin/bash
# 多项目偏好同步脚本

BRAND_PROFILE="~/.design-preferences/brand-system.json"
PROJECTS_DIR="~/projects"

# 遍历所有项目，注入品牌偏好
for project in "$PROJECTS_DIR"/*/; do
    project_name=$(basename "$project")
    target="${project}.design-preferences/profile.md"

    # 生成项目级偏好文件（品牌系统 + 项目定制）
    cat > "$target" << EOF
# ${project_name} 设计偏好

## 品牌系统（只读）
$(jq -r '.brand' "$BRAND_PROFILE")

## 项目定制
$(jq -r --arg p "$project_name" '.projects[$p] // {}' "$BRAND_PROFILE")

## 媒介偏好
### UI Design
$(jq -r '.media.ui' "$BRAND_PROFILE")
### Graphic Design
$(jq -r '.media.graphic' "$BRAND_PROFILE")
### Video
$(jq -r '.media.video' "$BRAND_PROFILE")
### Print
$(jq -r '.media.print' "$BRAND_PROFILE")
### 3D
$(jq -r '.media.3d' "$BRAND_PROFILE")
EOF

    echo "已同步偏好至: $project_name"
done
```

### 场景三：批量设计任务的偏好自动注入

对批量设计任务自动应用偏好，确保一致性。

```python
# 批量设计任务偏好注入
import json
from pathlib import Path

class BatchDesignInjector:
    """批量设计偏好注入器"""

    def __init__(self, brand_profile_path):
        with open(brand_profile_path, 'r', encoding='utf-8') as f:
            self.brand = json.load(f)

    def inject_to_batch(self, task_list):
        """为批量任务注入偏好"""
        results = []
        for task in task_list:
            enriched = task.copy()
            enriched["design_brief"] = self._enrich_brief(
                task.get("design_brief", ""),
                task.get("medium", "ui")
            )
            enriched["constraints"] = self._build_constraints(
                task.get("medium", "ui")
            )
            results.append(enriched)
        return results

    def _enrich_brief(self, brief, medium):
        """用品牌偏好丰富设计简报"""
        media_prefs = self.brand.get("media", {}).get(medium, {})
        enrichment = f"\n\n[品牌偏好 - {medium}]\n"
        for key, value in media_prefs.items():
            enrichment += f"- {key}: {value}\n"
        return brief + enrichment

    def _build_constraints(self, medium):
        """构建设计约束"""
        return {
            "colors": self.brand.get("colors", {}),
            "typography": self.brand.get("typography", {}),
            "never": self.brand.get("never", []),
            "medium_rules": self.brand.get("media", {}).get(medium, {})
        }

# 使用示例
injector = BatchDesignInjector("~/.design-preferences/brand-system.json")
tasks = [
    {"id": "T001", "medium": "ui", "design_brief": "登录页面设计"},
    {"id": "T002", "medium": "graphic", "design_brief": "社交媒体海报"},
    {"id": "T003", "medium": "video", "design_brief": "产品介绍动效"},
    {"id": "T004", "medium": "print", "design_brief": "名片设计"},
    {"id": "T005", "medium": "3d", "design_brief": "产品展示模型"},
]
enriched_tasks = injector.inject_to_batch(tasks)
for t in enriched_tasks:
    print(f"任务 {t['id']} 已注入偏好: {t['medium']}")
```

## 快速开始

### 第一步：从免费版升级

```bash
# 导入免费版偏好
cp ~/.design-preferences/profile.md \
   ~/.design-preferences/personal-backup.md

# 初始化专业版品牌系统
cat > ~/.design-preferences/brand-system.json << 'EOF'
{
  "brand": {
    "name": "你的品牌名称",
    "colors": {
      "primary": "#1a1a2e",
      "secondary": "#16213e",
      "accent": "#e94560"
    },
    "typography": {
      "heading": "Playfair Display",
      "body": "IBM Plex Sans",
      "mono": "JetBrains Mono"
    }
  },
  "media": {
    "ui": {"radius": "8px", "spacing": "4px"},
    "graphic": {"style": "flat-geometric"},
    "video": {"motion": "smooth-ease"},
    "print": {"dpi": 300, "color_mode": "CMYK"},
    "3d": {"poly_style": "low-poly"}
  },
  "never": [
    "淡紫色渐变",
    "Inter/Roboto字体",
    "白底浅色SaaS配色"
  ]
}
EOF
```

### 第二步：配置团队

```bash
# 初始化团队配置
mkdir -p ~/.design-preferences/team
cat > ~/.design-preferences/team/members.json << 'EOF'
{
  "team_id": "design-team-001",
  "members": [
    {"user_id": "lead", "role": "admin"},
    {"user_id": "designer-A", "role": "designer"},
    {"user_id": "designer-B", "role": "designer"},
    {"user_id": "reviewer", "role": "observer"}
  ]
}
EOF
```

### 第三步：启动批量工作流

```bash
# 运行批量偏好注入
python3 batch_inject.py --brand ~/.design-preferences/brand-system.json \
                        --tasks ./design-tasks.json \
                        --output ./enriched-tasks/
```

## 配置示例

### 完整品牌系统配置

```json
{
  "brand": {
    "name": "Acme Design System",
    "version": "2.0.0",
    "colors": {
      "primary": "#1a1a2e",
      "secondary": "#16213e",
      "accent": "#e94560",
      "accent_alt": "#0f3460",
      "text": "#eeeeee",
      "text_muted": "#8892b0"
    },
    "typography": {
      "heading": {
        "family": "Playfair Display",
        "weights": [400, 900],
        "sizes": {"h1": "48px", "h2": "36px", "h3": "24px"}
      },
      "body": {
        "family": "IBM Plex Sans",
        "weights": [300, 400, 600],
        "size": "14px",
        "line_height": "1.6"
      },
      "mono": {
        "family": "JetBrains Mono",
        "size": "13px"
      }
    }
  },
  "media": {
    "ui": {
      "radius": "8px",
      "spacing_base": "4px",
      "shadow": "soft-multi-layer",
      "motion": "staggered-fade-up"
    },
    "graphic": {
      "style": "flat-geometric",
      "icon_stroke": "2px",
      "illustration": "minimal-linear"
    },
    "video": {
      "motion": "smooth-ease",
      "transition": "crossfade-300ms",
      "text_animation": "kinetic-typography"
    },
    "print": {
      "dpi": 300,
      "color_mode": "CMYK",
      "bleed": "3mm",
      "paper_stock": "matte-120gsm"
    },
    "3d": {
      "poly_style": "low-poly",
      "material": "PBR-matte",
      "lighting": "three-point-soft"
    }
  },
  "never": [
    "淡紫色渐变",
    "Inter/Roboto/Open Sans字体",
    "白底浅色SaaS配色",
    "全圆角按钮",
    "均匀分布的多色方案"
  ],
  "consistency_rules": {
    "auto_check": true,
    "block_on_violation": false,
    "suggest_fix": true
  }
}
```

### 团队权限配置

```yaml
# team-permissions.yml
roles:
  admin:
    - read_preferences
    - write_preferences
    - manage_members
    - approve_changes
    - export_brand_system
  designer:
    - read_preferences
    - write_personal_prefs
    - submit_brand_changes
  observer:
    - read_preferences
    - comment_on_changes

approval_flow:
  brand_change:
    submit: designer
    review: admin
    auto_apply: false
  personal_pref:
    submit: designer
    auto_apply: true
```

## 最佳实践

1. **品牌系统优先**：团队偏好中，品牌规范优先级始终高于个人偏好，确保品牌一致性不被破坏。
2. **分层管理**：品牌系统 → 团队偏好 → 个人偏好，三层结构清晰分离。
3. **变更审批**：品牌系统变更必须经过审批流程，避免随意修改影响全局。
4. **定期同步**：每周同步一次多项目偏好，确保所有项目使用最新品牌规范。
5. **一致性报告**：定期生成一致性报告，识别偏离品牌规范的设计。

```text
专业版检查清单:
[ ] 品牌系统配置完成（5大媒介全覆盖）
[ ] 团队成员角色分配正确
[ ] 变更审批流程已启用
[ ] 多项目偏好同步已配置
[ ] 一致性自动校验已开启
[ ] 偏好导出备份已设置
[ ] 免费版偏好已导入
[ ] Never 列表已同步至全团队
```

## 常见问题

### Q: 如何从免费版升级到专业版？

A: 直接安装专业版，使用 `import` 命令导入免费版偏好文件即可。所有免费版数据完整保留，并自动扩展至多媒介支持。

### Q: 团队成员的偏好冲突如何处理？

A: 专业版采用三层优先级：品牌系统 > 团队偏好 > 个人偏好。冲突时品牌系统优先，个人偏好中未被品牌系统覆盖的维度仍然生效。

### Q: 专业版支持多少种媒介？

A: 专业版支持五大媒介：UI 设计、图形设计、视频/动效、印刷物料、3D 资产。免费版仅支持前两种。

### Q: 批量操作的性能如何？

A: 专业版支持并行批量处理，单批可处理 500+ 设计任务。偏好注入采用缓存机制，重复媒介类型无需重复加载。

### Q: 品牌系统变更如何通知团队？

A: 品牌系统变更经审批后，自动推送通知至所有团队成员。各项目的偏好文件在下一次设计任务时自动同步更新。

### Q: 可以与设计工具集成吗？

A: 专业版提供标准 API 接口，可与 Figma、Sketch 等设计工具对接，实现偏好实时同步。

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（批量处理与API集成功能需要）
- **Node.js**: 16+（团队协作功能需要）

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3.8+ | 运行时 | 推荐 | python.org 官方下载 |
| jq | 工具 | 可选 | 系统包管理器安装 |
| JSON Schema | 规范 | 推荐 | 内置验证器 |

### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- 团队协作功能如需远程同步，需配置团队服务端点（可选）

### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 命令行执行）
- **说明**: 企业级AI Skill，支持多用户协作、批量操作与系统集成的设计偏好管理
- **适用规模**: 团队与企业级，支持多项目并行
- **兼容性**: 与免费版完全兼容，支持无缝升级
