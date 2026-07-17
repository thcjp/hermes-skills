---
slug: stripe-payment-integrator
name: stripe-payment-integrator
version: "1.0.0"
displayName: "支付集成专家"
summary: "Stripe支付全链路集成,从支付意图到订阅分账,安全合规少踩坑"
license: MIT
description: |-
  支付集成专家——基于Stripe官方最佳实践实现全流程支付集成,安全合规少踩坑。从支付意图到订阅管理,从Webhook到退款分账,全链路覆盖,让收款这件事变得简单可靠。

  核心能力:
  - 支付意图创建:Payment Intent全流程+3D Secure认证
  - 订阅管理:创建/升级/降级/取消/试用期全生命周期
  - Webhook处理:签名验证/幂等处理/重试机制
  - 退款处理:全额/部分退款+退款策略
  - 平台分账:Connect分账/转账/佣金计算
  - 发票管理:自动发票生成/发送/PDF
  - Apple Pay/Google Pay:移动支付一键集成

  适用场景:
  - SaaS创业者订阅收费:定期订阅+试用期+升降级全流程
  - 电商卖家在线收款:支付意图+3D Secure+退款处理
  - 一人公司平台分账:多方分成/Connect转账/佣金
  - 副业达人知识付费:一次性支付+发票自动生成

  差异化:不是Stripe API文档翻译,而是基于官方最佳实践的支付集成专家,Webhook签名验证+幂等处理+安全合规,让没有支付经验的开发者也能安全收款。

  触发关键词:支付集成、Stripe、订阅、Webhook、退款、发票、支付意图、3D Secure、Apple Pay、Google Pay、分账、支付网关
tags: [支付集成, Stripe, 订阅付费, 电商支付, SaaS收款]
tools: [read, exec]
---

# 支付集成专家

基于 Stripe 官方最佳实践,实现安全、合规、可扩展的支付集成。从支付意图到订阅管理,从 Webhook 到退款,全链路覆盖。

## 使用场景

| 场景 | 触发条件 | 说明 |
|:-----|:---------|:-----|
| 电商支付 | 需要在线收款 | 支付意图创建 + 确认 + 3D Secure |
| SaaS 订阅 | 需要定期收费 | 订阅创建/升级/降级/取消/试用期 |
| 退款处理 | 需要退款 | 全额/部分退款,退款策略 |
| 平台分账 | 多方分成 | Connect 分账/转账/佣金 |
| 发票管理 | 需要开票 | 自动发票生成/发送/PDF |
| Webhook 处理 | 支付事件通知 | 签名验证/幂等处理/重试 |

## 工作流

### 1. 支付集成规划

1. **确定支付模式**:一次性支付 / 订阅 / 分账 / 混合
2. **选择集成方式**:Payment Elements / Checkout Session / 嵌入式表单
3. **设计数据模型**:客户/产品/价格/订阅/支付方式
4. **规划 Webhook 事件**:需要监听的关键事件清单
5. **安全合规检查**:PCI DSS 合规范围确认

### 2. 核心支付流程

1. **创建支付意图(PaymentIntent)**
   - 设置金额、货币、描述
   - 配置自动捕获 vs 手动捕获
   - 添加 metadata 关联业务数据
   - 启用 3D Secure 认证(SCA 合规)
2. **前端收集支付信息**
   - 使用 Stripe.js / Payment Elements
   - 绝不将卡号传到自有服务器
   - 处理支付确认回调
3. **后端确认支付**
   - 服务端确认 PaymentIntent
   - 处理 requires_action 状态(3D Secure)
   - 处理支付成功/失败/待定

### 3. 订阅管理

1. **创建订阅**
   - 定义产品(Products)和价格(Prices)
   - 设置计费周期(月/年)
   - 配置试用期
   - 添加优惠券/折扣
2. **订阅生命周期**
   - 升级/降级计划(按比例计算)
   - 暂停/恢复订阅
   - 取消订阅(立即/周期末)
   - 处理续费失败与催收
3. **客户门户**
   - 启用 Stripe Customer Portal
   - 客户自助管理订阅/支付方式/发票

### 4. Webhook 处理

1. **端点创建**:注册 Webhook URL,选择事件类型
2. **签名验证**:验证 Stripe-Signature 头,防止伪造
3. **幂等处理**:基于事件 ID 去重,防止重复处理
4. **事件路由**:根据事件类型分发到对应处理器
5. **错误重试**:失败事件自动重试,记录重试日志

### 5. 退款与争议

1. **退款流程**:全额/部分退款,退款原因记录
2. **争议处理**:接收争议通知,提交证据,跟踪状态
3. **防欺诈**:Radar 规则配置,风险评分监控

## 依赖说明

| 依赖类型 | 要求 | 说明 |
|:---------|:-----|:-----|
| LLM | 任意支持 Agent Skills 的 LLM | Claude/GPT/Gemini 等 |
| API Key | Stripe Secret Key (sk_live_/sk_test_) | 必须从 Stripe Dashboard 获取 |
| 运行环境 | Node.js 18+ 或 Python 3.10+ | 后端服务运行环境 |
| SDK | stripe (npm/pip) | 官方 SDK |
| Webhook | 公网可访问的 HTTPS 端点 | 用于接收 Stripe 事件通知 |
| 测试 | Stripe 测试模式 API Key | 开发测试用,不产生真实交易 |

## 异常处理

| 异常场景 | 处理方式 |
|:---------|:---------|
| 支付被拒绝 | 检查 decline_code,提示用户更换支付方式 |
| 3D Secure 超时 | 设置超时回退,引导用户重试 |
| Webhook 签名验证失败 | 拒绝请求,记录安全日志 |
| 订阅续费失败 | 进入催收流程(dunning),发送邮件通知 |
| 退款金额超限 | 校验可退金额,部分退款 |
| API 限流 | 实现指数退避重试 |
| 网络超时 | 设置合理超时(30s),异步重试 |

## 示例

### 输入:创建支付意图

```
用户请求:为一笔 $99.00 的订单创建支付意图,支持 3D Secure

输出:
- payment_intent_id: pi_xxx
- client_secret: pi_xxx_secret_xxx
- status: requires_payment_method
- amount: 9900 (cents)
- currency: usd
- payment_method_types: ["card"]
- metadata: { order_id: "ORD-001" }
```

### 输入:创建月度订阅

```
用户请求:创建每月 $29 的 Pro 订阅,7天试用期

输出:
- subscription_id: sub_xxx
- status: trialing
- current_period_end: <7天后>
- trial_end: <7天后>
- latest_invoice: in_xxx
- customer: cus_xxx
```
