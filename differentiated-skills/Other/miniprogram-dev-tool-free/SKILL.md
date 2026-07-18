---
slug: miniprogram-dev-tool-free
name: miniprogram-dev-tool-free
version: "1.0.0"
displayName: 小程序开发工具
summary: 面向个人开发者的微信小程序开发规范与避坑工具。
license: MIT
edition: free
description: |-
  面向个人开发者的微信小程序开发规范与避坑工具。

  核心能力:
  - 页面/组件结构与配置规范
  - 数据绑定、事件、生命周期避坑
  - WXSS 样式与 wx:key 性能要点
  - 单项目本地开发与预览

  适用场景:
  - 个人小程序项目开发
  - 单页面/组件规范核对
  - 本地预览与基础调试

  差异化: 免费版聚焦个人单项目开发与避坑，提供规范速查，零成本使用。

  触发关键词: 小程序, 微信小程序, wxml, wxss, wxml 规范, wx:key, 生命周期, miniprogram, wechat
tags:
- 小程序
- 前端开发
- 个人效率
- 其他工具
tools:
- read
- exec
---

# 小程序开发工具（免费版）

## 概述

本工具帮助个人开发者遵循微信小程序开发规范，覆盖页面/组件结构、数据绑定与事件、生命周期、WXSS 样式与 `wx:key` 性能要点。适合单项目本地开发与预览。

## 核心能力

| 能力 | 说明 | 免费版范围 |
|:-----|:-----|:-----------|
| 页面规范 | 目录结构、json 配置 | 单项目 |
| 组件规范 | 自定义组件与插槽 | 基础 |
| 数据绑定 | `{{}}`、事件、setData | 全覆盖 |
| 生命周期 | onLoad/onShow/onUnload | 全覆盖 |
| 样式性能 | WXSS、rpx、wx:key | 关键项 |

## 使用场景

### 场景一：页面结构规范

```text
pages/
  index/
    index.wxml     # 结构
    index.wxss     # 样式
    index.js       # 逻辑
    index.json     # 配置
```

```json
// index.json
{
  "usingComponents": {"nav": "/components/nav/nav"},
  "navigationBarTitleText": "首页"
}
```

### 场景二：数据绑定与事件

```html
<!-- index.wxml -->
<view wx:for="{{list}}" wx:key="id" bindtap="onTap" data-id="{{item.id}}">
  {{item.name}}
</view>
```

```javascript
// index.js
Page({
  data: { list: [{id: 1, name: 'A'}] },
  onTap(e) {
    const id = e.currentTarget.dataset.id;
    this.setData({ [`list[${idx}].name`]: 'B' });  // 局部更新
  }
});
```

### 场景三：wx:key 性能

```html
<!-- 列表必加 wx:key，提升 diff 性能 -->
<view wx:for="{{list}}" wx:key="id">{{item.name}}</view>
```

## 快速开始

1. 用开发者工具创建项目。
2. 按规范组织页面/组件目录。
3. 数据绑定用 `{{}}`，事件用 `bind`/`catch`。
4. 列表必加 `wx:key`。

## 配置示例

关键规范速查：

| 规范 | 说明 |
|:-----|:-----|
| `wx:key` | 列表必加，用唯一字段 |
| `setData` | 局部更新路径，别整对象 |
| `rpx` | 750rpx = 屏宽，响应式单位 |
| `catch` | 阻止冒泡，`bind` 不阻止 |
| 生命周期 | onLoad 一次，onShow 每次 |

## 最佳实践

- **wx:key 必加**：列表不加 wx:key 会告警且 diff 慢。
- **setData 局部**：用路径更新 `list[0].name`，别整个 setData。
- **rpx 适配**：用 rpx 而非 px，自动适配屏宽。
- **catch 阻冒泡**：内部事件用 catch 防止冒泡到父。
- **资源压缩**：图片用 CDN 或压缩，包体积限 2MB。

## 常见问题

**Q1：setData 卡顿怎么办？**
A：改为局部路径更新，减少数据量，避免频繁 setData。

**Q2：能开发多端（支付宝/字节）吗？**
A：免费版聚焦微信小程序。多端框架与跨平台为专业版能力。

**Q3：包体积超 2MB 怎么办？**
A：用分包加载，主包只留核心页，其余分包。

**Q4：免费版支持云开发吗？**
A：支持基础云开发对接。企业云治理与 CI/CD 为专业版能力。

**Q5：自定义组件能继承吗？**
A：用 behaviors 实现类似继承，组件间复用逻辑。

## 进阶用法

### 自定义组件开发

```text
components/
  nav/
    nav.wxml     # 组件结构
    nav.wxss     # 组件样式
    nav.js       # 组件逻辑
    nav.json     # 组件配置
```

```javascript
// nav.js
Component({
  properties: {
    title: { type: String, value: '' }
  },
  methods: {
    onTap() {
      this.triggerEvent('navtap', { title: this.data.title });
    }
  }
});
```

```html
<!-- nav.wxml -->
<view class="nav" bindtap="onTap">{{title}}</view>
```

### 数据绑定与 setData 优化

```javascript
// 错误：整对象 setData（慢）
this.setData({ list: newList });

// 正确：局部路径更新（快）
this.setData({ [`list[${index}].name`]: newValue });

// 批量更新合并
this.setData({
  [`list[0].name`]: 'A',
  [`list[1].name`]: 'B',
  count: 2
});
```

### 生命周期运用

```javascript
Page({
  onLoad(options) {
    // 页面加载一次，可取参数
    this.id = options.id;
  },
  onShow() {
    // 每次显示，刷新数据
    this.fetchData();
  },
  onHide() {
    // 隐藏，暂停定时器
    clearInterval(this.timer);
  },
  onUnload() {
    // 卸载，清理资源
    clearInterval(this.timer);
  }
});
```

## 性能优化要点

| 要点 | 做法 |
|:-----|:-----|
| wx:key | 列表必加唯一 key |
| setData | 局部路径更新，减少数据量 |
| 图片 | CDN + 压缩 + 懒加载 |
| 分包 | 主包 < 2MB，非核心分包 |
| 避免频繁 setData | 合并多次 setData |

## 分包加载

```json
// app.json
{
  "pages": ["pages/index/index"],
  "subpackages": [
    {
      "root": "subpackageA",
      "pages": ["pages/detail/detail"]
    }
  ],
  "preloadRule": {
    "pages/index/index": {
      "network": "all",
      "packages": ["subpackageA"]
    }
  }
}
```

## 开发规范

- **目录清晰**：按页面/组件分目录，命名一致。
- **配置分离**：页面 json 独立配置，别堆 app.json。
- **事件规范**：bind 不阻冒泡，catch 阻冒泡，按需用。
- **资源压缩**：图片压缩，包体 < 2MB。
- **真机调试**：模拟器与真机表现可能不同，必真机测。

## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **微信开发者工具**: 预览与调试

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| 微信开发者工具 | IDE | 必需 | 微信官方下载 |
| Node.js | 运行时 | 构建时必需 | nodejs.org |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 本工具为纯 Markdown 指令，无需额外 API Key
- 云开发需配置小程序 AppID 与云环境

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 生成小程序代码并核对规范
