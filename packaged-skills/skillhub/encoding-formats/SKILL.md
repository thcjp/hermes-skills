---
slug: "encoding-formats"
name: "encoding-formats"
version: 1.0.1
displayName: "编码格式工具"
summary: "编码解码与数据格式转换，覆盖Base64、URL编码、Hex、Unicode、JWT、哈希、序列化。编码解码与数据格式转换工具，覆盖Base64、URL编码、Hex、Unicode、JWT解"
license: "MIT"
description: |-
  编码解码与数据格式转换工具，覆盖Base64、URL编码、Hex、Unicode、JWT解码、
  哈希校验和序列化格式转换。支持命令行和代码两种方式，适用于API响应解码、
  HTTP请求参数编码、二进制数据检查、JWT令牌分析、文件完整性校验等场景.
tools:
  - read
  - exec
  - glob
  - grep
homepage: ""
tags:
  - 通用办公
  - 工具
  - 效率
  - 安全
  - base64
  - bash
  - url
  - hello
  - jwt
category: "Automation"
---
# 编码格式工具

编码、解码和检查常见数据格式。覆盖Base64、URL编码、Hex、Unicode、JWT、哈希校验和序列化格式.
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---|---|---|---|
| input | string | 是 | 编码格式工具处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|:-----|:-----|:-----|
| 基础功能 | 支持 | 支持 |
| 编码格式工具码解码与数据格式转换 | 不支持 | 支持 |
| 代码静态分析与质量评分 | 不支持 | 支持 |
| 依赖漏洞检测与升级建议 | 不支持 | 支持 |
| 批量代码审查与报告生成 | 不支持 | 支持 |
| CI/CD流水线集成 | 不支持 | 支持 |

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|---:|---:|---:|---:|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
如需调用外部API，请参考环境配置章节设置对应密钥

### 可用性分类
- **分类**: MD+EXEC（）

**API Key配置方式**:
```bash
export API_KEY="your_api_key_here"
```
配置后需重启会话或开启新终端生效。API Key应妥善保管,避免泄露到版本控制系统.
## 核心能力

### 1. Base64编码解码
支持标准Base64和URL安全Base64（RFC 4648）变体。Base64使数据增大约33%，适用于在文本格式中嵌入二进制数据.
```bash
echo -n "Hello, World!" | base64
# 输出: SGVsbG8sIFdvcmxkIQ==
# ...
echo "SGVsbG8sIFdvcmxkIQ==" | base64 -d
# 输出: Hello, World!
# ...
# URL安全变体
echo -n "Hello" | base64 | tr '+/' '-_' | tr -d '='
```- 验证返回数据的完整性和格式正确性
- 参考`Base64编码解码`的配置文档进行参数调优
### 2. URL编码解码
对HTTP请求参数进行编码，处理特殊字符和空格.
```bash
python3 -c "from urllib.parse import quote; print(quote('hello world & foo=bar'))"
# 输出: hello%20world%20%26%20foo%3Dbar
# ...
python3 -c "from urllib.parse import unquote; print(unquote('hello%20world%20%26%20foo%3Dbar'))"
# 输出: hello world & foo=bar
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `url编码解码` 选项
- 处理流程: 接收输入 -> 执行URL编码解码 -> 返回结果
- 输入: 用户提供URL编码解码所需的参数和指令
- 输出: 返回URL编码解码的处理结果,包含执行状态码、结果数据和执行日志

### 3. Hex查看与转换
查看二进制文件的十六进制转储，在Hex和文本之间转换.
```bash
xxd -p file.bin          # 纯Hex输出
xxd -l 64 file.bin       # 前64字节
echo "48656c6c6f" | xxd -r -p   # Hex转文本: Hello
```

**输入**: 用户提供Hex查看与转换所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `hex查看与转换` 选项

### 4. Unicode检查与编码转换
检查字符的Unicode码点，在不同编码间转换.
```bash
iconv -f ISO-8859-1 -t UTF-8 input.txt > output.txt
file -bi document.txt     # 检测文件编码
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `unicode检查与编码转换` 选项
- 处理流程: 接收输入 -> 执行Unicode检查与编码转换 -> 返回结果
- 输入: 用户提供Unicode检查与编码转换所需的参数和指令
- 输出: 返回Unicode检查与编码转换的处理结果,包含执行状态码、结果数据和执行日志

### 5. JWT解码
解码JWT令牌的header和payload（JWT是签名而非加密，任何人可解码）.
```bash
TOKEN="eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIn0.SflKxwRJSMeKKF2QT4fwpMeJf36POk6yJV_adQssw5c"
echo "$TOKEN" | cut -d. -f2 | tr '-_' '+/' | base64 -d 2>/dev/null | jq
# 输出: {"sub": "1234567890", "name": "John Doe"}
```

**输入**: 用户提供JWT解码所需的指令和必要参数.
**处理**: 解析JWT解码的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `jwt解码` 选项

### 6. 哈希与校验和
计算和验证文件哈希，用于完整性检查.
```bash
echo -n "Hello" | sha256sum
# 输出: 185f8db32271fe25f561a6fc938b2e264306ec304eda518007d1764826381969
# ...
sha256sum *.tar.gz > checksums.sha256
sha256sum -c checksums.sha256    # 验证
```

**输入**: 用户提供哈希与校验和所需的指令和必要参数。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `哈希与校验和` 选项

### 7. 序列化格式转换
在JSON、YAML、CSV、TOML、MessagePack、CBOR等格式间转换.
```bash
python3 -c "import json, yaml, sys; yaml.dump(json.load(sys.stdin), sys.stdout)" < data.json
jq -r '.[] | [.id, .name, .email] | @csv' data.json > data.csv
protoc --decode_raw < data.pb    # Protobuf解码
```

**输入**: 用户提供序列化格式转换所需的指令和必要参数.
**输出**: 返回序列化格式转换的处理结果,包含执行状态码、结果数据和执行日志.
#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 使用流程

1. **环境确认**: 确认Agent平台已加载本skill，检查依赖说明中的环境要求
2. **指令输入**: 向Agent描述需要执行的任务，引用`encoding-formats`的相关能力
3. **执行处理**: Agent按照核心能力章节的指令执行任务
4. **结果验证**: 检查输出结果是否符合预期，参考错误处理章节处理异常

#
## 真实示例

### 示例1：解码API响应中的Base64图片

```bash
base64 -d image.b64 > image.png
# 将Base64编码的图片数据解码并保存为PNG文件
```

### 示例2：URL编码搜索参数

```bash
curl -G --data-urlencode "q=hello world & more" https://api.example.com/search
# 正确编码空格和特殊字符，发送HTTP GET请求
```

### 示例3：检查JWT令牌是否过期

```python
import json, base64, time
# ...
token = "eyJhbGciOiJIUzI1NiJ9.eyJleHAiOjk3NDI0Mjg4MDB9.signature"
payload_b64 = token.split('.')[1]
# 添加padding
padded = payload_b64 + '=' * (4 - len(payload_b64) % 4)
payload = json.loads(base64.urlsafe_b64decode(padded))
is_expired = payload.get('exp', 0) < time.time()
print(f"Expired: {is_expired}")
# 输出: Expired: False
```

### 示例4：验证文件完整性

```bash
sha256sum file.bin
# 输出: 3a7bd8e1c4f2b9a6e8d5c1f4b7a2e9d6c3f8b1a4e7d2c9f6b3a8e1d5c4f7b2a9  file.bin
# ...
sha256sum -c checksums.sha256
# 输出: file.bin: OK
```

### 示例5：修复Mojibake（乱码）

```bash
# "café" 显示为 "café" → 文件是UTF-8但被当作Latin-1读取
file -bi document.txt
# 输出: text/plain; charset=iso-8859-1
iconv -f UTF-8 -t ISO-8859-1 document.txt 2>/dev/null | iconv -f UTF-8 -t UTF-8
# 或重新用正确编码读取
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| Base64解码失败 | 输入包含非Base64字符或padding错误 | 检查输入是否为有效Base64，添加 `=` padding |
| Mojibake（乱码） | 文件编码假设错误 | 用 `file -bi` 检测实际编码，用 `iconv` 转换 |
| JWT解码返回乱码 | Base64url使用 `-` 和 `_` 而非 `+` 和 `/` | 先 `tr '-_' '+/'` 转换再解码，添加padding |
| BOM导致解析错误 | UTF-8 BOM（`EF BB BF`）在文件开头 | 用 `sed -i '1s/^\xEF\xBB\xBF//' file.txt` 移除 |
| Hex转换失败 | 奇数长度Hex字符串 | 确保Hex字符串长度为偶数，每两个字符代表一个字节 |
| sha256sum不匹配 | 文件内容被修改或传输损坏 | 重新下载或传输文件，再次验证 |
| `encodeURI` vs `encodeURIComponent`混用 | `encodeURI`保留URL结构字符 | URL参数用 `encodeURIComponent`，完整URL用 `encodeURI` |

## 常见问题

### Q1: Base64使数据增大多少？
A: Base64使数据增大约33%（每3字节编码为4字符）。适用于在JSON、XML、邮件等文本格式中嵌入二进制数据，不适用于压缩或加密.
### Q2: Base64url和标准Base64有什么区别？
A: Base64url（RFC 4648）使用 `-` 和 `_` 替代 `+` 和 `/`，并省略padding `=`。JWT和URL参数使用此变体。转换方法：`tr '+/' '-_'` 和 `tr -d '='`.
### Q3: JWT是加密的吗？
A: JWT是签名的，不是加密的。任何人都可以解码header和payload。只有签名用于验证真实性。切勿在JWT claims中放置敏感信息.
### Q4: SHA-256和MD5应该用哪个？
A: SHA-256是完整性检查的标准。MD5适用于去重和非安全校验和，但在密码学上已被破解，不应用于安全场景.
### Q5: 如何处理UTF-8 BOM问题？
A: UTF-8 BOM是文件开头的 `EF BB BF` 三字节。某些解析器会将其误认为内容。移除方法：`sed -i '1s/^\xEF\xBB\xBF//' file.txt`。检测方法：`hexdump -C file.txt | head -1`.
### Q6: NFC和NFD归一化有什么区别？
A: "é" 可以是单个字符 U+00E9（NFC）或 e + 组合重音 U+0065 U+0301（NFD）。Python中用 `unicodedata.normalize('NFC', text)` 统一。数据库和搜索通常需要统一归一化形式.
### Q7: 如何快速判断字符串是什么编码？
A: 使用 `file -bi filename` 检测文件编码。对于字符串，尝试UTF-8解码，失败则尝试Latin-1。乱码几乎总是编码假设错误导致.
## 已知限制

- Base64不提供压缩或加密功能，仅做编码转换
- JWT解码不需要密钥，但验证签名需要密钥
- `xxd -p` 和 `xxd -r -p` 是命令行最快的二进制与Hex互转方式
- URL编码应使用 `encodeURIComponent`（JS）或 `urllib.parse.quote`（Python），不要手动编码
- Protobuf解码需要 `protoc --decode_raw`，且结果可能不完整
- 跨平台哈希命令不同：Linux用 `sha256sum`，macOS用 `shasum -a 256`

## 输出格式

```json
{
  "success": true,
  "data": {
    "result": "编码格式工具处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "encoding-formats"
    }
  },
  "execution_log": [
    "解析输入参数",
    "执行核心处理",
    "格式化输出结果"
  ],
  "error": null
}
```
