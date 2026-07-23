---
slug: encoding-formats
name: encoding-formats
version: "1.0.0"
displayName: Encoding & Formats
summary: Encode, decode, and convert between data formats. Use when working with Base64,
  URL encoding, hex...
license: MIT
description: |-
  Encode, decode, and convert between data formats。Use when working with
  Base64, URL encoding, hex。Use when 需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于实时流数据处理。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Encoding & Formats

Encode, decode, and inspect data in common formats. Covers Base64, URL encoding, hex, Unicode, JWTs, hashing, checksums, and serialization formats.

## When to Use

* Decoding a Base64 string from an API response or config
* URL-encoding parameters for HTTP requests
* Inspecting hex dumps of binary data
* Decoding JWT tokens to see claims
* Computing or verifying file checksums
* Converting between character encodings (UTF-8, Latin-1, etc.)
* Understanding wire formats (protobuf, MessagePack)

## Base64

### Encode and decode

```bash
echo -n "Hello, World!" | base64

echo "SGVsbG8sIFdvcmxkIQ==" | base64 -d

base64 image.png > image.b64
cat file.bin | base64

base64 -d image.b64 > image.png

echo -n "Hello" | base64 | tr '+/' '-_' | tr -d '='
echo "SGVsbG8" | tr '-_' '+/' | base64 -d
```

### In code

```javascript
// JavaScript (browser + Node.js 16+)
btoa('Hello');                    // "SGVsbG8="
atob('SGVsbG8=');                 // "Hello"

// Node.js Buffer
Buffer.from('Hello').toString('base64');           // "SGVsbG8="
Buffer.from('SGVsbG8=', 'base64').toString();      // "Hello"

// Binary data
Buffer.from(binaryData).toString('base64');
Buffer.from(b64String, 'base64');
```

```python
import base64

base64.b64encode(b"Hello").decode()     # "SGVsbG8="
base64.b64decode("SGVsbG8=")            # b"Hello"

base64.urlsafe_b64encode(b"Hello").decode()
base64.urlsafe_b64decode("SGVsbG8=")
```

## URL Encoding

### Encode and decode

```bash
python3 -c "from urllib.parse import quote; print(quote('hello world & foo=bar'))"

python3 -c "from urllib.parse import unquote; print(unquote('hello%20world%20%26%20foo%3Dbar'))"

curl -G --data-urlencode "q=hello world & more" https://api.example.com/search
```

### In code

```javascript
// JavaScript
encodeURIComponent('hello world & foo=bar');
// "hello%20world%20%26%20foo%3Dbar"

decodeURIComponent('hello%20world%20%26%20foo%3Dbar');
// "hello world & foo=bar"

// encodeURI vs encodeURIComponent:
encodeURI('https://example.com/path?q=hello world');
// "https://example.com/path?q=hello%20world" (preserves URL structure)
encodeURIComponent('https://example.com/path?q=hello world');
// "https%3A%2F%2Fexample.com%2Fpath%3Fq%3Dhello%20world" (encodes everything)
```

```python
from urllib.parse import quote, unquote, urlencode

quote('hello world')            # 'hello%20world'
unquote('hello%20world')        # 'hello world'
urlencode({'q': 'hello world', 'page': 1})  # 'q=hello+world&page=1'
```

## Hex

### View and convert

```bash
xxd file.bin | head -20
xxd -l 64 file.bin          # First 64 bytes only

xxd -p file.bin

echo "48656c6c6f" | xxd -r -p

od -A x -t x1z file.bin | head -20

hexdump -C file.bin | head -20

python3 -c "print(bytes.fromhex('48656c6c6f').decode())"  # Hello
python3 -c "print('Hello'.encode().hex())"                 # 48656c6c6f
```

### In code

```javascript
// JavaScript
Buffer.from('Hello').toString('hex');           // "48656c6c6f"
Buffer.from('48656c6c6f', 'hex').toString();    // "Hello"

// Number to hex
(255).toString(16);     // "ff"
parseInt('ff', 16);     // 255
```

```python
"Hello".encode().hex()                  # '48656c6c6f'
bytes.fromhex('48656c6c6f').decode()    # 'Hello'
hex(255)                                # '0xff'
int('ff', 16)                           # 255
```

## Unicode

### Inspect characters

```bash
echo -n "Hello 世界" | python3 -c "
import sys
for char in sys.stdin.read():
    print(f'U+{ord(char):04X}  {char}  {char.encode(\"utf-8\").hex()}')"

printf '\u0048\u0065\u006c\u006c\u006f'   # Hello
echo -e '\xE4\xB8\x96\xE7\x95\x8C'       # 世界

file -bi document.txt
```

### Encoding conversion

```bash
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
iconv -f UTF-16 -t UTF-8 input.txt > output.txt

iconv -l

python3 -c "
with open('latin1.txt', 'r', encoding='iso-8859-1') as f:
    content = f.read()
with open('utf8.txt', 'w', encoding='utf-8') as f:
    f.write(content)
"
```

### Common Unicode issues

```text
BOM (Byte Order Mark):
  UTF-8 BOM: EF BB BF at start of file
  Remove: sed -i '1s/^\xEF\xBB\xBF//' file.txt

Normalization (NFC vs NFD):
  "é" can be U+00E9 (one char) or U+0065 U+0301 (e + combining accent)
  Python: import unicodedata; unicodedata.normalize('NFC', text)

Mojibake (wrong encoding):
  "café" appears as "cafÃ©" → file is UTF-8 but read as Latin-1
  Fix: re-read with correct encoding
```

## JWT (JSON Web Tokens)

### Decode a JWT

```bash

TOKEN="[REDACTED]"

echo "$TOKEN" | cut -d. -f1 | tr '-_' '+/' | base64 -d 2>/dev/null | jq

echo "$TOKEN" | cut -d. -f2 | tr '-_' '+/' | base64 -d 2>/dev/null | jq

jwt_decode() {
    echo "$1" | cut -d. -f2 | tr '-_' '+/' | base64 -d 2>/dev/null | jq
}
jwt_decode "$TOKEN"
```

### In code

```javascript
// JavaScript (no library needed for decoding)
function decodeJWT(token) {
    const [header, payload] = token.split('.').slice(0, 2)
        .map(part => JSON.parse(atob(part.replace(/-/g, '+').replace(/_/g, '/'))));
    return { header, payload };
}

// Check expiry
function isJWTExpired(token) {
    const { payload } = decodeJWT(token);
    return payload.exp && payload.exp < Math.floor(Date.now() / 1000);
}
```

```python
import json, base64

def decode_jwt(token):
    parts = token.split('.')
    # Add padding
    def pad(s): return s + '=' * (4 - len(s) % 4)
    header = json.loads(base64.urlsafe_b64decode(pad(parts[0])))
    payload = json.loads(base64.urlsafe_b64decode(pad(parts[1])))
    return header, payload

header, payload = decode_jwt(token)
```

## Hashing

### Common hash functions

```bash
echo -n "Hello" | md5sum        # Linux
echo -n "Hello" | md5           # macOS

echo -n "Hello" | sha256sum
echo -n "Hello" | shasum -a 256

echo -n "Hello" | sha1sum

echo -n "Hello" | sha512sum

sha256sum file.bin
md5sum file.bin

echo -n "Hello" | openssl dgst -sha256
openssl dgst -sha256 file.bin
```

### In code

```javascript
// Node.js
const crypto = require('crypto');
crypto.createHash('sha256').update('Hello').digest('hex');
// "185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969"

// File hash
const fs = require('fs');
const hash = crypto.createHash('sha256');
hash.update(fs.readFileSync('file.bin'));
console.log(hash.digest('hex'));
```

```python
import hashlib
hashlib.sha256(b"Hello").hexdigest()

with open("file.bin", "rb") as f:
    print(hashlib.sha256(f.read()).hexdigest())
```

### Checksums for file integrity

```bash
sha256sum *.tar.gz > checksums.sha256

sha256sum -c checksums.sha256

sha256sum file1.bin file2.bin
cmp file1.bin file2.bin && echo "Identical" || echo "Different"
```

## Serialization Formats

### JSON ↔ other formats

```bash
python3 -c "import json, yaml, sys; yaml.dump(json.load(sys.stdin), sys.stdout)" < data.json

python3 -c "import json, yaml, sys; json.dump(yaml.safe_load(sys.stdin), sys.stdout, indent=2)" < data.yaml

jq -r '.[] | [.id, .name, .email] | @csv' data.json > data.csv

python3 -c "
import csv, json, sys
reader = csv.DictReader(open(sys.argv[1]))
print(json.dumps(list(reader), indent=2))
" data.csv

python3 -c "import json, tomli_w, sys; tomli_w.dump(json.load(sys.stdin), sys.stdout.buffer)" < data.json

jq '.' data.json
python3 -m json.tool data.json
```

### Binary formats (inspection)

```bash
python3 -c "
import msgpack, json, sys
data = msgpack.unpackb(sys.stdin.buffer.read(), raw=False)
print(json.dumps(data, indent=2))
" < data.msgpack

protoc --decode_raw < data.pb

python3 -c "
import cbor2, json, sys
data = cbor2.loads(sys.stdin.buffer.read())
print(json.dumps(data, indent=2, default=str))
" < data.cbor
```

## Quick Decode Script

```bash
#!/bin/bash
INPUT="${1:-$(cat)}"

B64_DECODED=$(echo "$INPUT" | base64 -d 2>/dev/null)
if [[ $? -eq 0 && -n "$B64_DECODED" ]]; then
    echo "Base64 → $B64_DECODED"
fi

if echo "$INPUT" | grep -q '%[0-9A-Fa-f]\{2\}'; then
    URL_DECODED=$(python3 -c "from urllib.parse import unquote; print(unquote('$INPUT'))" 2>/dev/null)
    echo "URL   → $URL_DECODED"
fi

if echo "$INPUT" | grep -qP '^eyJ[A-Za-z0-9_-]+\.eyJ[A-Za-z0-9_-]+\.'; then
    echo "JWT header:"
    echo "$INPUT" | cut -d. -f1 | tr '-_' '+/' | base64 -d 2>/dev/null | jq
    echo "JWT payload:"
    echo "$INPUT" | cut -d. -f2 | tr '-_' '+/' | base64 -d 2>/dev/null | jq
fi

if echo "$INPUT" | grep -qP '^[0-9a-fA-F]+$' && [[ $((${#INPUT} % 2)) -eq 0 ]]; then
    HEX_DECODED=$(echo "$INPUT" | xxd -r -p 2>/dev/null)
    if [[ -n "$HEX_DECODED" ]]; then
        echo "Hex   → $HEX_DECODED"
    fi
fi
```

## Tips

* Base64 increases data size by ~33%. Use it for embedding binary data in text formats (JSON, XML, email), not for compression or encryption.
* Base64url (RFC 4648) uses `-` and `_` instead of `+` and `/`, and omits padding `=`. JWTs and URL parameters use this variant.
* SHA-256 is the standard for integrity checks. MD5 is fine for dedup and non-security checksums but broken for cryptographic use.
* JWTs are signed, not encrypted. Anyone can decode the header and payload. Only the signature verifies authenticity. Never put secrets in JWT claims.
* When files display garbled text (mojibake), the problem is almost always wrong encoding assumption. Check with `file -bi` and re-read with the correct encoding.
* `xxd -p` (plain hex) and `xxd -r -p` (reverse) are the fastest way to convert between binary and hex on the command line.
* URL-encode with `encodeURIComponent` (JavaScript) or `urllib.parse.quote` (Python), not by hand. Manual encoding misses edge cases.

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

- Encode, decode, and convert between data formats
- Use when working with
  Base64, URL encoding, hex
- 触发关键词: encoding, convert, decode, formats, data, between, encode

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

### Q1: 如何开始使用Encoding & Formats？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Encoding & Formats有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
