#!/usr/bin/env python3
"""
关键函数单元测试（修复U-09：零测试覆盖）
=========================================
覆盖7个Critical问题的回归测试：
- U-01: scores表字段映射
- U-11: tools字段检查逻辑
- U-23: 评分阈值统一
- U-24: 付费判断一致性
- U-26: SQL注入防护
- U-27: 无限循环防护
- U-05: 类别归一化

运行: python test_fixes.py
"""

import sys
import os
import re

# 确保能导入config
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

passed = 0
failed = 0


def test_assert(name, condition, detail=""):
    global passed, failed
    if condition:
        passed += 1
        print(f"  ✓ {name}")
    else:
        failed += 1
        print(f"  ✗ {name} - {detail}")


def test_config_imports():
    """测试config.py导入"""
    print("\n[1] config.py 导入测试")
    try:
        from config import (
            DB_PATH, TRACE_PASS_THRESHOLD, TRACE_FIELD_MAPPING,
            is_paid_skill, safe_float, safe_int, create_backup,
            PACKAGED_SKILLS_DIR, MAX_SCAN_PAGES, MIN_PRICE, MAX_PRICE
        )
        test_assert("config导入成功", True)
        test_assert("TRACE_PASS_THRESHOLD=42", TRACE_PASS_THRESHOLD == 42, f"实际值: {TRACE_PASS_THRESHOLD}")
        test_assert("MAX_SCAN_PAGES=100", MAX_SCAN_PAGES == 100, f"实际值: {MAX_SCAN_PAGES}")
        test_assert("DB_PATH非空", bool(DB_PATH))
        test_assert("TRACE_FIELD_MAPPING有5个维度", len(TRACE_FIELD_MAPPING) == 5)
    except Exception as e:
        test_assert("config导入成功", False, str(e))


def test_is_paid_skill():
    """测试付费判断逻辑（U-24）"""
    print("\n[2] 付费判断逻辑测试 (U-24)")
    from config import is_paid_skill
    
    # 付费场景
    test_assert("license=Proprietary → 付费", is_paid_skill('Proprietary', '') == True)
    test_assert("license=Commercial → 付费", is_paid_skill('Commercial', '') == True)
    test_assert("edition=pro → 付费", is_paid_skill('', 'pro') == True)
    test_assert("edition=enterprise → 付费", is_paid_skill('', 'enterprise') == True)
    test_assert("edition=paid → 付费", is_paid_skill('', 'paid') == True)
    test_assert("edition=standard → 付费", is_paid_skill('', 'standard') == True)
    
    # 免费场景
    test_assert("license=MIT → 免费", is_paid_skill('MIT', '') == False)
    test_assert("license=Apache → 免费", is_paid_skill('Apache-2.0', '') == False)
    test_assert("edition=free → 免费", is_paid_skill('', 'free') == False)
    test_assert("edition=community → 免费", is_paid_skill('', 'community') == False)
    test_assert("无license无edition → 免费(默认)", is_paid_skill('', '') == False)


def test_trace_field_mapping():
    """测试TRACE字段映射（U-01）"""
    print("\n[3] TRACE字段映射测试 (U-01)")
    from config import TRACE_FIELD_MAPPING
    
    expected = {
        'trust': 'debranding_score',
        'reliability': 'quality_score',
        'adaptability': 'practicality_score',
        'convention': 'simplicity_score',
        'effectiveness': 'performance_score',
    }
    
    for dim, field in expected.items():
        test_assert(f"{dim} → {field}", TRACE_FIELD_MAPPING.get(dim) == field,
                    f"实际: {TRACE_FIELD_MAPPING.get(dim)}")
    
    # 确保不是错误的映射
    test_assert("trust ≠ quality_score", TRACE_FIELD_MAPPING['trust'] != 'quality_score')
    test_assert("reliability ≠ debranding_score", TRACE_FIELD_MAPPING['reliability'] != 'debranding_score')


def test_safe_conversions():
    """测试安全类型转换"""
    print("\n[4] 安全类型转换测试")
    from config import safe_float, safe_int
    
    test_assert("safe_float(3.14)=3.14", safe_float(3.14) == 3.14)
    test_assert("safe_float('abc')=0.0", safe_float('abc') == 0.0)
    test_assert("safe_float(None)=0.0", safe_float(None) == 0.0)
    test_assert("safe_float('')=0.0", safe_float('') == 0.0)
    test_assert("safe_float(0)=0.0", safe_float(0) == 0.0)
    
    test_assert("safe_int(42)=42", safe_int(42) == 42)
    test_assert("safe_int('abc')=0", safe_int('abc') == 0)
    test_assert("safe_int(None)=0", safe_int(None) == 0)
    test_assert("safe_int(3.7)=3", safe_int(3.7) == 3)


def test_tools_format_check():
    """测试tools字段格式检查（U-11）"""
    print("\n[5] tools字段格式检查测试 (U-11)")
    
    # 导入upload_gate的check_tools_format
    try:
        from upload_gate import check_tools_format
    except Exception as e:
        test_assert("upload_gate导入成功", False, str(e))
        return
    
    # 正确格式1: YAML数组
    fm1 = "slug: test\ntools:\n  - read\n  - exec\n"
    test_assert("YAML数组格式 → 通过", check_tools_format(fm1) is None,
                f"实际: {check_tools_format(fm1)}")
    
    # 正确格式2: 内联数组
    fm2 = "slug: test\ntools: [read, exec]\n"
    test_assert("内联数组格式 → 通过", check_tools_format(fm2) is None,
                f"实际: {check_tools_format(fm2)}")
    
    # 错误格式1: 字符串
    fm3 = "slug: test\ntools: read,exec\n"
    test_assert("字符串格式 → 报错", check_tools_format(fm3) is not None,
                f"实际: {check_tools_format(fm3)}")
    
    # 错误格式2: 缺失
    fm4 = "slug: test\nsummary: test\n"
    test_assert("缺失tools → 报错", check_tools_format(fm4) is not None,
                f"实际: {check_tools_format(fm4)}")
    
    # 关键测试：原bug场景（tools存在但格式错误，旧逻辑不报错）
    fm5 = "slug: test\ntools: \"read\"\n"
    result = check_tools_format(fm5)
    test_assert("字符串引号格式 → 报错(修复U-11)", result is not None,
                f"实际: {result}")


def test_normalize_category():
    """测试类别归一化（U-05）"""
    print("\n[6] 类别归一化测试 (U-05)")
    try:
        from market_monitor import normalize_category
    except Exception as e:
        test_assert("market_monitor导入成功", False, str(e))
        return
    
    # 中文类别直接匹配
    test_assert("中文'文案创作' → 文案创作", normalize_category('文案创作', '', '') == '文案创作')
    test_assert("中文'安全合规' → 安全合规", normalize_category('安全合规', '', '') == '安全合规')
    test_assert("中文'数据分析' → 数据分析", normalize_category('数据分析', '', '') == '数据分析')
    
    # 通过名称匹配中文
    test_assert("name含'文案' → 文案创作", normalize_category('', '文案生成器', '') == '文案创作')
    test_assert("name含'安全' → 安全合规", normalize_category('', '安全审计工具', '') == '安全合规')
    test_assert("name含'监控' → 监控运维", normalize_category('', '日志监控平台', '') == '监控运维')
    
    # 英文匹配
    test_assert("英文'writing' → 文案创作", normalize_category('writing', '', '') == '文案创作')
    test_assert("英文'security' → 安全合规", normalize_category('security', '', '') == '安全合规')
    
    # 无法匹配 → 其他
    test_assert("无匹配 → 其他", normalize_category('xyz', 'abc', '') == '其他')


def test_sql_injection_fix():
    """测试SQL注入修复（U-26）"""
    print("\n[7] SQL注入修复测试 (U-26)")
    
    # 验证trace_llm_scorer.py中不再使用f-string拼接LIMIT
    scorer_path = os.path.join(os.path.dirname(__file__), 'trace_llm_scorer.py')
    if os.path.exists(scorer_path):
        with open(scorer_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查是否还有 f" LIMIT {limit}" 这种模式
        has_fstring_limit = bool(re.search(r'f["\'].*LIMIT\s*\{', content))
        test_assert("无f-string拼接LIMIT", not has_fstring_limit, "仍存在f-string LIMIT拼接")
        
        # 检查是否有参数化LIMIT
        has_param_limit = 'query += " LIMIT ?"' in content or 'LIMIT ?' in content
        test_assert("有参数化LIMIT", has_param_limit)
    else:
        test_assert("trace_llm_scorer.py存在", False, "文件不存在")


def test_infinite_loop_fix():
    """测试无限循环修复（U-27）"""
    print("\n[8] 无限循环修复测试 (U-27)")
    
    monitor_path = os.path.join(os.path.dirname(__file__), 'market_monitor.py')
    if os.path.exists(monitor_path):
        with open(monitor_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查scan_skillhub不再有 while True
        # 找到scan_skillhub函数范围
        func_start = content.find('def scan_skillhub()')
        if func_start >= 0:
            func_end = content.find('\ndef ', func_start + 1)
            if func_end < 0:
                func_end = len(content)
            func_content = content[func_start:func_end]
            
            # 排除注释后检查是否有while True（处理行首注释和行内注释）
            code_lines = []
            for l in func_content.split('\n'):
                stripped = l.strip()
                if stripped.startswith('#'):
                    continue
                # 移除行内注释
                if '#' in l:
                    l = l[:l.index('#')]
                code_lines.append(l)
            code_content = '\n'.join(code_lines)
            has_while_true = 'while True' in code_content
            has_max_pages = 'MAX_SCAN_PAGES' in func_content or 'page <= MAX_PAGES' in func_content or 'page <= MAX_SCAN_PAGES' in func_content
            
            test_assert("scan_skillhub无while True", not has_while_true, "仍有while True")
            test_assert("scan_skillhub有MAX_PAGES限制", has_max_pages, "无MAX_PAGES限制")
        else:
            test_assert("找到scan_skillhub函数", False, "函数不存在")
    else:
        test_assert("market_monitor.py存在", False, "文件不存在")


def test_threshold_unification():
    """测试阈值统一（U-23）"""
    print("\n[9] 阈值统一测试 (U-23)")
    
    # 检查trace_llm_scorer.py不再有硬编码40
    scorer_path = os.path.join(os.path.dirname(__file__), 'trace_llm_scorer.py')
    if os.path.exists(scorer_path):
        with open(scorer_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查不再有 is_pass = 1 if total >= 40 else 0
        has_hardcoded_40 = 'total >= 40' in content
        test_assert("无硬编码阈值40", not has_hardcoded_40, "仍有硬编码40")
        
        has_trace_threshold = 'TRACE_PASS_THRESHOLD' in content
        test_assert("使用TRACE_PASS_THRESHOLD", has_trace_threshold)
    
    # 检查upload_gate.py使用config的MIN_TRACE_SCORE
    gate_path = os.path.join(os.path.dirname(__file__), 'upload_gate.py')
    if os.path.exists(gate_path):
        with open(gate_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # 检查不再有硬编码 MIN_TRACE_SCORE = 42
        has_hardcoded_42 = 'MIN_TRACE_SCORE = 42' in content
        test_assert("upload_gate无硬编码42", not has_hardcoded_42, "仍有硬编码42")
        
        has_config_import = 'from config import' in content
        test_assert("upload_gate使用config导入", has_config_import)


def main():
    print("=" * 80)
    print("关键函数单元测试 - 验证11个阻断性修复")
    print("=" * 80)
    
    test_config_imports()
    test_is_paid_skill()
    test_trace_field_mapping()
    test_safe_conversions()
    test_tools_format_check()
    test_normalize_category()
    test_sql_injection_fix()
    test_infinite_loop_fix()
    test_threshold_unification()
    
    print(f"\n{'=' * 80}")
    print(f"测试结果: {passed} 通过, {failed} 失败")
    print(f"{'=' * 80}")
    
    return 0 if failed == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
