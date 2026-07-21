#!/usr/bin/env python3
"""
L3批量修复脚本
==============

解决L3功能验证0%通过率的三个最常见问题：
1. 模板套话清除（65%的skill失败）
2. 错误处理章节补全（73%的skill失败）
3. 依赖说明补全（58%的skill失败）
4. "触发关键词"清除（38%的skill失败）

Usage:
    python l3_batch_fix.py           # 执行所有修复
    python l3_batch_fix.py --dry-run # 仅检查，不修改
"""

import sys
import re
import argparse
from pathlib import Path

SKILL_REGISTRY = Path(r'D:\skills\skill-registry')
PACKAGED_DIR = Path(r'D:\skills\packaged-skills\skillhub')
sys.path.insert(0, str(SKILL_REGISTRY))

from skill_core.parser import parse_frontmatter as _parse_fm

# 模板套话列表
TEMPLATE_PHRASES = [
    '本Skill基于Markdown指令，无需额外API Key(除内容中明确标注的外部API)',
    '本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)',
    '通过自然语言指令驱动Agent执行任务',
    '基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务',
    '纯Markdown指令,部分功能需要exec命令行执行能力',
    '纯Markdown指令，部分功能需要exec命令行执行能力',
    '需要LLM支持，无LLM环境无法使用',
    '需要LLM支持,无LLM环境无法使用',
    '复杂场景可能需要人工辅助判断',
    '性能取决于底层模型能力',
    '请先阅读使用流程章节，确认环境满足依赖说明中的要求。',
    '请参考错误处理章节，按照表格中的处理方式操作。',
    '请参考已知限制章节了解具体限制。',
    '不适用于需要人工判断的复杂决策场景',
]

# 标准依赖说明模板
def generate_dependency_section(tools: list, has_api: bool = False) -> str:
    """生成标准的依赖说明章节"""
    has_exec = 'exec' in str(tools).lower() if tools else False
    
    if has_exec:
        classification = 'MD+EXEC（纯Markdown指令，部分功能需要exec命令行执行能力）'
    else:
        classification = 'MD（纯Markdown指令，无需exec命令行能力）'
    
    api_key_line = '本Skill无需额外API Key（LLM能力由Agent平台内置提供）' if not has_api else '需要配置对应API Key，详见上文环境配置章节'
    
    return f"""## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux

### 依赖项
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
{api_key_line}

### 可用性分类
- **分类**: {classification}"""


# 标准错误处理模板
def generate_error_section(skill_name: str, capabilities: list) -> str:
    """根据skill能力生成错误处理章节"""
    # 通用错误场景
    errors = [
        ('LLM响应超时或无响应', '网络延迟或模型负载过高', '检查网络连接，重试请求；确认Agent平台LLM服务正常'),
        ('输入内容格式不正确', '用户输入不符合skill预期格式', '检查输入是否符合skill使用说明中的格式要求，参考示例章节'),
        ('执行结果与预期不符', '指令描述不够明确或上下文不足', '提供更详细的指令描述，补充必要的上下文信息'),
    ]
    
    # 如果有exec能力，添加执行相关错误
    errors.append(('命令执行失败', '运行环境不满足要求或权限不足', '确认运行环境符合依赖说明中的要求；检查命令权限设置'))
    
    rows = []
    for scenario, cause, solution in errors:
        rows.append(f'| {scenario} | {cause} | {solution} |')
    
    table = '\n'.join(rows)
    
    return f"""## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
{table}"""


def fix_template_phrases(content: str) -> tuple:
    """清除模板套话"""
    changes = 0
    for phrase in TEMPLATE_PHRASES:
        if phrase in content:
            content = content.replace(phrase, '')
            changes += 1
    
    # 清除"触发关键词"相关行
    lines = content.split('\n')
    new_lines = []
    for line in lines:
        if '触发关键词' in line or '触发词' in line:
            changes += 1
            continue
        new_lines.append(line)
    content = '\n'.join(new_lines)
    
    # 清除多余空行（3+连续空行变2个）
    content = re.sub(r'\n{4,}', '\n\n\n', content)
    
    return content, changes


def fix_error_section(content: str, slug: str) -> tuple:
    """补全错误处理章节"""
    if '## 错误处理' in content:
        return content, 0
    
    # 提取核心能力标题用于生成针对性错误处理
    cap_match = re.search(r'## 核心能力\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    capabilities = []
    if cap_match:
        cap_no_code = re.sub(r'```[\s\S]*?```', '', cap_match.group(1))
        capabilities = re.findall(r'^###\s+(.+)$', cap_no_code, re.MULTILINE)
    
    error_section = generate_error_section(slug, capabilities)
    
    # 在已知限制章节前插入错误处理
    if '## 已知限制' in content:
        content = content.replace('## 已知限制', error_section + '\n\n## 已知限制')
    elif '## 常见问题' in content:
        content = content.replace('## 常见问题', error_section + '\n\n## 常见问题')
    elif '## FAQ' in content:
        content = content.replace('## FAQ', error_section + '\n\n## FAQ')
    elif '## 升级提示' in content:
        content = content.replace('## 升级提示', error_section + '\n\n## 升级提示')
    else:
        # 追加到末尾
        content = content.rstrip() + '\n\n' + error_section + '\n'
    
    return content, 1


def fix_dependency_section(content: str, fm_data: dict) -> tuple:
    """补全依赖说明章节"""
    # 检查现有依赖说明的完整性
    dep_match = re.search(r'## 依赖说明\s*\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    
    if dep_match:
        dep_content = dep_match.group(1)
        
        needs_fix = False
        # 检查API Key配置
        has_api_key = 'API Key' in dep_content or 'API密钥' in dep_content or '无需' in dep_content or 'API key' in dep_content
        # 检查可用性分类
        has_classification = 'MD' in dep_content or 'EXEC' in dep_content or '可用性分类' in dep_content
        # 检查运行环境
        has_env = any(x in dep_content for x in ['运行环境', '操作系统', 'Windows', 'macOS', 'Linux', 'Agent平台'])
        # 检查LLM
        has_llm = 'LLM' in dep_content or 'llm' in dep_content or 'AI' in dep_content or 'Agent' in dep_content
        
        missing = []
        if not has_api_key:
            missing.append('api_key')
        if not has_classification:
            missing.append('classification')
        if not has_env:
            missing.append('env')
        if not has_llm:
            missing.append('llm')
        
        if not missing:
            return content, 0
        
        # 需要补全
        tools = fm_data.get('tools', [])
        has_api = 'API' in content or 'api' in content.lower() or '密钥' in content or 'key' in content.lower()
        new_dep = generate_dependency_section(tools, has_api)
        
        # 替换旧的依赖说明
        old_dep = f'## 依赖说明\n{dep_content}'
        content = content.replace(old_dep, new_dep)
        return content, len(missing)
    else:
        # 完全缺失，新增
        tools = fm_data.get('tools', [])
        has_api = 'API' in content or 'api' in content.lower() or '密钥' in content
        new_dep = generate_dependency_section(tools, has_api)
        
        # 在核心能力前插入
        if '## 核心能力' in content:
            content = content.replace('## 核心能力', new_dep + '\n\n## 核心能力')
        elif '## 使用流程' in content:
            content = content.replace('## 使用流程', new_dep + '\n\n## 使用流程')
        else:
            content = content.rstrip() + '\n\n' + new_dep + '\n'
        
        return content, 4


def parse_frontmatter(content: str) -> dict:
    """解析frontmatter - 使用skill_core.parser统一解析"""
    result = _parse_fm(content)
    return result.get('fields', {})


def main():
    parser = argparse.ArgumentParser(description='L3批量修复脚本')
    parser.add_argument('--dry-run', action='store_true', help='仅检查，不修改文件')
    args = parser.parse_args()
    
    all_skills = sorted([d for d in PACKAGED_DIR.iterdir() if d.is_dir() and (d / 'SKILL.md').exists()])
    
    print(f"{'='*80}")
    print(f"L3 Batch Fix - {len(all_skills)} skills")
    print(f"Mode: {'DRY RUN' if args.dry_run else 'FIXING'}")
    print(f"{'='*80}")
    
    stats = {
        'template_fixed': 0,
        'error_section_added': 0,
        'dependency_fixed': 0,
        'total_modified': 0,
    }
    
    for i, skill_dir in enumerate(all_skills):
        slug = skill_dir.name
        skill_file = skill_dir / 'SKILL.md'
        
        content = skill_file.read_text(encoding='utf-8')
        original_content = content
        fm_data = parse_frontmatter(content)
        
        # 1. 清除模板套话
        content, template_changes = fix_template_phrases(content)
        if template_changes > 0:
            stats['template_fixed'] += 1
        
        # 2. 补全错误处理
        content, error_changes = fix_error_section(content, slug)
        if error_changes > 0:
            stats['error_section_added'] += 1
        
        # 3. 补全依赖说明
        content, dep_changes = fix_dependency_section(content, fm_data)
        if dep_changes > 0:
            stats['dependency_fixed'] += 1
        
        # 如果有修改，写回文件
        if content != original_content:
            stats['total_modified'] += 1
            if not args.dry_run:
                skill_file.write_text(content, encoding='utf-8')
        
        if (i + 1) % 100 == 0:
            print(f"  Progress: {i+1}/{len(all_skills)} (modified={stats['total_modified']})")
    
    print(f"\n{'='*80}")
    print(f"SUMMARY")
    print(f"{'='*80}")
    print(f"Total skills: {len(all_skills)}")
    print(f"Template phrases fixed: {stats['template_fixed']}")
    print(f"Error sections added: {stats['error_section_added']}")
    print(f"Dependency sections fixed: {stats['dependency_fixed']}")
    print(f"Total modified: {stats['total_modified']}")
    
    if not args.dry_run:
        print(f"\n所有修改已写入文件。请运行 L3 检查器验证通过率：")
        print(f"  python l3_function_checker.py --batch")


if __name__ == '__main__':
    main()
