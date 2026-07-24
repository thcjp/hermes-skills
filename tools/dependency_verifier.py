#!/usr/bin/env python3
"""
Skill外部依赖验证器 (Dependency Verifier)
==========================================

在L2验证之后, 对SKILL.md引用的外部依赖进行真实可达性验证。
解决L2验证发现的"中文名称外部API服务无法识别"问题。

验证能力:
  1. API endpoint (https://xxx/api): HTTP HEAD请求检查可达性
  2. npm包 (npm install xxx): npm view命令检查存在性
  3. PyPI包 (pip install xxx): pip index versions检查存在性
  4. AI模型名: 与已知模型列表比对
  5. 中文名称外部API服务: 基于上下文模式识别,标记为"需人工验证"

设计理念:
  - 不硬编码API Key, 不实际调用需要认证的API
  - HTTP HEAD请求设置3秒超时, 失败标记为warning而非error
  - npm/pip检查通过subprocess执行, 捕获超时
  - 中文名称API服务无法自动验证, 标记为manual_review

Usage:
    python dependency_verifier.py --help
    python dependency_verifier.py verify <slug>
    python dependency_verifier.py verify <slug> --json
    python dependency_verifier.py verify <slug> -o report.json

流程:
    Step 1: 查找SKILL.md
    Step 2: 提取外部依赖(增强版, 识别中文名称API服务)
    Step 3: 逐个验证依赖
    Step 4: 输出依赖验证报告(JSON)
"""

import sys
import json
import argparse
import subprocess
import re
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection, PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR
from trace_llm_scorer import read_skill_md


# ============ 常量 ============

# HTTP请求超时(秒)
HTTP_TIMEOUT = 3

# subprocess超时(秒)
SUBPROCESS_TIMEOUT = 5

# 已知AI模型列表
KNOWN_AI_MODELS = [
    'GPT-4', 'GPT-3.5', 'GPT-4o', 'o1', 'o3',
    'Claude', 'Claude-3', 'Claude-3.5', 'Sonnet', 'Opus', 'Haiku',
    'BERT', 'RoBERTa', 'T5', 'LLaMA', 'GLM-4', '文心', '通义', 'DeepSeek',
    'Whisper', 'CLIP', 'DALL-E', 'Stable Diffusion',
    '通义千问', '文心一言', '智谱GLM', 'Kimi', '通义万相', '文心一格',
]

# 中文名称外部API服务识别模式
# 这些模式用于从SKILL.md上下文中识别未明确标注URL的外部API服务
CHINESE_API_SERVICE_PATTERNS = [
    # "XXX引擎" "XXXAPI" "XXX服务" "XXX平台" 等
    r'([\u4e00-\u9fa5A-Za-z0-9]{2,15}(?:AI|ai)?(?:引擎|API|服务|平台|写真|绘画|生成器|模型库))',
]

# 已知免费/通用服务(不需要验证)
KNOWN_FREE_SERVICES = [
    '通用绘画引擎', '通用绘画', '通用T2I', '通用引擎',
    '通用绘画', '通用绘画T2I',
]

# 通用描述性短语(不是特定外部API服务,应过滤掉)
GENERIC_DESCRIPTIONS = [
    'Agent平台', '任意LLM服务', 'AI绘画引擎', '图像生成API',
    '角色一致性引擎', '通用绘画', '通用引擎', '通用T2I',
    '视频引擎', '备选引擎', '通用绘画T2I',
    'LLM API', 'AI API', 'API Key',
]

# 误识别过滤关键词(匹配项包含这些词则不是真实的服务名)
FALSE_POSITIVE_KEYWORDS = [
    'md', '代码', '硬编码', '不包含', '严禁', '禁止', '环境变量',
    '配置', '设置', '注入', '暴露', '打印', '日志', '占位符',
    '示例', '真实', 'Key', 'Token', 'Secret',
]


# ============ Skill查找 ============

def find_skill_md(slug: str) -> Optional[Path]:
    """查找skill的SKILL.md路径"""
    packaged_path = PACKAGED_SKILLS_DIR / slug / "SKILL.md"
    if packaged_path.exists():
        return packaged_path

    opensource_path = OPENSOURCE_SKILLS_DIR / slug / "SKILL.md"
    if opensource_path.exists():
        return opensource_path

    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT local_path FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        conn.close()
        if row and row['local_path']:
            p = Path(row['local_path'])
            if p.name == 'SKILL.md' and p.exists():
                return p
            skill_md = p / 'SKILL.md'
            if skill_md.exists():
                return skill_md
    except Exception:
        pass

    return None


def get_skill_id(slug: str) -> Optional[int]:
    """从DB获取skill_id"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT id FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        conn.close()
        return row['id'] if row else None
    except Exception:
        return None


# ============ 依赖提取(增强版) ============

def extract_external_dependencies_enhanced(skill_content: str) -> List[Dict[str, Any]]:
    """从SKILL.md中提取外部依赖(增强版)
    
    增强点: 识别中文名称外部API服务(如"鹧应AI写真")
    
    识别类型:
      1. api_endpoint: https://xxx/api 格式的URL
      2. npm_package: npm install xxx
      3. pypi_package: pip install xxx
      4. ai_model: 已知AI模型名
      5. chinese_api_service: 中文名称外部API服务(新增)
      6. api_key_env: API Key环境变量引用
    """
    deps = []
    seen_names = set()

    def add_dep(dep_type, name, **extra):
        if name and name not in seen_names:
            seen_names.add(name)
            dep = {'type': dep_type, 'name': name, **extra}
            deps.append(dep)

    # 1. API endpoint URL
    api_pattern = r'https?://[a-zA-Z0-9._/-]+api[a-zA-Z0-9._/-]*'
    for m in re.finditer(api_pattern, skill_content, re.IGNORECASE):
        add_dep('api_endpoint', m.group(0),
                verification_method='HTTP HEAD请求',
                verified=False, status='pending')

    # 2. npm包
    npm_pattern = r'npm\s+(?:install|i)\s+([a-zA-Z0-9@/_-]+)'
    for m in re.finditer(npm_pattern, skill_content):
        pkg = m.group(1)
        if not pkg.startswith('@types/'):
            add_dep('npm_package', pkg,
                    verification_method='npm view <package>',
                    verified=False, status='pending')

    # 3. PyPI包
    pypi_pattern = r'pip\s+install\s+([a-zA-Z0-9_-]+)'
    for m in re.finditer(pypi_pattern, skill_content):
        add_dep('pypi_package', m.group(1),
                verification_method='pip index versions <package>',
                verified=False, status='pending')

    # 4. 已知AI模型
    for model in KNOWN_AI_MODELS:
        if model.lower() in skill_content.lower():
            add_dep('ai_model', model,
                    verification_method='已知模型列表比对',
                    verified=True, status='known_model')

    # 5. 中文名称外部API服务(新增核心能力)
    # 从"依赖说明"章节提取
    dep_section = extract_dependency_section(skill_content)
    if dep_section:
        # 识别"XXX引擎""XXX API""XXX服务"等
        for pattern in CHINESE_API_SERVICE_PATTERNS:
            for m in re.finditer(pattern, dep_section):
                name = m.group(1).strip()
                # 排除已知免费服务、通用描述、已识别的依赖
                # 排除包含误识别关键词的匹配(如"md或代码中硬编码API")
                is_false_positive = any(
                    kw.lower() in name.lower() for kw in FALSE_POSITIVE_KEYWORDS
                )
                if (name not in KNOWN_FREE_SERVICES
                        and name not in GENERIC_DESCRIPTIONS
                        and not is_false_positive
                        and not any(name in d['name'] for d in deps)
                        and len(name) >= 3):  # 过滤过短的匹配
                    # 判断是否为付费服务(含价格信息)
                    is_paid = bool(re.search(
                        rf'{re.escape(name)}.*?(?:\d+\.?\d*元|\d+\.?\d*元/张|付费|收费)',
                        skill_content
                    ))
                    add_dep('chinese_api_service', name,
                            verification_method='需人工验证(无URL无法自动检查)',
                            verified=False,
                            status='manual_review',
                            is_paid=is_paid,
                            context=extract_context(skill_content, name))

    # 6. API Key环境变量引用
    api_key_pattern = r'(?:环境变量|配置|设置)\s*(?:中)?\s*([A-Z_]{3,}_API_KEY)'
    for m in re.finditer(api_key_pattern, skill_content):
        add_dep('api_key_env', m.group(1),
                verification_method='环境变量存在性检查',
                verified=False, status='manual_review')

    return deps


def extract_dependency_section(skill_content: str) -> str:
    """提取"依赖说明"章节内容"""
    # 匹配 ## 依赖说明 到下一个 ## 章节
    pattern = r'##\s*依赖说明\s*\n(.*?)(?=\n##\s|\Z)'
    m = re.search(pattern, skill_content, re.DOTALL)
    if m:
        return m.group(1)
    return ''


def extract_context(skill_content: str, name: str, context_chars: int = 100) -> str:
    """提取依赖名称周围的上下文"""
    idx = skill_content.find(name)
    if idx == -1:
        return ''
    start = max(0, idx - context_chars // 2)
    end = min(len(skill_content), idx + len(name) + context_chars // 2)
    return skill_content[start:end].replace('\n', ' ').strip()


# ============ 依赖验证 ============

def verify_api_endpoint(url: str) -> Dict[str, Any]:
    """验证API endpoint可达性(HTTP HEAD请求)"""
    try:
        req = Request(url, method='HEAD', headers={'User-Agent': 'SkillDependencyVerifier/1.0'})
        resp = urlopen(req, timeout=HTTP_TIMEOUT)
        return {
            'verified': True,
            'status': 'reachable',
            'http_status': resp.status,
            'details': f'HTTP HEAD成功, 状态码{resp.status}'
        }
    except HTTPError as e:
        # 401/403表示需要认证, 但endpoint存在
        if e.code in (401, 403):
            return {
                'verified': True,
                'status': 'exists_requires_auth',
                'http_status': e.code,
                'details': f'Endpoint存在但需要认证(HTTP {e.code})'
            }
        return {
            'verified': False,
            'status': 'http_error',
            'http_status': e.code,
            'details': f'HTTP错误: {e.code} {e.reason}'
        }
    except URLError as e:
        return {
            'verified': False,
            'status': 'unreachable',
            'details': f'URL不可达: {str(e.reason)}'
        }
    except Exception as e:
        return {
            'verified': False,
            'status': 'error',
            'details': f'验证异常: {str(e)}'
        }


def verify_npm_package(package: str) -> Dict[str, Any]:
    """验证npm包存在性"""
    try:
        result = subprocess.run(
            ['npm', 'view', package, 'version'],
            capture_output=True, text=True, timeout=SUBPROCESS_TIMEOUT,
            shell=True
        )
        if result.returncode == 0 and result.stdout.strip():
            return {
                'verified': True,
                'status': 'exists',
                'version': result.stdout.strip(),
                'details': f'npm包存在, 最新版本: {result.stdout.strip()}'
            }
        else:
            return {
                'verified': False,
                'status': 'not_found',
                'details': f'npm包不存在: {result.stderr.strip()[:200]}'
            }
    except subprocess.TimeoutExpired:
        return {
            'verified': False,
            'status': 'timeout',
            'details': f'npm view超时({SUBPROCESS_TIMEOUT}秒)'
        }
    except Exception as e:
        return {
            'verified': False,
            'status': 'error',
            'details': f'验证异常: {str(e)}'
        }


def verify_pypi_package(package: str) -> Dict[str, Any]:
    """验证PyPI包存在性"""
    try:
        result = subprocess.run(
            [sys.executable, '-m', 'pip', 'index', 'versions', package],
            capture_output=True, text=True, timeout=SUBPROCESS_TIMEOUT
        )
        if result.returncode == 0 and 'Available versions:' in result.stdout:
            versions_line = [l for l in result.stdout.split('\n') if 'Available versions:' in l]
            versions = versions_line[0].split(':')[-1].strip() if versions_line else 'unknown'
            return {
                'verified': True,
                'status': 'exists',
                'versions': versions,
                'details': f'PyPI包存在, 可用版本: {versions[:100]}'
            }
        else:
            return {
                'verified': False,
                'status': 'not_found',
                'details': f'PyPI包不存在: {result.stderr.strip()[:200]}'
            }
    except subprocess.TimeoutExpired:
        return {
            'verified': False,
            'status': 'timeout',
            'details': f'pip index versions超时({SUBPROCESS_TIMEOUT}秒)'
        }
    except Exception as e:
        return {
            'verified': False,
            'status': 'error',
            'details': f'验证异常: {str(e)}'
        }


def verify_dependency(dep: Dict[str, Any]) -> Dict[str, Any]:
    """验证单个依赖"""
    dep_type = dep['type']
    name = dep['name']

    result = {
        'type': dep_type,
        'name': name,
        'verification_method': dep.get('verification_method', ''),
        'verified_at': datetime.now().isoformat(),
    }

    if dep_type == 'api_endpoint':
        verify_result = verify_api_endpoint(name)
        result.update(verify_result)

    elif dep_type == 'npm_package':
        verify_result = verify_npm_package(name)
        result.update(verify_result)

    elif dep_type == 'pypi_package':
        verify_result = verify_pypi_package(name)
        result.update(verify_result)

    elif dep_type == 'ai_model':
        result.update({
            'verified': True,
            'status': 'known_model',
            'details': f'已知AI模型: {name}'
        })

    elif dep_type == 'chinese_api_service':
        # 中文名称API服务无法自动验证
        result.update({
            'verified': False,
            'status': 'manual_review_required',
            'is_paid': dep.get('is_paid', False),
            'context': dep.get('context', ''),
            'details': f'中文名称外部API服务"{name}"无法自动验证, 需人工确认:\n'
                       f'  1. 搜索该服务是否真实存在\n'
                       f'  2. 检查API文档和定价是否与SKILL.md描述一致\n'
                       f'  3. 确认国内可用性和访问方式\n'
                       f'  上下文: {dep.get("context", "无")[:200]}'
        })

    elif dep_type == 'api_key_env':
        result.update({
            'verified': False,
            'status': 'manual_review_required',
            'details': f'API Key环境变量"{name}"需在运行时由用户配置, 无法静态验证'
        })

    else:
        result.update({
            'verified': False,
            'status': 'unknown_type',
            'details': f'未知依赖类型: {dep_type}'
        })

    return result


# ============ 主验证流程 ============

def run_dependency_verification(slug: str, output_json: bool = False, output_file: str = None) -> Dict[str, Any]:
    """运行依赖验证"""
    result = {
        'slug': slug,
        'verified_at': datetime.now().isoformat(),
        'verifier_version': '1.0',
    }

    # Step 1: 查找SKILL.md
    skill_md_path = find_skill_md(slug)
    if not skill_md_path:
        result['status'] = 'error'
        result['error'] = f'SKILL.md not found for slug: {slug}'
        return result

    result['skill_md_path'] = str(skill_md_path)
    skill_content = read_skill_md(str(skill_md_path.parent))

    if not skill_content:
        result['status'] = 'error'
        result['error'] = 'SKILL.md内容为空'
        return result

    # Step 2: 提取外部依赖(增强版)
    deps = extract_external_dependencies_enhanced(skill_content)
    result['total_deps'] = len(deps)
    result['dependencies_extracted'] = deps

    # Step 3: 逐个验证依赖
    verified_deps = []
    for dep in deps:
        verify_result = verify_dependency(dep)
        verified_deps.append(verify_result)

    result['verification_results'] = verified_deps

    # Step 4: 汇总统计
    verified_count = sum(1 for d in verified_deps if d.get('verified'))
    manual_review_count = sum(1 for d in verified_deps if d.get('status') == 'manual_review_required')
    failed_count = sum(1 for d in verified_deps if not d.get('verified') and d.get('status') != 'manual_review_required')

    result['summary'] = {
        'total': len(verified_deps),
        'verified': verified_count,
        'manual_review_required': manual_review_count,
        'failed': failed_count,
        'overall_status': 'PASS' if failed_count == 0 else ('WARN' if manual_review_count > 0 else 'FAIL'),
    }

    # 保存报告
    if output_file:
        report_path = Path(output_file)
    else:
        report_path = SKILL_REGISTRY_DIR / f'dep_verification_report_{slug}.json'

    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    result['report_path'] = str(report_path)

    # 终端输出
    if not output_json:
        print(f"\n{'='*70}")
        print(f"依赖验证报告: {slug}")
        print(f"{'='*70}")
        print(f"SKILL.md路径: {skill_md_path}")
        print(f"验证时间: {result['verified_at']}")
        print(f"\n--- 依赖提取({len(deps)}个) ---")
        for dep in deps:
            paid_tag = ' [付费]' if dep.get('is_paid') else ''
            print(f"  [{dep['type']}] {dep['name']}{paid_tag}")

        print(f"\n--- 验证结果 ---")
        for vd in verified_deps:
            status_icon = '✓' if vd.get('verified') else ('⚠' if vd.get('status') == 'manual_review_required' else '✗')
            print(f"  {status_icon} [{vd['type']}] {vd['name']}")
            print(f"    状态: {vd.get('status', 'N/A')}")
            if vd.get('details'):
                # 只打印第一行详情
                first_line = vd['details'].split('\n')[0]
                print(f"    详情: {first_line[:120]}")

        print(f"\n--- 汇总 ---")
        s = result['summary']
        print(f"  总计: {s['total']}个依赖")
        print(f"  已验证: {s['verified']}个")
        print(f"  需人工验证: {s['manual_review_required']}个")
        print(f"  验证失败: {s['failed']}个")
        print(f"  总体状态: {s['overall_status']}")
        print(f"\n  报告路径: {report_path}")
        print(f"{'='*70}")
    else:
        print(json.dumps(result, ensure_ascii=False, indent=2))

    return result


# ============ CLI ============

def main():
    parser = argparse.ArgumentParser(
        description='Skill外部依赖验证器 - 验证SKILL.md引用的外部依赖是否真实可达',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 验证单个skill的依赖
  python dependency_verifier.py verify ai-artist-workstation

  # 输出JSON格式
  python dependency_verifier.py verify ai-artist-workstation --json

  # 保存报告到指定文件
  python dependency_verifier.py verify ai-artist-workstation -o report.json

验证类型:
  - api_endpoint: HTTP HEAD请求检查可达性(3秒超时)
  - npm_package: npm view命令检查存在性
  - pypi_package: pip index versions检查存在性
  - ai_model: 与已知模型列表比对
  - chinese_api_service: 中文名称API服务,标记为需人工验证
  - api_key_env: API Key环境变量,标记为需运行时配置
        """
    )

    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # verify子命令
    val_parser = subparsers.add_parser('verify', help='验证单个skill的依赖')
    val_parser.add_argument('slug', help='Skill slug名称')
    val_parser.add_argument('--json', action='store_true', help='输出JSON格式')
    val_parser.add_argument('-o', '--output', help='报告保存路径')

    args = parser.parse_args()

    if args.command == 'verify':
        run_dependency_verification(args.slug, output_json=args.json, output_file=args.output)
    else:
        parser.print_help()


if __name__ == '__main__':
    main()
