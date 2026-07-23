---
slug: "monad-development"
name: "monad-development"
version: "1.0.0"
displayName: "Monad Development"
summary: "在Monad区块链建dapp,部署合约/配前端"
license: "Proprietary"
description: |-
  Builds dapps on Monad blockchain。Use when deploying contracts, setting
  up frontends with viem/wa。Use when 需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于无明确技术栈的模糊需求。适用于独立开发者、企业团队和自动化工作流场景。
tags:
  - Other
tools:
  - - read
  - exec
homepage: "https://skillhub.cn"
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
---
# Monad Development

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-------|:-------|
| Builds dapps on Monad blockchain | 支持 | 支持 |
| Use when deploying contracts, setting | 不支持 | 支持 |
| 批量处理 | 不支持 | 支持 |
| 高级配置 | 不支持 | 支持 |

## 核心能力

- Builds dapps on Monad blockchain
- Use when deploying contracts, setting
  up frontends with viem/wa
#
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

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| content | string | 否 | monad-development处理的内容输入 |,  |
| content | string | 否 | monad-development处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "development 相关配置参数",
    result: "development 相关配置参数",
    result: "development 相关配置参数",
    "metadata": {
      "template_used": "reviewer",
      "word_count": 0,
      "style": "专业"
    }
  },
  "error": null
}
```

输出模板参考: `assets/output.json`

## 异常处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 

### 可用性分类
- **分类**: MD+EXEC()
- **说明**: 基于Markdown的AI Skill,


**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统。
## 案例展示

**1. Create project:**

```bash
forge init my-token
cd my-token
```

**2. Configure `foundry.toml`:**

```toml
[profile.default]
src = "src"
out = "out"
libs = ["lib"]
evm_version = "prague"
solc_version = "0.8.28"
```

**3. Create contract `src/MyToken.sol`:**

solidity

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;

import "@openzeppelin/contracts/token/ERC20/ERC20.sol";

contract MyToken is ERC20 {
    constructor(uint256 initialSupply) ERC20("MyToken", "MTK") {
        _mint(msg.sender, initialSupply);
    }
}
```

**4. Install dependencies:**

```bash
forge install OpenZeppelin/openzeppelin-contracts --no-commit
```

**5. Create deploy script `（请参考skill目录中的脚本文件）`:**

solidity

```
// SPDX-License-Identifier: MIT
pragma solidity ^0.8.27;
import "forge-std/Script.sol";
import "../src/MyToken.sol";

contract DeployScript is Script {
    function run() external {
        vm.startBroadcast();
        MyToken token = new MyToken(1000000 * 10**18);
        console.log("Token deployed at:", address(token));
        vm.stopBroadcast();
    }
}
```

**6. Deploy:**

```bash
forge script （请参考skill目录中的脚本文件）:DeployScript \
  --rpc-url https://testnet-rpc.monad.xyz \
  --private-key $PRIVATE_KEY \
  --broadcast
```

**7. Verify:**

```bash
STANDARD_INPUT=$(forge verify-contract <TOKEN_ADDRESS> src/MyToken.sol:MyToken --chain 10143 --show-standard-json-input)
COMPILER_VERSION=$(jq -r '.metadata | fromjson | .compiler.version' out/MyToken.sol/MyToken.json)

curl -X POST https://agents.devnads.com/v1/verify \
  -H "Content-Type: application/json" \
  -d "{
    \"chainId\": 10143,
    \"contractAddress\": \"<TOKEN_ADDRESS>\",
    \"contractName\": \"src/MyToken.sol:MyToken\",
    \"compilerVersion\": \"v${COMPILER_VERSION}\",
    \"standardJsonInput\": $STANDARD_INPUT,
    \"constructorArgs\": \"$(cast abi-encode 'constructor(uint256)' 1000000000000000000000000 | sed 's/0x//')\"
  }"
```

## 常见问题

### Q1: 如何开始使用Monad Development？
A: 

### Q2: 遇到错误怎么办？
A: 

### Q3: Monad Development有什么限制？
A: 

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

