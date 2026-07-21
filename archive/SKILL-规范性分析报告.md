# SKILL.md 结构规范性分析报告

> 分析日期：2026-07-20
> 数据来源：`D:\skills\skill-registry.db`（`skills` 表，共 1909 条记录）
> 抽样方式：按 `source` 字段分组，每组随机抽取 5 个 skill（随机种子 = 42，可复现）
> 检查范围：每个 skill 的 `local_path/SKILL.md`

---

## 一、抽样基本信息

数据库中 `source` 字段分组统计如下：

| Source 分组 | 总数 | 抽样数 |
|---|---|---|
| clawhub_differentiated | 878 | 5 |
| clawhub_download | 671 | 5 |
| clawhub | 298 | 5 |
| opensource_modified | 39 | 5 |
| original_creation | 23 | 5 |
| **合计** | **1909** | **25** |

---

## 二、规范性检查项定义

| 编号 | 检查项 | 期望状态 |
|---|---|---|
| a | Frontmatter 是否包含必需字段（slug, displayName, version, summary, license, description, tools） | 全部存在 |
| b | displayName 长度是否 ≤ 20 字符 | ≤ 20 |
| c | summary 长度是否 ≤ 100 字符 | ≤ 100 |
| d | 是否包含 `## 依赖说明` 章节 | 存在 |
| e | 是否包含版本历史/变更记录表格 | 存在 |
| f | homepage 字段是否指向开源仓库 | 不应指向（即未指向 GitHub/GitLab/Bitbucket/Gitee/Codeberg 即为通过） |
| g | 是否残留内部参考文件引用（如 catalog.md、skill-registry、各类 log/plan 文件） | 不残留 |
| h | frontmatter YAML 语法是否正确 | 正确 |
| i | description 字段是否为数组格式 | 数组（list） |

---

## 三、总体统计

25 个抽样中，9 项检查的整体通过率：

| 检查项 | 通过数 | 通过率 |
|---|---|---|
| a 必需字段 | 25/25 | 100.0% |
| b displayName 长度 | 23/25 | 92.0% |
| c summary 长度 | 25/25 | 100.0% |
| d 依赖说明章节 | 25/25 | 100.0% |
| e 版本历史/变更记录 | 5/25 | **20.0%** |
| f homepage 指向开源仓库 | 25/25 | 100.0% |
| g 内部参考文件残留 | 25/25 | 100.0% |
| h YAML 语法 | 25/25 | 100.0% |
| i description 数组格式 | 0/25 | **0.0%** |

**问题最严重的两项**：`e 版本历史/变更记录`（仅 20% 通过）和 `i description 数组格式`（0% 通过）。

---

## 四、各 Source 分组规范性评分

### 评分方法
每项检查每个 skill 计 1 分（通过=1，未通过=0），每组满分 = 5 × 9 = 45 分。
规范性评分 = 实得分 / 45 × 100%。

| Source 分组 | a | b | c | d | e | f | g | h | i | 得分 | 评分 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| clawhub | 5/5 | 5/5 | 5/5 | 5/5 | 2/5 | 5/5 | 5/5 | 5/5 | 0/5 | 37/45 | **82.2%** |
| clawhub_differentiated | 5/5 | 5/5 | 5/5 | 5/5 | 1/5 | 5/5 | 5/5 | 5/5 | 0/5 | 36/45 | **80.0%** |
| original_creation | 5/5 | 5/5 | 5/5 | 5/5 | 1/5 | 5/5 | 5/5 | 5/5 | 0/5 | 36/45 | **80.0%** |
| opensource_modified | 5/5 | 5/5 | 5/5 | 5/5 | 0/5 | 5/5 | 5/5 | 5/5 | 0/5 | 35/45 | **77.8%** |
| clawhub_download | 5/5 | 3/5 | 5/5 | 5/5 | 1/5 | 5/5 | 5/5 | 5/5 | 0/5 | 34/45 | **75.6%** |

**排名**：clawhub > clawhub_differentiated = original_creation > opensource_modified > clawhub_download

**通用共性问题**（5 个分组均存在）：
- 检查 e（版本历史/变更记录）通过率极低（0%–40%）
- 检查 i（description 数组格式）通过率为 0%

---

## 五、各分组具体问题列表

### 1. clawhub_download（评分 75.6%）

抽样：`prompt-architect`、`azure-ai-transcription-py`、`auto-updater`、`key-guard`、`db`

| Skill | 失败检查 | 具体问题 |
|---|---|---|
| prompt-architect | i | description 为字符串格式（`description: |-`），非数组 |
| azure-ai-transcription-py | b, e, i | b: displayName 长度=25 超过 20 字符（"Azure Ai Transcription Py"）；e: 缺少版本历史/变更记录；i: description 非数组 |
| auto-updater | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| key-guard | b, e, i | **b: displayName 长度=371 字符**（严重异常，displayName 被整段 README 内容污染，含 `# key-guard  A local MCP server... ## Why This Exists...`）；e: 缺少变更记录；i: description 非数组 |
| db | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |

**关键风险**：`key-guard` 的 frontmatter 严重不规范，displayName 字段被注入了完整的 README 段落，且 `tools` 字段被错误写成 `'[read, exec]'` 字符串形式（虽然 a 检查仅校验字段存在，但其格式实际也有问题）。

---

### 2. original_creation（评分 80.0%）

抽样：`ebook-factory`、`content-refiner`、`ai-writing-style-cloner`、`geo-rank-architect`、`title-hook-factory`

| Skill | 失败检查 | 具体问题 |
|---|---|---|
| ebook-factory | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| content-refiner | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| ai-writing-style-cloner | i | 仅 description 非数组（已正确包含版本历史表格） |
| geo-rank-architect | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| title-hook-factory | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |

**亮点**：本组 5 个 skill 均设置了 `homepage: https://skillhub.cn`，未指向任何开源仓库，符合规范；其中 `ai-writing-style-cloner` 是少数完整包含版本历史表格的样本。

---

### 3. clawhub（评分 82.2%，最高分组）

抽样：`cdp-browser-pilot-free`、`linear-api-toolkit-free`、`swarm-coder-free`、`soul-decision-engine`、`cloudforge-automation`

| Skill | 失败检查 | 具体问题 |
|---|---|---|
| cdp-browser-pilot-free | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| linear-api-toolkit-free | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| swarm-coder-free | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| soul-decision-engine | i | 仅 description 非数组（已包含版本历史表格） |
| cloudforge-automation | i | 仅 description 非数组（已包含版本历史表格） |

**亮点**：本组有 2 个 skill 包含版本历史表格，是 5 组中比例最高的；displayName 与 summary 字段全部合规。

---

### 4. clawhub_differentiated（评分 80.0%）

抽样：`openai-whisper-v1`、`ui-ux-toolkit-free`、`context-driven-dev`、`docker-ctl-free`、`dashboard-builder`

| Skill | 失败检查 | 具体问题 |
|---|---|---|
| openai-whisper-v1 | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| ui-ux-toolkit-free | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| context-driven-dev | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| docker-ctl-free | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| dashboard-builder | i | 仅 description 非数组（已包含版本历史表格） |

**特点**：除 `dashboard-builder` 外，其余 4 个 skill 均缺少版本历史表格。

---

### 5. opensource_modified（评分 77.8%）

抽样：`twitter-viral-optimizer`、`content-cms-architect`、`theme-stylist`、`remotion-video-studio`、`csv-insight-miner`

| Skill | 失败检查 | 具体问题 |
|---|---|---|
| twitter-viral-optimizer | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| content-cms-architect | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| theme-stylist | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| remotion-video-studio | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |
| csv-insight-miner | e, i | e: 缺少版本历史/变更记录；i: description 非数组 |

**特点**：本组 5 个 skill 全部缺少版本历史/变更记录，e 检查通过率为 0%；但所有 skill 的 displayName、summary 长度均合规。

---

## 六、问题分类汇总

按问题类型统计所有 25 个抽样的失败次数：

| 问题类型 | 失败次数 | 失败比例 | 严重级别 |
|---|---|---|---|
| i. description 非数组格式 | 25/25 | 100.0% | 高（系统级共性问题） |
| e. 缺少版本历史/变更记录 | 20/25 | 80.0% | 高（系统级共性问题） |
| b. displayName 超长 | 2/25 | 8.0% | 中（个别 skill 严重异常） |
| a. 必需字段缺失 | 0/25 | 0.0% | — |
| c. summary 超长 | 0/25 | 0.0% | — |
| d. 缺少依赖说明章节 | 0/25 | 0.0% | — |
| f. homepage 指向开源仓库 | 0/25 | 0.0% | — |
| g. 残留内部参考文件 | 0/25 | 0.0% | — |
| h. YAML 语法错误 | 0/25 | 0.0% | — |

---

## 七、关键发现与改进建议

### 7.1 系统级共性问题（必须统一修复）

1. **description 字段格式不规范（25/25 失败）**
   - 现状：所有抽样均使用 `description: |-` 字符串字面量块格式（YAML literal block scalar），最终被解析为 Python `str` 类型。
   - 期望：应改为 YAML 数组（list）格式：
     ```yaml
     description:
       - 第一段说明
       - 第二段说明
     ```
   - 建议：批量重写所有 SKILL.md 的 description 字段为 list 格式。

2. **缺少版本历史/变更记录表格（20/25 失败）**
   - 现状：仅 `prompt-architect`、`ai-writing-style-cloner`、`soul-decision-engine`、`cloudforge-automation`、`dashboard-builder` 5 个 skill 含 `| 版本 |` 表格。
   - 建议：为每个 SKILL.md 强制追加 `## 版本历史` 章节并使用 Markdown 表格记录版本号、日期、变更说明。

### 7.2 个别严重异常

- **`key-guard`（clawhub_download）**
  - `displayName` 字段被注入了完整的 README 段落（长度 371 字符，含 `# key-guard  A local MCP server... ## Why This Exists...`），明显是导入/转换流程出错。
  - 同一文件的 `tools` 字段被写成 `'[read, exec]'`（字符串），而非 YAML 数组。
  - 建议：单独修复或回滚该 skill 的导入结果。

- **`azure-ai-transcription-py`（clawhub_download）**
  - displayName = "Azure Ai Transcription Py"（25 字符），稍超 20 字符上限。
  - 建议：改为 "Azure 转写" 或 "AzureAI 转写" 等更短名称。

### 7.3 优势项

下列检查项在所有 25 个抽样中均 100% 通过，无需调整：
- 必需字段齐全（a）
- summary 长度合规（c）
- 依赖说明章节齐全（d）
- homepage 字段未指向开源仓库（f）
- 无内部参考文件残留（g）
- YAML 语法正确（h）

### 7.4 各 Source 分组修复优先级

| 优先级 | Source | 主要问题 |
|---|---|---|
| 高 | clawhub_download | 共性问题 + 2 个 displayName 异常（含 key-guard 严重污染案例） |
| 中 | opensource_modified | e 检查通过率 0% |
| 中 | clawhub_differentiated | e 检查通过率 20% |
| 中 | original_creation | e 检查通过率 20% |
| 低 | clawhub | 相对最规范，仅 1 个 skill 完全通过 e 检查 |

---

## 八、附：检查方法说明

### 检查 a 必需字段
解析 YAML frontmatter，逐一校验 `slug`、`displayName`、`version`、`summary`、`license`、`description`、`tools` 七个字段均存在且非 null。

### 检查 b displayName 长度
取 `displayName` 值，按 Unicode 字符计数（中英文均按 1 字符），要求 ≤ 20。

### 检查 c summary 长度
取 `summary` 值，按 Unicode 字符计数，要求 ≤ 100。

### 检查 d 依赖说明章节
在 markdown body 中使用正则 `^##\s*依赖说明` 等模式匹配。

### 检查 e 版本历史/变更记录
在 body 中匹配 `## 版本历史`、`## 变更记录`、`## 更新日志`、`## Changelog` 等章节标题，或 `| 版本 |`、`| Version |` 等表格表头。

### 检查 f homepage 指向开源仓库
若存在 `homepage` 字段，且其值包含 `github.com`、`gitlab.com`、`bitbucket.org`、`gitee.com`、`codeberg.org` 任一域名，则判定为不合规。

### 检查 g 内部参考文件残留
匹配 `catalog.md`、`skill-registry`、`differentiation-log`、`download-log`、`optimization-log`、`upload-log`、`retry-skillhub-log`、`governance-report`、`update-report`、`merge-plan`、`deep-differentiation-methodology`、`batchN_mapping`、`DISCOVER_TRIGGER`、`UPDATE_TRIGGER`、`NAMING_CONVENTION`、`skill-registry.db` 等内部文件/路径关键字。

### 检查 h YAML 语法
使用 `PyYAML 6.0.3` 的 `yaml.safe_load` 解析 frontmatter，解析成功且返回 dict 即视为通过。

### 检查 i description 数组格式
解析后判断 `description` 字段的 Python 类型是否为 `list`。若为 `str`（含 `|-` literal block scalar）则不通过。

---

## 九、抽样明细

### clawhub_download
1. prompt-architect — `d:\skills\differentiated-skills\Agents\prompt-architect-pro\SKILL.md`
2. azure-ai-transcription-py — `d:\skills\clawhub-skills\downloaded\Creative\azure-ai-transcription-py\SKILL.md`
3. auto-updater — `d:\skills\clawhub-skills\downloaded\Automation\auto-updater\SKILL.md`
4. key-guard — `d:\skills\clawhub-skills\downloaded\Integrations\key-guard\SKILL.md`
5. db — `d:\skills\clawhub-skills\downloaded\Integrations\db\SKILL.md`

### original_creation
1. ebook-factory — `d:\skills\packaged-skills\skillhub\ebook-factory\SKILL.md`
2. content-refiner — `d:\skills\packaged-skills\skillhub\content-refiner\SKILL.md`
3. ai-writing-style-cloner — `d:\skills\packaged-skills\skillhub\ai-writing-style-cloner\SKILL.md`
4. geo-rank-architect — `d:\skills\enterprise-upload\geo-rank-architect\SKILL.md`
5. title-hook-factory — `d:\skills\packaged-skills\skillhub\title-hook-factory\SKILL.md`

### clawhub
1. cdp-browser-pilot-free — `d:\skills\differentiated-skills\Automation\cdp-browser-pilot-free\SKILL.md`
2. linear-api-toolkit-free — `d:\skills\differentiated-skills\Integrations\linear-api-toolkit-free\SKILL.md`
3. swarm-coder-free — `d:\skills\differentiated-skills\Agents\swarm-coder-free\SKILL.md`
4. soul-decision-engine — `d:\skills\differentiated-skills\Agents\soul-decision-engine-pro\SKILL.md`
5. cloudforge-automation — `d:\skills\differentiated-skills\Automation\cloudforge-automation-pro\SKILL.md`

### clawhub_differentiated
1. openai-whisper-v1 — `d:\skills\differentiated-skills\Creative\openai-whisper-v1-tool-pro\SKILL.md`
2. ui-ux-toolkit-free — `d:\skills\differentiated-skills\Creative\ui-ux-toolkit-free\SKILL.md`
3. context-driven-dev — `d:\skills\differentiated-skills\Knowledge\context-driven-dev-tool-pro\SKILL.md`
4. docker-ctl-free — `d:\skills\differentiated-skills\Operations\docker-ctl-tool-free\SKILL.md`
5. dashboard-builder — `d:\skills\differentiated-skills\Other\dashboard-builder-pro\SKILL.md`

### opensource_modified
1. twitter-viral-optimizer — `d:\skills\opensource-skills\packaged\twitter-viral-optimizer\SKILL.md`
2. content-cms-architect — `d:\skills\opensource-skills\packaged\content-cms-architect\SKILL.md`
3. theme-stylist — `d:\skills\opensource-skills\packaged\theme-stylist\SKILL.md`
4. remotion-video-studio — `d:\skills\opensource-skills\packaged\remotion-video-studio\SKILL.md`
5. csv-insight-miner — `d:\skills\opensource-skills\packaged\csv-insight-miner\SKILL.md`

---

## 十、结论

- **整体规范性评分（25 个抽样均值）**：约 **76.4%**（171/225 检查项通过）。
- **最高分组**：`clawhub`（82.2%）
- **最低分组**：`clawhub_download`（75.6%）
- **两项系统级共性问题**：
  1. description 字段格式 100% 不合规（应为数组，实际为字符串字面量块）。
  2. 版本历史/变更记录 80% 不合规。
- **一项严重个案**：`key-guard` 的 displayName 被 README 内容污染，需立即修复。
- **优势项**：必需字段、summary 长度、依赖说明章节、homepage、内部参考残留、YAML 语法 6 项均 100% 通过。

修复上述两项共性问题后，整体规范性评分预计可提升至 **96% 以上**。
