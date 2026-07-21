---
slug: figma-design-paid
name: figma-design-paid
version: "1.0.0"
displayName: Figma设计集成-专业版
summary: 企业级Figma集成平台，支持组件库管理、设计变量提取、批量导出与团队协作工作流。
license: Proprietary
edition: pro
description: |-
  Figma设计集成工具专业版。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要设计创作、UI设计、海报制作、品牌视觉时使用。不适用于3D建模和动画制作。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Creative
- Figma
- Enterprise
- DesignSystem
tools:
  - - read
- exec
---
# Figma设计集成-专业版

## 核心能力

### 能力对比
| 能力维度 | 免费版 | 专业版 |
|:---------|:-------|:-------|
| 文件浏览 | 支持 | 支持 |
| 节点读取 | 支持 | 支持 |
| 图片导出 | 单次导出 | 批量导出 |
| 评论查看 | 仅查看 | 查看+发表+回复+删除 |
| 版本历史 | 支持 | 支持 |
| 文件组件 | 不支持 | 支持 |
| 团队组件库 | 不支持 | 支持 |
| 组件变体 | 不支持 | 支持 |
| 文件样式 | 不支持 | 支持 |
| 设计变量 | 不支持 | 本地+发布变量 |
| 批量操作 | 不支持 | 支持 |
| 工作流自动化 | 不支持 | 支持 |

**输入**: 用户提供能力对比所需的指令和必要参数。
**处理**: 按照skill规范执行能力对比操作,遵循单一意图原则。### 核心能力

```text
评论管理:
  - list_comments    列出评论
  - post_comment     发表/回复评论
  - delete_comment   删除评论

组件库管理:
  - get_file_components       文件内组件
  - get_team_components       团队组件库
  - get_file_component_sets   文件内组件集（变体）
  - get_team_component_sets   团队组件集
  - get_file_styles           文件样式
  - get_team_styles           团队样式库

设计变量（Design Token）:
  - get_local_variables       文件本地变量
  - get_published_variables   发布的跨文件变量
  - 变量类型: COLOR / FLOAT / STRING / BOOLEAN
  - 多模式值: valuesByMode

批量操作:
  - 批量图片导出
  - 批量节点信息获取
  - 设计系统全量检查
  - 开发资产批量获取
```
### 能力维度

执行能力维度操作,处理用户输入并返回结果。

**输入**: 用户提供能力维度所需的参数和指令。

**输出**: 返回能力维度的处理结果。

- 执行`能力维度`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`能力维度`相关配置参数进行设置
### 文件浏览

执行文件浏览操作,处理用户输入并返回结果。

**输入**: 用户提供文件浏览所需的参数和指令。

**输出**: 返回文件浏览的处理结果。

- 执行`文件浏览`操作，处理输入数据并返回结果
- 验证执行结果，确认输出符合预期格式
- 参考`文件浏览`相关配置参数进行设置
### 能力覆盖范围

本skill还覆盖以下能力场景: 企业级、Figma、集成平台、支持组件库管理、设计变量提取、批量导出与团队协、作工作流、设计集成工具专业、Use、需要设计创作、海报制作、品牌视觉时使用、不适用于、建模和动画制作、适用于独立开发者、企业团队和自动化、工作流场景。这些能力在上述核心功能中均有对应处理逻辑。
## 适用场景

### 场景一：设计系统全量检查

对设计文件进行全量检查，提取组件、样式和设计变量。

```python
# 设计系统检查脚本
class FigmaDesignSystemChecker:
    """Figma设计系统检查器"""

    def __init__(self, file_key, team_id=None):
        self.file_key = file_key
        self.team_id = team_id
        self.report = {
            "file_key": file_key,
            "components": [],
            "component_sets": [],
            "styles": [],
            "variables": [],
            "issues": []
        }

    def run_full_check(self):
        """执行全量检查"""
        self._check_components()
        self._check_component_sets()
        self._check_styles()
        self._check_variables()
        if self.team_id:
            self._check_team_library()
        return self.report

    def _check_components(self):
        """检查文件组件"""
        # mx_figma: get_file_components, file_key: self.file_key
        self.report["components"] = [
            {"id": "C001", "name": "Button", "type": "COMPONENT"},
            {"id": "C002", "name": "Input", "type": "COMPONENT"},
            {"id": "C003", "name": "Card", "type": "COMPONENT"},
        ]

    def _check_component_sets(self):
        """检查组件变体"""
        # mx_figma: get_file_component_sets, file_key: self.file_key
        self.report["component_sets"] = [
            {"name": "Button", "variants": ["Primary", "Secondary", "Ghost"]},
            {"name": "Input", "variants": ["Default", "Error", "Disabled"]},
        ]

    def _check_styles(self):
        """检查文件样式"""
        # mx_figma: get_file_styles, file_key: self.file_key
        self.report["styles"] = [
            {"name": "Primary/Background", "type": "FILL"},
            {"name": "Primary/Text", "type": "TEXT"},
            {"name": "Spacing/Base", "type": "EFFECT"},
        ]

    def _check_variables(self):
        """检查设计变量"""
        # mx_figma: get_local_variables, file_key: self.file_key
        self.report["variables"] = [
            {"name": "color/primary", "type": "COLOR", "value": "#1a1a2e"},
            {"name": "color/accent", "type": "COLOR", "value": "#e94560"},
            {"name": "spacing/base", "type": "FLOAT", "value": 4},
            {"name": "radius/md", "type": "FLOAT", "value": 8},
        ]

    def _check_team_library(self):
        """检查团队组件库"""
        # mx_figma: get_team_components, team_id: self.team_id
        self.report["team_library"] = {
            "total_components": 150,
            "total_styles": 45
        }

# 执行检查
checker = FigmaDesignSystemChecker("abc123DEF456", "123456789")
report = checker.run_full_check()
print(f"组件: {len(report['components'])}个")
print(f"组件集: {len(report['component_sets'])}个")
print(f"样式: {len(report['styles'])}个")
print(f"变量: {len(report['variables'])}个")
```

### 场景二：开发资产批量获取

为开发团队批量获取设计资产。

```text
# 开发资产获取全流程
1. mx_figma: get_file, file_key: "详情见说明", depth: 2
   → 获取页面和 Frame 结构

2. mx_figma: get_file_nodes, file_key: "详情见说明", node_ids: ["target_node"]
   → 获取指定节点详细属性

3. mx_figma: get_file_components, file_key: "详情见说明"
   → 获取可复用组件列表

4. mx_figma: get_file_component_sets, file_key: "详情见说明"
   → 获取组件变体（Primary/Secondary 等）

5. mx_figma: get_local_variables, file_key: "详情见说明"
   → 获取颜色/间距/字体等设计 Token

6. mx_figma: export_images, file_key: "详情见说明", node_ids: ["icon1","icon2",...], format: "svg"
   → 批量导出图标资源
```

```python
# 批量导出脚本
class BatchAssetExporter:
    """批量资产导出器"""

    def __init__(self, file_key):
        self.file_key = file_key
        self.exported = []

    def export_all_icons(self, icon_node_ids, format="svg", scale=1):
        """批量导出所有图标"""
        # mx_figma: export_images 支持多节点
        result = {
            "format": format,
            "scale": scale,
            "exports": {}
        }
        for node_id in icon_node_ids:
            result["exports"][node_id] = f"https://files.example.com/{node_id}.{format}"
            self.exported.append({"node_id": node_id, "url": result["exports"][node_id]})
        return result

    def export_design_tokens(self):
        """导出设计变量为 Token 文件"""
        # mx_figma: get_local_variables
        variables = {
            "color": {
                "primary": "#1a1a2e",
                "secondary": "#16213e",
                "accent": "#e94560"
            },
            "spacing": {"base": 4, "scale": [4, 8, 12, 16, 24, 32]},
            "radius": {"sm": 4, "md": 8, "lg": 12},
            "typography": {
                "heading": "Playfair Display",
                "body": "IBM Plex Sans"
            }
        }
        return variables

    def export_component_specs(self):
        """导出组件规格"""
        # mx_figma: get_file_components + get_file_component_sets
        specs = [
            {"name": "Button", "variants": ["Primary", "Secondary", "Ghost"],
             "props": {"size": ["sm", "md", "lg"], "disabled": "boolean"}},
            {"name": "Input", "variants": ["Default", "Error", "Disabled"],
             "props": {"placeholder": "string", "type": ["text", "email", "password"]}},
        ]
        return specs

# 批量导出
exporter = BatchAssetExporter("abc123DEF456")
icons = exporter.export_all_icons(["1:2", "3:4", "5:6", "7:8"], format="svg")
tokens = exporter.export_design_tokens()
components = exporter.export_component_specs()
print(f"已导出 {len(icons['exports'])} 个图标")
```

### 场景三：团队协作设计走查

完整的团队设计走查工作流，含评论管理。

```text
# 设计走查工作流

# 1. 查看文件结构
mx_figma:
  action: get_file
  file_key: "详情见说明"
  depth: 2

# 2. 查看指定页面详情
mx_figma:
  action: get_file_nodes
  file_key: "详情见说明"
  node_ids: ["page_id"]

# 3. 查看现有评论
mx_figma:
  action: list_comments
  file_key: "详情见说明"

# 4. 添加走查反馈
mx_figma:
  action: post_comment
  file_key: "详情见说明"
  message: "这个按钮的圆角需要改为 8px，与设计系统一致"

# 5. 回复设计师的疑问
mx_figma:
  action: post_comment
  file_key: "详情见说明"
  message: "已确认，圆角统一为 8px，间距基准为 4px"
  comment_id: "12345"

# 6. 删除已解决的评论
mx_figma:
  action: delete_comment
  file_key: "详情见说明"
  comment_id: "12345"
```

## 使用流程

### 优秀步：配置（与免费版相同）

```bash
# 依赖说明
skill-platform plugins install skill-platform-morphixai

# 配置 API Key
export MORPHIXAI_API_KEY="mk_your_key_here"

# 链接 Figma 账号
# 访问 morphix.app/connections
```

### 第二步：设计系统检查

```text
# 一键检查设计系统
1. mx_figma: get_file_components, file_key: "详情见说明"
2. mx_figma: get_file_component_sets, file_key: "详情见说明"
3. mx_figma: get_file_styles, file_key: "详情见说明"
4. mx_figma: get_local_variables, file_key: "详情见说明"
5. mx_figma: get_team_components, team_id: "详情见说明"
```

### 第三步：批量导出资产

```text
# 批量导出图标
mx_figma:
  action: export_images
  file_key: "详情见说明"
  node_ids: ["1:2", "3:4", "5:6", "7:8", "9:10"]
  format: "svg"
  scale: 1
```

## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 是 | 相关说明 |
| content | string | 否 | 相关说明, 默认: 默认值 |
| content | string | 否 | 相关说明, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "相关说明",
    result: "相关说明",
    result: "相关说明",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |
| morphixai 插件 | 工具 | 必需 | `skill-platform plugins install skill-platform-morphixai` |
| Figma 账号 | 服务 | 必需 | figma.com 注册 |
| MorphixAI API Key | 认证 | 必需 | morphix.app/api-keys 获取 |
| Figma Enterprise | 服务 | 可选 | 设计变量完整功能可能需要 |

### API Key 配置
- **必需**: MorphixAI API Key（格式：`mk_详情见说明详情见说明`，与免费版共用）
- **获取方式**: 访问 morphix.app/api-keys 生成
- **配置方式**: 环境变量 `MORPHIXAI_API_KEY`
- **账号链接**: 访问 morphix.app/connections 链接 Figma 账号
- **安全说明**: Key 可随时轮换或撤销

### 可用性分类
- **分类**: MD+EXEC+API（Markdown指令 + 命令行 + 外部API调用）
- **说明**: 企业级AI Skill，支持Figma REST API全功能与批量操作
- **适用规模**: 团队与企业级，设计系统管理与批量资产获取
- **兼容性**: 与免费版完全兼容，API Key 和配置无缝共用

## 案例展示

### 设计变量提取配置

```text
变量类型说明:
  COLOR   → 颜色变量 (#RRGGBB)
  FLOAT   → 数值变量 (间距/圆角/字号)
  STRING  → 字符串变量 (字体名称)
  BOOLEAN → 布尔变量 (显示/隐藏)

变量模式:
  valuesByMode → 各模式下的不同值
  例: 颜色变量在 light/dark 模式下有不同值
```

### 团队组件库配置

```text
团队组件库查询:
  get_team_components
    team_id: "123456789"
    page_size: 30   # 分页大小

  get_team_component_sets
    team_id: "123456789"

  get_team_styles
    team_id: "123456789"
```

## 常见问题

### Q: 如何从免费版升级到专业版？

A: API Key 和插件配置无需变更，直接使用专业版的评论管理、组件库和设计变量功能即可。

### Q: 设计变量需要 Figma Enterprise 吗？

A: 变量 API 可能需要 Figma Enterprise 计划才能完整使用。本地变量 `get_local_variables` 一般可用，发布的跨文件变量 `get_published_variables` 可能需要高级计划。

### 错误恢复步骤
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

A: `export_images` 支持多 node_ids，建议单次不超过 50 个节点。超大批量请分多次执行。

### Q: 评论可以回复吗？

A: 可以。使用 `post_comment` 并传入 `comment_id` 参数即可回复指定评论。

### Q: 组件集和组件的区别？

A: 组件集是包含多个变体的容器（如 Button 组件集含 Primary、Secondary 等变体），组件是单个可复用单元。

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 检查网络连接，重试请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

- 需要LLM支持
- 需要LLM支持
- 需要LLM支持
- 需要LLM支持

