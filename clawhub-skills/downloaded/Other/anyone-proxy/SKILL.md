---
slug: anyone-proxy
name: anyone-proxy
version: "0.1.0"
displayName: Anyone Procotol Proxy
summary: This skill enables IP address masking and accessing hidden services on the
  Anyone Network. Route ...
license: MIT
description: |-
  This skill enables IP address masking and accessing hidden services
  on the Anyone Network. Route ...

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: address, procotol, enables, anyone, proxy, masking, skill
tags:
- Other
tools:
- read
- exec
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
