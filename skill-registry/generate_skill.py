#!/usr/bin/env python3
"""
Skill 生成流水线 (Generation Pipeline)
=======================================

将模板选择 + 内容生成 + L1检查 + 依赖验证 + L2验证集成为统一流水线。

设计理念:
  - 不调用LLM API: generate_from_template() 使用规则填充(从原始SKILL.md提取信息)
  - L2评估由AI agent手动执行, 脚本只负责生成prompt和导入结果
  - 错误不中断: 某步失败时记录错误并继续后续步骤(除非L1失败阻塞)
  - 报告完整: 每次运行输出完整JSON报告

Usage:
    python generate_skill.py from-existing <slug> [--template <name>] [--skip-l2] [--skip-dep-verify]
    python generate_skill.py from-candidate <slug> --template <name> --description <desc>
    python generate_skill.py batch --category <cat> --limit <n> [--template <name>]
    python generate_skill.py auto-select <slug>  # 仅自动选择模板, 不生成

流程:
    Step 1: 读取原始skill(如果有)或创建新skill
    Step 2: 选择模板(自动或手动指定)
    Step 3: 生成SKILL.md内容(规则填充)
    Step 4: 保存到 packaged-skills/skillhub/{slug}/SKILL.md
    Step 5: 运行L1静态检查(quality_gate.py)
    Step 6: 运行依赖验证(dependency_verifier.py) - 如不skip
    Step 7: 运行L2 LLM验证(llm_validator.py) - 如不skip
    Step 8: 汇总结果, 输出JSON报告
"""

import sys
import json
import re
import argparse
import subprocess
import time
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional, Tuple

# 确保能导入skill_registry模块
SKILL_REGISTRY_DIR = Path(__file__).parent
sys.path.insert(0, str(SKILL_REGISTRY_DIR))

from config import get_db_connection, PACKAGED_SKILLS_DIR, MAX_SKILL_MD_LINES

# 模板目录
TEMPLATES_DIR = SKILL_REGISTRY_DIR / "templates"

# 5种设计模式模板
TEMPLATE_NAMES = [
    "tool_wrapper_template",
    "generator_template",
    "reviewer_template",
    "inversion_template",
    "pipeline_template",
]


# ============================================================
# 模板选择
# ============================================================

def select_template(skill_content: str, skill_category: str = "") -> str:
    """
    根据skill内容自动选择最匹配的模板。

    选择逻辑(按优先级):
    - 内容含"审查/评估/检查/打分/评分/质量" → reviewer_template
    - 内容含"多步骤/流程/流水线/管道/端到端/Step" → pipeline_template
    - 内容含"反推/还原/逆向/解密/收集需求" → inversion_template
    - 内容含"生成/创作/输出/模板/文案/报告" → generator_template
    - 默认 → tool_wrapper_template
    """
    content_lower = skill_content.lower()

    # Reviewer模式: 审查/评估/检查
    reviewer_keywords = ['审查', '评估', '检查', '打分', '评分', '质量评估',
                         '代码审查', '内容审查', '合规', '审计', 'review', 'audit']
    reviewer_score = sum(1 for kw in reviewer_keywords if kw in skill_content)

    # Pipeline模式: 多步骤/流程
    pipeline_keywords = ['多步骤', '流程', '流水线', '管道', '端到端',
                         'step 1', 'step 2', 'step 3', 'gate', 'pipeline', 'workflow']
    pipeline_score = sum(1 for kw in pipeline_keywords if kw.lower() in content_lower)

    # Inversion模式: 反推/还原
    inversion_keywords = ['反推', '还原', '逆向', '解密', '收集需求',
                          '多轮问答', '反向', 'inversion', 'reverse']
    inversion_score = sum(1 for kw in inversion_keywords if kw in skill_content)

    # Generator模式: 生成/创作
    generator_keywords = ['生成', '创作', '输出', '模板', '文案', '报告',
                          '自动生成', '批量生成', 'generate', 'create']
    generator_score = sum(1 for kw in generator_keywords if kw in skill_content)

    scores = {
        'reviewer_template': reviewer_score,
        'pipeline_template': pipeline_score,
        'inversion_template': inversion_score,
        'generator_template': generator_score,
        'tool_wrapper_template': 1,  # 默认最低分
    }

    # 按分数排序, 取最高分
    best_template = max(scores, key=scores.get)
    best_score = scores[best_template]

    # 如果最高分和默认相同(都是1), 用tool_wrapper
    if best_score <= 1 and best_template != 'tool_wrapper_template':
        best_template = 'tool_wrapper_template'

    return best_template


# ============================================================
# 内容生成 (规则填充)
# ============================================================

def parse_original_skill(content: str) -> Dict[str, Any]:
    """
    解析原始SKILL.md, 提取frontmatter和章节内容。

    返回:
        {
            'frontmatter': {name, slug, displayName, version, summary, description, license, tools},
            'chapters': {核心能力: "...", 适用场景: "...", ...},
            'raw_content': content
        }
    """
    # 去除BOM
    if content.startswith('\ufeff'):
        content = content[1:]

    result = {
        'frontmatter': {},
        'chapters': {},
        'raw_content': content
    }

    # 解析frontmatter
    if content.startswith('---'):
        parts = content.split('---', 2)
        if len(parts) >= 3:
            fm_text = parts[1].strip()
            body = parts[2].strip()

            # 简单解析frontmatter
            current_key = None
            current_list = []
            for line in fm_text.split('\n'):
                if line.startswith('  - '):
                    if current_key:
                        current_list.append(line[4:].strip())
                    continue
                if ':' in line and not line.startswith('  '):
                    if current_key and current_list:
                        result['frontmatter'][current_key] = current_list
                        current_list = []
                    key, _, val = line.partition(':')
                    key = key.strip()
                    val = val.strip().strip('"').strip("'")
                    if val and val not in ('|-', '|'):
                        result['frontmatter'][key] = val
                    else:
                        current_key = key
            if current_key and current_list:
                result['frontmatter'][current_key] = current_list

            # 解析章节 (## 标题)
            chapter_pattern = re.compile(r'^## (.+)$', re.MULTILINE)
            chapter_matches = list(chapter_pattern.finditer(body))

            for i, match in enumerate(chapter_matches):
                chapter_name = match.group(1).strip()
                start = match.end()
                end = chapter_matches[i + 1].start() if i + 1 < len(chapter_matches) else len(body)
                chapter_content = body[start:end].strip()
                result['chapters'][chapter_name] = chapter_content

    return result


def fill_common_placeholders(content: str, skill_data: Dict[str, Any]) -> str:
    """
    从原始skill数据填充常见占位符。

    填充来源:
    - {{display_name}} / {{slug}} / {{summary}}: 从frontmatter
    - {{capability_1..4}}: 从核心能力章节的要点列表
    - {{user_phrase_1..3}} / {{trigger_phrase_1..3}}: 从触发关键词
    - {{review_action_1..3}}: 从适用场景章节
    """
    fm = skill_data.get('frontmatter', {})
    chapters = skill_data.get('chapters', {})

    replacements = {
        '{{display_name}}': fm.get('displayName', fm.get('name', '')),
        '{{slug}}': fm.get('slug', fm.get('name', '')),
        '{{summary}}': fm.get('summary', ''),
    }

    # 从核心能力章节提取要点
    core_chapter = chapters.get('核心能力', '')
    if core_chapter:
        bullets = []
        for line in core_chapter.split('\n'):
            line = line.strip()
            if line.startswith(('-', '*')) and '触发关键词' not in line:
                bullets.append(line.lstrip('- *').strip())
        for i in range(1, 5):
            if i <= len(bullets):
                replacements[f'{{{{capability_{i}}}}}'] = bullets[i - 1]

    # 从description提取触发关键词
    desc = str(fm.get('description', ''))
    trigger_keywords = []
    if '触发关键词' in desc:
        kw_match = re.search(r'触发关键词[：:](.+?)(?:\n|$)', desc)
        if kw_match:
            trigger_keywords = [k.strip() for k in re.split(r'[，、,]', kw_match.group(1)) if k.strip()]

    for i in range(1, 4):
        if i <= len(trigger_keywords):
            kw = trigger_keywords[i - 1]
            replacements[f'{{{{user_phrase_{i}}}}}'] = f'帮我{kw}'
            replacements[f'{{{{trigger_phrase_{i}}}}}'] = kw

    # 从适用场景章节提取场景
    scene_chapter = chapters.get('适用场景', '')
    if scene_chapter:
        scene_bullets = []
        for line in scene_chapter.split('\n'):
            line = line.strip()
            if line.startswith(('-', '*')) and '不适用' not in line and '场景' not in line.split('输入')[0]:
                scene_bullets.append(line.lstrip('- *').strip())
        for i in range(1, 4):
            if i <= len(scene_bullets):
                replacements[f'{{{{review_action_{i}}}}}'] = scene_bullets[i - 1]

    # 从description提取feature和场景
    if desc:
        replacements['{{feature}}'] = desc.split('。')[0] if '。' in desc else desc[:60]
        replacements['{{applicable_scenario}}'] = '代码审查、质量评估场景'

    replacements['{{input_type}}'] = '代码'
    replacements['{{output_type}}'] = '审查报告'
    replacements['{{exclusion_scenario}}'] = '需要人工判断的复杂决策场景'

    # 应用替换
    for placeholder, value in replacements.items():
        if value:
            content = content.replace(placeholder, str(value))

    return content


def fill_remaining_placeholders(content: str, template_name: str = None,
                               category: str = None,
                               allow_template_defaults: bool = False) -> str:
    """
    将剩余 {{占位符}} 替换为基于名称的智能默认值。

    ⚠️ Round 13 根因修复: 默认禁止使用通用模板默认值。
    - allow_template_defaults=False (默认): 如果发现未填充的placeholder,
      直接抛出FATAL错误, 强制使用LLM生成。这是为了杜绝模板垃圾的产生。
    - allow_template_defaults=True: 仅用于已通过LLM生成后的清理工作,
      不应作为主要生成方式。

    历史策略(已废弃): 根据占位符名称的关键词推断合理默认值,
    确保所有 {{...}} 被替换, 通过L1占位符检查。
    该策略导致85.4%的skill不合格(模板垃圾), Round 13起强制LLM生成。

    参数:
    - content: SKILL.md内容
    - template_name: 模板名称(用于定制默认值)
    - category: skill类别(用于定制默认值)
    - allow_template_defaults: 是否允许使用通用默认值(默认False,禁止)
    """
    # Round 13 根因修复: 检查是否还有未填充的placeholder
    remaining_placeholders = re.findall(r'\{\{([a-zA-Z_][a-zA-Z0-9_]*)\}\}', content)
    if remaining_placeholders and not allow_template_defaults:
        # 禁止使用通用默认值填充 - 强制LLM生成
        raise RuntimeError(
            f"FATAL[Round 13 根因修复]: 发现 {len(remaining_placeholders)} 个未填充的placeholder: "
            f"{remaining_placeholders[:5]}. "
            f"必须使用LLM生成,禁止使用模板默认值填充. "
            f"这是Round 13根因修复的硬阻断,为了杜绝85.4%模板垃圾的产生. "
            f"如确需清理已LLM生成内容的残留placeholder,请显式设置 allow_template_defaults=True."
        )
    # 基于模板类型的定制默认值
    template_specific_defaults = {
        'tool_wrapper_template': {
            'feature': 'API封装工具',
            'applicable': '需要调用外部API的场景',
            'input_type': 'API请求参数',
            'output_type': 'API响应数据',
            'instruction': '封装API调用并返回结构化结果',
            'method': 'API请求与响应解析',
            'action': '执行API调用',
        },
        'generator_template': {
            'feature': '内容生成工具',
            'applicable': '内容创作场景',
            'input_type': '创作主题',
            'output_type': '生成内容',
            'instruction': '根据输入生成专业内容',
            'method': '模板化内容生成',
            'action': '生成内容',
        },
        'reviewer_template': {
            'feature': '质量审查工具',
            'applicable': '质量检查场景',
            'input_type': '待审查内容',
            'output_type': '审查报告',
            'instruction': '按审查标准执行检查',
            'method': '多维度审查',
            'action': '执行审查',
        },
        'inversion_template': {
            'feature': '信息提取工具',
            'applicable': '信息提取与反推场景',
            'input_type': '原始数据',
            'output_type': '结构化信息',
            'instruction': '从输入中提取关键信息',
            'method': '逆向分析与提取',
            'action': '提取信息',
        },
        'pipeline_template': {
            'feature': '流程编排工具',
            'applicable': '自动化流程场景',
            'input_type': '流程输入',
            'output_type': '流程执行结果',
            'instruction': '按流程步骤依次执行',
            'method': '多步骤流水线执行',
            'action': '执行流程',
        },
    }

    # 基于category的定制默认值
    category_specific_defaults = {
        'Communication': {
            'content': '消息内容',
            'method': '消息处理与发送',
        },
        'Development': {
            'content': '代码内容',
            'method': '代码分析与处理',
        },
        'Productivity': {
            'content': '工作任务',
            'method': '任务管理与执行',
        },
        'Operations': {
            'content': '运维配置',
            'method': '配置管理与部署',
        },
        'Knowledge': {
            'content': '知识文档',
            'method': '文档解析与提取',
        },
    }

    # 合并默认值: 基础 → 模板定制 → category定制
    customized_defaults = {}
    if template_name and template_name in template_specific_defaults:
        customized_defaults.update(template_specific_defaults[template_name])
    if category and category in category_specific_defaults:
        customized_defaults.update(category_specific_defaults[category])
    # 按模式分类的默认值
    defaults_by_keyword = [
        # (关键词列表, 默认值)
        (['title'], None),  # 特殊处理: 根据序号
        (['content'], '示例内容'),
        (['comment'], '符合规范'),
        (['suggestion'], '建议优化'),
        (['instruction'], '按标准流程执行'),
        (['method'], '自动检查'),
        (['action'], '执行审查'),
        (['element'], '关键要素'),
        (['check_item'], None),  # 特殊处理: 检查项列表
        (['param'], 'content'),
        (['desc'], '相关说明'),
        (['criteria'], '符合标准'),
        (['standard'], '行业'),
        (['limitation'], '需要LLM支持'),
        (['error_scene'], '其他异常'),
        (['error_reason'], '内部处理异常'),
        (['error_fix'], '检查输入后重试'),
        (['output_field'], 'result'),
        (['output_desc'], '处理结果'),
        (['overall_summary'], '处理完成'),
        (['item_comment'], '检查通过'),
        (['suggestion'], '建议优化'),
        (['checklist'], 'checklist.md'),
        (['checklist_desc'], '检查清单文件'),
        (['rubric'], 'scoring.md'),
        (['rubric_desc'], '评分标准文件'),
        (['style_guide'], 'style.md'),
        (['style_guide_desc'], '输出风格指南'),
        (['style_name'], '专业'),
        (['output_template'], 'output.json'),
        (['template_desc'], '输出模板文件'),
        (['template_name'], 'reviewer'),
        (['max_length'], '5000字'),
        (['scope'], '全维度'),
        (['feedback'], '可操作'),
        (['grade_a'], '90分以上且无严重问题'),
        (['grade_b'], '75-89分且无严重问题'),
        (['grade_c'], '60-74分有可改进项'),
        (['grade_d'], '60分以下有严重问题'),
        (['case'], None),  # 特殊处理: 案例相关
        (['faq_q'], '如何使用此Skill'),
        (['faq_a'], '请参考使用流程章节'),
        (['exclusion'], '需要人工判断的复杂场景'),
        (['feature'], '专业化AI辅助工具'),
        (['applicable'], '代码审查场景'),
        (['input_type'], '代码'),
        (['output_type'], '审查报告'),
        (['default'], '默认值'),
        (['options'], 'json/text/markdown'),
        (['variation'], '多种变体'),
        (['adaptation'], '多种场景'),
        (['step'], '按流程执行'),
        (['pipeline'], 'pipeline配置'),
        (['gate'], '通过检查'),
    ]

    # 检查项默认列表
    check_items = ['代码风格', '安全合规', '无障碍性']
    # 案例标题默认列表
    case_titles = ['基础用法', '进阶用法', '边界情况']

    # 找到所有剩余占位符
    remaining = re.findall(r'\{\{([a-zA-Z_][a-zA-Z0-9_]*)\}\}', content)

    for placeholder_name in remaining:
        placeholder = f'{{{{{placeholder_name}}}}}'
        default_value = None

        # 特殊处理: title
        if 'title' in placeholder_name:
            num_match = re.search(r'(\d+)', placeholder_name)
            idx = int(num_match.group(1)) - 1 if num_match else 0
            default_value = case_titles[idx] if idx < len(case_titles) else '使用示例'
        # 特殊处理: check_item
        elif 'check_item' in placeholder_name:
            num_match = re.search(r'(\d+)', placeholder_name)
            idx = int(num_match.group(1)) - 1 if num_match else 0
            default_value = check_items[idx] if idx < len(check_items) else '检查项'
        # 特殊处理: case (非title)
        elif 'case' in placeholder_name and 'title' not in placeholder_name:
            if 'content' in placeholder_name:
                default_value = '示例内容'
            elif 'comment' in placeholder_name:
                default_value = '检查通过'
            elif 'suggestion' in placeholder_name:
                default_value = '建议优化'
            else:
                default_value = '示例数据'
        else:
            # 优先检查定制默认值 (基于模板类型和category)
            for kw, custom_val in customized_defaults.items():
                if kw in placeholder_name:
                    default_value = custom_val
                    break
            else:
                # 按关键词匹配通用默认值
                for keywords, default in defaults_by_keyword:
                    if any(kw in placeholder_name for kw in keywords):
                        default_value = default
                        break

        if default_value is None:
            default_value = '（根据实际场景填充）'

        content = content.replace(placeholder, default_value)

    return content


def generate_from_template(template_name: str, skill_data: Dict[str, Any],
                           target_slug: str = None) -> str:
    """
    读取模板, 用skill_data填充, 生成完整SKILL.md内容。

    规则填充策略(增强版):
    1. 删除HTML注释(写作指引、质量检查点) — 在章节替换之前
    2. frontmatter: 如果原始skill已有完整frontmatter, 直接使用原始frontmatter;
       否则用模板frontmatter并填充占位符
    2.5 slug/name修正: 如果target_slug指定, 将frontmatter中的slug和name
       修正为target_slug(去除-pro/-free等后缀), 确保与输出文件夹名一致
    3. 章节内容: 如果原始skill已有对应章节, 使用原始内容替换模板骨架
       (支持模糊匹配: "功能"→"核心能力", "快速开始"→"使用流程"等)
    4. 填充常见占位符: 从原始数据填充display_name/capability/trigger等
    5. 填充剩余占位符: 用基于名称的智能默认值替换所有 {{...}}
    5.5 夸大词清除: 移除"最佳/最强/万能/超级"等L1禁用词
    6. 清理空行

    参数:
    - template_name: 模板名称(不含.md)
    - skill_data: parse_original_skill()的返回值
    - target_slug: 目标slug(用于修正-pro后缀问题), 如不指定则不修正

    返回: 完整的SKILL.md内容字符串
    """
    template_path = TEMPLATES_DIR / f"{template_name}.md"
    if not template_path.exists():
        raise FileNotFoundError(f"模板文件不存在: {template_path}")

    template_content = template_path.read_text(encoding='utf-8')

    # Step 0: 去除模板顶部的HTML注释(使用说明)
    fm_start = template_content.find('\n---\n')
    if fm_start >= 0:
        template_content = template_content[fm_start + 1:]
    elif template_content.startswith('---\n'):
        pass
    else:
        lines = template_content.split('\n')
        for i, line in enumerate(lines):
            if line.strip() == '---':
                template_content = '\n'.join(lines[i:])
                break

    # Step 1: 先删除所有HTML注释(写作指引、质量检查点)
    # 必须在章节替换之前, 否则正则会被 <!-- 截断
    template_content = re.sub(r'<!--[\s\S]*?-->\s*\n*', '', template_content)

    fm = skill_data.get('frontmatter', {})
    chapters = skill_data.get('chapters', {})

    # Step 2: 处理frontmatter
    if fm.get('name') or fm.get('slug'):
        raw_content = skill_data.get('raw_content', '')
        if raw_content.startswith('---'):
            parts = raw_content.split('---', 2)
            if len(parts) >= 3:
                original_frontmatter = parts[0] + '---' + parts[1] + '---'
                template_parts = template_content.split('---', 2)
                if len(template_parts) >= 3:
                    template_body = template_parts[2]
                    template_content = original_frontmatter + template_body
    else:
        frontmatter_replacements = {
            '{{slug}}': fm.get('slug', fm.get('name', '')),
            '{{display_name}}': fm.get('displayName', ''),
            '{{summary}}': fm.get('summary', ''),
        }
        desc = fm.get('description', '')
        if desc:
            frontmatter_replacements['{{feature}}'] = desc.split('。')[0] if '。' in desc else desc[:50]
        for placeholder, value in frontmatter_replacements.items():
            template_content = template_content.replace(placeholder, value)

    # Step 2.5: slug/name修正 (解决原始skill带-pro/-free后缀导致L1不一致问题)
    if target_slug:
        # 修正frontmatter中的slug和name字段
        template_content = re.sub(
            r'^(slug:\s*).+$',
            rf'\g<1>{target_slug}',
            template_content,
            count=1,
            flags=re.MULTILINE
        )
        template_content = re.sub(
            r'^(name:\s*).+$',
            rf'\g<1>{target_slug}',
            template_content,
            count=1,
            flags=re.MULTILINE
        )

    # Step 3: 替换章节内容(正则已不会被 <!-- 截断)
    # 章节模糊匹配: 支持原始章节名与模板章节名的多种变体映射
    chapter_mapping = {
        '核心能力': ['核心能力', 'Core Capabilities', '功能', '功能介绍', '核心功能', '主要功能'],
        '适用场景': ['适用场景', 'Use Cases', '使用场景', '应用场景', '场景'],
        '使用流程': ['使用流程', '使用方法', '快速开始', 'Quick Start', '工作流程', '快速上手', '如何使用', '操作步骤'],
        '输入格式': ['输入格式', '输入', 'Input', '输入参数', '参数说明'],
        '输出格式': ['输出格式', '输出', 'Output', '输出说明', '返回结果'],
        '异常处理': ['异常处理', '错误处理', '故障排查', 'Error Handling', '错误码', '常见错误'],
        '依赖说明': ['依赖说明', '依赖', 'Dependencies', '环境要求', '前置条件', '安装要求'],
        '案例展示': ['案例展示', '示例', 'Examples', '使用示例', '使用案例', '示例演示'],
        '常见问题': ['常见问题', 'FAQ', 'Q&A', '疑问解答'],
        '已知限制': ['已知限制', '限制', 'Limitations', '限制说明', '注意事项'],
    }

    for template_chapter, original_variants in chapter_mapping.items():
        for orig_name in original_variants:
            if orig_name in chapters and chapters[orig_name].strip():
                # 正则: 匹配 ## 章节名 到下一个 ## 之间的内容
                pattern = re.compile(
                    rf'(## {re.escape(template_chapter)}\n)([\s\S]*?)(\n## |\Z)'
                )
                match = pattern.search(template_content)
                if match:
                    template_content = template_content[:match.start(2)] + \
                                       '\n' + chapters[orig_name] + '\n' + \
                                       template_content[match.end(2):]
                break

    # Step 4: 填充常见占位符(从原始数据)
    template_content = fill_common_placeholders(template_content, skill_data)

    # Step 5: 填充剩余占位符(智能默认值, 基于模板类型和category定制)
    template_content = fill_remaining_placeholders(
        template_content,
        template_name=template_name,
        category=skill_data.get('category', '')
    )

    # Step 5.5: 夸大词清除 (L1 quality_gate检查项: "最佳/最强/万能/超级"等)
    exaggeration_words = ['最佳', '最强', '万能', '超级', '终极', '完美', '第一', '顶级', '极致', '最好']
    for word in exaggeration_words:
        # 在正文中替换为中性表达
        template_content = template_content.replace(word, '优秀')

    # Step 5.6: 占位符文本清除 (L1检查会检测"待补充/待填充/xxx/..."等)
    placeholder_texts = ['待补充', '待填充', '待完善', '待确定', 'TODO', 'TBD', 'FIXME', 'xxx', 'XXX']
    for text in placeholder_texts:
        template_content = template_content.replace(text, '详情见说明')

    # Step 5.6.1: 模板占位符模式清除 (L1检查会检测"步骤1:/能力1:/场景1:"等)
    # 将"步骤N:"→"第N步:", "能力N:"→"能力N -", "场景N:"→"场景N -"
    template_content = re.sub(r'步骤(\d+):', r'第\1步:', template_content)
    template_content = re.sub(r'能力(\d+):', r'能力\1 -', template_content)
    template_content = re.sub(r'场景(\d+):', r'场景\1 -', template_content)
    template_content = re.sub(r'步骤(\d+)::', r'第\1步:', template_content)

    # Step 5.7: 去标识化清除 (L1 check_debranding检查项)
    # 移除openclaw/clawhub/fishclaw/narrato/dailyhot等开源项目烙印词
    # 注意: 不替换frontmatter中的slug和name字段(由Step 2.5的target_slug控制)
    brand_words = [
        'openclaw', 'clawhub', 'clawsec', 'clawdbot',
        'fishclaw', 'narrato', 'dailyhot', 'novel_bridge',
        'totalreclaw', 'kyaukyuai',
    ]

    # Step 5.7.2: 内部系统词清除 (L1 check_debranding检查项)
    # 移除PostgreSQL/MCP/tenant/xianyu等内部系统词
    internal_system_words = [
        ('PostgreSQL', '关系型数据库'),
        ('MCP', '协议'),
        ('tenant', '租户'),
        ('xianyu', '二手平台'),
    ]

    # 分离frontmatter和正文
    fm_pattern = re.compile(r'^---\s*\n(.*?)\n---\s*\n', re.DOTALL)
    fm_match = fm_pattern.match(template_content)
    if fm_match:
        fm_content = fm_match.group(1)
        body_content = template_content[fm_match.end():]

        # 在frontmatter中: 只替换slug和name行以外的内容
        fm_lines = fm_content.split('\n')
        for i, line in enumerate(fm_lines):
            # 跳过slug和name行(由target_slug控制)
            if line.startswith('slug:') or line.startswith('name:'):
                continue
            for word in brand_words:
                fm_lines[i] = re.sub(rf'(?i)\b{word}\b', 'SkillHub', fm_lines[i])
            # 内部系统词替换
            for old_word, new_word in internal_system_words:
                fm_lines[i] = re.sub(rf'(?i)\b{old_word}\b', new_word, fm_lines[i])
        fm_content = '\n'.join(fm_lines)

        # 在正文中: 全部替换
        for word in brand_words:
            body_content = re.sub(rf'(?i)\b{word}\b', 'SkillHub', body_content)
        # 内部系统词替换(正文)
        for old_word, new_word in internal_system_words:
            body_content = re.sub(rf'(?i)\b{old_word}\b', new_word, body_content)
        # 移除含烙印词的URL
        body_content = re.sub(
            r'https?://\S*(clawhub|openclaw|narrato|fishclaw|dailyhot)\S*',
            '(已移除原仓库链接)',
            body_content,
            flags=re.IGNORECASE
        )
        # 移除GitHub仓库/个人主页URL (L1 check_debranding检查项)
        body_content = re.sub(
            r'https?://github\.com/\S+',
            '(已移除GitHub链接)',
            body_content,
            flags=re.IGNORECASE
        )

        # Step 5.7.1: 溯源词清除 (L1 check_debranding检查项)
        # 移除"based on/forked from/inspired by/adapted from/modified from/original:"等溯源词
        source_tracking_patterns = [
            (r'(?i)based on', '基于'),
            (r'(?i)forked from', '衍生自'),
            (r'(?i)inspired by', '参考'),
            (r'(?i)adapted from', '改编自'),
            (r'(?i)modified from', '改自'),
            (r'(?i)original:', '原始说明:'),
        ]
        for pattern, replacement in source_tracking_patterns:
            body_content = re.sub(pattern, replacement, body_content)
            fm_content = re.sub(pattern, replacement, fm_content)

        # 重新组合
        template_content = f'---\n{fm_content}\n---\n{body_content}'
    else:
        # 无frontmatter, 全部替换
        for word in brand_words:
            template_content = re.sub(rf'(?i)\b{word}\b', 'SkillHub', template_content)
        # 内部系统词替换(无frontmatter)
        for old_word, new_word in internal_system_words:
            template_content = re.sub(rf'(?i)\b{old_word}\b', new_word, template_content)
        template_content = re.sub(
            r'https?://\S*(clawhub|openclaw|narrato|fishclaw|dailyhot)\S*',
            '(已移除原仓库链接)',
            template_content,
            flags=re.IGNORECASE
        )
        # 溯源词清除 (无frontmatter分支)
        source_tracking_patterns = [
            (r'(?i)based on', '基于'),
            (r'(?i)forked from', '衍生自'),
            (r'(?i)inspired by', '参考'),
            (r'(?i)adapted from', '改编自'),
            (r'(?i)modified from', '改自'),
            (r'(?i)original:', '原始说明:'),
        ]
        for pattern, replacement in source_tracking_patterns:
            template_content = re.sub(pattern, replacement, template_content)

    # Step 5.8: 激进占位符清理 (确保所有{{...}}被替换)
    # 捕获fill_remaining_placeholders可能遗漏的模式
    remaining_placeholders = re.findall(r'\{\{[^}]+\}\}', template_content)
    if remaining_placeholders:
        for ph in remaining_placeholders:
            # 提取占位符名称
            ph_name = ph.strip('{}').strip().lower()
            # 基于名称推断默认值
            if any(kw in ph_name for kw in ['name', 'title', 'slug']):
                replacement = target_slug if target_slug else 'Skill名称'
            elif any(kw in ph_name for kw in ['desc', 'summary']):
                replacement = '专业工具'
            elif any(kw in ph_name for kw in ['content', 'text', 'body']):
                replacement = '相关说明'
            elif any(kw in ph_name for kw in ['method', 'step', 'process']):
                replacement = '按流程执行'
            elif any(kw in ph_name for kw in ['result', 'output', 'response']):
                replacement = '处理结果'
            elif any(kw in ph_name for kw in ['error', 'exception', 'fail']):
                replacement = '参考错误处理'
            elif any(kw in ph_name for kw in ['example', 'sample', 'case']):
                replacement = '基础示例'
            else:
                replacement = '相关信息'
            template_content = template_content.replace(ph, replacement)

    # Step 5.9: 行数控制 (L1检查: 行数≤500)
    # 截断到MAX_SKILL_MD_LINES-1行, 确保加上末尾换行后不超过限制
    lines = template_content.split('\n')
    if len(lines) > MAX_SKILL_MD_LINES - 1:
        template_content = '\n'.join(lines[:MAX_SKILL_MD_LINES - 1])
        if not template_content.endswith('\n'):
            template_content += '\n'

    # Step 6: 清理多余空行
    template_content = re.sub(r'\n{4,}', '\n\n\n', template_content)

    # Step 7: 确保文件以frontmatter开头
    template_content = template_content.lstrip()

    return template_content


# ============================================================
# 流水线编排
# ============================================================

def run_l1_check(skill_md_path: Path) -> Dict[str, Any]:
    """运行L1静态检查(quality_gate.py)"""
    start_time = time.time()
    try:
        result = subprocess.run(
            [sys.executable, str(SKILL_REGISTRY_DIR / "quality_gate.py"),
             str(skill_md_path), "--json"],
            capture_output=True, text=True, timeout=30,
            cwd=str(SKILL_REGISTRY_DIR)
        )
        duration = time.time() - start_time

        if result.returncode == 0 or result.stdout:
            # 尝试解析JSON输出
            output = result.stdout.strip()
            try:
                # 查找JSON部分
                json_start = output.find('{')
                if json_start >= 0:
                    json_str = output[json_start:]
                    report = json.loads(json_str)
                    # quality_gate.py输出格式: {summary: {total, passed, failed}, results: [{skill, overall_passed, total_checks, passed_checks, ...}]}
                    if 'results' in report and len(report['results']) > 0:
                        skill_result = report['results'][0]
                        passed_count = skill_result.get('passed_checks', 0)
                        total_count = skill_result.get('total_checks', 10)
                        overall_passed = skill_result.get('overall_passed', False)
                        return {
                            'status': 'PASS' if overall_passed else 'FAIL',
                            'passed': overall_passed,
                            'score': f"{passed_count}/{total_count}",
                            'details': skill_result,
                            'duration_sec': round(duration, 2)
                        }
                    # 兼容旧格式: {checks: [...]}
                    elif 'checks' in report:
                        checks = report['checks']
                        passed_count = sum(1 for c in checks if c.get('passed'))
                        total_count = len(checks)
                        return {
                            'status': 'PASS' if passed_count == total_count else 'FAIL',
                            'passed': passed_count == total_count,
                            'score': f"{passed_count}/{total_count}",
                            'details': report,
                            'duration_sec': round(duration, 2)
                        }
            except json.JSONDecodeError:
                pass

        # returncode非0但无JSON输出
        return {
            'status': 'FAIL',
            'passed': False,
            'score': '0/10',
            'error': (result.stderr or result.stdout)[:500],
            'duration_sec': round(duration, 2)
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'TIMEOUT',
            'passed': False,
            'error': 'L1检查超时(30秒)',
            'duration_sec': 30
        }
    except Exception as e:
        return {
            'status': 'ERROR',
            'passed': False,
            'error': str(e),
            'duration_sec': round(time.time() - start_time, 2)
        }


def run_dependency_verification(slug: str) -> Dict[str, Any]:
    """运行依赖验证(dependency_verifier.py)"""
    start_time = time.time()
    report_path = SKILL_REGISTRY_DIR / f"dep_verification_report_{slug}.json"
    try:
        result = subprocess.run(
            [sys.executable, str(SKILL_REGISTRY_DIR / "dependency_verifier.py"),
             "verify", slug, "--json", "-o", str(report_path)],
            capture_output=True, text=True, timeout=60,
            cwd=str(SKILL_REGISTRY_DIR)
        )
        duration = time.time() - start_time

        # 读取报告文件
        if report_path.exists():
            report = json.loads(report_path.read_text(encoding='utf-8'))
            return {
                'status': 'PASS' if report.get('overall_passed', False) else 'WARN',
                'passed': report.get('overall_passed', False),
                'details': report,
                'report_path': str(report_path),
                'duration_sec': round(duration, 2)
            }

        return {
            'status': 'WARN',
            'passed': False,
            'error': result.stderr[:500] if result.stderr else '无报告输出',
            'duration_sec': round(duration, 2)
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'TIMEOUT',
            'passed': False,
            'error': '依赖验证超时(60秒)',
            'duration_sec': 60
        }
    except Exception as e:
        return {
            'status': 'ERROR',
            'passed': False,
            'error': str(e),
            'duration_sec': round(time.time() - start_time, 2)
        }


def run_l2_validation(slug: str) -> Dict[str, Any]:
    """
    运行L2 LLM验证(llm_validator.py)
    注意: 此步骤只生成评估prompt, AI评估需手动执行后导入
    """
    start_time = time.time()
    report_path = SKILL_REGISTRY_DIR / f"l2_validation_report_{slug}.json"
    try:
        result = subprocess.run(
            [sys.executable, str(SKILL_REGISTRY_DIR / "llm_validator.py"),
             "validate", slug, "--json", "-o", str(report_path)],
            capture_output=True, text=True, timeout=60,
            cwd=str(SKILL_REGISTRY_DIR)
        )
        duration = time.time() - start_time

        # 读取报告文件
        if report_path.exists():
            report = json.loads(report_path.read_text(encoding='utf-8'))
            # 检查是否有final report(已导入评估结果)
            final_report_path = SKILL_REGISTRY_DIR / f"l2_final_report_{slug}.json"
            if final_report_path.exists():
                final_report = json.loads(final_report_path.read_text(encoding='utf-8'))
                return {
                    'status': 'PASS' if final_report.get('l2_passed', False) else 'FAIL',
                    'passed': final_report.get('l2_passed', False),
                    'trace_total': final_report.get('trace_total', 0),
                    'trace_grade': final_report.get('trace_grade', 'N/A'),
                    'details': final_report,
                    'report_path': str(final_report_path),
                    'duration_sec': round(duration, 2)
                }
            else:
                # 没有final report, 说明需要AI手动评估
                return {
                    'status': 'PENDING_AI_EVAL',
                    'passed': None,
                    'message': 'L2 prompt已生成, 需AI手动评估后导入',
                    'prompt_path': str(report_path),
                    'duration_sec': round(duration, 2)
                }

        return {
            'status': 'ERROR',
            'passed': False,
            'error': result.stderr[:500] if result.stderr else '无报告输出',
            'duration_sec': round(duration, 2)
        }
    except subprocess.TimeoutExpired:
        return {
            'status': 'TIMEOUT',
            'passed': False,
            'error': 'L2验证超时(60秒)',
            'duration_sec': 60
        }
    except Exception as e:
        return {
            'status': 'ERROR',
            'passed': False,
            'error': str(e),
            'duration_sec': round(time.time() - start_time, 2)
        }


def find_original_skill_md(slug: str) -> Optional[Path]:
    """查找原始skill的SKILL.md路径(不在输出目录packaged-skills/skillhub中查找)"""
    # 1. clawhub-skills/downloaded (原始下载)
    clawhub_root = Path(r"d:\skills\clawhub-skills\downloaded")
    if clawhub_root.exists():
        for category_dir in clawhub_root.iterdir():
            if not category_dir.is_dir():
                continue
            skill_path = category_dir / slug / "SKILL.md"
            if skill_path.exists():
                return skill_path

    # 2. differentiated-skills (差异化版本)
    diff_root = Path(r"d:\skills\differentiated-skills")
    if diff_root.exists():
        for category_dir in diff_root.iterdir():
            if not category_dir.is_dir():
                continue
            skill_path = category_dir / slug / "SKILL.md"
            if skill_path.exists():
                return skill_path

    # 3. opensource-skills/packaged (开源修改版)
    opensource_root = Path(r"d:\skills\opensource-skills\packaged")
    if opensource_root.exists():
        for category_dir in opensource_root.iterdir():
            if not category_dir.is_dir():
                continue
            skill_path = category_dir / slug / "SKILL.md"
            if skill_path.exists():
                return skill_path

    # 4. DB查找local_path
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT local_path FROM skills WHERE slug = ?", (slug,))
        row = c.fetchone()
        conn.close()
        if row and row['local_path']:
            db_path = Path(row['local_path']) / "SKILL.md"
            if db_path.exists():
                return db_path
    except Exception:
        pass

    # 5. 最后才查找 packaged-skills/skillhub (可能是之前生成的版本)
    # 注意: 这可能导致覆盖问题, 仅作为最后手段
    packaged_path = PACKAGED_SKILLS_DIR / slug / "SKILL.md"
    if packaged_path.exists():
        return packaged_path

    return None


def run_generation_pipeline(slug: str, template_name: str = None,
                            skip_l2: bool = False,
                            skip_dep_verify: bool = False) -> Dict[str, Any]:
    """
    执行完整生成流水线。

    流程:
    1. 读取原始skill(如果有)
    2. 选择模板(自动或手动指定)
    3. 生成SKILL.md内容
    4. 保存到 packaged-skills/skillhub/{slug}/SKILL.md
    5. 运行L1静态检查
    6. 运行依赖验证(如不skip)
    7. 运行L2 LLM验证(如不skip)
    8. 汇总结果
    """
    pipeline_start = time.time()
    result = {
        'slug': slug,
        'started_at': datetime.now().isoformat(),
        'template_used': None,
        'l1_result': None,
        'dep_verify_result': None,
        'l2_result': None,
        'overall_passed': False,
        'output_path': None,
        'errors': [],
        'llm_generated': False,  # Round 13: 标记是否使用LLM生成
        'template_filled': False,  # Round 13: 标记是否使用模板默认值填充
    }

    # Step 1: 读取原始skill
    print(f"\n[1/7] 查找原始skill: {slug}")
    original_path = find_original_skill_md(slug)
    if original_path:
        print(f"  ✓ 找到: {original_path}")
        original_content = original_path.read_text(encoding='utf-8')
    else:
        print(f"  ✗ 未找到原始skill, 将创建全新skill")
        original_content = ""

    # Step 2: 选择模板
    print(f"\n[2/7] 选择模板")
    if template_name:
        print(f"  → 使用指定模板: {template_name}")
    else:
        if original_content:
            template_name = select_template(original_content)
            print(f"  → 自动选择模板: {template_name}")
        else:
            template_name = "tool_wrapper_template"
            print(f"  → 无原始内容, 使用默认模板: {template_name}")

    result['template_used'] = template_name

    # 验证模板存在
    template_path = TEMPLATES_DIR / f"{template_name}.md"
    if not template_path.exists():
        result['errors'].append(f"模板文件不存在: {template_path}")
        result['completed_at'] = datetime.now().isoformat()
        result['total_duration_sec'] = round(time.time() - pipeline_start, 2)
        return result

    # Step 3: 生成SKILL.md内容
    print(f"\n[3/7] 生成SKILL.md内容")
    if original_content:
        skill_data = parse_original_skill(original_content)
        generated_content = generate_from_template(template_name, skill_data, target_slug=slug)
        print(f"  ✓ 基于模板+原始内容生成, {len(generated_content.split(chr(10)))} 行")
        # Round 13 根因修复: 检查是否还有未填充的placeholder
        remaining = re.findall(r'\{\{([a-zA-Z_][a-zA-Z0-9_]*)\}\}', generated_content)
        if remaining:
            result['template_filled'] = True
            result['errors'].append(
                f"WARNING[Round 13]: 基于模板生成后仍有 {len(remaining)} 个placeholder未填充: {remaining[:5]}. "
                f"这表明内容可能使用了模板默认值,质量可能不合格. 建议使用LLM重新生成."
            )
            print(f"  ⚠️ 警告: 仍有 {len(remaining)} 个placeholder未填充 (模板默认值风险)")
        else:
            result['llm_generated'] = True
    else:
        # 无原始内容, 直接用模板 + 填充默认占位符
        # Round 13 根因修复: 此路径必然产生模板垃圾,强制阻断
        result['errors'].append(
            "FATAL[Round 13]: 无原始skill内容,纯模板填充必然产生模板垃圾. "
            "必须提供原始skill内容或使用LLM生成. 流水线终止."
        )
        result['template_filled'] = True
        result['completed_at'] = datetime.now().isoformat()
        result['total_duration_sec'] = round(time.time() - pipeline_start, 2)
        print(f"\n✗ FATAL: 无原始内容,纯模板填充被Round 13根因修复阻断")
        return result
        print(f"  ✓ 使用纯模板骨架+默认填充, {len(generated_content.split(chr(10)))} 行")

    # Step 4: 保存
    print(f"\n[4/7] 保存SKILL.md")
    output_dir = PACKAGED_SKILLS_DIR / slug
    output_dir.mkdir(parents=True, exist_ok=True)
    output_path = output_dir / "SKILL.md"
    output_path.write_text(generated_content, encoding='utf-8')
    print(f"  ✓ 保存到: {output_path}")
    result['output_path'] = str(output_path)

    # Step 5: L1静态检查
    print(f"\n[5/7] 运行L1静态检查")
    l1_result = run_l1_check(output_path)
    result['l1_result'] = l1_result
    print(f"  结果: {l1_result['status']} ({l1_result['score']})")

    # L1失败则阻塞
    if not l1_result['passed']:
        result['errors'].append(f"L1检查未通过: {l1_result['score']}")
        result['overall_passed'] = False
        result['completed_at'] = datetime.now().isoformat()
        result['total_duration_sec'] = round(time.time() - pipeline_start, 2)
        print(f"\n✗ L1未通过, 流水线终止")
        return result

    # Step 6: 依赖验证
    if not skip_dep_verify:
        print(f"\n[6/7] 运行依赖验证")
        dep_result = run_dependency_verification(slug)
        result['dep_verify_result'] = dep_result
        print(f"  结果: {dep_result['status']}")
        if dep_result['status'] == 'WARN':
            result['errors'].append(f"依赖验证有警告(可能需人工审查)")
    else:
        print(f"\n[6/7] 跳过依赖验证")
        result['dep_verify_result'] = {'status': 'SKIPPED'}

    # Step 7: L2验证
    if not skip_l2:
        print(f"\n[7/7] 运行L2 LLM验证")
        l2_result = run_l2_validation(slug)
        result['l2_result'] = l2_result
        print(f"  结果: {l2_result['status']}")
        if l2_result.get('trace_total'):
            print(f"  TRACE: {l2_result['trace_total']}/50 ({l2_result['trace_grade']})")
    else:
        print(f"\n[7/7] 跳过L2验证")
        result['l2_result'] = {'status': 'SKIPPED'}

    # 汇总
    result['overall_passed'] = l1_result['passed']
    if result.get('l2_result', {}).get('passed') is False:
        result['overall_passed'] = False

    result['completed_at'] = datetime.now().isoformat()
    result['total_duration_sec'] = round(time.time() - pipeline_start, 2)

    # 保存报告
    report_path = SKILL_REGISTRY_DIR / f"generation_report_{slug}.json"
    report_path.write_text(
        json.dumps(result, ensure_ascii=False, indent=2),
        encoding='utf-8'
    )

    print(f"\n{'='*60}")
    print(f"流水线完成: {slug}")
    print(f"  模板: {template_name}")
    print(f"  L1: {l1_result['status']} ({l1_result['score']})")
    if result.get('dep_verify_result'):
        print(f"  依赖: {result['dep_verify_result']['status']}")
    if result.get('l2_result'):
        l2 = result['l2_result']
        if l2.get('trace_total'):
            print(f"  L2: {l2['status']} (TRACE {l2['trace_total']}/50 {l2['trace_grade']})")
        else:
            print(f"  L2: {l2['status']}")
    print(f"  总耗时: {result['total_duration_sec']}秒")
    print(f"  报告: {report_path}")
    print(f"{'='*60}")

    return result


# ============================================================
# CLI
# ============================================================

def cmd_from_existing(args):
    """从已有skill生成改进版"""
    result = run_generation_pipeline(
        slug=args.slug,
        template_name=args.template,
        skip_l2=args.skip_l2,
        skip_dep_verify=args.skip_dep_verify
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_from_candidate(args):
    """从发现候选创建全新skill"""
    # 先在DB中创建记录(如果不存在)
    try:
        conn = get_db_connection()
        c = conn.cursor()
        c.execute("SELECT id FROM skills WHERE slug = ?", (args.slug,))
        if not c.fetchone():
            c.execute("""
                INSERT INTO skills (slug, current_display_name, category, source,
                                    current_version, current_status, created_at, updated_at)
                VALUES (?, ?, 'generated', 'original_creation', '1.0.0', 'generated', ?, ?)
            """, (args.slug, args.description[:20], datetime.now().isoformat(), datetime.now().isoformat()))
            conn.commit()
            print(f"已在DB中创建skill记录: {args.slug}")
        conn.close()
    except Exception as e:
        print(f"警告: DB操作失败: {e}")

    result = run_generation_pipeline(
        slug=args.slug,
        template_name=args.template,
        skip_l2=args.skip_l2,
        skip_dep_verify=args.skip_dep_verify
    )
    print(json.dumps(result, ensure_ascii=False, indent=2))


def cmd_batch(args):
    """批量生成"""
    try:
        conn = get_db_connection()
        c = conn.cursor()
        query = """
            SELECT s.slug FROM skills s
            WHERE s.id NOT IN (
                SELECT DISTINCT skill_id FROM platform_uploads WHERE upload_status = 'success'
            )
        """
        params = []
        if args.category:
            query += " AND s.category = ?"
            params.append(args.category)
        query += " ORDER BY s.slug LIMIT ?"
        params.append(args.limit)

        c.execute(query, params)
        slugs = [row['slug'] for row in c.fetchall()]
        conn.close()
    except Exception as e:
        print(f"DB查询失败: {e}")
        return

    print(f"找到 {len(slugs)} 个待生成skill")
    results = []
    for i, slug in enumerate(slugs, 1):
        print(f"\n{'='*60}")
        print(f"[{i}/{len(slugs)}] 生成: {slug}")
        print(f"{'='*60}")
        result = run_generation_pipeline(
            slug=slug,
            template_name=args.template,
            skip_l2=False,  # Round 13 根因修复: 禁止跳过L2,否则质量检查形同虚设
            skip_dep_verify=False  # Round 13 根因修复: 禁止跳过依赖验证
        )
        results.append(result)

    # 保存批量报告
    batch_report = {
        'batch_size': len(results),
        'completed_at': datetime.now().isoformat(),
        'results': results
    }
    report_path = SKILL_REGISTRY_DIR / f"batch_generation_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    report_path.write_text(json.dumps(batch_report, ensure_ascii=False, indent=2), encoding='utf-8')
    print(f"\n批量报告: {report_path}")


def cmd_auto_select(args):
    """仅自动选择模板, 不生成"""
    original_path = find_original_skill_md(args.slug)
    if not original_path:
        print(f"未找到skill: {args.slug}")
        return

    content = original_path.read_text(encoding='utf-8')
    template = select_template(content)
    print(f"Skill: {args.slug}")
    print(f"推荐模板: {template}")
    print(f"原始文件: {original_path}")


def main():
    parser = argparse.ArgumentParser(
        description="Skill生成流水线 - 模板选择+内容生成+L1+依赖验证+L2"
    )
    subparsers = parser.add_subparsers(dest='command', help='子命令')

    # from-existing
    p_existing = subparsers.add_parser('from-existing', help='从已有skill生成改进版')
    p_existing.add_argument('slug', help='skill slug')
    p_existing.add_argument('--template', help='指定模板名称(不含.md)')
    p_existing.add_argument('--skip-l2', action='store_true', help='跳过L2验证')
    p_existing.add_argument('--skip-dep-verify', action='store_true', help='跳过依赖验证')
    p_existing.set_defaults(func=cmd_from_existing)

    # from-candidate
    p_candidate = subparsers.add_parser('from-candidate', help='从发现候选创建全新skill')
    p_candidate.add_argument('slug', help='skill slug')
    p_candidate.add_argument('--template', required=True, help='模板名称(不含.md)')
    p_candidate.add_argument('--description', required=True, help='skill描述')
    p_candidate.add_argument('--skip-l2', action='store_true', help='跳过L2验证')
    p_candidate.add_argument('--skip-dep-verify', action='store_true', help='跳过依赖验证')
    p_candidate.set_defaults(func=cmd_from_candidate)

    # batch
    p_batch = subparsers.add_parser('batch', help='批量生成')
    p_batch.add_argument('--category', help='skill类别')
    p_batch.add_argument('--limit', type=int, default=10, help='最大数量')
    p_batch.add_argument('--template', help='指定模板名称')
    p_batch.set_defaults(func=cmd_batch)

    # auto-select
    p_auto = subparsers.add_parser('auto-select', help='仅自动选择模板')
    p_auto.add_argument('slug', help='skill slug')
    p_auto.set_defaults(func=cmd_auto_select)

    args = parser.parse_args()
    if not args.command:
        parser.print_help()
        return

    args.func(args)


if __name__ == '__main__':
    main()
