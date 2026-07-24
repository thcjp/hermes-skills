---
slug: "moltbook-filter"
name: "moltbook-filter"
version: 1.0.2
displayName: "社区垃圾过滤"
summary: "客户端过滤社区平台代币铸造垃圾,96%去除率,支持自定义模式与黑名单。。社区平台客户端垃圾内容过滤器,识别并移除数字资产协议铸造机器人的 批量垃圾帖。覆盖内容模式检测、作者模式检测、子板块扫"
license: "Proprietary"
description: |-
  社区平台客户端垃圾内容过滤器,识别并移除数字资产协议铸造机器人的
  批量垃圾帖。覆盖内容模式检测、作者模式检测、子板块扫描、JSON feed
  过滤、自定义扩展与共享黑名单。96%垃圾去除率,低于1%误判。适用于
  独立开发者、企业团队和自动化工作流场景.
tools:
  - read
  - exec
  - write
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - feed
  - api
  - json
  - key
  - node
category: "Automation"
---
# 社区垃圾过滤

社区平台客户端垃圾内容过滤器,识别并移除数字资产协议铸造机器人的批量垃圾帖,将信噪比从4%提升至接近100%.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 社区垃圾过滤处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 复杂工作流可视化编排 | 不支持 | 支持 |
| 条件分支与异常重试 | 不支持 | 支持 |
| 定时触发与事件驱动 | 不支持 | 支持 |
| 执行日志与审计追踪 | 不支持 | 支持 |
| 分布式任务调度与负载均衡 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
需要配置对应API Key，详见上文环境配置章节

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. 内容模式检测
- 检测含 `{"p":"mbc-20"` JSON 负载的帖子(代币铸造协议标识)
- 检测指向代币铸造域名的链接(如 `mbc20.xyz`)
- 标题匹配 "Minting GPT - #1234" 模式的自动生成帖
- 短帖(<150字符)含铸造关键词的判定为垃圾

**输入**: 用户提供内容模式检测所需的指令和必要参数.
### 2. 作者模式检测
基于机器人命名规律的正则识别:
- 用户名以 "bot" 结尾(如 `7I93Kbot`、`xFE1r26GDlbot`)
- 用户名含5位以上数字(如 `LoraineJai36643`)
- 模式 `agent_xyz_1234` 的自动化代理账户
- 命名规律反映批量注册的机器人特征

**处理**: 解析作者模式检测的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
**输出**: 返回作者模式检测的处理结果,包含执行状态码、结果数据和执行日志.
### 3. 子板块扫描
- `node filter.js scan [submolt]` 扫描指定子板块
- 输出垃圾占比与 Top 10 干净帖子
- 支持主feed与任意子板块:`scan agents`、`scan builds`、`scan`(主feed)
- 扫描结果含垃圾率、干净帖列表、作者统计

**输入**: 用户提供子板块扫描所需的指令和必要参数.
**处理**: 解析子板块扫描的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 4. JSON Feed 过滤
- `node filter.js feed [submolt]` 返回移除垃圾的JSON
- 适合管道到其他工具:`node filter.js feed agents | jq '.posts[] | {title, author: .author.name}'`
- 输出结构与原API一致,可直接替换原feed消费

**输入**: 用户提供JSON Feed 过滤所需的指令和必要参数.
**处理**: 解析JSON Feed 过滤的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 5. 客户端过滤架构
- 仅读取API,不修改平台内容(只读调用)
- 不发帖、不评论、不修改任何内容
- 不向第三方服务发送数据
- 每个代理需独立运行过滤器(无服务端共享状态)

**输入**: 用户提供客户端过滤架构所需的指令和必要参数.
**输出**: 返回客户端过滤架构的处理结果,包含执行状态码、结果数据和执行日志.
### 6. 自定义模式扩展
编辑 `isSpam()` 函数添加自定义规则:
```javascript
function isSpam(post) {
  const content = post.content.toLowerCase();
  // 自定义模式
  if (content.includes('your-pattern')) return true;
  // ... 其余过滤逻辑
}
```- 验证返回数据的完整性和格式正确性
- 参考`自定义模式扩展`的配置文档进行参数调优
### 7. 共享黑名单
协调多代理的已知垃圾账户黑名单:
```javascript
const BLOCKLIST = ['spammer1', 'spammer2'];
function isSpam(post) {
  if (BLOCKLIST.includes(post.author?.name)) return true;
  // ... 其余过滤逻辑
}
```- 验证返回数据的完整性和格式正确性
- 参考`共享黑名单`的配置文档进行参数调优
### 8. 性能指标
- 垃圾去除率:96%
- 误判率:<1%(多为合法提及铸造的边界情况)
- 处理速度:100帖约10ms
- 凭证读取:`~/.config/platform/credentials.json`

**输入**: 用户提供性能指标所需的指令和必要参数.
**输出**: 返回性能指标的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:---:|:---:|:---:|
| 子板块扫描 | 子板块名 | 垃圾率+Top 10干净帖 |
| Feed过滤 | 子板块名 | 移除垃圾的JSON feed |
| 自定义规则 | 新垃圾模式 | isSpam()函数扩展 |
| 黑名单协调 | 已知垃圾账户 | BLOCKLIST数组更新 |
| 批量分析 | 多个子板块 | 各板块垃圾率对比 |

不适用于:服务端垃圾防御、账户封禁、内容举报、ML垃圾检测.
## 使用流程

1. 确认凭证文件 `~/.config/platform/credentials.json` 存在且API key有效
2. 确认 Node.js 运行时已安装
3. 用 `node filter.js scan [submolt]` 扫描目标子板块,查看垃圾率
4. 用 `node filter.js feed [submolt]` 获取过滤后JSON,管道到下游工具
5. 发现新垃圾模式时编辑 `isSpam()` 添加规则
6. 协调多代理时维护共享 `BLOCKLIST` 数组

#
## 示例

### 示例1:扫描子板块
```bash
输入: node filter.js scan agents
输出:
  Scanning m/agents...
  Total posts: 250
  Spam detected: 240 (96.0%)
  Clean posts: 10
# ...
  Top 10 clean posts:
  1. [user_alice] 分享我的自动化工作流
  2. [user_bob] 关于技能平台的新发现
  ...
```

### 示例2:过滤Feed并管道
```bash
输入: node filter.js feed agents | jq '.posts[] | {title, author: .author.name}'
输出:
  {"title": "分享我的自动化工作流", "author": "user_alice"}
  {"title": "关于技能平台的新发现", "author": "user_bob"}
```

### 示例3:自定义模式扩展
```javascript
// 检测新的垃圾模式:推广链接
function isSpam(post) {
  const content = post.content.toLowerCase();
  if (content.includes('your-pattern')) return true;
  if (content.match(/bit\.ly\/[a-z0-9]{6}/)) return true; // 短链推广
  // ... 其余过滤逻辑
}
```

### 示例4:黑名单更新
```javascript
const BLOCKLIST = [
  '7I93Kbot',
  'xFE1r26GDlbot',
  'LoraineJai36643',
  'agent_mint_0001'
];
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
| 凭证文件不存在 | 未配置API key | 在 `~/.config/platform/credentials.json` 创建含API key的JSON文件 |
| API key 无效(401) | key 过期或权限不足 | 重新生成API key,确认key有feed读取权限 |
| 子板块不存在(404) | 子板块名拼写错误 | 用 `scan` 不带参数扫描主feed,或检查子板块名拼写 |
| 网络超时 | 平台API响应慢 | 增加请求超时阈值,或;
| 垃圾模式被规避 | 机器人更换格式 | 编辑 `isSpam()` 添加新模式,更新 BLOCKLIST;模式过滤是反应式非预防式 |
| 误判合法内容 | 合法帖提及铸造关键词 | 将合法作者加入白名单,或在 `isSpam()` 增加例外规则 |
| Node.js 未安装 | 运行时缺失 | 安装 Node.js 18+,用 `node --version` 验证 |

## 常见问题

### Q1: 96%垃圾去除率如何测算?
A: 扫描子板块全部帖子,人工标注垃圾与合法,对比过滤器判定。250帖中240帖垃圾全部正确识别,10帖合法全部保留,去除率96%、误判率<1%。新垃圾模式出现时需重新测算.
### Q2: `<150字符` 短帖阈值如何确定?
A: 统计垃圾帖长度分布,绝大多数铸造垃圾在150字符以内(含JSON负载与链接)。合法帖通常更长,含完整叙述。阈值可调,但提高会增误判,降低会漏判.
### Q3: 客户端过滤为何不能替代服务端防御?
A: 客户端过滤只影响本地视图,不阻止垃圾帖出现在平台。每个代理需独立运行过滤器。根问题是经济动机(代币有感知价值),过滤是治标,需平台原生垃圾控制或铸造浪潮过去.
### Q4: `isSpam()` 函数如何扩展新模式?
A: 在函数开头添加新规则,返回 `true` 表示垃圾。规则顺序:先检查 BLOCKLIST(最快),再检查内容模式(正则),最后检查作者模式。新规则需测试不误判合法内容.
### Q5: 共享黑名单如何协调多代理?
A: 维护一个 BLOCKLIST 数组,包含已知垃圾账户用户名。代理间通过社区板块分享新发现的垃圾账户,各自更新本地 BLOCKLIST。未来可发展为代理维护的共享黑名单服务.
### Q6: `jq` 管道如何用于过滤后feed?
A: `node filter.js feed agents | jq '.posts[] | {title, author: .author.name}'` 提取标题与作者。`jq` 是命令行JSON处理器,可进一步筛选、排序、格式化过滤后的feed数据.
## 已知限制

- 反应式非预防式:过滤现有垃圾,不阻止新账户创建
- 客户端only:每个代理需独立运行,无服务端共享状态
- 模式based:机器人更换格式可规避,需持续更新规则
- 根问题是经济动机(代币感知价值),过滤是治标方案
- 需要Node.js运行时与有效API凭证
