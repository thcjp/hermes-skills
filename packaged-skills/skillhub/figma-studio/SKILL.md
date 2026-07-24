---

slug: "figma-studio"
name: "figma-studio"
version: 1.0.1
displayName: "Figma工作室(专业版)"
summary: "企业级Figma设计协作工具，支持批量导出、Webhook管理、设计变更监控与团队资源治理。。Figma工作室专业版是一款面向设计团队与企业级设计工程化场景的全功能Figma协作工具。在免费"
license: "Proprietary"
edition: "pro"
description: |-，可生成提升工作效率
  Figma工作室专业版是一款面向设计团队与企业级设计工程化场景的全功能Figma协作工具。在免费版的文件读取、评论管理、图片导出、设计令牌提取基础上，新增批量导出、Webhook管理、设计变更监控、团队资源治理、设计令牌转Tailwind与设计版本对比六大高级能力，覆盖从单文件读取到企业级设计系统治理的全场景需求
tags:
  - 设计协作
  - 设计工程化
  - 企业工具
  - 工具
  - 效率
  - 自动化
  - 开发
  - 代码
  - 集成
  - integration
  - 创意
tools:
  - read
  - exec
  - write
homepage: ""
# 定价元数据
category: "Automation"

---

# Figma工作室(专业版)

## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| Figma工作室(专业版)支持批量导出 | 不支持 | 支持 |
| Figma工作室(专业版)Webhook管理 | 不支持 | 支持 |
| Figma工作室(专业版)设计变更监控 | 不支持 | 支持 |
| 高清分辨率与无损输出 | 不支持 | 支持 |
| 批量生成与风格预设 | 不支持 | 支持 |

## 核心能力

### 能力1：批量并行导出
| 模式 | 适用场景 | 并发策略 |
|:-----|:-----|:-----|
| 单节点导出 | 调试期、单次任务 | 单请求 |
| 批量节点导出 | 10+节点 | 每批50个，并行下载 |
| 全文件导出 | 整文件所有节点 | 递归收集+分批请求+8线程下载 |
| 多文件导出 | 多个Figma文件 | 文件级并行+节点级并行 |

**Agent执行规则**：Figma API单次导出请求最多50个节点；下载用8线程并行；输出每个节点的下载状态与耗时；失败节点重试3次。- 验证返回数据的完整性和格式正确性
- 参考`能力6：设计版本对比`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`能力5：设计令牌转Tailwind`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`能力4：团队资源治理`的配置文档进行参数调优- 验证返回数据的完整性和格式正确性
- 参考`能力3：设计变更监控`的配置文档进行参数调优
### 能力2：Webhook全生命周期管理
```python
def list_webhooks(team_id: str) -> list:
    """列出团队所有Webhook"""
    resp = requests.get(f'{FIGMA_BASE}/teams/{team_id}/webhooks', headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json().get('webhooks', [])
# ...
def update_webhook(webhook_id: str, status: str = 'ACTIVE', endpoint: str = None):
    """更新Webhook状态或端点"""
    payload = {'status': status}  # ACTIVE / PAUSED
    if endpoint:
        payload['endpoint'] = endpoint
    resp = requests.put(f'{FIGMA_BASE}/webhooks/{webhook_id}',
                        headers={**headers, 'Content-Type': 'application/json'},
                        json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()
# ...
def delete_webhook(webhook_id: str):
    """删除Webhook"""
    resp = requests.delete(f'{FIGMA_BASE}/webhooks/{webhook_id}', headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.status_code == 200
# ...
def get_webhook_requests(webhook_id: str):
    """查询Webhook请求历史（最近7天）"""
    resp = requests.get(f'{FIGMA_BASE}/webhooks/{webhook_id}/requests', headers=headers, timeout=30)
    resp.raise_for_status()
    return resp.json().get('requests', [])
```

**支持的事件类型**：`FILE_UPDATE`（文件更新）、`FILE_COMMENT`（评论）、`FILE_DELETE`（文件删除）、`FILE_VERSION_UPDATE`（版本更新）、`LIBRARY_PUBLISH`（库发布）、`LIBRARY_DELETE`（库删除）.
**处理**: 解析能力2：Webhook全生命周期管理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态.
### 能力3：设计变更监控
```python
import hashlib, json, time
from pathlib import Path
# ...
STATE_FILE = '.figma_watch_state.json'
# ...
def watch_file_changes(file_key: str, callback_url: str = None):
    """监控Figma文件变更"""
    state = load_state()
    last_version = state.get(file_key, {}).get('version')
# ...
    resp = requests.get(f'{FIGMA_BASE}/files/{file_key}/metadata', headers=headers, timeout=30)
    resp.raise_for_status()
    meta = resp.json()
    current_version = meta['version']
# ...
    if last_version and current_version != last_version:
        change = {
            'file_key': file_key,
            'old_version': last_version,
            'new_version': current_version,
            'last_modified': meta['lastModified'],
            'detected_at': time.time()
        }
        if callback_url:
            requests.post(callback_url, json=change, timeout=10)
        state[file_key] = {'version': current_version, 'last_checked': time.time()}
        save_state(state)
        return {'status': 'changed', 'change': change}
    else:
        state[file_key] = {'version': current_version, 'last_checked': time.time()}
        save_state(state)
        return {'status': 'unchanged'}
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力3：设计变更监控` 选项
- 处理流程: 接收输入 -> 执行能力3：设计变更监控 -> 返回结果
- 输入: 用户提供能力3：设计变更监控所需的参数和指令
- 输出: 返回能力3：设计变更监控的处理结果,包含执行状态码、结果数据和执行日志

### 能力4：团队资源治理
```python
def generate_team_asset_report(team_id: str) -> dict:
    """生成团队资产清单报告"""
    report = {'team_id': team_id, 'projects': [], 'libraries': [], 'components': 0, 'styles': 0}
# ...
    resp = requests.get(f'{FIGMA_BASE}/teams/{team_id}/projects', headers=headers, timeout=30)
    resp.raise_for_status()
    projects = resp.json().get('projects', [])
# ...
    for project in projects:
        proj_info = {'name': project['name'], 'id': project['id'], 'files': []}
        resp = requests.get(f'{FIGMA_BASE}/projects/{project["id"]}/files', headers=headers, timeout=30)
        resp.raise_for_status()
        files = resp.json().get('files', [])
        for f in files:
            proj_info['files'].append({'name': f['name'], 'key': f['key'], 'modified': f['last_modified']})
        report['projects'].append(proj_info)
# ...
    resp = requests.get(f'{FIGMA_BASE}/teams/{team_id}/components', headers=headers, timeout=30)
    resp.raise_for_status()
    report['components'] = len(resp.json().get('meta', {}).get('components', []))
# ...
    resp = requests.get(f'{FIGMA_BASE}/teams/{team_id}/styles', headers=headers, timeout=30)
    resp.raise_for_status()
    report['styles'] = len(resp.json().get('meta', {}).get('styles', []))
# ...
    return report
```

**处理**: 解析能力4：团队资源治理的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力4：团队资源治理` 选项
- 处理流程: 接收输入 -> 执行能力4：团队资源治理 -> 返回结果
- 输入: 用户提供能力4：团队资源治理所需的参数和指令
- 输出: 返回能力4：团队资源治理的处理结果,包含执行状态码、结果数据和执行日志

### 能力5：设计令牌转Tailwind
```python
def tokens_to_tailwind_config(file_key: str) -> str:
    """提取设计令牌并转为Tailwind CSS配置"""
    resp = requests.get(f'{FIGMA_BASE}/files/{file_key}/styles', headers=headers, timeout=30)
    resp.raise_for_status()
    styles = resp.json().get('meta', {}).get('styles', [])
# ...
    tokens = {'colors': {}, 'fontSize': {}, 'boxShadow': {}}
    for style in styles:
        node_id = style['node_id']
        r = requests.get(f'{FIGMA_BASE}/files/{file_key}/nodes',
                        headers=headers, params={'ids': node_id}, timeout=30)
        r.raise_for_status()
        node_data = r.json().get('nodes', {}).get(node_id, {}).get('document', {})
# ...
        style_type = style.get('style_type', '').lower()
        name = style['name'].lower().replace(' ', '-')
# ...
        if style_type == 'fill' and 'fills' in node_data:
            fill = node_data['fills'][0]
            if fill.get('type') == 'SOLID':
                color = fill['color']
                tokens['colors'][name] = f"rgb({int(color['r']*255)}, {int(color['g']*255)}, {int(color['b']*255)})"
        elif style_type == 'text':
            tokens['fontSize'][name] = node_data.get('style', {}).get('fontSize', 16)
        elif style_type == 'effect':
            tokens['boxShadow'][name] = '0 1px 2px rgba(0,0,0,0.1)'  # 简化示例
    config = f"""module.exports = {{
  theme: {{
    extend: {{
      colors: {json.dumps(tokens['colors'], indent=6)},
      fontSize: {json.dumps(tokens['fontSize'], indent=6)},
      boxShadow: {json.dumps(tokens['boxShadow'], indent=6)}
    }}
  }}
}}"""
    return config
```

**处理**: 解析能力5：设计令牌转Tailwind的输入参数,执行核心处理逻辑,返回结构化结果和执行状态。- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力5：设计令牌转tailwind` 选项
- 处理流程: 接收输入 -> 执行能力5：设计令牌转Tailwind -> 返回结果
- 输入: 用户提供能力5：设计令牌转Tailwind所需的参数和指令
- 输出: 返回能力5：设计令牌转Tailwind的处理结果,包含执行状态码、结果数据和执行日志

### 能力6：设计版本对比
```python
def compare_versions(file_key: str, old_version: str, new_version: str) -> dict:
    """对比两个版本的设计文件差异"""
    old_resp = requests.get(f'{FIGMA_BASE}/files/{file_key}',
                           headers=headers, params={'version': old_version}, timeout=60)
    new_resp = requests.get(f'{FIGMA_BASE}/files/{file_key}',
                           headers=headers, params={'version': new_version}, timeout=60)
    old_data = old_resp.json()
    new_data = new_resp.json()
# ...
    def collect_nodes(node, path=''):
        nodes = {}
        if 'id' in node:
            nodes[node['id']] = {
                'name': node.get('name', ''),
                'type': node.get('type', ''),
                'path': path
            }
        for child in node.get('children', []):
            nodes.update(collect_nodes(child, path + '/' + node.get('name', '')))
        return nodes
# ...
    old_nodes = collect_nodes(old_data['document'])
    new_nodes = collect_nodes(new_data['document'])
# ...
    added = {k: v for k, v in new_nodes.items() if k not in old_nodes}
    removed = {k: v for k, v in old_nodes.items() if k not in new_nodes}
    modified = {}
    for k, v in new_nodes.items():
        if k in old_nodes and old_nodes[k] != v:
            modified[k] = {'old': old_nodes[k], 'new': v}
# ...
    return {
        'file_key': file_key,
        'old_version': old_version,
        'new_version': new_version,
        'added': len(added),
        'removed': len(removed),
        'modified': len(modified),
        'details': {
            'added': list(added.values())[:20],
            'removed': list(removed.values())[:20],
            'modified': list(modified.values())[:20]
        }
    }
```- 验证执行结果,确认输出符合预期格式
- 异常时参考错误处理章节进行恢复
- 关键参数: `能力6：设计版本对比` 选项

#
## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

### 场景一：企业级设计系统治理（设计负责人角色）
**痛点**：团队组件库散乱，不知道有多少组件、哪些在用、哪些废弃.
**使用方式**：对Agent说"生成我们团队的设计资产清单报告"，Agent按本工具的团队资源治理模板输出报告，含项目数、文件数、组件数、样式数与详细清单.
**效果**：设计资产盘点从1周降至10分钟，治理有据可依.
### 场景二：设计变更驱动前端自动更新（前端架构师角色）
**痛点**：设计稿改了，前端不知道，导致设计与代码脱节.
**使用方式**：对Agent说"配置Webhook监听Figma文件变更，变更后自动触发前端构建"，Agent生成Webhook创建脚本+变更监控脚本+CI/CD触发脚本.
**效果**：设计变更从人工通知改为自动触发，设计与代码同步延迟从天级降至分钟级.
### 场景三：设计令牌工程化（前端工程师角色）
**痛点**：设计令牌（颜色、字体、阴影）散落在Figma，前端用Tailwind需要手抄，易错且不同步.
**使用方式**：对Agent说"读取Figma设计令牌并生成Tailwind配置"，Agent按本工具的令牌转换模板输出 `tailwind.config.js`，直接集成到前端项目.
**效果**：令牌同步从手抄30分钟降至脚本10秒，准确率100%.
### 场景四：设计版本审计与回滚（设计系统管理员角色）
**痛点**：设计系统迭代频繁，某次更新引入错误，要回滚到上一版本但不知道差异.
**使用方式**：对Agent说"对比当前版本与上一版本的差异"，Agent输出结构化diff报告，列出新增/删除/修改的节点，辅助决策回滚.
**效果**：版本审计从无记录改为有据可查，回滚决策从凭感觉改为看diff.
## 使用流程

### 60秒上手：批量导出+自动下载
直接对Agent说：

Agent会按本工具的批量导出模板输出：

```python
import requests, os, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
# ...
FIGMA_TOKEN = os.environ.get('FIGMA_ACCESS_TOKEN', '')
FIGMA_BASE = 'https://api.figma.com/v1'
headers = {'X-Figma-Token': FIGMA_TOKEN}
# ...
def batch_export_and_download(file_key: str, out_dir: str, format: str = 'svg'):
    """批量导出文件所有节点图片并自动下载"""
    resp = requests.get(f'{FIGMA_BASE}/files/{file_key}', headers=headers, timeout=60)
    resp.raise_for_status()
    file_data = resp.json()
# ...
    node_ids = []
    def collect_nodes(node, path=''):
        if 'id' in node:
            node_ids.append(node['id'])
        for child in node.get('children', []):
            collect_nodes(child, path + '/' + node.get('name', ''))
    for page in file_data['document']['children']:
        collect_nodes(page)
# ...
    Path(out_dir).mkdir(parents=True, exist_ok=True)
    all_images = {}
    for i in range(0, len(node_ids), 50):
        batch = node_ids[i:i+50]
        params = {'ids': ','.join(n.replace(':', '-') for n in batch), 'format': format}
        r = requests.get(f'{FIGMA_BASE}/images/{file_key}', headers=headers, params=params, timeout=60)
        r.raise_for_status()
        all_images.update(r.json().get('images', {}))
# ...
    def download_one(node_id: str, url: str):
        if not url:
            return None
        ext = 'svg' if format == 'svg' else format
        out_path = Path(out_dir) / f'{node_id.replace(":", "_")}.{ext}'
        r = requests.get(url, timeout=60)
        r.raise_for_status()
        out_path.write_bytes(r.content)
        return str(out_path)
# ...
    with ThreadPoolExecutor(max_workers=8) as pool:
        futures = [pool.submit(download_one, nid, url) for nid, url in all_images.items()]
        results = [f.result() for f in futures if f.result()]
# ...
    return {'total': len(node_ids), 'downloaded': len(results), 'output_dir': out_dir}
# ...
result = batch_export_and_download('ABC123xyz', './icons', 'svg')
print(f"导出完成：{result['downloaded']}/{result['total']} 个图标")
```

### 120秒上手：Webhook创建
```python
def create_figma_webhook(event_type: str, endpoint: str, file_key: str = None, team_id: str = None):
    """创建Figma Webhook"""
    payload = {
        'event_type': event_type,  # FILE_UPDATE, FILE_COMMENT, FILE_DELETE
        'endpoint': endpoint,
        'passcode': os.environ.get('FIGMA_WEBHOOK_PASSCODE', ''),
    }
    if file_key:
        payload['file_key'] = file_key
    if team_id:
        payload['team_id'] = team_id
    resp = requests.post(f'{FIGMA_BASE}/webhooks',
                         headers={**headers, 'Content-Type': 'application/json'},
                         json=payload, timeout=30)
    resp.raise_for_status()
    return resp.json()
# ...
webhook = create_figma_webhook(
    event_type='FILE_UPDATE',
    endpoint='https://your-server.com/webhooks/figma',
    file_key='ABC123xyz'
)
print(f"Webhook已创建，ID: {webhook['id']}")
```

#
## 输入格式

| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| content | string | 否 | figma-studio处理的内容输入 |,  |
| content | string | 否 | figma-studio处理的内容输入 |, 可选值: json/text/markdown |
| style | string | 否 | 输出风格, 参考 `references/style.md` |

## 输出格式

```json
{
  "success": true,
  "data": {
    result: "studio 相关配置参数",
    result: "studio 相关配置参数",
    result: "studio 相关配置参数",
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
|:---:|:---:|:---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+（推荐3.10+）
- **Node.js**: 16+（若使用Node.js模板）

### 依赖说明(补充)
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:------|------:|:------|:------|
| LLM API | API | 必需 | 由Agent平台内置LLM提供（专业版路由GPT-4o） |
| requests | Python库 | 必需 | `pip install requests`（HTTP调用） |
| Figma API | 外部API | 必需 | 需注册Figma账号并创建应用获取凭证 |
| Flask/FastAPI | Python库 | 可选 | `pip install flask` 或 `pip install fastapi`（Webhook服务端） |
| json | Python模块 | 必需 | Python标准库，无需安装 |

### API Key 配置
- Figma Personal Token：从Figma设置页生成，存入环境变量 `FIGMA_ACCESS_TOKEN`
- Figma OAuth2凭证：从Figma开发者后台创建应用获取，`CLIENT_ID`/`CLIENT_SECRET` 存入环境变量
- Webhook passcode：自定义随机字符串，存入环境变量 `FIGMA_WEBHOOK_PASSCODE`
- 凭证文件存入 `d:\skills\.secrets\figma.json`（已gitignore），脚本通过环境变量读取
- **禁止**：在SKILL.md或脚本中硬编码Token

### 可用性分类
- **分类**: MD+EXEC（）
- **说明**: 基于Markdown的AI Skill，通过自然语言指令驱动Agent生成可执行的企业级Figma协作流水线

## 案例展示

### 示例1：基础用法
```
直接对Agent说：
# ...
Agent会按本工具的批量导出模板输出：
# ...
```python
import requests, os, json
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

FIGMA_TOKEN = os.environ.get('FIGMA_ACCESS_TOKEN', '')
FIGMA_BASE = 'https://api.figma.com/v1'
headers = {'X-Figma-Token': FIGMA_TOKEN}

def batch_export_and_download(file_key: str, out_dir: str, format: str = 'svg'):
    """批量导出文件所有节点图片并自动下载"""
    # 1. 读取文件所有节点ID
    resp = requests
```
# ...
## 常见问题
# ...
### Q1：专业版能导出多少个节点？
专业版采用分批+并行，实测1000个节点可在5分钟内完成导出与下载。节点数超过1万时建议按页面拆分多次执行，避免单次任务过长.
# ...
### Q2：Webhook推送失败如何重试？
Figma官方对Webhook推送有内置重试机制（失败后间隔递增重试，最多5次）。专业版在服务端也提供失败队列与手动重试接口。Webhook请求历史可在 `/webhooks/{id}/requests` 查询.
# ...
### Q3：变更监控的频率如何设置？
Figma API对单文件的读取有速率限制（每分钟约30次）。专业版默认每5分钟轮询一次，可根据业务需求调整。若需实时性，建议用Webhook而非轮询.
# ...
### Q4：团队资源治理需要什么权限？
需要团队管理员权限。普通成员只能看到自己有权限的项目与文件。专业版的治理脚本会在权限不足时提示具体缺失的权限.
# ...
### Q5：设计令牌转Tailwind支持所有令牌类型吗？
支持颜色、字体大小、阴影、间距四类核心令牌。Figma的网格（Grid）令牌因Tailwind无对应概念，仅输出为注释。自定义令牌（如动画时长）需用专业版的自定义映射功能.
# ...
### Q6：版本对比能定位到具体字段变更吗？
能。专业版的深度对比模式可对比节点的 `fills`、`strokes`、`effects`、`style` 等字段，输出字段级diff。但深度对比需下载两次完整JSON，大文件较慢.
# ...
### Q7：专业版与免费版的脚本可以混用吗？
可以。专业版兼容免费版的所有模板，免费版的单文件读取脚本在专业版环境下可直接运行。反向不兼容：专业版的批量导出、Webhook、团队治理脚本依赖额外库与权限.
# ...
### Q8：批量导出时如何处理命名冲突？
专业版默认用 `node_id` 命名（如 `1_2.svg`），避免重名。若需用节点名命名，开启 `--use-names` 选项，遇到重名自动追加序号（如 `icon.svg`、`icon_2.svg`）.
# ...
### Q9：Webhook支持自签名证书吗？
支持。Figma Webhook端点要求HTTPS，但接受自签名证书。若企业内部用自签名CA，需在Figma Webhook配置中上传CA证书（联系Figma支持）.
# ...
### Q10：专业版如何与设计系统CI/CD集成？
专业版提供GitHub Actions与GitLab CI的集成模板：设计令牌变更后自动提交到代码仓库，触发前端构建。集成流程：Figma变更→Webhook→CI拉取令牌→生成Tailwind配置→提交PR→前端构建.
# ...
## 错误处理
# ...
# ...
| 错误场景(续)| 原因 | 处理方式 |
|----:|:----|----:|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | ，请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |
# ...
## 已知限制
# ...
- 需要API Key，无Key环境无法使用
# ...