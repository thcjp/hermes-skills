#!/usr/bin/env python3
"""
LLM驱动的TRACE评分脚本 v2.1 (V178增强)
===========================
增强功能：
1. 静态评分（T+C维度）- 全自动
2. LLM评分（R+A+E维度）- 批量生成评估内容，LLM评估后导入
3. 批量评估 - 支持大批量skill的高效评分
4. 评分报告 - 生成详细的TRACE评分报告
5. V178新增: llm-batch — 直接在脚本内调用LLM API进行批量TRACE评估

Usage:
    python trace_llm_scorer.py static                    # 全部skill静态评分
    python trace_llm_scorer.py static --packaged         # 仅60个packaged skill静态评分
    python trace_llm_scorer.py static --dry-run          # 模拟评分, 不写入数据库
    python trace_llm_scorer.py export --packaged         # 导出60个skill供LLM评估
    python trace_llm_scorer.py export --limit 100        # 导出100个skill供LLM评估
    python trace_llm_scorer.py import <results.json>     # 导入LLM评估结果
    python trace_llm_scorer.py import <results.json> --dry-run  # 模拟导入, 不写入数据库
    python trace_llm_scorer.py report                    # 生成评分报告
    python trace_llm_scorer.py report --packaged         # 仅60个packaged skill报告
    python trace_llm_scorer.py llm-batch                # V178: 批量LLM评估(补充R+A+E维度)
    python trace_llm_scorer.py llm-batch --limit 50     # 仅评估50个
    python trace_llm_scorer.py llm-batch --dry-run       # 模拟运行
    python trace_llm_scorer.py llm-batch --rate 1.0      # 每次调用间隔1秒
"""

import json
import re
import sys
import os
import time
import requests
from pathlib import Path
from datetime import datetime
from typing import Any, Dict, List, Optional

# 导入统一配置（修复U-21硬编码路径、U-23阈值不一致）
# V117 W5: 清理os.path.dirname用法, 统一用Path(__file__).resolve().parent
_sys_path = str(Path(__file__).resolve().parent)
if _sys_path not in sys.path:
    sys.path.insert(0, _sys_path)
_config_path = str(Path(__file__).resolve().parent.parent / "config")
if _config_path not in sys.path:
    sys.path.insert(0, _config_path)
from project_config import (
    PACKAGED_SKILLS_DIR, OPENSOURCE_SKILLS_DIR, SCORE_TYPE_TRACE_LLM,
    L2_PASS_THRESHOLD, L2_EXCELLENT_THRESHOLD, L2_MANUAL_REVIEW_THRESHOLD,
    TRACE_SCORE_GRADE_B, TRACE_SCORE_GRADE_C, TRACE_RELIABILITY_THRESHOLD,  # V121 W3: trace评分等级阈值(与TRACE_GRADE_B/C不同)
    EXPORT_DIR, DATA_DIR,  # V152 R4修复: 补充缺失的路径导入
    TRACE_PASS_THRESHOLD, TRACE_FIELD_MAPPING,  # V152 R4修复: 补充缺失的阈值和映射导入
)

# A3修复: 从skill_core导入共享解析和规则,消除第三套检查实现
from skill_core.parser import parse_frontmatter
from skill_core.rules import EXAGGERATION_WORDS, RESERVED_WORDS
from skill_core import db as db_module  # V116 W1: 统一db入口(替代import db)

# TRACE评估Prompt模板（用于LLM评估）
TRACE_EVAL_PROMPT = """请按照SkillHub TRACE评测体系评估以下Skill。

## TRACE五维度
- T (Trust 可信任度): 安全性、国内可用性、中文支持
- R (Reliability 可靠性): 异常处理、边界输入、失败反馈
- A (Adaptability 适用性): description精准、能力边界清晰、触发条件明确
- C (Convention 规范性): 信息架构、文档充分性、章节完整性
- E (Effectiveness 有效性): 解决问题、输出可用、额外价值

## 评分标准(每维度0-10分)
- 9-10: 卓越，行业标杆
- 7-8: 良好，满足要求
- 5-6: 及格，有改进空间
- 3-4: 不足，需要修复
- 0-2: 严重缺失

## 待评估SKILL.md
{skill_content}

## 输出格式(严格JSON)
{{
  "trace_scores": {{
    "trust": {{"score": 0, "reason": "", "suggestion": ""}},
    "reliability": {{"score": 0, "reason": "", "suggestion": ""}},
    "adaptability": {{"score": 0, "reason": "", "suggestion": ""}},
    "convention": {{"score": 0, "reason": "", "suggestion": ""}},
    "effectiveness": {{"score": 0, "reason": "", "suggestion": ""}}
  }},
  "total_score": 0,
  "top_3_issues": ["", "", ""],
  "quality_grade": "A|B|C|D"
}}

等级: A(45-50) B(40-44) C(30-39) D(<30)
"""

def get_all_skills(limit=None, specific_slugs=None, packaged_only=False):
    """获取待评估的skill列表
    
    修复U-26：使用参数化查询替代f-string拼接LIMIT
    修复U-21：使用config中的路径常量替代硬编码
    """
    conn = db_module.get_db()
    c = conn.cursor()
    
    if packaged_only:
        # 获取60个packaged skills
        skills = []
        # JueJin 20个（使用config路径）
        if PACKAGED_SKILLS_DIR.exists():
            for d in sorted(PACKAGED_SKILLS_DIR.iterdir()):
                if d.is_dir() and (d / "SKILL.md").exists():
                    c.execute("SELECT id, slug, current_display_name, local_path, source, edition FROM skills WHERE slug = ?", (d.name,))
                    row = c.fetchone()
                    if row:
                        skills.append(dict(row))
        # Open Source 40个（使用config路径）
        if OPENSOURCE_SKILLS_DIR.exists():
            for d in sorted(OPENSOURCE_SKILLS_DIR.iterdir()):
                if d.is_dir() and (d / "SKILL.md").exists():
                    c.execute("SELECT id, slug, current_display_name, local_path, source, edition FROM skills WHERE slug = ?", (d.name,))
                    row = c.fetchone()
                    if row:
                        skills.append(dict(row))
        conn.close()
        return skills
    
    if specific_slugs:
        placeholders = ','.join('?' * len(specific_slugs))
        c.execute(f"""
            SELECT id, slug, current_display_name, local_path, source, edition
            FROM skills
            WHERE slug IN ({placeholders})
              AND workflow_state != 'deprecated'
            ORDER BY slug
        """, specific_slugs)
    else:
        query = """
            SELECT id, slug, current_display_name, local_path, source, edition
            FROM skills
            WHERE workflow_state != 'deprecated'
            ORDER BY slug
        """
        if limit:
            query += " LIMIT ?"
            c.execute(query, (limit,))
        else:
            c.execute(query)
    
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    return results

def read_skill_md(local_path):
    """读取SKILL.md内容"""
    if not local_path:
        return ""
    skill_md_path = Path(local_path) / "SKILL.md"
    if not skill_md_path.exists():
        skill_md_path = Path(local_path)
        if not skill_md_path.exists():
            return ""
    content = skill_md_path.read_text(encoding='utf-8')
    if content.startswith('\ufeff'):
        content = content[1:]
    return content

def static_check(skill_content):
    """静态检查（T和C维度的静态部分）"""
    checks = {
        'has_frontmatter': False,
        'has_displayName': False,
        'has_summary': False,
        'has_description': False,
        'has_license': False,
        'has_tools': False,
        'has_core_capability': False,
        'has_use_cases': False,
        'has_workflow': False,
        'has_examples': False,
        'has_error_handling': False,
        'has_dependencies': False,
        'has_faq': False,
        'has_limitations': False,
        'frontmatter_valid': False,
        'description_length': 0,
        'body_line_count': 0,
        'has_hardcoded_keys': False,
        'has_exaggeration': False,
        'has_reserved_words': False,
        'issues': []
    }
    
    if not skill_content:
        checks['issues'].append('SKILL.md内容为空')
        return checks
    
    # A3修复: 使用skill_core.parse_frontmatter替代自行解析
    parsed = parse_frontmatter(skill_content)
    if parsed['raw']:
        fm = parsed['raw']
        body = parsed['body']
        checks['has_frontmatter'] = True
        checks['frontmatter_valid'] = True
        
        checks['has_displayName'] = bool(re.search(r'^displayName:', fm, re.MULTILINE))
        checks['has_summary'] = bool(re.search(r'^summary:', fm, re.MULTILINE))
        checks['has_license'] = bool(re.search(r'^license:', fm, re.MULTILINE))
        checks['has_tools'] = bool(re.search(r'^tools:', fm, re.MULTILINE))
        
        # description长度
        desc_match = re.search(r'description:\s*\|-\s*\n((?:\s+.+\n?)+)', fm)
        if desc_match:
            desc_text = desc_match.group(1).strip()
            checks['description_length'] = len(desc_text)
            checks['has_description'] = True
        else:
            desc_match = re.search(r'description:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if desc_match:
                checks['description_length'] = len(desc_match.group(1).strip())
                checks['has_description'] = True
        
        # 检查硬编码凭证（排除代码块）
        fm_no_code = re.sub(r'```[\s\S]*?```', '', fm)
        key_patterns = [
            r'sk-[a-zA-Z0-9]{20,}',
            r'AKIA[A-Z0-9]{16}',
            r'ghp_[a-zA-Z0-9]{36}',
        ]
        for pattern in key_patterns:
            if re.search(pattern, fm_no_code):
                checks['has_hardcoded_keys'] = True
                checks['issues'].append('frontmatter含硬编码凭证')
                break
        
        # 检查保留词
        for field in ['displayName', 'summary']:
            match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if match:
                value = match.group(1).lower()
                # A3修复: 使用skill_core.rules.RESERVED_WORDS替代硬编码
                for word in RESERVED_WORDS:
                    if re.search(rf'\b{word}\b', value):
                        checks['has_reserved_words'] = True
                        checks['issues'].append(f'{field}含保留词{word}')
                        break
        
        # 检查夸大词
        for field in ['displayName', 'summary']:
            match = re.search(rf'^{field}:\s*["\']?(.+?)["\']?\s*$', fm, re.MULTILINE)
            if match:
                # A3修复: 使用skill_core.rules.EXAGGERATION_WORDS替代硬编码(消除16词vs10词不一致)
                for word in EXAGGERATION_WORDS:
                    if word in match.group(1):
                        checks['has_exaggeration'] = True
                        checks['issues'].append(f'{field}含夸大词{word}')
                        break
    else:
        body = parsed['body']
        if skill_content.startswith('---'):
            checks['issues'].append('frontmatter格式错误')
        else:
            checks['issues'].append('缺少frontmatter')
    
    # 检查正文章节 — V181增强: 覆盖章节多样化标题和常见同义替代名
    # V173章节多样化将统一标题替换为基于slug哈希的变体, 需同步更新检测关键词
    # 同时覆盖实际SKILL.md中使用的常见同义词(如"核心特性"/"能力清单"/"应用场景"等)
    checks['has_core_capability'] = any(kw in body for kw in [
        '核心能力', '核心功能', '## 功能', '核心特性', '能力清单', '主要功能',
        '功能概览', '专业版增强能力', '功能介绍', '功能说明', '核心模块',
        # V185: 新增变体根词(覆盖所有V184/V185变体)
        '核心特点', '关键特性', '主要特性', '核心属性', '关键特点', '主要特点',
        '功能特点', '功能亮点', '功能特色', '功能特征', '功能描述',
        '能力概览', '能力总览', '能力一览', '能力矩阵', '能力清单', '能力图谱',
        '功能总览', '功能简介', '功能速览', '功能一览', '功能梳理',
        '功能矩阵', '功能清单', '功能图谱',
    ])
    checks['has_use_cases'] = any(kw in body for kw in [
        '适用场景', '使用场景', '## 场景', '应用场景', '使用案例', '典型场景',
        '应用案例', '适用范围', '使用范围',
        # V183: 新增变体标题检测
        '排除场景', '不推荐用法', '场景排除',
        # V185: 新增变体根词
        '场景介绍', '场景示例', '典型场景',
    ])
    checks['has_workflow'] = any(kw in body for kw in [
        '使用流程', '工作流程', '## Step', '### Step', '## 步骤', '快速开始', '快速上手',
        '快速入门', '开始使用', '操作步骤', '使用方法', '操作流程', '调用流程',
        '运行方式', '使用指南', '上手指南',
        # V183: 新增变体标题检测
        '使用指引', '实操说明', '操作入门', '使用向导', '快速指引',
        '部署指引', '安装步骤', '部署说明', '安装向导', '上线流程',
        # V185: 新增变体根词(覆盖所有V184/V185变体)
        '即刻上手', '零基础入门', '新手引导', '初学指南', '启动指引',
        '入门指引', '快速启航', '初次使用指南', '快速熟悉',
        '即学即用', '快速掌握', '迅速上手', '轻松上手', '快速启动',
        '入门教程', '初学者指南', '首次设置', '环境初始化',
        '配置向导', '系统准备', '初始设定',
    ])
    checks['has_examples'] = any(kw in body for kw in [
        '示例', 'Example', '## 示例', '输入', '输出', '案例展示', '用法示例',
        '请求格式', '结果格式', '输出说明', '输出规范', '参数说明', '输入参数',
        '输入定义', '使用范例', '调用示例', '实战案例', '应用实例',
        # V185: 新增变体根词
        '案例', '示例展示', '用法',
    ])
    checks['has_error_handling'] = any(kw in body for kw in [
        '错误处理', '异常处理', 'Error Handling', '故障排查', '错误码',
        '错误处理机制', '异常应对', '诊断与修复', '异常管理', '排障手册',
        '问题处理指引', '错误恢复', '异常恢复', '边界条件与错误处理',
        '排错指南', '故障排除', '错误应对',
        # V185: 新增变体根词(覆盖所有V184/V185变体)
        '错误应对策略', '错误处理指南', '故障处理方案', '异常应对措施',
        '错误处理指引', '问题应对方案', '异常处理指南', '错误处理策略',
        '故障应对方案', '异常处理指引',
        '异常处理架构', '错误处理体系', '异常处理体系', '错误处理框架',
        '异常处理框架', '错误管理机制', '异常管理机制',
        '错误恢复指南', '错误恢复流程', '故障恢复', '异常修复',
        '错误恢复方案', '故障恢复流程', '异常恢复方案',
        '错误恢复策略', '故障修复指南', '异常恢复指引',
    ])
    checks['has_dependencies'] = any(kw in body for kw in [
        '依赖说明', '## 依赖', 'Dependencies', 'API Key', 'LLM',
        # V173多样化标题变体
        '环境要求', '前置条件', '依赖与配置', '运行环境', '安装与配置',
        '初始配置', '技术要求', '系统要求', '配置说明', '环境配置',
    ])
    checks['has_faq'] = any(kw in body for kw in [
        '常见问题', 'FAQ', 'Q:', 'A:',
        # V173多样化标题变体
        '常见问答', '用户答疑', '问题与解答', '常见疑问解答', '帮助中心',
        '热门问题', '疑问解答', '常见疑问', '问答中心',
        # V185: 新增变体根词(覆盖所有V184/V185变体)
        '问答', '疑问', '咨询', '答疑',
        '疑问速答', '高频问答', '热门问答', '常见咨询',
        '用户疑问', '用户咨询', '用户问答',
        '问答集', '问题答疑', '问题解答',
        '高频疑问', '常见疑问答疑', '热门疑问',
        '支持中心', '技术支持', '帮助指南', '使用支持',
        '协助指南', '支持文档', '帮助文档', '帮助手册',
        '问题汇编', '问题汇总', '疑问汇编', '常见问题集',
        '问题整理', '问题合集',
        '问答集锦', '问答合集', '问答整理', '问答集成',
        '问答速查', '问答总汇',
    ])
    checks['has_limitations'] = any(kw in body for kw in [
        '已知限制', '限制说明', 'Limitations', '不适用',
        '功能边界', '能力边界', '使用限制', '注意事项', '约束条件',
        '适用限制', '范围限制', '局限性',
        # V183: 新增变体标题检测
        '使用限制说明', '排除场景', '不推荐用法', '适用边界说明', '场景排除',
        # V185: 新增变体根词
        '使用边界', '功能边界', '适用边界', '限制与边界', '范围与限制',
        '能力限制说明', '使用范围限制', '功能适用范围', '边界与约束',
        '能力边界说明',
    ])
    
    checks['body_line_count'] = len([l for l in body.split('\n') if l.strip()])
    
    # 缺失章节
    missing = []
    if not checks['has_core_capability']: missing.append('核心能力')
    if not checks['has_use_cases']: missing.append('适用场景')
    if not checks['has_workflow']: missing.append('使用流程')
    if not checks['has_examples']: missing.append('示例')
    if not checks['has_error_handling']: missing.append('错误处理')
    if not checks['has_dependencies']: missing.append('依赖说明')
    if not checks['has_faq']: missing.append('常见问题')
    if missing:
        checks['issues'].append(f'缺失章节: {", ".join(missing)}')
    
    return checks

def calculate_static_scores(checks):
    """根据静态检查计算T/R/A/C/E五个维度的基础分

    V181修正: V180曾将R/A/E从0改为静态估算, 导致2025个skill获得虚高分数
    (avg 49.3/50, 100% >=45), 与local_quality_scorer的LLM评分(338个<4.5)严重
    不一致。根因: 静态检查仅验证"章节存在"而非"内容质量", 模板生成的skill
    都有完整章节但内容质量参差不齐。

    修正策略: R/A/E回归0(仅静态检查无法评估质量), 静态评分仅作为T+C基线
    (max 20/50), 必须通过llm-batch命令补充R+A+E维度才能获得完整TRACE评分。
    这确保只有经过LLM真实评估的skill才能达到45+通过阈值。

    各维度评分依据:
      T (Trust): frontmatter完整性+安全性(无硬编码密钥/保留词/夸大词) — 静态可判
      R (Reliability): 需LLM评估错误处理质量/边界条件覆盖/降级策略 — 静态不可判
      A (Adaptability): 需LLM评估场景描述精准度/触发条件明确性 — 静态不可判
      C (Convention): 章节完整性+frontmatter字段+描述长度 — 静态可判
      E (Effectiveness): 需LLM评估示例可用性/输出价值/额外收益 — 静态不可判
    """
    # === T (Trust) 基础分 (0-10) — 静态可判 ===
    trust = 0
    if checks['has_frontmatter']: trust += 1.5
    if checks['frontmatter_valid']: trust += 1.5
    if checks['has_license']: trust += 1.5
    if checks['has_tools']: trust += 1.5
    if not checks['has_hardcoded_keys']: trust += 1.5
    if not checks['has_reserved_words']: trust += 1.5
    if not checks['has_exaggeration']: trust += 1.0
    trust = min(10, trust)

    # === R (Reliability) 基础分 — V181: 回归0, 需LLM评估 ===
    # 可靠性评估需要判断错误处理的质量(而非仅存在), 静态检查无法替代
    reliability = 0

    # === A (Adaptability) 基础分 — V181: 回归0, 需LLM评估 ===
    # 适用性评估需要判断场景描述的精准度(而非仅存在), 静态检查无法替代
    adaptability = 0

    # === C (Convention) 基础分 (0-10) — 静态可判 ===
    section_count = sum([
        checks['has_core_capability'], checks['has_use_cases'],
        checks['has_workflow'], checks['has_examples'],
        checks['has_error_handling'], checks['has_dependencies'],
        checks['has_faq'], checks['has_limitations']
    ])
    convention = min(8, section_count * 1.0)  # 8个章节满分8
    if checks['has_displayName']: convention += 0.5
    if checks['has_summary']: convention += 0.5
    if checks['has_description']: convention += 0.5
    if 50 <= checks['description_length'] <= 300: convention += 0.5
    convention = min(10, convention)

    # === E (Effectiveness) 基础分 — V181: 回归0, 需LLM评估 ===
    # 有效性评估需要判断示例的可用性和输出价值(而非仅存在), 静态检查无法替代
    effectiveness = 0

    return {
        'trust_static': round(trust, 1),
        'reliability_static': round(reliability, 1),
        'adaptability_static': round(adaptability, 1),
        'convention_static': round(convention, 1),
        'effectiveness_static': round(effectiveness, 1),
    }

def save_trace_score(skill_id, checks, static_scores, llm_result=None):
    """保存TRACE评分到数据库
    
    修复U-01：使用TRACE_FIELD_MAPPING保证字段语义正确
    修复U-23：使用TRACE_PASS_THRESHOLD统一阈值（原为硬编码40）
    TD-24修复: 新增cost_score维度传递(辅助维度,不参与total_score计算)
    
    TRACE维度 → scores表字段 完整映射关系(TD-27完善):
    ┌──────────────────┬──────────────────────┬───────────────────────────────────────┐
    │ TRACE维度        │ scores表字段         │ 说明                                  │
    ├──────────────────┼──────────────────────┼───────────────────────────────────────┤
    │ T (Trust)        │ debranding_score     │ 去品牌化+安全性+frontmatter规范性     │
    │ R (Reliability)  │ quality_score        │ 可靠性: 异常处理/边界条件/降级策略    │
    │ A (Adaptability) │ practicality_score   │ 适用性: 场景描述/触发条件/限制说明    │
    │ C (Convention)   │ simplicity_score     │ 规范性: 章节完整性/文档充分性         │
    │ E (Effectiveness)│ performance_score    │ 有效性: 示例/代码/输出格式/FAQ        │
    │ cost (辅助)      │ cost_score           │ 成本评估: 免费/开源/API限制(TD-24)    │
    ├──────────────────┼──────────────────────┼───────────────────────────────────────┤
    │ (T副本)          │ compliance_score     │ 合规维度: 存trust副本,同T值          │
    │ (E副本)          │ differentiation_score│ 差异化维度: 存effectiveness副本,同E值│
    └──────────────────┴──────────────────────┴───────────────────────────────────────┘
    
    设计意图说明:
    - compliance_score存trust副本: 合规维度与可信任度共享相同的安全评估基础
    - differentiation_score存effectiveness副本: 差异化维度与有效性共享输出价值评估
    - cost_score为辅助维度: 不参与total_score计算,仅记录到DB供参考(TD-24新增)
    - total_score = T + R + A + C + E (5个核心维度,满分50)
    """
    conn = db_module.get_db()
    c = conn.cursor()
    now = datetime.now().isoformat()
    
    if llm_result:
        # 合并静态分和LLM分
        trace = llm_result.get('trace_scores', {})
        trust_score = max(static_scores['trust_static'], trace.get('trust', {}).get('score', 0))
        reliability_score = trace.get('reliability', {}).get('score', 0)
        adaptability_score = trace.get('adaptability', {}).get('score', 0)
        convention_score = max(static_scores['convention_static'], trace.get('convention', {}).get('score', 0))
        effectiveness_score = trace.get('effectiveness', {}).get('score', 0)
        # TD-24: 提取cost_score(辅助维度, 不参与total计算)
        cost_score = llm_result.get('cost_score', 0)
        total = round(trust_score + reliability_score + adaptability_score + convention_score + effectiveness_score, 1)
        grade = llm_result.get('quality_grade', 'D')
        notes = json.dumps({
            'issues': checks['issues'],
            'top_3': llm_result.get('top_3_issues', []),
            'suggestions': {k: v.get('suggestion', '') for k, v in trace.items()},
            'static_scores': static_scores,
            'llm_scores': {k: v.get('score', 0) for k, v in trace.items()},
            'evaluated_at': now,
            'field_mapping': TRACE_FIELD_MAPPING,
        }, ensure_ascii=False)
        is_pass = 1 if total >= TRACE_PASS_THRESHOLD else 0
    else:
        # V180: 仅静态评分 — 使用五维度静态估算(不再将R/A/E设为0)
        trust_score = static_scores['trust_static']
        reliability_score = static_scores.get('reliability_static', 0)
        adaptability_score = static_scores.get('adaptability_static', 0)
        convention_score = static_scores['convention_static']
        effectiveness_score = static_scores.get('effectiveness_static', 0)
        cost_score = 0  # 辅助维度, 静态评分时为0
        total = round(trust_score + reliability_score + adaptability_score + convention_score + effectiveness_score, 1)
        # V180: 基于实际总分判定等级和通过状态(不再强制D/0)
        if total >= L2_EXCELLENT_THRESHOLD:
            grade = 'A'
        elif total >= TRACE_SCORE_GRADE_B:
            grade = 'B'
        elif total >= TRACE_SCORE_GRADE_C:
            grade = 'C'
        else:
            grade = 'D'
        notes = json.dumps({
            'issues': checks['issues'],
            'static_only': True,
            'static_scores': static_scores,
            'message': 'V180五维度静态估算, LLM评估可覆盖提升',
            'field_mapping': TRACE_FIELD_MAPPING,
        }, ensure_ascii=False)
        is_pass = 1 if total >= TRACE_PASS_THRESHOLD else 0
    
    # 使用映射常量写入，语义清晰可追溯
    # TD-27: compliance_score存trust副本(合规维度), differentiation_score存effectiveness副本(差异化维度)
    # cost_score为辅助维度(TD-24),已在上方提取
    differentiation_val = effectiveness_score
    compliance_val = trust_score
    
    # R7-1收口: 使用db_module.save_score替代裸SQL，保持is_current历史保护
    conn.close()  # 关闭前面的连接，save_score内部会自建连接
    
    db_module.save_score(
        skill_id=skill_id,
        score_type=SCORE_TYPE_TRACE_LLM,
        total_score=total,
        quality=reliability_score,
        practicality=adaptability_score,
        simplicity=convention_score,
        performance=effectiveness_score,
        debranding=trust_score,
        differentiation=differentiation_val,
        compliance=compliance_val,
        cost=cost_score,  # TD-24: 传递cost_score到DB
        reviewer='trace_llm_scorer_v2',
        notes=notes,
        is_pass=is_pass,
        pass_threshold=TRACE_PASS_THRESHOLD,
    )
    
    return {
        'total': total, 'grade': grade,
        'trust': trust_score, 'reliability': reliability_score,
        'adaptability': adaptability_score, 'convention': convention_score,
        'effectiveness': effectiveness_score,
        'is_llm_evaluated': llm_result is not None
    }


# ============================================================
# L2低分标注机制 (Round 09 Step 5.4优化项3)
# ============================================================

def annotate_low_score_skills(limit: int = None) -> List[Dict[str, Any]]:
    """
    扫描L2评分低于L2_MANUAL_REVIEW_THRESHOLD的skill, 标注需AI手动优化的章节。

    标注规则:
    - 总分 < L2_PASS_THRESHOLD(35): 标记为"需重新生成"
    - 总分 < L2_MANUAL_REVIEW_THRESHOLD(40): 标记为"需AI手动优化"
    - 总分 >= L2_EXCELLENT_THRESHOLD(45): 标记为"优秀, 可跳过优化"

    对需优化的skill, 基于TRACE维度得分识别薄弱章节:
    - T < 7: 依赖说明/frontmatter需优化
    - R < 7: 异常处理章节需优化
    - A < 7: 适用场景/description需优化
    - C < 7: 章节完整性需优化
    - E < 7: 案例展示/输出格式需优化

    参数:
    - limit: 最多处理多少个skill (None=全部)

    返回: 标注结果列表
    """
    conn = db_module.get_db()
    c = conn.cursor()

    # 查询低于L2_MANUAL_REVIEW_THRESHOLD的skill
    query = """
        SELECT s.id, s.slug, s.local_path,
               sc.total_score, sc.quality_score, sc.practicality_score,
               sc.simplicity_score, sc.performance_score, sc.debranding_score,
               sc.notes
        FROM scores sc
        JOIN skills s ON sc.skill_id = s.id
        WHERE sc.score_type = 'trace_llm'
          AND sc.total_score < ?
        ORDER BY sc.total_score ASC
    """
    params = (L2_MANUAL_REVIEW_THRESHOLD,)
    if limit:
        query += " LIMIT ?"
        params = (L2_MANUAL_REVIEW_THRESHOLD, limit)

    c.execute(query, params)
    rows = c.fetchall()

    annotations = []
    for row in rows:
        slug = row['slug']
        total = row['total_score']

        # 确定优化级别
        if total < L2_PASS_THRESHOLD:
            action = 'regenerate'
            action_label = '需重新生成'
        else:
            action = 'manual_optimize'
            action_label = '需AI手动优化'

        # 识别薄弱维度和对应章节
        weak_chapters = []
        dimension_chapter_map = {
            'T': ('debranding_score', '依赖说明/frontmatter', '检查frontmatter完整性和依赖配置'),
            'R': ('quality_score', '异常处理', '补充边界输入处理和错误恢复方案'),
            'A': ('practicality_score', '适用场景/description', '优化description精准度和场景描述'),
            'C': ('simplicity_score', '章节完整性', '补全缺失的标准8章节'),
            'E': ('performance_score', '案例展示/输出格式', '增加真实可用的示例和输出模板'),
        }

        for dim, (field, chapter, suggestion) in dimension_chapter_map.items():
            score = row[field]
            if score is not None and score < TRACE_RELIABILITY_THRESHOLD:  # V121 W3: 可靠性维度阈值
                weak_chapters.append({
                    'dimension': dim,
                    'score': score,
                    'chapter': chapter,
                    'suggestion': suggestion,
                })

        annotation = {
            'slug': slug,
            'skill_id': row['id'],
            'l2_total': total,
            'action': action,
            'action_label': action_label,
            'weak_chapters': weak_chapters,
            'scores': {
                'T': row['debranding_score'],
                'R': row['quality_score'],
                'A': row['practicality_score'],
                'C': row['simplicity_score'],
                'E': row['performance_score'],
            }
        }
        annotations.append(annotation)

    conn.close()
    return annotations


def print_low_score_annotations(annotations: List[Dict[str, Any]]):
    """打印低分标注报告"""
    if not annotations:
        print("  ✓ 无需优化的skill (所有skill L2评分≥{})".format(L2_MANUAL_REVIEW_THRESHOLD))
        return

    print(f"  发现 {len(annotations)} 个需优化的skill:")
    print(f"  {'slug':40s} | L2分 | 操作       | 薄弱章节")
    print(f"  " + "-" * 85)

    for a in annotations:
        weak_str = ', '.join(f"{w['dimension']}({w['score']}):{w['chapter']}" for w in a['weak_chapters'])
        if not weak_str:
            weak_str = '-'
        print(f"  {a['slug']:40s} | {a['l2_total']:4.1f} | {a['action_label']:10s} | {weak_str}")


def cmd_static(args, dry_run=False):
    """静态评分（全部skill或packaged或指定slug）

    dry_run=True时仅打印评分结果, 不调用save_trace_score写入数据库。
    V182新增: --slugs slug1,slug2,... 支持指定skill重新评分
    """
    packaged = '--packaged' in args
    limit = None
    specific_slugs = None
    for i, a in enumerate(args):
        if a == '--limit' and i+1 < len(args):
            limit = int(args[i+1])
        elif a == '--slugs' and i+1 < len(args):
            specific_slugs = [s.strip() for s in args[i+1].split(',') if s.strip()]

    skills = get_all_skills(limit=limit, packaged_only=packaged, specific_slugs=specific_slugs)
    print(f"待评估skill数: {len(skills)}")
    if dry_run:
        print("[DRY-RUN] 模拟模式: 仅打印评分结果, 不写入数据库")

    results = []
    for i, skill in enumerate(skills):
        content = read_skill_md(skill.get('local_path'))
        checks = static_check(content)
        static_scores = calculate_static_scores(checks)

        if dry_run:
            # V180: dry_run模式显示五维度评分
            trust_score = static_scores['trust_static']
            reliability_score = static_scores.get('reliability_static', 0)
            adaptability_score = static_scores.get('adaptability_static', 0)
            convention_score = static_scores['convention_static']
            effectiveness_score = static_scores.get('effectiveness_static', 0)
            total = round(trust_score + reliability_score + adaptability_score + convention_score + effectiveness_score, 1)
            print(f"  [DRY-RUN] {skill['slug']}: {total:.1f}/50 "
                  f"(T={trust_score}, R={reliability_score}, A={adaptability_score}, C={convention_score}, E={effectiveness_score})")
            result = {
                'total': total, 'grade': 'A' if total >= 45 else 'B' if total >= 40 else 'C' if total >= 30 else 'D',
                'trust': trust_score, 'reliability': reliability_score,
                'adaptability': adaptability_score, 'convention': convention_score,
                'effectiveness': effectiveness_score, 'is_llm_evaluated': False,
            }
        else:
            result = save_trace_score(skill['id'], checks, static_scores)

        result['slug'] = skill['slug']
        results.append(result)

        if (i + 1) % 200 == 0:
            print(f"  已评估 {i+1}/{len(skills)}")
    
    # 汇总
    graded = {'A': 0, 'B': 0, 'C': 0, 'D': 0}
    for r in results:
        graded[r['grade']] = graded.get(r['grade'], 0) + 1
    
    avg = sum(r['total'] for r in results) / len(results) if results else 0
    print(f"\n静态评分完成:")
    print(f"  A: {graded.get('A', 0)}, B: {graded.get('B', 0)}, C: {graded.get('C', 0)}, D: {graded.get('D', 0)}")
    print(f"  平均分: {avg:.1f}/50 (V180五维度静态估算)")

def cmd_export(args):
    """导出skill供LLM评估"""
    packaged = '--packaged' in args
    limit = None
    for i, a in enumerate(args):
        if a == '--limit' and i+1 < len(args):
            limit = int(args[i+1])
    
    skills = get_all_skills(limit=limit, packaged_only=packaged)
    print(f"导出 {len(skills)} 个skill供LLM评估...")
    
    export_data = []
    for skill in skills:
        content = read_skill_md(skill.get('local_path'))
        if content:
            # 截取前2500字符避免过长
            truncated = content[:2500] + ('...(截断)' if len(content) > 2500 else '')
            checks = static_check(content)
            static_scores = calculate_static_scores(checks)
            
            export_data.append({
                'id': skill['id'],
                'slug': skill['slug'],
                'display_name': skill.get('current_display_name', ''),
                'source': skill.get('source', ''),
                'edition': skill.get('edition', ''),
                'content': truncated,
                'static_scores': static_scores,
                'static_issues': checks['issues']
            })
    
    # 按批次保存（每批20个）
    batch_size = 20
    for i in range(0, len(export_data), batch_size):
        batch = export_data[i:i+batch_size]
        batch_num = i // batch_size + 1
        output_path = EXPORT_DIR / f"trace_eval_batch_{batch_num}.json"
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(batch, f, ensure_ascii=False, indent=2)
        print(f"  批次 {batch_num}: {len(batch)} skills → {output_path}")
    
    # 保存汇总文件
    summary_path = EXPORT_DIR / "trace_eval_summary.json"
    with open(summary_path, 'w', encoding='utf-8') as f:
        json.dump({
            'total_skills': len(export_data),
            'total_batches': (len(export_data) + batch_size - 1) // batch_size,
            'batch_size': batch_size,
            'exported_at': datetime.now().isoformat()
        }, f, ensure_ascii=False, indent=2)
    
    print(f"\n共导出 {len(export_data)} skills, {(len(export_data)+batch_size-1)//batch_size} 个批次")

def cmd_import(args, dry_run=False):
    """导入LLM评估结果

    dry_run=True时仅打印将要导入的数据, 不写入数据库。
    """
    if not args:
        print("用法: python trace_llm_scorer.py import <results.json>")
        return

    results_file = Path(args[0])
    if not results_file.exists():
        print(f"文件不存在: {results_file}")
        return

    with open(results_file, 'r', encoding='utf-8') as f:
        results = json.load(f)

    # 支持单个结果或结果列表
    if isinstance(results, dict):
        results = [results]

    print(f"导入 {len(results)} 个LLM评估结果...")
    if dry_run:
        print("[DRY-RUN] 模拟模式: 仅打印将要导入的数据, 不写入数据库")

    conn = db_module.get_db()
    c = conn.cursor()

    imported = 0
    for result in results:
        slug = result.get('slug')
        if not slug:
            continue

        # 查找skill
        c.execute("SELECT id, local_path FROM skills WHERE slug = ? AND workflow_state != 'deprecated'", (slug,))
        row = c.fetchone()
        if not row:
            print(f"  [SKIP] {slug}: skill不存在")
            continue

        skill_id = row['id']

        if dry_run:
            # dry_run模式: 仅打印将要导入的数据, 不写入数据库
            print(f"  [DRY-RUN] {slug}: {result.get('total_score', 0)}/50 "
                  f"({result.get('quality_grade', 'D')}) — 将写入skill_id={skill_id}")
            imported += 1
            continue

        # 读取内容进行静态检查
        content = read_skill_md(row['local_path'])
        checks = static_check(content)
        static_scores = calculate_static_scores(checks)

        # 保存合并评分
        save_trace_score(skill_id, checks, static_scores, result)
        imported += 1
        print(f"  [OK] {slug}: {result.get('total_score', 0)}/50 ({result.get('quality_grade', 'D')})")

    conn.close()
    print(f"\n导入完成: {imported}/{len(results)}")

def cmd_report(args):
    """生成评分报告"""
    packaged = '--packaged' in args
    
    conn = db_module.get_db()
    c = conn.cursor()
    
    if packaged:
        # 获取60个packaged skill的评分
        packaged_slugs = []
        skillhub_dir = PACKAGED_SKILLS_DIR
        if skillhub_dir.exists():
            for d in sorted(skillhub_dir.iterdir()):
                if d.is_dir():
                    packaged_slugs.append(d.name)
        opensource_dir = OPENSOURCE_SKILLS_DIR
        if opensource_dir.exists():
            for d in sorted(opensource_dir.iterdir()):
                if d.is_dir():
                    packaged_slugs.append(d.name)
        
        placeholders = ','.join('?' * len(packaged_slugs))
        c.execute(f"""
            SELECT s.slug, s.current_display_name, s.source, s.edition,
                   sc.total_score, sc.debranding_score AS trust,
                   sc.quality_score AS reliability, sc.practicality_score AS adaptability,
                   sc.simplicity_score AS convention, sc.performance_score AS effectiveness,
                   sc.is_pass, sc.notes
            FROM skills s
            LEFT JOIN scores sc ON s.id = sc.skill_id AND sc.score_type = 'trace_llm'
            WHERE s.slug IN ({placeholders})
            ORDER BY CASE WHEN sc.total_score IS NULL THEN 1 ELSE 0 END, sc.total_score DESC
        """, packaged_slugs)
    else:
        c.execute("""
            SELECT s.slug, s.current_display_name, s.source, s.edition,
                   sc.total_score, sc.debranding_score AS trust,
                   sc.quality_score AS reliability, sc.practicality_score AS adaptability,
                   sc.simplicity_score AS convention, sc.performance_score AS effectiveness,
                   sc.is_pass, sc.notes
            FROM skills s
            LEFT JOIN scores sc ON s.id = sc.skill_id AND sc.score_type = 'trace_llm'
            WHERE s.workflow_state != 'deprecated'
            ORDER BY CASE WHEN sc.total_score IS NULL THEN 1 ELSE 0 END, sc.total_score DESC
        """)
    
    results = [dict(r) for r in c.fetchall()]
    conn.close()
    
    scope = "Packaged Skills" if packaged else "全部Skills"
    print(f"\n{'='*90}")
    print(f"TRACE评分报告 - {scope}")
    print(f"{'='*90}")
    print(f"总计: {len(results)}个skill")
    
    graded = [r for r in results if r['total_score'] is not None]
    not_graded = [r for r in results if r['total_score'] is None]
    
    if graded:
        avg = sum(r['total_score'] for r in graded) / len(graded)
        llm_evaluated = sum(1 for r in graded if r['reliability'] and r['reliability'] > 0)
        static_only = len(graded) - llm_evaluated
        
        print(f"\n已评分: {len(graded)}/{len(results)}")
        print(f"  LLM评估: {llm_evaluated}个")
        print(f"  仅静态: {static_only}个")
        print(f"  未评分: {len(not_graded)}个")
        print(f"  平均分: {avg:.1f}/50")
        
        # 等级分布
        grades = {'A (45-50)': 0, 'B (40-44)': 0, 'C (30-39)': 0, 'D (<30)': 0}
        for r in graded:
            score = r['total_score']
            if score >= L2_EXCELLENT_THRESHOLD: grades['A (45-50)'] += 1
            elif score >= TRACE_SCORE_GRADE_B: grades['B (40-44)'] += 1  # V121 W3: TRACE评级
            elif score >= TRACE_SCORE_GRADE_C: grades['C (30-39)'] += 1
            else: grades['D (<30)'] += 1
        
        print(f"\n等级分布:")
        for grade, count in grades.items():
            pct = count/len(graded)*100 if graded else 0
            bar = '█' * int(pct/2)
            print(f"  {grade}: {count:>4} ({pct:.1f}%) {bar}")
        
        # 五维度均分
        if llm_evaluated > 0:
            llm_graded = [r for r in graded if r['reliability'] and r['reliability'] > 0]
            dims = {
                'T (Trust)': sum(r['trust'] or 0 for r in llm_graded) / len(llm_graded),
                'R (Reliability)': sum(r['reliability'] or 0 for r in llm_graded) / len(llm_graded),
                'A (Adaptability)': sum(r['adaptability'] or 0 for r in llm_graded) / len(llm_graded),
                'C (Convention)': sum(r['convention'] or 0 for r in llm_graded) / len(llm_graded),
                'E (Effectiveness)': sum(r['effectiveness'] or 0 for r in llm_graded) / len(llm_graded),
            }
            print(f"\n五维度均分(LLM评估的{llm_evaluated}个):")
            for dim, score in dims.items():
                bar = '█' * int(score)
                print(f"  {dim:<25} {score:.1f}/10 {bar}")
        
        # Top 15
        print(f"\nTop 15:")
        for r in graded[:15]:
            llm_tag = " [LLM]" if r['reliability'] and r['reliability'] > 0 else " [静态]"
            print(f"  {r['slug']:<40} {r['total_score']:>5.1f}/50{llm_tag}  {r['current_display_name'] or ''}")
        
        # Bottom 15
        if len(graded) > 15:
            print(f"\nBottom 15:")
            for r in graded[-15:]:
                llm_tag = " [LLM]" if r['reliability'] and r['reliability'] > 0 else " [静态]"
                print(f"  {r['slug']:<40} {r['total_score']:>5.1f}/50{llm_tag}  {r['current_display_name'] or ''}")
    
    # 保存报告到JSON
    report_path = DATA_DIR / "reports" / "trace_evaluation_report.json"
    with open(report_path, 'w', encoding='utf-8') as f:
        json.dump({
            'timestamp': datetime.now().isoformat(),
            'scope': scope,
            'total': len(results),
            'graded': len(graded),
            'not_graded': len(not_graded),
            'results': [{k: v for k, v in r.items() if v is not None} for r in results]
        }, f, ensure_ascii=False, indent=2)
    print(f"\n报告保存到: {report_path}")

def cmd_annotate(args):
    """低分标注 - 扫描L2低分skill并标注需优化的章节"""
    import argparse
    parser = argparse.ArgumentParser(description='L2低分标注')
    parser.add_argument('--limit', type=int, help='最多处理数量')
    parser.add_argument('--json', action='store_true', help='JSON格式输出')
    parsed = parser.parse_args(args)

    annotations = annotate_low_score_skills(limit=parsed.limit)

    if parsed.json:
        print(json.dumps(annotations, ensure_ascii=False, indent=2))
    else:
        print(f"\n{'='*70}")
        print(f"L2低分标注报告 (阈值<{L2_MANUAL_REVIEW_THRESHOLD})")
        print(f"{'='*70}")
        print_low_score_annotations(annotations)


# ============================================================
# V178: 批量LLM评估 — 为仅有静态评分(T+C)的skill补充R+A+E维度
# ============================================================

def _load_trace_llm_config():
    """加载LLM配置（复用quality_scoring_config.json）"""
    config_path = DATA_DIR / "config" / "quality_scoring_config.json"
    if not config_path.exists():
        raise FileNotFoundError(f"配置文件不存在: {config_path}")
    with open(config_path, "r", encoding="utf-8") as f:
        return json.load(f)


def _get_trace_api_key(config):
    """获取API密钥（复用local_quality_scorer的密钥获取逻辑）"""
    env_var = config.get("llm", {}).get("api_key_env", "ZHIPU_API_KEY")
    api_key = os.environ.get(env_var, "")
    if not api_key:
        for fallback_env in ["SILICONFLOW_API_KEY", "DEEPSEEK_API_KEY", "OPENAI_API_KEY"]:
            api_key = os.environ.get(fallback_env, "")
            if api_key:
                return api_key
    return api_key


def _call_trace_llm(skill_content, config, api_key):
    """调用LLM API进行TRACE五维度评估

    V178: 新增 — 直接在trace_llm_scorer内部调用LLM API,
    不再依赖export/import外部流程。复用quality_scoring_config.json的LLM配置。

    返回: {"trace_scores": {...}, "total_score": float, "quality_grade": str, "top_3_issues": [...]}
    或 {"error": str}
    """
    llm_config = config.get("llm", {})
    # 复用quality_scoring_config的endpoint，但使用TRACE专有prompt
    endpoint = llm_config.get("api_endpoint", "https://open.bigmodel.cn/api/paas/v4/chat/completions")
    model = llm_config.get("model", "glm-4-flash")
    fallback_model = llm_config.get("fallback_model", "glm-4-flash")
    max_tokens = llm_config.get("max_tokens", 4000)
    temperature = llm_config.get("temperature", 0.3)
    timeout = llm_config.get("timeout", 120)

    # 截断过长内容（避免token超限）
    max_chars = 15000
    if len(skill_content) > max_chars:
        skill_content = skill_content[:max_chars] + "\n... (内容已截断)"

    # 使用TRACE评估prompt
    prompt = TRACE_EVAL_PROMPT.format(skill_content=skill_content)

    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}",
    }

    models_to_try = [model]
    if fallback_model and fallback_model != model:
        models_to_try.append(fallback_model)

    for current_model in models_to_try:
        payload = {
            "model": current_model,
            "messages": [
                {"role": "system", "content": "你是SkillHub TRACE评测专家，请严格按照JSON格式返回评测结果。"},
                {"role": "user", "content": prompt},
            ],
            "max_tokens": max_tokens,
            "temperature": temperature,
        }

        try:
            resp = requests.post(endpoint, headers=headers, json=payload, timeout=timeout)
            if resp.status_code == 429 and current_model != models_to_try[-1]:
                print(f"    [429] {current_model}余额不足，降级到{fallback_model}")
                continue
            resp.raise_for_status()
            data = resp.json()
            content = data["choices"][0]["message"]["content"]
            return _parse_trace_llm_response(content)
        except requests.exceptions.Timeout:
            if current_model != models_to_try[-1]:
                continue
            return {"error": f"LLM API请求超时({timeout}s)"}
        except requests.exceptions.ConnectionError as e:
            if current_model != models_to_try[-1]:
                continue
            return {"error": f"LLM API连接失败: {e}"}
        except requests.exceptions.HTTPError as e:
            if resp.status_code == 429 and current_model != models_to_try[-1]:
                continue
            return {"error": f"LLM API HTTP错误: {e}"}
        except (KeyError, IndexError) as e:
            return {"error": f"LLM API返回格式异常: {e}"}
        except Exception as e:
            return {"error": f"LLM API调用异常: {e}"}

    return {"error": "LLM API调用失败，已尝试所有模型"}


def _parse_trace_llm_response(content):
    """解析LLM返回的TRACE评估JSON

    V178: 新增 — 健壮解析TRACE评估结果，支持markdown代码块包裹的JSON
    """
    # 从markdown代码块中提取JSON
    json_match = re.search(r"```(?:json)?\s*(\{.*?\})\s*```", content, re.DOTALL)
    if json_match:
        content = json_match.group(1)

    # 清理控制字符
    sanitized = content.replace("\x00", "").replace("\x01", "").replace("\x02", "")
    for i in range(3, 32):
        sanitized = sanitized.replace(chr(i), "")

    # 尝试直接解析JSON
    try:
        data = json.loads(sanitized, strict=False)
        return data
    except json.JSONDecodeError as e:
        print(f"[WARN] _parse_trace_llm_response: 直接解析JSON失败: {e}")

    # 尝试提取JSON部分
    start = sanitized.find("{")
    end = sanitized.rfind("}")
    if start != -1 and end != -1:
        json_str = sanitized[start: end + 1]
        try:
            data = json.loads(json_str, strict=False)
            return data
        except json.JSONDecodeError as e:
            print(f"[WARN] _parse_trace_llm_response: 提取JSON部分解析失败: {e}")

    # 最终回退：用正则提取各维度分数
    trace_scores = {}
    for dim in ["trust", "reliability", "adaptability", "convention", "effectiveness"]:
        score_match = re.search(
            rf'"{dim}"\s*:\s*\{{\s*"score"\s*:\s*([0-9.]+)',
            sanitized, re.IGNORECASE
        )
        if score_match:
            trace_scores[dim] = {"score": float(score_match.group(1)), "reason": "", "suggestion": ""}

    total_match = re.search(r'"total_score"\s*:\s*([0-9.]+)', sanitized)
    grade_match = re.search(r'"quality_grade"\s*:\s*"?([ABCD])"?', sanitized)

    if trace_scores:
        total = float(total_match.group(1)) if total_match else sum(
            v["score"] for v in trace_scores.values()
        )
        grade = grade_match.group(1) if grade_match else "D"
        return {
            "trace_scores": trace_scores,
            "total_score": total,
            "quality_grade": grade,
            "top_3_issues": [],
        }

    return {"error": f"无法解析LLM返回的TRACE评估结果: {content[:200]}"}


def cmd_llm_batch(args, dry_run=False):
    """批量LLM评估 — 为仅有静态评分(T+C)的skill补充R+A+E维度

    V178: 新增命令，增强现有trace_llm_scorer.py而非创建新脚本。

    工作流程:
    1. 查询DB中score_type='trace_llm'且is_current=1但quality_score=0(静态评分)的skill
    2. 对每个skill读取SKILL.md，调用LLM API进行TRACE五维度评估
    3. 合并静态T/C分和LLM R/A/E分，保存完整TRACE评分
    4. 支持断点续扫、速率限制、进度报告

    Usage:
        python trace_llm_scorer.py llm-batch                 # 评估所有静态评分的skill
        python trace_llm_scorer.py llm-batch --limit 50     # 仅评估50个
        python trace_llm_scorer.py llm-batch --dry-run       # 模拟运行
        python trace_llm_scorer.py llm-batch --rate 1.0      # 每次调用间隔1秒
    """
    limit = None
    rate_limit = 0.5
    for i, a in enumerate(args):
        if a == '--limit' and i + 1 < len(args):
            limit = int(args[i + 1])
        elif a == '--rate' and i + 1 < len(args):
            rate_limit = float(args[i + 1])

    # 1. 加载配置
    try:
        config = _load_trace_llm_config()
    except FileNotFoundError as e:
        print(f"错误: {e}")
        return

    api_key = _get_trace_api_key(config)
    if not api_key:
        print("错误: 未找到LLM API密钥，请设置环境变量 ZHIPU_API_KEY")
        return

    # 2. 查询需要LLM评估的skill — V181: 使用reviewer字段区分静态/LLM评分
    # V180曾使R/A/E不为0导致此查询失效, V181回归R/A/E=0后reviewer字段成为唯一可靠标识
    conn = db_module.get_db()
    c = conn.cursor()
    c.execute("""
        SELECT s.id, s.slug, s.local_path, sc.total_score as static_total
        FROM skills s
        JOIN scores sc ON sc.skill_id = s.id AND sc.is_current = 1
        WHERE s.current_status NOT IN ('deleted')
        AND (s.skill_type IS NULL OR s.skill_type != 'source')
        AND sc.score_type = 'trace_llm'
        AND sc.reviewer = 'trace_llm_scorer_v2'
        ORDER BY s.slug
    """)
    rows = c.fetchall()
    conn.close()

    total_to_eval = len(rows)
    if limit:
        rows = rows[:limit]

    print(f"\n{'='*60}")
    print(f"V178: TRACE批量LLM评估")
    print(f"{'='*60}")
    print(f"待评估: {len(rows)}/{total_to_eval} 个skill (仅有静态T+C评分)")
    if dry_run:
        print("[DRY-RUN] 模拟模式: 仅打印将要评估的skill，不调用API")
    print(f"速率限制: {rate_limit}秒/次")
    print(f"模型: {config.get('llm', {}).get('model', 'glm-4-flash')}")
    print()

    if dry_run:
        for row in rows[:20]:
            print(f"  [DRY-RUN] {row['slug']}: 静态分={row['static_total']}/50 → 将补充R+A+E维度")
        if len(rows) > 20:
            print(f"  ... 还有 {len(rows) - 20} 个")
        return

    # 3. 批量评估
    success_count = 0
    error_count = 0
    skip_count = 0

    for i, row in enumerate(rows):
        slug = row['slug']
        skill_id = row['id']
        local_path = row['local_path']

        # 读取SKILL.md
        content = read_skill_md(local_path)
        if not content:
            print(f"  [{i+1}/{len(rows)}] SKIP {slug}: 无法读取SKILL.md")
            skip_count += 1
            continue

        # 调用LLM评估
        result = _call_trace_llm(content, config, api_key)

        if "error" in result:
            print(f"  [{i+1}/{len(rows)}] ERROR {slug}: {result['error'][:80]}")
            error_count += 1
        else:
            # 读取内容进行静态检查（用于合并静态分）
            checks = static_check(content)
            static_scores = calculate_static_scores(checks)

            # 保存合并评分（静态T/C + LLM R/A/E）
            save_trace_score(skill_id, checks, static_scores, result)

            total = result.get('total_score', 0)
            grade = result.get('quality_grade', 'D')
            pass_str = "PASS" if total >= TRACE_PASS_THRESHOLD else "FAIL"
            print(f"  [{i+1}/{len(rows)}] {pass_str} {slug}: {total:.1f}/50 ({grade})")
            success_count += 1

        # 速率限制
        if rate_limit > 0:
            time.sleep(rate_limit)

        # 每100个输出进度
        if (i + 1) % 100 == 0:
            print(f"\n  --- 进度: {i+1}/{len(rows)} | 成功={success_count} 失败={error_count} 跳过={skip_count} ---\n")

    # 4. 汇总
    print(f"\n{'='*60}")
    print(f"TRACE LLM批量评估完成")
    print(f"{'='*60}")
    print(f"  成功: {success_count}")
    print(f"  失败: {error_count}")
    print(f"  跳过: {skip_count}")
    print(f"  总计: {len(rows)}")

    if success_count > 0:
        # 查询更新后的通过率
        conn = db_module.get_db()
        c = conn.cursor()
        c.execute("""
            SELECT COUNT(*) as total,
                SUM(CASE WHEN sc.total_score >= ? THEN 1 ELSE 0 END) as pass_count
            FROM scores sc
            JOIN skills s ON sc.skill_id = s.id
            WHERE s.current_status NOT IN ('deleted')
            AND (s.skill_type IS NULL OR s.skill_type != 'source')
            AND sc.score_type = 'trace_llm'
            AND sc.is_current = 1
        """, (TRACE_PASS_THRESHOLD,))
        result = c.fetchone()
        conn.close()
        total_scores = result[0] if result else 0
        pass_count = result[1] if result else 0
        print(f"\n  全局TRACE通过率: {pass_count}/{total_scores} = {pass_count*100/max(total_scores,1):.1f}%")


def main():
    import argparse
    parser = argparse.ArgumentParser(
        description='LLM驱动的TRACE评分脚本 v2.0',
        add_help=False
    )
    parser.add_argument('command', nargs='?', help='命令: static/export/import/report/annotate')
    parser.add_argument('--dry-run', action='store_true',
                        help='模拟运行, 仅打印结果不写入数据库(适用于static和import)')
    parsed, remaining_args = parser.parse_known_args()

    if not parsed.command:
        print(__doc__)
        return

    cmd = parsed.command
    dry_run = parsed.dry_run
    # remaining_args包含子命令专属参数(如--packaged, --limit, 文件路径等)
    args = remaining_args

    if cmd == 'static':
        cmd_static(args, dry_run=dry_run)
    elif cmd == 'export':
        cmd_export(args)
    elif cmd == 'import':
        cmd_import(args, dry_run=dry_run)
    elif cmd == 'report':
        cmd_report(args)
    elif cmd == 'annotate':
        cmd_annotate(args)
    elif cmd == 'llm-batch':
        cmd_llm_batch(args, dry_run=dry_run)
    else:
        print(f"未知命令: {cmd}")
        print(__doc__)

if __name__ == '__main__':
    main()
