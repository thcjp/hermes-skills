---
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
summary: "经Anyone Protocol网络路由请求"
---
# Anyone Procotol Proxy

This skill enables Clawdbot to route requests through the Anyone Protocol network.

## How It Works

The skill uses the `@anyone-protocol/anyone-client` NPM package to:

1. Start a local SOCKS5 proxy server (default port: 9050)
2. Create encrypted circuits through the Anyone Network
3. Route traffic through these circuits
4. Return responses while keeping the origin IP hidden


## Install anyone-client

```bash
npm install -g @anyone-protocol/anyone-client
```

## Start the proxy

```bash
npx @anyone-protocol/anyone-client -s 9050
```

## Usage

Once the proxy is running, route requests through it:

```bash
curl --socks5-hostname localhost:9050 https://check.en.anyone.tech/api/ip
```

```javascript
import { Anon } from "@anyone-protocol/anyone-client";
import { AnonSocksClient } from "@anyone-protocol/anyone-client";

async function main() {
    const anon = new Anon();
    const anonSocksClient = new AnonSocksClient(anon);

    try {
        await anon.start();
        // Wait for circuits to establish
        await new Promise(resolve => setTimeout(resolve, 15000));

        const response = await anonSocksClient.get('https://check.en.anyone.tech/api/ip');
        console.log('Response:', response.data);

    } catch(error) {
        console.error('Error:', error);
    } finally {
        await anon.stop();
    }
}

main();
```

## Notes

* First connection may take up to 30 seconds while circuits are established
* The proxy persists across requests once started

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

- This skill enables IP address masking and accessing hidden services
  on the Anyone Network
- 触发关键词: address, procotol, enables, anyone, proxy, masking, skill

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

### Q1: 如何开始使用Anyone Proxy？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Anyone Proxy有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
