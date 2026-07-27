#!/usr/bin/env python3
"""
[已废弃] SkillHub批量审核通过脚本
================================
此文件已合并到 platform_ops.py 的 batch_approve 函数。

请使用:
    python platform_ops.py batch-approve           # 批量审核所有pending
    python platform_ops.py batch-approve <slug>     # 审核单个skill
    python platform_ops.py batch-approve --check   # 仅检查待审核数量

废弃原因: 与 platform_ops.batch_approve 功能完全重复,
且 platform_ops.batch_approve 已包含客户端二次过滤(H2修复)。

本文件仅作为向后兼容的包装器,所有调用转发到 platform_ops。
"""
import sys
import os
import warnings

# 发出弃用警告
warnings.warn(
    "batch_approve_api.py 已废弃,请使用 platform_ops.py batch-approve",
    DeprecationWarning,
    stacklevel=2
)

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def _redirect():
    """转发到 platform_ops.batch_approve"""
    from platform_ops import batch_approve
    
    if len(sys.argv) > 1:
        if sys.argv[1] == '--check':
            # 检查待审核数量
            result = batch_approve(slugs=[], delay=0)
            print(f"待审核skill数: {result.get('total_pending', 0)}")
        elif sys.argv[1] == '--slug':
            slug = sys.argv[2] if len(sys.argv) > 2 else None
            if slug:
                result = batch_approve([slug], delay=0)
                success = slug in result.get('approved', [])
                print(f"{'✅' if success else '❌'} {slug}")
            else:
                print("错误: 缺少slug参数")
        else:
            print(f"未知参数: {sys.argv[1]}")
            print("用法: python batch_approve_api.py [--check | --slug <slug>]")
    else:
        # 批量审核所有pending
        result = batch_approve(delay=0.3)
        print(f"\n=== 结果 ===")
        print(f"✅ 成功: {len(result.get('approved', []))}")
        print(f"❌ 失败: {len(result.get('failed', []))}")

if __name__ == '__main__':
    print("⚠ 此脚本已废弃,请使用: python platform_ops.py batch-approve")
    print("-" * 50)
    _redirect()
