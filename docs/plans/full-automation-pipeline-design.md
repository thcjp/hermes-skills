# Skill 全自动流水线设计方案

> **创建时间**: 2026-07-22
> **最后更新**: 2026-07-22 (v2 - 深度审查后增强)
> **评估方法**: staff-engineer-mode (architecture-decisions) + hotl (writing-plans) + hotl (document-review)
> **状态**: Draft → 五轮交叉审核通过

---

## 一、项目深度分析

### 1.1 项目目的

本项目是一个 **AI Skill 商业化发布平台**，核心目标是：

| 维度 | 说明 |
|------|------|
| **发现** | 从多平台（ClawHub/GitHub/Hermes）扫描、发现高价值 AI Skill |
| **生产** | 通过深度差异化改造（去标识化+质量增强+中文化+成本优化），将源 Skill 升级为可商用产品 |
| **质量保证** | 6 层质量审计系统确保每个 Skill 达到可销售标准 |
| **上传运维** | 三平台发布（SkillHub 付费+ClawHub 免费+Hermes 开源），版本追踪、状态同步 |
| **盈利** | SkillHub SkillPay 机制（按次付费/月度/买断），免费版引流+付费版变现 |

### 1.2 当前规模

| 指标 | 数值 |
|------|------|
| 源 Skill | 640 个（ClawHub 下载） |
| 生产 Skill | 2075 个（983 packaged + 1100 differentiated） |
| SkillHub 发布 | 2068 个（99.7%） |
| ClawHub 发布 | 430 个（46%，限频阻塞） |
| Hermes 发布 | 1067 个（100%） |
| 付费 Skill | 1320 个 |
| 免费 Skill | 755 个 |
| 质量审计通过率 | 100%（6 层全 A 级） |

### 1.3 工作原理

#### 数据流

```
[外部来源: ClawHub / GitHub / Hermes / N8N / Dify / Coze]
        ↓ (auto_discover.py 扫描)
[sources 表] ← 原始发现记录
        ↓ (LLM 分析: 合并增强 vs 全新增)
[决策: merge_to_existing / create_new / skip]
        ↓ (AI 差异化改造)
[skills 表] ← 产出记录 (free + paid 双版本)
        ↓ (6层质量审计)
[质量门禁: 不达标阻止上传]
        ↓ (auto_publish.py)
[SkillHub / ClawHub / Hermes 三平台]
        ↓ (状态追踪+报告)
[数据报告: 发布率/质量分/收入预估]
```

#### 三大触发机制

| 触发词 | 系统 | 作用 |
|--------|------|------|
| **"发现"** | auto_discover.py | 扫描平台发现新 Skill，差异化后发布 |
| **"更新"** | update_mechanism.py | 检查已有 Skill 的来源更新，升级版本 |
| **"治理"** | clean_naming.py | 清理 DB 中的命名规范问题 |

### 1.4 工作流程（10 步状态机）

```
step1_read_original → step2_debrand → step3_enhance → step4_chineseize
→ step5_add_deps → step6_generate_dual → step7_validate → step8_upload_free
→ step9_upload_paid → completed
```

### 1.5 质量保证原理

#### 6 层质量审计系统 v3.0

| 层级 | 名称 | 检查内容 | 评级 |
|------|------|---------|------|
| Layer 1-3 | 格式检查 | slug/version/name 必需字段、slug 与目录一致、frontmatter 解析 | critical/warning/info |
| Layer 4 | 功能质量 | 内容深度(25)+指令性(25)+代码示例(20)+任务定义(15)+错误处理(15) | A(70+)/B(50+)/C/D/F |
| Layer 5 | 可销售性 | 内容深度(25)+功能完整(20)+技术深度(20)+用户体验(20)+专业性(15) | A/B/C/D |
| Layer 6 | 内容真实性 | 模板填充检测(10种模式)、空段落、截断文本、占位符 | A(85+)/B(65+)/C/D/F |

#### 质量门禁（上传前强制）

10 项检查：去标识化、slug 一致性、行数限制、必需字段、长度限制、tools 格式、XML 检测、占位符检测、夸大词检测。任一 high 级 fail → 阻止上传。

### 1.6 盈利方式

| 平台 | 模式 | 收入来源 | 现状 |
|------|------|---------|------|
| SkillHub | SkillPay | 按次付费(9.90 CNY/次)、月度订阅、一次性买断 | 1320 付费 Skill |
| ClawHub | 开源引流 | 免费 Skill 导流到 SkillHub 付费版 | 755 免费 Skill |
| Hermes | GitHub 开源 | 社区影响力、品牌建设 | 1067 Skill |

**盈利策略**: 免费版引流 → 付费版变现。同一 Skill 生成 free + paid 双版本，免费版在 ClawHub/Hermes 发布引流，付费版在 SkillHub 收费。

---

## 二、全自动流水线架构设计

### 2.1 架构概览

```
┌─────────────────────────────────────────────────────────────┐
│                    全自动流水线编排器                          │
│              (pipeline_orchestrator.py)                      │
├─────────┬──────────┬──────────┬──────────┬─────────────────┤
│  阶段1   │  阶段2    │  阶段3   │  阶段4   │    阶段5        │
│  发现    │  LLM分析  │  生产    │  上传    │   数据报告      │
│         │          │          │          │                 │
│ 多源头   │ 合并/新增 │ 差异化   │ 三平台   │  发布率/质量   │
│ 扫描    │ 决策     │ 改造     │ 发布     │  收入预估      │
│         │          │          │          │                 │
│ GitHub  │ Trae Work│ 去标识化  │ SkillHub │  可视化报告    │
│ N8N     │ 大模型   │ 质量增强  │ ClawHub  │  状态追踪      │
│ Dify    │ 分析     │ 中文化   │ Hermes   │  告警通知      │
│ Coze    │          │ 双版本   │          │                 │
│ Hermes  │          │          │          │                 │
│ ClawHub │          │          │          │                 │
└─────────┴──────────┴──────────┴──────────┴─────────────────┘
```

### 2.2 阶段1: 多源头发现（扩展）

#### 新增源头

| 源头 | 发现方式 | Skill 形态 | 价值 |
|------|---------|-----------|------|
| **GitHub 高星 AI 项目** | GitHub API + 主题搜索 | Agent/Tool 定义文件 | 前沿技术、高星验证 |
| **N8N 社区** | N8N Workflow 模板市场 | Workflow JSON → Skill | 自动化场景丰富 |
| **Dify 社区** | Dify Template 市场 | Agent Template → Skill | 对话式 AI 场景 |
| **Coze 社区** | Coze Bot 商店 | Bot 定义 → Skill | 中文场景适配好 |
| **Hermes 社区** | Hermes Publisher Portal | 已发布 Skill | 交叉发现 |
| **ClawHub** | API + 本地扫描 | SKILL.md | 现有主力来源 |
| **awesome-lists** | GitHub awesome-* 仓库 | 工具/资源列表 | 领域覆盖广 |

#### 发现脚本设计: `multi_source_discover.py`

```python
# 新增多源头发现脚本
class MultiSourceDiscover:
    """多源头 Skill 发现引擎"""
    
    sources = {
        'github_ai': GitHubAIScanner(),      # GitHub AI 项目扫描
        'n8n_community': N8NScanner(),        # N8N 工作流模板
        'dify_community': DifyScanner(),      # Dify Agent 模板
        'coze_community': CozeScanner(),      # Coze Bot 定义
        'hermes_portal': HermesScanner(),     # Hermes 已发布
        'clawhub': ClawHubScanner(),          # ClawHub 现有
        'awesome_lists': AwesomeListScanner() # awesome-* 列表
    }
    
    def scan_all(self):
        """扫描所有源头，统一输出候选列表"""
        # 每个源头独立扫描，统一格式输出
        # 输出: discovery/candidates_unified.json
        pass
```

### 2.3 阶段2: LLM 智能分析决策（核心创新）

#### 当前问题

现有 `auto_discover.py` 的去重逻辑是**硬规则**：
- 精确匹配 `source_slug` → 跳过
- 模糊匹配 `display_name` → 跳过
- 匹配 `slug` → 跳过

**缺陷**: 无法判断一个新发现的 Skill 是否应该与已有 Skill 合并增强，还是作为全新 Skill 新增。

#### LLM 分析决策设计

```
新发现 Skill
    ↓
┌───────────────────────────────────┐
│        LLM 智能分析引擎            │
│  (Trae Work 大模型分析)            │
├───────────────────────────────────┤
│  输入:                            │
│  1. 新发现 Skill 的内容摘要        │
│  2. 本地已有 Skill 的能力索引      │
│  3. 已有 Skill 的 frontmatter     │
│                                   │
│  分析维度:                         │
│  - 功能重叠度 (0-100%)            │
│  - 能力互补性 (高/中/低)           │
│  - 质量对比 (优于/持平/劣于)       │
│  - 用户痛点覆盖 (独有/重叠)        │
│  - 技术栈兼容性                   │
│                                   │
│  输出决策:                         │
│  A. merge_enhance: 合并到已有Skill │
│     → 指定目标 slug + 增强方案     │
│  B. create_new: 全新增加          │
│     → 指定新 slug + 分类          │
│  C. skip: 跳过(质量低/重复度高)    │
│     → 记录原因                    │
│                                   │
│  原则:                            │
│  - 专事专办，不做瑞士军刀          │
│  - 功能重叠>70% 且无互补 → skip    │
│  - 功能重叠>50% 且有互补 → merge   │
│  - 功能重叠<30% → create_new      │
│  - 中间地带由 LLM 综合判断         │
└───────────────────────────────────┘
```

#### LLM 分析脚本设计: `llm_skill_analyzer.py`

```python
class LLMSkillAnalyzer:
    """基于 Trae Work 大模型的 Skill 分析决策引擎"""
    
    def analyze(self, candidate_skill, existing_skills_index):
        """
        分析新发现 Skill 应该合并增强还是全新增加
        
        Args:
            candidate_skill: 新发现的 Skill 信息
            existing_skills_index: 本地已有 Skill 的能力索引
            
        Returns:
            {
                'decision': 'merge_enhance' | 'create_new' | 'skip',
                'target_slug': str,  # merge 时指定
                'new_slug': str,     # create_new 时指定
                'reason': str,       # 决策理由
                'enhancement_plan': str,  # 增强方案
                'confidence': float  # 置信度
            }
        """
        pass
```

**关键约束**: 这一步**必须是 Trae Work 大模型分析**，不是硬规则。硬规则只做预过滤（去除完全相同的），LLM 做最终决策。

### 2.4 阶段3: 生产（差异化改造升级）

#### 现有流程（保留）

```
step1_read_original → step2_debrand → step3_enhance → step4_chineseize
→ step5_add_deps → step6_generate_dual → step7_validate
```

#### 新增能力

| 新增项 | 说明 |
|--------|------|
| **合并增强模式** | 当 LLM 决策为 merge_enhance 时，读取目标已有 Skill，将新发现的能力整合进去 |
| **跨平台格式转换** | N8N Workflow JSON → SKILL.md、Dify Template → SKILL.md、Coze Bot → SKILL.md |
| **自动化差异报告** | 生成改造前后对比报告，记录差异点 |

### 2.5 阶段4: 上传运维（三平台发布）

#### 现有流程（保留+增强）

| 平台 | 现有方式 | 增强项 |
|------|---------|--------|
| SkillHub | 浏览器 cookie 认证 + API 上传 | 自动重试 + 审核状态追踪 |
| ClawHub | CLI publish + 200/天限频 | 限频自动排队 + 批量续传 |
| Hermes | Git push + 三语 README | 自动同步 |

### 2.6 阶段5: 数据报告

#### 报告内容

| 报告类型 | 指标 | 频率 |
|---------|------|------|
| **发布完成度** | 三平台发布率、待处理数、阻塞数 | 每次流水线执行后 |
| **质量分布** | 6 层审计等级分布、F 级 Skill 数 | 每次审计后 |
| **源头效率** | 各源头发现数、采纳率、跳过率 | 每次发现后 |
| **LLM 决策统计** | merge/create_new/skip 分布 | 每次分析后 |
| **收入预估** | 付费 Skill 数 × 预估调用量 × 单价 | 每周 |
| **版本更新** | 源 Skill 变更检测、已更新数 | 每次更新检查后 |

---

## 三、多步骤任务清单

### 任务总览

| 步骤 | 任务 | 依赖 | 预计工时 |
|------|------|------|---------|
| Step 1 | 扩展多源头发现系统 | 无 | 2h |
| Step 2 | LLM 智能分析决策引擎 | Step 1 | 2h |
| Step 3 | 跨平台格式转换器 | Step 1 | 1.5h |
| Step 4 | 合并增强生产流程 | Step 2, 3 | 1.5h |
| Step 5 | 上传运维增强 | Step 4 | 1h |
| Step 6 | 数据报告自动化 | Step 5 | 1h |
| Step 7 | 流水线编排器 | Step 1-6 | 1h |
| Step 8 | 端到端测试验证 | Step 7 | 1h |

---

### Step 1: 扩展多源头发现系统

**目标**: 新增 GitHub AI 项目、N8N、Dify、Coze、Hermes 社区、awesome-lists 六个源头

**具体提示词**:

```
复核Round 42的完成情况，然后开始实施全自动流水线Step 1: 扩展多源头发现系统。

当前auto_discover.py仅支持ClawHub本地扫描和5个GitHub仓库。需要新增以下源头扫描器：

1. GitHub AI项目扫描器（扩展）:
   - 新增搜索关键词: "ai agent", "llm tool", "ai workflow", "claude skill", "gpt skill"
   - 按star数排序，扫描top 50仓库
   - 提取仓库中的skill/tool/agent定义文件

2. N8N社区扫描器:
   - 扫描 https://n8n.io/workflows/ 模板市场
   - 提取workflow JSON，识别可转化为skill的自动化场景
   - 输出格式: {source: 'n8n', workflow_id, name, description, nodes_count, category}

3. Dify社区扫描器:
   - 扫描 https://cloud.dify.ai/explore 模板市场
   - 提取agent template，识别可转化为skill的对话场景
   - 输出格式: {source: 'dify', template_id, name, description, model, category}

4. Coze社区扫描器:
   - 扫描 https://www.coze.cn/store/bot 商店
   - 提取bot定义，识别可转化为skill的中文场景
   - 输出格式: {source: 'coze', bot_id, name, description, category}

5. Hermes社区扫描器:
   - 扫描已发布到Hermes的skill，交叉发现本地没有的
   - 输出格式: {source: 'hermes', slug, name, description}

6. awesome-lists扫描器:
   - 扫描GitHub上awesome-ai-agents、awesome-llm-tools等列表
   - 提取列表中提到的工具/项目
   - 输出格式: {source: 'awesome-list', repo, tool_name, url, description}

创建文件: d:\skills\skill-registry\multi_source_discover.py
所有扫描器统一输出到: d:\skills\skill-registry\discovery\candidates_unified.json
格式: [{source, source_id, name, description, category, content_preview, url, metadata}, ...]

注意:
- **必须 import auto_discover 复用**现有 ClawHub/GitHub 扫描器（scan_clawhub_local, scan_github_repo, fetch_url, deduplicate），仅新增 N8N/Dify/Coze/Hermes/awesome-lists 五个源头扫描器
- 新增扫描器独立实现，可单独运行
- 网络请求复用 auto_discover.fetch_url()，不重新实现
- 输出统一格式，供Step 2的LLM分析使用
- 扫描结果需要记录到数据库sources表

完成后生成下一步提示词。
```

---

### Step 2: LLM 智能分析决策引擎

**目标**: 使用 Trae Work 大模型分析每个新发现 Skill 应该合并增强、全新增加还是跳过

**具体提示词**:

```
复核Step 1的完成情况（多源头发现系统），然后开始实施Step 2: LLM智能分析决策引擎。

当前问题: auto_discover.py的去重逻辑是硬规则（source_slug/display_name/slug匹配），无法判断新发现Skill应该合并增强还是全新增加。

需要创建: d:\skills\skill-registry\llm_skill_analyzer.py

核心功能:
1. 预过滤（复用现有 auto_discover.deduplicate()，不重新实现）:
   - 调用 from auto_discover import deduplicate 进行 source_slug 精确匹配去重
   - 预筛用嵌入向量(sentence-transformers)计算功能重叠度，仅 30-70% 重叠区间进入 LLM
   - 不做display_name模糊匹配（交给LLM判断）

2. LLM分析（Trae Work大模型，核心决策）:
   对每个预过滤后的候选Skill，构建以下prompt供大模型分析:

   输入:
   - 候选Skill的名称、描述、内容摘要、来源平台
   - 本地已有Skill中功能最相似的top 10（通过关键词匹配预筛）
   - 每个相似Skill的slug、displayName、summary、category

   大模型分析维度:
   a. 功能重叠度: 候选Skill与最相似已有Skill的功能重叠百分比
   b. 能力互补性: 候选Skill是否带来已有Skill不具备的新能力
   c. 质量对比: 候选Skill的质量是否优于已有Skill
   d. 用户痛点覆盖: 候选Skill覆盖的痛点是否与已有Skill重叠
   e. 技术栈兼容性: 候选Skill的技术栈是否与已有Skill兼容

   大模型输出决策（三选一）:
   A. merge_enhance: 合并到已有Skill
      - 指定目标slug
      - 提供增强方案（新增哪些功能/改进哪些方面）
      - 理由: 功能重叠>50%且有明显互补能力
   B. create_new: 全新增加
      - 建议新slug（kebab-case，<=20字符）
      - 建议分类
      - 理由: 功能重叠<30%，或虽有重叠但有独立价值
   C. skip: 跳过
      - 记录跳过原因
      - 理由: 功能重叠>70%且无互补，或质量明显劣于已有

   关键原则:
   - 专事专办，不做瑞士军刀（如果合并后Skill过于臃肿，选择create_new）
   - 中间地带（重叠30-70%）由LLM综合判断
   - LLM分析结果需要记录到数据库（llm_decisions表或skills表notes字段）
   - 每次分析需要记录: 候选信息、相似Skill列表、决策结果、决策理由、置信度

3. 批量分析:
   - 支持批量处理candidates_unified.json
   - 每次分析一个Skill，结果追加到: d:\skills\skill-registry\discovery\llm_decisions.json
   - 支持断点续传（跳过已分析的）

4. 分析报告:
   - 统计merge_enhance/create_new/skip的分布
   - 输出到: d:\skills\skill-registry\discovery\analysis_report.json

数据库新增表:
CREATE TABLE IF NOT EXISTS llm_decisions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    candidate_source TEXT,
    candidate_id TEXT,
    candidate_name TEXT,
    candidate_content_preview TEXT,
    decision TEXT CHECK(decision IN ('merge_enhance', 'create_new', 'skip')),
    target_slug TEXT,
    new_slug TEXT,
    reason TEXT,
    enhancement_plan TEXT,
    confidence REAL,
    similar_slugs TEXT,  -- JSON array
    created_at TEXT NOT NULL
);

注意:
- LLM分析是核心，不能简化为硬规则
- 需要构建有效的prompt，包含足够上下文
- 分析结果需要可追溯（记录决策理由）
- 支持dry-run模式（只分析不执行）

完成后生成下一步提示词。
```

---

### Step 3: 跨平台格式转换器

**目标**: 将 N8N Workflow、Dify Template、Coze Bot 等格式统一转换为 SKILL.md

**具体提示词**:

```
复核Step 2的完成情况（LLM智能分析决策引擎），然后开始实施Step 3: 跨平台格式转换器。

不同源头发现的Skill格式各异，需要统一转换为SKILL.md格式:

创建文件: d:\skills\skill-registry\format_converter.py

转换器列表:

1. N8NWorkflowConverter:
   - 输入: N8N workflow JSON (nodes, connections, settings)
   - 输出: SKILL.md
   - 转换逻辑:
     * workflow name → displayName
     * workflow description → summary
     * nodes中的HTTP Request节点 → API调用说明
     * nodes中的Function节点 → 代码逻辑说明
     * connections → 工作流步骤
     * 生成## 工作原理章节
     * 生成## 使用示例章节

2. DifyTemplateConverter:
   - 输入: Dify agent template JSON (model, prompt, tools, config)
   - 输出: SKILL.md
   - 转换逻辑:
     * template name → displayName
     * template description → summary
     * system prompt → 核心指令
     * tools配置 → 工具说明
     * 生成## 能力定义章节
     * 生成## 配置说明章节

3. CozeBotConverter:
   - 输入: Coze bot定义 (name, description, prompt, plugins)
   - 输出: SKILL.md
   - 转换逻辑:
     * bot name → displayName
     * bot description → summary
     * bot prompt → 核心指令
     * plugins → 工具依赖说明
     * 生成## 能力定义章节

4. GitHubRepoConverter:
   - 输入: GitHub仓库README.md + 目录结构
   - 输出: SKILL.md
   - 转换逻辑:
     * repo name → slug
     * README第一段 → summary
     * README内容 → 核心能力说明
     * 检测是否有SKILL.md，有则直接使用
     * 检测是否有agent/tool定义文件

5. AwesomeListConverter:
   - 输入: awesome-list条目 (name, url, description)
   - 输出: SKILL.md (基础模板，需后续差异化)
   - 转换逻辑:
     * tool name → slug
     * description → summary
     * 生成基础SKILL.md框架
     * 标记为needs_enhancement

统一输出格式:
- 所有转换器输出标准SKILL.md
- frontmatter包含: slug, name, version, displayName, summary, license, description, tags, tools
- 必须包含## 依赖说明章节
- 转换后的SKILL.md保存到: d:\skills\skill-registry\discovery\converted\{slug}\SKILL.md

转换日志:
- 记录到: d:\skills\skill-registry\discovery\conversion_log.json
- 字段: source, source_id, target_slug, conversion_status, warnings

注意:
- 转换是基础框架生成，后续仍需AI差异化改造
- 转换器需要处理各种边界情况（空字段、格式异常等）
- 不要修改现有deep-differentiation-methodology.md

完成后生成下一步提示词。
```

---

### Step 4: 合并增强生产流程

**目标**: 根据 LLM 决策结果，执行合并增强或全新增加的生产流程

**具体提示词**:

```
复核Step 3的完成情况（跨平台格式转换器），然后开始实施Step 4: 合并增强生产流程。

根据Step 2的LLM决策结果，需要支持两种生产模式:

创建文件: d:\skills\skill-registry\enhanced_production.py

模式A: merge_enhance（合并增强已有Skill）
流程:
1. 读取LLM决策中指定的target_slug
2. 读取目标已有Skill的SKILL.md
3. 读取候选Skill的转换后SKILL.md（Step 3输出）
4. 按LLM的enhancement_plan整合:
   - 新增候选Skill独有的功能模块
   - 补充候选Skill中更完善的错误处理
   - 整合候选Skill的使用示例
   - 保持已有Skill的核心能力不变
5. 更新SKILL.md:
   - version: minor+1 (1.0.0 → 1.1.0)
   - description: 补充新增能力
   - 新增## 更新历史 记录合并来源
6. 质量审计: 调用deep_quality_audit.py验证
7. 生成双版本（如果是新分类需要）

模式B: create_new（全新增加Skill）
流程:
1. 读取LLM决策中建议的new_slug和分类
2. 读取候选Skill的转换后SKILL.md（Step 3输出）
3. 执行标准差异化改造（**调用现有差异化改造函数，不重新实现 step1-step7 逻辑**）:
   - 遵循 deep-differentiation-methodology.md 定义的流程
   - step1: 读取原始内容
   - step2: 去标识化（移除源项目烙印）
   - step3: 质量增强（补充边界处理、错误码、示例）
   - step4: 中文化（displayName和summary）
   - step5: 添加依赖说明
   - step6: 生成双版本（free + paid）
   - step7: 质量验证
4. 保存到:
   - 付费版: d:\skills\packaged-skills\skillhub\{new-slug}\SKILL.md
   - 免费版: d:\skills\packaged-skills\skillhub\{new-slug}-free\SKILL.md
5. 录入数据库

模式C: skip（跳过）
- 记录到日志，不执行生产

批量执行:
- 读取llm_decisions.json
- 按决策类型批量执行
- 支持dry-run模式
- 执行结果记录到: d:\skills\skill-registry\production_log.json

关键原则:
- 合并增强时，不做瑞士军刀（如果增强后SKILL.md超过500行，考虑拆分）
- 合并增强时，保持已有Skill的slug不变
- 全新增加时，遵循现有命名规范和frontmatter规范
- 所有生产结果必须通过6层质量审计

数据库更新:
- merge_enhance: 更新已有Skill的version和current_score
- create_new: 新增Skill记录（free + paid双版本）
- 更新workflow_state到step7_validate

注意:
- 合并增强是新增能力，不是覆盖
- 需要保留已有Skill的用户基础
- 合并后的版本变更记录需要写入versions表

完成后生成下一步提示词。
```

---

### Step 5: 上传运维增强

**目标**: 增强三平台上传的自动化能力，支持自动重试、限频排队、状态同步

**具体提示词**:

```
复核Step 4的完成情况（合并增强生产流程），然后开始实施Step 5: 上传运维增强。

当前上传系统(auto_publish.py和automated_review_system.py)已有基础功能，需要增强:

修改文件: d:\skills\skill-registry\auto_publish.py
新增文件: d:\skills\skill-registry\upload_queue_manager.py

关键约束: upload_queue_manager.py 仅负责队列状态管理和限频调度，实际上传操作必须调用 auto_publish.py 的 publish_to_skillhub() 等函数，不得重新实现上传逻辑。

增强项1: ClawHub限频自动排队
- 检测200/24h滑动窗口限频状态
- 待上传Skill自动排队，按FIFO顺序
- 限频重置后自动触发批量上传
- 排队状态可视化: 显示预计上传时间

增强项2: SkillHub审核状态追踪
- 定期检查pending_review状态Skill
- 审核通过后自动更新数据库状态
- 审核被拒后记录拒绝原因，触发修复流程

增强项3: 上传失败自动重试
- 指数退避重试（最多3次）
- HTTP 429: 等待120s后重试
- HTTP 500: 等待60s后重试
- HTTP 401: 标记需要重新认证
- 其他错误: 记录日志，人工介入

增强项4: 三平台状态同步（版本更新检测移至编排器，避免循环依赖）
- 确保每个Skill在三个平台的状态一致
- 生成状态同步报告
- 异常状态告警
- 注意: 版本更新检测由 pipeline_orchestrator.py 作为独立定期任务执行，检测到更新后编排器重新从 Step 4 启动新流水线，而非 upload 阶段反向调用 produce

upload_queue_manager.py设计:
class UploadQueueManager:
    def enqueue(self, slug, platform, priority='normal'):
        """入队"""
        
    def process_queue(self):
        """处理队列（考虑限频）"""
        
    def get_queue_status(self):
        """获取队列状态"""
        
    def auto_retry(self):
        """自动重试失败项"""

注意:
- 不破坏现有上传功能
- 增强项是叠加，不是重写
- 限频检测需要准确（基于上次上传时间窗口计算）
- 所有上传操作需要记录审计日志

完成后生成下一步提示词。
```

---

### Step 6: 数据报告自动化

**目标**: 生成全流水线数据报告，包括发布完成度、质量分布、源头效率、LLM决策统计、收入预估

**具体提示词**:

```
复核Step 5的完成情况（上传运维增强），然后开始实施Step 6: 数据报告自动化。

创建文件: d:\skills\skill-registry\pipeline_reporter.py

报告类型1: 流水线执行报告（每次执行后生成）
包含:
- 发现阶段: 各源头扫描数、候选总数、去重后数量
- LLM分析阶段: merge/create_new/skip决策分布、平均置信度
- 生产阶段: 合并增强数、全新增加数、质量审计通过率
- 上传阶段: 三平台上传成功/失败/排队数
- 总耗时、各阶段耗时

报告类型2: 三平台发布完成度报告
包含:
| 平台 | 已发布 | 待处理 | 发布率 | 阻塞项 |
- SkillHub: 付费+免费分布、pending_review数
- ClawHub: 限频状态、预计完成时间
- Hermes: 同步状态

报告类型3: 质量分布报告
包含:
- 6层审计等级分布(A/B/C/D/F)
- F级Skill列表（需内容充实）
- 模板填充检测统计
- 功能质量评分分布
- 可销售性评分分布

报告类型4: 源头效率报告
包含:
| 源头 | 发现数 | 采纳数 | 跳过数 | 采纳率 |
- 每个源头的效率分析
- 高价值源头识别
- 低价值源头优化建议

报告类型5: LLM决策统计报告
包含:
- merge_enhance/create_new/skip比例
- 高置信度决策（>0.8）占比
- 低置信度决策（<0.5）列表（需人工复核）
- 决策理由聚类分析

报告类型6: 收入预估报告
包含:
- 付费Skill总数 × 预估月调用量 × 单价
- 按分类的收入预估
- 增长趋势（与上次报告对比）

报告类型7: 版本更新报告
包含:
- 源Skill变更检测数
- 已更新Skill数
- 待更新Skill列表

输出格式:
- JSON: d:\skills\skill-registry\reports\pipeline_report_{timestamp}.json
- HTML可视化: d:\skills\skill-registry\reports\pipeline_report_{timestamp}.html
- 控制台摘要

HTML报告要求:
- 使用图表展示数据分布（柱状图/饼图）
- 表格展示详细列表
- 支持按时间范围筛选
- 响应式设计

注意:
- 报告数据从数据库和日志文件读取
- 不要硬编码数据
- 支持指定时间范围生成报告
- 报告文件保存到d:\skills\skill-registry\reports\目录

完成后生成下一步提示词。
```

---

### Step 7: 流水线编排器

**目标**: 创建统一编排器，串联 Step 1-6 形成完整全自动流水线

**具体提示词**:

```
复核Step 6的完成情况（数据报告自动化），然后开始实施Step 7: 流水线编排器。

创建文件: d:\skills\skill-registry\pipeline_orchestrator.py

这是全自动流水线的核心编排器，串联所有阶段:

class PipelineOrchestrator:
    """Skill全自动流水线编排器"""
    
    def run_full_pipeline(self, options):
        """
        执行完整流水线:
        1. 多源头发现 → candidates_unified.json
        2. LLM智能分析 → llm_decisions.json
        3. 格式转换 → converted/*.SKILL.md
        4. 生产(合并/新增) → production_log.json
        5. 上传运维 → upload_results.json
        6. 数据报告 → reports/pipeline_report_*.html
        """
        
    def run_stage(self, stage_name, options):
        """单独执行某个阶段"""
        
    def resume_from(self, stage_name):
        """从指定阶段恢复执行（断点续传）"""
        
    def get_pipeline_status(self):
        """获取流水线当前状态"""

阶段定义:
stages = [
    {
        'name': 'discover',
        'description': '多源头发现',
        'script': 'multi_source_discover.py',
        'command': 'scan --all',
        'output': 'discovery/candidates_unified.json',
        'timeout': 300  # 5分钟
    },
    {
        'name': 'analyze',
        'description': 'LLM智能分析',
        'script': 'llm_skill_analyzer.py',
        'command': 'analyze --batch',
        'output': 'discovery/llm_decisions.json',
        'timeout': 600  # 10分钟
    },
    {
        'name': 'convert',
        'description': '格式转换',
        'script': 'format_converter.py',
        'command': 'convert --all',
        'output': 'discovery/converted/',
        'timeout': 300
    },
    {
        'name': 'produce',
        'description': '生产(合并/新增)',
        'script': 'enhanced_production.py',
        'command': 'produce --from-decisions',
        'output': 'production_log.json',
        'timeout': 1800  # 30分钟
    },
    {
        'name': 'upload',
        'description': '上传运维',
        'script': 'upload_queue_manager.py',
        'command': 'process --all',
        'output': 'upload_results.json',
        'timeout': 3600  # 1小时
    },
    {
        'name': 'report',
        'description': '数据报告',
        'script': 'pipeline_reporter.py',
        'command': 'generate --full',
        'output': 'reports/pipeline_report_*.html',
        'timeout': 120
    }
]

编排逻辑:
1. 按顺序执行各阶段
2. 每阶段完成后检查输出文件是否存在
3. 如果某阶段失败，暂停流水线，记录错误
4. 支持--resume从失败阶段恢复
5. 支持--dry-run只模拟不执行
6. 每阶段执行前后记录状态到: d:\skills\skill-registry\pipeline_state.json

状态追踪:
{
    "pipeline_id": "20260722_001",
    "started_at": "2026-07-22T10:00:00",
    "current_stage": "analyze",
    "stages": {
        "discover": {"status": "completed", "duration": "45s", "output_size": 12345},
        "analyze": {"status": "running", "started_at": "..."},
        "convert": {"status": "pending"},
        ...
    },
    "total_candidates": 150,
    "total_decisions": {"merge": 30, "new": 80, "skip": 40},
    "total_produced": 0,
    "total_uploaded": 0
}

命令行接口:
python pipeline_orchestrator.py run              # 执行完整流水线
python pipeline_orchestrator.py run --stage discover  # 仅执行发现阶段
python pipeline_orchestrator.py run --resume     # 从上次中断处恢复
python pipeline_orchestrator.py run --dry-run    # 模拟执行
python pipeline_orchestrator.py status           # 查看当前状态

注意:
- 编排器不实现具体逻辑，只调度各阶段脚本
- 每阶段脚本独立可运行
- 编排器负责状态管理和错误处理
- 需要处理各阶段之间的数据传递（通过中间文件）

完成后生成下一步提示词。
```

---

### Step 8: 端到端测试验证

**目标**: 对完整流水线进行端到端测试，验证各环节衔接是否完善

**具体提示词**:

```
复核Step 7的完成情况（流水线编排器），然后开始实施Step 8: 端到端测试验证。

对全自动流水线进行端到端测试:

测试1: 发现阶段测试
- 运行: python multi_source_discover.py scan --all
- 验证: candidates_unified.json 生成且格式正确
- 验证: 各源头扫描器独立运行正常
- 验证: 网络超时/错误处理正常

测试2: LLM分析测试
- 运行: python llm_skill_analyzer.py analyze --batch --dry-run
- 验证: 对候选Skill生成决策结果
- 验证: merge_enhance/create_new/skip三种决策都有出现
- 验证: 决策理由记录完整
- 验证: 数据库llm_decisions表写入正常

测试3: 格式转换测试
- 运行: python format_converter.py convert --all
- 验证: 各格式转换器输出正确的SKILL.md
- 验证: frontmatter格式合规
- 验证: 转换日志记录正确

测试4: 生产流程测试
- 运行: python enhanced_production.py produce --dry-run
- 验证: merge_enhance模式正确整合已有Skill
- 验证: create_new模式正确生成双版本
- 验证: 质量审计通过
- 验证: 数据库记录更新正确

测试5: 上传运维测试
- 运行: python upload_queue_manager.py process --dry-run
- 验证: 限频检测正确
- 验证: 排队逻辑正确
- 验证: 重试逻辑正确

测试6: 数据报告测试
- 运行: python pipeline_reporter.py generate --full
- 验证: HTML报告生成正确
- 验证: 数据准确（与数据库一致）
- 验证: 图表渲染正常

测试7: 编排器端到端测试
- 运行: python pipeline_orchestrator.py run --dry-run
- 验证: 各阶段按顺序执行
- 验证: 状态追踪正确
- 验证: 断点续传功能正常

测试8: 实际执行测试（小规模）
- 选择3-5个候选Skill
- 执行完整流水线（非dry-run）
- 验证: 从发现到上传的完整流程
- 验证: 数据报告准确反映执行结果

发现问题修复后，生成最终的全自动流水线完成报告和日常使用提示词。

日常使用提示词应包含:
1. 如何一键执行完整流水线
2. 如何单独执行某个阶段
3. 如何从中断处恢复
4. 如何查看流水线状态
5. 如何生成数据报告
```

---

## 四、验证清单

### 4.1 架构完整性验证

| 检查项 | 验证方法 | 通过标准 |
|--------|---------|---------|
| 依赖方向单向 | 检查各模块import关系 | 无循环依赖 |
| 数据流完整 | 检查各阶段输出文件 | 每阶段输出可作为下阶段输入 |
| 状态可追踪 | 检查pipeline_state.json | 每阶段状态可查询 |
| 断点可恢复 | 测试--resume功能 | 从任意阶段恢复 |
| 错误可隔离 | 模拟某阶段失败 | 不影响其他阶段 |

### 4.2 LLM决策质量验证

| 检查项 | 验证方法 | 通过标准 |
|--------|---------|---------|
| 决策合理性 | 人工抽检10个决策 | 80%以上合理 |
| 非硬规则 | 检查决策代码 | LLM分析为核心 |
| 可追溯性 | 检查llm_decisions表 | 每决策有理由 |
| 专事专办 | 检查合并后Skill行数 | ≤500行 |

### 4.3 端到端完整性验证

| 检查项 | 验证方法 | 通过标准 |
|--------|---------|---------|
| 全流程可执行 | dry-run完整流水线 | 无报错 |
| 实际小规模执行 | 3-5个Skill实跑 | 从发现到上传完成 |
| 数据报告准确 | 对比报告与数据库 | 数据一致 |
| 日常可用 | 生成使用提示词 | 可独立操作 |

---

## 五、深度审查：质量门禁真实效果分析

### 5.1 核心发现：质量审计是"格式校验器"而非"质量审计器"

对 `deep_quality_audit.py` 的深度审查发现，当前 6 层质量审计系统**无法保证 skill 产出质量**。2097 个 skill 全部 A 级通过审计，但多个 skill 存在严重质量问题。

#### 5.1.1 Layer 4 功能质量检查的致命缺陷

Layer 4 的全部评分基于 regex 关键词匹配，从不验证内容是否可执行：

| 维度 | 实现方式 | 问题 |
|------|---------|------|
| 内容深度 | `len(body_text)` 字符数 | 模板填充也能产生长文本 |
| 指令性内容 | `re.search(r'步骤\|首先\|然后\|输入\|输出')` | 关键词出现即得分 |
| 代码块 | `body_text.count("```") // 2` | 不检查代码是否完整或可运行 |
| 任务定义 | `re.search(r'##\s*(功能\|Features)')` | 只检查标题存在 |
| 错误处理 | `re.search(r'错误\|Error\|异常')` | 不检查错误处理是否与 skill 相关 |

**后果**: 堆砌关键词即可获得 A 级（70+分）。

#### 5.1.2 Layer 6 模板检测的逃逸漏洞

Layer 6 的核心 regex `执行.{0,20}操作[,，]处理输入数据并返回结果` 要求精确匹配"处理输入**数据**"，但实际 skill 使用"处理**用户**输入"这一同义变种即可完全绕过。

#### 5.1.3 实证案例

| Skill | 审计结果 | 实际问题 |
|-------|---------|---------|
| api-doc-writer | A 级 100 分 | 三个能力描述全部使用"执行X操作,处理用户输入并返回结果"空泛模板句 |
| ace-music | A 级 100 分 | 代码块截断、大段内容重复、错误处理表格混入 ping 网络排查模板 |
| bilibili-helper | A 级 100 分 | 标题被拼接到正文末尾、错误处理模板被重复拼接两次 |

### 5.2 解决方案：引入 Layer 7 语义级质量审计（LLM 介入）

**不是新增独立模块，而是增强现有 `deep_quality_audit.py`，新增 Layer 7 作为第 7 层审计。**

#### 5.2.1 Layer 7 设计原则

- **增强而非替换**: Layer 1-3 格式检查保留（有效），Layer 4-6 regex 检查保留（作为快速预筛），新增 Layer 7 LLM 语义审计作为最终质量门禁
- **分层策略控制成本**: 不是对每个 skill 都做全量 LLM 审计，而是 Layer 4-6 标记为"疑似问题"的 skill 才进入 Layer 7 深审
- **Trae Work 大模型为核心**: 语义理解、模拟执行、上下文一致性检查全部由 LLM 完成

#### 5.2.2 Layer 7 三大机制

| 机制 | 替代 | LLM 任务 | 门禁级别 |
|------|------|---------|---------|
| 语义模板填充检测 | Layer 6 regex | 判断多个能力描述是否使用相同句式仅替换名词 | blocking |
| 模拟执行测试 | Layer 4 关键词检查 | 模拟 Agent 按 skill 指令执行，判断输出质量 | blocking |
| 上下文一致性检查 | 无（新增） | 检测跨域模板错配、内容截断、大段重复 | blocking |

#### 5.2.3 集成方式

在 `deep_quality_audit.py` 的 `check_skill` 函数末尾增加 Layer 7 调用：
- Layer 4-6 全 A 级 → 跳过 Layer 7（节省成本）
- Layer 4-6 有任何 warning/issue → 触发 Layer 7 LLM 深审
- Layer 7 判定"指令不可执行"或"严重模板填充" → 最终评级降为 F，阻止上传

---

## 六、深度审查：定价与营销话术分析

### 6.1 系统性问题

| 问题 | 影响范围 | 严重性 |
|------|---------|--------|
| 收费 skill 使用 `license: "MIT"` | 566 个 skill (67.4%) | P0 - 与收费模式直接矛盾 |
| 缺失 `suggested_price` 定价字段 | 抽样 4 个全部缺失 | P1 - 无法在平台展示价格 |
| 付费版无"付费版专享能力"对比章节 | 抽样 4 个全部缺失 | P1 - 买家看不到付费价值 |
| ace-music 的 summary 写"API 永久免费" | 直接削弱付费理由 | P0 - 自毁商业模式 |
| displayName 缺少价值主张和差异化标识 | 抽样 4 个均偏通用 | P2 - 转化率低 |

### 6.2 定价改进方案（增强现有 pricing 表，非新增模块）

**分级定价模型**（基于 5 维度评估）：

| 层级 | 价格 | 适用类型 | 示例 |
|------|------|---------|------|
| L1 入门级 | 9.9 CNY/次 | 单一功能、纯文本生成 | api-doc-writer |
| L2 标准级 | 19.9 CNY/次或月 | 多功能组合、含 API 调用 | bilibili-helper, ace-music |
| L3 专业级 | 29.9~49.9 CNY/次 | 高复杂度、商业级产出 | ai-image-gen (4K印刷级) |

### 6.3 营销话术增强（集成到现有差异化改造流程 step4_chineseize）

**displayName 公式**: `[核心场景] + [角色定位] + [差异化标识]`
**summary 公式**: `[目标用户] + [核心痛点] + [解决方案] + [量化价值] + [差异化亮点]`
**新增标准章节**: 每个付费版 SKILL.md 在"核心能力"后增加"## 付费版专享能力"对比表

### 6.4 License 修正（批量更新，非新增模块）

| Skill 类型 | 正确 License | 操作 |
|------------|-------------|------|
| 收费 skill | `Proprietary` | 批量 UPDATE skills SET ... WHERE skill_type='paid' |
| 免费引流 skill | `MIT` | 保持不变 |
| 开源改造 skill | 保留原始许可 | 保持不变 |

---

## 七、网页看板设计

### 7.1 文件

`d:\skills\skill-registry\dashboard_server.py` — 完整的 Python HTTP 服务器，内嵌 HTML 前端。

### 7.2 功能

| 区域 | 展示内容 | 数据源 |
|------|---------|--------|
| 顶部按钮栏 | 发现、更新、治理、上传运营、刷新数据 | 触发对应脚本 |
| 核心指标卡 | 总数、付费数、免费数、月收入预估 | SQLite |
| 三平台状态 | SkillHub/ClawHub/Hermes 发布数+待处理数 | SQLite platform_uploads |
| 质量分布 | 各状态 skill 数量条形图 | SQLite |
| 分类分布 | Top 15 分类条形图 | SQLite |
| 来源分布 | 各来源 skill 数量 | SQLite |
| 操作记录 | 最近 20 条操作 | SQLite operations |
| 任务日志 | 实时任务执行状态 | 内存 task_status |

### 7.3 启动方式

```bash
python d:\skills\skill-registry\dashboard_server.py
# 访问 http://localhost:8765
```

### 7.4 集成方式

看板**不新增独立模块**，而是复用现有的 `auto_discover.py`、`update_mechanism.py`、`clean_naming.py`、`auto_publish.py`，通过 `subprocess` 异步调用。看板本身只负责数据展示和任务触发，不实现业务逻辑。

---

## 八、差距分析：现有设计 vs 项目目的

### 8.1 项目核心目的回顾

**找到更多 skill → 优化升级 → 提供给更多做 AI 项目的人 → 赚钱**

### 8.2 差距清单

| 差距 | 现状 | 目标 | 改进方案 |
|------|------|------|---------|
| **质量保证虚假** | 6 层全 A 级但实际模板填充严重 | LLM 语义审计确保真实可执行 | 新增 Layer 7（第五章方案） |
| **定价缺失** | 566 个收费 skill 无定价字段 | 分级定价 + 定价元数据 | 批量补充 suggested_price 字段 |
| **营销话术弱** | 纯功能罗列，无价值主张 | 痛点+方案+量化+差异 | 集成到差异化改造 step4 |
| **License 矛盾** | 收费 skill 用 MIT | 收费 skill 用 Proprietary | 批量 UPDATE |
| **无看板** | 命令行操作，无全局视图 | 网页看板一目了然 | dashboard_server.py |
| **源头单一** | 仅 ClawHub + 5 个 GitHub 仓库 | 7+ 源头覆盖 | Step 1 多源头扩展 |
| **去重硬规则** | 精确匹配 slug/name | LLM 语义分析合并/新增 | Step 2 LLM 分析决策 |
| **格式不统一** | 仅支持 SKILL.md 输入 | N8N/Dify/Coze 格式转换 | Step 3 格式转换器 |
| **无合并增强** | 只能全新增加 | 合并已有 Skill 增强 | Step 4 增强生产流程 |
| **上传无限频管理** | ClawHub 200/天手动等待 | 自动排队+续传 | Step 5 上传队列管理 |
| **无自动报告** | 手动统计 | 7 类报告自动生成 | Step 6 报告自动化 |

### 8.3 改进原则

所有改进**必须是集成升级增强，而非新增碎片化模块**：

1. **Layer 7 语义审计** → 增强到 `deep_quality_audit.py`，不新建文件
2. **定价字段** → 增强到现有 `pricing` 表和差异化改造流程，不新建表
3. **营销话术** → 集成到 `deep-differentiation-methodology.md` 的 step4_chineseize
4. **License 修正** → 批量 UPDATE，不新增脚本
5. **网页看板** → 复用现有脚本，不重写业务逻辑
6. **多源头发现** → 扩展 `auto_discover.py`，不替换

---

## 九、五轮交叉审核记录

### 审核方法

使用 hotl:document-review 技能，对本文档进行五轮串联多 agent 交叉分析审核，重点验证：所有修改是否采用集成升级增强而非新增碎片化冗余代码。

### Round 1: 架构完整性审核

**审核重点**: 各新增组件是否与现有系统集成，而非平行独立

**结论**: REVISE
- Layer 7 集成到 `deep_quality_audit.py` — PASS（技术上可行）
- 看板 commands 映射 — **FAIL**（4/4 命令不匹配实际脚本接口，已修复）
- 定价增强基于现有 `pricing` 表 — PASS
- 营销话术集成到现有 step4_chineseize — PASS

**修复**: 看板命令已修正为 `scan --source all`、`check`、`execute`、`auto-flow`

### Round 2: 冗余代码检测

**审核重点**: 是否有重复实现的功能

**结论**: REVISE — 已识别 4 项重叠风险，全部已制定集成约束

| 重叠风险 | 约束措施 |
|---------|---------|
| upload_queue_manager.py 与 auto_publish.py | upload_queue_manager 仅管理队列状态，实际上传调用 `auto_publish.publish_to_skillhub()` |
| pipeline_reporter.py 与 dashboard_server.py | 提取共享 DB 查询函数到 `db.py`，两模块均调用 |
| enhanced_production.py create_new 模式 | 调用现有差异化改造函数，不重新实现 step1-step7 |
| multi_source_discover.py 与 auto_discover.py | `import auto_discover` 复用 ClawHub/GitHub 扫描器，仅新增 5 个源头 |

### Round 3: 最优方案验证

**审核重点**: 是否存在更简单的替代方案

**结论**: REVISE — Layer 7 和 LLM 分析可分两级降低成本

| 方案 | 是否最优 | 改进 |
|------|---------|------|
| Layer 7 LLM 语义审计 | 基本最优 | 内部分两级：L7a 嵌入向量快速筛查模板填充，L7b LLM 深审模拟执行 |
| LLM 智能分析决策 | 基本最优 | 预筛改用嵌入向量计算功能重叠度，仅 30-70% 重叠区间进入 LLM |
| 网页看板内嵌 HTML | PASS | 单机工具场景最优，无需 Flask |
| 分级定价模型 | PASS | 务实合理，未来可用 LLM 自动判定层级 |

### Round 4: 依赖方向验证

**审核重点**: 各模块依赖是否单向，无循环

**结论**: REVISE — 发现 1 个循环依赖，已修复

| 依赖关系 | 是否单向 | 修复 |
|---------|---------|------|
| discover → analyze → convert → produce → upload → report | PASS | 单向数据流 |
| Layer 4-6 → Layer 7 | PASS | 单向，Layer 7 降级后阻止上传非触发重审 |
| 看板 → 现有脚本 | PASS | 单向 subprocess 调用 |
| **Step 5 版本更新 → 触发 Step 4** | **FAIL** | **循环依赖** |

**循环依赖修复**: 将"版本更新自动检测"从 Step 5（upload 阶段）移出到 `pipeline_orchestrator.py` 作为独立定期任务。检测到更新后编排器重新从 Step 4 启动新流水线，而非 upload 阶段反向调用 produce。

### Round 5: 集成升级 vs 碎片化最终判定

**审核重点**: 所有修改是否为集成升级增强

**结论**: REVISE → 修复后 PASS

| 新增组件 | 集成方式 | 判定 | 审核修正 |
|---------|---------|------|---------|
| Layer 7 语义审计 | 增强到 deep_quality_audit.py check_skill() | PASS | 内部分 L7a(嵌入向量)+L7b(LLM) |
| 定价字段+营销话术 | 增强到 pricing 表+step4_chineseize | PASS | — |
| License 修正 | 批量 UPDATE 现有数据 | PASS | — |
| 看板 | 复用现有 4 个脚本 | PASS | 命令已修正 |
| multi_source_discover.py | **import auto_discover 复用** ClawHub/GitHub 扫描器 | REVISE→PASS | 仅新增 5 个源头，不重复实现 |
| llm_skill_analyzer.py | **from auto_discover import deduplicate** 复用预过滤 | REVISE→PASS | LLM 分析是核心新增，预过滤复用 |
| format_converter.py | 全新能力，复用 skill_core.parser 统一 frontmatter | PASS | — |
| enhanced_production.py | create_new **调用现有差异化函数**，merge_enhance 为新增 | REVISE→PASS | 不重新实现 step1-step7 |
| upload_queue_manager.py | **from auto_publish import publish_to_skillhub**，仅管理队列 | REVISE→PASS | 上传委托给现有函数 |
| pipeline_reporter.py | 全新能力，DB 查询提取共享到 db.py | PASS | 与看板共享查询函数 |
| pipeline_orchestrator.py | 全新编排能力，**参考 auto_flow() 模式** | REVISE→PASS | 版本更新检测移入此处消除循环 |

**最终总结**: 11 个组件中，4 个直接 PASS，7 个经审核修正后 PASS。所有修正均为增强集成约束（import 复用现有函数、不重新实现），无碎片化冗余代码。审核后方案为最优集成方案。
