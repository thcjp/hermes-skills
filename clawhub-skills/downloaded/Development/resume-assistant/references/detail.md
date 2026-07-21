# 详细参考 - resume-assistant

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
from langchain.tools import Tool

resume_tools = [
    Tool(
        name="resume_polish",
        description="Polish and improve resume with 40+ checklist items",
        func=lambda input: agent.run_skill(
            "resume-assistant", "polish",
            {"resume_content": input, "language": "en"}
        )
    ),
    Tool(
        name="resume_score",
        description="Score a resume on 100-point scale with improvement suggestions",
        func=lambda input: agent.run_skill(
            "resume-assistant", "score",
            {"resume_content": input, "language": "en"}
        )
    ),
    Tool(
        name="resume_customize",
        description="Customize resume for a specific job position",
        func=lambda input: agent.run_skill(
            "resume-assistant", "customize",
            {"resume_content": input.split("---JD---")[0],
             "job_description": input.split("---JD---")[1],
             "language": "en"}
        )
    ),
    Tool(
        name="resume_export",
        description="Export resume to Word/Markdown/HTML/LaTeX/PDF",
        func=lambda input: agent.run_skill(
            "resume-assistant", "export",
            {"resume_content": input, "format": "html", "template": "modern"}
        )
    ),
]
```

## 代码示例 (bash)

```bash
curl -X POST https://your-agent-api.com/skills/resume-assistant/polish \
  -H "Content-Type: application/json" \
  -d '{
    "resume_content": "Your resume content...",
    "language": "en"
  }'

curl -X POST https://your-agent-api.com/skills/resume-assistant/score \
  -H "Content-Type: application/json" \
  -d '{
    "resume_content": "Your resume content...",
    "target_role": "Senior Frontend Engineer",
    "language": "en"
  }'

curl -X POST https://your-agent-api.com/skills/resume-assistant/customize \
  -H "Content-Type: application/json" \
  -d '{
    "resume_content": "Your resume content...",
    "job_description": "Job description...",
    "language": "en"
  }'

curl -X POST https://your-agent-api.com/skills/resume-assistant/export \
  -H "Content-Type: application/json" \
  -d '{
    "resume_content": "Your resume content...",
    "format": "html",
    "template": "modern"
  }'
```

## 代码示例 (javascript)

```javascript
// JavaScript pseudocode
const ROLE_SYS = 'system';  // LLM message role constant
const ROLE_USR = 'user';    // LLM message role constant

async function buildPrompt(command, args) {
  // Step 1: Load the skill persona prompt
  const personaPrompt = await loadFile('prompts/system.md');

  // Step 2: Load command-specific prompt
  const commandPrompt = await loadFile(`prompts/${command}.md`);

  // Step 3: Combine prompts into LLM messages
  const combined = `${personaPrompt}\n\n${commandPrompt}`;
  const messages = [
    { role: ROLE_SYS, content: combined },
    { role: ROLE_USR, content: args.resume_content }
  ];

  // Step 4: Add optional parameters
  if (args.language) {
    messages[1].content += `\n\nLanguage: ${args.language}`;
  }

  return messages;
}
```

## 代码示例 (python)

```python
def validate_args(command, args):
    """Validate arguments against skill.json schema."""
    schema = load_skill_json()
    cmd_schema = next(c for c in schema["commands"] if c["name"] == command)

    for arg in cmd_schema["arguments"]:
        if arg["required"] and arg["name"] not in args:
            raise ValueError(f"Missing required argument: {arg['name']}")

        if "enum" in arg and arg["name"] in args:
            if args[arg["name"]] not in arg["enum"]:
                raise ValueError(
                    f"Invalid value for {arg['name']}: {args[arg['name']]}. "
                    f"Must be one of: {arg['enum']}"
                )

        if arg["name"] not in args and "default" in arg:
            args[arg["name"]] = arg["default"]

    max_len = schema["config"]["max_resume_length"]
    if len(args.get("resume_content", "")) > max_len:
        raise ValueError(f"Resume exceeds {max_len} character limit")

    return args
```

## 代码示例 ()

```
┌──────────────────────────────────────────────────────┐
│                  Recommended Workflow                 │
├──────────────────────────────────────────────────────┤
│                                                      │
│  1. /resume score     ← Know where you stand         │
│     💬 "Score my resume"                             │
│          │                                           │
│          ▼                                           │
│  2. /resume polish    ← Fix all issues               │
│     💬 "Polish my resume"                            │
│          │                                           │
│          ▼                                           │
│  3. /resume customize ← Tailor per application       │
│     💬 "Tailor for this JD: ..."                     │
│          │                                           │
│          ▼                                           │
│  4. /resume export    ← Generate final files         │
│     💬 "Convert to PDF"                              │
│          │                                           │
│          ▼                                           │
│  5. /resume score     ← Verify improvement           │
│     💬 "Score my resume again"                       │
│                                                      │
└──────────────────────────────────────────────────────┘
```

## 代码示例 ()

```
resume-assistant/
├── skill.json                    # Skill manifest (JSON)
├── skill.yaml                    # Skill manifest (YAML)
├── SKILL.md                      # This documentation
├── prompts/
│   ├── system.md                 # Persona definition & quality standards
│   ├── polish.md                 # Polish prompt: 40+ item checklist
│   ├── customize.md              # Customize prompt: gap analysis & keywords
│   ├── export.md                 # Export prompt: 5 formats × 4 templates
│   └── score.md                  # Score prompt: 100-point rubric
├── templates/
│   ├── professional.md           # Classic corporate template
│   ├── modern.md                 # Contemporary tech/startup template
│   ├── minimal.md                # Ultra-clean senior template
│   ├── academic.md               # Formal academic CV template
│   └── export/
│       ├── resume.html           # HTML template (4 CSS themes)
│       └── resume.tex            # LaTeX template (XeLaTeX + CJK)
└── examples/
    ├── sample-resume-en.md       # English sample (high quality)
    ├── sample-resume-zh.md       # Chinese sample (high quality)
    ├── sample-resume-weak.md     # Weak sample (for scoring demo)
    └── usage.md                  # Usage examples & workflow guide
```

