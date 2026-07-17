---
slug: note-processor
name: note-processor
version: "1.0.0"
displayName: Note Processor
summary: Summarize, extract keywords, search, and list research notes from research-assistant's
  database t...
license: MIT
description: |-
  Summarize, extract keywords, search, and list research notes from research-assistant's
  database t...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: summarize, list, note, search, processor, extract, keywords'
tags:
- Integrations
- Research
tools:
- read
- exec
---

# Note Processor

Analyze and summarize research notes to extract insights quickly.

## Quick Start

```bash
note_processor.py summarize <topic>
note_processor.py keywords <topic>
note_processor.py extract <topic> <keyword>
note_processor.py list
```

**Examples:**

```bash
note_processor.py summarize income-experiments

note_processor.py keywords security-incident

note_processor.py extract income-experiments skill

note_processor.py list
```

## Features

* **Summaries** - Overview of topic with statistics, tags, key points
* **Keywords** - Extract most common words (filters stop words)
* **Search** - Find notes containing specific keywords
* **List** - See all research topics with basic stats
* **Integration** - Works with research-assistant's database format

## When to Use

### After Research Sessions

```bash
note_processor.py summarize new-research-topic

note_processor.py keywords new-research-topic
```

### Before Writing Reports

```bash
note_processor.py extract income-experiments monetization

note_processor.py summarize income-experiments
```

### Reviewing Progress

```bash
note_processor.py list

note_processor.py keywords income-experiments
```

## Command Details

### summarize

Shows:

* Note count and word count
* Creation and last update dates
* Top 5 tags
* Key points (sentences with important words)
* 3 most recent notes

**Output example:**

```text
📊 Summary: income-experiments
------------------------------------------------------------
Notes: 4
Words: 63
Created: 2026-02-07
Last update: 2026-02-07

🏷️  Top Tags:
   content: 2
   automation: 2
   experiment: 2

💡 Key Points:
   1. First experiment: create and publish skills...
   2. Second experiment: content automation pipeline...
```

### keywords

Shows:

* Total unique keywords
* Top 20 keywords with frequency
* Filters common stop words (that, this, with, from, etc.)

**Output example:**

```text
🔤 Keywords: income-experiments
------------------------------------------------------------
Total unique keywords: 38

Top 20 Keywords:
  1. experiment           ( 4x)
  2. skill                ( 3x)
  3. SkillHub              ( 2x)
  4. content              ( 2x)
```

### extract

Shows:

* All notes containing the keyword
* Keyword highlighted in uppercase
* Timestamps and tags
* Preview of matched content

**Output example:**

```text
🔍 Search Results: 'skill' in income-experiments
------------------------------------------------------------
Found 4 match(es)

1. [2026-02-07 19:09:51]
   Tags: ideas, autonomous
   First experiment: create and publish **SKILL**s to SkillHub...
```

### list

Shows:

* All research topics
* Note count and word count
* Last update date
* Preview of most recent note

**Output example:**

```text
📚 Research Topics (5)
------------------------------------------------------------

income-experiments
   Notes: 4 | Words: 63 | Updated: 2026-02-07
   Latest: Experiment 2 STARTING: Content automation...

security-incident
   Notes: 1 | Words: 45 | Updated: 2026-02-07
   Latest: Day 1: Security vulnerability found...
```

## Integration with research-assistant

note-processor works with the same database as research-assistant (`research_db.json`).

### Typical Workflow

```bash
research_organizer.py add "new-topic" "Research finding here" "tag1" "tag2"

research_organizer.py add "new-topic" "Another finding" "tag3"

note_processor.py summarize new-topic

note_processor.py extract new-topic keyword

note_processor.py list
```

### Using Both Together

```bash
research_organizer.py add "experiment" "Test result 1" "testing"
research_organizer.py add "experiment" "Test result 2" "testing"
research_organizer.py add "experiment" "Conclusion: worked!" "results"

note_processor.py summarize experiment
note_processor.py keywords experiment

note_processor.py extract experiment conclusion
```

## Key Point Detection

The `summarize` command detects key points by finding sentences with important words:

* important, key, critical, essential
* must, should, note, remember
* warning, priority, critical

This helps surface actionable insights from your research.

## Keyword Extraction

The `keywords` command:

* Filters words shorter than 4 characters
* Removes common stop words
* Counts frequency across all notes
* Shows top 20 keywords

**Stop words filtered:**
that, this, with, from, have, been, will, what, when, where, which, their, there, would, could, should, about, these, those, other, into, through

## Use Cases

### Before Writing a Report

```bash
note_processor.py summarize research-topic

note_processor.py extract research-topic metrics

note_processor.py keywords research-topic
```

### Reviewing Research Progress

```bash
note_processor.py list

note_processor.py summarize current-project

note_processor.py keywords current-project
```

### Finding Specific Information

```bash
note_processor.py extract income-experiments monetization

note_processor.py extract security-incident path-validation

note_processor.py extract experiment conclusion
```

## Best Practices

1. **Use summaries** - Get overview before diving into details
2. **Search first** - Use extract before reading all notes
3. **Check keywords** - Find themes you might have missed
4. **List regularly** - Review all topics to see gaps
5. **Tag consistently** - Makes keywords more meaningful

## Data Location

Database: `~/.skill-platform/workspace/research_db.json`
Format: Compatible with research-assistant skill

## Limitations

* **Simple keyword extraction** - Frequency-based, not semantic
* **No NLP** - Basic text processing (no ML/AI)
* **Stop word list** - English-focused, customize for other languages
* **Key point detection** - Pattern-based, not understanding-based

## Tips

### For Better Keywords

* Use consistent terminology in your notes
* Avoid abbreviations or synonyms for the same concept
* Tag notes with important terms
* Review keywords to see if important terms appear

### For Better Summaries

* Write complete sentences in notes
* Include important words (key, critical, must, etc.)
* Tag notes with themes
* Regularly summarize to track progress

### For Better Search

* Use specific keywords in extract
* Search for related terms (synonyms)
* Check tags in results
* Use summaries to find the right topic

## Troubleshooting

### "Topic not found"

```text
Topic 'x' not found.
```

**Solution:** Check topic name spelling. Use `note_processor.py list` to see all topics.

### "No matches found"

```text
No matches for 'keyword' in topic 'x'
```

**Solution:** Try different keywords, check spelling, use `note_processor.py keywords` to find related terms.

### Poor keyword results

```text
Top Keywords are mostly common words
```

**Solution:**

* Use more specific terms in your notes
* Tag notes with important terms
* The stop word filter can be customized in the code

## Examples by Use Case

### Project Review

```bash
note_processor.py list

note_processor.py summarize project-x

note_processor.py keywords project-x
```

### Writing Documentation

```bash
note_processor.py extract security-incident vulnerability

note_processor.py summarize security-incident

note_processor.py keywords security-incident
```

### Preparing a Report

```bash
note_processor.py extract income-experiments monetization

note_processor.py summarize income-experiments

note_processor.py summarize income-experiments
```

## Integration with Other Skills

### With research-assistant

* research-assistant: add notes
* note-processor: analyze notes
* Use together: add → analyze → write report

### With task-runner

```bash
task_runner.py add "Summarize experiment results" "documentation"

note_processor.py summarize experiment

task_runner.py complete 1
```

### With file skills

```bash
note_processor.py extract research-topic important

research_organizer.py export research-topic ~/shared/summary.md

note_processor.py summarize research-topic > ~/shared/summary.txt
```

## Zero-Cost Advantage

This skill requires:

* ✅ Python 3 (included)
* ✅ No API keys
* ✅ No external dependencies
* ✅ No paid services
* ✅ Works with research-assistant (free)

Perfect for autonomous research workflows with no additional costs.

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
