#!/usr/bin/env python3
"""
模板填充清理工具 (Template Cleanup Tool)
========================================
自动识别并移除SKILL.md中批量生成的模板填充内容。

清理项:
  1. "能力覆盖范围" 乱码拼接段落
  2. "指令解析与执行" / "数据处理与转换" / "结果验证与输出" 通用模板段落
  3. "技术细节" 通用模板表格 (parser/processor/output)
  4. "命令参数说明" 无意义flag列举
  5. "源能力映射" 通用模板段落
  6. "领域术语" 仅罗列单词段落
  7. 空的"已知限制"段落
  8. 空FAQ答案
  9. "案例展示"占位符内容
 10. "相关说明"表格占位符行

使用方式:
    python template_cleanup.py              # 扫描并报告
    python template_cleanup.py --apply      # 执行清理
    python template_cleanup.py --report     # 仅生成报告
"""

# === Phase 1: 统一配置导入 ===
import sys as _sys
from pathlib import Path as _Path
_sys.path.insert(0, str(_Path(__file__).resolve().parent.parent / "config"))
from project_config import DIFFERENTIATED_DIR
# === End Phase 1 ===


import re
import json
import sys
from pathlib import Path
from datetime import datetime

PACKAGED_DIR = Path(r"D:\skills\packaged-skills\skillhub")
# DIFFERENTIATED_DIR imported from config
REGISTRY_DIR = Path(r"D:\skills\skill-registry")

# 需要移除的模板section patterns (匹配整个section包括内容)
# 每个 pattern 匹配从 ## header 到下一个 ## 或文件结尾
TEMPLATE_SECTIONS = [
    # "能力覆盖范围" 乱码拼接
    r'##\s*能力覆盖范围\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "指令解析与执行" 通用模板
    r'##\s*指令解析与执行\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "数据处理与转换" 通用模板
    r'##\s*数据处理与转换\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "结果验证与输出" 通用模板
    r'##\s*结果验证与输出\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "技术细节" 通用模板表格 (parser/processor/output)
    r'##\s*技术细节\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "命令参数说明" 无意义flag列举
    r'##\s*命令参数说明\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "源能力映射" 通用模板
    r'##\s*源能力映射\s*\n[\s\S]*?(?=\n##\s|\Z)',
    # "领域术语" 仅罗列单词
    r'##\s*领域术语\s*\n[\s\S]*?(?=\n##\s|\Z)',
]

# "执行X操作，处理输入数据并返回结果" 通用模板句子
GENERIC_SENTENCE_REGEX = re.compile(
    r'[\s]*[-*]?\s*(?:执行|进行|完成)[^\n]{0,30}操作[,，]\s*处理输入数据并返回结果[^\n]*\n',
    re.MULTILINE
)

# 空的"已知限制"段落 (只有破折号或空行)
EMPTY_LIMITATIONS_REGEX = re.compile(
    r'##\s*(?:已知限制|Limitations)\s*\n(?:[\s\-|]*\n){1,10}(?=\n##\s|\Z)',
    re.MULTILINE
)

# "案例展示" 占位内容
PLACEHOLDER_CASE_REGEX = re.compile(
    r'##\s*案例展示\s*\n[\s\S]*?(?:输入[:：]\s*(?:用户请求|示例数据|示例内容)[\s\S]*?输出[:：]\s*(?:处理结果|示例输出|建议优化))[\s\S]*?(?=\n##\s|\Z)',
    re.MULTILINE
)

# "相关说明" 表格占位符行
PLACEHOLDER_TABLE_ROW_REGEX = re.compile(
    r'\|[^\n]*\|\s*相关说明\s*\|[^\n]*\n',
    re.MULTILINE
)

# 通用输入输出模板行
GENERIC_IO_REGEX = re.compile(
    r'(?:\*\*输入\*\*|输入[:：])\s*用户提供[^\n]*所需[^\n]*\n'
    r'(?:\*\*处理\*\*|处理[:：])\s*按照skill规范执行[^\n]*\n'
    r'(?:\*\*输出\*\*|输出[:：])\s*返回[^\n]*执行结果[^\n]*\n',
    re.MULTILINE
)


def collect_skill_files():
    """收集所有 SKILL.md 文件"""
    files = []
    if PACKAGED_DIR.exists():
        for skill_dir in sorted(PACKAGED_DIR.iterdir()):
            if not skill_dir.is_dir():
                continue
            skill_md = skill_dir / "SKILL.md"
            if skill_md.exists():
                files.append((skill_md, "packaged"))
    if DIFFERENTIATED_DIR.exists():
        for cat_dir in sorted(DIFFERENTIATED_DIR.iterdir()):
            if not cat_dir.is_dir():
                continue
            for skill_dir in sorted(cat_dir.iterdir()):
                if not skill_dir.is_dir():
                    continue
                skill_md = skill_dir / "SKILL.md"
                if skill_md.exists():
                    files.append((skill_md, f"differentiated/{cat_dir.name}"))
    return files


def clean_skill(content: str) -> tuple:
    """清理单个SKILL.md内容中的模板填充

    Returns:
        (cleaned_content, stats_dict)
    """
    original_len = len(content)
    stats = {
        "sections_removed": 0,
        "sentences_removed": 0,
        "limitations_removed": 0,
        "cases_removed": 0,
        "table_rows_removed": 0,
        "io_templates_removed": 0,
        "bytes_removed": 0,
    }

    # 1. 移除模板section
    for pattern in TEMPLATE_SECTIONS:
        matches = re.findall(pattern, content, re.MULTILINE)
        if matches:
            stats["sections_removed"] += len(matches)
            content = re.sub(pattern, '', content, flags=re.MULTILINE)

    # 2. 移除通用模板句子
    sentences = GENERIC_SENTENCE_REGEX.findall(content)
    if sentences:
        stats["sentences_removed"] = len(sentences)
        content = GENERIC_SENTENCE_REGEX.sub('', content)

    # 3. 移除空的"已知限制"
    limitations = EMPTY_LIMITATIONS_REGEX.findall(content)
    if limitations:
        stats["limitations_removed"] = len(limitations)
        content = EMPTY_LIMITATIONS_REGEX.sub('', content)

    # 4. 移除占位案例展示
    cases = PLACEHOLDER_CASE_REGEX.findall(content)
    if cases:
        stats["cases_removed"] = len(cases)
        content = PLACEHOLDER_CASE_REGEX.sub('', content)

    # 5. 移除"相关说明"表格行
    table_rows = PLACEHOLDER_TABLE_ROW_REGEX.findall(content)
    if table_rows:
        stats["table_rows_removed"] = len(table_rows)
        content = PLACEHOLDER_TABLE_ROW_REGEX.sub('', content)

    # 6. 移除通用输入输出模板
    io_templates = GENERIC_IO_REGEX.findall(content)
    if io_templates:
        stats["io_templates_removed"] = len(io_templates)
        content = GENERIC_IO_REGEX.sub('', content)

    # 清理多余空行 (3+连续空行变为2个)
    content = re.sub(r'\n{4,}', '\n\n\n', content)

    stats["bytes_removed"] = original_len - len(content)
    return content, stats


def main():
    apply_mode = "--apply" in sys.argv
    report_mode = "--report" in sys.argv

    print("=" * 60)
    print("模板填充清理工具 (Template Cleanup Tool)")
    print("=" * 60)
    if apply_mode:
        print("[模式] 扫描 + 清理")
    else:
        print("[模式] 仅扫描 (使用 --apply 执行清理)")
    print()

    files = collect_skill_files()
    print(f"共发现 {len(files)} 个 SKILL.md 文件")

    results = []
    total_stats = {
        "skills_with_templates": 0,
        "total_sections_removed": 0,
        "total_sentences_removed": 0,
        "total_bytes_removable": 0,
    }

    for skill_path, source in files:
        try:
            content = skill_path.read_text(encoding='utf-8', errors='replace')
        except Exception:
            continue

        cleaned, stats = clean_skill(content)

        has_templates = (
            stats["sections_removed"] > 0 or
            stats["sentences_removed"] > 0 or
            stats["limitations_removed"] > 0 or
            stats["cases_removed"] > 0 or
            stats["table_rows_removed"] > 0 or
            stats["io_templates_removed"] > 0
        )

        if has_templates:
            total_stats["skills_with_templates"] += 1
            total_stats["total_sections_removed"] += stats["sections_removed"]
            total_stats["total_sentences_removed"] += stats["sentences_removed"]
            total_stats["total_bytes_removable"] += stats["bytes_removed"]

            results.append({
                "slug": skill_path.parent.name,
                "source": source,
                "path": str(skill_path),
                "stats": stats,
            })

            if apply_mode:
                skill_path.write_text(cleaned, encoding='utf-8')

    # 打印汇总
    print()
    print("=" * 60)
    print("清理汇总")
    print("=" * 60)
    print(f"  有模板填充的skill: {total_stats['skills_with_templates']} / {len(files)}")
    print(f"  可移除模板段落: {total_stats['total_sections_removed']}")
    print(f"  可移除模板句子: {total_stats['total_sentences_removed']}")
    print(f"  可移除字节数: {total_stats['total_bytes_removable']} ({total_stats['total_bytes_removable']//1024}KB)")

    if apply_mode:
        print(f"\n  ✅ 已清理 {total_stats['skills_with_templates']} 个skill")
    else:
        print(f"\n  ⚠ 仅扫描模式，使用 --apply 执行清理")

    # 保存报告
    report = {
        "scan_date": datetime.now().isoformat(),
        "total_files": len(files),
        "skills_with_templates": total_stats["skills_with_templates"],
        "apply_mode": apply_mode,
        "total_sections_removable": total_stats["total_sections_removed"],
        "total_sentences_removable": total_stats["total_sentences_removed"],
        "total_bytes_removable": total_stats["total_bytes_removable"],
        "details": results[:500],
    }

    report_path = REGISTRY_DIR / "template_cleanup_report.json"
    report_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False),
        encoding='utf-8'
    )
    print(f"\n报告已保存: {report_path}")


if __name__ == "__main__":
    main()
