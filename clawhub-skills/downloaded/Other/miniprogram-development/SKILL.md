---
slug: miniprogram-development
name: miniprogram-development
version: "1.28.12"
displayName: Miniprogram Development
summary: WeChat Mini Program development skill for building, debugging, previewing,
  testing, publishing, a...
license: MIT-0
description: |-
  WeChat Mini Program development skill for building, debugging, previewing,
  testing, publishing, a...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: program, development, miniprogram, wechat, mini, skill
tags:
- Other
tools:
- read
- exec
---

# Miniprogram Development

## Standalone Install Note

If this environment only installed the current skill, start from the CloudBase main entry and use the published `cloudbase/references/...` paths for sibling skills.

* CloudBase main entry: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/SKILL.md`
* Current skill raw source: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/miniprogram-development/SKILL.md`

Keep local `references/...` paths for files that ship with the current skill directory. When this file points to a sibling skill such as `auth-tool` or `web-development`, use the standalone fallback URL shown next to that reference.

**Cross-cutting protocols** (required before code changes or uploads):

* Change Safety Protocol: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/cloudbase-platform/references/protocols/change-safety-protocol.md`
* Deployment Gate: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/cloudbase-platform/references/protocols/deployment-gate.md`

## Activation Contract

### Use this first when

* The request is about WeChat Mini Program structure, pages, preview, publishing, or CloudBase mini program integration.

### Read before writing code if

* The user mentions `wx.cloud`, CloudBase mini programs, OPENID, or mini program deployment/debug workflows.

### Then also read

* CloudBase auth -> `../auth-wechat/SKILL.md` (standalone fallback: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/auth-wechat/SKILL.md`)
* CloudBase document DB -> `../no-sql-wx-mp-sdk/SKILL.md` (standalone fallback: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/no-sql-wx-mp-sdk/SKILL.md`)
* Mini Program WeChat Pay or Integration Center generated payment functions -> `../cloudbase-wechat-integration/SKILL.md` (standalone fallback: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/cloudbase-wechat-integration/SKILL.md`; official docs: `https://docs.cloudbase.net/integration/wechat-pay-miniprogram/index.md`)
* UI generation -> `../ui-design/SKILL.md` (standalone fallback: `https://cnb.cool/tencent/cloud/cloudbase/cloudbase-skills/-/git/raw/main/skills/cloudbase/references/ui-design/SKILL.md`) first

### Do NOT use for

* Web auth flows or Web SDK-specific frontend implementation.
* WeChat Pay, payment callbacks, refunds, or Official Account OAuth details; use `cloudbase-wechat-integration` for those scenarios.

### Common mistakes / gotchas

* Generating a Web-style login flow for mini programs.
* Mixing Web SDK assumptions into `wx.cloud` projects.
* Applying CloudBase constraints before confirming the project actually uses CloudBase.
* Making code or configuration changes without first following the Change Safety Protocol (`cloudbase-platform/references/protocols/change-safety-protocol.md`).
* Performing mini program upload/publish without first completing the checks in `cloudbase-platform/references/protocols/deployment-gate.md`.

## When to use this skill

Use this skill for **WeChat Mini Program development** when you need to:

* Build or modify mini program pages and components
* Organize mini program project structure and configuration
* Debug, preview, or publish mini program projects
* Work with WeChat Developer Tools workflows
* Handle mini program runtime behavior, assets, or page config files
* Integrate CloudBase in a mini program project when explicitly needed

**Do NOT use for:**

* Web frontend development (use `web-development`)
* Pure backend service development (use `cloudrun-development` or `cloud-functions` as appropriate)
* UI design-only tasks without mini program development context (use `ui-design`)

---

## How to use this skill (for a coding agent)

1. **Start with the general mini program workflow**

   * Treat WeChat Mini Program development as the default scope
   * Do not assume the project uses CloudBase unless the user or codebase indicates it
2. **Follow mini program project conventions**

   * Keep mini program source under the configured mini program root
   * Ensure page files include the required configuration file such as `index.json`
   * Check `project.config.json` before suggesting preview or IDE workflows
3. **Route by scenario**

   * If the task involves CloudBase, `wx.cloud`, cloud functions, CloudBase database/storage, or CloudBase identity handling, read [CloudBase integration reference](/api/v1/skills/miniprogram-development/file?path=references%2Fcloudbase-integration.md&ownerHandle=binggg)
   * If the task involves debugging, previewing, publishing, WeChat Developer Tools, or no-DevTools workflows, read [debug and preview reference](/api/v1/skills/miniprogram-development/file?path=references%2Fdevtools-debug-preview.md&ownerHandle=binggg)
   * If the task involves `tabBar`, icon assets, or label spacing, prefer the text-only custom `tabBar` default below unless the user explicitly requires icons
4. **Use CloudBase rules only when applicable**

   * CloudBase is an important mini program integration path, but not a universal requirement
   * Only apply CloudBase-specific auth, database, storage, or cloud function constraints when the project is using CloudBase
5. **Recommend the right preview/debug path**

   * Prefer WeChat Developer Tools for simulator, panel-based debugging, preview, and real-device validation
   * If WeChat Developer Tools is unavailable, use `miniprogram-ci` for preview, upload, and npm build workflows where appropriate

---

## General Project Rules

1. **Project Structure**

   * Mini program code should follow the project root configured in `project.config.json`
   * Keep page-level files complete, including `.json` configuration files
   * Ensure referenced local assets actually exist to avoid compile failures
2. **Configuration Checks**

   * Check `project.config.json` before opening, previewing, or publishing a project
   * Confirm `appid` is available when a real preview, upload, or WeChat Developer Tools workflow is required
   * Confirm `miniprogramRoot` and related path settings are correct
3. **Resource Handling**

   * For `tabBar`, prefer a text-only custom `tabBar` by default when the user does not explicitly need icons. This avoids icon asset handling, removes reserved icon space, and makes the label area easier to align.
   * Only generate local icon assets and configure `iconPath` / `selectedIconPath` when the user explicitly asks for tab icons or the design requires them.
   * When generating local asset references such as icons, ensure the files are downloaded into the project.
   * Keep file paths stable and consistent with mini program config files.

### Recommended default for simple `tabBar`

Use `tabBar.custom = true`, keep only `pagePath` and `text` in `app.json`, and render text-only items in the custom component so there is no icon slot and no extra blank area above the label.

`app.json`

```json
{
  "tabBar": {
    "custom": true,
    "list": [
      { "pagePath": "pages/index/index", "text": "首页" },
      { "pagePath": "pages/travel/travel", "text": "行程" },
      { "pagePath": "pages/my/my", "text": "我的" }
    ]
  }
}
```

Keep the custom `tabBar` layout text-only, and use flex centering or matching `height` and `line-height` to remove the blank area above the label. Switch to downloaded local icons only when the user explicitly wants icon-based tabs.

## CloudBase as a Mini Program Sub-Scenario

* If the user explicitly uses CloudBase, `wx.cloud`, Tencent CloudBase, 腾讯云开发, or 云开发, follow the CloudBase integration reference
* In CloudBase mini program projects, use `wx.cloud` APIs and CloudBase environment configuration appropriately
* Do not apply CloudBase-specific rules to non-CloudBase mini program projects

## Debugging, Preview, and Publishing

* If WeChat Developer Tools is available, use it as the primary path for simulator debugging, panel inspection, preview, and device validation
* If WeChat Developer Tools is not available, use `miniprogram-ci` as the fallback path for preview, upload, and npm build-related automation
* For detailed workflows, read [debug and preview reference](/api/v1/skills/miniprogram-development/file?path=references%2Fdevtools-debug-preview.md&ownerHandle=binggg)

## Minimal project skeleton

`app.js`

```js
App({
  onLaunch() {
    console.log("Mini Program launched");
  },
});
```

`pages/index/index.js`

```js
Page({
  data: {
    message: "Hello CloudBase Mini Program",
  },
});
```

`pages/index/index.wxml`

```xml
<view class="page">
  <text>{{message}}</text>
</view>
```

`pages/index/index.json`

```json
{
  "navigationBarTitleText": "Home"
}
```

`project.config.json`

```json
{
  "appid": "your-mini-program-appid",
  "projectname": "cloudbase-mini-program",
  "miniprogramRoot": "./",
  "compileType": "miniprogram"
}
```

## References

* [CloudBase Mini Program Integration](/api/v1/skills/miniprogram-development/file?path=references%2Fcloudbase-integration.md&ownerHandle=binggg) — use this when the mini program project explicitly integrates CloudBase
* [WeChat DevTools Debug and Preview](/api/v1/skills/miniprogram-development/file?path=references%2Fdevtools-debug-preview.md&ownerHandle=binggg) — use this for debugging, preview, publishing, and no-DevTools fallback workflows
* [Common Pitfalls](/api/v1/skills/miniprogram-development/file?path=references%2Fpitfalls.md&ownerHandle=binggg) — read before generating code for optional chaining, TDesign styling, Canvas + storage, and environment issues

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
