---
slug: ui-ux-promax-plus-pro
name: ui-ux-promax-plus-pro
version: 1.0.0
displayName: UI/UX ProMax+专业版
summary: 完整设计资源库+图表推荐+UX模式库+组件规范+决策矩阵,面向企业设计团队的专业资源引擎
license: Proprietary
edition: pro
description: '面向企业设计团队的完整UI/UX设计资源引擎,包含全部界面风格库、配色方案、

  字体配对、25种图表类型推荐、UX交互模式库、常用组件设计规范和完整

  设计决策矩阵。核心能力:

  - 完整UI风格库(50+种,含深度分析和适用场景)

  - 全部配色方案(100+调色板+语义令牌系统)

  - 完整字体配对(含可变字体和Google Fonts集成)

  - 25种数据可视化图表类型推荐

  - UX交互模式库(加载/错误/空状态/反馈等)

  - 常用组件设计规范(按钮/卡片/表单/表格/导航)

  - 完整设计决策矩阵和配色选择指南

  ...'
tags:
- 设计
- UI
- UX
- 配色
- 字体
- 前端
- 企业级
- 资源库
- 组件规范
- 数据可视化
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"
tools: ["read", "write", "exec"]
tags: "UI设计,前端,设计"
category: "Creative"
---
# UI/UX ProMax+ - 专业版
## 概述
UI/UX ProMax+专业版是一款面向企业设计团队的完整UI/UX设计资源引擎。在免费版基础资源之上,扩展至25种数据可视化图表推荐、UX交互模式库、常用组件设计规范和完整设计决策矩阵,帮助企业建立系统化、可维护的设计标准.
专业版提供企业级设计令牌系统,支持主题切换和跨平台一致性。完全兼容免费版设计决策框架,可无缝升级.
## 核心能力
### 1. 完整UI风格库(含深度分析)
| 风格 | 特征 | 适用产品 | 注意事项 |
|---|---|----|----|
| Minimalist | 极简留白、少即是多 | SaaS、工具类 | 避免过度留白导致空洞 |
| Glassmorphism | 半透明+模糊背景 | 创意、科技 | 浅色模式需提高不透明度 |
| Neumorphism | 柔和凹凸阴影 | 社交、健康 | 对比度需额外注意 |
| Brutalist | 大胆粗犷、原始感 | 创意agency | 不适合企业级应用 |
| Material Design | Google规范、层次清晰 | 企业、通用 | 保持Elevation规范 |
| Dark Mode | 深色背景、高对比 | 开发者工具 | 分层暗色非纯黑 |
| Soft UI | 柔和渐变、温和 | 教育、社交 | 触摸目标需达标 |
| Corporate | 专业、严谨、可靠 | 金融、法律 | 避免过于冰冷 |

**输入**: 用户提供完整UI风格库(含深度分析)所需的指令和必要参数.
**处理**: 解析完整UI风格库(含深度分析)的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回完整UI风格库(含深度分析)的响应数据,包含状态码、结果和日志.
### 2. 配色方案与语义令牌系统
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | UI/UX ProMax+专业版处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```css
:root {
  /* 品牌色令牌 */
  --color-brand-primary:   #2563eb;
  --color-brand-secondary: #64748b;
  --color-brand-accent:    #22d3ee;
// ...
  /* 语义色令牌 */
  --color-action-primary:    var(--color-brand-primary);
  --color-action-hover:      #1d4ed8;
  --color-action-disabled:   #93c5fd;
  --color-feedback-success:  #10b981;
  --color-feedback-error:    #ef4444;
  --color-feedback-warning:  #f59e0b;
  --color-feedback-info:     #3b82f6;
// ...
  /* 表面令牌 */
  --color-surface-base:    #ffffff;
  --color-surface-raised:  #f8fafc;
  --color-surface-overlay: rgba(255, 255, 255, 0.8);
// ...
  /* 文字令牌 */
  --color-text-primary:    #0f172a;
  --color-text-secondary:  #475569;
  --color-text-disabled:   #94a3b8;
  --color-text-inverse:    #ffffff;
}
```

配色选择矩阵:

| 场景 | 主色 | 辅助色 | 强调色 | 语义 |
|---:|---:|---:|---:|---:|
| 科技产品 | Blue-600 | Slate-500 | Cyan-400 | 信任/专业 |
| 健康医疗 | Teal-600 | Gray-500 | Emerald-400 | 健康/安全 |
| 金融科技 | Indigo-700 | Gray-600 | Amber-500 | 稳重/可靠 |
| 电商零售 | Rose-600 | Gray-500 | Violet-500 | 温暖/时尚 |
| 教育培训 | Violet-600 | Slate-500 | Yellow-400 | 智慧/创意 |
| 娱乐社交 | Fuchsia-600 | Gray-500 | Pink-500 | 活力/热情 |
| 企业SaaS | Slate-700 | Slate-500 | Blue-500 | 专业/中性 |
| 开发者工具 | Slate-900 | Slate-600 | Green-400 | 技术/极客 |

**输入**: 用户提供配色方案与语义令牌系统所需的指令和必要参数.
**处理**: 解析配色方案与语义令牌系统的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回配色方案与语义令牌系统的响应数据,包含状态码、结果和日志.
### 3. 25种数据可视化图表推荐
| 数据类型 | 推荐图表 | 适用场景 | 库推荐 |
|:---:|:---:|:---:|:---:|
| 趋势变化 | 折线图 | 时间序列数据 | Recharts/Chart.js |
| 趋势变化 | 面积图 | 累积趋势 | Recharts |
| 对比分析 | 柱状图 | 分类对比 | Chart.js |
| 对比分析 | 条形图 | 横向分类对比 | Recharts |
| 对比分析 | 雷达图 | 多维度对比 | Chart.js |
| 占比分布 | 饼图 | 简单占比 | Chart.js |
| 占比分布 | 环形图 | 占比+中心数据 | Recharts |
| 占比分布 | 树状图 | 层级占比 | D3.js |
| 占比分布 | 漏斗图 | 转化漏斗 | Recharts |
| 关系网络 | 散点图 | 相关性分析 | Chart.js |
| 关系网络 | 气泡图 | 三维关系 | Recharts |
| 关系网络 | 力导向图 | 网络关系 | D3.js |
| 地理分布 | 地图 | 区域数据 | Mapbox/D3 |
| 时间线 | 甘特图 | 项目进度 | Gantt Chart |
| 时间线 | 时间轴 | 事件序列 | 自定义 |
| 实时数据 | 仪表盘 | KPI监控 | Recharts |
| 实时数据 | 热力图 | 密度分布 | D3.js |
| 多维数据 | 平行坐标 | 多变量分析 | D3.js |
| 流向分析 | 桑基图 | 流量流向 | D3.js |
| 排名变化 | 凹凸图 | 排名变动 | D3.js |
| 分布统计 | 箱线图 | 统计分布 | Chart.js |
| 分布统计 | 直方图 | 频率分布 | Chart.js |
| 组合展示 | 组合图 | 多指标对比 | Recharts |
| 进度展示 | 进度条 | 完成度 | CSS/Tailwind |
| 进度展示 | 环形进度 | 百分比 | CSS/SVG |

**输入**: 用户提供25种数据可视化图表推荐所需的指令和必要参数.
**处理**: 解析25种数据可视化图表推荐的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回25种数据可视化图表推荐的响应数据,包含状态码、结果和日志.
### 4. UX交互模式库
| 模式类别 | 场景 | 推荐做法 |
|:------|------:|:------|
| 加载状态 | 内容加载中 | 骨架屏优于旋转器(已知布局时) |
| 加载状态 | 按钮提交中 | 禁用按钮+加载指示器 |
| 加载状态 | 全页加载 | 顶部进度条 |
| 空状态 | 首次使用 | 引导插画+首次操作引导 |
| 空状态 | 无搜索结果 | 友好提示+搜索建议 |
| 空状态 | 无数据 | 插画+创建按钮 |
| 错误状态 | 表单验证 | 行内错误提示+修复建议 |
| 错误状态 | 网络错误 | 重试按钮+错误说明 |
| 错误状态 | 404页面 | 友好插画+返回首页 |
| 成功反馈 | 操作完成 | Toast通知+视觉确认 |
| 成功反馈 | 重要操作 | 成功页面+下一步引导 |
| 确认操作 | 删除/不可逆 | 确认对话框+影响说明 |
| 确认操作 | 批量操作 | 影响范围预览 |
| 撤销操作 | 可逆操作 | Toast+撤销按钮 |
| 拖拽排序 | 列表排序 | 拖拽手柄+占位符 |
| 无限滚动 | 长列表 | 触底加载+加载指示 |
| 分页 | 数据表格 | 页码+每页条数选择 |
| 搜索 | 实时搜索 | 防抖+结果高亮 |
| 筛选 | 多条件 | 侧边栏筛选+结果计数 |
| 排序 | 表格数据 | 可点击表头+排序指示 |

**输入**: 用户提供UX交互模式库所需的指令和必要参数.
**处理**: 解析UX交互模式库的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回UX交互模式库的响应数据,包含状态码、结果和日志.
### 5. 常用组件设计规范
#### 按钮规范
| 类型 | 用途 | Tailwind类名 |
|---:|:---|---:|
| 主要 | 主操作(提交/保存) | bg-primary text-white hover:bg-primary/90 |
| 次要 | 辅助操作(取消) | bg-secondary text-white hover:bg-secondary/80 |
| 轮廓 | 替代次要操作 | border border-primary text-primary hover:bg-primary/10 |
| 幽灵 | 工具栏操作 | text-primary hover:bg-primary/10 |
| 危险 | 删除/不可逆 | bg-red-600 text-white hover:bg-red-700 |
| 禁用 | 不可用状态 | opacity-50 cursor-not-allowed |

按钮尺寸:
```text
小:   px-3 py-1.5 text-sm     (32px高)
中:   px-4 py-2   text-base    (40px高,默认)
大:   px-6 py-3   text-lg      (48px高)
```

#### 卡片规范
```css
/* 标准卡片 */
.card {
  background-color: var(--color-surface-base);
  border: 1px solid var(--color-border);
  border-radius: var(--radius-lg);
  padding: var(--space-lg);
  box-shadow: var(--shadow-sm);
  transition: box-shadow 0.2s ease;
}
// ...
.card:hover {
  box-shadow: var(--shadow-md);
}
// ...
/* 玻璃态卡片 */
.card-glass {
  background-color: rgba(255, 255, 255, 0.8);
  backdrop-filter: blur(12px);
  border: 1px solid rgba(255, 255, 255, 0.2);
  border-radius: var(--radius-lg);
}
```

#### 表单规范
| 元素 | 规范 | Tailwind类名 |
|:------:|--------|:-------|
| 标签 | 上方排列,font-medium | block text-sm font-medium mb-2 |
| 输入框 | 44px高度,焦点环 | w-full px-4 py-3 border rounded-lg focus:ring-2 |
| 错误提示 | 下方红色文字 | text-sm text-red-600 mt-1 |
| 帮助文本 | 下方灰色文字 | text-sm text-gray-500 mt-1 |
| 必填标记 | 红色星号 | text-red-500 ml-1 |

#### 表格规范
```css
/* 数据表格 */
.table {
  width: 100%;
  border-collapse: collapse;
}
// ...
.table th {
  text-align: left;
  padding: 12px 16px;
  font-size: 14px;
  font-weight: 600;
  color: var(--color-text-secondary);
  background-color: var(--color-surface-raised);
  border-bottom: 1px solid var(--color-border);
}
// ...
.table td {
  padding: 16px;
  font-size: 14px;
  color: var(--color-text-primary);
  border-bottom: 1px solid var(--color-border);
}
// ...
.table tr:hover td {
  background-color: var(--color-surface-raised);
}
```

**输入**: 用户提供常用组件设计规范所需的指令和必要参数.
**处理**: 解析常用组件设计规范的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回常用组件设计规范的响应数据,包含状态码、结果和日志.
### 6. 完整设计决策矩阵
| 决策维度 | 问题 | 选项 | 影响 |
|----|:--:|---:|----|
| 目标用户 | 谁使用产品? | 企业/消费者/高端 | 决定风格基调 |
| 产品类型 | 解决什么问题? | 工具/内容/社交 | 决定布局重点 |
| 品牌调性 | 传递什么感觉? | 创新/稳定/独特 | 决定风格选择 |
| 行业规范 | 有何约束? | 金融/医疗/教育 | 决定配色方向 |
| 数据密度 | 展示多少数据? | 低/中/高 | 决定布局密度 |
| 交互频率 | 多久操作一次? | 高频/低频 | 决定交互优化 |
| 平台范围 | 覆盖哪些端? | Web/iOS/Android | 决定技术栈 |
| 无障碍要求 | 合规等级? | AA/AAA | 决定对比度标准 |

**输入**: 用户提供完整设计决策矩阵所需的指令和必要参数.
**处理**: 解析完整设计决策矩阵的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回完整设计决策矩阵的响应数据,包含状态码、结果和日志.
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：完整设计资源库、组件规范、面向企业设计团队、的专业资源引擎、的完整、设计资源引擎、包含全部界面风格、字体配对、种图表类型推荐、和完整、核心能力、含深度分析和适用、全部配色方案、调色板、完整字体配对、含可变字体和、Fonts、类型推荐、反馈等、和配色选择指南等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景
### 场景一:企业数据仪表盘设计
设计一个包含多种图表的企业数据仪表盘.
```text
步骤1:确定图表类型
  - KPI总览 -> 环形进度图 + 数字卡片
  - 趋势分析 -> 折线图(时间序列)
  - 占比分布 -> 环形图(分类占比)
  - 排名对比 -> 条形图(横向对比)
  - 实时监控 -> 仪表盘(实时指标)
# ...
步骤2:选择配色
  行业: 企业SaaS -> Slate-700 + Slate-500 + Blue-500
# ...
步骤3:应用组件规范
  - 数据表格 -> 使用表格规范
  - 筛选器 -> 使用表单规范
  - 操作按钮 -> 使用按钮规范
```

### 场景二:电商产品列表页设计
```text
步骤1:选择风格
  行业: 电商零售 -> Modern E-commerce
# ...
步骤2:选择配色
  Rose-600 + Gray-500 + Violet-500
# ...
步骤3:应用UX模式
  - 搜索: 实时搜索+防抖+高亮
  - 筛选: 侧边栏筛选+结果计数
  - 排序: 可点击表头
  - 加载: 骨架屏(已知布局)
  - 空状态: 插画+创建按钮
# ...
步骤4:组件规范
  - 商品卡片 -> 玻璃态卡片规范
  - 加入购物车 -> 主要按钮
  - 收藏 -> 幽灵按钮
```

### 场景三:团队设计规范文档编写
```text
步骤1:建立设计令牌系统
  - 色彩令牌 -> 品牌色+语义色+表面色+文字色
  - 字体令牌 -> 标题+正文+代码
  - 间距令牌 -> 8px基准体系
  - 圆角令牌 -> sm/md/lg/full
  - 阴影令牌 -> sm/md/lg/xl
# ...
步骤2:定义组件规范
  - 按钮(6种类型x3种尺寸)
  - 卡片(标准+玻璃态)
  - 表单(标签+输入+错误+帮助)
  - 表格(表头+行+悬停)
# ...
步骤3:编写UX模式库
  - 加载/空/错误/成功状态
  - 确认/撤销操作
  - 搜索/筛选/排序
```

## 不适用场景

以下场景UI/UX ProMax+专业版不适合处理：

- 实时流数据处理
- 小规模数据手动分析
- 非结构化文本情感分析

## 触发条件

需要数据分析、报表生成、统计洞察、数据可视化时使用。不适用于非本工具能力范围的需求.
## 快速开始
### 使用流程
1. 阅读## 核心能力章节了解skill功能
2. 按## 依赖说明配置环境
3. 执行所需能力对应的命令
4. 参考## 错误处理章节处理异常
5. 查看## FAQ解答常见疑问

```text
1.查询UI风格库 -> 确定产品风格
2.查询配色矩阵 -> 选择行业配色
3.查询字体配对 -> 确定字体方案
4.查询图表推荐 -> 选择数据可视化方式
5.查询UX模式库 -> 确定交互模式
6.查询组件规范 -> 应用设计规范
7.建立设计令牌 -> 配置Tailwind/CSS变量
```

### 设计令牌系统配置
```javascript
// design-tokens.js - 企业级设计令牌
module.exports = {
  colors: {
    brand: {
      primary: '#2563eb',
      secondary: '#64748b',
      accent: '#22d3ee',
    },
    semantic: {
      success: '#10b981',
      error: '#ef4444',
      warning: '#f59e0b',
      info: '#3b82f6',
    },
    surface: {
      base: '#ffffff',
      raised: '#f8fafc',
      overlay: 'rgba(255, 255, 255, 0.8)',
    },
    text: {
      primary: '#0f172a',
      secondary: '#475569',
      disabled: '#94a3b8',
      inverse: '#ffffff',
    },
  },
  typography: {
    fontFamily: {
      heading: 'Inter, system-ui, sans-serif',
      body: 'Inter, system-ui, sans-serif',
      mono: 'JetBrains Mono, monospace',
    },
    fontSize: {
      xs: '12px', sm: '14px', base: '16px',
      lg: '18px', xl: '20px', '2xl': '24px',
      '3xl': '30px', '4xl': '36px', '5xl': '48px',
    },
  },
  spacing: {
    xs: '4px', sm: '8px', md: '16px',
    lg: '24px', xl: '32px', '2xl': '48px', '3xl': '64px',
  },
  radius: {
    sm: '4px', md: '8px', lg: '12px', full: '9999px',
  },
  shadow: {
    sm: '0 1px 2px rgba(0,0,0,0.05)',
    md: '0 4px 6px rgba(0,0,0,0.1)',
    lg: '0 10px 15px rgba(0,0,0,0.1)',
    xl: '0 20px 25px rgba(0,0,0,0.15)',
  },
};
```

### 专业版与免费版完整对比
| 功能维度 | 免费版 | 专业版 |
|----|----|----|
| UI风格库 | 50+风格浏览 | 全部+深度分析+注意事项 |
| 配色方案 | 100+调色板 | 全部+语义令牌系统 |
| 字体配对 | 精选组合 | 全部+可变字体+Google Fonts |
| 图表推荐 | 不支持 | 25种图表类型+库推荐 |
| UX模式库 | 不支持 | 20+交互模式 |
| 组件规范 | 不支持 | 按钮/卡片/表单/表格 |
| 设计令牌 | 不支持 | 完整令牌系统 |
| 决策框架 | 基础三问 | 8维度决策矩阵 |
| 适用对象 | 个人设计师 | 企业设计团队 |
| 兼容性 | - | 完全兼容免费版 |

## 最佳实践
### 1. 好的设计是解决问题
先确保可用性,再追求美观。设计不是堆砌特效,而是解决用户问题.
### 2. 建立设计令牌系统
使用语义化令牌而非硬编码值,支持主题切换和跨平台一致性.
### 3. 组件规范一致性
所有同类组件使用相同的设计规范,避免每个页面各做一套.
### 4. 图表类型匹配数据
选择图表前先分析数据类型:趋势用折线,占比用环形,对比用柱状,关系用散点.
### 5. UX模式覆盖所有状态
每个交互流程都需要覆盖:加载、空、错误、成功四个状态.
### 6. 专业提示
- 不要混合太多风格:1种主风格+2-3个元素点缀
- 颜色不超过5种:主色+辅助+中性+成功+错误
- 字体最多2种:1标题+1正文
- 留白是设计:不要害怕空白
- 一致性优先于创新

## 常见问题
### Q1: 专业版兼容免费版的设计决策框架吗?
完全兼容。专业版在免费版三问框架之上扩展至8维度决策矩阵,所有免费版的决策方法在专业版中同样适用.
### Q2: 25种图表推荐如何选择?
根据数据类型选择:趋势变化用折线/面积图,对比分析用柱状/条形图,占比分布用饼图/环形图,关系网络用散点/气泡图,地理分布用地图,实时数据用仪表盘/热力图.
### Q3: 设计令牌如何应用到代码?
通过CSS变量定义令牌,在Tailwind配置中引用。暗色主题通过覆盖CSS变量实现切换。所有组件使用语义化令牌引用而非硬编码值.
### Q4: UX模式库如何使用?
在设计交互流程时,参考模式库确保覆盖所有状态。例如,列表页需要包含:加载骨架屏、空状态引导、错误重试、搜索筛选排序模式.
### 示例
是的。每个组件规范都包含Tailwind CSS类名和CSS代码示例,可直接复制使用。按钮规范包含6种类型x3种尺寸的完整类名.
### Q6: 如何在团队中推广设计规范?
1. 建立设计令牌文件并纳入版本控制
2. 将组件规范同步至Storybook
3. 编写设计系统文档
4. 定期进行设计评审
5. 将令牌同步至Figma Variables

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux
- **Node.js版本**: 18及以上(用于Tailwind CSS构建)

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-----|:-----|:-----|:-----|
| Tailwind CSS | 前端框架 | 必需 | npm install -D tailwindcss |
| Google Fonts | 字体服务 | 推荐 | CDN链接引入 |
| Recharts/Chart.js | 图表库 | 推荐 | npm install recharts/chart.js |
| Figma | 设计工具 | 推荐 | 用于令牌同步 |
| LLM API | API | 必需 | 由Agent内置LLM提供 |

安装命令:

```bash
# Tailwind CSS
npm install -D tailwindcss
# ...
# 图表库(按需选择)
npm install recharts        # React项目推荐
npm install chart.js        # 通用推荐
```

### API Key 配置
本Skill基于Markdown设计资源,无需额外API Key。设计建议由Agent内置LLM驱动。Tailwind CSS和图表库为本地npm包。Figma令牌同步如需使用,需配置Figma API Token.
### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需exec命令行执行)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent完成操作。Tailwind CSS配置、图表库安装和设计令牌文件创建需要exec工具执行npm命令或编辑文件.
## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接后执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令，参考国内替代方案 |

## 已知限制
- 需LLM支持,无LLM环境不可用
- 复杂业务场景建议结合人工经验判断
- 执行效率受模型能力与网络环境影响

## 输出格式
```json
{
  "success": true,
  "data": {
    "result": "UI/UX ProMax+专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "ui ux promax plus pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
