# skill-registry.db source_slug 重复问题深度分析报告（Round 2）

数据库：`d:\skills\skill-registry.db`  
生成时间：2026-07-20


## 一、总体概况

### 1.1 source_slug 记录数分布

| 每组记录数 | 组数 | 说明 |
|---|---|---|
| 1 | 41 | 无重复（单条） |
| 3 | 547 | 原始下载 + 差异化free + 差异化paid（**预期结构**） |
| 4 | 51 | 多出 1 条「第一轮差异化孤立paid」记录 |

**COUNT(\*)>2 的重复组共 598 组，涉及 1845 条记录。**


### 1.2 source 字段取值分布（全表）

| source | 记录数 |
|---|---|
| clawhub_differentiated | 878 |
| clawhub_download | 671 |
| clawhub | 298 |
| opensource_modified | 39 |
| original_creation | 23 |

### 1.3 重复组内的角色组合模式

| 角色组合模式 | 组数 | 含义 |
|---|---|---|
| 差异化free版 + 差异化paid版（有free配对） + 原始下载 | 547 | 预期干净结构 |
| 差异化free版 + 差异化paid版（有free配对） + 原始下载 + 第一轮差异化孤立paid版 | 51 | 多出一条round1孤立paid |

## 二、为什么同一 source_slug 会产生多条记录

经过逐条角色分类，重复来自**两个层级**：

**A. 预期的多版本结构（3 记录组的根因）**
每个上游 skill 下载后会做一次差异化，产出 free 与 paid 两个 edition，它们与原始下载共享同一个 `source_slug`（因为追溯的是同一个上游来源）。因此 3 记录组 = `原始下载 + 差异化free + 差异化paid`，这是**设计内的多版本结构，并非脏数据**。

**B. 第二轮差异化重复（4 记录组的根因）**
4 记录组在上述结构基础上，**多出 1 条「第一轮差异化孤立 paid」记录**。时间线显示存在两批差异化运行：
- **第一批（约 2026-07-18 07:42，round-1）**：对原始 skill 做了一次差异化，但**只产出了 paid 版**（edition=paid, pricing=freemium, parent_slug=NULL），并已上传到平台。
- **第二批（约 2026-07-18 08:45 / 10:12，round-2）**：对**同一个原始 skill** 又做了一次差异化，这次产出了完整的 free+paid 配对（new slug，parent_slug 互相关联）。
于是同一 `source_slug` 下出现：1 原始 + 1 round-1孤立paid + 1 round-2 free + 1 round-2 paid = 4 条。

**结论：4 记录组的「第 4 条记录」= 第一批差异化遗留的孤立 paid 版**，它被第二批的 free+paid 对所「取代」，但记录本身（含版本历史与平台上传）仍残留在库中。


## 三、local_path 文件存在性

重复组共 1845 条记录，local_path 检查结果：

- **存在：1844 条**
- **缺失：1 条**

### 缺失明细

| skill_id | slug | source_slug | role | edition | pricing | local_path |
|---|---|---|---|---|---|---|
| 644 | pcb-design-assistant | jlc-eda-drawing | round1_paid | paid | freemium | `d:\skills\differentiated-skills\Automation\pcb-design-assistant` |

> 注：该缺失记录 (id=644) 属于 round-1 孤立 paid，其父目录存在但 skill 子目录不存在，说明第一批差异化的产物文件可能已被清理，但 DB 记录仍保留。


## 四、parent_slug 关联分析

- 598/598 组存在 parent_slug 链。
- 51/598 组含有 round-1 孤立 paid 记录。

parent_slug 的规律：

- `diff_free` 的 parent_slug 指向同组的 `diff_paid` slug（free↔paid 配对）。

- `round1_paid` 的 parent_slug 为 NULL，且**没有任何记录的 parent_slug 指向它**（孤立无子）。

- `original` 的 parent_slug 为 NULL。


> 这印证了 round-1 paid 是「无配对、无子节点」的孤立产物，与 round-2 的 free+paid 配对在结构上完全脱钩。


## 五、4 记录组专项分析（第 4 条记录来源）

**实际共有 51 组 4 条记录的 source_slug**（注：用户提到的「10 组」为低估，实际 51 组；其中 10 组的第二批差异化 source 字段为 `clawhub_download`，另 41 组为 `clawhub`，这可能是「10」这一数字的来源）。


### 5.1 第 4 条记录的来源（round-1 孤立 paid）

每个 4 记录组的第 4 条均为第一批差异化遗留的孤立 paid 记录，样例：

| source_slug | original slug | round-1 孤立paid (第4条) | round-2 free | round-2 paid |
|---|---|---|---|---|
| admapix | admapix | ad-insight-hub | ad-creative-intel-free | ad-creative-intel |
| afrexai-business-automation | afrexai-business-automation | biz-auto-hub | bizauto-flow-free | bizauto-flow |
| ai-agent-helper | ai-agent-helper | agent-copilot-pro | prompt-architect-free | prompt-architect |
| auto-updater | auto-updater | update-guardian | smart-update-agent-free | smart-update-agent |
| auto-workflow | auto-workflow | autopilot-flow | workflow-catalyst-free | workflow-catalyst |
| automate-excel | automate-excel | excel-maestro | excel-ninja-free | excel-ninja |
| automation-workflow-builder | automation-workflow-builder | flow-architect | flowforge-builder-free | flowforge-builder |
| automation-workflows | automation-workflows | workflow-symphony | solo-workflow-engine-free | solo-workflow-engine |
| automation-workflows-0-1-0 | automation-workflows-0-1-0 | workflow-lite | workflow-essentials-free | workflow-essentials |
| aws-agentcore-langgraph | aws-agentcore-langgraph | aws-graph-agent | aws-agent-orchestrator-free | aws-agent-orchestrator |
| aws-infra | aws-infra | aws-cloud-architect | aws-cloud-inspector-free | aws-cloud-inspector |
| azure-infra | azure-infra | azure-cloud-architect | azure-cloud-inspector-free | azure-cloud-inspector |
| ... | （共 51 组，完整明细见 CSV） | | | |

### 5.2 round-1 与 round-2 的时间批次

**round-1 孤立 paid 记录的创建时间（按小时）：**

| 创建批次(到小时) | round-1 记录数 |
|---|---|
| 2026-07-18T07 | 51 |

**round-2 (free+paid 配对) 记录的创建时间（按小时）：**

| 创建批次(到小时) | round-2 记录数 |
|---|---|
| 2026-07-18T08 | 20 |
| 2026-07-18T10 | 82 |

> round-1 集中在 07:42，round-2 集中在 08:45 与 10:12，证实是**两次独立的差异化运行**。


### 5.3 round-1 孤立 paid 记录的外键引用（删除成本）

51 条 round-1 孤立 paid 记录在子表中的引用：

| 子表 | 引用行数 |
|---|---|
| versions | 102 |
| scores | 0 |
| operations | 1002 |
| platform_uploads | 95 |
| workflow_states | 0 |
| dependencies | 0 |
| pricing | 0 |

**51 条 round-1 记录全部带有子表引用**（versions=102、operations=1002、platform_uploads=95），其中 platform_uploads=95 表示**这些记录已经被上传到平台**，不能简单删除。


### 5.4 round-1 孤立 paid 记录清单（全部 51 条）

| id | slug | source_slug | pricing | created | versions | ops | uploads | path_exists |
|---|---|---|---|---|---|---|---|---|
| 601 | ad-insight-hub | admapix | freemium | 2026-07-18 07:42:43 | 2 | 23 | 4 | 是 |
| 627 | biz-auto-hub | afrexai-business-automation | freemium | 2026-07-18 07:42:44 | 2 | 22 | 2 | 是 |
| 602 | agent-copilot-pro | ai-agent-helper | freemium | 2026-07-18 07:42:43 | 2 | 22 | 4 | 是 |
| 647 | update-guardian | auto-updater | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 625 | autopilot-flow | auto-workflow | freemium | 2026-07-18 07:42:43 | 2 | 22 | 2 | 是 |
| 636 | excel-maestro | automate-excel | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 637 | flow-architect | automation-workflow-builder | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 651 | workflow-symphony | automation-workflows | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 650 | workflow-lite | automation-workflows-0-1-0 | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 604 | aws-graph-agent | aws-agentcore-langgraph | freemium | 2026-07-18 07:42:43 | 2 | 22 | 4 | 是 |
| 603 | aws-cloud-architect | aws-infra | freemium | 2026-07-18 07:42:43 | 2 | 22 | 4 | 是 |
| 605 | azure-cloud-architect | azure-infra | freemium | 2026-07-18 07:42:43 | 2 | 22 | 4 | 是 |
| 617 | netdisk-sync-pro | baidu-netdisk-skills | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 626 | batch-processor-pro | batch | freemium | 2026-07-18 07:42:43 | 2 | 22 | 2 | 是 |
| 629 | cdp-browser-master | browser-automation-cdp | freemium | 2026-07-18 07:42:44 | 2 | 24 | 4 | 是 |
| 609 | llm-assistant-hub | claude | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 645 | security-radar | clawsec-feed | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 630 | cloud-ops-orchestrator | cloud-infra-automation | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 646 | system-controller | control | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 634 | cron-scheduler-pro | cron | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 631 | cron-assist | cron-helper | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 633 | cron-master-pro | cron-mastery | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 632 | cron-guard | cron-worker-guardrails | freemium | 2026-07-18 07:42:44 | 2 | 24 | 4 | 是 |
| 635 | desktop-autopilot | desktop-control | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 628 | cad-insight-pro | drawing-analyzer | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 611 | longmemo-elite | elite-longterm-memory | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 610 | localmemo-pro | elite-longterm-memory-local | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 644 | pcb-design-assistant | jlc-eda-drawing | freemium | 2026-07-18 07:42:44 | 2 | 18 | 1 | 否 |
| 639 | linear-cli-pro | kyaukyuai-linear-cli | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 640 | linear-workflow-bot | linear-autopilot | freemium | 2026-07-18 07:42:44 | 2 | 24 | 4 | 是 |
| 641 | macro-pulse | macro-monitor | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 619 | persistent-memory-engine | memory | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 613 | memory-distiller-v2 | memory-compress | freemium | 2026-07-18 07:42:43 | 2 | 3 | 1 | 是 |
| 615 | memory-radar | memory-scan | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 606 | decision-architect | neosoul-decision-agent | freemium | 2026-07-18 07:42:43 | 2 | 22 | 4 | 是 |
| 618 | neurocache-pro | neural-memory-enhanced | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 638 | flow-editor-pro | node-red-manager | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 648 | vault-master-pro | obsidian | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 649 | vault-sync-engine | obsidian-1-0-0 | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 642 | notes-cli-toolkit | obsidian-notesmd-cli | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 643 | office-productivity-hub | office-automation-pro | freemium | 2026-07-18 07:42:44 | 2 | 21 | 1 | 是 |
| 608 | knowledge-ontology | ontology | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 620 | productivity-boost | productivity | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 621 | redis-cache-master | redis-store | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 607 | evolution-engine-v2 | self-improving | freemium | 2026-07-18 07:42:43 | 2 | 3 | 1 | 是 |
| 622 | self-evolving-ai | self-improving-agent | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 612 | memo-quickstart | simple-memory-skill | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |
| 614 | memory-orchestrator-v2 | smart-memory-manager | freemium | 2026-07-18 07:42:43 | 2 | 3 | 1 | 是 |
| 616 | multi-agent-dev-v2 | subagent-driven-development | freemium | 2026-07-18 07:42:43 | 2 | 3 | 1 | 是 |
| 623 | token-guard-pro | token-saver-skill | freemium | 2026-07-18 07:42:43 | 2 | 21 | 2 | 是 |
| 624 | tool-orchestrator | totalreclaw | freemium | 2026-07-18 07:42:43 | 2 | 20 | 2 | 是 |

## 六、去重策略建议

### 6.1 分类处置原则

| 组类型 | 数量 | 是否为脏数据 | 建议处置 |
|---|---|---|---|
| 3 记录组（original+diff_free+diff_paid） | 547 | 否（设计内多版本） | **全部保留**，无需去重 |
| 4 记录组（多 1 条 round1_paid） | 51 | 部分冗余 | 见 6.2/6.3，**不建议直接删除** |
| 1 记录组 | 41 | 否 | 保留 |

### 6.2 关于 round-1 孤立 paid 记录（4 记录组的第 4 条）

这些记录**已被上传到平台（95 条 platform_uploads）并带有版本/操作历史**，属于「已发布但被后续 round-2 取代」的产物。直接物理删除会：
1. 丢失平台上传记录（platform_uploads 95 行），导致线上制品与库脱钩；
2. 破坏 versions / operations 的历史可追溯性；
3. 其中 1 条（id=644）local_path 已缺失，删除反而能清理孤儿引用。

因此给出三套可选策略，按推荐度排序：


**策略 A（推荐）：保留全部 + 显式标记取代关系，不动 source_slug**

- 不删除任何记录，给 51 条 round-1 孤立 paid 记录的 `notes` 或新增 `superseded_by` 字段，标记被哪个 round-2 slug 取代（按 source_slug 关联即可定位）。
- 在查询层把 round-1 记录从「当前有效 edition」中排除（current_status 置为 `deprecated`/`superseded`）。
- 优点：零数据丢失，平台上传历史完整，可回滚。
- 适用：需要保留完整审计与上线历史的场景。


**策略 B：保留记录但重分配 source_slug，消除分组碰撞**

- 给每条 round-1 孤立 paid 记录一个**独立的 source_slug**（例如 `原source_slug__r1`），使其不再与 round-2 共享 source_slug。
- 这样 4 记录组将拆成：1 组 3 记录（original+round2_free+round2_paid）+ 1 组 1 记录（round1_paid）。
- 优点：source_slug 语义干净（一个 source_slug = 一次差异化的全部 edition）；保留全部记录与引用。
- 缺点：round-1 与原上游的溯源关系被弱化（需在 notes 里记原 source_slug）。


**策略 C（不推荐除非确认废弃）：物理删除 round-1 孤立 paid 记录**

- 仅当确认 round-1 制品已从平台下架、且不需要历史时，按 `id` 级联删除子表引用后删除 skills 行。
- 必须先删 `versions/operations/platform_uploads/pricing/dependencies/workflow_states/scores` 中 `skill_id IN (51个id)` 的行，再删 skills 行。
- 对 id=644（local_path 已缺失）可优先清理；其余 50 条均已有平台上传，删除风险高。


### 6.3 合并建议

- **不建议做内容合并**：round-1 与 round-2 是两次独立差异化，slug/local_path/品牌名均不同，内容并不等同，合并会造成语义混乱。
- 唯一可「合并」的是**元数据视角**：在展示层把同一 source_slug 下的多个 paid 版本按时间排序，只把最新 round-2 paid 作为「当前 paid edition」展示，round-1 paid 折叠为历史版本。


### 6.4 具体保留/删除/合并清单

| 对象 | 数量 | 动作 |
|---|---|---|
| 3 记录组的全部记录 | 1641 | **保留**（设计内结构） |
| 4 记录组的 original / diff_free / diff_paid | 153 | **保留**（等价于 3 记录结构） |
| 4 记录组的 round-1 孤立 paid | 51 | **保留但标记 deprecated/superseded**（策略A）；或重分配 source_slug（策略B） |
| id=644 (pcb-design-assistant) | 1 | local_path 已缺失，单独清理孤儿引用或重建目录 |
| 任何记录的内容合并 | 0 | **不合并**（两次差异化内容不等同） |

## 七、结论

1. `source_slug` 重复的根因是**多版本/多轮差异化**，而非下载重复。
2. **3 记录组（547 组）是预期的 original+free+paid 结构，无需处理。**
3. **4 记录组（51 组）多出的第 4 条 = 第一轮差异化遗留的孤立 paid 记录**，集中在 2026-07-18 07:42 批次，已被第二批（08:45/10:12）的 free+paid 配对取代。
4. 这 51 条 round-1 记录全部带有子表引用（含 95 条平台上传），**不可简单删除**，推荐采用策略 A（标记 deprecated）或策略 B（重分配 source_slug）。
5. local_path 完整率 1844/1845，仅 id=644 缺失，数据落盘情况良好。
