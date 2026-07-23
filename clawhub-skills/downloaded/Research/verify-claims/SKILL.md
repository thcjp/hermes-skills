---
slug: verify-claims
name: verify-claims
version: "1.0.0"
displayName: Verify Claims
summary: "事实核查技能,自动创建延迟跟进频道,验证声明真伪,降低 misinformation 传播风险"
  delayed follow-up ch...
license: MIT
description: |-
  This fact-checking skill is mostly coherent, but it can automatically
  create delayed follow-up ch。Use when 需要AI模型调用、智能对话、Agent编排、LLM应用时使用。不适用于需要100%确定性的关键决策。
tags:
- Research
tools:
  - - read
- exec
# Verify Claims
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---

Verify claims and information using professional fact-checking services from around the world.

## Core Principles
1. **Multiple sources** - Cross-reference findings from several fact-checking organizations
2. **Regional relevance** - Prioritize fact-checkers appropriate to the content's context
3. **Language matching** - Use fact-checkers in the native language of the content when possible
4. **Credible sources only** - Never use fraudulent or unreliable fact-checking services
5. **Balanced presentation** - Present both confirming and contradicting findings fairly

## When to Use This Skill
Trigger this skill when the user:

* Explicitly asks to fact-check, verify, or validate information
* Shares an article, video transcript, or claim and asks "is this true?"
* Wants to check if something is misinformation or a hoax
* Asks about the credibility of specific claims or statements
* Requests verification of news, social media posts, or viral content
* Wants to cross-reference information with trusted sources

Do NOT trigger for:

* General research or information gathering (use web search instead)
* Checking grammar, spelling, or writing quality
* Verifying code functionality or technical documentation
* Questions about opinions rather than factual claims

## Workflow
### Step 1: Understand the Content
Before beginning verification, analyze what needs to be checked:

1. **Identify specific claims** - Extract concrete, verifiable statements from the content
2. **Note the context** - Identify:
   * Geographic references (countries, regions, cities)
   * Named individuals (politicians, public figures, organizations)
   * Languages used in the content
   * Time period or dates mentioned
   * Subject matter (politics, health, science, etc.)
3. **Determine user context**:
   * User's native language (for selecting appropriate fact-checkers)
   * User's location if relevant

**Example Analysis:**

* Content: "Video claiming vaccines cause autism, mentions Andrew Wakefield, references UK study"
* Claims to verify: Vaccine-autism link, Wakefield's research
* Context: Medical/health topic, UK origin, English language
* Key entities: Andrew Wakefield, MMR vaccine, UK medical establishment

### Step 2: Select Fact-Checking Services
**CRITICAL**: Begin by fetching the current list of fact-checking services:

```text
Fetch: https://en.wikipedia.org/wiki/List_of_fact-checking_websites
```

From this list, select 3-7 relevant fact-checking services based on:

#### Selection Criteria
1. **User's language/location** - Always include fact-checkers in the user's native language
2. **Content language/location** - If different from user's language, also include fact-checkers in the content's language and region
3. **Geographic relevance** - If content mentions specific countries/regions:

   * Include fact-checkers from those countries
   * Example: Content about French politics → include French fact-checkers
4. **Subject matter specialists** - Some fact-checkers specialize:

   * Health/medical claims → Health Feedback, Science Feedback
   * Politics → country-specific political fact-checkers
   * General → Snopes, FactCheck.org, Full Fact
5. **Person-specific** - If content focuses on specific public figures:

   * Include fact-checkers from their home countries
   * Example: Claims about a US politician → include US fact-checkers

#### Exclusion Rule
**NEVER use services listed under "Fraudulent fact-checking websites"** on the Wikipedia page, regardless of how well they match other criteria.

#### Prioritization
When you must limit selections:

* Prioritize: User's language > Content's language > Geographic relevance
* Prefer well-established services (FactCheck.org, Snopes, Full Fact, AFP Fact Check, etc.)
* Include at least one international/general service

**Example Selection:**

* User: Polish speaker
* Content: English article about US vaccines
* Selected services:
  1. Demagog.pl (Polish, for user)
  2. FactCheck.org (US, for content geography)
  3. Snopes (US, general/medical)
  4. Health Feedback (health specialist)
  5. Full Fact (UK, English-speaking, general)

### Step 3: Search Each Fact-Checking Service
For each selected service, conduct targeted searches:

#### Search Strategy
1. **Extract 2-4 search terms** from the content:

   * Key person names
   * Main topics/subjects
   * Specific claims or events
   * Important keywords
2. **Translate terms** to the fact-checker's native language if needed
3. **Construct search queries** using DuckDuckGo with site operator:

   text

   ```
   Format: site:domain.com [search terms in appropriate language]

   Examples:
   - site:fullfact.org vaccines autism
   - site:demagog.org.pl szczepionki autyzm
   - site:factcheck.org Andrew Wakefield MMR
   - site:healthfeedback.org vaccine safety
   ```
4. **Execute 1-3 searches per fact-checker** (depending on content complexity)

#### Search Best Practices
* Keep queries concise (2-4 words typically)
* Start broad, then narrow if needed
* Don't repeat very similar queries
* If first search yields good results, proceed to analysis
* If first search yields poor results, try alternative terms

### Step 4: Analyze Search Results
For each fact-checking service:

1. **Review search results** - Examine the first 5-10 results from each search
2. **Select relevant articles** - Choose articles where:

   * Headline directly addresses the claim being verified
   * Content appears substantial (not just brief mentions)
   * Publication date is relevant (recent for ongoing issues, any date for historical debunks)
3. **Fetch and read articles** - Use `web_fetch` to retrieve the full text of 2-4 most relevant articles per fact-checker
4. **Extract key findings** for each article:

   * **Verdict** - What did the fact-checker conclude? (True, False, Misleading, Mixed, Unproven, etc.)
   * **Evidence** - What evidence did they cite?
   * **Context** - Any important nuance or context
   * **Relevance** - How directly does this address the user's claim?

> 详细内容已移至 `references/detail.md` - ### Step 5: Synthesize and Present Results
## Common Scenarios
### Scenario 1: Single Specific Claim
**User request:** "Is it true that 5G causes COVID-19?"

**Approach:**

* Identify claim: 5G technology causes or spreads COVID-19
* Select 4-5 general fact-checkers (international scope, tech/health focus)
* Search for "5G COVID" or "5G coronavirus"
* Expected result: Multiple fact-checkers will have debunked this
* Present: Clear consensus with explanation of why the claim is false

### Scenario 2: Article with Multiple Claims
**User request:** "Can you fact-check this article about climate change?"

**Approach:**

* Extract 3-5 specific verifiable claims from the article
* Select fact-checkers: user's language + climate-focused services
* Search each claim separately
* Present: Findings organized by claim, with overall assessment

### Scenario 3: Complex Political Claim
**User request:** "Did [politician] really say/do [thing]?"

**Approach:**

* Identify the specific claim and context
* Select fact-checkers from politician's country + user's language
* Search politician's name + key terms
* Present: Direct answer with context, including if statement was taken out of context

### Scenario 4: Viral Social Media Content
**User request:** "I saw this video on TikTok claiming [X], is it real?"

**Approach:**

* Identify what's being claimed in the video
* Select broad, well-known fact-checkers (viral content often fact-checked widely)
* Search for key terms from the claim
* Present: Whether it's been debunked, original context if misrepresented

### Scenario 5: Historical Claim
**User request:** "Did [historical event] really happen this way?"

**Approach:**

* Note that this is historical verification, may need broader research
* Select fact-checkers + consider using general web search for historical records
* Present: What fact-checkers say if available, acknowledge if claim is outside typical fact-checking scope

### Scenario 6: Very Fresh Content (Breaking News)
**User request:** "I just saw this article published today claiming [X]. Is it true?"

**Approach:**

* Check publication date: is it 3 days old or less?
* Search fact-checkers anyway (sometimes they work very quickly on major stories)
* If no fact-checks found:
  + **With task scheduling**: Schedule follow-up check for 3 days later, notify user of the scheduled check
  + **Without task scheduling**: Inform user that content is too fresh, suggest returning in 3 days
* Offer preliminary analysis using general web search
* Present: "This is very recent content. Fact-checkers haven't had time to verify yet. Here's what I found from general sources, but I recommend waiting for professional fact-checking."

**Example response:**

```text
This article was published just [X hours/days] ago, which is too recent for professional
fact-checkers to have verified the claims yet. They typically need a few days to conduct
thorough research.

I've scheduled a follow-up fact-check for [date in 3 days]. I'll notify you automatically
if fact-checkers publish verification by then.

In the meantime, here's what I found through general web research:
[preliminary findings with appropriate caveats]

Note: These are preliminary findings only. Professional fact-checkers may provide more
thorough verification in the coming days.
```

## 已知限制
### When Fact-Checkers Haven't Covered the Topic
If searches return no relevant results:

1. Try broader search terms
2. Try related claims that fact-checkers may have covered
3. If still no results, check if the content is recent (3 days or less)
4. **For fresh content (≤3 days old)**:
   * Acknowledge: "This is very recent content. Professional fact-checkers typically need a few days to verify claims."
   * If scheduling tools are available: Schedule a follow-up fact-check for 3 days later
   * If scheduling is not available: Suggest the user returns in 3 days for updated verification
   * Offer to do preliminary general web research in the meantime
5. **For older content**: Acknowledge "Professional fact-checkers haven't specifically addressed this claim"
6. Offer to do general web research instead
7. Consider if the claim is too obscure or too local for major fact-checkers

### Contradicting Fact-Checkers
If fact-checkers disagree:

1. Present all perspectives fairly
2. Note the disagreement explicitly
3. Consider if they're addressing slightly different aspects
4. Look for consensus on specific sub-points
5. Don't force a conclusion if the evidence is genuinely mixed

### Outdated Information
If fact-checks are old but the claim is current:

1. Note the publication dates
2. Search for more recent fact-checks
3. Consider if circumstances have changed
4. Acknowledge if using older sources due to lack of recent coverage

### Language Barriers
If key fact-checkers are in languages you don't fully understand:

1. Use web_fetch to retrieve the content
2. Focus on verdicts, ratings, and conclusion sections which are often clear
3. Use any English summaries or abstracts
4. Acknowledge limitations if language creates uncertainty

### Bias Concerns
Users may question fact-checker reliability:

1. Stick to well-established, internationally recognized services
2. Present findings from multiple fact-checkers to show consensus
3. Note if you're using fact-checkers from multiple countries/perspectives
4. Acknowledge that no source is perfect, but these are professional verification services

## Quality Checklist
Before presenting results, verify:

* Checked at least 3 different fact-checking services
* Included fact-checkers relevant to the user's language/location
* Included fact-checkers relevant to the content's context
* Excluded any fraudulent fact-checking services
* Read full articles, not just headlines or snippets
* Provided direct links to all sources cited
* Presented findings objectively without adding personal judgment
* Acknowledged any uncertainty or disagreement between sources
* Organized response clearly with specific findings, not vague summaries
* Used natural prose for main findings, lists only where truly helpful
* **If content is ≤3 days old with no fact-checks**: Noted this and scheduled follow-up OR suggested user return in 3 days
* **If providing preliminary analysis**: Clearly distinguished it from professional fact-checking

## Examples of Good Fact-Checking Services
**International/English:**

* FactCheck.org (US, general)
* Snopes (US, general)
* Full Fact (UK, general)
* AFP Fact Check (International, multilingual)
* PolitiFact (US, politics)

**Regional/Language-Specific:**

* Demagog.pl (Poland, Polish)
* Les Décodeurs (France, French)
* Correctiv (Germany, German)
* Maldita.es (Spain, Spanish)
* Aos Fatos (Brazil, Portuguese)
* Alt News (India, English/Hindi)
* Africa Check (Africa, multilingual)

**Specialized:**

* Health Feedback (health/medical claims)
* Climate Feedback (climate science claims)
* Science Feedback (general science claims)

**Note:** This is not exhaustive. Always fetch the current list from Wikipedia to see all available services.

## Final Notes
### Task Scheduling for Fresh Content
When content is very recent (≤3 days old) and hasn't been fact-checked yet:

**If task scheduling tools are available:**

* Automatically schedule a follow-up fact-check for 3 days later
* Store the original query, claims, and context
* When the scheduled task runs:
  + Re-search the same fact-checking services
  + Compare new findings to preliminary analysis
  + Notify user only if new fact-checks were found
  + Provide updated verification with links

**If task scheduling is NOT available:**

* Inform the user that the content is too fresh
* Suggest they return in 3 days for updated verification
* Provide preliminary analysis from general sources with appropriate caveats
* Make it clear that preliminary findings are not from professional fact-checkers

### Core Approach
This skill focuses on using professional fact-checking organizations rather than doing original research. These organizations employ journalists and researchers who specialize in verification. Your role is to:

1. Find what they've already published
2. Synthesize their findings
3. Present them clearly to the user
4. Schedule follow-ups for very recent content when possible

If a topic hasn't been covered by fact-checkers, acknowledge this and offer to do general research instead. Don't try to replace professional fact-checking with web searches alone, but do provide preliminary information when users need it for fresh content.

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力
- This fact-checking skill is mostly coherent, but it can automatically
  create delayed follow-up ch
- 触发关键词: checking, claims, skill, verify, mostly, fact

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程
1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 错误处理
| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题
### Q1: 如何开始使用Verify Claims？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Verify Claims有什么限制？
A: 请参考已知限制章节了解具体限制。
