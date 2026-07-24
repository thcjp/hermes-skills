---
slug: "podcast-toolkit"
name: "podcast-toolkit"
version: 1.0.1
displayName: "播客创作工具包专业版"
summary: "企业级播客创作与运营工具包,支持多节目管理、增长分析、变现策略与AI生成,适配团队协作。"
license: "Proprietary"
edition: "pro"
description: |-
  面向团队与专业创作者的播客创作与运营工具包(专业版)。核心能力:
  - 涵盖免费版全部能力(选题、脚本、节目笔记、检查清单)
  - 多节目矩阵管理
  - 增长分析与数据驱动决策
  - 变现策略与商业化路径
  - AI 辅助内容生成(大纲、笔记、切片文案)
  - 团队协作与角色分工
  - 跨平台发布与 SEO 优化
  - 嘉宾关系管理(CRM)

  适用场景:
  - 播客矩阵运营与团队协作
  - 数据驱动的增长决策
  - 商业化变现路径设计
  - AI 辅助批量内容生产
  - 企业品牌播客管理

  差异化:
  - 专业...
tags:
  - 创意设计
  - 播客
  - 内容创作
  - 企业级
  - 增长分析
  - 变现策略
  - AI生成
tools:
  - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"

---
# 播客创作工具包专业版

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 播客创作工具包专业版支持多节目管理 | 不支持 | 支持 |
| 播客创作工具包专业版增长分析 | 不支持 | 支持 |
| 播客创作工具包专业版变现策略与AI生成 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |

## 核心能力

### 免费版 vs 专业版对比
| 能力 | 免费版 | 专业版 | 增量价值 |
|:-----|:-----|:-----|:-----|
| 节目定位 | 单节目 | 多节目矩阵 | 矩阵运营 |
| 选题规划 | 单集 | 多节目选题池 | 选题管理 |
| 脚本大纲 | 手动 | AI 辅助生成 | 效率提升 |
| 节目笔记 | 模板 | AI 自动生成 | 自动化 |
| 录制检查 | 基础清单 | 团队协作流程 | 角色分工 |
| 项目结构 | 单节目 | 多节目统一管理 | 矩阵管理 |
| 增长分析 | 不支持 | 数据驱动决策 | 增长闭环 |
| 变现策略 | 不支持 | 多路径设计 | 商业化 |
| AI 生成 | 不支持 | 大纲/笔记/切片 | 生产力 |
| 嘉宾管理 | 基础记录 | CRM 系统 | 关系维护 |
| 跨平台发布 | 不支持 | 多平台 + SEO | 触达扩大 |
| 团队协作 | 不支持 | 角色与权限 | 团队化 |

**输入**: 用户提供免费版 vs 专业版对比所需的指令和必要参数.
### 节目定位

针对节目定位,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供节目定位相关的配置参数、输入数据和处理选项.
**输出**: 返回节目定位的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`节目定位`的配置文档进行参数调优
### 选题规划

针对选题规划,自动解析输入参数、调度任务队列、格式化输出,返回结构化响应.
**输入**: 用户提供选题规划相关的配置参数、输入数据和处理选项.
**输出**: 返回选题规划的处理结果。- 验证返回数据的完整性和格式正确性
- 参考`选题规划`的配置文档进行参数调优
#
## 适用场景

### 场景一:播客矩阵管理

管理多个节目,统一规划选题与资源.
```bash
# 多节目矩阵目录结构
mkdir -p ~/podcasts-network/
cd ~/podcasts-network/
# ...
# 矩阵配置
cat > matrix-config.yaml << 'EOF'
network:
  name: "创作者网络"
  shows:
    - slug: "indie-maker"
      name: "独立开发者"
      format: "interview"
      cadence: "weekly"
      audience: "独立开发者与创业者"
    - slug: "design-talk"
      name: "设计对谈"
      format: "solo"
      cadence: "biweekly"
      audience: "UI/UX 设计师"
    - slug: "tech-trends"
      name: "科技趋势"
      format: "panel"
      cadence: "weekly"
      audience: "科技从业者"
  shared_resources:
    - brand/assets/         # 共享品牌素材
    - guests/               # 共享嘉宾池
    - sponsors/             # 赞助商管理
EOF
# ...
# 生成矩阵概览
cat > dashboard.md << 'EOF'
# 播客矩阵概览
# ...
## 使用流程
# ...
### 1. 初始化矩阵项目
# ...
```bash
# 创建矩阵目录
mkdir -p ~/podcasts-network/{brand,guests,sponsors,analytics}

# 为每个节目创建标准结构
for show in indie-maker design-talk tech-trends; do
    mkdir -p ~/podcasts-network/$show/{brand,episodes}
done
```
# ...
### 2. 配置团队协作
# ...
```markdown
# team-roles.md

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | podcast-toolkit处理的内容输入 |,  |
| content | string | 否 | podcast-toolkit处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

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

输出模板参考: `assets/output.json`

## 异常处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **协作工具**: 推荐使用 Notion / 飞书 / Lark 管理团队任务

### 依赖说明(补充)

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| Markdown 编辑器 | 工具 | 推荐 | VS Code / Obsidian |
| 音频编辑软件 | 工具 | 推荐 | Audacity / Descript |
| OpenAI Python SDK | Python 库 | 可选(AI 生成) | `pip install openai` |
| Python 3.9+ | 运行时 | 可选(脚本) | `python.org` 下载 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 核心 Markdown 流程**无需 API Key**
- AI 辅助生成功能需配置 `OPENAI_API_KEY`
- 企业部署建议通过密钥管理服务统一托管
- 团队协作场景建议配置统一的 API Key 配额管理

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,。专业版支持多节目管理、增长分析、变现策略与 AI 辅助生成,适合专业创作者与团队的企业级播客运营.
## 案例展示

### 多节目发布配置

```yaml
# publish-config.yaml
platforms:
  xiaoyuzhoufm:
    enabled: true
    auto_publish: false
    categories: ["科技", "商业"]
  apple_podcasts:
    enabled: true
    auto_publish: true
  spotify:
    enabled: true
    auto_publish: true
  youtube:
    enabled: true
    video_required: true
# ...
seo:
  keywords:
    - "独立开发者"
    - "创业"
    - "AI 工具"
  description_template: "{show_name} 第 {episode} 期:{title}"
  transcript_indexing: true
```

### 嘉宾 CRM 模板

```markdown
# guests-crm.md
# ...
## 常见问题
# ...
### Q1: 什么时候应该升级到专业版?
# ...
当出现以下情况时建议升级:
- 计划运营多个节目
- 需要团队协作
- 听众增长进入瓶颈,需要数据驱动
- 准备商业化变现
- 内容生产效率需要提升
# ...
### Q2: AI 生成的内容质量如何?
# ...
AI 生成的大纲与笔记为初稿,质量可达 70-80%,需人工优化。建议:
- 大纲:AI 生成框架,人工填充细节
- 笔记:AI 生成初稿,人工校对时间戳
- 切片:AI 推荐,人工最终筛选
# ...
### Q3: 多节目如何避免资源分散?
# ...
- 优先做好一个节目再扩展
- 共享后期与运营资源
- 不同节目错峰发布
- 建立统一的内容日历
# ...
### Q4: 变现从什么时候开始?
# ...
建议在 1000+ 稳定听众后开始尝试赞助。过早变现可能影响用户体验。付费订阅建议在 5000+ 听众后探索.
# ...
### Q5: 专业版与免费版的迁移成本?
# ...
零迁移成本。专业版是免费版的超集,目录结构与流程完全兼容。升级后原有项目可直接使用,新特性按需启用.
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