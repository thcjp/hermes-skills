#!/usr/bin/env python3
"""
多源头发现系统 (v34.0 Task 6 - Step 1)
======================================
扩展 auto_discover.py，新增 N8N / Dify / Coze / Hermes / AwesomeList 五个源头扫描器，
并扩展 GitHub 扫描器支持关键词搜索（按 star 数排序，top 50 仓库）。

所有扫描器统一输出到: d:\\skills\\data\\discovery\\candidates_unified.json
格式: [{source, source_id, name, description, category, content_preview, url, metadata}, ...]
扫描结果记录到数据库 sources 表。

用法:
  python multi_source_discover.py --all              # 运行所有扫描器
  python multi_source_discover.py --source n8n       # 仅运行 n8n 扫描器
  python multi_source_discover.py --source dify      # 仅运行 dify 扫描器
  python multi_source_discover.py --source coze      # 仅运行 coze 扫描器
  python multi_source_discover.py --source hermes    # 仅运行 hermes 扫描器
  python multi_source_discover.py --source awesome   # 仅运行 awesome-list 扫描器
  python multi_source_discover.py --source github    # 仅运行扩展 github 扫描器
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DB_PATH, DATA_DIR
# === End Phase 1 ===


import argparse
import json
import sqlite3
import os
import sys
import re
import time
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Set, Tuple

# ============================================================
# 复用 auto_discover 的函数（网络请求必须复用 fetch_url）
# ============================================================

_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)

from auto_discover import (
    fetch_url,            # 统一网络请求函数
    deduplicate,          # 去重比对
    ensure_dir,           # 确保发现目录存在
    get_existing_slugs,   # 获取本地DB已有slug
    get_existing_source_slugs,  # 获取已有source_slug
    get_existing_display_names, # 获取已有display_name
    scan_github_repo,     # 扫描单个GitHub仓库（保留以供需要时使用）
    get_db,               # 获取数据库连接
)
from platform_config import GITHUB_SCAN_REPOS

# ============================================================
# 配置
# ============================================================

# DB_PATH imported from config
DISCOVERY_DIR = DATA_DIR / "discovery"
CANDIDATES_UNIFIED_FILE = DISCOVERY_DIR / "candidates_unified.json"

# Hermes GitHub 仓库
HERMES_GITHUB_OWNER = "thcjp"
HERMES_GITHUB_REPO = "hermes-skills"

# GitHub 搜索关键词（扩展）
GITHUB_SEARCH_KEYWORDS = [
    "ai agent",
    "llm tool",
    "ai workflow",
    "claude skill",
    "gpt skill",
]
GITHUB_SEARCH_PER_PAGE = 10  # 5 关键词 × 10 = top 50

# Awesome list 仓库
AWESOME_LIST_REPOS = [
    {"owner": "e2b-dev", "repo": "awesome-ai-agents"},
    {"owner": "Shubhamsaboo", "repo": "awesome-llm-apps"},
    # MCP 生态相关 awesome-list
    {"owner": "punkpeye", "repo": "awesome-mcp-servers"},
    {"owner": "punkpeye", "repo": "fastmcp"},
    {"owner": "modelcontextprotocol", "repo": "servers"},
]

# N8N API (公开无需认证，但响应慢，需60s超时; categories=25为AI分类)
# 注意: api.n8n.io 位于 Cloudflare 后方，可能因 bot 防护导致请求超时（socket 超时是按操作计而非按请求计，
# Cloudflare 可能缓慢滴答数据使每次 recv 都在超时窗口内，导致实际耗时远超设定值）
N8N_API_URLS = [
    "https://api.n8n.io/api/templates/workflows?skip=0&limit=50",
]
N8N_CATEGORIES_URL = "https://api.n8n.io/api/templates/categories"
N8N_FETCH_TIMEOUT = 10  # N8N API被Cloudflare拦截，socket超时按操作计，实际耗时远超此值

# Dify (Explore API需要session cookie认证，暂不可用)
# 备选方案: 从 https://creators.dify.ai/ 获取或从Dify GitHub社区获取
DIFY_EXPLORE_URL = "https://cloud.dify.ai/explore"
DIFY_API_URLS = [
    "https://cloud.dify.ai/api/explore/apps",  # 需要认证
    "https://cloud.dify.ai/console/api/explore/apps",  # 需要认证
]

# Dify GitHub 社区仓库（Cloud API 需要认证时的备选数据源）
# 扫描这些仓库的目录结构，提取可作为 skill 候选的模板/插件
DIFY_GITHUB_REPOS = [
    # Dify 官方插件仓库（tools, agent-strategies, datasources, extensions, triggers 等分类目录）
    {"owner": "langgenius", "repo": "dify-official-plugins", "paths": ["tools", "agent-strategies", "datasources", "extensions", "triggers"]},
    # Dify 社区插件市场仓库（根目录包含大量社区插件，435+）
    {"owner": "langgenius", "repo": "dify-plugins", "paths": [""]},
    # Dify 主仓库内置工具提供者目录
    {"owner": "langgenius", "repo": "dify", "paths": ["api/core/tools/builtin_tool/providers"]},
]

# Coze (Store API需要登录认证，返回 code:700012006)
# 备选方案: 使用headless browser爬取 https://www.coze.cn/store/bot
COZE_STORE_URL = "https://www.coze.cn/store/bot"
COZE_API_URLS = [
    "https://www.coze.cn/api/store/bot/list",  # 需要认证
    "https://api.coze.cn/api/store/bot/list",  # 需要认证
]


# ============================================================
# 辅助函数
# ============================================================

def categorize(name: str, description: str) -> str:
    """根据名称和描述推断分类"""
    text = f"{name} {description}".lower()
    category_keywords: Dict[str, List[str]] = {
        'Development': [
            'code', 'github', 'git', 'docker', 'kubernetes', 'api', 'programming',
            'build', 'deploy', 'compiler', 'lint', 'test', 'debug', 'refactor',
            'python', 'javascript', 'typescript', 'rust', 'java', 'sql', 'npm',
            'pip', 'package', 'framework', 'library', 'sdk', 'cli',
        ],
        'Creative': [
            'image', 'video', 'music', 'art', 'design', 'draw', 'paint', 'media',
            'photo', 'audio', 'podcast', 'gif', 'logo', 'banner', 'poster',
            'animation', 'render', '3d', 'canvas', 'figma',
        ],
        'Research': [
            'search', 'research', 'analyze', 'data', 'paper', 'study', 'arxiv',
            'scholar', 'literature', 'survey', 'citation', 'embedding',
        ],
        'Automation': [
            'workflow', 'automate', 'schedule', 'pipeline', 'cron', 'n8n',
            'integration', 'sync', 'trigger', 'zapier', 'ifttt', 'bot',
        ],
        'Productivity': [
            'task', 'todo', 'calendar', 'email', 'note', 'document', 'reminder',
            'planner', 'project', 'kanban', 'notion', 'obsidian', 'spreadsheet',
        ],
        'Communication': [
            'chat', 'message', 'slack', 'discord', 'telegram', 'wechat',
            'notification', 'alert', 'sms', 'email', 'feishu', 'lark',
        ],
        'Agents': [
            'agent', 'assistant', 'copilot', 'gpt', 'llm', 'autonomous',
            'reasoning', 'planning', 'rag', 'chain-of-thought', 'prompt',
        ],
        'Knowledge': [
            'knowledge', 'wiki', 'docs', 'rag', 'vector', 'memory',
            'graph', 'semantic', 'embedding', 'database', 'index',
        ],
        'Security': [
            'security', 'vulnerability', 'pentest', 'audit', 'firewall',
            'crypto', 'encrypt', 'auth', 'password', 'malware', 'cve',
        ],
        'Finance': [
            'finance', 'trading', 'stock', 'crypto', 'payment', 'invoice',
            'accounting', 'bank', 'portfolio', 'forex', 'bitcoin',
        ],
        'Operations': [
            'monitor', 'log', 'server', 'cloud', 'devops', 'infrastructure',
            'container', 'nginx', 'aws', 'azure', 'gcp', 'kubernetes',
        ],
        'Lifestyle': [
            'recipe', 'weather', 'travel', 'fitness', 'health', 'game',
            'movie', 'book', 'news', 'shopping', 'food', 'sport',
        ],
    }
    for category, keywords in category_keywords.items():
        if any(kw in text for kw in keywords):
            return category
    return 'Other'


def record_source_to_db(candidate: Dict[str, Any]) -> bool:
    """将发现的候选项记录到数据库 sources 表"""
    try:
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()

        # 检查是否已存在（按 source_type + original_slug 去重）
        c.execute(
            "SELECT id FROM sources WHERE source_type = ? AND original_slug = ?",
            (candidate.get('source', ''), candidate.get('source_id', ''))
        )
        existing = c.fetchone()
        if existing:
            conn.close()
            return False

        metadata = candidate.get('metadata', {})
        c.execute("""
            INSERT INTO sources (
                source_type, source_name, source_url, source_author,
                source_license, source_version, download_date, original_slug, notes
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            candidate.get('source', ''),
            candidate.get('name', ''),
            candidate.get('url', ''),
            metadata.get('author', ''),
            metadata.get('license', ''),
            metadata.get('version', ''),
            datetime.now().isoformat(),
            candidate.get('source_id', ''),
            json.dumps(metadata, ensure_ascii=False),
        ))
        conn.commit()
        conn.close()
        return True
    except Exception as e:
        print(f"  [DB ERROR] 记录 source 失败: {e}")
        return False


def save_unified(candidates: List[Dict[str, Any]]):
    """保存统一格式的候选列表"""
    ensure_dir()
    output = {
        'generated_at': datetime.now().isoformat(),
        'total_count': len(candidates),
        'candidates': candidates,
    }
    with open(CANDIDATES_UNIFIED_FILE, 'w', encoding='utf-8') as f:
        json.dump(output, f, ensure_ascii=False, indent=2)
    print(f"\n统一候选列表已保存: {CANDIDATES_UNIFIED_FILE}")
    print(f"总计 {len(candidates)} 个候选项")


# ============================================================
# 基础扫描器类
# ============================================================

class BaseScanner:
    """所有扫描器的基类，提供统一输出格式"""
    source_name = 'base'

    def scan(self) -> List[Dict[str, Any]]:
        """执行扫描，返回候选列表"""
        raise NotImplementedError

    def make_candidate(
        self,
        source_id: str,
        name: str,
        description: str,
        category: str,
        content_preview: str,
        url: str,
        metadata: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """构造统一格式的候选项"""
        return {
            'source': self.source_name,
            'source_id': str(source_id),
            'name': name or '',
            'description': (description or '')[:500],
            'category': category or 'Other',
            'content_preview': (content_preview or '')[:500],
            'url': url or '',
            'metadata': metadata or {},
            'discovered_at': datetime.now().isoformat(),
        }


# ============================================================
# 1. N8N 工作流模板市场扫描器
# ============================================================

class N8NScanner(BaseScanner):
    """扫描 https://n8n.io/workflows/ 模板市场，提取可转化为 skill 的自动化场景"""
    source_name = 'n8n'

    def scan(self) -> List[Dict[str, Any]]:
        candidates: List[Dict[str, Any]] = []
        print("\n[N8NScanner] 扫描 N8N 工作流模板市场...")

        # 尝试多个 API 端点 (N8N API响应极慢，需60秒超时)
        # 使用自带诊断的请求方法，避免 fetch_url 静默吞掉异常
        data = None
        for url in N8N_API_URLS:
            content = self._fetch_with_diagnostics(url, N8N_FETCH_TIMEOUT)
            if not content:
                continue
            try:
                data = json.loads(content)
                if data:
                    print(f"  [N8N] 成功获取数据 (HTTP 200, {len(content)} bytes): {url}")
                    break
            except json.JSONDecodeError as e:
                print(f"  [N8N] 响应非 JSON 格式 ({e}): {url}")
                continue

        if not data:
            print("  [N8N] 所有 API 端点均无法访问（网络超时或被 Cloudflare 拦截），跳过 N8N 扫描")
            print("  [N8N] 诊断: api.n8n.io 位于 Cloudflare 后方，可能因 bot 防护导致请求超时")
            return candidates

        # 解析工作流模板列表
        workflows: List[Dict[str, Any]] = []
        if isinstance(data, dict):
            if 'data' in data and isinstance(data['data'], list):
                workflows = data['data']
            elif 'workflows' in data and isinstance(data['workflows'], list):
                workflows = data['workflows']
            elif 'items' in data and isinstance(data['items'], list):
                workflows = data['items']
        elif isinstance(data, list):
            workflows = data

        print(f"  [N8N] 发现 {len(workflows)} 个工作流模板")

        for wf in workflows:
            if not isinstance(wf, dict):
                continue

            wf_id = wf.get('id', '')
            name = wf.get('name', wf.get('title', ''))
            description = wf.get('description', '')

            if not name:
                continue

            # 提取节点信息
            nodes = wf.get('nodes', [])
            nodes_count = len(nodes) if isinstance(nodes, list) else 0
            node_types: List[str] = []
            if isinstance(nodes, list):
                for node in nodes:
                    if isinstance(node, dict):
                        ntype = node.get('type', '')
                        if ntype:
                            node_types.append(ntype)

            # 提取分类信息
            wf_categories: List[str] = []
            cats = wf.get('categories', [])
            if isinstance(cats, list):
                for cat in cats:
                    if isinstance(cat, dict):
                        wf_categories.append(cat.get('name', ''))
                    elif isinstance(cat, str):
                        wf_categories.append(cat)

            category = categorize(name, description + ' ' + ' '.join(node_types))

            content_preview = (
                f"工作流: {name}\n"
                f"节点数: {nodes_count}\n"
                f"节点类型: {', '.join(node_types[:10])}\n"
                f"描述: {description[:200]}"
            )

            # 提取作者
            author = ''
            user = wf.get('user')
            if isinstance(user, dict):
                author = user.get('name', user.get('username', ''))

            candidate = self.make_candidate(
                source_id=wf_id,
                name=name,
                description=description,
                category=category,
                content_preview=content_preview,
                url=f"https://n8n.io/workflows/{wf_id}" if wf_id else "https://n8n.io/workflows/",
                metadata={
                    'nodes_count': nodes_count,
                    'node_types': node_types[:15],
                    'categories': wf_categories,
                    'author': author,
                    'source_platform': 'n8n',
                },
            )
            candidates.append(candidate)

        print(f"  [N8N] 提取 {len(candidates)} 个候选")
        return candidates

    def _fetch_with_diagnostics(self, url: str, timeout: int) -> Optional[str]:
        """带诊断信息的 HTTP 请求，捕获并打印具体异常类型（超时/HTTP错误/网络错误）

        与 fetch_url 不同，此方法不会静默吞掉异常，
        而是打印具体的失败原因，便于排查 N8N API 连接问题。

        使用线程级总超时：urllib 的 socket timeout 是按操作计（per-recv），
        无法应对 Cloudflare 缓慢滴答数据的行为（每次 recv 都在超时窗口内，
        但总耗时远超设定值）。因此用 concurrent.futures 实现硬性总超时。
        """
        import urllib.request
        import urllib.error
        import socket as _socket
        from concurrent.futures import ThreadPoolExecutor, TimeoutError as _FutTimeout

        def _do_fetch() -> str:
            req = urllib.request.Request(url, headers={
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
                'Accept': 'application/json',
            })
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read().decode('utf-8', errors='replace')

        try:
            with ThreadPoolExecutor(max_workers=1) as executor:
                future = executor.submit(_do_fetch)
                return future.result(timeout=timeout + 5)
        except _FutTimeout:
            print(f"  [N8N] 请求总超时 ({timeout}s, Cloudflare 滴答数据): {url}")
            return None
        except _socket.timeout:
            print(f"  [N8N] socket 超时 ({timeout}s): {url}")
            return None
        except urllib.error.HTTPError as e:
            print(f"  [N8N] HTTP {e.code} {e.reason}: {url}")
            return None
        except urllib.error.URLError as e:
            reason = str(e.reason)
            print(f"  [N8N] URL错误 ({reason}): {url}")
            return None
        except Exception as e:
            print(f"  [N8N] 请求异常 ({type(e).__name__}: {e}): {url}")
            return None


# ============================================================
# 2. Dify 模板市场扫描器
# ============================================================

class DifyScanner(BaseScanner):
    """扫描 https://cloud.dify.ai/explore 模板市场，提取可转化为 skill 的对话场景"""
    source_name = 'dify'

    def scan(self) -> List[Dict[str, Any]]:
        candidates: List[Dict[str, Any]] = []
        print("\n[DifyScanner] 扫描 Dify 模板市场...")

        # 尝试多个 API 端点
        data = None
        for url in DIFY_API_URLS:
            content = fetch_url(url, timeout=10)
            if not content:
                print(f"  [Dify] 无法获取数据: {url}")
                continue
            try:
                data = json.loads(content)
                if data:
                    print(f"  [Dify] 成功获取数据: {url}")
                    break
            except json.JSONDecodeError:
                # 可能是 HTML 页面，尝试从中提取嵌入的 JSON 数据
                print(f"  [Dify] 响应非 JSON，尝试解析 HTML: {url}")
                html_candidates = self._parse_html_for_data(content, url)
                if html_candidates:
                    candidates.extend(html_candidates)
                    data = None  # 标记已从HTML提取
                    break
                continue

        if data is not None:
            # 解析模板列表
            templates: List[Dict[str, Any]] = []
            if isinstance(data, dict):
                if 'data' in data and isinstance(data['data'], list):
                    templates = data['data']
                elif 'apps' in data and isinstance(data['apps'], list):
                    templates = data['apps']
                elif 'items' in data and isinstance(data['items'], list):
                    templates = data['items']
                elif 'templates' in data and isinstance(data['templates'], list):
                    templates = data['templates']
            elif isinstance(data, list):
                templates = data

            print(f"  [Dify] 发现 {len(templates)} 个模板")

            for tpl in templates:
                if not isinstance(tpl, dict):
                    continue

                tpl_id = tpl.get('id', tpl.get('app_id', tpl.get('slug', '')))
                name = tpl.get('name', tpl.get('title', ''))
                description = tpl.get('description', tpl.get('desc', ''))

                if not name:
                    continue

                # 提取模型信息
                model = ''
                model_config = tpl.get('model_config')
                if isinstance(model_config, dict):
                    model = model_config.get('model', model_config.get('provider', ''))
                elif isinstance(model_config, str):
                    model = model_config
                if not model:
                    model = tpl.get('model', '')

                app_type = tpl.get('app_type', tpl.get('mode', tpl.get('type', '')))
                category = categorize(name, description)

                content_preview = (
                    f"模板: {name}\n"
                    f"类型: {app_type}\n"
                    f"模型: {model}\n"
                    f"描述: {description[:200]}"
                )

                candidate = self.make_candidate(
                    source_id=tpl_id,
                    name=name,
                    description=description,
                    category=category,
                    content_preview=content_preview,
                    url=f"https://cloud.dify.ai/explore/{tpl_id}" if tpl_id else DIFY_EXPLORE_URL,
                    metadata={
                        'model': model,
                        'app_type': app_type,
                        'author': tpl.get('author', ''),
                        'source_platform': 'dify',
                    },
                )
                candidates.append(candidate)

        if not candidates:
            print("  [Dify] Cloud API 需要认证，尝试从 Dify GitHub 社区获取...")
            github_candidates = self._scan_github_community()
            candidates.extend(github_candidates)

        print(f"  [Dify] 提取 {len(candidates)} 个候选")
        return candidates

    def _parse_html_for_data(self, html: str, base_url: str) -> List[Dict[str, Any]]:
        """尝试从 HTML 页面中提取嵌入的 JSON 数据（如 Next.js __NEXT_DATA__）"""
        candidates: List[Dict[str, Any]] = []

        # 查找 __NEXT_DATA__ 脚本标签
        matches = re.findall(
            r'<script[^>]*id="__NEXT_DATA__"[^>]*>(.*?)</script>',
            html, re.DOTALL
        )
        for match in matches:
            try:
                data = json.loads(match)
                found = self._extract_templates_from_data(data, depth=0)
                for tpl in found:
                    if isinstance(tpl, dict) and tpl.get('name'):
                        tpl_id = tpl.get('id', tpl.get('app_id', ''))
                        name = tpl.get('name', '')
                        description = tpl.get('description', '')
                        candidate = self.make_candidate(
                            source_id=tpl_id,
                            name=name,
                            description=description,
                            category=categorize(name, description),
                            content_preview=str(tpl)[:500],
                            url=base_url,
                            metadata={'source_platform': 'dify', 'raw': tpl},
                        )
                        candidates.append(candidate)
            except json.JSONDecodeError:
                continue

        return candidates

    def _extract_templates_from_data(self, data: Any, depth: int) -> List[Dict[str, Any]]:
        """递归查找数据结构中的模板/应用列表"""
        if depth > 6:
            return []
        results: List[Dict[str, Any]] = []
        if isinstance(data, dict):
            for key in ('apps', 'templates', 'data', 'items', 'list', 'explore_apps'):
                val = data.get(key)
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, dict) and item.get('name'):
                            results.append(item)
            for v in data.values():
                if isinstance(v, (dict, list)):
                    results.extend(self._extract_templates_from_data(v, depth + 1))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    results.extend(self._extract_templates_from_data(item, depth + 1))
        return results

    def _scan_github_community(self) -> List[Dict[str, Any]]:
        """从 Dify GitHub 社区仓库获取模板/插件目录作为候选

        当 Cloud API 需要认证无法使用时，此方法作为备选数据源：
        - langgenius/dify: 检查 templates/、workflows/ 等目录
        - weixians/dify-plugins: 扫描根目录和 plugins/ 目录
        """
        candidates: List[Dict[str, Any]] = []
        seen_paths: Set[str] = set()

        for repo_config in DIFY_GITHUB_REPOS:
            owner = repo_config['owner']
            repo = repo_config['repo']
            paths = repo_config.get('paths', [''])

            for path in paths:
                # 构造 GitHub Contents API URL
                path_query = f"/{path}" if path else ""
                api_url = (
                    f"https://api.github.com/repos/{owner}/{repo}/contents{path_query}"
                )
                print(f"  [Dify-GitHub] 获取目录列表: {owner}/{repo}/{path or '(root)'}")
                content = fetch_url(api_url, timeout=15)
                if not content:
                    print(f"  [Dify-GitHub] 无法获取: {owner}/{repo}/{path or '(root)'}")
                    continue

                try:
                    items = json.loads(content)
                except json.JSONDecodeError:
                    print(f"  [Dify-GitHub] JSON 解析失败: {owner}/{repo}/{path or '(root)'}")
                    continue

                if not isinstance(items, list):
                    # 可能是单文件或 404
                    if isinstance(items, dict) and items.get('message'):
                        print(f"  [Dify-GitHub] {items.get('message')}: {owner}/{repo}/{path or '(root)'}")
                    continue

                # 筛选目录（模板/插件通常以目录形式存在）
                dirs = [
                    item for item in items
                    if isinstance(item, dict) and item.get('type') == 'dir'
                ]
                print(f"  [Dify-GitHub] {owner}/{repo}/{path or '(root)'}: {len(dirs)} 个目录")

                for d in dirs:
                    name = d.get('name', '')
                    if not name:
                        continue

                    # 跳过常见基础设施/构建目录（非模板/插件）
                    skip_names = {
                        '.github', '.git', '.gitignore', 'node_modules', '__pycache__',
                        '.vscode', '.idea', '.assets', '.claude', '.difyignore',
                        '.devcontainer', '.gemini', '.vite-hooks', '.agents',
                        'tests', 'docs', 'CONTRIBUTING.md', 'LICENSE', 'README.md',
                    }
                    if name.lower() in skip_names:
                        continue

                    source_id = f"{owner}/{repo}/{path}/{name}" if path else f"{owner}/{repo}/{name}"
                    if source_id in seen_paths:
                        continue
                    seen_paths.add(source_id)

                    html_url = d.get('html_url', '')
                    display_name = name.replace('-', ' ').replace('_', ' ').title()
                    category = categorize(name, display_name)
                    content_preview = (
                        f"来源: {owner}/{repo}\n"
                        f"路径: {path or '(root)'}/{name}\n"
                        f"类型: Dify GitHub 社区模板/插件"
                    )

                    candidate = self.make_candidate(
                        source_id=source_id,
                        name=display_name,
                        description=f"Dify 社区模板: {name} (from {owner}/{repo})",
                        category=category,
                        content_preview=content_preview,
                        url=html_url or f"https://github.com/{owner}/{repo}/tree/main/{path}/{name}" if path else f"https://github.com/{owner}/{repo}/tree/main/{name}",
                        metadata={
                            'source_repo': f"{owner}/{repo}",
                            'source_platform': 'dify-github',
                            'original_path': f"{path}/{name}" if path else name,
                        },
                    )
                    candidates.append(candidate)

                # GitHub API 速率限制（未认证 60 次/小时）
                time.sleep(1)

        print(f"  [Dify-GitHub] 从 GitHub 社区提取 {len(candidates)} 个候选")
        return candidates


# ============================================================
# 3. Coze 商店扫描器
# ============================================================

class CozeScanner(BaseScanner):
    """扫描 https://www.coze.cn/store/bot 商店，提取可转化为 skill 的中文场景"""
    source_name = 'coze'

    def scan(self) -> List[Dict[str, Any]]:
        candidates: List[Dict[str, Any]] = []
        print("\n[CozeScanner] 扫描 Coze 商店...")

        # 尝试多个 API 端点
        data = None
        for url in COZE_API_URLS:
            content = fetch_url(url, timeout=10)
            if not content:
                print(f"  [Coze] 无法获取数据: {url}")
                continue
            try:
                data = json.loads(content)
                if data:
                    print(f"  [Coze] 成功获取数据: {url}")
                    break
            except json.JSONDecodeError:
                print(f"  [Coze] 响应非 JSON，尝试解析 HTML: {url}")
                html_candidates = self._parse_html_for_data(content, url)
                if html_candidates:
                    candidates.extend(html_candidates)
                    data = None
                    break
                continue

        if data is not None:
            # 解析 bot 列表
            bots: List[Dict[str, Any]] = []
            if isinstance(data, dict):
                # Coze API 可能有多种返回格式
                for key in ('data', 'bots', 'bot_list', 'items', 'list'):
                    val = data.get(key)
                    if isinstance(val, list):
                        bots = val
                        break
                    elif isinstance(val, dict):
                        for sub_key in ('bots', 'bot_list', 'items', 'list'):
                            sub_val = val.get(sub_key)
                            if isinstance(sub_val, list):
                                bots = sub_val
                                break
                        if bots:
                            break
            elif isinstance(data, list):
                bots = data

            print(f"  [Coze] 发现 {len(bots)} 个 bot")

            for bot in bots:
                if not isinstance(bot, dict):
                    continue

                bot_id = bot.get('bot_id', bot.get('id', bot.get('bot_id_str', '')))
                name = bot.get('name', bot.get('title', ''))
                description = bot.get('description', bot.get('desc', bot.get('bot_intro', '')))

                if not name:
                    continue

                category = categorize(name, description)
                bot_type = bot.get('bot_type', bot.get('type', ''))
                publish_status = bot.get('publish_status', bot.get('status', ''))

                content_preview = (
                    f"Bot: {name}\n"
                    f"类型: {bot_type}\n"
                    f"描述: {description[:200]}"
                )

                candidate = self.make_candidate(
                    source_id=bot_id,
                    name=name,
                    description=description,
                    category=category,
                    content_preview=content_preview,
                    url=f"https://www.coze.cn/store/bot/{bot_id}" if bot_id else COZE_STORE_URL,
                    metadata={
                        'bot_type': bot_type,
                        'publish_status': publish_status,
                        'author': bot.get('author', bot.get('creator', '')),
                        'source_platform': 'coze',
                    },
                )
                candidates.append(candidate)

        if not candidates:
            print("  [Coze] 所有端点均无法访问或未提取到数据，跳过 Coze 扫描")

        print(f"  [Coze] 提取 {len(candidates)} 个候选")
        return candidates

    def _parse_html_for_data(self, html: str, base_url: str) -> List[Dict[str, Any]]:
        """尝试从 HTML 页面中提取嵌入的 JSON 数据"""
        candidates: List[Dict[str, Any]] = []

        # 查找各种嵌入 JSON 的方式
        patterns = [
            r'<script[^>]*id="__NEXT_DATA__"[^>]*>(.*?)</script>',
            r'window\.__INITIAL_STATE__\s*=\s*(\{.*?\});',
            r'window\.__NUXT__\s*=\s*(\{.*?\});',
        ]
        for pattern in patterns:
            matches = re.findall(pattern, html, re.DOTALL)
            for match in matches:
                try:
                    data = json.loads(match)
                    found = self._extract_bots_from_data(data, depth=0)
                    for bot in found:
                        if isinstance(bot, dict) and bot.get('name'):
                            bot_id = bot.get('bot_id', bot.get('id', ''))
                            name = bot.get('name', '')
                            description = bot.get('description', '')
                            candidate = self.make_candidate(
                                source_id=bot_id,
                                name=name,
                                description=description,
                                category=categorize(name, description),
                                content_preview=str(bot)[:500],
                                url=base_url,
                                metadata={'source_platform': 'coze', 'raw': bot},
                            )
                            candidates.append(candidate)
                except (json.JSONDecodeError, TypeError):
                    continue

        return candidates

    def _extract_bots_from_data(self, data: Any, depth: int) -> List[Dict[str, Any]]:
        """递归查找数据结构中的 bot 列表"""
        if depth > 6:
            return []
        results: List[Dict[str, Any]] = []
        if isinstance(data, dict):
            for key in ('bots', 'bot_list', 'data', 'items', 'list', 'store_bots'):
                val = data.get(key)
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, dict) and item.get('name'):
                            results.append(item)
            for v in data.values():
                if isinstance(v, (dict, list)):
                    results.extend(self._extract_bots_from_data(v, depth + 1))
        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    results.extend(self._extract_bots_from_data(item, depth + 1))
        return results


# ============================================================
# 4. Hermes 社区扫描器
# ============================================================

class HermesScanner(BaseScanner):
    """扫描已发布到 Hermes 的 skill（GitHub 仓库），交叉发现本地没有的

    优化: 只获取仓库目录列表(1次API调用), 不逐个获取SKILL.md,
    避免对759个目录发起1518个HTTP请求。
    """
    source_name = 'hermes'

    def scan(self) -> List[Dict[str, Any]]:
        candidates: List[Dict[str, Any]] = []
        print("\n[HermesScanner] 扫描 Hermes 社区仓库 (GitHub)...")

        # 通过 GitHub API 获取仓库根目录内容（1次API调用）
        api_url = f"https://api.github.com/repos/{HERMES_GITHUB_OWNER}/{HERMES_GITHUB_REPO}/contents/"
        print(f"  [Hermes] 获取仓库目录列表: {HERMES_GITHUB_OWNER}/{HERMES_GITHUB_REPO}")
        content = fetch_url(api_url, timeout=15)
        if not content:
            print(f"  [Hermes] 无法获取仓库内容，跳过 Hermes 扫描")
            return candidates

        try:
            items = json.loads(content)
        except json.JSONDecodeError:
            print(f"  [Hermes] 仓库内容 JSON 解析失败，跳过 Hermes 扫描")
            return candidates

        if not isinstance(items, list):
            print(f"  [Hermes] 仓库内容格式异常，跳过 Hermes 扫描")
            return candidates

        # 筛选目录（每个目录是一个 skill）
        dirs = [item for item in items if isinstance(item, dict) and item.get('type') == 'dir']
        print(f"  [Hermes] 仓库共 {len(dirs)} 个 skill 目录")

        # 获取本地已有的 slug 和 source_slug，进行交叉比对
        existing_slugs = get_existing_slugs()
        existing_source_slugs = get_existing_source_slugs()

        new_count = 0
        dup_count = 0
        for d in dirs:
            slug = d.get('name', '')
            if not slug:
                continue

            # 交叉比对：本地是否已有
            if slug in existing_slugs or slug in existing_source_slugs:
                dup_count += 1
                continue

            new_count += 1
            # 从 slug 生成可读名称
            display_name = slug.replace('-', ' ').replace('-free', '').strip().title()
            html_url = d.get('html_url', f"https://github.com/{HERMES_GITHUB_OWNER}/{HERMES_GITHUB_REPO}/tree/main/{slug}")
            category = categorize(slug, display_name)

            candidate = self.make_candidate(
                source_id=slug,
                name=display_name,
                description=f"Hermes 社区 skill: {slug}",
                category=category,
                content_preview=f"slug: {slug}\nrepo: {HERMES_GITHUB_OWNER}/{HERMES_GITHUB_REPO}\nurl: {html_url}",
                url=html_url,
                metadata={
                    'source_repo': f"{HERMES_GITHUB_OWNER}/{HERMES_GITHUB_REPO}",
                    'source_platform': 'hermes',
                    'original_slug': slug,
                },
            )
            candidates.append(candidate)

        print(f"  [Hermes] 新发现 {new_count} 个，本地已存在 {dup_count} 个")
        return candidates


# ============================================================
# 5. Awesome List 扫描器
# ============================================================

class AwesomeListScanner(BaseScanner):
    """扫描 GitHub 上 awesome-ai-agents、awesome-llm-tools 等列表，提取工具/项目"""
    source_name = 'awesome-list'

    # 匹配 Markdown 列表项中的 GitHub 链接
    # 格式: - [Name](https://github.com/owner/repo) - Description
    GITHUB_LINK_PATTERN = re.compile(
        r'^\s*[-*+]\s*\[([^\]]+)\]\((https://github\.com/[^/]+/[^/)]+)\)\s*[-–—:|]?\s*(.*)$',
        re.MULTILINE
    )

    def scan(self) -> List[Dict[str, Any]]:
        candidates: List[Dict[str, Any]] = []
        print("\n[AwesomeListScanner] 扫描 GitHub awesome-lists...")

        for repo_config in AWESOME_LIST_REPOS:
            owner = repo_config['owner']
            repo = repo_config['repo']
            print(f"  [AwesomeList] 扫描: {owner}/{repo}")

            # 尝试获取 README.md
            readme_content = self._fetch_readme(owner, repo)
            if not readme_content:
                print(f"  [AwesomeList] 无法获取 README: {owner}/{repo}")
                continue

            # 解析 README 中的 GitHub 项目链接
            projects = self._parse_readme_links(readme_content)
            print(f"  [AwesomeList] 从 {owner}/{repo} 提取 {len(projects)} 个项目")

            for proj in projects:
                name = proj['name']
                url = proj['url']
                description = proj['description']
                # 从 URL 提取 owner/repo 作为 source_id
                match = re.match(r'https://github\.com/([^/]+/[^/]+)', url)
                source_id = match.group(1) if match else url

                category = categorize(name, description)
                content_preview = (
                    f"项目: {name}\n"
                    f"URL: {url}\n"
                    f"描述: {description[:200]}"
                )

                candidate = self.make_candidate(
                    source_id=source_id,
                    name=name,
                    description=description,
                    category=category,
                    content_preview=content_preview,
                    url=url,
                    metadata={
                        'list_repo': f"{owner}/{repo}",
                        'source_platform': 'awesome-list',
                    },
                )
                candidates.append(candidate)

        print(f"  [AwesomeList] 总计提取 {len(candidates)} 个候选")
        return candidates

    def _fetch_readme(self, owner: str, repo: str) -> Optional[str]:
        """获取仓库的 README.md 内容"""
        # 尝试多种 README 文件名和分支
        readme_urls = [
            f"https://raw.githubusercontent.com/{owner}/{repo}/main/README.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/master/README.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/main/readme.md",
            f"https://raw.githubusercontent.com/{owner}/{repo}/master/readme.md",
        ]
        for url in readme_urls:
            content = fetch_url(url, timeout=10)
            if content and len(content) > 100:
                return content
        return None

    def _parse_readme_links(self, readme: str) -> List[Dict[str, str]]:
        """解析 README 中的 GitHub 项目链接"""
        projects: List[Dict[str, str]] = []
        seen_urls: Set[str] = set()

        for match in self.GITHUB_LINK_PATTERN.finditer(readme):
            name = match.group(1).strip()
            url = match.group(2).strip().rstrip('/')
            description = match.group(3).strip()

            # 去除描述中的多余标记
            description = re.sub(r'^[-–—:|\s]+', '', description).strip()

            # 跳过非项目链接（如仓库自身 owner 的 profile）
            if url in seen_urls:
                continue
            seen_urls.add(url)

            projects.append({
                'name': name,
                'url': url,
                'description': description,
            })

        return projects


# ============================================================
# 6. 扩展 GitHub 扫描器（关键词搜索 + 现有仓库）
# ============================================================

class ExtendedGitHubScanner(BaseScanner):
    """
    扩展 GitHub 扫描器：
    1. 新增搜索关键词: ai agent, llm tool, ai workflow, claude skill, gpt skill
    2. 按 star 数排序，扫描 top 50 仓库
    3. 同时包含现有配置的 GitHub 仓库扫描
    """
    source_name = 'github-search'

    def scan(self) -> List[Dict[str, Any]]:
        candidates: List[Dict[str, Any]] = []
        print("\n[ExtendedGitHubScanner] 扫描 GitHub（关键词搜索 + 现有仓库）...")

        # Part 1: 扫描现有配置的 GitHub 仓库（仅获取目录列表，不逐个获取SKILL.md）
        print("  [GitHub] Part 1: 扫描现有配置仓库...")
        try:
            for repo_config in GITHUB_SCAN_REPOS:
                owner = repo_config['owner']
                repo = repo_config['repo']
                license_str = repo_config.get('license', '')
                print(f"    获取目录列表: {owner}/{repo}")
                api_url = f"https://api.github.com/repos/{owner}/{repo}/contents/"
                content = fetch_url(api_url, timeout=15)
                if not content:
                    print(f"    无法获取: {owner}/{repo}")
                    continue
                try:
                    items = json.loads(content)
                except json.JSONDecodeError:
                    print(f"    JSON解析失败: {owner}/{repo}")
                    continue
                if not isinstance(items, list):
                    continue

                dirs = [item for item in items if isinstance(item, dict) and item.get('type') == 'dir']
                print(f"    {owner}/{repo}: {len(dirs)} 个目录")

                for d in dirs:
                    slug = d.get('name', '')
                    if not slug:
                        continue
                    display_name = slug.replace('-', ' ').title()
                    html_url = d.get('html_url', f"https://github.com/{owner}/{repo}/tree/main/{slug}")
                    category = categorize(slug, display_name)

                    candidate = self.make_candidate(
                        source_id=f"{owner}/{repo}/{slug}",
                        name=display_name,
                        description=f"GitHub skill: {slug} (from {owner}/{repo})",
                        category=category,
                        content_preview=f"slug: {slug}\nrepo: {owner}/{repo}\nlicense: {license_str}",
                        url=html_url,
                        metadata={
                            'source_repo': f"{owner}/{repo}",
                            'source_platform': 'github',
                            'original_slug': slug,
                            'license': license_str,
                        },
                    )
                    candidates.append(candidate)
        except Exception as e:
            print(f"  [GitHub] 现有仓库扫描失败: {e}")

        # Part 2: 关键词搜索 GitHub（按 star 数排序，top 50）
        print("  [GitHub] Part 2: 关键词搜索 GitHub...")
        search_candidates = self._search_github_keywords()
        candidates.extend(search_candidates)

        print(f"  [GitHub] 总计提取 {len(candidates)} 个候选")
        return candidates

    def _search_github_keywords(self) -> List[Dict[str, Any]]:
        """使用 GitHub Search API 按关键词搜索仓库"""
        candidates: List[Dict[str, Any]] = []
        seen_repos: Set[str] = set()

        for keyword in GITHUB_SEARCH_KEYWORDS:
            print(f"    搜索关键词: \"{keyword}\"...")
            query = keyword.replace(' ', '+')
            search_url = (
                f"https://api.github.com/search/repositories?"
                f"q={query}&sort=stars&order=desc&per_page={GITHUB_SEARCH_PER_PAGE}"
            )

            content = fetch_url(search_url, timeout=10)
            if not content:
                print(f"    无法获取搜索结果: \"{keyword}\"")
                continue

            try:
                data = json.loads(content)
            except json.JSONDecodeError:
                print(f"    搜索结果 JSON 解析失败: \"{keyword}\"")
                continue

            items = data.get('items', []) if isinstance(data, dict) else []
            if not items:
                print(f"    未找到结果: \"{keyword}\"")
                continue

            print(f"    获取 {len(items)} 个仓库")

            for item in items:
                if not isinstance(item, dict):
                    continue

                full_name = item.get('full_name', '')
                if not full_name or full_name in seen_repos:
                    continue
                seen_repos.add(full_name)

                name = item.get('name', full_name)
                description = item.get('description', '') or ''
                html_url = item.get('html_url', f"https://github.com/{full_name}")
                stars = item.get('stargazers_count', 0)
                language = item.get('language', '') or ''
                topics = item.get('topics', []) or []
                license_info = item.get('license')
                license_name = ''
                if isinstance(license_info, dict):
                    license_name = license_info.get('spdx_id', license_info.get('name', ''))

                category = categorize(name, description + ' ' + language + ' ' + ' '.join(topics))

                content_preview = (
                    f"仓库: {full_name}\n"
                    f"Stars: {stars}\n"
                    f"语言: {language}\n"
                    f"License: {license_name}\n"
                    f"描述: {description[:200]}\n"
                    f"Topics: {', '.join(topics[:10])}"
                )

                candidate = self.make_candidate(
                    source_id=full_name,
                    name=name,
                    description=description,
                    category=category,
                    content_preview=content_preview,
                    url=html_url,
                    metadata={
                        'stars': stars,
                        'language': language,
                        'license': license_name,
                        'topics': topics[:15],
                        'search_keyword': keyword,
                        'source_platform': 'github-search',
                        'repo_full_name': full_name,
                    },
                )
                candidates.append(candidate)

            # 避免 GitHub Search API 速率限制（未认证 10 次/分钟）
            time.sleep(2)

        return candidates


# ============================================================
# 多源头发现主类
# ============================================================

class MultiSourceDiscover:
    """多源头发现系统主控制器"""

    def __init__(self):
        self.scanners: Dict[str, BaseScanner] = {
            'n8n': N8NScanner(),
            'dify': DifyScanner(),
            'coze': CozeScanner(),
            'hermes': HermesScanner(),
            'awesome': AwesomeListScanner(),
            'github': ExtendedGitHubScanner(),
        }

    def scan_all(self) -> List[Dict[str, Any]]:
        """运行所有扫描器"""
        print("=" * 70)
        print("多源头发现系统 - 全量扫描")
        print("=" * 70)

        all_candidates: List[Dict[str, Any]] = []

        for name, scanner in self.scanners.items():
            try:
                candidates = scanner.scan()
                all_candidates.extend(candidates)

                # 记录到数据库 sources 表
                db_count = 0
                for c in candidates:
                    if record_source_to_db(c):
                        db_count += 1
                print(f"  [{name}] 发现 {len(candidates)} 个候选，记录 {db_count} 条到 DB")

            except Exception as e:
                print(f"  [{name}] 扫描异常: {e}")
                import traceback
                traceback.print_exc()
                continue

        # 按 (source, source_id) 去重
        all_candidates = self._deduplicate(all_candidates)

        # 保存统一输出
        save_unified(all_candidates)

        # 打印汇总
        self._print_summary(all_candidates)

        return all_candidates

    def scan_source(self, source_name: str) -> List[Dict[str, Any]]:
        """运行指定扫描器"""
        if source_name not in self.scanners:
            print(f"未知扫描器: {source_name}")
            print(f"可用扫描器: {', '.join(self.scanners.keys())}")
            return []

        print("=" * 70)
        print(f"多源头发现系统 - 单源扫描: {source_name}")
        print("=" * 70)

        scanner = self.scanners[source_name]
        candidates: List[Dict[str, Any]] = []

        try:
            candidates = scanner.scan()

            # 记录到数据库
            db_count = 0
            for c in candidates:
                if record_source_to_db(c):
                    db_count += 1
            print(f"  [{source_name}] 发现 {len(candidates)} 个候选，记录 {db_count} 条到 DB")

        except Exception as e:
            print(f"  [{source_name}] 扫描异常: {e}")
            import traceback
            traceback.print_exc()

        # 去重
        candidates = self._deduplicate(candidates)

        # 保存
        save_unified(candidates)

        # 汇总
        self._print_summary(candidates)

        return candidates

    def _deduplicate(self, candidates: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        """按 (source, source_id) 去重"""
        seen: Set[Tuple[str, str]] = set()
        result: List[Dict[str, Any]] = []
        for c in candidates:
            key = (c.get('source', ''), c.get('source_id', ''))
            if key in seen:
                continue
            seen.add(key)
            result.append(c)
        if len(result) < len(candidates):
            print(f"\n去重: {len(candidates)} -> {len(result)}（移除 {len(candidates) - len(result)} 个重复）")
        return result

    def _print_summary(self, candidates: List[Dict[str, Any]]):
        """打印扫描结果汇总"""
        print("\n" + "=" * 70)
        print("扫描结果汇总")
        print("=" * 70)

        if not candidates:
            print("\n  未发现任何候选")
            return

        by_source: Dict[str, int] = {}
        by_category: Dict[str, int] = {}
        for c in candidates:
            source = c.get('source', 'unknown')
            category = c.get('category', 'Other')
            by_source[source] = by_source.get(source, 0) + 1
            by_category[category] = by_category.get(category, 0) + 1

        print("\n按来源统计:")
        for source, count in sorted(by_source.items(), key=lambda x: -x[1]):
            print(f"  {source:20s}: {count:>4d}")

        print(f"\n总计: {len(candidates)} 个候选")

        print("\n按分类统计:")
        for category, count in sorted(by_category.items(), key=lambda x: -x[1]):
            print(f"  {category:20s}: {count:>4d}")

        print(f"\n输出文件: {CANDIDATES_UNIFIED_FILE}")


# ============================================================
# CLI 入口
# ============================================================

def main():
    parser = argparse.ArgumentParser(
        description='多源头发现系统 - 扫描 N8N/Dify/Coze/Hermes/AwesomeList/GitHub 等多平台来源',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python multi_source_discover.py --all              # 运行所有扫描器
  python multi_source_discover.py --source n8n       # 仅运行 N8N 扫描器
  python multi_source_discover.py --source dify      # 仅运行 Dify 扫描器
  python multi_source_discover.py --source coze      # 仅运行 Coze 扫描器
  python multi_source_discover.py --source hermes    # 仅运行 Hermes 扫描器
  python multi_source_discover.py --source awesome   # 仅运行 AwesomeList 扫描器
  python multi_source_discover.py --source github    # 仅运行扩展 GitHub 扫描器
        """,
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument('--all', action='store_true',
                       help='运行所有扫描器')
    group.add_argument('--source', type=str,
                       choices=['n8n', 'dify', 'coze', 'hermes', 'awesome', 'github'],
                       help='仅运行指定扫描器')

    args = parser.parse_args()

    discoverer = MultiSourceDiscover()

    if args.all:
        discoverer.scan_all()
    elif args.source:
        discoverer.scan_source(args.source)


if __name__ == '__main__':
    main()
