# 详细参考 - verify-claims

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (text)

```text
Based on verification from five established fact-checking organizations, the claim that vaccines cause autism has been thoroughly debunked. Multiple independent reviews of the evidence have found no causal link between vaccination and autism spectrum disorder.

The origins of this claim trace back to a fraudulent 1998 study by Andrew Wakefield, which was later retracted by The Lancet. Fact-checkers consistently note that Wakefield lost his medical license, and subsequent large-scale studies involving millions of children have found no connection.

[Full Fact reviewed the evidence in 2023](link), concluding "There is no link between the MMR vaccine and autism." Their analysis examined 12 major studies and found consistent results across different populations and methodologies.

[FactCheck.org's comprehensive analysis](link) explains that "The myth persists despite overwhelming scientific consensus against it" and details how the original study was not only retracted but shown to involve falsified data.

However, [Demagog.pl](link) notes that while the vaccine-autism link is false, concerns about vaccine safety in general are legitimate and should be addressed through proper scientific channels rather than dismissed.

**Important context**: The persistence of this myth has real public health consequences, as fact-checkers note declining vaccination rates in some communities. Understanding why the claim was debunked helps address ongoing concerns.

**Sources consulted:**
- Full Fact: "MMR vaccine does not cause autism" - [link]
- FactCheck.org: "Wakefield's Fraudulent Research" - [link]
- Snopes: "Vaccines and Autism" - [link]
- Demagog.pl: "Szczepionki i autyzm - mit czy prawda?" - [link]
- Health Feedback: "Scientific consensus on vaccine safety" - [link]
```

### Step 5: Synthesize and Present Results
Organize findings into a clear, user-friendly format:

#### Handle Fresh Content First
Before presenting results, check if the content is very recent (3 days old or less):

1. **If fact-checks found**: Proceed normally with presentation
2. **If no fact-checks found AND content is ≤3 days old**:

   * Note that the content is too fresh for fact-checkers to have covered it yet
   * **If task scheduling is available**:
     + Schedule a follow-up fact-check for 3 days from now
     + Inform user: "I've scheduled a follow-up check for [date]. I'll notify you if fact-checkers have published verification by then."
   * **If task scheduling is NOT available**:
     + Suggest: "This content is very recent (published [date]). Fact-checkers typically need a few days to verify claims. I recommend checking back in 3 days for updated verification."
   * Offer preliminary analysis using general web search
   * Proceed with any available information from general sources
3. **If no fact-checks found AND content is older**:

   * Note that fact-checkers haven't specifically covered this
   * Offer general web research instead

#### Structure Your Response
1. **Opening summary** (2-3 sentences)

   * Overall consensus from fact-checkers
   * Brief answer to the user's question
2. **Key findings by claim** (if multiple claims)

   * Group related findings together
   * Present contradicting evidence if it exists
3. **Detailed evidence** (organized by fact-checker or by claim)

   * Include specific verdicts
   * Cite evidence fact-checkers used
   * Note any disagreements between fact-checkers
4. **Important context** (if relevant)

   * Historical background
   * Why the claim persists
   * Common misconceptions
5. **Source citations**

   * Provide direct links to all fact-checking articles referenced
   * Format: `[Fact-Checker Name]: Article Title (Date if available) - [URL]`

#### Presentation Guidelines
* **Be objective** - Present findings without inserting personal judgment
* **Be nuanced** - Avoid oversimplifying complex issues
* **Be clear about uncertainty** - If fact-checkers disagree or evidence is inconclusive, say so
* **Be balanced** - If some evidence supports and some contradicts, present both
* **Use accessible language** - Avoid jargon, explain technical terms
* **Highlight consensus** - When multiple fact-checkers agree, emphasize this

#### Formatting
* Use clear headers to organize different claims or themes
* Use natural prose, not bullet points, for the main findings
* Only use lists for: multiple similar items, source citations, or when explicitly helpful
* Include clickable citations throughout (not just at the end)

#### 示例
```text
Based on verification from five established fact-checking organizations, the claim that vaccines cause autism has been thoroughly debunked. Multiple independent reviews of the evidence have found no causal link between vaccination and autism spectrum disorder.

The origins of this claim trace back to a fraudulent 1998 study by Andrew Wakefield, which was later retracted by The Lancet. Fact-checkers consistently note that Wakefield lost his medical license, and subsequent large-scale studies involving millions of children have found no connection.

[Full Fact reviewed the evidence in 2023](link), concluding "There is no link between the MMR vaccine and autism." Their analysis examined 12 major studies and found consistent results across different populations and methodologies.

[FactCheck.org's comprehensive analysis](link) explains that "The myth persists despite overwhelming scientific consensus against it" and details how the original study was not only retracted but shown to involve falsified data.

However, [Demagog.pl](link) notes that while the vaccine-autism link is false, concerns about vaccine safety in general are legitimate and should be addressed through proper scientific channels rather than dismissed.

**Important context**: The persistence of this myth has real public health consequences, as fact-checkers note declining vaccination rates in some communities. Understanding why the claim was debunked helps address ongoing concerns.

**Sources consulted:**
- Full Fact: "MMR vaccine does not cause autism" - [link]
- FactCheck.org: "Wakefield's Fraudulent Research" - [link]
- Snopes: "Vaccines and Autism" - [link]
- Demagog.pl: "Szczepionki i autyzm - mit czy prawda?" - [link]
- Health Feedback: "Scientific consensus on vaccine safety" - [link]
```



