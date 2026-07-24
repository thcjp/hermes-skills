# Skill生产规范v1.1 安全与合规审核报告（v2 / 第5轮终审）

> 审核角色：资深安全合规专家
> 审核日期：2026-07-18
> 审核范围：check_debranding.py、db.py、4个改造后SKILL.md（License）、skill-production-standards第三章（去标识）、数据安全、2个抽样改造文件
> 审核类型：五轮串联审核的最后一轮，需汇总全部发现
> 前四轮评分：QA 70 / 架构师 65 / PM 72 / 开发者 68

---

## 一、总体评分

**本轮（第5轮 安全合规）：63 / 100**

| 维度 | 得分 | 说明 |
|------|------|------|
| 安全漏洞修复（\b正则） | 5/20 | 第4轮发现的P0-3完全未修复，且经实测确认漏洞更严重（`(?<!\w)(?!\w)`修复方案也失效） |
| 数据安全（Token/权限/Git） | 8/20 | Token仍硬编码在2个Git跟踪文件中，文件权限过宽，.gitignore覆盖不全 |
| License合规 | 12/20 | 4个文件License章节存在但2个明确删除原作者署名，违反MIT要求 |
| 去标识合规 | 18/20 | 6+9项检测覆盖完整，但因\b失效导致自动化检测在中文上下文不可信 |
| 改造文件安全约束 | 12/10 | pan-file-commander-pro路径遍历防护不充分；infinite-memory-vault-pro风险可控 |
| db.py安全 | 8/10 | 参数化查询完整、db.py本身无硬编码Token（positive），但DB文件未加密 |
| **总计** | **63/100** | **未达安全合规基线（≥80分）** |

**评分理由**：第4轮开发者发现的P0-3（\b正则失效）经本轮验证完全属实且影响范围比预期更大——常规lookahead修复方案也失效，必须使用ASCII-only lookarounds。此外本轮新发现2个License P0级违规（memory-fortress-pro自相矛盾、pan-file-commander-pro明确删除原作者署名），以及Token仍残留在Git跟踪文件中。综合判断v1.1规范在安全合规维度尚未达到可发布标准。

---

## 二、安全与合规问题清单（P0/P1/P2分级）

### P0级问题（必须立即修复，阻断发布）

#### P0-1【安全·重复·已验证】\b正则在中文上下文中完全失效，禁止词检测形同虚设
- **状态**：第4轮发现，本轮验证属实，且修复方案比预期复杂
- **文件**：`d:\skills\skill-registry\check_debranding.py` 第15、16、19、22、23、24行
- **影响**：所有使用`\b`的禁止模式（clawhub、PostgreSQL、MCP、tenant等）在中文SKILL.md中完全无法检测
- **验证结果**：见第三节测试代码，4/4中文上下文测试用例失败
- **新增发现**：常规修复方案`(?<!\w)(?!\w)`也失效（因为Python 3的`\w`匹配Unicode字符含中文），必须使用`(?<![A-Za-z0-9_])(?![A-Za-z0-9_])`

#### P0-2【安全·重复】API Token硬编码在Git跟踪文件中
- **状态**：v1审计已发现，v1.1未修复
- **文件**：
  - `d:\skills\PROJECT_MEMORY.md` 第7行：`skh_7906ab19cefaf3854349fae7b8b97310c5582073b76acf1557731c0f1c612c11`（**Git已跟踪**，commit `40bb917`）
  - `d:\skills\upload-to-skillhub.ps1` 第80行：`clh_FYKOzz03rZocoNFDQiP8w1Z6JLIPDsORrCIJzjtBHdg`（**Git已跟踪**）
  - `d:\skills\retry-skillhub.ps1` 第8行：同SkillHub token（未跟踪但磁盘存在）
  - `d:\skills\retry-skillhub-v2.ps1` 第3行：同SkillHub token（未跟踪但磁盘存在）
  - `d:\skills\upload-differentiated.ps1` 第114、221行：两个token均有（未跟踪但磁盘存在）
- **影响**：Git仓库一旦push到公开remote（GitHub/GitLab），两个API Token立即泄露；即使后续删除文件，Git历史仍保留

#### P0-3【安全·重复】敏感文件权限过宽
- **状态**：v1审计已发现，v1.1未修复
- **文件**：
  - `d:\skills\skill-registry.db`：`NT AUTHORITY\Authenticated Users Allow Modify, Synchronize`
  - `d:\skills\.skillhub-credentials\api-key.txt`：`NT AUTHORITY\Authenticated Users Allow Modify, Synchronize`
- **影响**：任何通过Windows认证的用户（包括低权限服务账户）均可读取/修改数据库和Token文件

#### P0-4【安全·新发现】.gitignore未覆盖含Token的文件和数据库
- **状态**：本轮新发现
- **文件**：`d:\skills\.gitignore`
- **问题**：.gitignore仅排除`.skillhub-credentials/`、`*.key`、`*.pem`、`.env`，但**未排除**：
  - `PROJECT_MEMORY.md`（含SkillHub token，已被Git跟踪）
  - `upload-to-skillhub.ps1`（含ClawHub token，已被Git跟踪）
  - `retry-skillhub*.ps1`、`upload-differentiated.ps1`（含token，虽未跟踪但无防护）
  - `skill-registry.db`（含全量skill元数据，虽未跟踪但无防护，存在误提交风险）
- **影响**：未来`git add .`可能误将敏感文件加入版本控制

#### P0-5【License·新发现】memory-fortress-pro License章节自相矛盾
- **状态**：本轮新发现
- **文件**：`d:\skills\differentiated-skills\Agents\memory-fortress-pro\SKILL.md`
- **问题**：License章节声明"本技能基于原始开源作品改进，**保留原始版权声明**"，但改进记录中明确写"**删除所有外部URL引用与原作者署名**"。两处直接矛盾。
- **影响**：违反MIT License第1条"上述版权声明...应包含在所有副本中"

#### P0-6【License·新发现】pan-file-commander-pro明确删除原作者署名
- **状态**：本轮新发现
- **文件**：`d:\skills\differentiated-skills\Agents\pan-file-commander-pro\SKILL.md`
- **问题**：改进记录明确写"**移除原作者署名，改为本地引用格式**"
- **影响**：直接违反MIT License的版权保留要求；属于"完全清除原作者署名"的违规情况

---

### P1级问题（重要，需在下一版本修复）

#### P1-1【License·新发现】4个改造SKILL.md均未保留实际的原始版权声明
- **状态**：本轮新发现
- **文件**：ad-creative-intel-pro、aws-cloud-inspector-pro、doc-reasoning-analyst-pro、memory-fortress-pro
- **问题**：4个文件License章节均只写"原始作品：[名称]"，但**没有任何一行实际的"© [年份] [原作者姓名]"版权声明**。MIT License文本被完整粘贴，但版权人字段为空或仅写"改进作品：© 2026 [XXX]"
- **影响**：MIT License要求保留"上述版权声明"，仅粘贴License文本不含具体版权人信息不合规

#### P1-2【License·新发现】doc-reasoning-analyst-pro对MIT-0的描述误导
- **状态**：本轮新发现
- **文件**：`d:\skills\differentiated-skills\Agents\doc-reasoning-analyst-pro\SKILL.md`
- **问题**：声明"原始license：MIT-0（与MIT完全兼容，无版权限制）"
  - "与MIT完全兼容"：技术上正确（MIT-0代码可纳入MIT项目）
  - "无版权限制"：**误导**。MIT-0仍保留责任免责条款和"AS IS"条件，并非"无版权限制"
  - MIT-0与MIT是**两个不同license**：MIT-0明确放弃署名要求，MIT要求署名
- **影响**：可能误导后续维护者认为可以随意处置原始作品

#### P1-3【合规·重复·已验证】"71个文件全部通过检测"结论可信度存疑
- **状态**：第4轮已质疑，本轮验证确认方法论缺陷
- **问题**：因\b正则失效（P0-1），自动化检测在中文上下文不可靠。本轮使用修复版正则（ASCII-only lookarounds）对71个文件重新扫描，**实际未发现遗漏的禁止词**（数据本身是干净的），但**检测机制本身是坏的**——结论"正确"只是因为运气好，不是因为检测有效
- **影响**：未来若新增skill含中文上下文的禁止词，将无法被检测

#### P1-4【安全·新发现】pan-file-commander-pro路径遍历防护不充分
- **状态**：本轮新发现
- **文件**：`d:\skills\differentiated-skills\Agents\pan-file-commander-pro\SKILL.md` 第131、187、190、284-286、315、325、349行
- **问题**：示例命令使用相对路径（`./local-file.txt`、`docs/local.txt`），但**无显式的`../`路径遍历防护说明**。虽有第604行FAQ说明"单文件上传远端路径必须是文件名"，但未禁止`../`前缀
- **影响**：中低风险——bdpan工具本身可能处理路径校验，且路径相对于`/apps/bdpan/`限制了爆炸半径，但Skill应明确禁止`../`

#### P1-5【安全·新发现】infinite-memory-vault-pro记忆数据明文存储
- **状态**：本轮新发现
- **文件**：`d:\skills\differentiated-skills\Agents\infinite-memory-vault-pro\SKILL.md`
- **问题**：记忆系统以Markdown明文存储用户会话数据（SESSION-STATE.md、DECISIONS.md等），无加密
- **影响**：低风险——本地使用场景下可接受，但若记忆目录被同步到云盘或共享，存在泄露风险。建议在文档中明确"记忆目录禁止同步到云端"

---

### P2级问题（建议优化）

#### P2-1【安全·新发现】db.py的register_skill函数缺少edition/parent_slug参数
- **状态**：第1、4轮已发现，本轮确认db.py第85行`register_skill`函数签名未包含`edition`和`parent_slug`参数
- **影响**：与规范要求的edition机制不匹配（虽非安全问题，但影响数据完整性）

#### P2-2【安全·新发现】skill-registry.db无加密无认证
- **状态**：本轮发现
- **问题**：`sqlite3.connect(DB_PATH)`使用默认连接，无SQLCipher加密、无访问认证
- **影响**：低风险——本地SQLite通常不加密，但结合P0-3的过宽权限，风险叠加

#### P2-3【合规·新发现】技术术语allowlist中clawhub自身存在歧义
- **状态**：本轮发现
- **问题**：skill-production-standards第3章allowlist将`clawhub`列为禁止词，但skill-production-standards自身SKILL.md第232、236、239、251、255行**大量使用clawhub**（用于说明禁止词本身）。因skill-production-standards在`exclude_dirs`中被排除，故未触发检测
- **影响**：极低——设计合理（标准文档需要引用禁止词），但应在规范中明确说明"标准文档自身引用禁止词属于豁免"

---

## 三、\b正则失效的验证测试代码和修复方案

### 3.1 验证测试代码

测试文件已保存至工作目录，核心验证逻辑如下：

```python
import re

test_cases = [
    # (pattern_word, test_text, expected_matches)
    ('clawhub', '上传到clawhub平台', 1),       # 中文前后
    ('clawhub', '上传到clawhub', 1),            # 中文前，结尾后
    ('clawhub', 'clawhub平台', 1),              # 开头前，中文后
    ('clawhub', '使用clawhub工具', 1),
    ('PostgreSQL', '支持PostgreSQL数据源', 1),
    ('MCP', '支持MCP工具协议', 1),
    ('tenant', '使用tenant参数', 1),
    ('fishclaw', '基于fishclaw项目', 1),
    # 英文上下文（对照组，应总是匹配）
    ('clawhub', 'upload to clawhub platform', 1),
    ('clawhub', 'upload to clawhub.', 1),
    ('PostgreSQL', 'I use PostgreSQL database', 1),
    # 不应匹配（子串）
    ('clawhub', 'clawhubX should not match', 0),    # 后缀
    ('clawhub', 'Xclawhub should not match', 0),     # 前缀
]

# === 原始（漏洞）\b 模式 ===
# 8/13 用例失败，所有中文上下文用例均0匹配（应为1）
print("--- 原始 \\b 模式（漏洞）---")
for word, text, expected in test_cases:
    pattern = r'\b(' + word + r')\b'
    matches = [m.group(0) for m in re.finditer(pattern, text)]
    status = 'PASS' if len(matches) == expected else 'FAIL'
    print(f"  [{status}] \\b({word})\\b in \"{text}\": {matches}")

# === 修复方案1：(?<!\w)(?!\w) lookarounds ===
# 【关键发现】此方案也失效！因为Python 3的\w默认匹配Unicode（含中文）
# 中文与英文相邻时，两者都是\w，不产生边界
print("--- 修复方案1：(?<!\\w)(?!\\w) - 同样失效 ---")
for word, text, expected in test_cases:
    pattern = r'(?<!\w)(' + word + r')(?!\w)'
    matches = [m.group(0) for m in re.finditer(pattern, text)]
    status = 'PASS' if len(matches) == expected else 'FAIL'
    print(f"  [{status}] (?<!\\w)({word})(?!\\w) in \"{text}\": {matches}")

# === 修复方案2：(?<![A-Za-z0-9_])(?![A-Za-z0-9_]) ASCII-only ===
# 【正确修复】仅将ASCII字母数字下划线视为word字符
# 中文字符不属于[A-Za-z0-9_]，因此中文与英文相邻时产生边界
print("--- 修复方案2：(?<![A-Za-z0-9_])(?![A-Za-z0-9_]) - 正确 ---")
for word, text, expected in test_cases:
    pattern = r'(?<![A-Za-z0-9_])(' + word + r')(?![A-Za-z0-9_])'
    matches = [m.group(0) for m in re.finditer(pattern, text)]
    status = 'PASS' if len(matches) == expected else 'FAIL'
    print(f"  [{status}] ASCII-boundary({word}) in \"{text}\": {matches}")
```

### 3.2 测试结果（实测）

```
=== Verify \b failure on Chinese context ===
Test 1 (clawhub): []          <- 失败，应匹配1个
Test 2 (PostgreSQL): []       <- 失败，应匹配1个
Test 3 (MCP): []              <- 失败，应匹配1个
Test 4 (tenant): []           <- 失败，应匹配1个
Test 5 (English context): ['clawhub']  <- 对照组通过

--- 原始 \b 模式（漏洞）---
  [FAIL] \b(clawhub)\b in "上传到clawhub平台": []          <- 0匹配，应1
  [FAIL] \b(clawhub)\b in "上传到clawhub": []               <- 0匹配，应1
  [FAIL] \b(clawhub)\b in "clawhub平台": []                 <- 0匹配，应1
  [FAIL] \b(clawhub)\b in "使用clawhub工具": []             <- 0匹配，应1
  [FAIL] \bPostgreSQL\b in "支持PostgreSQL数据源": []       <- 0匹配，应1
  [FAIL] \bMCP\b in "支持MCP工具协议": []                   <- 0匹配，应1
  [FAIL] \btenant\b in "使用tenant参数": []                <- 0匹配，应1
  [FAIL] \bfishclaw\b in "基于fishclaw项目": []             <- 0匹配，应1
  [PASS] \b(clawhub)\b in "upload to clawhub platform": ['clawhub']
  [PASS] \b(clawhub)\b in "upload to clawhub.": ['clawhub']
  [PASS] \bPostgreSQL\b in "I use PostgreSQL database": ['PostgreSQL']
  [PASS] \b(clawhub)\b in "clawhubX should not match": []
  [PASS] \b(clawhub)\b in "Xclawhub should not match": []

Total failures with \b: 8/13

--- 修复方案1：(?<!\w)(?!\w) - 同样失效 ---
  [FAIL] (?<!\w)(clawhub)(?!\w) in "上传到clawhub平台": []   <- 同样0匹配！
  ... (8/13失败，与\b完全相同)

--- 修复方案2：(?<![A-Za-z0-9_])(?![A-Za-z0-9_]) - 正确 ---
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "上传到clawhub平台": ['clawhub']
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "上传到clawhub": ['clawhub']
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "clawhub平台": ['clawhub']
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "使用clawhub工具": ['clawhub']
  [PASS] (?<![A-Za-z0-9_])(PostgreSQL)(?![A-Za-z0-9_]) in "支持PostgreSQL数据源": ['PostgreSQL']
  [PASS] (?<![A-Za-z0-9_])(MCP)(?![A-Za-z0-9_]) in "支持MCP工具协议": ['MCP']
  [PASS] (?<![A-Za-z0-9_])(tenant)(?![A-Za-z0-9_]) in "使用tenant参数": ['tenant']
  [PASS] (?<![A-Za-z0-9_])(fishclaw)(?![A-Za-z0-9_]) in "基于fishclaw项目": ['fishclaw']
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "upload to clawhub platform": ['clawhub']
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "upload to clawhub.": ['clawhub']
  [PASS] (?<![A-Za-z0-9_])(PostgreSQL)(?![A-Za-z0-9_]) in "I use PostgreSQL database": ['PostgreSQL']
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "clawhubX should not match": []
  [PASS] (?<![A-Za-z0-9_])(clawhub)(?![A-Za-z0-9_]) in "Xclawhub should not match": []
  全部13/13 PASS
```

### 3.3 漏洞根因分析

```
Python 3 的 \w 默认匹配 Unicode word 字符（含中文汉字）
\b 仅在 \w 与 \W 的交界处匹配
当中文字符与英文字符相邻时：
  - 中文字符（如"到"）= \w（Unicode word）
  - 英文字符（如"clawhub"的"c"）= \w（ASCII word）
  - 两者都是 \w => 不产生 \b 边界 => \b(clawhub)\b 匹配失败
```

### 3.4 推荐修复方案

**修复check_debranding.py**（第15-24行的所有`\b`模式）：

```python
# 修复前（漏洞）
FORBIDDEN_PATTERNS = [
    (r'\b(clawhub|clawsec|clawdbot|openclaw)\b', '平台烙印词', 'high'),
    (r'\b(clawhut|clawhob|clawhvb)\b', '平台烙印词变体', 'high'),
    (r'\b(fishclaw|narrato|dailyhot|novel_bridge|totalreclaw|kyaukyuai)\b', '项目烙印词', 'high'),
    (r'\bPostgreSQL\b', '内部系统词-PostgreSQL', 'high'),
    (r'\bMCP\b', '内部系统词-MCP', 'medium'),
    (r'\btenant\b', '内部系统词-tenant', 'high'),
]

# 修复后（正确）- 使用 ASCII-only lookarounds
FORBIDDEN_PATTERNS = [
    (r'(?<![A-Za-z0-9_])(clawhub|clawsec|clawdbot|openclaw)(?![A-Za-z0-9_])', '平台烙印词', 'high'),
    (r'(?<![A-Za-z0-9_])(clawhut|clawhob|clawhvb)(?![A-Za-z0-9_])', '平台烙印词变体', 'high'),
    (r'(?<![A-Za-z0-9_])(fishclaw|narrato|dailyhot|novel_bridge|totalreclaw|kyaukyuai)(?![A-Za-z0-9_])', '项目烙印词', 'high'),
    (r'(?<![A-Za-z0-9_])PostgreSQL(?![A-Za-z0-9_])', '内部系统词-PostgreSQL', 'high'),
    (r'(?<![A-Za-z0-9_])MCP(?![A-Za-z0-9_])', '内部系统词-MCP', 'medium'),
    (r'(?<![A-Za-z0-9_])tenant(?![A-Za-z0-9_])', '内部系统词-tenant', 'high'),
]
```

**重要警告**：不要使用`re.UNICODE`标志或`(?u)`——这会让`\w`继续匹配中文，问题依旧。也不要用`(?<!\w)(?!\w)`——同样失效。**唯一正确方案是显式ASCII字符类`[A-Za-z0-9_]`**。

### 3.5 修复后对71个文件的实际扫描结果

本轮使用修复版正则对`d:\skills\differentiated-skills`下所有SKILL.md重新扫描：

```
TOTAL SCAN SUMMARY
  Files scanned: 71
  Files with NEW issues (missed by \b): 0
  Total new issues missed: 0
  Original '71 files all passed' conclusion: OK (by luck, not by design)
```

**结论**：71个文件实际上**不包含**中文上下文中的禁止词（数据是干净的），所以"71个文件全部通过"的结论**碰巧正确**。但**检测机制本身是坏的**——这次通过纯属运气，未来新增skill若含中文上下文的禁止词将无法被检测。修复正则是必须的。

---

## 四、License合规审核结果表

| 文件 | 原始License | 原始版权声明保留 | 改进作品署名 | License兼容性 | 违规情况 | 严重度 |
|------|-------------|------------------|--------------|---------------|----------|--------|
| ad-creative-intel-pro | MIT | 部分（仅写"原始作品：广告创意数据API客户端"，无具体版权人） | 改进作品：© 2026 Ad Creative Intel Pro | MIT→MIT 兼容 | 未保留实际版权人姓名 | P1 |
| aws-cloud-inspector-pro | MIT | 部分（保留slug：aws-infra，无版权人） | 改进作品：© 2026 aws-cloud-inspector-pro contributors | MIT→MIT 兼容 | 未保留实际版权人姓名 | P1 |
| doc-reasoning-analyst-pro | MIT-0 | 不适用（MIT-0明确放弃署名要求） | 改进作品：© 2026 文档推理分析师（专业版） | MIT-0→MIT 兼容（MIT-0允许重license） | 描述"无版权限制"误导 | P1 |
| memory-fortress-pro | MIT | **未保留**（明确写"删除所有外部URL引用与原作者署名"） | 改进作品：© 2026 记忆堡垒（专业版） | MIT→MIT 兼容 | **License章节自相矛盾**，明确删除原作者署名 | **P0** |
| pan-file-commander-pro（抽样） | MIT | **未保留**（明确写"移除原作者署名，改为本地引用格式"） | 改进作品：© 2026 pan-file-commander-pro | MIT→MIT 兼容 | **明确删除原作者署名** | **P0** |

### 4.1 详细审核说明

**ad-creative-intel-pro**：
- License章节结构完整，包含MIT License全文
- 原始作品仅写"广告创意数据 API 客户端"（generic名称，无具体作者）
- 改进作品署名正确
- 问题：未保留实际的"© [year] [original author]"版权人信息

**aws-cloud-inspector-pro**：
- License章节保留原始slug（aws-infra），但无版权人
- 改进作品署名包含"contributors"措辞，相对规范
- 问题：同上，未保留实际版权人信息

**doc-reasoning-analyst-pro（原始license为MIT-0）**：
- 这是4个文件中**唯一License处理技术上合规**的（MIT-0明确放弃署名要求）
- 但描述"MIT-0（与MIT完全兼容，无版权限制）"存在两处误导：
  1. "与MIT完全兼容"——技术上正确，但暗示两者等同，实际是两个不同license
  2. "无版权限制"——错误。MIT-0仍保留"AS IS"条件和责任免责条款
- 正确描述应为："MIT-0（放弃署名要求，保留责任免责条款；可与MIT兼容）"

**memory-fortress-pro**：
- **最严重的License违规**：License章节声明"保留原始版权声明"，但改进记录明确写"删除所有外部URL引用与原作者署名"
- 这是直接的内部矛盾，属于"完全清除原作者署名"的违规情况
- 必须二选一：要么真正保留原作者署名，要么修改License章节声明不保留

**pan-file-commander-pro（抽样审核）**：
- 改进记录明确写"移除原作者署名，改为本地引用格式"
- 这是**主动承认删除原作者署名**，直接违反MIT License
- 即使改为"本地引用格式"，也不等同于保留版权声明

### 4.2 是否有"完全清除原作者署名"的违规情况？

**是，有2个文件存在明确违规**：
1. `memory-fortress-pro`：License章节声称保留但实际删除（自相矛盾）
2. `pan-file-commander-pro`：改进记录明确写"移除原作者署名"

**另外2个文件（ad-creative-intel-pro、aws-cloud-inspector-pro）**：
- 未明确声明删除，但也未实际保留原作者姓名
- 属于"未保留"而非"主动清除"，违规程度较轻

**doc-reasoning-analyst-pro**：
- 原始license为MIT-0，MIT-0明确放弃署名要求
- 因此不保留原作者署名是**合规的**
- 但描述存在误导（见4.1）

---

## 五、去标识合规审核结果

### 5.1 6项自动化检测 + 9项人工检查覆盖度

读取`d:\skills\differentiated-skills\Agents\skill-production-standards\SKILL.md`第三章：

**6项自动化检测（3.1节）**：
1. 平台烙印词检测（clawhub/clawsec/clawdbot/openclaw等）
2. 项目烙印词检测（fishclaw/narrato/dailyhot等）
3. 内部系统词检测（PostgreSQL/MCP/tenant）
4. 溯源词检测（based on/forked from/inspired by等）
5. 原仓库URL检测（github.com + clawhub/openclaw等域名）
6. 原作者署名检测（author:/created by字段）

**9项人工检查（3.2节）**：
1. 原作者姓名残留
2. 原作者GitHub用户名残留
3. 原仓库内部URL残留
4. 原项目内部代号残留
5. 原项目内部术语残留
6. 原项目特有注释残留
7. 原项目特有文件名残留
8. 原项目特有目录结构残留
9. 原项目特有错误信息残留

**覆盖度评估**：6+9项覆盖了去标识的主要场景，**覆盖度合格**。

### 5.2 技术术语allowlist合规性

allowlist（3.3节）包含：
- `MCP`：Agent工具协议标准术语——合规
- `PostgreSQL`：主流数据库——合规
- `tenant`：多租户标准术语——合规
- `SkillHub`：当前平台名称——合规（自身平台）
- `clawhub`：在allowlist的`ALLOWED_CONTEXTS`中——用于说明禁止词本身

**合规性评估**：allowlist设计合理，技术术语保留是必要的。

### 5.3 "71个文件全部通过检测"结论的可信度

**结论：可信度存疑（P1-3）**

**原因**：
1. 检测机制本身存在P0-1漏洞（\b正则失效）
2. 本轮使用修复版正则重新扫描，71个文件**实际未发现遗漏的禁止词**
3. 因此"71个文件全部通过"的**结论碰巧正确**，但**方法论是坏的**
4. 未来若新增skill含中文上下文的禁止词（如"上传到clawhub平台"），将无法被检测
5. 在修复P0-1之前，任何"通过检测"的结论都不能完全信任

**建议**：修复P0-1后，重新运行check_debranding.py对全部71个文件进行复检，并发布"修复后复检通过"的结论。

---

## 六、数据安全审核

### 6.1 数据库中存储的skill元数据是否有敏感信息？

**审核db.py后确认**：
- 数据库存储：slug、name、version、category、description、price_tier、file_path、hash等元数据
- **未存储**：API Token、用户密码、个人身份信息（PII）
- **风险**：低——元数据本身非敏感，但skill内容可能含敏感示例

### 6.2 API Token存储方式是否安全？

**审核结果：不安全（P0-2、P0-3、P0-7）**

| 存储位置 | 方式 | 风险 |
|----------|------|------|
| `.skillhub-credentials/api-key.txt` | 明文文件 | 文件权限过宽（Authenticated Users可读） |
| `PROJECT_MEMORY.md` | 明文，**Git已跟踪** | Git历史泄露风险 |
| `retry-skillhub.ps1` 等4个脚本 | 明文硬编码 | 脚本泄露即Token泄露 |

**正确做法**：
1. Token仅存储在`.skillhub-credentials/api-key.txt`，使用DPAPI加密（PowerShell的`ConvertTo-SecureString`）
2. 脚本运行时从加密文件读取，不在代码中硬编码
3. 文件权限设置为仅当前用户可读（`icacls /inheritance:r /grant:r "$env:USERNAME:(R)"`）

### 6.3 Git仓库是否可能泄露Token？

**审核结果：是，存在泄露风险（P0-2、P0-8）**

**Git仓库状态**：
- 仓库路径：`d:\skills\.git`
- 提交历史：3个commit（Initial commit / feat: add 600 optimized ClawHub skills / docs: add upload script）

**Git跟踪状态验证**：
```
TRACKED: PROJECT_MEMORY.md              <- 含SkillHub Token
TRACKED: upload-to-skillhub.ps1         <- 含ClawHub Token
NOT TRACKED: retry-skillhub.ps1          <- 含Token，未跟踪但磁盘存在
NOT TRACKED: retry-skillhub-v2.ps1       <- 含Token，未跟踪但磁盘存在
NOT TRACKED: upload-differentiated.ps1   <- 含Token，未跟踪但磁盘存在
NOT TRACKED: .skillhub-credentials/      <- 正确排除
NOT TRACKED: skill-registry.db          <- 未跟踪但未在.gitignore中
```

**风险场景**：
1. 若`git push`到公开remote（GitHub/GitLab），`PROJECT_MEMORY.md`和`upload-to-skillhub.ps1`中的Token立即泄露
2. 即使后续`git rm`删除文件，Git历史仍保留Token
3. 即使从未push，若仓库被复制或备份，Token随之泄露

**.gitignore覆盖度**：
- 已排除：`.skillhub-credentials/`、`*.key`、`*.pem`、`.env`
- **未排除**：`PROJECT_MEMORY.md`、`*.ps1`（含token的脚本）、`skill-registry.db`

---

## 七、改造文件安全审核

### 7.1 pan-file-commander-pro审核

**文件**：`d:\skills\differentiated-skills\Agents\pan-file-commander-pro\SKILL.md`

**安全约束审核**：
- 路径使用相对路径（`./local-file.txt`、`docs/local.txt`）——合理
- 第604行FAQ说明"单文件上传远端路径必须是文件名，禁止以`/`结尾"——部分约束
- **缺失**：无显式的`../`路径遍历防护说明

**路径遍历风险**（P1-4）：
- 示例命令使用`bdpan upload ./local.txt docs/local.txt`格式
- 虽未显式禁止`../`，但路径相对于`/apps/bdpan/`，限制了爆炸半径
- 风险等级：中低
- 建议：在安全约束章节明确禁止`../`前缀，并说明bdpan工具自身的路径校验机制

**其他安全约束**：
- 无敏感操作（如删除）的二次确认机制
- 无文件大小限制说明
- 无并发操作的安全说明

### 7.2 infinite-memory-vault-pro审核

**文件**：`d:\skills\differentiated-skills\Agents\infinite-memory-vault-pro\SKILL.md`

**数据泄露风险审核**：
- 记忆系统以Markdown明文存储（SESSION-STATE.md、DECISIONS.md等）——P1-5
- 无加密机制
- 无访问控制

**风险场景**：
1. 若记忆目录被同步到云盘（OneDrive/Dropbox），用户会话数据泄露
2. 若记忆目录在共享文件夹中，其他用户可读取
3. 若记忆内容含敏感信息（如API Key、密码），将以明文存储

**风险等级**：低（本地使用场景下可接受）

**建议**：
- 在SKILL.md中明确警告"记忆目录禁止同步到云端"
- 建议添加`.gitignore`排除记忆目录
- 建议提供"敏感记忆脱敏"工具，自动检测并加密敏感信息

---

## 八、全部5轮审核综合总结

### 8.1 各轮评分汇总

| 轮次 | 角色 | 评分 | 主要发现 |
|------|------|------|----------|
| 第1轮 | QA工程师 | 70/100 | skills表缺edition列、parent_slug缺失、3张死表、clawhub/PostgreSQL未加入allowlist |
| 第2轮 | 架构师 | 65/100 | 8大维度评分无持久化、10步工作流无状态机持久化、外键约束未启用、无事务边界 |
| 第3轮 | 产品经理 | 72/100 | 规范自身frontmatter缺edition字段、memory-fortress-pro换皮嫌疑（46.8%重叠）、3个专业版定价归类争议 |
| 第4轮 | 开发者 | 68/100 | **\b正则中文失效（P0-3新发现）**、skills表缺edition/parent_slug、评分无持久化、工作流无状态机、反引号计数误判、memory-fortress-pro 46.8%重叠 |
| 第5轮 | 安全合规 | 63/100 | **\b正则失效验证+修复方案（P0-1）**、Token硬编码在Git跟踪文件（P0-2）、文件权限过宽（P0-3）、.gitignore覆盖不全（P0-4）、memory-fortress-pro License自相矛盾（P0-5）、pan-file-commander-pro删除原作者署名（P0-6） |
| **平均** | - | **67.6/100** | **未达发布标准（≥80分）** |

### 8.2 P0/P1/P2问题统计

| 严重度 | 第1轮 | 第2轮 | 第3轮 | 第4轮 | 第5轮 | 去重后总数 |
|--------|-------|-------|-------|-------|-------|------------|
| P0 | 3 | 2 | 1 | 4 | 6 | **9个独立P0** |
| P1 | 1 | 2 | 2 | 2 | 5 | **9个独立P1** |
| P2 | - | - | - | - | 3 | **3个独立P2** |
| **合计** | **4** | **4** | **3** | **6** | **14** | **21个独立问题** |

### 8.3 重复问题清单（跨轮重复）

| 问题 | 出现轮次 | 是否修复 |
|------|----------|----------|
| skills表缺edition列 | 第1、4、5轮 | 未修复 |
| parent_slug缺失 | 第1、4轮 | 未修复 |
| 评分无持久化 | 第2、4轮 | 未修复 |
| 工作流无状态机 | 第2、4轮 | 未修复 |
| memory-fortress-pro内容重叠 | 第3、4轮 | 未修复 |
| 规范frontmatter缺edition | 第3轮 | 未修复 |
| **\b正则中文失效** | **第4、5轮** | **未修复，本轮验证修复方案** |
| **API Token硬编码** | **第1轮（v1）、第5轮** | **未修复，本轮发现仍在Git跟踪文件中** |
| **文件权限过宽** | **第1轮（v1）、第5轮** | **未修复** |

### 8.4 本轮新发现问题（第5轮独有）

| 编号 | 问题 | 严重度 |
|------|------|--------|
| P0-4 | .gitignore未覆盖含Token的文件和数据库 | P0 |
| P0-5 | memory-fortress-pro License章节自相矛盾 | P0 |
| P0-6 | pan-file-commander-pro明确删除原作者署名 | P0 |
| P1-1 | 4个改造SKILL.md均未保留实际原始版权声明 | P1 |
| P1-2 | doc-reasoning-analyst-pro对MIT-0描述误导 | P1 |
| P1-4 | pan-file-commander-pro路径遍历防护不充分 | P1 |
| P1-5 | infinite-memory-vault-pro记忆数据明文存储 | P1 |
| P2-2 | skill-registry.db无加密无认证 | P2 |
| P2-3 | allowlist中clawhub自身存在歧义 | P2 |

**本轮新发现共9个问题**（3个P0 + 4个P1 + 2个P2），主要集中在License合规和数据安全两个维度，是前四轮未覆盖的盲区。

### 8.5 五轮审核的关键启示

1. **\b正则漏洞是跨轮未修复的严重问题**：第4轮发现，第5轮验证，但v1.1仍未修复。这表明开发流程缺乏"安全发现→立即修复"的闭环机制。

2. **Token硬编码是历史遗留的顽固问题**：从v1审计到第5轮，Token始终硬编码在脚本中，且部分进入了Git历史。这表明缺乏"凭证管理"的工程实践。

3. **License合规是前四轮的盲区**：第5轮首次系统审核License，发现2个P0级违规（memory-fortress-pro自相矛盾、pan-file-commander-pro删除署名），表明前四轮的审核维度不够全面。

4. **"71个文件全部通过"的结论方法论有缺陷**：即使结论碰巧正确，检测机制本身的漏洞使结论可信度存疑。这表明需要"方法论审计"而非仅"结果审计"。

5. **平均67.6分远低于80分发布基线**：5轮审核均未达到80分，表明v1.1规范在多个维度存在系统性问题，需要重大修订而非局部修补。

---

## 九、优先修复建议（按修复难度和影响排序）

### 第一优先级（立即修复，阻断发布）

#### 1. 修复\b正则漏洞（P0-1）
- **修复难度**：低（仅需替换正则模式）
- **影响**：高（所有禁止词检测在中文上下文失效）
- **修复方案**：见第三节3.4，将所有`\b`替换为`(?<![A-Za-z0-9_])`和`(?![A-Za-z0-9_])`
- **验证**：运行第三节3.1的测试代码，13/13 PASS
- **预估工时**：1小时

#### 2. 从Git历史清除Token（P0-2）
- **修复难度**：中（需用`git filter-branch`或`BFG Repo-Cleaner`重写历史）
- **影响**：高（Token泄露风险）
- **修复方案**：
  ```powershell
  # 1. 使用BFG清除历史中的token
  bfg --replace-text passwords.txt
  git reflog expire --expire=now --all
  git gc --prune=now --aggressive
  # 2. 立即吊销并重新生成两个Token
  # 3. 将新Token存入加密的.skillhub-credentials/api-key.txt
  ```
- **预估工时**：2小时（含Token吊销和重新部署）

#### 3. 修复License违规（P0-5、P0-6）
- **修复难度**：中（需联系原作者或重新声明）
- **影响**：高（MIT License合规性）
- **修复方案**：
  - memory-fortress-pro：要么真正保留原作者署名，要么修改License章节声明
  - pan-file-commander-pro：恢复原作者署名，或在License章节明确"原始作品已进入公有领域/原作者已放弃署名"
- **预估工时**：3小时

#### 4. 收紧文件权限（P0-3）
- **修复难度**：低（PowerShell命令）
- **影响**：中（防止未授权访问）
- **修复方案**：
  ```powershell
  icacls "d:\skills\.skillhub-credentials" /inheritance:r /grant:r "$env:USERNAME:(F)"
  icacls "d:\skills\.skillhub-credentials\api-key.txt" /inheritance:r /grant:r "$env:USERNAME:(R)"
  icacls "d:\skills\skill-registry.db" /inheritance:r /grant:r "$env:USERNAME:(F)"
  ```
- **预估工时**：30分钟

#### 5. 完善.gitignore（P0-4）
- **修复难度**：低（添加几行）
- **影响**：中（防止误提交）
- **修复方案**：
  ```gitignore
  # 追加到现有.gitignore
  PROJECT_MEMORY.md
  retry-skillhub*.ps1
  upload-differentiated.ps1
  upload-to-skillhub.ps1
  skill-registry.db
  skill-registry/
  ```
- **预估工时**：15分钟

### 第二优先级（下一版本修复）

#### 6. 补充实际原始版权声明（P1-1）
- **修复难度**：中（需查找原作者信息）
- **影响**：中（MIT合规性）
- **修复方案**：在4个SKILL.md的License章节添加"原始版权：© [year] [author name]"
- **预估工时**：2小时

#### 7. 修正MIT-0描述（P1-2）
- **修复难度**：低（修改文案）
- **影响**：低（避免误导）
- **修复方案**：改为"MIT-0（放弃署名要求，保留责任免责条款；可与MIT兼容）"
- **预估工时**：15分钟

#### 8. 补充路径遍历防护说明（P1-4）
- **修复难度**：低（添加安全约束章节）
- **影响**：低（防御性）
- **修复方案**：在pan-file-commander-pro的SKILL.md中明确禁止`../`前缀
- **预估工时**：30分钟

#### 9. 补充记忆数据安全警告（P1-5）
- **修复难度**：低（添加警告章节）
- **影响**：低（防御性）
- **修复方案**：在infinite-memory-vault-pro的SKILL.md中添加"记忆目录禁止同步到云端"警告
- **预估工时**：30分钟

### 第三优先级（长期优化）

#### 10. 修复数据库schema（P2-1）
- 添加edition和parent_slug列到skills表
- 预估工时：2小时

#### 11. 评估数据库加密（P2-2）
- 评估SQLCipher加密的必要性
- 预估工时：4小时（含评估和实施）

#### 12. 完善allowlist说明（P2-3）
- 在规范中明确"标准文档自身引用禁止词属于豁免"
- 预估工时：30分钟

---

## 十、审核结论

### 10.1 总体判断

**v1.1规范在安全合规维度尚未达到可发布标准。**

本轮审核评分63/100，低于80分发布基线。主要问题集中在三个维度：

1. **安全漏洞未修复**：第4轮发现的\b正则漏洞完全未修复，且经本轮验证影响范围比预期更大（常规修复方案也失效）。Token硬编码问题从v1审计延续至今未解决，且部分Token已进入Git历史。

2. **License合规违规**：本轮首次系统审核License，发现2个P0级违规（memory-fortress-pro自相矛盾、pan-file-commander-pro明确删除原作者署名），4个文件均未保留实际原始版权声明。这是前四轮审核的盲区。

3. **数据安全防护不足**：.gitignore覆盖不全、文件权限过宽、Token明文存储、Git历史泄露风险等问题叠加。

### 10.2 发布建议

**建议：暂缓发布v1.1，先完成第一优先级的5项修复（预估工时6.75小时）。**

修复完成后，需重新运行：
1. 修复版正则的check_debranding.py对71个文件复检
2. `git log --all -p | grep -E "skh_|clh_"`确认Git历史无Token残留
3. License合规复检（4个SKILL.md）
4. 文件权限复检

复检全部通过后，方可发布v1.2（含安全修复的版本）。

### 10.3 五轮审核的最终启示

五轮审核累计发现21个独立问题（9个P0 + 9个P1 + 3个P2），平均评分67.6分。这表明：

1. **多角色审核是必要的**：每个角色发现的问题不同，QA发现schema问题、架构师发现持久化问题、PM发现产品问题、开发者发现代码漏洞、安全合规专家发现License和数据安全问题。单一角色审核会遗漏大量问题。

2. **重复问题未修复是流程问题**：多个P0问题在多轮审核中重复出现（\b正则、Token硬编码、文件权限），表明开发流程缺乏"审核发现→立即修复→复检确认"的闭环。

3. **v1.1需要重大修订**：局部修补无法解决系统性问题。建议基于5轮审核的21个发现，重新规划v1.2版本，重点解决安全合规、License合规、数据安全三个维度的问题。

---

**审核人**：资深安全合规专家
**审核完成时间**：2026-07-18
**报告版本**：v2（第5轮终审）
**下一步**：将本报告提交至开发团队，按第九节优先级修复，修复后重新审核
