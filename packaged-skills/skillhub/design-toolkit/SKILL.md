---
slug: "design-toolkit"
name: "design-toolkit"
version: 1.0.1
displayName: "设计偏好工具箱-专业版"
summary: "企业级视觉偏好管理系统，支持多媒介、品牌系统、团队协作与批量设计生成。。设计偏好工具箱专业版，面向团队与企业的视觉偏好管理平台。核心能力： - 覆盖 UI、图形、视频、印刷、3D 五大媒介的"
license: "MIT"
edition: "pro"
description: |-
  设计偏好工具箱专业版，面向团队与企业的视觉偏好管理平台。核心能力：
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

  差异化：专业版在免费版基础上扩展至五大多媒介...
tags:
  - Creative
  - Design
  - Enterprise
  - BrandSystem
  - 设计
  - UI/UX
  - 创意
  - self
  - brand
  - user_id
  - design-preferences
tools:
  - read
  - exec
  - write
homepage: ""
category: "Creative"
---
# 设计偏好工具箱-专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 设计偏好工具箱-专业版企业级视觉偏好管理 | 不支持 | 支持 |
| 设计偏好工具箱-专业版队协作与批量设计生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |
| 自定义模型微调 | 不支持 | 支持 |

## 核心能力

### 能力对比
| 能力维度 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 支持媒介 | UI、图形（2类） | UI、图形、视频、印刷、3D（5类） |
| 用户模式 | 单用户 | 多用户团队协作 |
| 品牌系统 | 不支持 | 完整品牌系统管理 |
| 偏好维度 | 审美、配色、字体 | 审美、配色、字体、动效、深度、布局、交互 |
| 一致性校验 | 手动检查 | 自动校验与修正建议 |
| 批量操作 | 不支持 | 批量设计任务偏好注入 |
| 数据管理 | 单文件 | 多项目、多档案、导入导出 |
| 团队共享 | 手动复制 | 权限化共享与版本控制 |

### 核心能力(补充)
```text
多媒介支持:
  - UI Design（界面设计）
  - Graphic Design（图形设计）
  - Video（视频/动效）
  - Print（印刷物料）
  - 3D（三维资产）
# ...
团队协作:
  - 多用户偏好档案
  - 角色权限控制（管理员/设计师/观察者）
  - 偏好变更审批流程
  - 版本历史与回滚
# ...
品牌系统:
  - 品牌色彩体系
  - 字体规范体系
  - 组件风格规范
  - 一致性自动校验
# ...
工作流集成:
  - 批量设计任务偏好注入
  - CI/CD 设计审查钩子
  - 跨项目偏好同步
  - API 接口对接
```

**处理**: 解析核心能力的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回核心能力的处理结果,包含执行状态码、结果数据和执行日志.
### 能力维度

针对能力维度,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供能力维度相关的配置参数、输入数据和处理选项.
**输出**: 返回能力维度的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`能力维度`的配置文档进行参数调优
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业设计团队统一视觉语言
当多个设计师协作时，确保所有人的输出符合品牌规范.
```python
# 示例
class TeamPreferenceManager:
    """团队偏好管理器"""
# ...
    def __init__(self, team_id, brand_system):
        self.team_id = team_id
        self.brand = brand_system
        self.members = {}
# ...
    def register_member(self, user_id, role="designer"):
        """注册团队成员"""
        self.members[user_id] = {
            "role": role,
            "personal_prefs": {},
            "brand_overrides": {}
        }
# ...
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
# ...
    def _resolve_conflicts(self, personal, brand):
        """冲突消解：品牌规范优先"""
        resolved = brand.copy()
        for key, value in personal.items():
            if key not in brand:  # 品牌未定义的维度采纳个人偏好
                resolved[key] = value
        return resolved
# ...
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
同时进行多个项目时，确保所有项目遵循同一品牌系统.
```bash
#!/bin/bash
# 多项目偏好同步脚本
BRAND_PROFILE="~/.design-preferences/brand-system.json"
PROJECTS_DIR="~/projects"
# ...
# 遍历所有项目，注入品牌偏好
for project in "$PROJECTS_DIR"/*/; do
    project_name=$(basename "$project")
    target="${project}.design-preferences/profile.md"
# ...
    # 生成项目级偏好文件（品牌系统 + 项目定制）
    cat > "$target" << EOF
# ${project_name} 设计偏好
# ...
## 使用流程
# ...
### 优秀步：从免费版升级
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
# ...
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
# ...
### 第三步：启动批量工作流
```bash
# 运行批量偏好注入
python3 batch_inject.py --brand ~/.design-preferences/brand-system.json \
                        --tasks ./design-tasks.json \
                        --output ./enriched-tasks/
```
# ...
#
## 输入格式
# ...
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | design-toolkit处理的内容输入 |,  |
| content | string | 否 | design-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |
# ...
## 输出格式
# ...
```json
{
  "success": true,
  "data": {
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    result: "toolkit 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```
# ...
输出模板参考: `assets/output.json`
# ...
## 异常处理
# ...
# ...
| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 
# ...
## 依赖说明
# ...
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（批量处理与API集成功能需要）
- **Node.js**: 16+（团队协作功能需要）
# ...
### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| Python 3.8+ | 运行时 | 推荐 | python.org 官方下载 |
| jq | 工具 | 可选 | 系统包管理器安装 |
| JSON Schema | 规范 | 推荐 | 内置验证器 |
# ...
### API Key 配置
- 本Skill采用纯Markdown指令驱动，无需额外API Key
- 团队协作功能如需远程同步，需配置团队服务端点（可选）
# ...
### 可用性分类
- **分类**: MD+EXEC（Markdown指令 + 命令行执行）
- **说明**: 企业级AI Skill，支持多用户协作、批量操作与系统集成的设计偏好管理
- **适用规模**: 团队与企业级，支持多项目并行
- **兼容性**: 与免费版完全兼容，支持无缝升级
# ...
## 案例展示
# ...
### 示例1: 基础用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```
# ...
### 示例2: 进阶用法
**输入**:
```json
{
  "content": "示例数据",
  "content": "示例数据",
  "style": "示例数据"
}
```
**输出**:
```
示例数据
```
# ...
### 示例3: 边界情况 - 边界情况
**输入**:
```json
{
  "content": "示例数据"
}
```
**输出**:
```
示例数据
```
# ...
## 常见问题
# ...
### Q: 如何从免费版升级到专业版？
A: 直接安装专业版，使用 `import` 命令导入免费版偏好文件即可。所有免费版数据完整保留，并自动扩展至多媒介支持.
# ...
### Q: 团队成员的偏好冲突如何处理？
A: 专业版采用三层优先级：品牌系统 > 团队偏好 > 个人偏好。冲突时品牌系统优先，个人偏好中未被品牌系统覆盖的维度仍然生效.
# ...
### Q: 专业版支持多少种媒介？
A: 专业版支持五大媒介：UI 设计、图形设计、视频/动效、印刷物料、3D 资产。免费版仅支持前两种.
# ...
### Q: 批量操作的性能如何？
A: 专业版支持并行批量处理，单批可处理 500+ 设计任务。偏好注入采用缓存机制，重复媒介类型无需重复加载.
# ...
### Q: 品牌系统变更如何通知团队？
A: 品牌系统变更经审批后，自动推送通知至所有团队成员。各项目的偏好文件在下一次设计任务时自动同步更新.
# ...
### Q: 可以与设计工具集成吗？
A: 专业版提供标准 API 接口，可与 Figma、Sketch 等设计工具对接，实现偏好实时同步.
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
# ...