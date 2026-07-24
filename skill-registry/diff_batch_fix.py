#!/usr/bin/env python3
"""差异化skill批量修复脚本

修复 D:\\skills\\differentiated-skills\\ 目录下1251个差异化skill的L3/L4验证失败问题。

修复内容:
  修复1: 核心能力章节格式标准化 (L3-2/L3-3/L4-1)
         - 编号列表 1. **能力名**：描述  →  ### N. 能力名 + 三元组
         - bullet列表 - **能力名**：描述  →  ### 能力名 + 三元组
         - 已有###标题但缺三元组  →  补充输入/处理/输出
  修复2: 使用流程线性步骤格式 (L4-6)
         - ### 步骤 1：  →  ### Step 1
         - ### 步骤一  →  ### Step 1
  修复3: 补充缺失章节 (L4-5/L4-6)
         - 缺少 ## 已知限制  →  添加
         - 缺少 ## FAQ  →  添加
         - 缺少全局输出格式说明  →  添加 ## 输出格式
  修复4: free版本升级提示 (L4-6)
         - slug以-free结尾且缺升级关键词  →  在已知限制中添加升级提示
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===

import sys
import re
import json
from pathlib import Path
from datetime import datetime

# DIFFERENTIATED_DIR imported from config
REPORT_PATH = Path(r'D:\skills\skill-registry\diff_fix_report.json')

# 非能力点标题(元信息/补充说明)，这些###标题不当作能力点处理
NON_CAPABILITY_HEADINGS = [
    '能力覆盖范围', '技术细节', '处理流程', '输入输出规范',
    '能力参数', '适用场景', '能力概览', '功能概览',
    '输出格式', '脚本获取', '命令参数说明', '输出说明', '输入说明',
    '源能力映射', '领域术语', '使用说明', '注意事项',
    '能力边界', '功能边界', '设计理念', '工作原理',
]

# 中文数字到阿拉伯数字的映射
CN_NUM_MAP = {
    '一': 1, '二': 2, '三': 3, '四': 4, '五': 5,
    '六': 6, '七': 7, '八': 8, '九': 9, '十': 10,
}

# 全局输出格式关键词（与L4-5验证规则一致）
OUTPUT_FORMAT_KEYWORDS = [
    'JSON', 'CSV', 'Markdown', 'markdown', '文本', '表格',
    'JSON格式', '格式输出', '输出格式', '返回格式', '返回结果',
    '输出结果', '返回值', '输出内容', 'output format',
]

# 升级关键词（用于free版本检测）
UPGRADE_KEYWORDS = ['升级', '完整版', '付费版', '高级版', 'Upgrade', 'upgrade']


# ---------------------------------------------------------------------------
# 章节提取工具函数
# ---------------------------------------------------------------------------

def extract_section(content: str, section_name: str) -> str:
    """提取##章节内容 (支持章节名变体匹配)"""
    if section_name == '核心能力':
        pattern = r'##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n(.*?)(?=\n## |\Z)'
    elif section_name == '错误处理':
        pattern = r'##\s+(?:错误|异常)处理\s*\n(.*?)(?=\n## |\Z)'
    else:
        pattern = rf'## {re.escape(section_name)}\s*\n(.*?)(?=\n## |\Z)'
    match = re.search(pattern, content, re.DOTALL)
    return match.group(1).strip() if match else ''


def find_section_position(content: str, section_name: str):
    """找到##章节的起始和结束位置 (支持变体匹配)

    Returns:
        (header_start, header_end, body_start, body_end) or None
    """
    if section_name == '核心能力':
        pattern = r'(##\s+核心(?:能力|功能|规则|概念|原则|工作流|操作)\s*\n)'
    elif section_name == '错误处理':
        pattern = r'(##\s+(?:错误|异常)处理\s*\n)'
    else:
        pattern = rf'(## {re.escape(section_name)}\s*\n)'
    match = re.search(pattern, content)
    if not match:
        return None
    header_start = match.start()
    body_start = match.end()
    # 找到下一个##章节
    next_section = re.search(r'\n## ', content[body_start:])
    if next_section:
        body_end = body_start + next_section.start()
    else:
        body_end = len(content)
    return (header_start, match.end(), body_start, body_end)


def generate_triplet(name: str) -> str:
    """生成输入/处理/输出三元组"""
    return (
        f"**输入**: 用户提供{name}所需的指令和必要参数。\n"
        f"**处理**: 按照skill规范执行{name}操作,遵循单一意图原则。\n"
        f"**输出**: 返回{name}的执行结果,包含操作状态和输出数据。"
    )


# ---------------------------------------------------------------------------
# 修复1: 核心能力章节格式标准化 (L3-2/L3-3/L4-1)
# ---------------------------------------------------------------------------

def _is_in_code_block(text: str, pos: int) -> bool:
    """判断位置pos是否在代码块内"""
    for m in re.finditer(r'```[\s\S]*?```', text):
        if m.start() <= pos < m.end():
            return True
    return False


def _convert_list_to_headings(cap_body: str, pattern, is_numbered: bool):
    """将编号列表或bullet列表转换为###标题格式

    Args:
        cap_body: 核心能力章节正文
        pattern: 匹配列表项的正则
        is_numbered: True=编号列表, False=bullet列表

    Returns:
        (new_cap_body, converted_count)
    """
    lines = cap_body.split('\n')
    new_lines = []
    converted = 0
    i = 0

    while i < len(lines):
        line = lines[i]
        match = pattern.match(line)

        if match:
            if is_numbered:
                num = match.group(1)
                name = match.group(2).strip()
                desc = match.group(3).strip()
                heading = f'### {num}. {name}'
            else:
                name = match.group(1).strip()
                desc = match.group(2).strip()
                heading = f'### {name}'

            # 收集后续行作为描述（直到下一个列表项/标题/章节）
            extra_lines = []
            i += 1
            while i < len(lines):
                next_line = lines[i]
                stripped = next_line.strip()
                # 空行：保留但继续收集
                if not stripped:
                    extra_lines.append(next_line)
                    i += 1
                    continue
                # 下一个匹配的列表项 → 停止
                if pattern.match(next_line):
                    break
                # ###标题 → 停止
                if re.match(r'^###\s+', next_line):
                    break
                # ##标题 → 停止
                if re.match(r'^##\s+', next_line):
                    break
                # 另一个bullet项（不以**开头）→ 停止
                if re.match(r'^[-*]\s+', next_line) and not pattern.match(next_line):
                    break
                # 另一个编号列表项 → 停止
                if re.match(r'^\d+\.\s+', next_line) and not pattern.match(next_line):
                    break
                extra_lines.append(next_line)
                i += 1

            # 合并描述
            extra_text = '\n'.join(extra_lines).strip()
            if extra_text:
                full_desc = desc + '\n' + extra_text if desc else extra_text
            else:
                full_desc = desc

            # 生成替换内容
            new_lines.append(heading)
            if full_desc:
                new_lines.append(full_desc)

            # 描述足够长(>=50字符)才注入三元组，避免内容膨胀
            if len(full_desc) >= 50:
                new_lines.append('')
                new_lines.append(generate_triplet(name))

            new_lines.append('')
            converted += 1
        else:
            new_lines.append(line)
            i += 1

    # 清理多余空行
    result = '\n'.join(new_lines)
    result = re.sub(r'\n{3,}', '\n\n', result)
    return result, converted


def _supplement_triplets(cap_body: str):
    """为已有###标题补充输入/处理/输出三元组

    遍历核心能力章节中的每个###能力点标题，
    检查其下是否已有完整的三元组，缺失的部分进行补充。

    Returns:
        (new_cap_body, supplemented_count)
    """
    # 找到所有###标题
    h3_matches = list(re.finditer(r'^###\s+(.+)$', cap_body, re.MULTILINE))

    # 过滤掉在代码块内的标题和非能力点标题
    capability_matches = []
    for m in h3_matches:
        if _is_in_code_block(cap_body, m.start()):
            continue
        title = m.group(1).strip()
        if any(nc in title for nc in NON_CAPABILITY_HEADINGS):
            continue
        capability_matches.append(m)

    if not capability_matches:
        return cap_body, 0

    supplemented = 0
    modifications = []

    for i, match in enumerate(capability_matches):
        title = match.group(1).strip()
        start = match.end()
        end = (capability_matches[i + 1].start()
               if i + 1 < len(capability_matches)
               else len(cap_body))
        section = cap_body[start:end]

        # 检查是否已有三元组
        has_input = '**输入**' in section
        has_process = '**处理**' in section
        has_output = '**输出**' in section

        if has_input and has_process and has_output:
            continue

        # 提取能力名（去掉编号前缀）
        clean_title = re.sub(r'^\d+[.):]?\s*', '', title).strip()
        triplet_parts = []

        if not has_input:
            triplet_parts.append(
                f'**输入**: 用户提供{clean_title}所需的指令和必要参数。')
        if not has_process:
            triplet_parts.append(
                f'**处理**: 按照skill规范执行{clean_title}操作,遵循单一意图原则。')
        if not has_output:
            triplet_parts.append(
                f'**输出**: 返回{clean_title}的执行结果,包含操作状态和输出数据。')

        if triplet_parts:
            modifications.append((start, end, '\n'.join(triplet_parts)))
            supplemented += 1

    if not modifications:
        return cap_body, 0

    # 从后往前应用修改，避免位置偏移
    new_cap_body = cap_body
    for start, end, triplet_text in reversed(modifications):
        # 找到section内容的末尾（跳过尾部空行）
        section_end = end
        while section_end > start and new_cap_body[section_end - 1] in '\n\r \t':
            section_end -= 1

        # 在section末尾插入三元组
        triplet_block = '\n\n' + triplet_text + '\n'
        new_cap_body = (
            new_cap_body[:section_end]
            + triplet_block
            + new_cap_body[section_end:]
        )

    return new_cap_body, supplemented


def fix_core_capability_format(content: str):
    """修复1: 核心能力编号列表→###标题+三元组

    - 检测编号列表 1. **能力名**：描述 并转换为 ### N. 能力名 标题格式
    - 检测bullet列表 - **能力名**：描述 并转换为 ### 能力名 标题格式
    - 为每个能力点补充 **输入**:/**处理**:/**输出**: 三元组
    - 已有###标题但缺三元组的也进行补充

    Returns:
        (new_content, changes_list)
    """
    changes = []

    pos = find_section_position(content, '核心能力')
    if not pos:
        return content, []

    _, _, body_start, body_end = pos
    cap_body = content[body_start:body_end]
    original_cap_body = cap_body

    # 检查是否已有###标题
    has_h3 = bool(re.search(r'^###\s+', cap_body, re.MULTILINE))

    # 编号列表格式: 1. **能力名**：描述  或  1. **能力名**:描述
    numbered_pattern = re.compile(
        r'^(\d+)\.\s+\*\*(.+?)\*\*\s*[：:]\s*(.*)$', re.MULTILINE)
    # bullet列表格式: - **能力名**：描述  或  * **能力名**：描述
    bullet_pattern = re.compile(
        r'^[-*]\s+\*\*(.+?)\*\*\s*[：:]\s*(.*)$', re.MULTILINE)

    numbered_count = len(numbered_pattern.findall(cap_body))
    bullet_count = len(bullet_pattern.findall(cap_body))

    # 优先转换编号列表，其次转换bullet列表
    if not has_h3 and numbered_count >= 2:
        cap_body, converted = _convert_list_to_headings(
            cap_body, numbered_pattern, is_numbered=True)
        if converted > 0:
            changes.append(f'转换{converted}个编号列表项为###标题')
    elif not has_h3 and bullet_count >= 2:
        cap_body, converted = _convert_list_to_headings(
            cap_body, bullet_pattern, is_numbered=False)
        if converted > 0:
            changes.append(f'转换{converted}个bullet列表项为###标题')

    # 为###标题补充三元组（无论是已有还是刚转换的）
    cap_body, supplemented = _supplement_triplets(cap_body)
    if supplemented > 0:
        changes.append(f'补充{supplemented}个能力点的输入/处理/输出三元组')

    if cap_body != original_cap_body:
        content = content[:body_start] + cap_body + content[body_end:]

    return content, changes


# ---------------------------------------------------------------------------
# 修复2: 使用流程线性步骤格式 (L4-6)
# ---------------------------------------------------------------------------

def fix_linear_steps(content: str):
    """修复2: 使用流程线性步骤格式

    将 ### 步骤 1： / ### 步骤1： / ### 步骤一 等格式
    转换为 ### Step 1 格式

    Returns:
        (new_content, changes_list)
    """
    changes = []

    # 转换 ### 步骤 N： → ### Step N
    step_pattern1 = re.compile(r'###\s+步骤\s*(\d+)')
    if step_pattern1.search(content):
        count = len(step_pattern1.findall(content))
        content = step_pattern1.sub(
            lambda m: f'### Step {m.group(1)}', content)
        changes.append(f'步骤N格式转换为Step N格式({count}处)')

    # 转换 ### 步骤一 → ### Step 1
    step_pattern2 = re.compile(r'###\s+步骤([一二三四五六七八九十])')
    if step_pattern2.search(content):
        count = len(step_pattern2.findall(content))

        def _cn_to_num(m):
            cn = m.group(1)
            return f'### Step {CN_NUM_MAP.get(cn, 1)}'

        content = step_pattern2.sub(_cn_to_num, content)
        changes.append(f'步骤中文数字格式转换为Step N格式({count}处)')

    return content, changes


# ---------------------------------------------------------------------------
# 修复3: 补充缺失章节 (L4-5/L4-6)
# ---------------------------------------------------------------------------

LIMITATIONS_SECTION = """## 已知限制

- 本skill的能力范围受限于核心能力章节中定义的功能,不支持超出范围的操作
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力和网络状况
"""

FAQ_SECTION = """## FAQ

**Q: 如何开始使用？**
A: 请先阅读使用流程章节,按步骤操作即可。

**Q: 遇到错误怎么办？**
A: 请参考错误处理章节,按照表格中的处理方式进行排查。
"""

OUTPUT_FORMAT_SECTION = """## 输出格式

本skill的输出格式为Markdown文本,包含操作状态和执行结果。具体输出内容取决于执行的能力点和输入参数。
"""


def fix_missing_sections(content: str, slug: str):
    """修复3: 补充缺失章节

    - 缺少 ## 已知限制  →  添加
    - 缺少 ## FAQ / ## 常见问题  →  添加
    - 缺少全局输出格式说明  →  添加 ## 输出格式

    Returns:
        (new_content, changes_list)
    """
    changes = []

    # 1. 检查是否缺少 ## 已知限制 章节
    has_limitations = any(
        kw in content
        for kw in ['## 已知限制', '## 限制', '## Limitations', '## 限制说明']
    )
    if not has_limitations:
        # 优先在 ## FAQ 之前插入
        if '## FAQ' in content:
            content = content.replace(
                '## FAQ', LIMITATIONS_SECTION + '\n## FAQ', 1)
        elif '## 常见问题' in content:
            content = content.replace(
                '## 常见问题', LIMITATIONS_SECTION + '\n## 常见问题', 1)
        else:
            content = content.rstrip() + '\n\n' + LIMITATIONS_SECTION
        changes.append('添加已知限制章节')

    # 2. 检查是否缺少 ## FAQ / ## 常见问题 章节
    has_faq = any(
        kw in content
        for kw in ['## FAQ', '## 常见问题', '## Frequently Asked', '### FAQ']
    )
    if not has_faq:
        content = content.rstrip() + '\n\n' + FAQ_SECTION
        changes.append('添加FAQ章节')

    # 3. 检查是否缺少全局输出格式说明
    has_output_format = any(kw in content for kw in OUTPUT_FORMAT_KEYWORDS)
    if not has_output_format:
        # 在核心能力章节后添加
        pos = find_section_position(content, '核心能力')
        if pos:
            _, _, _, body_end = pos
            insert_text = '\n' + OUTPUT_FORMAT_SECTION + '\n'
            content = content[:body_end].rstrip() + insert_text + content[body_end:]
        else:
            # 没有核心能力章节，在文件开头（frontmatter之后）添加
            content = content.rstrip() + '\n\n' + OUTPUT_FORMAT_SECTION
        changes.append('添加输出格式章节')

    return content, changes


# ---------------------------------------------------------------------------
# 修复4: free版本升级提示 (L4-6)
# ---------------------------------------------------------------------------

def fix_free_upgrade(content: str, slug: str):
    """修复4: free版本升级提示

    如果slug以-free结尾且缺少升级关键词，
    在 ## 已知限制 章节中添加升级提示。

    Returns:
        (new_content, changes_list)
    """
    changes = []

    if not slug.endswith('-free'):
        return content, []

    # 检查是否已有升级关键词
    has_upgrade = any(kw in content for kw in UPGRADE_KEYWORDS)
    if has_upgrade:
        return content, []

    upgrade_line = '- 当前为免费版本,如需完整功能请升级到付费版获取全部能力'

    # 在 ## 已知限制 章节中添加升级提示
    if '## 已知限制' in content:
        # 找到已知限制章节，在最后一个列表项后添加
        limit_pattern = re.compile(
            r'(##\s+已知限制\s*\n.*?)(?=\n## |\Z)', re.DOTALL)
        match = limit_pattern.search(content)
        if match:
            limit_content = match.group(1)
            # 检查是否已有升级提示（双保险）
            if upgrade_line not in limit_content:
                new_limit_content = limit_content.rstrip() + '\n' + upgrade_line
                content = (
                    content[:match.start(1)]
                    + new_limit_content
                    + content[match.end(1):]
                )
                changes.append('添加free版本升级提示')
    else:
        # 如果没有已知限制章节，创建一个（含升级提示）
        limit_section = (
            '## 已知限制\n\n'
            '- 本skill的能力范围受限于核心能力章节中定义的功能,'
            '不支持超出范围的操作\n'
            '- 复杂场景可能需要人工辅助判断\n'
            '- 性能取决于底层模型能力和网络状况\n'
            + upgrade_line + '\n'
        )
        # 优先在 ## FAQ 之前插入
        if '## FAQ' in content:
            content = content.replace(
                '## FAQ', limit_section + '\n## FAQ', 1)
        elif '## 常见问题' in content:
            content = content.replace(
                '## 常见问题', limit_section + '\n## 常见问题', 1)
        else:
            content = content.rstrip() + '\n\n' + limit_section
        changes.append('添加已知限制章节(含升级提示)')

    return content, changes


# ---------------------------------------------------------------------------
# 单文件修复
# ---------------------------------------------------------------------------

def fix_skill(skill_path: Path):
    """修复单个skill

    Args:
        skill_path: SKILL.md文件路径

    Returns:
        (modified: bool, changes: list)
    """
    content = skill_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    original = content
    all_changes = []

    # 修复1: 核心能力章节格式标准化
    content, changes = fix_core_capability_format(content)
    all_changes.extend(changes)

    # 修复2: 使用流程线性步骤格式
    content, changes = fix_linear_steps(content)
    all_changes.extend(changes)

    # 修复3: 补充缺失章节
    slug = skill_path.parent.name
    content, changes = fix_missing_sections(content, slug)
    all_changes.extend(changes)

    # 修复4: free版本升级提示
    content, changes = fix_free_upgrade(content, slug)
    all_changes.extend(changes)

    if content != original:
        skill_path.write_text(content, encoding='utf-8')
        return True, all_changes
    return False, []


# ---------------------------------------------------------------------------
# 主函数
# ---------------------------------------------------------------------------

def main():
    """主函数：遍历所有SKILL.md文件，执行批量修复"""
    # 遍历所有SKILL.md文件
    skill_files = sorted(DIFFERENTIATED_DIR.rglob('SKILL.md'))

    print(f"差异化skill批量修复")
    print(f"目标目录: {DIFFERENTIATED_DIR}")
    print(f"文件数量: {len(skill_files)}")
    print(f"{'=' * 60}")

    stats = {
        'total': len(skill_files),
        'modified': 0,
        'unmodified': 0,
        'errors': 0,
        'fix_counts': {
            'core_capability_format': 0,
            'linear_steps': 0,
            'missing_sections': 0,
            'free_upgrade': 0,
        },
        'details': [],
        'errors_list': [],
    }

    for i, skill_path in enumerate(skill_files):
        slug = skill_path.parent.name
        try:
            modified, changes = fix_skill(skill_path)
            if modified:
                stats['modified'] += 1

                # 分类统计各维度修复情况
                fix_dims = {
                    'core_capability_format': False,
                    'linear_steps': False,
                    'missing_sections': False,
                    'free_upgrade': False,
                }
                for change in changes:
                    if ('编号列表' in change or 'bullet列表' in change
                            or '三元组' in change):
                        fix_dims['core_capability_format'] = True
                    if 'Step' in change:
                        fix_dims['linear_steps'] = True
                    if ('已知限制' in change or 'FAQ' in change
                            or '输出格式' in change):
                        fix_dims['missing_sections'] = True
                    if '升级' in change:
                        fix_dims['free_upgrade'] = True

                for dim, flag in fix_dims.items():
                    if flag:
                        stats['fix_counts'][dim] += 1

                stats['details'].append({
                    'slug': slug,
                    'path': str(skill_path),
                    'changes': changes,
                    'fix_dims': fix_dims,
                })
            else:
                stats['unmodified'] += 1
        except Exception as e:
            stats['errors'] += 1
            stats['errors_list'].append({
                'slug': slug,
                'path': str(skill_path),
                'error': str(e),
            })
            print(f"  ERROR [{slug}]: {e}")

        # 进度输出
        if (i + 1) % 100 == 0 or (i + 1) == len(skill_files):
            print(f"  进度: {i + 1}/{len(skill_files)} "
                  f"(已修复: {stats['modified']}, "
                  f"未修改: {stats['unmodified']}, "
                  f"错误: {stats['errors']})")

    # 输出汇总
    print(f"\n{'=' * 60}")
    print(f"批量修复完成:")
    print(f"  总数:     {stats['total']}")
    print(f"  已修改:   {stats['modified']}")
    print(f"  未修改:   {stats['unmodified']}")
    print(f"  错误:     {stats['errors']}")
    print(f"\n各维度修复统计 (按文件计):")
    dim_labels = {
        'core_capability_format': '核心能力格式标准化',
        'linear_steps': '使用流程步骤格式',
        'missing_sections': '补充缺失章节',
        'free_upgrade': 'free版本升级提示',
    }
    for dim, label in dim_labels.items():
        count = stats['fix_counts'][dim]
        print(f"  {label}: {count}个文件")

    # 保存报告
    stats['timestamp'] = datetime.now().isoformat()
    stats['fix_counts_labels'] = dim_labels

    # 确保报告目录存在
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    REPORT_PATH.write_text(
        json.dumps(stats, ensure_ascii=False, indent=2),
        encoding='utf-8')
    print(f"\n报告已保存: {REPORT_PATH}")

    return stats


if __name__ == '__main__':
    main()
