---
slug: photo-webcam
name: photo-webcam
version: "1.0.6"
displayName: Photo Webcam
summary: List and snapshot retrieval for webcams (especially foto-webcam.eu). Use
  this skill when the user...
license: MIT-0
description: |-
  List and snapshot retrieval for webcams (especially foto-webcam。eu)。Use when 用户需要Photo Webcam相关功能时使用。不适用于超出本技能能力范围的复杂需求。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。
tags:
- Other
tools:
  - - read
- exec
---

# Photo Webcam

Goal: Fetch a current image from a saved favorites list (number -> webcam page) and send it to the user.

## Data source (favorites)

Default file in the workspace:

* `docs/webcams/favorites-muenchen.json`

Format:

* `items[].id` (int)
* `items[].name` (string)
* `items[].page` (URL of the webcam page)
* optional `items[].image` (direct image URL)

## Typical user commands

* webcam 1
* webcam 3+4+5
* liste
* liste webcams
* fuege   hinzu

## Workflow: webcam N -> send image

1. Load favorites list from docs/webcams/favorites-muenchen.json.
2. Find entry with id equal to N.
3. Fetch snapshot:
   * If image is set: load that URL directly
   * Otherwise: derive current 1200 jpg from page URL
4. Save image to /tmp/webcamN.jpg
5. Send image via skill-platform CLI:
   skill-platform message send --channel telegram --target <CHAT_ID> --message “Webcam N Name” --media /tmp/webcamN.jpg

## Workflow: webcam 3+4+5 -> multiple images

Maximum 6 images per request; ask first if more are requested.

Run a separate skill-platform call for each ID — never bundle multiple images into a single command or response.

Example for “webcam 1+3”:

python3 ... --id 1 --out /tmp/webcam1.jpg
-> read name from script output
skill-platform message send --channel telegram --target <CHAT_ID> --message “Webcam 1 ” --media /tmp/webcam1.jpg

python3 ... --id 3 --out /tmp/webcam3.jpg
-> read name from script output
skill-platform message send --channel telegram --target <CHAT_ID> --message “Webcam 3 ” --media /tmp/webcam3.jpg

Each skill-platform command runs separately. The caption for each image comes exclusively from the script output (field “name”) of the respective call.

## Workflow: liste -> send favorites list

Send a plain text list:
Webcam 1 Name
Webcam 2 Name
etc.

No formatting, plain text only.

## Resolving the image URL (foto-webcam.eu)

For a webcam page like:

* `https://www.foto-webcam.eu/webcam/zugspitze/`

there is usually a direct “current” image at:

* `https://www.foto-webcam.eu/webcam/zugspitze/current/1200.jpg`

In practice: fetch the HTML with a browser User-Agent and search for a link matching `.../current/<digits>.jpg`.

## Script

Use the script:

* `skills/public/foto-webcam/scripts/foto_webcam_snapshot.py`

Examples:

* Snapshot via favorites ID:

  + `python3 skills/public/foto-webcam/scripts/foto_webcam_snapshot.py --favorites docs/webcams/favorites-muenchen.json --id 4 --out /tmp/webcam4.jpg`
* Snapshot via URL:

  + `python3 skills/public/foto-webcam/scripts/foto_webcam_snapshot.py --url https://www.foto-webcam.eu/webcam/zugspitze/ --out /tmp/zugspitze.jpg`

## Maintenance / adding webcams

* Add a new webcam: append to `favorites-muenchen.json` (new `id`, `name`, `page`).
* If a source is unreliable, set `image` to a direct JPG link.

Important: chat responses must be plain text only (no Markdown). For audio, use clean speech only (no special characters or formatting).

---

> Eine deutsche Version dieser Skill-Beschreibung ist weiter unten zu finden.

---

Ziel: Ein aktuelles Bild aus einer gespeicherten Favoritenliste (Nummer → Webcam-Seite) abrufen und an den Benutzer senden.

## Datenquelle (Favoriten)

Standarddatei im Workspace:

* `docs/webcams/favorites-muenchen.json`

Format:

* `items[].id` (int)
* `items[].name` (string)
* `items[].page` (URL der Webcam-Seite)
* optional `items[].image` (direkte Bild-URL)

## Typische Benutzerbefehle

* webcam 1
* webcam 3+4+5
* liste
* liste webcams
* fuege   hinzu

## Ablauf: webcam N -> Bild senden

1. Favoritenliste aus docs/webcams/favorites-muenchen.json laden.
2. Eintrag mit der entsprechenden ID finden.
3. Schnappschuss abrufen:
   * Falls `image` gesetzt ist: diese URL direkt laden
   * Andernfalls: aktuelles 1200-JPG aus der Seiten-URL ableiten
4. Bild unter /tmp/webcamN.jpg speichern
5. Bild per skill-platform CLI senden:
   skill-platform message send --channel telegram --target <CHAT_ID> --message "Webcam N Name" --media /tmp/webcamN.jpg

## Ablauf: webcam 3+4+5 -> mehrere Bilder

Maximal 6 Bilder pro Anfrage; bei mehr zuerst nachfragen.

Für jede ID einen separaten skill-platform-Aufruf ausführen — niemals mehrere Bilder in einem einzigen Befehl oder einer Antwort bündeln.

Beispiel für „webcam 1+3":

python3 ... --id 1 --out /tmp/webcam1.jpg
-> Name aus Script-Ausgabe lesen
skill-platform message send --channel telegram --target <CHAT_ID> --message "Webcam 1 " --media /tmp/webcam1.jpg

python3 ... --id 3 --out /tmp/webcam3.jpg
-> Name aus Script-Ausgabe lesen
skill-platform message send --channel telegram --target <CHAT_ID> --message "Webcam 3 " --media /tmp/webcam3.jpg

Jeder skill-platform-Befehl läuft separat. Die Bildunterschrift kommt ausschließlich aus der Script-Ausgabe (Feld „name") des jeweiligen Aufrufs.

## Ablauf: liste -> Favoritenliste senden

Einfache Textliste senden:
Webcam 1 Name
Webcam 2 Name
usw.

Keine Formatierung, nur reiner Text.

## Bild-URL auflösen (foto-webcam.eu)

Für eine Webcam-Seite wie:

* `https://www.foto-webcam.eu/webcam/zugspitze/`

gibt es normalerweise ein aktuelles Bild unter:

* `https://www.foto-webcam.eu/webcam/zugspitze/current/1200.jpg`

In der Praxis: HTML mit Browser-User-Agent abrufen und nach einem Link suchen, der auf `.../current/<Ziffern>.jpg` passt.

## Script

Das Script verwenden:

* `skills/public/foto-webcam/scripts/foto_webcam_snapshot.py`

Beispiele:

* Schnappschuss per Favoriten-ID:

  + `python3 skills/public/foto-webcam/scripts/foto_webcam_snapshot.py --favorites docs/webcams/favorites-muenchen.json --id 4 --out /tmp/webcam4.jpg`
* Schnappschuss per URL:

  + `python3 skills/public/foto-webcam/scripts/foto_webcam_snapshot.py --url https://www.foto-webcam.eu/webcam/zugspitze/ --out /tmp/zugspitze.jpg`

## Pflege / Webcams hinzufügen

* Neue Webcam hinzufügen: Eintrag in `favorites-muenchen.json` ergänzen (neue `id`, `name`, `page`).
* Bei unzuverlässiger Quelle: `image` auf eine direkte JPG-URL setzen.

Wichtig: Chat-Antworten nur als reiner Text (kein Markdown). Für Sprachausgabe: sauberer Text ohne Sonderzeichen oder Formatierung.

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

- List and snapshot retrieval for webcams (especially foto-webcam
- Use this skill when the user
- 触发关键词: retrieval, photo, list, webcams, especially, webcam, snapshot

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

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Photo Webcam？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Photo Webcam有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
