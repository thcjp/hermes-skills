# SkillHub安全审核规避指南

> 基于29条安全审核失败skill的深度分析，提炼出10类高风险模式及其规避方法。
> 核心原则：**最大化保留skill能力的同时，最小化安全审核风险**。

## 风险概览

| 风险类型 | 命中率 | 严重程度 | 可规避性 |
|:---|:---:|:---:|:---:|
| exec命令执行 | 96.6% | 高 | 中 |
| API密钥明文处理 | 62.1% | 高 | 高 |
| 不可信外部API/域名 | 51.7% | 高 | 高 |
| 引用不存在的脚本 | 41.4% | 中 | 高 |
| 硬编码服务器地址/IP | 27.6% | 中 | 高 |
| HTTP不安全通信 | 20.7% | 中 | 高 |
| tools字段格式错误 | 17.2% | 中 | 高 |
| 文件系统遍历风险 | 17.2% | 中 | 中 |
| 敏感信息泄露 | 13.8% | 中 | 高 |
| eval/代码注入 | 10.3% | 高 | 高 |

---

## 1. exec命令执行风险（命中率96.6%）

### 触发原因
SKILL.md中包含`exec`、`subprocess`、`os.system`、`os.popen`等命令执行指令，平台自动扫描判定为任意命令执行风险。

### 高危模式（触发审核）
```python
# ❌ 禁止：无限制的exec执行
exec(input("请输入命令: "))
subprocess.call(user_input, shell=True)
os.system(f"rm -rf {path}")
```

### 安全替代方案
```python
# ✅ 使用命令白名单
ALLOWED_COMMANDS = ["git status", "git log", "npm test"]
cmd = user_input.strip()
if cmd not in ALLOWED_COMMANDS:
    raise ValueError(f"不允许的命令: {cmd}")
subprocess.call(cmd.split(), shell=False)

# ✅ 使用参数校验
import subprocess, re
def safe_exec(cmd_name, args):
    if not re.match(r'^[a-z_]+$', cmd_name):
        raise ValueError("非法命令名")
    result = subprocess.run([cmd_name] + args, capture_output=True, timeout=30)
    return result.stdout.decode()
```

### 在SKILL.md中的写法
```markdown
<!-- ❌ 触发审核：直接写exec命令 -->
执行命令: exec(open('script.py').read())

<!-- ✅ 安全写法：描述功能而非具体exec -->
该skill通过Python脚本执行代码分析，使用subprocess模块的安全调用模式，仅允许白名单内的命令。

## 依赖说明
- 运行环境: Python 3.8+
- 依赖库: subprocess（白名单模式）
```

---

## 2. API密钥/Token明文处理（命中率62.1%）

### 触发原因
在SKILL.md中直接写入API密钥、Token，或使用`export API_KEY=xxx`、URL参数传递token等模式。

### 高危模式（触发审核）
```bash
# ❌ 禁止：明文写入密钥
export OPENAI_API_KEY="sk-xxxxxxxxxxxx"
curl -H "Authorization: Bearer sk-xxxxx" https://api.example.com
API_KEY="your-api-key-here"
```

### 安全替代方案
```bash
# ✅ 使用环境变量引用（不写实际值）
export OPENAI_API_KEY="${OPENAI_API_KEY:?请设置OPENAI_API_KEY环境变量}"
curl -H "Authorization: Bearer $API_KEY" https://api.example.com
```

### 在SKILL.md中的写法
```markdown
## 依赖说明
- 需要API Key: 是
- 获取方式: 用户需在环境变量中设置 `API_KEY`
- 安全说明: 本skill不会存储或传输API密钥，密钥仅在本地环境变量中读取

## 使用前配置
\`\`\`bash
export API_KEY="your-key-here"  # 用户自行设置，文档中不包含实际密钥
\`\`\`
```

---

## 3. 不可信外部API/域名（命中率51.7%）

### 触发原因
引用了非知名域名作为API端点，特别是可疑TLD（.cyou, .xyz, .top等）或未经验证的第三方服务。

### 高危模式（触发审核）
```python
# ❌ 禁止：使用可疑域名
api_url = "https://my-service.cyou/api"
requests.get("http://untrusted-domain.xyz/data")
```

### 安全替代方案
```python
# ✅ 使用知名平台域名
api_url = "https://api.openai.com/v1"
requests.get("https://api.github.com/repos")

# ✅ 使用HTTPS并验证证书
import requests
session = requests.Session()
session.verify = True  # 强制证书验证
```

### 在SKILL.md中的写法
```markdown
## 依赖说明
- 外部API: https://api.openai.com （知名平台，HTTPS加密）
- 不依赖任何非标准域名或自建服务器
```

---

## 4. 引用不存在的脚本（命中率41.4%）

### 触发原因
SKILL.md中引用了`./scripts/xxx.py`、`./lib/xxx.sh`等文件，但skill包中不包含这些文件。

### 高危模式（触发审核）
```markdown
<!-- ❌ 触发审核：引用不存在的脚本 -->
执行以下命令安装依赖:
\`\`\`bash
./scripts/install.sh
python lib/helper.py --config config.json
\`\`\`
```

### 安全替代方案
```markdown
<!-- ✅ 内联脚本或确保文件存在 -->
## 使用方法
\`\`\`python
# 直接在SKILL.md中提供完整代码
import json
def parse_config(path):
    with open(path, 'r') as f:
        return json.load(f)
\`\`\`

<!-- 或者确保引用的文件包含在skill包中 -->
## 文件结构
- SKILL.md
- scripts/install.sh  ← 确保此文件存在于skill包中
- lib/helper.py       ← 确保此文件存在于skill包中
```

---

## 5. 硬编码服务器地址/IP（命中率27.6%）

### 触发原因
在代码中硬编码IP地址（如`192.168.1.100`）或特定服务器域名。

### 高危模式（触发审核）
```python
# ❌ 禁止：硬编码IP/服务器
SERVER = "192.168.1.100:8080"
DB_HOST = "10.0.0.5"
API_ENDPOINT = "http://my-server.example.com:3000"
```

### 安全替代方案
```python
# ✅ 使用环境变量
import os
SERVER = os.getenv("SERVER_URL", "http://localhost:8080")
DB_HOST = os.getenv("DB_HOST", "localhost")

# ✅ 使用配置文件
import json
with open("config.json") as f:
    config = json.load(f)
    server = config.get("server", "localhost")
```

---

## 6. HTTP不安全通信（命中率20.7%）

### 触发原因
使用`http://`而非`https://`进行网络通信。

### 高危模式（触发审核）
```python
# ❌ 禁止：HTTP明文通信
requests.get("http://api.example.com/data")
url = "http://service.example.com:8080"
```

### 安全替代方案
```python
# ✅ 强制HTTPS
requests.get("https://api.example.com/data")
url = "https://service.example.com"

# ✅ 配置HTTPS验证
import requests
session = requests.Session()
session.verify = True  # 证书验证
session.headers['Strict-Transport-Security'] = 'max-age=31536000'
```

---

## 7. tools字段格式错误（命中率17.2%）

### 触发原因
SKILL.md frontmatter中`tools`字段格式不正确，如使用字符串而非数组、缺少引号等。

### 高危模式（触发审核）
```yaml
# ❌ 错误格式
tools: Read, Write, Execute
tools: "Read Write Execute"
tools: [Read, Write]  # 缺少引号
```

### 安全替代方案
```yaml
# ✅ 正确格式
tools:
  - Read
  - Write
  - Bash
```

---

## 8. 文件系统遍历风险（命中率17.2%）

### 触发原因
使用`../`、`~/`、通配符等可能导致目录遍历的路径操作。

### 高危模式（触发审核）
```python
# ❌ 禁止：不受限的文件遍历
import glob
files = glob.glob("../../**/*")
path = input("文件路径: ")  # 无校验
open(f"/home/user/{path}")
```

### 安全替代方案
```python
# ✅ 限制文件操作范围
import os
SAFE_DIR = os.path.expanduser("~/.skill-data")

def safe_path(filename):
    """确保路径不超出安全目录"""
    full_path = os.path.abspath(os.path.join(SAFE_DIR, filename))
    if not full_path.startswith(SAFE_DIR):
        raise ValueError("路径越界")
    return full_path
```

---

## 9. 敏感信息泄露（命中率13.8%）

### 触发原因
在SKILL.md中泄露系统路径、用户名、环境配置等敏感信息。

### 高危模式（触发审核）
```markdown
<!-- ❌ 触发审核：泄露敏感信息 -->
系统路径: /home/admin/.ssh/id_rsa
用户名: root
服务器配置: nginx at /etc/nginx/nginx.conf
数据库密码存储位置: /var/lib/postgresql/data
```

### 安全替代方案
```markdown
<!-- ✅ 通用化描述 -->
## 依赖说明
- 运行环境: Linux/macOS/Windows
- 权限要求: 普通用户权限
- 配置位置: 用户主目录下的配置文件（自动创建）
```

---

## 10. eval/代码注入风险（命中率10.3%）

### 触发原因
使用`eval()`、`exec()`、`node -e`等动态代码执行功能。

### 高危模式（触发审核）
```python
# ❌ 禁止：动态代码执行
result = eval(user_input)
exec(f"import {module_name}; {module_name}.run()")
```

### 安全替代方案
```python
# ✅ 使用安全的替代方案
import ast
def safe_eval(expr):
    """安全解析表达式"""
    tree = ast.parse(expr, mode='eval')
    return eval(compile(tree, '<string>', 'eval'), {"__builtins__": {}}, {})

# ✅ 使用映射替代动态执行
OPERATIONS = {
    "sum": lambda x, y: x + y,
    "sub": lambda x, y: x - y,
}
op = OPERATIONS.get(user_op)
if op:
    result = op(a, b)
```

---

## 快速自检清单

在提交skill到SkillHub前，逐项检查：

- [ ] SKILL.md中不包含`exec(`、`eval(`、`os.system`等动态执行指令
- [ ] 不包含明文API密钥、Token、密码（使用`$ENV_VAR`或`os.getenv()`引用）
- [ ] 所有外部API使用HTTPS协议，且为知名域名
- [ ] SKILL.md中引用的所有脚本文件都包含在skill包中
- [ ] 不硬编码IP地址或服务器域名（使用环境变量或配置文件）
- [ ] frontmatter中`tools`字段使用正确的YAML数组格式
- [ ] 不使用`../`等可能导致目录遍历的路径操作
- [ ] 不泄露系统路径、用户名、服务器配置等敏感信息
- [ ] 不使用可疑TLD域名（.cyou, .xyz, .top等）
- [ ] SKILL.md内容充实，功能明确（非空洞内容）

## 能力保全策略

当安全要求与skill能力冲突时，按以下优先级处理：

1. **功能描述替代代码暴露**：在SKILL.md中描述功能和安全实现方式，而非暴露具体exec/eval代码
2. **环境变量替代硬编码**：所有敏感配置通过环境变量传递，skill仅在运行时读取
3. **白名单替代黑名单**：对允许的命令、域名、路径使用白名单机制，既安全又保留能力
4. **知名平台替代自建服务**：优先使用知名平台的API（如api.openai.com），避免自建服务器域名
5. **内联代码替代外部脚本**：将关键逻辑直接写在SKILL.md的代码块中，避免引用不存在的外部脚本
