---
slug: code-review-sentinel
name: code-review-sentinel
version: 1.0.1
displayName: 代码审查哨兵
summary: 合并前五维度质量审查,以高级工程师标准把关每次代码提交
license: Proprietary
description: 代码审查哨兵——在代码合并前执行五维度质量审查，以"高级工程师是否会批准"为标准把关每次提交。适用于PR审查、变更评估、质量门禁、代码健康度审计、新人指导等场景。正确性/可维护性/安全性/性能/可测试性全面覆盖，支持严重度标签与拆分策略，让代码腐化止于合并前。触发关键词：代码审查、代码review、合并前审查、代码质量、PR审查、五维审查、代码健康度、变更尺寸、代码拆分、质量门禁
tags:
- 代码审查
- 质量门禁
- 代码质量
- PR审查
- 工程规范
tools:
- read
- exec
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "write", "exec", "glob", "grep"]
tags: "开发工具,代码生成,编程辅助"
---
# 代码审查哨兵

在代码合并前执行结构化质量审查。以"高级工程师是否会批准这次合并"为标准，从五个维度全面把关。

## 核心能力

- **变更概览与尺寸评估**：`git diff` 获取变更 + 统计规模 + 尺寸分级（理想 ~100 行/可接受 100-300/需拆分 >300）+ 变更分类
- **五维度审查**：正确性（逻辑/边界/错误处理/回归）+ 可维护性（命名/职责/重复/复杂度）+ 安全性（注入/权限/密钥/依赖）+ 性能（计算/查询/内存/阻塞）+ 可测试性（覆盖/路径/可 mock）
- **严重度标签体系**：Blocking（阻塞）/ Should Fix（建议修复）/ Nit（小问题）/ Optional（可选）/ FYI（参考）/ Praise（表扬）
- **拆分策略**：按功能/按层/按文件拆分 + 先重构后功能 + 确保子 PR 独立可编译可测试
- **审查报告输出**：总体评估 + 五维度评分（0-10）+ 问题清单 + 改进建议 + 亮点表扬

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| PR 审查 | PR diff + 上下文 | 五维度审查报告 + 问题清单 + Approve/Request Changes |
| 变更评估 | 代码变更量 + 文件清单 | 尺寸评估 + 拆分建议 + 审查优先级 |
| 质量门禁 | CI/CD 触发的 diff | 自动化质量检查 + Blocking 问题拦截 |
| 代码健康度 | 代码库全量/抽样 | 健康度评分 + 趋势分析 + 改进建议 |
| 新人指导 | 新成员提交的 PR | 建设性反馈 + 学习建议 + 亮点表扬 |

**不适用于**：
- 自动化静态分析（用 ESLint/SonarQube/Snyk 等工具）
- 安全渗透测试（属专业安全审计）
- 性能基准测试（属性能测试工具，如 JMeter/k6）
- 代码风格格式化（用 Prettier/Black 等工具自动处理）

## 使用流程

### Step 1: 获取变更概览
- 执行 `git diff` 或读取 PR diff
- 统计变更规模：新增行数 / 删除行数 / 涉及文件数
- 变更尺寸评估：
  - 理想：~100 行（易审查、易回滚）
  - 可接受：100-300 行（需分段审查）
  - 需拆分：> 300 行（建议拆分为多个 PR）
- 变更分类：新功能 / Bug 修复 / 重构 / 配置 / 文档

### Step 2: 五维度审查

#### 维度一：正确性
- 逻辑是否正确实现需求
- 边界条件是否处理（空值/零值/极值/并发）
- 错误处理是否完整（异常捕获/错误传播/降级）
- 是否引入回归

#### 维度二：可维护性
- 命名是否清晰表达意图
- 函数/类职责是否单一
- 是否存在重复代码（应抽象）
- 复杂度是否可控（圈复杂度 < 10）
- 注释是否解释"为什么"而非"是什么"

#### 维度三：安全性
- 输入是否校验（防注入/XSS）
- 权限检查是否到位
- 密钥/凭证是否泄露
- 依赖是否有已知漏洞
- 是否遵循最小权限原则

#### 维度四：性能
- 是否有不必要的计算/查询
- N+1 查询问题
- 内存泄漏风险
- 大数据集处理是否分页/流式
- 是否阻塞主线程/事件循环

#### 维度五：可测试性
- 是否有对应的测试
- 测试是否覆盖关键路径
- 是否易于编写测试（依赖注入/可 mock）
- 测试是否快速且稳定

### Step 3: 标注严重度
- **Blocking**：必须修复才能合并（安全漏洞/逻辑错误/数据丢失风险）
- **Should Fix**：强烈建议修复（性能问题/边界缺失/可维护性差）
- **Nit**：吹毛求疵的小问题（命名偏好/格式微调）
- **Optional**：可选的改进建议（重构建议/优化方向）
- **FYI**：仅供参考的信息（相关知识/未来注意）
- **Praise**：值得表扬的写法（优秀设计/清晰注释）

### Step 4: 拆分策略（当变更过大时）
- 按功能拆分：一个 PR 一个功能点
- 按层拆分：数据层/业务层/接口层分开
- 按文件拆分：独立文件变更独立 PR
- 先重构后功能：重构 PR 先合并，再提功能 PR
- 拆分顺序：确保每个子 PR 独立可编译可测试

### Step 5: 输出审查报告
- 总体评估：Approve / Request Changes / Needs Discussion
- 五维度评分：每维度 0-10 分
- 问题清单：按严重度排序
- 改进建议：具体可执行的修改建议
- 亮点表扬：值得学习的优秀写法

## 示例

### 示例 1：用户注册功能 PR 审查

**输入**：
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | 代码审查哨兵处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
PR: 添加用户注册功能
变更：+180 行 / -5 行 / 3 文件
文件：
  - src/auth/register.ts (新增注册逻辑)
  - src/api/routes.ts (添加 POST /register 路由)
  - src/db/users.ts (添加 createUser 方法)
```

**输出**：
```markdown
# 代码审查报告：用户注册功能
# ...
## 总体评估：Request Changes
- 变更尺寸：180 行（可接受）
- 五维度评分：正确性 7/10 | 可维护性 8/10 | 安全性 4/10 | 性能 7/10 | 可测试性 3/10
# ...
## 问题清单（按严重度排序）
# ...
### Blocking（必须修复）
# ...
**[B1] 密码明文存储**
- 文件：`src/db/users.ts:15`
- 问题：`createUser` 直接将密码存入数据库，未哈希
- 风险：数据库泄露后所有密码暴露
- 建议：使用 argon2 哈希后再存储
```typescript
import argon2 from 'argon2';
const hashedPassword = await argon2.hash(password);
// 存储 hashedPassword 而非 password
```
# ...
**[B2] 缺少输入校验**
- 文件：`src/auth/register.ts:8`
- 问题：未校验 email 格式和 password 强度
- 风险：脏数据入库 + 弱密码风险
- 建议：使用 zod/joi 校验
```typescript
const schema = z.object({
  email: z.string().email(),
  password: z.string().min(8).regex(/[A-Z]/).regex(/[0-9]/),
});
```
# ...
### Should Fix（强烈建议修复）
# ...
**[S1] 缺少速率限制**
- 文件：`src/api/routes.ts:45`
- 问题：注册接口无速率限制，可被暴力注册
- 建议：添加 IP 级速率限制（5 次/15 分钟）
# ...
**[S2] 缺少单元测试**
- 文件：无
- 问题：注册逻辑无测试覆盖
- 建议：补充测试用例（正常注册/重复邮箱/弱密码/无效邮箱）
# ...
### Praise（值得表扬）
# ...
**[P1] 错误处理清晰**
- 文件：`src/auth/register.ts:25`
- 表扬：错误分类明确（VALIDATION_FAILED/EMAIL_EXISTS），包含 requestId，便于排查
```

### 示例 2：大 PR 拆分建议

**输入**：
```
PR: 重构用户模块 + 添加 OAuth 登录 + 修改数据库 Schema
变更：+850 行 / -320 行 / 18 文件
```

**输出**：
```markdown
# 拆分建议
# ...
## 评估
- 变更尺寸：850 行（需拆分）
- 涉及多个独立功能，建议拆分为 4 个 PR
# ...
## 拆分方案
# ...
### PR 1: 数据库 Schema 变更（独立先合并）
- 文件：`src/db/schema.ts`, `migrations/001_users_oauth.sql`
- 行数：~80 行
- 说明：纯 Schema 变更，向后兼容（新增字段），可独立合并
# ...
### PR 2: 重构用户模块（依赖 PR 1）
- 文件：`src/db/users.ts`, `src/auth/user-service.ts`
- 行数：~250 行
- 说明：提取 UserService，为 OAuth 做准备，无功能变更
# ...
### PR 3: OAuth 登录功能（依赖 PR 2）
- 文件：`src/auth/oauth.ts`, `src/api/routes.ts`
- 行数：~300 行
- 说明：核心功能 PR，添加 Google/GitHub OAuth
# ...
### PR 4: 测试与文档（依赖 PR 3）
- 文件：`tests/auth.test.ts`, `docs/oauth.md`
- 行数：~220 行
- 说明：补充测试用例与 OAuth 接入文档
# ...
## 合并顺序
PR 1 → PR 2 → PR 3 → PR 4
每个 PR 独立可编译可测试，降低审查难度与回滚风险。
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 无法获取 diff | git 命令失败或 PR 不存在 | 检查 git 仓库状态 + 确认 PR 编号 + 提供文件路径手动审查 |
| 变更过大 | > 1000 行单 PR | 建议拆分 + 提供拆分方案 + 优先审查 Blocking 问题 |
| 跨语言审查 | 多语言混合 PR | 按语言分组审查 + 标注语言特定问题 |
| 缺少上下文 | 无需求文档或关联 issue | 标注"假设" + 请求补充上下文 + 基于代码本身审查 |
| 误报问题 | LLM 理解偏差 | 标注"需人工确认" + 提供依据 + 允许作者解释 |
| 审查超时 | 大型 PR 审查耗时 | 分段审查 + 优先 Blocking + 异步输出报告 |

## 依赖说明

### 运行环境
- **Agent 平台**：Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持 SKILL.md 的任意 Agent
- **操作系统**：Windows / macOS / Linux
- **运行时**：需要 Agent 支持 exec（命令行执行）能力（执行 git diff）

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| Git | 工具 | 必需 | `git` 命令行（获取变更差异） |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供代码分析 |
| 静态分析工具 | 工具 | 可选 | ESLint/SonarQube/Snyk（补充自动化检查） |

### API Key 配置
- 本 Skill 无需额外 API Key 配置
- 代码审查由 Agent LLM 完成，API Key 由 Agent 平台托管
- 若集成 GitHub/GitLab API（可选），Token 通过环境变量注入，Skill 内零硬编码

### 可用性分类
- **分类**：MD + EXEC
- **说明**：纯 Markdown 方法论，需要 exec 能力执行 git diff 获取变更，审查本身由 Agent LLM 完成

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 支付服务PR审查

**输入**:
```
PR: 重构支付服务，从同步调用改为异步事件驱动
变更: +320行 / -180行 / 8文件
关键文件:
  - src/payment/service.ts (核心逻辑重构)
  - src/payment/event publisher.ts (新增事件发布)
  - src/api/routes.ts (API端点修改)
```

**LLM生成输出**:
```markdown
# 代码审查报告：支付服务异步化重构
# ...
## 总体评估: Request Changes
- 变更尺寸: 320行（需拆分）
- 五维度评分: 正确性 6/10 | 可维护性 7/10 | 安全性 8/10 | 性能 5/10 | 可测试性 4/10
# ...
## 问题清单（按严重度排序）(续1)
# ...
### Blocking（必须修复）(补充)
# ...
**[B1] 支付事件幂等性缺失**
- 文件: src/payment/event_publisher.ts:42
- 问题: 事件发布无幂等键，网络重试可能导致重复扣款
- 风险: 资金损失，客户投诉
- 建议: 使用Idempotency-Key，消费端去重
```typescript
// 修复方案
async function publishPaymentEvent(payment: Payment) {
  const idempotencyKey = `pay_${payment.id}_${payment.version}`;
  await eventBus.publish('payment.completed', {
    paymentId: payment.id,
    amount: payment.amount,
  }, {
    idempotencyKey,  // 幂等键
    headers: { 'x-idempotency-key': idempotencyKey }
  });
}
```
# ...
**[B2] 异步异常未补偿**
- 文件: src/payment/service.ts:78
- 问题: 支付成功后发布事件失败，未回滚支付
- 风险: 客户已扣款但订单未更新
- 建议: 实现Saga补偿事务或本地事务表
```typescript
// 修复方案: 本地事务表模式
async function processPayment(orderId: string) {
  await db.transaction(async (tx) => {
    // 1. 扣款（同事务）
    await tx.payments.deduct(orderId);
    // 2. 写入事件表（同事务，保证原子性）
    await tx.outbox.insert({
      event: 'payment.completed',
      payload: { orderId },
      status: 'pending'
    });
  });
  // 3. 异步推送事件（失败重试不影响扣款）
  await eventPublisher.flush();
}
```
# ...
### Should Fix（强烈建议修复）(补充)
# ...
**[S1] N+1查询问题**
- 文件: src/payment/service.ts:120
- 问题: 循环中查询用户信息，100笔支付触发100次DB查询
- 建议: 批量查询用户信息
```typescript
// 优化前: N+1查询
for (const payment of payments) {
  const user = await db.users.findById(payment.userId); // N次查询
  // ...
}

// 优化后: 批量查询
const userIds = [...new Set(payments.map(p => p.userId))];
const users = await db.users.findByIds(userIds); // 1次查询
const userMap = new Map(users.map(u => [u.id, u]));
for (const payment of payments) {
  const user = userMap.get(payment.userId);
  // ...
}
```
# ...
**[S2] 缺少并发控制**
- 文件: src/payment/service.ts:55
- 问题: 同一订单可能并发处理，导致重复扣款
- 建议: 使用乐观锁或分布式锁
```typescript
// 修复方案: 乐观锁
const result = await db.payments.update(
  { id: paymentId, version: payment.version },  // WHERE version = ?
  { status: 'completed', version: payment.version + 1 }
);
if (result.affected === 0) {
  throw new ConcurrencyError('Payment already processed');
}
```
# ...
### Nit（小问题）
# ...
**[N1] 命名不清晰**
- 文件: src/payment/service.ts:15
- 问题: `proc` 函数名缩写过度，应为 `processPayment`
- 建议: 使用完整动词+名词命名
# ...
### Praise（值得表扬）(补充)
# ...
**[P1] 事件版本化设计**
- 文件: src/payment/event_publisher.ts:8
- 表扬: 事件schema包含version字段，为后续演化预留空间，是优秀的实践
```

**效果验证**: ✓五维度评分完整 ✓2个Blocking问题含修复代码 ✓Should Fix含N+1查询优化 ✓Saga补偿事务方案 ✓Praise表扬优秀实践

### 案例2: 安全漏洞审查

**输入**:
```
PR: 添加文件上传功能
变更: +85行 / 4文件
关键代码片段:
```typescript
// src/upload/handler.ts
app.post('/upload', async (req, res) => {
  const file = req.files.file;
  const filePath = `/uploads/${file.name}`;
  await file.mv(filePath);
  const url = await db.query(
    `SELECT * FROM files WHERE name = '${file.name}'`
  );
  res.json({ url: filePath });
});
```
```

**LLM生成输出**:
```markdown
# 代码审查报告：文件上传功能
# ...
## 总体评估: Request Changes（安全审查严重不通过）
- 变更尺寸: 85行（理想）
- 五维度评分: 正确性 5/10 | 可维护性 6/10 | 安全性 1/10 | 性能 7/10 | 可测试性 3/10
# ...
## 问题清单
# ...
# ...
**[B1] SQL注入漏洞（严重）**
- 文件: src/upload/handler.ts:7
- 问题: 直接拼接SQL，攻击者可通过文件名注入
- 攻击示例: 文件名 `'; DROP TABLE files; --`
- 建议: 使用参数化查询
```typescript
// 修复方案
const url = await db.query(
  'SELECT * FROM files WHERE name = $1',
  [file.name]  // 参数化
);
// 或使用ORM
const url = await db.files.findFirst({ where: { name: file.name } });
```
# ...
**[B2] 路径遍历漏洞（严重）**
- 文件: src/upload/handler.ts:4
- 问题: 未过滤文件名，攻击者可上传 `../../../etc/passwd`
- 建议: 生成随机文件名，过滤特殊字符
```typescript
import path from 'path';
import crypto from 'crypto';

// 修复方案
const ext = path.extname(file.name).toLowerCase();
const safeExt = ['.jpg', '.png', '.pdf'].includes(ext) ? ext : '';
if (!safeExt) {
  return res.status(400).json({ error: 'INVALID_TYPE' });
}
const safeName = crypto.randomUUID() + safeExt;
const filePath = path.join('/uploads', safeName);

// 二次校验: 确保最终路径在uploads目录内
const resolved = path.resolve(filePath);
if (!resolved.startsWith(path.resolve('/uploads'))) {
  return res.status(400).json({ error: 'INVALID_PATH' });
}
```
# ...
**[B3] 无文件类型校验**
- 文件: src/upload/handler.ts:3
- 问题: 接受任意文件类型，可上传可执行文件
- 建议: 白名单校验MIME类型和扩展名
```typescript
const allowedTypes = ['image/jpeg', 'image/png', 'application/pdf'];
if (!allowedTypes.includes(file.mimetype)) {
  return res.status(400).json({ error: 'INVALID_TYPE' });
}
// 注意: mimetype可伪造，需校验文件头
const fileHeader = await readFile(file.tempFilePath, { length: 4 });
const isRealImage = await verifyImageHeader(fileHeader);
if (!isRealImage) {
  return res.status(400).json({ error: 'FILE_CORRUPTED' });
}
```
# ...
**[B4] 无文件大小限制**
- 文件: src/upload/handler.ts:2
- 问题: 无大小限制，可上传超大文件耗尽磁盘
- 建议: 限制文件大小
```typescript
// 修复方案
const MAX_SIZE = 10 * 1024 * 1024;  // 10MB
if (file.size > MAX_SIZE) {
  return res.status(413).json({ error: 'FILE_TOO_LARGE' });
}
```
# ...
**[B5] 上传文件可公开访问**
- 文件: src/upload/handler.ts:5
- 问题: 文件存储在web可访问目录，可能泄露敏感文件
- 建议: 存储在非web目录，通过API鉴权访问
```typescript
// 修复方案
const filePath = path.join('/data/uploads', safeName);  // 非web目录
// 通过API提供受控访问
app.get('/files/:id', authMiddleware, async (req, res) => {
  const file = await db.files.findById(req.params.id);
  if (file.userId !== req.user.id) {
    return res.status(403).json({ error: 'FORBIDDEN' });
  }
  res.sendFile(file.path);
});
```
```

**效果验证**: ✓5个Blocking安全漏洞识别 ✓SQL注入攻击示例 ✓路径遍历攻击防护 ✓文件头校验防伪造 ✓受控访问替代公开目录

### 案例3: 性能问题审查

**输入**:
```
PR: 添加用户活动时间线API
变更: +120行 / 2文件
关键代码:
```typescript
// src/api/timeline.ts
app.get('/timeline/:userId', async (req, res) => {
  const userId = req.params.userId;
  const activities = await db.query(
    `SELECT * FROM activities WHERE user_id = ${userId} ORDER BY created_at DESC`
  );
  
  const enriched = [];
  for (const activity of activities) {
    const user = await db.query(`SELECT * FROM users WHERE id = ${activity.user_id}`);
    const post = activity.post_id ? 
      await db.query(`SELECT * FROM posts WHERE id = ${activity.post_id}`) : null;
    const comment = activity.comment_id ?
      await db.query(`SELECT * FROM comments WHERE id = ${activity.comment_id}`) : null;
    enriched.push({ ...activity, user, post, comment });
  }
  
  res.json(enriched);
});
```
```

**LLM生成输出**:
```markdown
# 代码审查报告：用户活动时间线API
# ...
## 总体评估: Request Changes(续1)
- 变更尺寸: 120行（理想）
- 五维度评分: 正确性 7/10 | 可维护性 6/10 | 安全性 3/10 | 性能 2/10 | 可测试性 4/10
# ...
## 问题清单(续1)
# ...
# ...
**[B1] SQL注入漏洞**
- 文件: src/api/timeline.ts:3
- 问题: `userId`直接拼接SQL
- 建议: 参数化查询
# ...
# ...
**[S1] 严重N+1查询问题（性能）**
- 文件: src/api/timeline.ts:8-12
- 问题: 每条活动查询user/post/comment，100条活动=300+次DB查询
- 影响: 100条活动API响应时间预计5-10秒
- 建议: 批量查询 + JOIN
```typescript
// 修复方案1: JOIN查询（推荐）
app.get('/timeline/:userId', async (req, res) => {
  const userId = req.params.userId;
  const enriched = await db.query(`
    SELECT 
      a.*,
      json_build_object('id', u.id, 'name', u.name, 'avatar', u.avatar) as user,
      p.id as post_id, p.title as post_title, p.content as post_content,
      c.id as comment_id, c.content as comment_content
    FROM activities a
    LEFT JOIN users u ON a.user_id = u.id
    LEFT JOIN posts p ON a.post_id = p.id
    LEFT JOIN comments c ON a.comment_id = c.id
    WHERE a.user_id = $1
    ORDER BY a.created_at DESC
    LIMIT 50 OFFSET $2
  `, [userId, offset]);
  res.json(enriched);
});

// 修复方案2: 批量查询
const activities = await db.query(
  'SELECT * FROM activities WHERE user_id = $1 ORDER BY created_at DESC LIMIT 50',
  [userId]
);
const userIds = [...new Set(activities.map(a => a.user_id))];
const postIds = activities.filter(a => a.post_id).map(a => a.post_id);
const commentIds = activities.filter(a => a.comment_id).map(a => a.comment_id);

const [users, posts, comments] = await Promise.all([
  db.query('SELECT * FROM users WHERE id = ANY($1)', [userIds]),
  postIds.length ? db.query('SELECT * FROM posts WHERE id = ANY($1)', [postIds]) : [],
  commentIds.length ? db.query('SELECT * FROM comments WHERE id = ANY($1)', [commentIds]) : [],
]);
// 内存中关联
```
# ...
**[S2] 无分页限制**
- 文件: src/api/timeline.ts:3
- 问题: 查询所有活动，活跃用户可能上万条
- 建议: 强制分页，默认50条
```typescript
const limit = Math.min(parseInt(req.query.limit) || 50, 100);
const offset = parseInt(req.query.offset) || 0;
```
# ...
**[S3] 无缓存策略**
- 文件: src/api/timeline.ts:2
- 问题: 时间线是高频访问接口，无缓存导致DB压力
- 建议: Redis缓存 + 短TTL
```typescript
import Redis from 'ioredis';
const redis = new Redis();

app.get('/timeline/:userId', cacheMiddleware, async (req, res) => {
  const cacheKey = `timeline:${req.params.userId}:${req.query.offset}`;
  const cached = await redis.get(cacheKey);
  if (cached) return res.json(JSON.parse(cached));
  
  const data = await fetchTimeline(req.params.userId, req.query.offset);
  await redis.setex(cacheKey, 60, JSON.stringify(data));  // 60秒TTL
  res.json(data);
});
```
# ...
**[S4] 无索引提示**
- 文件: src/api/timeline.ts:3
- 问题: ORDER BY created_at可能全表扫描
- 建议: 确保有(user_id, created_at DESC)复合索引
```sql
CREATE INDEX idx_activities_user_time ON activities(user_id, created_at DESC);
```
```

**效果验证**: ✓N+1查询问题量化(300+次→1次) ✓两种优化方案(JOIN/批量) ✓分页强制限制 ✓Redis缓存策略 ✓复合索引建议

### 案例4: 大PR拆分建议

**输入**:
```
PR: 用户系统大重构 - 包含认证重构+权限系统+审计日志+API网关
变更: +1200行 / -450行 / 28文件
```

**LLM生成输出**:
```markdown
# 大PR拆分建议
# ...
## 评估(续1)
- 变更尺寸: 1200行（严重超标，需拆分）
- 涉及4个独立功能模块
- 建议: 拆分为5个PR
# ...
## 拆分方案(续1)
# ...
### PR 1: 数据库Schema变更（基础，先合并）
- 文件: 
  - migrations/002_user_permissions.sql
  - migrations/003_audit_logs.sql
  - src/db/schema.ts
- 行数: ~150行
- 说明: 新增权限表和审计日志表，向后兼容
- 审查重点: 索引设计、字段类型、外键约束
# ...
### PR 2: 认证模块重构（依赖PR1）
- 文件:
  - src/auth/auth-service.ts
  - src/auth/token-manager.ts
  - src/auth/middleware.ts
- 行数: ~280行
- 说明: 从密码认证重构为JWT+Refresh Token
- 审查重点: 安全性（Token存储/刷新/撤销）、回归测试
# ...
### PR 3: 权限系统实现（依赖PR1, PR2）
- 文件:
  - src/auth/rbac.ts
  - src/auth/permission-checker.ts
  - src/api/middleware/permission.ts
- 行数: ~250行
- 说明: RBAC权限模型实现
- 审查重点: 权限粒度、性能（缓存）、边界测试
# ...
### PR 4: 审计日志（依赖PR3）
- 文件:
  - src/audit/logger.ts
  - src/audit/middleware.ts
  - src/audit/exporter.ts
- 行数: ~200行
- 说明: 操作日志记录与导出
- 审查重点: 性能影响（异步写入）、日志完整性
# ...
### PR 5: API网关（依赖PR2, PR3）
- 文件:
  - src/api/gateway.ts
  - src/api/routes.ts
  - src/api/middleware/composite.ts
- 行数: ~320行
- 说明: 统一鉴权+限流+日志中间件
- 审查重点: 中间件顺序、错误处理、性能
# ...
## 合并顺序与依赖图
```
PR1 (Schema) ──┬──→ PR2 (Auth) ──┬──→ PR5 (Gateway)
               │                  │
               └──→ PR3 (RBAC) ──┘
                      │
                      └──→ PR4 (Audit)
```
# ...
## 每个PR的审查清单
- [ ] PR1: Schema变更是否向后兼容？索引是否合理？
- [ ] PR2: Token刷新逻辑是否安全？是否有撤销机制？
- [ ] PR3: 权限检查是否影响性能？是否有缓存？
- [ ] PR4: 日志写入是否阻塞主流程？是否异步？
- [ ] PR5: 中间件顺序是否正确？错误是否传播？
# ...
## 风险评估
| PR | 风险 | 回滚难度 |
|:------|------:|:------|
| PR1 | 低（向后兼容） | 易（drop table） |
| PR2 | 高（认证变更） | 中（保留旧逻辑） |
| PR3 | 中（权限模型） | 中 |
| PR4 | 低（新增功能） | 易 |
| PR5 | 高（网关变更） | 难（影响全量API） |
```

**效果验证**: ✓1200行拆分为5个PR ✓依赖关系图清晰 ✓每个PR有审查重点 ✓合并顺序明确 ✓风险评估含回滚难度

### 案例5: 新人代码指导审查

**输入**:
```
PR: 新人开发者首次提交 - 用户列表查询功能
开发者: 入职2周的新人
变更: +60行 / 2文件
代码:
```typescript
// src/api/users.ts
export async function getUsers(req, res) {
  try {
    const users = await User.findAll();
    return res.json(users);
  } catch (e) {
    return res.status(500).json({ error: e.message });
  }
}
```
```

**LLM生成输出**:
```markdown
# 代码审查报告：用户列表查询（新人指导）
# ...
## 总体评估: Approve with Suggestions
- 变更尺寸: 60行（理想）
- 五维度评分: 正确性 7/10 | 可维护性 6/10 | 安全性 5/10 | 性能 6/10 | 可测试性 4/10
- 总体: 逻辑正确，错误处理有意识，建议在以下方面改进
# ...
## 问题清单(续2)
# ...
### Should Fix（建议改进）
# ...
**[S1] 返回所有用户数据可能泄露敏感信息**
- 文件: src/api/users.ts:4
- 问题: `User.findAll()` 返回所有字段，可能包含密码哈希
- 学习点: 永远不要返回敏感字段，使用字段选择
```typescript
// 改进方案
const users = await User.findAll({
  attributes: ['id', 'name', 'email', 'createdAt']  // 明确字段
});
```
# ...
**[S2] 缺少分页**
- 文件: src/api/users.ts:3
- 问题: 返回所有用户，用户量大会导致性能问题
- 学习点: 列表API必须分页
```typescript
// 改进方案
const page = parseInt(req.query.page) || 1;
const limit = Math.min(parseInt(req.query.limit) || 20, 100);
const offset = (page - 1) * limit;
const { rows: users, count } = await User.findAndCountAll({
  attributes: ['id', 'name', 'email'],
  limit, offset,
  order: [['createdAt', 'DESC']]
});
return res.json({
  users,
  pagination: { page, limit, total: count }
});
```
# ...
**[S3] 错误信息泄露内部实现**
- 文件: src/api/users.ts:6
- 问题: `e.message`可能包含SQL语句等敏感信息
- 学习点: 对外错误用通用消息，内部细节记录日志
```typescript
// 改进方案
import logger from '../utils/logger';

export async function getUsers(req, res) {
  try {
    // ... 业务逻辑
  } catch (e) {
    logger.error('Failed to fetch users', { error: e, requestId: req.id });
    return res.status(500).json({ 
      error: 'INTERNAL_ERROR',
      message: 'Failed to fetch users',
      requestId: req.id  // 便于排查
    });
  }
}
```
# ...
### Optional（可选改进）
# ...
**[O1] 添加输入校验**
- 学习点: 永远不信任用户输入
```typescript
import { z } from 'zod';

const querySchema = z.object({
  page: z.string().regex(/^\d+$/).optional(),
  limit: z.string().regex(/^\d+$/).optional(),
});

const parsed = querySchema.safeParse(req.query);
if (!parsed.success) {
  return res.status(400).json({ error: 'INVALID_QUERY' });
}
```
# ...
### Praise（值得表扬）(补充)(补充)
# ...
**[P1] 错误处理意识**
- 表扬: 新人能主动try-catch捕获异常，是良好的起点
- 鼓励: 继续保持错误处理的意识，进一步学习错误分类与传播
# ...
**[P2] 函数职责单一**
- 表扬: `getUsers`函数只做一件事，命名清晰
- 鼓励: 保持这种单一职责的设计思维
# ...
## 学习建议（针对新人）
1. **安全意识**: 阅读 OWASP Top 10，理解常见Web漏洞
2. **API设计**: 学习RESTful最佳实践，特别是分页与过滤
3. **错误处理**: 区分业务错误（4xx）和系统错误（5xx）
4. **测试**: 补充单元测试，覆盖正常和异常路径
# ...
## 总结
作为首次提交，代码质量良好。主要改进方向是安全性和性能意识。建议合并后，在后续PR中逐步改进上述Should Fix项。
```

**效果验证**: ✓建设性反馈语气 ✓3个Should Fix含学习点 ✓2个Praise鼓励 ✓针对新人的学习建议 ✓Approve with Suggestions非阻塞

## 常见问题

### Q1: 代码审查哨兵与 ESLint/SonarQube 有何区别？
A: ESLint/SonarQube 是**自动化静态分析工具**，基于规则匹配发现已知模式问题（如未使用变量、复杂度过高）。代码审查哨兵是**LLM 驱动的语义审查**，能理解业务逻辑、跨文件上下文、设计意图。两者互补：静态分析快速拦截常见问题，哨兵深入审查语义与架构。

### Q2: 审查标准是否过于严格？
A: 标准可配置。Blocking 仅针对"必须修复才能合并"的问题（安全漏洞/逻辑错误/数据丢失）。Should Fix 是建议，不阻塞合并。Nit 是小问题，可选修复。团队可根据成熟度调整阈值。

### Q3: 如何避免审查中的"误报"？
A: 所有问题标注依据（代码行/风险说明/建议方案）。作者可对问题回复"需讨论"或"误报"，审查者确认后调整。LLM 不确定时标注"需人工确认"，避免过度自信。

### Q4: 大 PR（> 500 行）如何高效审查？
A: 1）先看变更概览与尺寸评估；2）优先审查 Blocking 问题；3）按文件/模块分段审查；4）提供拆分建议（如示例 2）；5）异步输出完整报告，避免阻塞。

## 已知限制

- 依赖 LLM 能力，复杂业务逻辑理解可能不如领域专家深入
- 无法执行代码运行时验证（如实际测试、性能基准），仅静态审查
- 跨仓库依赖分析能力有限（仅审查当前 diff，不追踪外部依赖变更）
- 性能取决于底层 LLM，大 PR 审查可能耗时较长
- 不替代人工审查的"经验判断"（如架构合理性、产品需求匹配度）

## 安全

- **API Key 零暴露**：本 Skill 不涉及外部 API 调用，无需配置密钥
- **密钥泄露检测**：审查时强制检查代码中是否硬编码密钥/令牌/凭证
- **最小权限原则**：审查代码是否遵循最小权限（如数据库用户、API 角色）
- **输入校验检查**：强制审查输入校验（防 SQL 注入/XSS/CSRF）
- **依赖漏洞扫描**：提醒检查依赖是否有已知 CVE（建议配合 Snyk/Dependabot）
- **敏感信息提醒**：审查时如发现敏感信息（密钥/客户数据），提醒立即移除并轮换
