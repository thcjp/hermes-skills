---
slug: smart-cache
name: smart-cache
version: "1.0.0"
displayName: Smart Cache
summary: Intelligent caching with LRU/LFU strategies and TTL management
license: MIT
description: |-
  Intelligent caching with LRU/LFU strategies and TTL management

  核心能力:

  - 其他工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 通用工具、辅助功能、扩展能力

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范
tags:
- Other
tools:
  - - read
- exec
---

# Smart Cache

High-performance caching with multiple eviction strategies.

## Implementation

```javascript
class SmartCache {
  constructor(options = {}) {
    this.strategy = options.strategy || 'lru'; // 'lru' or 'lfu'
    this.maxSize = options.maxSize || 500;
    this.defaultTTL = options.defaultTTL || 3600000; // 1 hour

    this.cache = new Map();
    this.accessCount = new Map();
    this.accessOrder = [];
  }

  set(key, value, ttl = this.defaultTTL) {
    // Evict if at capacity
    if (this.cache.size >= this.maxSize && !this.cache.has(key)) {
      this.evict();
    }

    const entry = {
      value,
      expiresAt: Date.now() + ttl,
      createdAt: Date.now()
    };

    this.cache.set(key, entry);
    this.accessCount.set(key, 0);
    this.updateAccessOrder(key);

    return true;
  }

  get(key) {
    const entry = this.cache.get(key);

    if (!entry) {
      return { hit: false, value: null };
    }

    // Check TTL
    if (Date.now() > entry.expiresAt) {
      this.delete(key);
      return { hit: false, value: null, reason: 'expired' };
    }

    // Update access tracking
    this.accessCount.set(key, (this.accessCount.get(key) || 0) + 1);
    this.updateAccessOrder(key);

    return { hit: true, value: entry.value };
  }

  delete(key) {
    this.cache.delete(key);
    this.accessCount.delete(key);
    this.accessOrder = this.accessOrder.filter(k => k !== key);
  }

  evict() {
    if (this.strategy === 'lru') {
      this.evictLRU();
    } else if (this.strategy === 'lfu') {
      this.evictLFU();
    }
  }

  evictLRU() {
    // Remove least recently used
    if (this.accessOrder.length > 0) {
      const keyToEvict = this.accessOrder[0];
      this.delete(keyToEvict);
    }
  }

  evictLFU() {
    // Remove least frequently used
    let minCount = Infinity;
    let keyToEvict = null;

    for (const [key, count] of this.accessCount.entries()) {
      if (count < minCount) {
        minCount = count;
        keyToEvict = key;
      }
    }

    if (keyToEvict) {
      this.delete(keyToEvict);
    }
  }

  updateAccessOrder(key) {
    // Remove from current position
    this.accessOrder = this.accessOrder.filter(k => k !== key);
    // Add to end (most recent)
    this.accessOrder.push(key);
  }

  clear() {
    this.cache.clear();
    this.accessCount.clear();
    this.accessOrder = [];
  }

  getStats() {
    return {
      size: this.cache.size,
      maxSize: this.maxSize,
      strategy: this.strategy,
      hitRate: this.calculateHitRate()
    };
  }

  calculateHitRate() {
    // Simplified - would track actual hits/misses in production
    return Math.round((this.cache.size / this.maxSize) * 100);
  }
}

// Export for Skill平台
module.exports = { SmartCache };
```

## Usage

```javascript
const cache = new skills.smartCache.SmartCache({
  strategy: 'lru',
  maxSize: 500,
  defaultTTL: 3600000
});

// Set value
cache.set('key1', { data: 'value' }, 60000);

// Get value
const result = cache.get('key1');
if (result.hit) {
  console.log('Cache hit:', result.value);
}

// Stats
console.log(cache.getStats());
```

## Configuration

```json
{
  "strategy": "lru",
  "maxSize": 500,
  "defaultTTL": 3600000
}
```

## 依赖说明

### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 核心能力

- 触发关键词: cache, caching, intelligent, strategies, management, smart

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 使用流程

1. 确认运行环境满足依赖说明中的要求
2. 根据适用场景选择合适的使用方式
3. 执行操作并检查输出结果
4. 如遇错误，参考错误处理章节

## 示例

### 示例1：基础用法

```
输入: 用户请求
处理: 根据使用流程执行
输出: 处理结果
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Smart Cache？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Smart Cache有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要LLM支持，无LLM环境无法使用
- 复杂场景可能需要人工辅助判断
- 性能取决于底层模型能力
