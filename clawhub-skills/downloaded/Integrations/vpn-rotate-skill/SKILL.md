---
slug: vpn-rotate-skill
name: vpn-rotate-skill
version: "0.1.0"
displayName: Vpn Rotate Skill
summary: Bypass API rate limits by rotating VPN servers. Works with any OpenVPN-compatible
  VPN (ProtonVPN,...
license: MIT
description: |-
  Bypass API rate limits by rotating VPN servers. Works with any OpenVPN-compatible
  VPN (ProtonVPN,...

  核心能力:

  - 集成工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 第三方API集成、平台对接、数据同步

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: limits, servers, rotating, vpn, rate, rotate, bypass, skill
tags:
- Integrations
tools:
- read
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

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务
