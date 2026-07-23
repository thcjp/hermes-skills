---
slug: test-driven-coder
name: test-driven-coder
version: 1.1.0
displayName: 测试驱动编码器
summary: 强制TDD:Red-Green-Refactor循环,先写测试再写代码,质量内建
license: Proprietary
description: 测试驱动编码器——强制执行测试驱动开发(TDD)流程,先写失败的测试,再写实现代码,最后重构。Red-Green-Refactor循环 +
  测试金字塔分层(单元80%/集成15%/E2E 5%),让代码质量内建于开发过程。适用于新功能开发、Bug修复、重构保护、测试补充、测试审查场景。触发关键词:测试驱动、TDD、单元测试、集成测试、端到端测试、Red-Green-Refactor、测试金字塔、测试覆盖、自动化测试、测试先行、pytest、jest
tags:
- 测试驱动
- TDD
- 单元测试
- 自动化测试
- 代码质量
tools:
- read
- exec
# 定价元数据
suggested_price: "19.9 CNY/per_use"
pricing_tier: "L2-标准级"
pricing_model: "per_use"
---
# 测试驱动编码器

强制执行测试驱动开发流程。核心理念:测试是证明,不是负担。先写失败的测试,再写实现代码,最后重构。让代码质量内建于开发过程,而非事后补丁。

## 核心能力

1. **Red-Green-Refactor 循环**:严格三步法,先红后绿再重构,小步迭代
2. **测试金字塔分层**:单元测试 80% / 集成测试 15% / E2E 测试 5%,合理分布
3. **多语言测试框架**:Python(pytest)/ JavaScript(jest/vitest)/ Go(testing)/ Java(JUnit)
4. **测试反模式检测**:冰激凌测试、实现细节测试、过度 Mock、测试依赖顺序识别
5. **覆盖率与质量评估**:行/分支/函数覆盖率,测试有效性分析(突变测试)

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 新功能开发 | 需求文档、接口定义 | 失败测试用例 + 实现代码 + 重构后的代码 |
| Bug 修复 | Bug 描述、复现步骤 | 复现测试 + 修复代码 + 回归测试 |
| 重构保护 | 现有代码 + 重构目标 | 测试套件 + 重构后代码 + 测试报告 |
| 测试补充 | 遗留无测试代码 | 渐进式测试用例 + 覆盖率提升报告 |
| 测试审查 | 现有测试代码 | 测试质量评估 + 反模式清单 + 改进建议 |

**不适用于**:
- 探索性研究/原型开发(TDD 增加不必要的开销,适合稳定需求)
- UI 视觉调整(布局/颜色/动画,难以用单元测试覆盖)
- 性能优化(使用基准测试工具,如 JMeter/k6)
- 一次性脚本(简单脚本无需 TDD)
- 紧急修复生产故障(先修复,后补测试)
- 文档/注释编写(非代码逻辑)

## 使用流程

### Step 1: Red - 先写失败测试
1. **理解需求**:明确输入、输出、边界条件
2. **写一个失败的测试**:
   - 测试名称描述行为(`should_return_empty_array_when_no_input`)
   - 只写让测试编译通过的最少代码(不实现逻辑)
   - 运行测试,确认它**因正确原因失败**(而非编译错误)
3. **原则**:一次只测一个行为,测试要小而专注

### Step 2: Green - 写最少代码让测试通过
1. **写实现代码**:
   - 只写让测试通过的最少代码
   - 不提前设计,不过度工程化
   - 允许"硬编码"先让测试过
2. **运行测试**:确认绿色通过
3. **原则**:用最简单的方式让测试通过,不追求优雅

### Step 3: Refactor - 重构改善
1. **在测试保护下重构**:
   - 消除重复代码
   - 改善命名和结构
   - 提取公共逻辑
   - 优化性能
2. **每步重构后运行测试**:确保始终绿色
3. **原则**:小步重构,频繁验证,不引入新行为

### Step 4: 测试金字塔分层

## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|--------|------|------|------|
| input | string | 是 | 测试驱动编码器处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
        /\
       /E2E\        5%  端到端测试(慢、脆弱、高信心)
      /------\
     /Integration\  15%  集成测试(中速、模块间交互)
    /--------------\
   /    Unit        \ 80%  单元测试(快、稳定、高覆盖)
  /------------------\
```

#### 单元测试(80%)
- 测试单个函数/类的行为
- 依赖全部 mock
- 执行时间 < 100ms/个
- 命名:`describe('ClassName', () => { it('should_behavior_when_condition') })`

#### 集成测试(15%)
- 测试模块间协作(如 Service + Repository)
- 使用真实依赖或测试数据库
- 执行时间 < 1s/个

#### 端到端测试(5%)
- 测试完整用户流程
- 使用真实环境或接近真实
- 执行时间可接受较慢

### Step 5: 验证与交付
1. 运行全部测试,确认绿色
2. 检查覆盖率(行/分支/函数)
3. 检查测试反模式
4. 生成测试报告

## 核心原则

### DAMP 优于 DRY
- **DRY**(Don't Repeat Yourself):生产代码消除重复
- **DAMP**(Descriptive And Meaningful Phrases):测试代码可读性优先
- 测试中允许重复,只要每个测试自包含、易理解

### Beyoncé 规则
> "If you liked it then you should have put a test on it."

- 任何被用户/其他模块依赖的行为,必须有测试
- 没有测试的代码 = 不存在保证的行为

### 测试命名
- 描述行为而非实现:`should_return_discounted_price_when_user_is_vip`
- 不描述方法调用:`should_call_database_save`(脆弱)
- Given-When-Then 结构可选

### 测试独立性
- 每个测试独立运行,不依赖其他测试
- 不依赖执行顺序
- 每个测试自己准备数据(Setup)和清理(Teardown)

## 测试反模式(避免)

1. **冰激凌测试**:大量 E2E + 少量单元(倒金字塔),慢且脆弱
2. **测试实现细节**:测私有方法、测 mock 调用次数
3. **一个测试测多事**:一个测试包含多个断言不同行为
4. **测试依赖顺序**:必须按特定顺序运行
5. **过度 mock**:mock 了被测对象本身,测试无意义

## 示例

### 示例1: Python TDD - 折扣计算(输入→输出)

**输入**:
```
需求: 实现一个折扣计算函数
规则: VIP 用户享受 20% 折扣,普通用户无折扣,金额为负返回 0
语言: Python (pytest)
```

**输出**(Step 1: Red - 失败测试):
```python
# test_discount.py
import pytest
from discount import calculate_discount

class TestCalculateDiscount:
    def test_should_return_discounted_price_for_vip_user(self):
        result = calculate_discount(amount=100, is_vip=True)
        assert result == 80  # 100 * 0.8

    def test_should_return_original_price_for_normal_user(self):
        result = calculate_discount(amount=100, is_vip=False)
        assert result == 100

    def test_should_return_zero_for_negative_amount(self):
        result = calculate_discount(amount=-50, is_vip=True)
        assert result == 0
```

```python
# discount.py (Step 2: Green - 最少实现)
def calculate_discount(amount: float, is_vip: bool) -> float:
    if amount < 0:
        return 0
    if is_vip:
        return amount * 0.8
    return amount
```

```python
# discount.py (Step 3: Refactor - 重构改善)
from enum import Enum

class UserType(Enum):
    VIP = "vip"
    NORMAL = "normal"

DISCOUNT_RATES = {UserType.VIP: 0.8, UserType.NORMAL: 1.0}

def calculate_discount(amount: float, user_type: UserType) -> float:
    if amount < 0:
        return 0
    return amount * DISCOUNT_RATES[user_type]
```

### 示例2: JavaScript TDD - 数组去重(输入→输出)

**输入**:
```
需求: 实现数组去重函数,支持自定义 key
语言: TypeScript (vitest)
```

**输出**(Red-Green-Refactor 完整流程):
```typescript
// unique.test.ts (Red: 失败测试)
import { describe, it, expect } from 'vitest';
import { uniqueBy } from './unique';

describe('uniqueBy', () => {
  it('should_remove_duplicates_by_default_key', () => {
    const input = [{ id: 1 }, { id: 2 }, { id: 1 }];
    expect(uniqueBy(input, 'id')).toEqual([{ id: 1 }, { id: 2 }]);
  });

  it('should_return_empty_array_for_empty_input', () => {
    expect(uniqueBy([], 'id')).toEqual([]);
  });

  it('should_preserve_first_occurrence', () => {
    const input = [{ id: 1, name: 'A' }, { id: 1, name: 'B' }];
    const result = uniqueBy(input, 'id');
    expect(result).toEqual([{ id: 1, name: 'A' }]);
  });
});
```

```typescript
// unique.ts (Green + Refactor)
export function uniqueBy<T>(arr: T[], key: keyof T): T[] {
  if (arr.length === 0) return [];
  const seen = new Set<unknown>();
  return arr.filter(item => {
    const value = item[key];
    if (seen.has(value)) return false;
    seen.add(value);
    return true;
  });
}
```

### 示例3: 测试审查(输入→输出)

**输入**:
```
现有测试代码:
- 200 个单元测试,30 个 E2E 测试,5 个集成测试
- 单元测试平均执行时间 500ms
- 部分测试依赖执行顺序
```

**输出**(test-report.md 片段):
```markdown
## 测试质量审查报告

### 测试金字塔分析
- 当前比例: 单元 85% / 集成 2% / E2E 13% (倒金字塔倾向)
- 建议: 减少 E2E 至 5%,增加集成测试至 15%

### 反模式检测
1. [Critical] 12 个测试依赖执行顺序(测试共享状态)
   - 修复: 每个 Setup 创建独立数据
2. [High] 单元测试平均 500ms(应 <100ms)
   - 原因: 测试中发起了真实 HTTP 请求
   - 修复: Mock 外部依赖
3. [Medium] 8 个测试断言 Mock 调用次数(脆弱)
   - 修复: 断言行为而非实现

### 覆盖率
- 行覆盖: 78% (目标 85%)
- 分支覆盖: 62% (目标 80%)
- 函数覆盖: 85% (达标)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| 测试框架未安装 | 项目无 pytest/jest | 提示安装命令 `pip install pytest` 或 `npm install -D vitest` |
| 测试无法编译/运行 | 语法错误或导入错误 | 先修复编译错误,再确认测试因正确原因失败 |
| 测试间歇性失败 | 测试依赖外部状态(时间/网络/数据库) | Mock 外部依赖,确保测试独立 |
| 覆盖率无法达标 | 难以测试的代码(如异常处理) | 使用依赖注入解耦,或使用突变测试评估 |
| 重构后测试失败 | 重构引入新行为或破坏接口 | 回退重构,小步迭代,每步运行测试 |
| Mock 过多导致测试无意义 | 测试了 Mock 而非真实逻辑 | 减少 Mock,只 Mock 外部边界(数据库/HTTP) |
| E2E 测试脆弱 | 依赖 UI 变化或网络 | 减少依赖,使用 data-testid 而非 CSS 选择器 |
| 测试执行过慢 | 大量 I/O 操作或同步等待 | 单元测试禁止 I/O,移至集成测试 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:-------|:-----|:---------|:---------|:---------|
| LLM API | API | 必需 | Agent 内置 LLM 提供代码生成 | 通义/文心/智谱 |
| pytest | 工具 | Python 必需 | `pip install pytest` | 国内 PyPI 镜像 |
| jest / vitest | 工具 | JS/TS 必需 | `npm install -D vitest` | npmmirror 国内镜像 |
| Go testing | 工具 | Go 内置 | Go 标准库 | - |
| JUnit 5 | 工具 | Java 必需 | Maven/Gradle 依赖 | 阿里云 Maven 镜像 |
| coverage | 工具 | 可选 | pytest-cov / jest --coverage | - |
| mutmut | 工具 | 可选(突变测试) | `pip install mutmut` | 国内 PyPI 镜像 |

### API Key 配置
- **本Skill无需额外API Key配置**
- **安全要求**: 测试中不使用真实 API Key,使用环境变量 TEST_API_KEY 或 Mock

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行测试框架

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: Python TDD - 密码强度验证器(边界条件+多规则)

**输入**:
```
需求: 实现密码强度验证函数 validate_password(password, rules)
规则:
  - 长度 >= 8
  - 包含至少1个大写字母
  - 包含至少1个小写字母
  - 包含至少1个数字
  - 包含至少1个特殊字符(!@#$%^&*)
  - 不包含空格
返回: (is_valid: bool, errors: list[str])
语言: Python (pytest)
```

**LLM生成输出** (Step 1: Red - 失败测试):
```python
# test_password_validator.py
import pytest
from password_validator import validate_password

class TestValidatePassword:
    def test_should_return_valid_for_strong_password(self):
        is_valid, errors = validate_password("Str0ng!Pass")
        assert is_valid is True
        assert errors == []

    def test_should_return_error_when_password_too_short(self):
        is_valid, errors = validate_password("Ab1!x")
        assert is_valid is False
        assert "长度不足,至少需要8位" in errors

    def test_should_return_error_when_no_uppercase(self):
        is_valid, errors = validate_password("str0ng!pass")
        assert is_valid is False
        assert "需包含至少1个大写字母" in errors

    def test_should_return_error_when_no_lowercase(self):
        is_valid, errors = validate_password("STR0NG!PASS")
        assert is_valid is False
        assert "需包含至少1个小写字母" in errors

    def test_should_return_error_when_no_digit(self):
        is_valid, errors = validate_password("Strong!Pass")
        assert is_valid is False
        assert "需包含至少1个数字" in errors

    def test_should_return_error_when_no_special_char(self):
        is_valid, errors = validate_password("Str0ngPass")
        assert is_valid is False
        assert "需包含至少1个特殊字符(!@#$%^&*)" in errors

    def test_should_return_error_when_contains_space(self):
        is_valid, errors = validate_password("Str0ng! Pass")
        assert is_valid is False
        assert "密码不能包含空格" in errors

    def test_should_return_multiple_errors_for_weak_password(self):
        is_valid, errors = validate_password("ab")
        assert is_valid is False
        assert len(errors) >= 4  # 长度+大写+数字+特殊字符

    def test_should_return_valid_for_minimum_acceptable_password(self):
        is_valid, errors = validate_password("Abcdef1!")
        assert is_valid is True
        assert errors == []
```

**LLM生成输出** (Step 2: Green - 最少实现):
```python
# password_validator.py
import re

def validate_password(password: str, rules: dict = None) -> tuple[bool, list[str]]:
    errors = []

    if len(password) < 8:
        errors.append("长度不足,至少需要8位")
    if not re.search(r'[A-Z]', password):
        errors.append("需包含至少1个大写字母")
    if not re.search(r'[a-z]', password):
        errors.append("需包含至少1个小写字母")
    if not re.search(r'\d', password):
        errors.append("需包含至少1个数字")
    if not re.search(r'[!@#$%^&*]', password):
        errors.append("需包含至少1个特殊字符(!@#$%^&*)")
    if ' ' in password:
        errors.append("密码不能包含空格")

    return (len(errors) == 0, errors)
```

**LLM生成输出** (Step 3: Refactor - 可配置规则):
```python
# password_validator.py (重构后)
import re
from dataclasses import dataclass, field
from typing import Callable

@dataclass
class PasswordRule:
    name: str
    error_message: str
    validator: Callable[[str], bool]

def _has_uppercase(s): return bool(re.search(r'[A-Z]', s))
def _has_lowercase(s): return bool(re.search(r'[a-z]', s))
def _has_digit(s): return bool(re.search(r'\d', s))
def _has_special(s): return bool(re.search(r'[!@#$%^&*]', s))
def _no_space(s): return ' ' not in s
def _min_length_8(s): return len(s) >= 8

DEFAULT_RULES = [
    PasswordRule("length", "长度不足,至少需要8位", _min_length_8),
    PasswordRule("uppercase", "需包含至少1个大写字母", _has_uppercase),
    PasswordRule("lowercase", "需包含至少1个小写字母", _has_lowercase),
    PasswordRule("digit", "需包含至少1个数字", _has_digit),
    PasswordRule("special", "需包含至少1个特殊字符(!@#$%^&*)", _has_special),
    PasswordRule("no_space", "密码不能包含空格", _no_space),
]

def validate_password(password: str, rules: list[PasswordRule] = None) -> tuple[bool, list[str]]:
    rules = rules or DEFAULT_RULES
    errors = [rule.error_message for rule in rules if not rule.validator(password)]
    return (len(errors) == 0, errors)
```

**效果验证**: ✓Red阶段9个测试覆盖全部规则与边界 ✓Green阶段最少实现让测试通过 ✓Refactor引入PasswordRule数据类支持自定义规则 ✓测试命名描述行为(should_return_valid_for_strong_password) ✓重构后全部测试仍绿色

### 案例2: TypeScript TDD - 购物车折扣计算(Red-Green-Refactor完整循环)

**输入**:
```
需求: 实现购物车折扣计算
规则:
  - 满100减10,满200减25,满500减60(阶梯不叠加,取最优)
  - VIP用户额外9折(在满减后计算)
  - 优惠券-15元(与满减可叠加)
  - 最终价格不低于0
语言: TypeScript (vitest)
```

**LLM生成输出** (Red: 失败测试):
```typescript
// cart.test.ts
import { describe, it, expect } from 'vitest';
import { calculateFinalPrice } from './cart';

describe('calculateFinalPrice', () => {
  it('should_apply_no_discount_when_subtotal_below_100', () => {
    expect(calculateFinalPrice({ subtotal: 80, isVip: false })).toBe(80);
  });

  it('should_apply_10_off_when_subtotal_reaches_100', () => {
    expect(calculateFinalPrice({ subtotal: 100, isVip: false })).toBe(90);
  });

  it('should_apply_25_off_when_subtotal_reaches_200', () => {
    expect(calculateFinalPrice({ subtotal: 200, isVip: false })).toBe(175);
  });

  it('should_apply_60_off_when_subtotal_reaches_500', () => {
    expect(calculateFinalPrice({ subtotal: 500, isVip: false })).toBe(440);
  });

  it('should_apply_vip_10_percent_after_tier_discount', () => {
    // 100 - 10 = 90, VIP 9折 = 81
    expect(calculateFinalPrice({ subtotal: 100, isVip: true })).toBe(81);
  });

  it('should_apply_coupon_on_top_of_tier_and_vip', () => {
    // 200 - 25 = 175, VIP 9折 = 157.5, 优惠券 -15 = 142.5
    expect(calculateFinalPrice({ subtotal: 200, isVip: true, coupon: 15 })).toBe(142.5);
  });

  it('should_return_zero_when_discounts_exceed_subtotal', () => {
    expect(calculateFinalPrice({ subtotal: 10, isVip: false, coupon: 50 })).toBe(0);
  });

  it('should_not_apply_tier_discounts_cumulatively', () => {
    // 500时只减60,不减(60+25+10)
    expect(calculateFinalPrice({ subtotal: 500, isVip: false })).toBe(440);
  });
});
```

**LLM生成输出** (Green + Refactor):
```typescript
// cart.ts
interface CartInput {
  subtotal: number;
  isVip: boolean;
  coupon?: number;
}

const TIER_DISCOUNTS = [
  { threshold: 500, discount: 60 },
  { threshold: 200, discount: 25 },
  { threshold: 100, discount: 10 },
];

function getTierDiscount(subtotal: number): number {
  for (const tier of TIER_DISCOUNTS) {
    if (subtotal >= tier.threshold) return tier.discount;
  }
  return 0;
}

export function calculateFinalPrice(input: CartInput): number {
  const { subtotal, isVip, coupon = 0 } = input;

  const tierDiscount = getTierDiscount(subtotal);
  const afterTier = subtotal - tierDiscount;

  const afterVip = isVip ? afterTier * 0.9 : afterTier;

  const final = afterVip - coupon;

  return Math.max(0, Math.round(final * 100) / 100);
}
```

**效果验证**: ✓8个测试覆盖阶梯满减/VIP折扣/优惠券叠加/最低价保护 ✓TIER_DISCOUNTS数组使阶梯规则可配置 ✓取最优阶梯(非累加)逻辑通过测试验证 ✓Math.max(0,...)确保不低于0 ✓重构后TIER_DISCOUNTS提取为常量便于维护

### 案例3: Go TDD - 限流器(表驱动测试+并发安全)

**输入**:
```
需求: 实现令牌桶限流器 TokenBucketLimiter
规则:
  - 容量 capacity, 每秒补充 rate 个令牌
  - Allow() 方法:有令牌返回true并消耗1个,否则返回false
  - 并发安全(多goroutine同时调用)
语言: Go (testing)
```

**LLM生成输出** (Red: 失败测试):
```go
// ratelimiter_test.go
package ratelimiter

import (
	"sync"
	"testing"
	"time"
)

func TestTokenBucketLimiter_Allow_WhenBucketFull(t *testing.T) {
	limiter := NewTokenBucketLimiter(5, 1) // 容量5,每秒1个
	for i := 0; i < 5; i++ {
		if !limiter.Allow() {
			t.Fatalf("第%d次请求应被允许,但被拒绝", i+1)
		}
	}
}

func TestTokenBucketLimiter_Deny_WhenBucketEmpty(t *testing.T) {
	limiter := NewTokenBucketLimiter(2, 1)
	limiter.Allow()
	limiter.Allow()
	if limiter.Allow() {
		t.Fatal("桶空时应拒绝请求")
	}
}

func TestTokenBucketLimiter_Refill_AfterWait(t *testing.T) {
	limiter := NewTokenBucketLimiter(1, 10) // 每秒10个=每100ms 1个
	limiter.Allow() // 耗尽
	time.Sleep(150 * time.Millisecond)
	if !limiter.Allow() {
		t.Fatal("等待150ms后应已补充至少1个令牌")
	}
}

func TestTokenBucketLimiter_ConcurrentSafety(t *testing.T) {
	limiter := NewTokenBucketLimiter(100, 1)
	var wg sync.WaitGroup
	allowed := make([]bool, 200)

	for i := 0; i < 200; i++ {
		wg.Add(1)
		go func(idx int) {
			defer wg.Done()
			allowed[idx] = limiter.Allow()
		}(i)
	}
	wg.Wait()

	count := 0
	for _, a := range allowed {
		if a {
			count++
		}
	}
	if count > 100 {
		t.Fatalf("并发下允许数%d超过容量100,存在竞态条件", count)
	}
}

func TestTokenBucketLimiter_TableDriven(t *testing.T) {
	tests := []struct {
		name      string
		capacity  int
		rate      float64
		requests  int
		expectAllow int
	}{
		{"capacity_3_rate_1", 3, 1, 5, 3},
		{"capacity_10_rate_5", 10, 5, 10, 10},
		{"capacity_1_rate_1", 1, 1, 3, 1},
	}

	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			limiter := NewTokenBucketLimiter(tt.capacity, tt.rate)
			allowed := 0
			for i := 0; i < tt.requests; i++ {
				if limiter.Allow() {
					allowed++
				}
			}
			if allowed != tt.expectAllow {
				t.Errorf("期望允许%d次,实际%d次", tt.expectAllow, allowed)
			}
		})
	}
}
```

**LLM生成输出** (Green + Refactor):
```go
// ratelimiter.go
package ratelimiter

import (
	"sync"
	"time"
)

type TokenBucketLimiter struct {
	mu         sync.Mutex
	capacity   int
	tokens     float64
	rate       float64 // 每秒补充令牌数
	lastRefill time.Time
}

func NewTokenBucketLimiter(capacity int, rate float64) *TokenBucketLimiter {
	return &TokenBucketLimiter{
		capacity:   capacity,
		tokens:     float64(capacity),
		rate:       rate,
		lastRefill: time.Now(),
	}
}

func (l *TokenBucketLimiter) Allow() bool {
	l.mu.Lock()
	defer l.mu.Unlock()

	now := time.Now()
	elapsed := now.Sub(l.lastRefill).Seconds()
	l.tokens += elapsed * l.rate
	if l.tokens > float64(l.capacity) {
		l.tokens = float64(l.capacity)
	}
	l.lastRefill = now

	if l.tokens >= 1 {
		l.tokens--
		return true
	}
	return false
}
```

**效果验证**: ✓表驱动测试覆盖多种容量/速率组合 ✓并发安全测试(200 goroutine)验证竞态条件 ✓令牌补充测试验证时间流逝后的补充逻辑 ✓sync.Mutex保证并发安全 ✓Allow()方法懒补充(lazy refill)避免定时器开销

### 案例4: 遗留代码测试补充+反模式审查

**输入**:
```
现有项目: 电商订单服务(Java/Spring Boot)
现状:
  - 总代码行: 12000行
  - 测试代码: 800行(6.7%覆盖率)
  - 单元测试: 15个(平均执行800ms)
  - 集成测试: 2个
  - E2E测试: 25个
  - 问题: 测试执行总时长15分钟,部分E2E间歇性失败
目标: 补充测试 + 审查反模式 + 优化测试金字塔
```

**LLM生成输出** (`test-audit-report.md`):
```markdown
# 测试审查与补充报告

## 1. 测试金字塔分析

### 当前分布(倒金字塔)
| 层级 | 数量 | 占比 | 平均耗时 | 目标占比 |
|:-----|:-----|:-----|:---------|:---------|
| 单元测试 | 15 | 36% | 800ms | 80% |
| 集成测试 | 2 | 5% | 3.2s | 15% |
| E2E测试 | 25 | 60% | 12s | 5% |

### 问题诊断
- **倒金字塔**: E2E占60%,单元仅36%,与理想80/15/5严重倒挂
- **单元测试过慢**: 平均800ms(应<100ms),可能包含真实I/O
- **E2E脆弱**: 25个E2E中间歇性失败,依赖外部环境

## 2. 反模式检测

### [Critical] 8个单元测试包含真实HTTP调用
```java
// 反模式: 单元测试中发起真实HTTP请求
@Test
void testGetOrder() {
    OrderService service = new OrderService();
    Order order = service.getOrder("ORD-001"); // 实际调用数据库!
    assertNotNull(order);
}
```
**修复**: 使用Mockito Mock外部依赖
```java
@Test
void should_return_order_when_order_exists() {
    OrderRepository mockRepo = mock(OrderRepository.class);
    when(mockRepo.findById("ORD-001")).thenReturn(Optional.of(testOrder));
    OrderService service = new OrderService(mockRepo);

    Order result = service.getOrder("ORD-001");

    assertNotNull(result);
    assertEquals("ORD-001", result.getId());
    verify(mockRepo).findById("ORD-001");
}
```

### [High] 5个E2E测试依赖执行顺序
- TestOrderFlow中 `testCreateOrder` 必须先于 `testUpdateOrder` 运行
- **修复**: 每个测试使用@BeforeEach创建独立订单数据

### [Medium] 3个测试断言Mock调用次数
```java
// 脆弱: 断言实现细节而非行为
verify(repo, times(2)).save(any()); // 重构后times可能变,测试就挂
```
**修复**: 断言最终状态而非调用次数
```java
assertThat(repository.findAll()).hasSize(1);
```

## 3. 测试补充计划(优先级排序)

### P0: 核心业务逻辑(订单计算)
```java
// OrderPriceCalculator 测试 - 金额计算是核心,必须有测试
class OrderPriceCalculatorTest {
    private OrderPriceCalculator calculator;

    @BeforeEach
    void setUp() {
        calculator = new OrderPriceCalculator();
    }

    @Test
    void should_calculate_subtotal_from_items() {
        List<OrderItem> items = List.of(
            new OrderItem("P1", new BigDecimal("29.90"), 2),
            new OrderItem("P2", new BigDecimal("15.50"), 1)
        );
        BigDecimal subtotal = calculator.calculateSubtotal(items);
        assertThat(subtotal).isEqualByComparingTo("75.30");
    }

    @Test
    void should_apply_tiered_discount_correctly() {
        BigDecimal result = calculator.applyTierDiscount(new BigDecimal("200"));
        assertThat(result).isEqualByComparingTo("175.00");
    }

    @Test
    void should_not_allow_negative_final_price() {
        BigDecimal result = calculator.calculate(
            new BigDecimal("10"), true, new BigDecimal("50")
        );
        assertThat(result).isEqualByComparingTo("0.00");
    }

    @Test
    void should_use_BigDecimal_not_double_for_currency() {
        // 防止浮点精度问题: 0.1 + 0.2 != 0.3
        BigDecimal result = calculator.calculateSubtotal(List.of(
            new OrderItem("P1", new BigDecimal("0.10"), 1),
            new OrderItem("P2", new BigDecimal("0.20"), 1)
        ));
        assertThat(result).isEqualByComparingTo("0.30");
    }
}
```

### P1: 边界条件(库存扣减)
- 库存为0时下单应抛出InsufficientStockException
- 并发下单同一商品最后一个库存(乐观锁)
- 负数数量应拒绝

### P2: 状态机(订单状态流转)
- PENDING -> PAID -> SHIPPED -> DELIVERED -> COMPLETED
- 非法流转应拒绝(如 PENDING -> SHIPPED)
- CANCELLED状态不可逆

## 4. 测试金字塔优化方案

### 短期(1周): 将E2E降级为集成测试
- 15个E2E实际测的是API层,可降级为@SpringBootTest集成测试
- 预计: E2E从25→10,集成从2→17
- 执行时间从15分钟降至6分钟

### 中期(2周): 补充单元测试
- 优先: OrderPriceCalculator / InventoryService / StateMachine
- 目标: 单元测试从15→80,覆盖率6.7%→45%

### 长期(1月): 达到目标金字塔
| 层级 | 目标数量 | 目标占比 | 目标平均耗时 |
|:-----|:---------|:---------|:-------------|
| 单元 | 120+ | 80% | <50ms |
| 集成 | 20+ | 15% | <2s |
| E2E | 8 | 5% | <15s |
```

**效果验证**: ✓诊断倒金字塔(E2E 60% vs 目标5%) ✓识别8个单元测试含真实HTTP调用的反模式 ✓提供Mockito修复示例代码 ✓测试补充计划按P0/P1/P2优先级排序 ✓金额计算使用BigDecimal防浮点精度 ✓金字塔优化分短/中/长期

## 常见问题

### Q1: TDD 会不会拖慢开发速度?
A: 短期会增加 15-30% 编码时间,但长期收益:
- 减少 50%+ 的 Debug 时间(测试即文档)
- 减少 70%+ 的回归 Bug(测试保护)
- 重构信心大幅提升(测试守护)
- 适合稳定需求;对于高度不确定的原型开发,可先写代码后补测试

### Q2: 哪些代码必须测试,哪些可以不测?
A: 必须测试:
- 核心业务逻辑(计算、规则、状态机)
- 公共 API/接口契约
- 边界条件(空值、极值、异常输入)
- 复杂条件分支

可以不测:
- 简单的 CRUD(框架已测试)
- 纯视图组件(用快照测试或视觉测试)
- 配置文件(用 schema 校验)
- 第三方库(信任其测试)

### Q3: Mock 还是真实依赖?
A: 按测试类型决定:
- **单元测试**: 全部 Mock 外部依赖(数据库/HTTP/文件系统)
- **集成测试**: 使用真实依赖或测试数据库(如 SQLite/H2)
- **E2E 测试**: 使用真实环境或接近真实
- 原则: 测试速度与信心平衡,越外层越真实

### Q4: 覆盖率 100% 是目标吗?
A: 不是。覆盖率只是参考指标,不是目的:
- 100% 覆盖率不代表测试质量高(可能只是行覆盖,未覆盖分支)
- 目标: 行覆盖 85%+ / 分支覆盖 80%+ / 函数覆盖 90%+
- 更重要: 测试有效性(突变测试评分)+ 测试可读性 + 测试独立性
- 过度追求覆盖率会导致测试为覆盖而写,而非为行为而写

## 已知限制

- 对于探索性研究/原型开发,TDD 增加不必要的开销
- UI 视觉效果(布局/颜色/动画)难以用单元测试覆盖,需视觉测试
- 性能测试不适用(使用 JMeter/k6/ab 等专用工具)
- 遗留代码无测试时,TDD 需要先补测试,成本较高
- 测试框架与项目语言/框架强耦合,需手动配置
- 国内安装测试依赖可能较慢,建议配置国内镜像源

## 安全声明

- 测试代码中禁止硬编码真实 API Key/密码/凭证
- 测试环境与生产环境严格隔离(使用 TEST_ 前缀环境变量)
- E2E 测试使用测试账号,禁止使用生产账号
- 测试数据自动清理,不残留到生产数据库
- 输出的测试代码示例中凭证一律使用占位符
