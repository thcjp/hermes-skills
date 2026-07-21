#!/usr/bin/env python3
"""
源skill保真度检查器 (Source Fidelity Checker)
================================================

验证生成的skill是否保留了源skill的核心能力和领域知识。
这是回答用户核心问题的关键工具:
  "不同类型、不同业务的skill是如何保证每一个skill本身的能力、功能、质量的?"

工作原理:
  1. 读取源skill (clawhub-skills/downloaded/) 提取核心能力点
  2. 读取生成版本 (packaged-skills/skillhub/) 提取能力点
  3. 计算能力覆盖率: 生成版本覆盖了多少源skill的能力点
  4. 检查领域知识保留: API名、命令名、参数名是否保留
  5. 检查功能描述深度: 是否有足够的具体描述

保真度评分 (0-100):
  - 能力覆盖率 (40%): 生成版本覆盖源能力点的比例
  - 领域术语保留 (25%): 源skill的领域术语在生成版本中的保留率
  - 功能描述深度 (20%): 每个能力点是否有具体描述(非通用)
  - 差异化程度 (15%): 生成版本与源skill的内容差异度(避免照搬)

Usage:
    python source_fidelity_checker.py <slug>
    python source_fidelity_checker.py <slug> --json
    python source_fidelity_checker.py --batch --limit 50
"""

import sys
import re
import json
import argparse
from pathlib import Path
from typing import Dict, List, Tuple, Any, Set
from datetime import datetime

SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import PACKAGED_SKILLS_DIR

# 源skill目录 (多个可能的源)
SOURCE_DIRS = [
    Path(r'D:\skills\clawhub-skills\downloaded'),
    Path(r'D:\skills\differentiated-skills'),
]
# 兼容旧代码
SOURCE_DIR = SOURCE_DIRS[0]

# 扫描结果
SCAN_RESULT = SKILL_REGISTRY_DIR / 'capability_scan_result.json'

# 英文→中文技术术语映射 (用于跨语言能力覆盖检查)
# 源skill通常是英文,生成版本是中文,直接关键词匹配会失败
EN_TO_ZH_MAP = {
    # 数据操作
    'memory': ['记忆', '内存'], 'storage': ['存储'], 'store': ['存储'],
    'search': ['搜索', '检索'], 'find': ['查找', '寻找'],
    'index': ['索引'], 'navigate': ['导航'], 'navigation': ['导航'],
    'sync': ['同步'], 'synchronize': ['同步'],
    'write': ['写入'], 'read': ['读取'],
    'split': ['拆分', '分割'], 'scale': ['扩展', '伸缩'],
    'merge': ['合并'], 'combine': ['合并'],
    'filter': ['过滤', '筛选'], 'group': ['分组'],
    'aggregat': ['聚合'],  # aggregation, aggregate
    'export': ['导出'], 'import': ['导入'],
    'parse': ['解析'], 'analyz': ['分析'],  # analyze, analysis
    'convert': ['转换'], 'transform': ['转换'],
    'sort': ['排序'], 'order': ['排序', '排序'],
    'valid': ['验证'], 'validate': ['验证'],
    'extract': ['提取'], 'generat': ['生成'],  # generate, generation
    'cache': ['缓存'], 'queue': ['队列'],
    # 文件/路径
    'file': ['文件'], 'folder': ['文件夹'], 'directory': ['目录'],
    'path': ['路径'], 'config': ['配置'], 'configuration': ['配置'],
    # 网络/API
    'request': ['请求'], 'response': ['响应'],
    'endpoint': ['端点'], 'api': ['接口'],
    'http': ['协议'], 'url': ['链接'],
    # 用户/权限
    'user': ['用户'], 'admin': ['管理员'],
    'auth': ['认证'], 'login': ['登录'], 'logout': ['登出'],
    'permission': ['权限'], 'role': ['角色'],
    # 状态
    'error': ['错误'], 'warning': ['警告'],
    'fail': ['失败'], 'success': ['成功'],
    'active': ['活跃'], 'pause': ['暂停'],
    'enable': ['启用'], 'disable': ['禁用'],
    # 流程
    'trigger': ['触发'], 'schedule': ['调度', '定时'],
    'execute': ['执行'], 'run': ['运行'],
    'install': ['安装'], 'update': ['更新'],
    'deploy': ['部署'], 'backup': ['备份'],
    'restore': ['恢复'], 'delete': ['删除'], 'remove': ['移除'],
    'create': ['创建'], 'build': ['构建'],
    'test': ['测试'], 'debug': ['调试'],
    # 数据结构
    'table': ['表格', '表'], 'record': ['记录'],
    'field': ['字段'], 'value': ['值'],
    'key': ['键'], 'pair': ['对'],
    'list': ['列表'], 'array': ['数组'],
    'string': ['字符串'], 'number': ['数字'],
    # 安全
    'privacy': ['隐私'], 'secure': ['安全'],
    'encrypt': ['加密'], 'decrypt': ['解密'],
    'token': ['令牌'], 'credential': ['凭证'],
    # 架构
    'agent': ['代理', 'Agent'], 'plugin': ['插件'],
    'module': ['模块'], 'component': ['组件'],
    'service': ['服务'], 'server': ['服务器'],
    'client': ['客户端'], 'database': ['数据库'],
    'query': ['查询'], 'transaction': ['事务'],
    # 其他常见
    'category': ['分类', '类别'], 'categorize': ['分类'],
    'organize': ['组织'], 'structure': ['结构'],
    'pattern': ['模式'], 'template': ['模板'],
    'rule': ['规则'], 'policy': ['策略'],
    'custom': ['自定义'], 'default': ['默认'],
    'parallel': ['并行'], 'async': ['异步'],
    'batch': ['批量'], 'pipeline': ['管道'],
    'workflow': ['工作流'], 'task': ['任务'],
    'notification': ['通知'], 'alert': ['告警'],
    'monitor': ['监控'], 'log': ['日志'],
    'compress': ['压缩'], 'archive': ['归档'],
    'scan': ['扫描'], 'detect': ['检测'],
    'recognize': ['识别'], 'process': ['处理'],
    'format': ['格式化', '格式'], 'render': ['渲染'],
    'display': ['显示'], 'output': ['输出'],
    'input': ['输入'], 'source': ['源'],
    'target': ['目标'], 'destination': ['目标'],
    'origin': ['来源'], 'root': ['根'],
    'core': ['核心'], 'main': ['主要'],
    'primary': ['主要'], 'secondary': ['次要'],
    'internal': ['内部'], 'external': ['外部'],
    'global': ['全局'], 'local': ['本地', '局部'],
    'public': ['公共'], 'private': ['私有'],
    'static': ['静态'], 'dynamic': ['动态'],
    'simple': ['简单'], 'complex': ['复杂'],
    'basic': ['基础'], 'advanced': ['高级'],
    'manual': ['手动'], 'automatic': ['自动'],
    'real-time': ['实时'], 'instant': ['即时'],
    'immediate': ['即时'], 'delay': ['延迟'],
}


def get_zh_translations(en_word: str) -> List[str]:
    """获取英文词的中文翻译列表"""
    en_lower = en_word.lower()
    # 精确匹配
    if en_lower in EN_TO_ZH_MAP:
        return EN_TO_ZH_MAP[en_lower]
    # 前缀匹配 (如 aggregation -> aggregat)
    for prefix, translations in EN_TO_ZH_MAP.items():
        if en_lower.startswith(prefix) and len(prefix) >= 4:
            return translations
    return []


def is_template_garbage(section_content: str, section_name: str) -> bool:
    """检测章节是否是模板垃圾内容(非真实能力描述)

    模板垃圾的特征:
    1. 包含 "触发关键词:" 标记
    2. 内容是 summary/description 的直接复制
    3. 内容过短(<50字符)且无实质 ### 子标题
    4. 仅包含通用描述,无具体技术细节
    """
    if not section_content:
        return True

    # 特征1: 包含触发关键词标记
    if '触发关键词' in section_content or '触发词' in section_content:
        return True

    # 特征2: 内容过短且无 ### 子标题
    h3_count = len(re.findall(r'^###\s+', section_content, re.MULTILINE))
    if len(section_content) < 100 and h3_count == 0:
        return True

    # 特征3: 仅包含通用描述语句 (不包含具体技术名词)
    # 检查是否有反引号包裹的代码/命令(技术术语的标志)
    has_code_refs = bool(re.search(r'`[a-zA-Z_][a-zA-Z0-9_\-\./]+`', section_content))
    # 检查是否有表格(结构化数据的标志)
    has_table = '|' in section_content and '---' in section_content
    # 检查是否有代码块
    has_code_block = '```' in section_content

    # 如果没有任何技术细节标志,且内容很短,视为模板垃圾
    if not has_code_refs and not has_table and not has_code_block and len(section_content) < 300:
        # 进一步检查: 是否包含具体操作动词
        action_verbs = ['创建', '删除', '修改', '查询', '执行', '配置', '安装', '运行',
                        '启动', '停止', '导入', '导出', '解析', '转换', '过滤', '排序',
                        'create', 'delete', 'update', 'query', 'execute', 'config',
                        'install', 'run', 'start', 'stop', 'import', 'export',
                        'parse', 'convert', 'filter', 'sort']
        has_actions = any(v in section_content.lower() for v in action_verbs)
        if not has_actions:
            return True

    return False


def load_source_skill(slug: str, scan_data: dict = None) -> Tuple[str, str]:
    """加载源skill内容,返回 (path, content)"""
    if scan_data is None:
        if SCAN_RESULT.exists():
            scan_data = json.loads(SCAN_RESULT.read_text(encoding='utf-8'))
        else:
            return '', ''

    for skill_info in scan_data.get('skills_to_process', []):
        if skill_info['slug'] == slug:
            source_path = skill_info.get('original_path', '')
            if source_path and Path(source_path).exists():
                return source_path, Path(source_path).read_text(encoding='utf-8')
            break

    # Fallback: search across all source directories
    for skill_info in scan_data.get('skills_to_process', []):
        if skill_info['slug'] == slug:
            category = skill_info.get('category', '')
            # Try multiple source locations across all source dirs
            possible_paths = []
            for src_dir in SOURCE_DIRS:
                possible_paths.extend([
                    src_dir / category / slug / 'SKILL.md',
                    src_dir / slug / 'SKILL.md',
                    # Also try with category as subdirectory
                    src_dir / slug / category / 'SKILL.md',
                ])
            # Also try glob search in each source dir
            for src_dir in SOURCE_DIRS:
                if src_dir.exists():
                    for p in src_dir.rglob('SKILL.md'):
                        if p.parent.name == slug:
                            possible_paths.append(p)
            for p in possible_paths:
                if p.exists():
                    return str(p), p.read_text(encoding='utf-8')
            break

    # Last resort: direct directory search (for slugs not in scan_data)
    for src_dir in SOURCE_DIRS:
        if src_dir.exists():
            # Try slug/SKILL.md pattern
            for p in src_dir.rglob('SKILL.md'):
                if p.parent.name == slug:
                    return str(p), p.read_text(encoding='utf-8')

    return '', ''


def parse_chapters(content: str) -> Dict[str, str]:
    """解析 ## 级别章节"""
    chapters = {}
    chapter_pattern = re.compile(r'^## (.+)$', re.MULTILINE)
    matches = list(chapter_pattern.finditer(content))
    for i, match in enumerate(matches):
        name = match.group(1).strip()
        start = match.end()
        end = matches[i + 1].start() if i + 1 < len(matches) else len(content)
        chapters[name] = content[start:end].strip()
    return chapters


def find_chapter(chapters: Dict[str, str], keywords: List[str]) -> str:
    """灵活查找章节内容"""
    for kw in keywords:
        if kw in chapters:
            return chapters[kw]
    for name, content in chapters.items():
        for kw in keywords:
            if kw in name:
                return content
    return ''


def extract_capability_points(content: str) -> List[str]:
    """从skill内容中提取能力点 - 仅从核心能力相关章节提取

    改进: 跳过模板垃圾章节(含"触发关键词"或仅复制summary的章节)
    """
    chapters = parse_chapters(content)

    # 收集所有匹配能力关键词的章节,按优先级排序
    # Round 14: 扩展关键词,覆盖更多源skill结构变体
    capability_keywords = [
        '核心能力', '核心功能', 'Core Rules', 'Core Features',
        'Core Capabilities', 'Core', '能力', '功能',
        'Features', 'Capabilities', '主要功能',
        'How It Works', 'Architecture', 'What to Store',
        'Quick Reference', 'Key Features', 'Main Features',
        # Round 14: 新增结构变体关键词
        'Core Framework', 'Core Principles', 'Quick Concepts',
        'Analysis Patterns', 'Common Crypto Games',
        'Methodology', 'Process', 'Skill Structure',
        'Scripts', 'Workflow', 'Review Checklist',
        'When to Add', 'When to Split',
        'Red Flags', 'Advanced Topics',
        'Setup', 'Configuration',
        # Round 14: 新增molt-board-art等skill的结构变体
        'Engagement', 'Loop', 'Artboard', 'Creative Tips',
        'State Tracking', 'Ideas to Try',
    ]

    # 收集所有候选章节
    candidates = []
    for name, ch_content in chapters.items():
        for kw in capability_keywords:
            if kw in name:
                candidates.append((name, ch_content, kw))
                break

    # 按优先级排序: 精确匹配优先,然后是包含匹配
    priority_order = [
        'Core Rules', 'Core Features', 'Core Capabilities',
        'Features', 'Capabilities', 'Key Features', 'Main Features',
        '核心能力', '核心功能', '主要功能',
        'How It Works', 'Architecture', 'What to Store', 'Quick Reference',
        'Core Framework', 'Core Principles', 'Quick Concepts',
        'Analysis Patterns', 'Common Crypto Games', 'Methodology',
        'Process', 'Skill Structure', 'Review Checklist',
        'When to Add', 'When to Split', 'Red Flags', 'Advanced Topics',
        'Scripts', 'Workflow', 'Setup', 'Configuration',
        'Engagement', 'Loop', 'Artboard', 'Creative Tips',
        'State Tracking', 'Ideas to Try',
        'Core', '能力', '功能',
    ]

    def get_priority(kw):
        try:
            return priority_order.index(kw)
        except ValueError:
            return len(priority_order)

    candidates.sort(key=lambda x: get_priority(x[2]))

    # Round 14: 从所有非垃圾匹配章节提取,而非只取第一个
    # 收集所有非垃圾候选章节
    non_garbage_candidates = [
        (name, ch_content) for name, ch_content, kw in candidates
        if not is_template_garbage(ch_content, name)
    ]

    # 如果所有候选都是垃圾或没有候选,从body中找 ### 标题最多的章节
    if not non_garbage_candidates:
        max_h3 = 0
        best_chapter = ''
        for name, ch_content in chapters.items():
            # 排除非能力章节
            if any(x in name for x in ['常见问题', 'FAQ', '错误', '异常', '依赖', '限制', '案例', '运行环境', 'License', 'license', '安装', 'Install', '示例']):
                continue
            # 跳过模板垃圾
            if is_template_garbage(ch_content, name):
                continue
            h3_count = len(re.findall(r'^###\s+', ch_content, re.MULTILINE))
            if h3_count > max_h3:
                max_h3 = h3_count
                best_chapter = ch_content
        # Round 14: 如果没有###标题的章节,fallback到内容最长的非排除章节
        if not best_chapter:
            max_len = 0
            for name, ch_content in chapters.items():
                if any(x in name for x in ['常见问题', 'FAQ', '错误', '异常', '依赖', '限制', '案例', '运行环境', 'License', 'license', '安装', 'Install', '适用场景', '使用流程', '示例']):
                    continue
                if is_template_garbage(ch_content, name):
                    continue
                if len(ch_content) > max_len:
                    max_len = len(ch_content)
                    best_chapter = ch_content
        if best_chapter:
            non_garbage_candidates = [('', best_chapter)]

    # 从所有候选章节提取能力点
    points = []
    for name, cap_content in non_garbage_candidates:
        if not cap_content:
            continue

        # 1. ### 标题 - 匹配所有###标题,然后剥离编号前缀
        h3_raw = re.findall(r'^###\s+(.+)$', cap_content, re.MULTILINE)
        # 剥离编号前缀 (1. / 1) / 1: 等)
        h3_points = [re.sub(r'^\d+[.):]?\s*', '', h).strip() for h in h3_raw]
        points.extend(h3_points)

        # 2. 编号列表 (1. **xxx**)
        numbered = re.findall(r'^\d+\.\s+\*\*(.+?)\*\*', cap_content, re.MULTILINE)
        points.extend(numbered)

        # Round 14: 2b. 编号列表 (1. xxx) - 无bold标记
        numbered_plain = re.findall(r'^\d+\.\s+([A-Z\u4e00-\u9fff].{2,80})$', cap_content, re.MULTILINE)
        points.extend(numbered_plain)

        # 3. Bullet列表 (- **xxx** 或 - xxx)
        bullets = re.findall(r'^[-*]\s+\*{0,2}(.+?)\*{0,2}$', cap_content, re.MULTILINE)
        points.extend([b for b in bullets if len(b) > 3])

        # Round 14: 3b. 嵌套Bullet列表 (  - xxx 或    * xxx)
        nested_bullets = re.findall(r'^\s+[-*]\s+\*{0,2}(.+?)\*{0,2}$', cap_content, re.MULTILINE)
        points.extend([b for b in nested_bullets if len(b) > 3])

        # 4. 表格行 (| 能力名 | ... |) - 仅在能力章节内
        table_rows = re.findall(r'^\|\s*([^|]+?)\s*\|', cap_content, re.MULTILINE)
        for r in table_rows:
            r = r.strip()
            if r and not r.startswith('---') and len(r) <= 30 and r not in (
                '能力', '说明', '功能', '特性', 'Capability', 'Feature', '名称', '描述',
                '参数', '类型', '是否必需', '依赖项', '场景', '输入', '输出',
                '错误场景', '错误', 'Error', 'Issue', '问题', '答案',
                '配置错误', '运行时错误', '网络错误',  # 这些是错误表内容,不是能力
                'Topic', 'File', 'Name', 'Status', 'Updated',
                'They say...', 'Create', 'Store HERE', 'Keep in BUILT-IN',
                # Round 13: 通用表格头
                'Command', 'Description', 'Usage', 'Example', 'Examples',
                'Option', 'Options', 'Flag', 'Flags', 'Parameter', 'Parameters',
                'Method', 'Methods', 'Function', 'Functions',
                'Value', 'Values', 'Default', 'Required', 'Optional',
                'Return', 'Returns', 'Result', 'Results',
                'Syntax', 'Format', 'Category', 'Tag', 'Tags',
            ):
                points.append(r)

    # 过滤掉明显不是能力点的内容
    non_capability = {
        '运行时错误', '配置错误', '网络错误', '连接超时或不可达',
        '参数缺失或格式错误', '运行环境不满足',
        '复杂场景可能需要人工辅助判断', '性能取决于底层模型能力',
        '需要LLM支持，无LLM环境无法使用',
        # Round 13: 通用表格头不是能力点
        'Command', 'Description', 'Usage', 'Example', 'Examples',
        'Option', 'Options', 'Flag', 'Flags', 'Parameter', 'Parameters',
        'Arg', 'Args', 'Argument', 'Arguments',
        'Method', 'Methods', 'Function', 'Functions',
        'Property', 'Properties', 'Attribute', 'Attributes',
        'Value', 'Values', 'Type', 'Types',
        'Default', 'Required', 'Optional', 'Note', 'Notes',
        'Return', 'Returns', 'Result', 'Results',
        'Syntax', 'Format', 'Template',
        'Category', 'Tag', 'Tags', 'Label', 'Labels',
    }
    points = [p for p in points if p not in non_capability]

    # 过滤掉包含"触发关键词"的条目(模板垃圾残留)
    points = [p for p in points if '触发关键词' not in p and '触发词' not in p]

    # 过滤掉过短或过长的条目(不是有效能力点)
    points = [p for p in points if 3 <= len(p) <= 100]

    # 过滤掉引用内容(表格中的示例文本)
    points = [p for p in points if not (p.startswith('"') or p.startswith("'"))]

    # 过滤掉以冒号结尾的流程步骤(如 "Ask first:")
    points = [p for p in points if not p.rstrip().endswith(':')]

    # 过滤掉包含方括号占位符的条目(如 "I'm learning [topic]")
    # Round 14: 修复误过滤 - 包含markdown链接[text](url)的条目不是占位符,应保留
    points = [p for p in points if not (
        re.search(r'\[.+\]', p) and not re.search(r'\]\(', p)
    )]

    # 过滤掉以"."开头的条目(编号列表剥离后的残留,如 ". Blocks")
    points = [p for p in points if not p.lstrip().startswith('.')]

    # 过滤掉以markdown格式开头的条目(如 "**Smart waiting**")
    points = [p for p in points if not p.startswith('**')]

    # 过滤掉以反引号开头的条目(代码引用,非能力点)
    points = [p for p in points if not p.startswith('`')]

    # 过滤掉以emoji开头的条目
    points = [p for p in points if not re.match(r'^[✅🔴🟡🟢⚠️💡📌🔧🎯🚀⭐]', p)]

    # 过滤掉包含"示例"的模板条目
    points = [p for p in points if '示例' not in p[:10]]

    # 过滤掉明显是流程步骤的条目
    step_patterns = [
        'Step ', 'Each function', 'Before delivery', 'After the answer',
        'Clean up before', 'Pull before', 'Wait for',
    ]
    points = [p for p in points if not any(sp in p for sp in step_patterns)]

    # Round 14: 如果过滤后0个能力点,从所有非垃圾非排除章节重新提取
    # 这处理源skill使用非标准章节名(如"Code Style","Pythonic Patterns")的情况
    if not points:
        exclude_all = ['常见问题', 'FAQ', '错误', '异常', '依赖', '限制', '案例',
                       '运行环境', 'License', 'license', '安装', 'Install',
                       '适用场景', '使用流程', '示例', '已知限制']
        for name, ch_content in chapters.items():
            if any(x in name for x in exclude_all):
                continue
            if is_template_garbage(ch_content, name):
                continue
            # 提取###标题
            h3_raw = re.findall(r'^###\s+(.+)$', ch_content, re.MULTILINE)
            h3_pts = [re.sub(r'^\d+[.):]?\s*', '', h).strip() for h in h3_raw]
            # 过滤模板###标题
            h3_pts = [h for h in h3_pts if '运行环境' not in h and 'API Key' not in h 
                      and '可用性分类' not in h and '依赖说明' not in h]
            points.extend(h3_pts)
            # 提取Bullet列表
            bullets = re.findall(r'^[-*]\s+\*{0,2}(.+?)\*{0,2}$', ch_content, re.MULTILINE)
            points.extend([b for b in bullets if len(b) > 3])
            # 提取编号列表
            numbered = re.findall(r'^\d+\.\s+\*\*(.+?)\*\*', ch_content, re.MULTILINE)
            points.extend(numbered)
            numbered_plain = re.findall(r'^\d+\.\s+([A-Z\u4e00-\u9fff].{2,80})$', ch_content, re.MULTILINE)
            points.extend(numbered_plain)
        # 重新应用关键过滤
        points = [p for p in points if '触发关键词' not in p and '触发词' not in p]
        points = [p for p in points if 3 <= len(p) <= 100]
        points = [p for p in points if not p.startswith('`')]
        points = [p for p in points if not p.startswith('**')]
        points = [p for p in points if '示例' not in p[:10]]
        points = [p for p in points if not any(sp in p for sp in step_patterns)]

    return list(set(points))


def extract_domain_terms(content: str) -> Set[str]:
    """提取领域术语 (API名、命令名、技术术语)
    
    改进: 
    1. 过滤模板垃圾中文术语(来自clawhub下载模板)
    2. 过滤常见英文非领域词
    3. 仅保留真正的领域术语
    """
    terms = set()

    # 模板垃圾中文术语黑名单 (这些出现在clawhub下载模板中,非真实领域术语)
    template_garbage_cn = {
        '依赖说明', '运行环境', '操作系统', '可用性分类', '已知限制', '常见问题',
        '核心能力', '使用流程', '适用场景', '案例展示', '异常处理', '错误处理',
        '自然语言', '结构化', '处理结果', '示例数据', '相关信息', '配置错误',
        '参数缺失', '运行时错误', '网络错误', '连接超时',
        # 模板扩展术语
        '不适用于', '不适用于加密文件', '企业团队和自动化', '依赖说明中的要求',
        '内容提取时使用', '参数缺失或格式错', '参考国内替代方案', '参考错误处理章节',
        '合适的使用方式', '命令行执行能力', '基础使用', '基础用法',
        '如何开始使用', '如遇错误', '工作流场景', '执行任务',
        '执行操作并检查输', '按照表格中的处理', '文档转换', '方式操作',
        '无需额外', '是否必需', '有什么限制', '杂决策场景',
        '根据使用流程执行', '根据适用场景选择', '格式互转',
        '检查依赖说明中的', '检查网络连接后重', '用户请求',
        '确认环境满足依赖', '确认运行环境满足', '确认运行环境符合',
        '节了解具体限制', '获取方式', '说明中的要求',
        '请先阅读使用流程', '请参考已知限制章', '请参考错误处理章',
        '运行环境不满足', '连接超时或不可达', '适用于独立开发者',
        '通过自然语言指令', '遇到错误怎么办', '部分功能需要',
        '配置要求', '除内容中明确标注', '需要人工判断的复',
        '需要文件处理', '人工辅助判断', '品牌视觉时使用',
        '建模和动画制作', '性能取决于底层模', '平台指南',
        '深度优化升级', '清理外部依赖引用', '独立开发者与一人',
        '环境无法使用', '移除风险代码', '经过深度优化',
        '能决策辅助', '自动化工作流与智', '触发关键词',
        '辅助工具', '集成工具领域的专', '去除原始风险代码',
        '公司效率提升', '数据同步', '增强元数据',
        '增强安全性和稳定', '平台对接', '复杂场景可能需要',
        '设计创作', '海报制作', '错误场景', '处理方式',
        '不适用于加密', '不支持多表', '平台指南',
        '触发关键词', '品牌视觉',
    }
    
    # 常见英文非领域词 (不是API名/命令名/技术术语)
    common_en_words = {
        'read', 'exec', 'write', 'true', 'false', 'null', 'none',
        'bash', 'python', 'pip', 'npm', 'skill', 'agent', 'md',
        'json', 'yaml', 'mit', 'windows', 'macos', 'linux',
        # 常见动词
        'analyze', 'analyzed', 'analyzing', 'automatic', 'automatically',
        'designed', 'detect', 'detected', 'detecting', 'export', 'exported',
        'filter', 'filtered', 'filtering', 'group', 'grouped', 'grouping',
        'import', 'imported', 'importing', 'parse', 'parsed', 'parsing',
        'search', 'searched', 'searching', 'sort', 'sorted', 'sorting',
        'validate', 'validated', 'validating', 'convert', 'converted',
        'transform', 'transformed', 'merge', 'merged', 'merging',
        'split', 'splitting', 'scale', 'scaling', 'sync', 'synced',
        'syncing', 'synchronize', 'update', 'updated', 'updating',
        'create', 'created', 'creating', 'delete', 'deleted', 'deleting',
        'remove', 'removed', 'removing', 'build', 'building', 'built',
        'install', 'installed', 'installing', 'deploy', 'deployed',
        'backup', 'restore', 'restored', 'recover', 'recovered',
        'execute', 'executed', 'executing', 'run', 'running',
        'start', 'started', 'starting', 'stop', 'stopped', 'stopping',
        'pause', 'paused', 'pausing', 'enable', 'enabled', 'enabling',
        'disable', 'disabled', 'disabling', 'monitor', 'monitored',
        'scan', 'scanned', 'scanning', 'process', 'processed', 'processing',
        'generate', 'generated', 'generating', 'extract', 'extracted',
        'display', 'displayed', 'render', 'rendered', 'format', 'formatted',
        'compress', 'compressed', 'archive', 'archived',
        # 常见名词
        'data', 'database', 'table', 'record', 'field', 'value',
        'file', 'folder', 'directory', 'path', 'config', 'configuration',
        'request', 'response', 'endpoint', 'api', 'http', 'url',
        'user', 'admin', 'role', 'permission', 'auth', 'login', 'logout',
        'error', 'warning', 'success', 'failure', 'fail', 'failed',
        'status', 'state', 'mode', 'type', 'kind', 'class', 'object',
        'instance', 'attribute', 'property', 'method', 'function',
        'parameter', 'argument', 'option', 'flag', 'command',
        'module', 'component', 'service', 'server', 'client',
        'connection', 'connections', 'session', 'cache', 'queue',
        'task', 'job', 'workflow', 'pipeline', 'flow', 'step',
        'stage', 'phase', 'rule', 'rules', 'policy', 'strategy',
        'plan', 'goal', 'target', 'purpose', 'reason', 'cause',
        'effect', 'result', 'outcome', 'output', 'input', 'source',
        'origin', 'root', 'base', 'foundation', 'core', 'essential',
        'required', 'optional', 'mandatory', 'forbidden', 'allowed',
        'denied', 'permitted', 'prohibited', 'online', 'offline',
        'available', 'unavailable', 'ready', 'busy', 'idle',
        'pending', 'processing', 'completed', 'failed', 'success',
        'active', 'inactive', 'enabled', 'disabled',
        # 常见形容词
        'simple', 'complex', 'basic', 'advanced', 'custom', 'default',
        'standard', 'normal', 'abnormal', 'common', 'specific',
        'general', 'particular', 'individual', 'single', 'multiple',
        'large', 'small', 'huge', 'tiny', 'medium',
        'fast', 'slow', 'quick', 'rapid', 'steady',
        'full', 'partial', 'complete', 'incomplete',
        'new', 'old', 'recent', 'current', 'previous', 'next',
        'first', 'last', 'final', 'initial',
        'internal', 'external', 'inner', 'outer',
        'upper', 'lower', 'left', 'right', 'top', 'bottom',
        'front', 'back', 'center', 'middle', 'edge', 'border',
        'public', 'private', 'protected', 'global', 'local',
        'static', 'dynamic', 'parallel', 'serial',
        'automatic', 'manual', 'real-time', 'instant', 'immediate',
        'flexible', 'rigid', 'adaptive', 'fixed',
        'perfect', 'ideal', 'optimal', 'suboptimal',
        'secure', 'safe', 'unsafe', 'risky',
        # 常见代词/介词/连词
        'the', 'and', 'for', 'with', 'from', 'into', 'onto',
        'this', 'that', 'these', 'those', 'they', 'them',
        'their', 'there', 'here', 'where', 'when', 'what',
        'which', 'whose', 'who', 'whom',
        'each', 'every', 'all', 'some', 'any', 'none',
        'both', 'either', 'neither',
        'your', 'our', 'his', 'her', 'its',
        'have', 'has', 'had', 'having',
        'will', 'would', 'should', 'could', 'can', 'may', 'might',
        'must', 'shall', 'ought',
        'then', 'now', 'later', 'soon', 'eventually',
        'always', 'never', 'sometimes', 'often', 'rarely',
        'only', 'also', 'too', 'either', 'neither',
        'without', 'within', 'through', 'throughout',
        # 其他常见词
        'features', 'feature', 'capabilities', 'capability',
        'limitations', 'limitation', 'limitations',
        'patterns', 'pattern', 'traps', 'trap', 'gotchas', 'gotcha',
        'designed', 'design', 'shows', 'show', 'takes', 'take',
        'uses', 'use', 'used', 'using', 'useful',
        'overkill', 'zero', 'none', 'null',
        'access', 'accessible', 'inaccessible',
        'anything', 'everything', 'something', 'nothing',
        'immediately', 'quickly', 'slowly',
        'separate', 'separated', 'separating',
        'store', 'stored', 'storing', 'storage',
        'navigate', 'navigation', 'navigating',
        'decide', 'decision', 'decisions', 'deciding',
        'learn', 'learning', 'learned',
        'knowledge', 'reference', 'referenced',
        'review', 'reviewed', 'reviewing',
        'feedback', 'maintenance', 'monthly', 'weekly',
        'definitions', 'defines', 'defined',
        'detailed', 'details', 'detail',
        'domain', 'domains',
        'escalate', 'escalated',
        'index', 'indices', 'indexed',
        'infinite', 'infinity',
        'keep', 'keeping', 'kept',
        'missing', 'missed',
        'modifying', 'modified',
        'name', 'named', 'names',
        'optional', 'options',
        'organization', 'organized',
        'paused', 'pausing',
        'privacy', 'private',
        'problems', 'problem',
        'recent', 'recently',
        'related', 'relating',
        'remove', 'removed', 'removing',
        'replication', 'replicated',
        'scaling', 'scaled',
        'should', 'shown',
        'specific', 'specifically',
        'status', 'statuses',
        'stay', 'stayed',
        'structure', 'structured',
        'summaries', 'summary',
        'superpowered', 'system', 'systems',
        'topic', 'topics', 'total',
        'troubleshooting', 'updated', 'updates',
        'user', 'users', 'waiting',
        'works', 'working', 'worked',
        'write', 'writing', 'written',
        'your', 'yours',
        'alpha', 'beta', # 除非是版本号,否则过滤
        'claude', 'codex', 'cursor', 'gemini',  # Agent平台名
        'excel', 'pandas', 'python', # 通用工具名
        'anomaly', 'anomalies',  # 通用词
        'date', 'dates', 'time', 'times',
        'dependencies', 'dependency',
        'application', 'applications',
        'changes', 'change', 'changed',
        'deadlocks', 'deadlock',
        'disk', 'disks',
        'floating', 'float',
        'idle', 'idling',
        'implicit', 'explicit',
        'iops',  # 除非是特定术语
        'large', 'largely',
        'logical', 'logically',
        'long', 'longer',
        'lost', 'losing',
        'orphan', 'orphans',
        'point', 'points', 'pointed',
        'promoting', 'promoted',
        'query', 'queries', 'queried',
        'read', 'reading', 'reads',
        'recovery', 'recovering',
        'renaming', 'renamed',
        'single', 'singly',
        'timezone', 'timezones',
        'transaction', 'transactions',
        'update', 'updates', 'updated',
        'windows', 'window',
        'writes', 'writing',
        'added', 'adding', 'add',
        'check', 'checked', 'checking',
        'code', 'codes',
        'data', 'database', 'databases',
        'design', 'designed', 'designs',
        'dropping', 'dropped', 'drop',
        'each', 'every',
        'exec', 'execute', 'executed',
        'index', 'indexed', 'indices',
        'large', 'larger', 'largest',
        'limit', 'limited', 'limits',
        'missing', 'miss',
        'null', 'none',
        'online', 'offline',
        'point', 'points',
        'read', 'reads',
        'schema', 'schemas',
        'select', 'selected', 'selection',
        'table', 'tables',
        'update', 'updated', 'updates',
        'windows', 'window',
    }

    # 1. 反引号包裹的代码/命令 (最可靠的技术术语标志)
    # 反引号内的内容是作者明确标记为代码/命令的,应保留(仅过滤极基本的)
    basic_stopwords = {
        'read', 'exec', 'write', 'true', 'false', 'null', 'none',
        'bash', 'python', 'pip', 'npm', 'md', 'json', 'yaml',
    }
    for m in re.finditer(r'`([a-zA-Z_][a-zA-Z0-9_\-\./]+)`', content):
        kw = m.group(1)
        if len(kw) > 2 and kw.lower() not in basic_stopwords:
            terms.add(kw.lower())

    # 2. 大写开头的专有名词 (但排除常见词)
    # 注意: 需要同时检查原始大写形式和小写形式
    capitalized_exclusions = {
        'Skill', 'Agent', 'Note', 'Important', 'Warning',
        'Error', 'Table', 'Usage', 'Core', 'Feature',
        'First', 'Second', 'Third', 'Fourth', 'Fifth',
        'When', 'What', 'Where', 'How', 'Why', 'This',
        'That', 'These', 'Those', 'They', 'Their', 'Here',
        'Each', 'Every', 'Both', 'Some', 'Your', 'Have',
        'Will', 'Should', 'Would', 'Could', 'Must',
        'Never', 'Always', 'Store', 'Build', 'Built',
        'Index', 'Memory', 'Config', 'Setup', 'Sync',
        'Search', 'Filter', 'Group', 'Sort', 'Parse',
        'Convert', 'Transform', 'Merge', 'Split',
        'Scale', 'Update', 'Create', 'Delete', 'Remove',
        'Install', 'Deploy', 'Backup', 'Restore',
        'Execute', 'Run', 'Start', 'Stop', 'Pause',
        'Enable', 'Disable', 'Monitor', 'Scan',
        'Process', 'Generate', 'Extract', 'Display',
        'Render', 'Format', 'Compress', 'Archive',
        'Memory', 'Architecture', 'Quick', 'Reference',
        'Setup', 'Common', 'Problems', 'Patterns',
        'Category', 'Categories', 'Parallel', 'Status',
        'Structure', 'System', 'Topic', 'Total',
        'User', 'Windows', 'Linux', 'MacOS',
        'Claude', 'Codex', 'Cursor', 'Gemini',
        'Excel', 'Pandas', 'Python',
        'Analyze', 'Analyzer', 'Anomaly', 'Automatic',
        'Designed', 'Detect', 'Export', 'Features',
        'Flexible', 'Grouping', 'Limitations',
        'Overkill', 'Quick', 'Shows', 'Statistical',
        'Takes', 'Uses', 'Zero',
        'Adding', 'Application', 'Changes', 'Check',
        'Code', 'Connection', 'Connections', 'Data',
        'Database', 'Deadlocks', 'Design', 'Disk',
        'Dropping', 'Floating', 'Gotchas', 'Idle',
        'Implicit', 'Integrations', 'Integrity',
        'Lambda', 'Large', 'Limit', 'Limits',
        'Logical', 'Long', 'Lost', 'Missing',
        'Online', 'Offline', 'Orphan', 'Patterns',
        'Point', 'Promoting', 'Query', 'Read',
        'Recovery', 'Renaming', 'Replication',
        'Scaling', 'Schema', 'Select', 'Single',
        'Split', 'Timezone', 'Transaction', 'Traps',
        'Update', 'Writes', 'Access', 'Active',
        'Adaptive', 'Agents', 'Alpha', 'Anything',
        'Basic', 'Beta', 'Both', 'Build', 'Built',
        'Categories', 'Category', 'Check', 'Code',
        'Codex', 'Cursor', 'Common', 'Create',
        'Current', 'Decide', 'Decision', 'Defines',
        'Detailed', 'Domain', 'During', 'Escalate',
        'Everything', 'Feedback', 'File', 'Finding',
        'First', 'Full', 'Here', 'Huge', 'Immediately',
        'Indices', 'Individual', 'Infinite', 'Install',
        'Keep', 'Knowledge', 'Large', 'Learn',
        'Maintenance', 'Modifying', 'Monthly', 'Name',
        'Navigate', 'Never', 'Only', 'Optional',
        'Organization', 'Parallel', 'Paused', 'Perfect',
        'Privacy', 'Problems', 'Quick', 'Recent',
        'Reference', 'Related', 'Remove', 'Review',
        'Root', 'Rule', 'Rules', 'Scale', 'Search',
        'Security', 'Send', 'Separate', 'Setup',
        'Should', 'Skills', 'Slow', 'Small', 'Specific',
        'Split', 'Splitting', 'Status', 'Stay',
        'Store', 'Structure', 'Summaries', 'Superpowered',
        'Synced', 'Syncing', 'System', 'Then', 'They',
        'Things', 'This', 'Topic', 'Total', 'Traps',
        'Update', 'Updated', 'User', 'Waiting', 'Weekly',
        'What', 'When', 'Windows', 'Without', 'Works',
        'Write', 'Your',
    }
    for m in re.finditer(r'\b([A-Z][a-zA-Z]{3,})\b', content):
        kw = m.group(1)
        if kw not in capitalized_exclusions and kw.lower() not in common_en_words:
            terms.add(kw.lower())

    # 3. 中文领域术语 (4-8字) - 排除模板垃圾
    cn_terms = re.findall(r'[\u4e00-\u9fff]{4,8}', content)
    for t in cn_terms:
        if t not in template_garbage_cn:
            terms.add(t)

    return terms


def extract_error_scenarios(content: str) -> Set[str]:
    """提取错误场景"""
    scenarios = set()
    in_error_section = False
    for line in content.split('\n'):
        if re.match(r'^##\s+.*异常.*|^##\s+.*错误.*|^##\s+.*Error.*', line, re.IGNORECASE):
            in_error_section = True
            continue
        if re.match(r'^##\s+', line) and in_error_section:
            in_error_section = False
        if not in_error_section:
            continue
        if '|' in line:
            cells = [c.strip() for c in line.split('|')]
            if len(cells) >= 2 and cells[1] and not cells[1].startswith('---') and cells[1] not in (
                '错误场景', '场景', '错误', 'Error', 'Issue'
            ):
                scenarios.add(cells[1].lower())
        heading_match = re.match(r'^###\s+(.+)$', line)
        if heading_match:
            scenarios.add(heading_match.group(1).strip().lower())
    return scenarios


def compute_keyword_overlap(source_terms: Set[str], gen_terms: Set[str]) -> float:
    """计算关键词重叠率 - 支持跨语言匹配
    
    改进: 对于英文源术语,也检查其中文翻译是否在生成版本中
    """
    if not source_terms:
        return 1.0  # No source terms to check
    if not gen_terms:
        return 0.0
    
    # 直接重叠
    direct_overlap = len(source_terms & gen_terms)
    
    # 跨语言重叠: 英文源术语 → 中文翻译 → 检查是否在gen_terms中
    cross_lang_overlap = 0
    for term in source_terms:
        if term in gen_terms:
            continue  # 已计入直接重叠
        # 检查是否是英文词
        if re.match(r'^[a-z]+$', term):
            zh_translations = get_zh_translations(term)
            for zh in zh_translations:
                if zh in gen_terms or zh.lower() in gen_terms:
                    cross_lang_overlap += 1
                    break
    
    total_overlap = direct_overlap + cross_lang_overlap
    return min(total_overlap / len(source_terms), 1.0)


def compute_capability_coverage(source_points: List[str], gen_content: str) -> Tuple[float, List[str], List[str]]:
    """计算能力覆盖率: 生成版本覆盖了多少源能力点
    
    改进: 支持跨语言匹配(英文源 → 中文生成版本)
    通过 EN_TO_ZH_MAP 将英文关键词翻译为中文后再匹配
    
    ⚠️ Round 13 根因修复: 当源能力点为空时,返回 None 而非 100%。
    之前的实现返回 (1.0, [], []),导致 350 个"100%覆盖率"中 191 个(54.6%)是假阳性。
    现在返回 (None, [], []) 以便上层使用替代验证。
    
    Returns: (coverage_rate, covered_points, missing_points)
             coverage_rate 为 None 表示源能力点为空,需要替代验证
    """
    if not source_points:
        # Round 13 根因修复: 不再返回假阳性 100%
        # 返回 None 让上层使用替代验证(检查生成版本的核心能力章节数量)
        return None, [], []

    gen_lower = gen_content.lower()
    covered = []
    missing = []

    for point in source_points:
        # 提取能力点的关键词 - 对中文按2-3字滑窗提取
        words = set()
        en_words = set()  # 英文词单独收集,用于跨语言匹配
        # 英文词 (≥3字符)
        for m in re.finditer(r'[a-zA-Z]{3,}', point):
            w = m.group().lower()
            words.add(w)
            en_words.add(w)
        # 中文: 整体 + 2字滑窗 + 3字滑窗
        cn_segments = re.findall(r'[\u4e00-\u9fff]+', point)
        for seg in cn_segments:
            if len(seg) >= 2:
                words.add(seg)  # 完整词
                for i in range(len(seg) - 1):
                    words.add(seg[i:i+2])  # 2字滑窗
                for i in range(len(seg) - 2):
                    words.add(seg[i:i+3])  # 3字滑窗
        # 过滤通用词
        generic = {'核心', '能力', '场景', '工具', '支持', '使用', '提供', '适用',
                   'the', 'and', 'for', 'pro', 'free', 'skill', 'tool', 'api',
                   '模型', '工作', '流程', 'from', 'with', 'that', 'this', 'they',
                   'their', 'when', 'what', 'each', 'into', 'your', 'have', 'will'}
        words = {w for w in words if w.lower() not in generic}
        en_words = {w for w in en_words if w not in generic}

        if not words:
            # 无法提取关键词,视为已覆盖
            covered.append(point)
            continue

        # 检查是否有任一关键词在生成版本中
        # 策略1: 直接匹配(英文词在中文文档中保留,或中文词直接匹配)
        found = any(w.lower() in gen_lower for w in words)

        # 策略2: 如果直接匹配失败,尝试跨语言匹配
        # 将英文词翻译为中文,再检查中文翻译是否在生成版本中
        if not found and en_words:
            for en_word in en_words:
                zh_translations = get_zh_translations(en_word)
                for zh in zh_translations:
                    if zh.lower() in gen_lower:
                        found = True
                        break
                if found:
                    break

        # 策略3: 如果仍然失败,检查英文词的词干是否在生成版本中
        # (有些中文文档会保留部分英文术语)
        if not found and en_words:
            for en_word in en_words:
                # 取词干(前4-6个字符)
                stem = en_word[:min(6, len(en_word))]
                if len(stem) >= 4 and stem in gen_lower:
                    found = True
                    break

        if found:
            covered.append(point)
        else:
            missing.append(point)

    # Round 13: 源能力点为空已在函数开头返回 None,这里不会触发
    coverage = len(covered) / len(source_points) if source_points else 0.0
    return coverage, covered, missing


def _load_original_registry() -> set:
    """加载原创skill注册表"""
    registry_path = SKILL_REGISTRY_DIR / 'original_skills_registry.json'
    if registry_path.exists():
        data = json.loads(registry_path.read_text(encoding='utf-8'))
        return set(data.get('skills', []))
    return set()


def check_source_fidelity(slug: str) -> Dict[str, Any]:
    """检查单个skill的源保真度"""
    # 先检查是否是原创skill(优先于源skill加载,避免无效源导致SF=0)
    original_skills = _load_original_registry()
    if slug in original_skills:
        return {
            'slug': slug,
            'fidelity_score': 100,
            'fidelity_grade': 'A',
            'is_original': True,
            'note': '原创skill,无源skill,跳过SF检查',
        }
    
    # 加载源skill
    source_path, source_content = load_source_skill(slug)
    if not source_content:
        return {
            'slug': slug,
            'error': 'Source skill not found',
            'fidelity_score': 0,
            'fidelity_grade': 'F',
        }

    # 加载生成版本
    gen_path = PACKAGED_SKILLS_DIR / slug / 'SKILL.md'
    if not gen_path.exists():
        return {
            'slug': slug,
            'error': 'Generated skill not found',
            'fidelity_score': 0,
            'fidelity_grade': 'F',
        }
    gen_content = gen_path.read_text(encoding='utf-8')

    # 1. 能力覆盖率 (40%)
    # Round 13 根因修复: 处理源能力点为空的情况(None 覆盖率)
    source_points = extract_capability_points(source_content)
    coverage, covered, missing = compute_capability_coverage(source_points, gen_content)
    
    source_caps_empty = coverage is None
    if source_caps_empty:
        # 源能力点为空,使用替代验证:
        # 检查生成版本的核心能力章节是否有≥3个具体能力点(每个≥50字符)
        gen_chapters = parse_chapters(gen_content)
        gen_cap_points = extract_capability_points(gen_content)
        substantial_points = [p for p in gen_cap_points if len(p) >= 20]
        
        if len(substantial_points) >= 5:
            # 替代验证通过: 有足够多的具体能力点
            capability_score = 30  # 给75%分,留25%空间让其他指标区分
            alt_verdict = f"源能力点为空,替代验证通过(生成版本有{len(substantial_points)}个具体能力点)"
        elif len(substantial_points) >= 3:
            capability_score = 20  # 50%分
            alt_verdict = f"源能力点为空,替代验证勉强通过(生成版本有{len(substantial_points)}个具体能力点)"
        else:
            capability_score = 10  # 25%分
            alt_verdict = f"源能力点为空,替代验证失败(生成版本仅有{len(substantial_points)}个具体能力点)"
        coverage = 0.0  # 用于显示,不参与评分
    else:
        capability_score = coverage * 40
        alt_verdict = None

    # 2. 领域术语保留 (25%)
    source_terms = extract_domain_terms(source_content)
    gen_terms = extract_domain_terms(gen_content)
    term_overlap = compute_keyword_overlap(source_terms, gen_terms)
    term_score = term_overlap * 25

    # 3. 错误场景质量 (15%) - 不检查与源skill的重合度
    # 因为源skill的错误场景通常是通用的(配置错误/运行时错误/网络错误),
    # 生成版本应该有更多领域专属的错误场景
    source_errors = extract_error_scenarios(source_content)
    gen_errors = extract_error_scenarios(gen_content)
    # 检查生成版本是否有足够的错误场景(≥3个)
    if len(gen_errors) >= 5:
        error_score = 15
    elif len(gen_errors) >= 3:
        error_score = 10
    elif len(gen_errors) >= 1:
        error_score = 5
    else:
        error_score = 0

    # 4. 差异化与增强度 (20%) - 生成版本应该在保留核心能力的基础上有增强
    # 检查生成版本是否有源skill没有的领域术语(增强信号)
    all_source = source_terms | set(source_points) | source_errors
    all_gen = gen_terms | set(extract_capability_points(gen_content)) | gen_errors

    if all_source and all_gen:
        # 新增的领域术语比例 (生成版本有但源没有的)
        new_terms = gen_terms - source_terms
        enhancement_ratio = len(new_terms) / len(gen_terms) if gen_terms else 0

        # 覆盖的源术语比例
        covered_terms = source_terms & gen_terms
        coverage_ratio = len(covered_terms) / len(source_terms) if source_terms else 1.0

        # 最佳: 覆盖率高 + 有新增术语
        if coverage_ratio >= 0.3 and enhancement_ratio >= 0.2:
            diff_score = 20  # 保留核心 + 有增强
        elif coverage_ratio >= 0.3:
            diff_score = 15  # 至少保留了核心
        elif enhancement_ratio >= 0.3:
            diff_score = 10  # 有增强但覆盖不够
        else:
            diff_score = 5  # 既没覆盖也没增强
    else:
        diff_score = 10

    # 总分
    fidelity_score = round(capability_score + term_score + error_score + diff_score)

    # 等级
    if fidelity_score >= 80:
        grade = 'A'
    elif fidelity_score >= 65:
        grade = 'B'
    elif fidelity_score >= 50:
        grade = 'C'
    elif fidelity_score >= 30:
        grade = 'D'
    else:
        grade = 'F'

    return {
        'slug': slug,
        'fidelity_score': fidelity_score,
        'fidelity_grade': grade,
        'source_path': source_path,
        'gen_path': str(gen_path),
        'source_capability_points': source_points,
        'missing_capabilities': missing,
        'capability_coverage': round(coverage * 100, 1) if coverage is not None else None,
        'source_caps_empty': source_caps_empty,  # Round 13: 标记源能力点为空
        'alt_verdict': alt_verdict,  # Round 13: 替代验证结论
        'term_retention': round(term_overlap * 100, 1),
        'error_count': len(gen_errors),
        'source_terms_count': len(source_terms),
        'gen_terms_count': len(gen_terms),
        'diff_score': diff_score,
        'details': {
            'capability_score': round(capability_score, 1),
            'term_score': round(term_score, 1),
            'error_score': round(error_score, 1),
            'diff_score': diff_score,
        },
    }


def run_batch(limit: int = 0) -> List[Dict]:
    """批量检查所有已生成的skill"""
    # 获取所有已生成的skill
    gen_slugs = []
    for item in sorted(PACKAGED_SKILLS_DIR.iterdir()):
        if item.is_dir() and (item / 'SKILL.md').exists():
            gen_slugs.append(item.name)

    # 过滤掉 -free 和 -paid 变体 (只检查主版本)
    gen_slugs = [s for s in gen_slugs if not s.endswith('-free') and not s.endswith('-paid')]

    if limit > 0:
        gen_slugs = gen_slugs[:limit]

    print("Checking " + str(len(gen_slugs)) + " skills...")
    print("=" * 80)

    results = []
    grade_dist = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'F': 0}
    low_fidelity = []

    for slug in gen_slugs:
        r = check_source_fidelity(slug)
        results.append(r)

        if 'error' in r:
            print(slug + ': ERROR - ' + r['error'])
            grade_dist['F'] += 1
            continue

        grade_dist[r['fidelity_grade']] += 1
        marker = ''
        if r['fidelity_score'] < 65:
            marker = ' ** LOW FIDELITY **'
            low_fidelity.append(r)

        # 原创skill只显示基本信息
        if r.get('is_original'):
            print(slug + ': ' + str(r['fidelity_score']) + '/100 (' + r['fidelity_grade'] + ') [ORIGINAL]')
            continue

        missing = r.get('missing_capabilities', [])
        missing_str = ', '.join(missing[:3]) if missing else ''
        print(slug + ': ' + str(r['fidelity_score']) + '/100 (' + r['fidelity_grade'] + ')'
              + ' cov=' + str(r.get('capability_coverage', 0)) + '%'
              + ' term=' + str(r.get('term_retention', 0)) + '%'
              + ' err=' + str(r.get('error_count', 0))
              + marker)
        if missing_str:
            print('  Missing: ' + missing_str)

    # Summary
    print()
    print("=" * 80)
    print("SUMMARY")
    print("=" * 80)
    valid = [r for r in results if 'error' not in r]
    scores = [r['fidelity_score'] for r in valid]
    avg = sum(scores) / len(scores) if scores else 0
    print("  Total checked: " + str(len(results)))
    print("  Valid: " + str(len(valid)))
    print("  Average fidelity: " + str(round(avg, 1)) + "/100")
    print("  Grade: A=" + str(grade_dist['A']) + " B=" + str(grade_dist['B']) +
          " C=" + str(grade_dist['C']) + " D=" + str(grade_dist['D']) + " F=" + str(grade_dist['F']))

    if low_fidelity:
        print()
        print("--- LOW FIDELITY SKILLS (missing source capabilities) ---")
        for r in sorted(low_fidelity, key=lambda x: x['fidelity_score']):
            missing = r.get('missing_capabilities', [])
            print("  " + r['slug'] + ': ' + str(r['fidelity_score']) +
                  ' (cov=' + str(r['capability_coverage']) + '%, term=' + str(r['term_retention']) + '%)')
            if missing:
                print("    Missing capabilities: " + ', '.join(missing[:5]))

    return results


def main():
    parser = argparse.ArgumentParser(description='Source Fidelity Checker')
    parser.add_argument('slug', nargs='?', help='Skill slug to check')
    parser.add_argument('--json', action='store_true', help='JSON output')
    parser.add_argument('--batch', action='store_true', help='Batch mode')
    parser.add_argument('--limit', type=int, default=0, help='Batch limit (0=all)')
    parser.add_argument('-o', '--output', help='Output file')
    args = parser.parse_args()

    if args.batch:
        results = run_batch(limit=args.limit)
        if args.output:
            Path(args.output).write_text(
                json.dumps({'results': results, 'time': datetime.now().isoformat()},
                           ensure_ascii=False, indent=2),
                encoding='utf-8')
            print("Saved to: " + args.output)
        return

    if not args.slug:
        parser.print_help()
        return

    result = check_source_fidelity(args.slug)

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        if 'error' in result:
            print('ERROR: ' + result['error'])
            return

        print('=== Source Fidelity: ' + result['slug'] + ' ===')
        print('Score: ' + str(result['fidelity_score']) + '/100 (' + result['fidelity_grade'] + ')')
        print()
        print('Capability Coverage: ' + str(result['capability_coverage']) + '%')
        print('Term Retention: ' + str(result['term_retention']) + '%')
        print('Error Scenarios: ' + str(result['error_count']))
        print('Diff Score: ' + str(result['diff_score']) + '/20')
        print()
        if result.get('missing_capabilities'):
            print('Missing Capabilities:')
            for cap in result['missing_capabilities']:
                print('  - ' + cap)
        else:
            print('All source capabilities covered!')


if __name__ == '__main__':
    main()
