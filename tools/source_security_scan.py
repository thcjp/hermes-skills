#!/usr/bin/env python3
"""
源Skill安全扫描器 (流水线 Step 1.5 — 差异化前安全预检)
=====================================================

在差异化(auto_differentiate.py)之前, 对源skill内容进行安全扫描。
核心原则: 我们的skill基于其他项目/别人的skill升级强化,
如果源skill本身有风险或安全隐患,必须先行规避。

扫描21项安全风险模式:
  --- 基础高风险模式 (v2.1, 来自29条安全审核失败分析) ---
  1. exec命令执行 (96.6%命中率)
  2. API密钥明文处理 (62.1%)
  3. 不可信外部API/域名 (51.7%)
  4. 引用不存在的脚本 (41.4%)
  5. 硬编码服务器地址/IP (27.6%)
  6. HTTP不安全通信 (20.7%)
  7. tools字段格式错误 (17.2%)
  8. 文件系统遍历风险 (17.2%)
  9. 敏感信息泄露 (13.8%)
  10. eval/代码注入 (10.3%)
  --- 科恩实验室 + 云鼎实验室特有检测 (v2.2新增) ---
  11. SSRF服务端请求伪造 (云鼎特有)
  12. 数据外泄风险 (云鼎特有)
  13. 混淆代码/编码载荷 (科恩特有)
  14. 反向Shell/Shell反弹 (科恩特有)
  15. 权限提升风险 (科恩特有)
  16. 加密货币挖矿 (云鼎特有)
  17. AI Prompt注入风险 (云鼎特有)
  18. 持久化/自启动 (科恩特有)
  19. 不安全反序列化 (科恩特有)
  20. 依赖混淆/供应链风险 (云鼎特有)
  --- 直接封禁 ---
  21. VPN/翻墙关键词 (直接封禁)

处理策略:
  - critical风险: 源skill不可用, 标记BLOCKED, 跳过差异化
  - high风险: 标记WARNING, 差异化时自动移除风险模式
  - medium风险: 标记NOTICE, 差异化时自动修复
  - 通过: 标记SAFE, 正常差异化

用法:
  python source_security_scan.py                          # 扫描所有候选
  python source_security_scan.py --limit 50               # 扫描前50个
  python source_security_scan.py --source hermes           # 只扫描hermes来源
  python source_security_scan.py --content "skill内容"     # 扫描指定文本
  python source_security_scan.py --json                    # 输出JSON
"""

import argparse
import json
import os
import re
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

# 复用 quality_gate.py 的安全模式定义
_sys_path = os.path.dirname(os.path.abspath(__file__))
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)

from quality_gate import (
    _SECURITY_RISK_PATTERNS,
    _VPN_BLOCKED_KEYWORDS,
    _check_security_risk_pattern,
    _check_vpn_keywords,
)

# 路径常量
DATA_DIR = Path(__file__).resolve().parent.parent / "data"
CANDIDATES_FILE = DATA_DIR / "discovery" / "candidates_unified.json"
SCAN_RESULTS_FILE = DATA_DIR / "source_security_scan_results.json"

# 风险级别 → 处理策略
RISK_ACTION_MAP = {
    'critical': 'BLOCKED',   # 源skill不可用,跳过差异化
    'high': 'WARNING',       # 差异化时自动移除风险模式
    'medium': 'NOTICE',      # 差异化时自动修复
    'low': 'SAFE',           # 无需处理
}


def scan_content(content: str) -> Dict[str, Any]:
    """扫描文本内容中的安全风险

    参数:
        content: 要扫描的文本内容(SKILL.md全文或源skill描述)

    返回:
        {
            'passed': bool,           # 是否通过安全检查
            'risk_level': str,        # overall/critical/high/medium/safe
            'action': str,            # BLOCKED/WARNING/NOTICE/SAFE
            'total_checks': int,
            'passed_checks': int,
            'failed_checks': int,
            'checks': [检查结果列表],
            'fixes_applied': [自动修复项],
        }
    """
    if not content:
        return {
            'passed': True,
            'risk_level': 'safe',
            'action': 'SAFE',
            'total_checks': 0,
            'passed_checks': 0,
            'failed_checks': 0,
            'checks': [],
            'fixes_applied': [],
        }

    # 处理BOM
    if content.startswith('\ufeff'):
        content = content[1:]

    # 解析frontmatter和body
    if content.startswith('---'):
        parts = re.split(r'^---\s*$', content, maxsplit=2, flags=re.MULTILINE)
        fm_str = parts[1] if len(parts) > 1 else ''
        body = parts[2] if len(parts) > 2 else ''
        full_text = fm_str + '\n' + body
    else:
        fm_str = ''
        body = content
        full_text = content

    # 执行21项安全检查
    checks = []
    for pattern_def in _SECURITY_RISK_PATTERNS:
        check_result = _check_security_risk_pattern(full_text, pattern_def)
        checks.append(check_result)

    # VPN关键词检查
    vpn_check = _check_vpn_keywords(full_text)
    checks.append(vpn_check)

    # 统计
    failed_checks = [c for c in checks if not c.get('passed')]
    passed_checks = [c for c in checks if c.get('passed')]

    # 确定整体风险级别
    if not failed_checks:
        risk_level = 'safe'
        action = 'SAFE'
    else:
        severities = [c.get('severity', 'medium') for c in failed_checks]
        if 'critical' in severities:
            risk_level = 'critical'
            action = 'BLOCKED'
        elif 'high' in severities:
            risk_level = 'high'
            action = 'WARNING'
        elif 'medium' in severities:
            risk_level = 'medium'
            action = 'NOTICE'
        else:
            risk_level = 'low'
            action = 'SAFE'

    return {
        'passed': len(failed_checks) == 0,
        'risk_level': risk_level,
        'action': action,
        'total_checks': len(checks),
        'passed_checks': len(passed_checks),
        'failed_checks': len(failed_checks),
        'checks': failed_checks,  # 只返回失败的检查项
        'fixes_applied': [],
        'scanned_at': datetime.now().isoformat(),
    }


def auto_fix_risks(content: str, scan_result: Dict[str, Any]) -> Tuple[str, List[Dict]]:
    """根据扫描结果自动修复风险模式

    修复策略:
    - exec/eval命令: 替换为描述性文字
    - API密钥: 替换为环境变量引用
    - http://: 替换为https://
    - 硬编码IP: 替换为环境变量
    - 敏感路径: 替换为通配符
    - 其他高风险模式: 移除或注释化

    参数:
        content: 原始内容
        scan_result: scan_content返回的扫描结果

    返回:
        (修复后内容, 修复项列表)
    """
    if not content or scan_result.get('passed'):
        return content, []

    fixes = []
    fixed_content = content

    for check in scan_result.get('checks', []):
        if check.get('passed'):
            continue

        name = check.get('name', '').replace('安全审核: ', '')
        details = check.get('details', [])

        # 根据风险类型执行修复
        if 'exec命令执行' in name:
            # 替换exec/os.system为安全描述
            fixed_content = re.sub(
                r'\bexec\s*\(', '# [安全修复] exec调用已移除: ',
                fixed_content
            )
            fixed_content = re.sub(
                r'os\.system\s*\(', '# [安全修复] os.system调用已移除: ',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': 'exec/os.system调用替换为注释',
                'severity': 'critical',
            })

        elif 'eval/代码注入' in name:
            fixed_content = re.sub(
                r'\beval\s*\(', '# [安全修复] eval调用已移除: ',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': 'eval调用替换为注释',
                'severity': 'critical',
            })

        elif 'API密钥' in name:
            # 替换明文密钥为环境变量引用
            fixed_content = re.sub(
                r'(API_KEY|API_SECRET|SECRET_KEY|ACCESS_TOKEN|PRIVATE_KEY)\s*=\s*["\'][^"\']+["\']',
                r'\1 = os.getenv("\1")  # [安全修复] 明文密钥已替换为环境变量',
                fixed_content
            )
            fixed_content = re.sub(
                r'export\s+(API_KEY|API_SECRET|SECRET_KEY|ACCESS_TOKEN)\s*=\s*["\'][^"\']+["\']',
                r'export \1="${\1:?请设置环境变量}"  # [安全修复]',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': '明文密钥替换为环境变量引用',
                'severity': 'critical',
            })

        elif 'HTTP不安全通信' in name:
            # http:// → https://
            count = len(re.findall(r'http://', fixed_content))
            fixed_content = fixed_content.replace('http://', 'https://')
            if count > 0:
                fixes.append({
                    'risk': name,
                    'action': f'{count}处http://替换为https://',
                    'severity': 'medium',
                })

        elif '硬编码服务器地址' in name:
            # 替换硬编码IP为环境变量
            fixed_content = re.sub(
                r'(SERVER|ENDPOINT|HOST|URL)\s*=\s*["\']https?://\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}[^"\']*["\']',
                r'\1 = os.getenv("\1_URL", "")  # [安全修复] 硬编码IP替换为环境变量',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': '硬编码IP替换为环境变量',
                'severity': 'medium',
            })

        elif '敏感信息泄露' in name:
            # 替换敏感路径为通配符 (使用lambda避免re.sub的\U转义问题)
            fixed_content = re.sub(
                r'C:\\Users\\[a-zA-Z]+',
                lambda m: r'C:\Users\<username>',
                fixed_content
            )
            fixed_content = re.sub(
                r'/home/[a-z]+/',
                lambda m: '/home/<user>/',
                fixed_content
            )
            fixed_content = re.sub(
                r'/Users/[a-zA-Z]+/',
                lambda m: '/Users/<user>/',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': '敏感路径替换为通配符',
                'severity': 'medium',
            })

        elif 'VPN' in name or '翻墙' in name:
            # VPN关键词: 添加安全注释包裹
            for kw in _VPN_BLOCKED_KEYWORDS:
                if kw.lower() in fixed_content.lower():
                    fixed_content = re.sub(
                        re.escape(kw), f'<!-- [安全修复] 移除VPN关键词: {kw} -->',
                        fixed_content, flags=re.IGNORECASE
                    )
            fixes.append({
                'risk': name,
                'action': 'VPN关键词替换为安全注释',
                'severity': 'critical',
            })

        elif '反向Shell' in name:
            # 反向Shell: 完全移除相关行
            lines = fixed_content.split('\n')
            filtered = []
            for line in lines:
                if re.search(r'(?:bash|sh|nc|ncat)\s+.*(?:-i|/dev/tcp/)', line):
                    filtered.append(f'# [安全修复] 反向Shell代码已移除')
                else:
                    filtered.append(line)
            fixed_content = '\n'.join(filtered)
            fixes.append({
                'risk': name,
                'action': '反向Shell代码行移除',
                'severity': 'critical',
            })

        elif '加密货币挖矿' in name:
            # 挖矿地址: 完全移除
            fixed_content = re.sub(
                r'(?:xmrig|stratum\+tcp|cryptonight|coinhive)[^\n]*',
                '# [安全修复] 挖矿相关内容已移除',
                fixed_content, flags=re.IGNORECASE
            )
            fixes.append({
                'risk': name,
                'action': '挖矿相关内容移除',
                'severity': 'critical',
            })

        elif 'SSRF' in name:
            # SSRF: 添加URL校验注释
            fixed_content = re.sub(
                r'requests\.(get|post)\s*\(\s*(user|input|url)',
                r'# [安全修复] SSRF风险: requests.\1(user_input) 需URL白名单校验\n# requests.\1(',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': 'SSRF风险代码添加安全注释',
                'severity': 'critical',
            })

        elif '数据外泄' in name:
            # 数据外泄: 移除读取敏感文件并上传的代码
            fixed_content = re.sub(
                r'(?:cat|type|Get-Content)\s+(?:/etc/passwd|/etc/shadow|\.env|\.ssh/id_rsa)',
                '# [安全修复] 敏感文件读取已移除',
                fixed_content, flags=re.IGNORECASE
            )
            fixes.append({
                'risk': name,
                'action': '敏感文件读取代码移除',
                'severity': 'critical',
            })

        elif '不安全反序列化' in name:
            # pickle.loads → json.loads
            fixed_content = fixed_content.replace('pickle.loads', 'json.loads')
            fixed_content = fixed_content.replace('pickle.load', 'json.load')
            fixed_content = re.sub(
                r'yaml\.load\s*\((?!.*Loader)',
                'yaml.safe_load(',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': 'pickle.loads→json.loads, yaml.load→yaml.safe_load',
                'severity': 'critical',
            })

        elif '依赖混淆' in name:
            # http源 → https源
            fixed_content = re.sub(
                r'pip\s+install\s+(?:--index-url|--extra-index-url)\s+["\']http://',
                'pip install --index-url https://',
                fixed_content
            )
            fixed_content = re.sub(
                r'npm\s+install\s+.*--registry\s+["\']http://',
                'npm install --registry https://',
                fixed_content
            )
            fixes.append({
                'risk': name,
                'action': 'http依赖源替换为https',
                'severity': 'high',
            })

    return fixed_content, fixes


def load_candidates(source_filter: Optional[str] = None) -> List[Dict[str, Any]]:
    """从 candidates_unified.json 加载候选 skill 列表"""
    if not CANDIDATES_FILE.exists():
        print(f"[ERROR] 候选文件不存在: {CANDIDATES_FILE}")
        print("        请先运行 multi_source_discover.py 生成候选数据。")
        return []

    with open(CANDIDATES_FILE, 'r', encoding='utf-8') as f:
        data = json.load(f)

    if isinstance(data, dict):
        candidates = data.get('candidates', [])
    elif isinstance(data, list):
        candidates = data
    else:
        candidates = []

    if source_filter:
        candidates = [c for c in candidates if c.get('source') == source_filter]

    return candidates


def scan_candidates(
    candidates: List[Dict[str, Any]],
    limit: int = 0,
    auto_fix: bool = False,
) -> Dict[str, Any]:
    """批量扫描候选 skill 的安全风险

    参数:
        candidates: 候选 skill 列表
        limit: 限制扫描数量(0=全部)
        auto_fix: 是否自动修复可修复的风险

    返回:
        扫描结果汇总
    """
    if limit > 0:
        candidates = candidates[:limit]

    stats = {
        'total': len(candidates),
        'safe': 0,
        'notice': 0,
        'warning': 0,
        'blocked': 0,
        'details': [],
        'scanned_at': datetime.now().isoformat(),
    }

    print(f"\n{'='*60}")
    print(f"源Skill安全扫描器 — 差异化前安全预检")
    print(f"{'='*60}")
    print(f"候选总数: {len(candidates)}")
    print(f"自动修复: {'是' if auto_fix else '否'}")
    print(f"{'='*60}\n")

    for idx, candidate in enumerate(candidates, 1):
        source = candidate.get('source', 'unknown')
        source_id = candidate.get('source_id', '')
        name = candidate.get('name', '')
        description = candidate.get('description', '')
        content_preview = candidate.get('content_preview', '')
        url = candidate.get('url', '')

        # 合并所有可扫描内容
        scan_text = f"{description}\n{content_preview}"

        # 执行安全扫描
        result = scan_content(scan_text)

        # 如果有风险且开启了自动修复
        if auto_fix and not result['passed']:
            fixed_text, fixes = auto_fix_risks(scan_text, result)
            result['fixes_applied'] = fixes
            # 重新扫描修复后的内容
            recheck = scan_content(fixed_text)
            result['recheck_passed'] = recheck['passed']
            result['recheck_risk_level'] = recheck['risk_level']

        action = result['action']
        risk_level = result['risk_level']

        # 统计
        if action == 'SAFE':
            stats['safe'] += 1
        elif action == 'NOTICE':
            stats['notice'] += 1
        elif action == 'WARNING':
            stats['warning'] += 1
        elif action == 'BLOCKED':
            stats['blocked'] += 1

        # 输出
        status_icon = {
            'SAFE': '✓',
            'NOTICE': '⚠',
            'WARNING': '⚠⚠',
            'BLOCKED': '✗',
        }.get(action, '?')

        print(
            f"[{idx:4d}/{len(candidates)}] {status_icon} {action:8s} | "
            f"{risk_level:8s} | "
            f"source={source:15s} | "
            f"name={name[:30]}"
        )

        if not result['passed']:
            for check in result.get('checks', []):
                print(f"           → [{check.get('severity', '?').upper()}] {check.get('name', '')}")
                for detail in check.get('details', [])[:1]:
                    print(f"             {detail[:80]}")

        detail = {
            'index': idx,
            'source': source,
            'source_id': source_id,
            'name': name,
            'url': url,
            'risk_level': risk_level,
            'action': action,
            'failed_checks': result.get('failed_checks', 0),
            'checks': result.get('checks', []),
            'fixes_applied': result.get('fixes_applied', []),
            'recheck_passed': result.get('recheck_passed'),
        }
        stats['details'].append(detail)

    # 输出统计
    print(f"\n{'='*60}")
    print(f"扫描完成")
    print(f"{'='*60}")
    print(f"总候选数:    {stats['total']}")
    print(f"安全(✓):     {stats['safe']}")
    print(f"注意(⚠):     {stats['notice']}")
    print(f"警告(⚠⚠):    {stats['warning']}")
    print(f"阻断(✗):     {stats['blocked']}")
    print(f"{'='*60}")

    # 保存结果
    save_json(SCAN_RESULTS_FILE, stats)
    print(f"结果已保存: {SCAN_RESULTS_FILE}")

    return stats


def get_safe_candidates(scan_results: Optional[Dict] = None) -> List[str]:
    """获取通过安全扫描的候选 source_id 列表

    用于 auto_differentiate.py 调用, 过滤掉不安全的候选
    """
    if scan_results is None:
        if not SCAN_RESULTS_FILE.exists():
            return []
        scan_results = load_json(SCAN_RESULTS_FILE)

    safe_ids = []
    for detail in scan_results.get('details', []):
        if detail.get('action') in ('SAFE', 'NOTICE'):
            safe_ids.append(detail.get('source_id', ''))

    return [sid for sid in safe_ids if sid]


def get_blocked_candidates(scan_results: Optional[Dict] = None) -> List[Dict]:
    """获取被安全扫描阻断的候选列表"""
    if scan_results is None:
        if not SCAN_RESULTS_FILE.exists():
            return []
        scan_results = load_json(SCAN_RESULTS_FILE)

    return [
        d for d in scan_results.get('details', [])
        if d.get('action') == 'BLOCKED'
    ]


def load_json(path: Path) -> Dict:
    if not path.exists():
        return {}
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)


def save_json(path: Path, data: Dict):
    path.parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def main():
    parser = argparse.ArgumentParser(
        description='源Skill安全扫描器 — 差异化前安全预检 (流水线 Step 1.5)',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  python source_security_scan.py                          # 扫描所有候选
  python source_security_scan.py --limit 50               # 扫描前50个
  python source_security_scan.py --source hermes           # 只扫描hermes来源
  python source_security_scan.py --content "skill内容"     # 扫描指定文本
  python source_security_scan.py --auto-fix               # 扫描并自动修复
  python source_security_scan.py --json                   # 输出JSON
        """,
    )
    parser.add_argument('--limit', type=int, default=0,
                        help='只扫描前N个候选 (默认: 0=全部)')
    parser.add_argument('--source', type=str, default=None,
                        help='只扫描指定来源的候选')
    parser.add_argument('--content', type=str, default=None,
                        help='扫描指定的文本内容(不走候选文件)')
    parser.add_argument('--auto-fix', action='store_true',
                        help='扫描并自动修复可修复的风险模式')
    parser.add_argument('--json', action='store_true',
                        help='输出JSON格式')
    args = parser.parse_args()

    # 模式1: 扫描指定文本
    if args.content:
        result = scan_content(args.content)
        if args.auto_fix and not result['passed']:
            fixed, fixes = auto_fix_risks(args.content, result)
            result['fixes_applied'] = fixes
            result['fixed_content'] = fixed

        if args.json:
            print(json.dumps(result, ensure_ascii=False, indent=2))
        else:
            print(f"\n扫描结果:")
            print(f"  通过: {result['passed']}")
            print(f"  风险级别: {result['risk_level']}")
            print(f"  处理策略: {result['action']}")
            print(f"  检查项: {result['passed_checks']}/{result['total_checks']} 通过")
            if result.get('fixes_applied'):
                print(f"\n自动修复:")
                for fix in result['fixes_applied']:
                    print(f"  [{fix['severity']}] {fix['risk']}: {fix['action']}")
            if not result['passed']:
                print(f"\n失败项:")
                for check in result.get('checks', []):
                    print(f"  [{check.get('severity', '').upper()}] {check.get('name', '')}")
                    for d in check.get('details', []):
                        print(f"    → {d[:100]}")
        return

    # 模式2: 扫描候选文件
    candidates = load_candidates(source_filter=args.source)
    if not candidates:
        print("没有符合条件的候选, 退出。")
        return

    results = scan_candidates(
        candidates=candidates,
        limit=args.limit,
        auto_fix=args.auto_fix,
    )

    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
