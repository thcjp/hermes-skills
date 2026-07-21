---
slug: vpn-rotate-skill
name: vpn-rotate-skill
version: "0.1.0"
displayName: Vpn Rotate Skill
summary: Bypass API rate limits by rotating VPN servers. Works with any OpenVPN-compatible
  VPN (ProtonVPN,...
license: MIT
description: |-
  Bypass API rate limits by rotating VPN servers。Works with any OpenVPN-compatible
  VPN (ProtonVPN,。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags:
- Integrations
tools:
  - - read
- exec
---

# Vpn Rotate Skill

Rotate VPN servers to bypass API rate limits. Works with any OpenVPN-compatible VPN.

## Setup

### 1. Run Setup Wizard

```bash
./scripts/setup.sh
```

This will:

* Check OpenVPN is installed
* Help you configure your VPN provider
* Set up passwordless sudo
* Test the connection

### 2. Manual Setup

If you prefer manual setup:

```bash
sudo apt install openvpn

mkdir -p ~/.vpn/servers


echo "your_username" > ~/.vpn/creds.txt
echo "your_password" >> ~/.vpn/creds.txt
chmod 600 ~/.vpn/creds.txt

echo "$USER ALL=(ALL) NOPASSWD: /usr/sbin/openvpn, /usr/bin/killall" | sudo tee /etc/sudoers.d/openvpn
```

## Usage

### Decorator (Recommended)

```python
from scripts.decorator import with_vpn_rotation

@with_vpn_rotation(rotate_every=10, delay=1.0)
def scrape(url):
    return requests.get(url).json()

for url in urls:
    data = scrape(url)
```

### VPN Class

```python
from scripts.vpn import VPN

vpn = VPN()

vpn.connect()
print(vpn.get_ip())  # New IP

vpn.rotate()
print(vpn.get_ip())  # Different IP

vpn.disconnect()
```

### Context Manager

```python
from scripts.vpn import VPN

vpn = VPN()

with vpn.session():
    # VPN connected
    for url in urls:
        vpn.before_request()  # Handles rotation
        data = requests.get(url).json()
```

### CLI

```bash
python scripts/vpn.py connect
python scripts/vpn.py status
python scripts/vpn.py rotate
python scripts/vpn.py disconnect
python scripts/vpn.py ip
```

## Configuration

### Decorator Options

```python
@with_vpn_rotation(
    rotate_every=10,      # Rotate after N requests
    delay=1.0,            # Seconds between requests
    config_dir=None,      # Override config directory
    creds_file=None,      # Override credentials file
    country=None,         # Filter servers by country prefix (e.g., "us")
    auto_connect=True,    # Connect automatically on first request
)
```

### VPN Class Options

```python
VPN(
    config_dir="~/.vpn/servers",
    creds_file="~/.vpn/creds.txt",
    rotate_every=10,
    delay=1.0,
    verbose=True,
)
```

## Recommended Settings

| API Aggressiveness | rotate_every | delay |
| --- | --- | --- |
| Aggressive (Catastro, LinkedIn) | 5 | 2.0s |
| Standard | 10 | 1.0s |
| Lenient | 20-50 | 0.5s |

## Files

```text
vpn-rotate-skill/
├── SKILL.md              # This file
├── README.md             # Overview
├── scripts/
│   ├── vpn.py            # VPN controller
│   ├── decorator.py      # @with_vpn_rotation
│   └── setup.sh          # Setup wizard
├── examples/
│   └── catastro.py       # Spanish property API example
└── providers/
    ├── protonvpn.md      # ProtonVPN setup
    ├── nordvpn.md        # NordVPN setup
    └── mullvad.md        # Mullvad setup
```

## Troubleshooting

### "sudo: a password is required"

Run the setup script or manually add sudoers entry:

```bash
echo "$USER ALL=(ALL) NOPASSWD: /usr/sbin/openvpn, /usr/bin/killall" | sudo tee /etc/sudoers.d/openvpn
```

### Connection fails

1. Check credentials are correct
2. Test manually: `sudo openvpn --config ~/.vpn/servers/server.ovpn --auth-user-pass ~/.vpn/creds.txt`
3. Check VPN provider account is active

### Still getting blocked

1. Lower `rotate_every` (try 5 instead of 10)
2. Increase `delay` (try 2-3 seconds)
3. Check if API blocks VPN IPs entirely

### No .ovpn files

Download from your VPN provider:

* ProtonVPN: <https://protonvpn.com/support/vpn-config-download/>
* NordVPN: <https://nordvpn.com/ovpn/>
* Mullvad: <https://mullvad.net/en/account/#/openvpn-config>

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

- Bypass API rate limits by rotating VPN servers
- Works with any OpenVPN-compatible
  VPN (ProtonVPN,
- 触发关键词: limits, servers, rotating, vpn, rate, rotate, bypass, skill

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

## 常见问题

### Q1: 如何开始使用Vpn Rotate Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Vpn Rotate Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
