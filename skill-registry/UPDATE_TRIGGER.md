# Skill 自动更新触发机制

> **触发词**: "更新"
> **创建时间**: 2026-07-20
> **位置**: `d:\skills\skill-registry\UPDATE_TRIGGER.md`

---

## 触发规则

当用户输入 **"更新"**（精确匹配或包含该词）时，立即启动本文件定义的更新流水线。
无需用户额外确认，直接执行全流程，完成后汇报结果。

---

## 执行流程（6阶段）

### 阶段1: 来源检测 (Source Check)

**目标**: 对每个 skill 检测其原始来源是否有更新

**命令**:
```bash
cd d:\skills\skill-registry
python update_mechanism.py check
```

**输出**: `d:\skills\skill-registry\update-report.json`

**处理逻辑**:
- 读取 `skill-registry.db` 中所有有 `source_slug` 的 skill
- 对 clawhub 来源: 查找本地 `clawhub-skills/downloaded/` 目录中的原始文件
- 对 github 来源: 通过 `raw.githubusercontent.com` 拉取最新内容
- 对原创 skill: 标记为 `no_source`，跳过来源检测
- SHA256 比对: 新内容 hash vs DB 中记录的 `last_hash`

**判断标准**:
| 状态 | 含义 | 后续动作 |
|------|------|---------|
| `changed` | 来源内容已变更 | 进入阶段2分析 |
| `up_to_date` | 来源无变化 | 跳过 |
| `no_source` | 原创skill无外部来源 | 跳过 |
| `fetch_failed` | 无法获取来源内容 | 记录错误，跳过 |
| `no_baseline` | DB中无历史hash | 记录hash作为基线 |

---

### 阶段2: 变更分析 (Change Analysis)

**目标**: 对每个 `changed` 状态的 skill，分析变更内容

**AI操作**（此阶段由AI执行，非脚本）:

1. 读取 `update-report.json` 中 `changed` 列表
2. 对每个已变更的 skill:
   a. 读取当前本地 SKILL.md: `find_skill_md(slug)` 返回的路径
   b. 读取来源原始 SKILL.md: `find_source_skill_md` 返回的路径
   c. 对比两个版本的差异
   d. 分析变更类型:
      - **功能新增**: 原始skill新增了功能模块
      - **Bug修复**: 修复了已知问题
      - **破坏性变更**: API/接口变更，需适配
      - **文档优化**: 仅文档/说明更新
      - **性能优化**: 算法/逻辑优化
   e. 评估差异化改造是否需要更新:
      - 如果原始新增了功能 → 需要在差异化版本中同步增强
      - 如果原始修复了Bug → 需要在差异化版本中同步修复
      - 如果仅文档更新 → 可选同步

**输出**: 对每个变更 skill 生成分析结论

---

### 阶段3: 本地升级 (Local Update)

**目标**: 更新本地 SKILL.md 文件

**AI操作**:

1. 对每个需要更新的 skill:
   a. 基于变更分析，重新应用差异化改造:
      - 保持去标识化（不出现原始仓库名/作者名）
      - 保持差异化增强（新增的功能/优化）
      - 同步原始的关键修复
   b. 递增版本号:
      - Bug修复/文档优化 → patch 版本+1 (1.0.0 → 1.0.1)
      - 功能新增 → minor 版本+1 (1.0.0 → 1.1.0)
      - 破坏性变更 → major 版本+1 (1.0.0 → 2.0.0)
   c. 更新 SKILL.md 的 frontmatter `version` 字段
   d. 在 SKILL.md 末尾的「变更历史」表格添加新行
   e. 保存文件到原始路径

2. 更新数据库:
   ```bash
   python update_mechanism.py update-db --slug <slug> --version <new_version> --changelog "<说明>"
   ```
   或通过 AI 直接操作 SQLite DB:
   - 更新 `skills.current_version`
   - 插入 `versions` 记录（新 hash, version, changelog）
   - 插入 `operations` 记录（operation_type='auto_update'）

---

### 阶段4: 双版本生成 (Dual Edition Generation)

**目标**: 为每个更新的 skill 生成免费版和付费版 payload

**命令**:
```bash
# 单个生成
python update_mechanism.py generate <slug> --version <new_version> --changelog "<说明>"

# 或在 upload-all 中自动生成
```

**生成规则**:
| 版本 | 特征 | 上传方式 | 定价字段 |
|------|------|---------|---------|
| 免费版 | 完整功能，无定价 | CLI publish | 无 `pricing` 字段 |
| 付费版 | 完整功能，含定价 | 企业API | `pricing.billingType: "per_call"`, `pricePerCall: "9.90"` |

**文件输出**:
- 免费版: `c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\payloads\{slug}-free.json`
- 付费版: `c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5\payloads\{slug}-paid.json`

**定价策略**（参照 INDEX.md）:
- 冲奖款（5个）: 仅免费版，无付费版
- 获奖款（3个）: 仅免费版，无付费版
- 赚款项（12个）: 免费版 + 付费版，定价按 INDEX.md 指定
- 开源改造款（25个）: 免费版 + 付费版，统一 9.9元/次

---

### 阶段5: 平台同步 (Platform Sync)

**目标**: 将更新后的 skill 上传到 SkillHub 平台

**命令**:
```bash
# 上传所有已变更 skill
python update_mechanism.py upload-all

# 或上传单个
python update_mechanism.py upload <slug> --version <new_version>
```

**上传机制**:

#### 免费版上传（CLI方式）
```bash
bash d:\skills\run-skillhub.sh publish <skill_dir>
```
- 使用个人账号 `skh_` token
- 通过 `skillhub publish` CLI 命令
- 输出捕获到 `d:\skills\.skillhub-credentials\last-output.txt`

#### 付费版上传（企业API方式）
- 需要浏览器 session cookies 认证
- API: `POST https://api.skillhub.cn/api/v1/orgs/862/skills/{slug}/versions`
- FormData: `payload` 字段 = JSON字符串（不是Blob）
- pricing 结构:
  ```json
  {
    "billingType": "per_call",
    "pricingMode": "unified",
    "pricePerCall": "9.90",
    "currency": "CNY"
  }
  ```
- 通过浏览器 MCP `browser_evaluate` 执行 fetch 请求
- **注意**: 避免通过 MCP 传 base64 内容（会导致乱码），使用本地 HTTP 服务器中转

#### HTTP服务器中转（防乱码）
如果本地 HTTP 服务器（端口 18765）未运行，先启动:
```bash
cd c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5
python start_dual_server.py
```
然后通过 `fetch('http://localhost:18765/payloads/{slug}-paid.json')` 获取 payload

---

### 阶段6: 结果汇报 (Report)

**目标**: 汇总更新结果，向用户报告

**AI操作**:

1. 汇总每个 skill 的处理结果:
   - 来源检测状态
   - 变更分析结论
   - 本地更新结果
   - 平台上传状态

2. 生成可视化报告:
   - 使用 `PureShowWidget` 展示更新汇总
   - 表格列出: skill名称 | 来源状态 | 变更类型 | 新版本 | 免费上传 | 付费上传

3. 更新数据库:
   ```bash
   python update_mechanism.py status  # 确认最终状态
   ```

---

## 完整一键执行

如果用户输入"更新"且没有其他限定条件，执行以下完整流程:

```bash
# 步骤1: 检查来源
cd d:\skills\skill-registry
python update_mechanism.py check

# 步骤2: AI读取报告，分析变更，更新本地文件
# (AI执行，非命令行)

# 步骤3: 生成双版本 + 上传
python update_mechanism.py upload-all

# 步骤4: 生成状态报告
python update_mechanism.py status
```

---

## 边界情况处理

### 1. 数据库未初始化
```bash
cd d:\skills\skill-registry
python db.py  # 初始化数据库
python scan_and_import.py  # 扫描导入所有skill
```

### 2. 本地HTTP服务器未运行
```bash
cd c:\Users\thcd\.trae-cn\work\6a5cf90c2aab822b9b427eb5
python start_dual_server.py &
```

### 3. SkillHub CLI未认证
```bash
skillhub login  # 交互式登录
# 或使用 token
skillhub auth --token skh_xxxxx
```

### 4. 企业API认证过期
- 需要通过浏览器访问 `https://skillhub.cn` 并登录企业账号
- session cookies 会自动刷新
- 如果 401 错误，提示用户重新登录

### 5. 无变更时的处理
- 如果 `check` 结果显示 0 个变更，直接报告"所有skill均为最新版本"
- 不执行后续阶段

---

## 文件清单

| 文件 | 路径 | 作用 |
|------|------|------|
| 主控脚本 | `d:\skills\skill-registry\update_mechanism.py` | 6阶段流水线主入口 |
| 触发指令 | `d:\skills\skill-registry\UPDATE_TRIGGER.md` | AI执行手册（本文件）|
| 数据库 | `d:\skills\skill-registry.db` | SQLite，追踪所有skill状态 |
| 数据库模块 | `d:\skills\skill-registry\db.py` | 数据库操作封装 |
| 扫描导入 | `d:\skills\skill-registry\scan_and_import.py` | 初始扫描导入 |
| 检查报告 | `d:\skills\skill-registry\update-report.json` | 来源检测结果 |
| 上传结果 | `d:\skills\skill-registry\upload-results.json` | 平台上传结果 |
| Payload目录 | `c:\Users\thcd\.trae-cn\work\...\payloads\` | 生成的上传payload |
| HTTP服务器 | `c:\Users\thcd\.trae-cn\work\...\start_dual_server.py` | 防乱码中转服务器 |
| CLI运行器 | `d:\skills\run-skillhub.sh` | skillhub CLI封装 |

---

## 定价配置

| Skill类型 | 免费版 | 付费版 | 付费价格 |
|-----------|--------|--------|---------|
| 冲奖款(5个) | 有 | 无 | - |
| 获奖款(3个) | 有 | 无 | - |
| 赚款项-9.9/次(4个) | 有 | 有 | 9.90 CNY |
| 赚款项-9.9/月(3个) | 有 | 有 | 9.90 CNY/月 |
| 赚款项-19.9(3个) | 有 | 有 | 19.90 CNY |
| 赚款项-29.9(2个) | 有 | 有 | 29.90 CNY |
| 赚款项-39.9/49.9(2个) | 有 | 有 | 39.90/49.90 CNY |
| 开源改造款(25个) | 有 | 有 | 9.90 CNY |

> 当前实际已上传的12个skill统一使用9.9元/次，后续上传按INDEX.md定价

---

## 更新日志

| 日期 | 变更 |
|------|------|
| 2026-07-20 | 初版创建，6阶段流水线，支持clawhub/github/原创三种来源检测 |
