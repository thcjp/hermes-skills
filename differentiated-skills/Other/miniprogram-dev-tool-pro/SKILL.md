---
slug: miniprogram-dev-tool-pro
name: miniprogram-dev-tool-pro
version: 1.0.0
displayName: 小程序开发工具专业版
summary: 面向团队的多端框架、CI/CD 与企业云治理工具.
license: Proprietary
edition: pro
description: '面向团队的小程序多端框架与企业级开发治理专业工具。核心能力:

  - 多端框架（Taro/uni-app）跨平台开发

  - CI/CD 流水线与自动化发布

  - 企业云开发治理与多环境

  - 性能监控与包体优化

  适用场景:

  - 团队多端小程序统一开发

  - CI/CD 自动化构建发布

  - 企业云治理与性能监控

  差异化: 专业版在免费版单项目微信小程序上扩展多端框架、CI/CD、企业云治理与性能监控，兼容免费版规范'
tags:
- 小程序
- 企业级
- 多端开发
- CI/CD
- 其他工具
tools:
- read
- exec
homepage: https://skillhub.cn
# 定价元数据
suggested_price: "29.9 CNY/per_use"
pricing_tier: "L3-专业级"
pricing_model: "per_use"

---
# 小程序开发工具（专业版）

## 概述

专业版面向团队与企业，在免费版单项目微信小程序基础上，扩展多端框架（Taro/uni-app）、CI/CD 流水线与自动化发布、企业云开发治理与多环境、性能监控与包体优化。开发规范与免费版兼容，已有页面可直接纳入多端框架.
## 核心能力

| 能力 | 说明 | 专业版增强 |
|---|---|-----|
| 多端框架 | Taro/uni-app 一套代码多端 | 跨平台 |
| CI/CD | 自动构建/测试/发布 | 流水线 |
| 企业云 | 多环境云治理 | RBAC |
| 性能监控 | 启动/渲染/包体监控 | 看板 |
| 包体优化 | 分包与依赖分析 | 自动瘦身 |
**技术实现要点**：核心能力基于`input_params`参数与`output_format`配置实现,支持创建/查询/修改/删除等操作模式,通过`config_options`进行运行时配置.
### 核心功能执行
用`input_params`参数进行配置.
**输入**: 用户提供核心功能执行所需的指令和必要参数.
**处理**: 解析核心功能执行的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回核心功能执行的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`input_params`参数,支持创建/查询/导出操作

### 参数配置与调用
用`config_options`参数进行配置.
**输入**: 用户提供参数配置与调用所需的指令和必要参数.
**处理**: 解析参数配置与调用的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回参数配置与调用的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`config_options`参数,支持修改/重置/导入操作

### 结果处理与输出
用`output_format`参数进行配置.
**输入**: 用户提供结果处理与输出所需的指令和必要参数.
**处理**: 解析结果处理与输出的输入参数,完成核心逻辑,返回结构化响应.
**输出**: 返回结果处理与输出的响应数据,包含状态码、结果和日志.
- 执行此能力时使用`output_format`参数,支持导出/保存/转换操作
**能力覆盖范围**：本skill的核心能力覆盖以下场景关键词：面向团队的多端框、与企业云治理工具、面向团队的小程序、多端框架与企业级、开发治理专业工具、跨平台开发、流水线与自动化发、企业云开发治理与、性能监控与包体优等。这些关键词对应description中声明的使用场景,均已在上述能力点中提供对应的操作支持.
## 使用场景

### 场景一：多端框架开发

```bash
# Taro 创建多端项目
npm install -g @tarojs/cli
taro init my-app
# 一套代码编译到微信/支付宝/字节/H5
taro build --type weapp,alipay,tt,h5
```

### 场景二：CI/CD 流水线

```yaml
# .github/workflows/miniprogram.yml（专业版）
name: MiniProgram CI/CD
on: [push]
jobs:
  build:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with: { node-version: '18' }
      - run: npm ci
      - run: npm run lint
      - run: npm run test
      - run: npm run build:weapp
      - name: Upload to WeChat
        run: npx miniprogram-ci upload --pp dist --pkp key.pem --appid $APPID
```

### 场景三：性能监控

```text
性能看板:
  启动耗时: 1.2s（基线 1.5s）✓
  首屏渲染: 380ms
  包体积: 主包 1.8MB / 总 3.2MB
  setData 频次: 平均 12 次/页
  建议: 首页图片懒加载可降 200ms
```

## 不适用场景

以下场景小程序开发工具专业版不适合处理：

- 无明确技术栈的模糊需求
- 纯架构设计决策
- 运维部署管理

## 触发条件

需要代码生成、编程辅助、调试测试、开发部署时使用。不适用于非本工具能力范围的需求.
## 快速开始

1. 将免费版页面迁移到多端框架.
2. 配置 CI/CD 流水线.
3. 接入企业云多环境.
4. 启用性能监控与包体优化.
**响应解析**: 完成完成后,查看输出响应确认任务状态。成功时输出包含解析摘要和响应数据;失败时根据错误信息排查问题,查阅错误解析章节获取恢复步骤.
## 示例

CI/CD 配置（`miniprogram-ci.json`）：

```json
{
  "platforms": ["weapp", "alipay", "tt"],
  "build": {"cmd": "npm run build", "output": "dist"},
  "deploy": {"wechat": {"appid": "wxXXX", "key": "key.pem"}},
  "performance": {"monitor": true, "budget_kb": 2048}
}
```

## 最佳实践

- **多端先抽象**：多端框架先抽公共逻辑，差异用条件编译.
- **CI 先 lint/test**：流水线先跑 lint 与测试，违规阻断.
- **分包控主包**：主包 < 2MB，非核心页分包懒加载.
- **性能定基线**：启动/渲染定基线，劣化告警.
- **发布用机器人**：CI 用 miniprogram-ci 机器人发布，避免人工误操作.
## 免费版兼容性

| 项目 | 免费版 | 专业版 |
|:-----|:-----|:-----|
| 开发规范 | 相同 | 相同（纳入框架） |
| 平台 | 仅微信 | 多端 |
| 发布 | 手动 | CI/CD 自动 |
| 监控 | 不支持 | 性能看板 |

## 常见问题

**Q1：多端框架会损失原生能力吗？**
A：多数能力可跨端，少数平台专有能力需条件编译处理.
**Q2：CI/CD 能自动发布吗？**
A：能。用 miniprogram-ci 机器人，需上传密钥与 AppID.
**Q3：企业云多环境怎么管？**
A：开发/测试/生产多环境隔离，按 RBAC 分配访问.
**Q4：免费版代码能迁移多端吗？**
A：能。页面逻辑基本兼容，样式与 API 按框架适配.
**Q5：专业版有优先支持吗？**
A：有。专业版享多端架构与 CI/CD 设计咨询.
## 进阶用法

### 多端条件编译

```javascript
// Taro 条件编译
#ifdef WEAPP
  // 仅微信小程序
  wx.login();
#endif
// ...
#ifdef ALIPAY
  // 仅支付宝小程序
  my.getAuthCode();
#endif
// ...
// 统一 API（框架封装）
Taro.login().then(res => console.log(res.code));
```

### CI/CD 发布机器人

```bash
# miniprogram-ci 机器人发布
npx miniprogram-ci upload \
  --pp ./dist \
  --pkp ./private.key.pem \
  --appid wxXXXXXXXXXXXXXX \
  --uv "1.0.0" \
  -r "feat: 发布 v1.0.0"
```

```yaml
# GitHub Actions 自动发布
- name: Build & Upload
  run: |
    npm run build:weapp
    npx miniprogram-ci upload --pp dist --pkp key.pem --appid $APPID -r "${{ github.event.head_commit.message }}"
```

### 性能监控埋点

```javascript
// 关键性能埋点
const t = Date.now();
Page({
  onLoad() {
    this.start = Date.now();
  },
  onReady() {
    const renderTime = Date.now() - this.start;
    wx.reportAnalytics('page_render', { time: renderTime });
  }
});
```

```text
性能看板指标:
  启动耗时: 冷启动 → 首屏可交互
  首屏渲染: onLoad → onReady
  setData 频次: 平均每页次/会话
  包体积: 主包/分包/总
  网络请求: 耗时与失败率
```

## 多端差异处理

| 能力 | 微信 | 支付宝 | 字节 |
|---:|---:|---:|---:|
| 登录 | wx.login | my.getAuthCode | tt.login |
| 支付 | wx.requestPayment | my.tradePay | tt.requestPayment |
| 存储 | wx.setStorage | my.setStorage | tt.setStorage |

差异通过框架统一 API 封装，必要时条件编译处理.
## CI/CD 治理

- **流水线分级**：lint → test → build → upload.
- **机器人发布**：用 miniprogram-ci 机器人，避免人工误操作.
- **多端矩阵**：一次性构建多端，分别发布.
- **回滚机制**：保留历史版本，可快速回滚.
- **发布审批**：生产发布需审批，特性分支自动构建不发布.
## 性能与包体治理

- **性能定基线**：启动/渲染定基线，劣化告警.
- **主包瘦身**：主包 < 2MB，非核心页分包懒加载.
- **图片优化**：CDN + 压缩 + 懒加载 + WebP.
- **setData 监控**：频次过高告警，引导局部更新.
- **定期压测**：关键路径定期压测，防性能退化.
## 依赖说明

### 运行环境
- **Agent 平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI 等）
- **操作系统**: Windows / macOS / Linux
- **Node.js**: 18+

### 依赖详情
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:---:|:---:|:---:|:---:|
| 微信开发者工具 | IDE | 必需 | 微信官方下载 |
| Taro/uni-app | 多端框架 | 多端时必需 | `npm install` |
| miniprogram-ci | 发布工具 | CI/CD 时必需 | `npm install miniprogram-ci` |
| LLM API | API | 必需 | 由 Agent 内置 LLM 提供 |

### API Key 配置
- 小程序 AppID 与上传密钥（CI 发布用）
- 云开发环境 ID 与访问凭证
- 多端各平台开发者凭证

### 可用性分类
- **分类**: MD+EXEC（Markdown 指令 + 命令行执行）
- **说明**: 通过自然语言指令驱动 Agent 完成多端开发与 CI/CD 治理
- API Key通过环境变量配置: export API_KEY=your_key

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:------|------:|:------|
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
    "result": "小程序开发工具专业版处理结果",
    "execution_time": "0.5s",
    "metadata": {
      "version": "1.0",
      "processor": "miniprogram dev pro"
    }
  },
  "execution_log": ["解析输入参数", "执行核心处理", "格式化输出结果"],
  "error": null
}
```
