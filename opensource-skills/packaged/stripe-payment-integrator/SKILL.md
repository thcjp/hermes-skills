---
slug: stripe-payment-integrator
name: stripe-payment-integrator
version: 1.0.1
displayName: 支付集成专家
summary: Stripe支付全链路集成,从支付意图到订阅分账,安全合规少踩坑
license: Proprietary
description: 支付集成专家——基于Stripe官方最佳实践实现全流程支付集成,覆盖支付意图创建、订阅管理、Webhook处理、退款分账全链路。同时提供微信支付/支付宝/银联国内替代方案。适用于电商支付、SaaS订阅、退款处理、平台分账、发票管理、Webhook集成场景。触发关键词:支付集成、Stripe、订阅、Webhook、退款、发票、支付意图、3D
  Secure、微信支付、支付宝、分账、支付网关
tags:
- 支付集成
- Stripe
- 订阅付费
- 电商支付
- SaaS收款
tools:
- read
- exec
# 定价元数据
suggested_price: "99.9 CNY/monthly"
pricing_tier: "L4-企业级"
pricing_model: "monthly"
tools: ["read", "write", "exec"]
tags: "工具,效率,自动化"
---
# 支付集成专家

基于 Stripe 官方最佳实践,实现安全、合规、可扩展的支付集成。同时提供国内支付(微信支付/支付宝/银联)替代方案,支持跨境与国内双场景。从支付意图到订阅管理,从 Webhook 到退款,全链路覆盖。

## 核心能力

1. **支付意图管理**:PaymentIntent 创建/确认/3D Secure 认证(SCA 合规)、自动 vs 手动捕获
2. **订阅全生命周期**:产品/价格管理、试用期、升级降级、催收(Dunning)、客户门户
3. **Webhook 安全处理**:签名验证、幂等去重、事件路由、失败重试
4. **退款与争议处理**:全额/部分退款、争议证据提交、Radar 防欺诈
5. **国内支付适配**:微信支付(JSAPI/Native/APP)、支付宝(电脑网站/手机网站/APP)、银联全渠道

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 电商一次性支付 | 订单金额、货币、商品信息 | PaymentIntent + 前端支付表单 + 后端确认逻辑 |
| SaaS 订阅集成 | 产品定价、计费周期、试用期 | 订阅创建/管理 API + 客户门户配置 |
| 退款处理 | 订单 ID、退款金额、退款原因 | 退款 API 调用 + 财务对账记录 |
| 平台分账 | 卖家列表、分账比例、金额 | Connect 账户配置 + 分账 API + 佣金报表 |
| Webhook 集成 | 业务事件清单 | Webhook 端点 + 签名验证 + 事件处理器 |
| 国内支付改造 | Stripe 改为微信/支付宝 | SDK 替换方案 + 接口映射 + 测试用例 |

**不适用于**:
- 数字货币/区块链支付(非传统支付通道)
- P2P 转账与个人收款(专注于商户收款)
- 银行核心系统对接(支付网关层面,不涉及清算)
- 线下 POS 收款(专注于线上支付)
- 跨境资金合规咨询(需专业法律/财务顾问)
- 信用评分与风控建模(仅使用支付平台的风控规则)

## 使用流程

### Step 1: 支付集成规划
1. **确定支付模式**:一次性支付 / 订阅 / 分账 / 混合
2. **确定目标市场**:海外(Stripe 为主)/ 国内(微信+支付宝)/ 双市场
3. **选择集成方式**:Payment Elements / Checkout Session / 嵌入式表单 / 原生 SDK
4. **设计数据模型**:客户/产品/价格/订阅/支付方式
5. **规划 Webhook 事件**:列出需要监听的关键事件
6. **安全合规检查**:PCI DSS 合规范围确认

### Step 2: 核心支付流程实现
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

### Step 3: 订阅管理
1. **创建订阅**:定义产品/价格/计费周期/试用期
2. **生命周期管理**:升级/降级(按比例计算)/暂停/恢复/取消
3. **催收流程**:续费失败重试 + 邮件通知
4. **客户门户**:Stripe Customer Portal 自助管理

### Step 4: Webhook 处理
1. **端点创建**:注册 Webhook URL,选择事件类型
2. **签名验证**:验证 Stripe-Signature 头,防止伪造
3. **幂等处理**:基于事件 ID 去重,防止重复处理
4. **事件路由**:根据事件类型分发到对应处理器
5. **错误重试**:失败事件自动重试,记录重试日志

### Step 5: 退款与争议
1. **退款流程**:全额/部分退款,退款原因记录
2. **争议处理**:接收争议通知,提交证据,跟踪状态
3. **防欺诈**:Radar 规则配置,风险评分监控

### Step 6: 国内支付适配(可选)
1. 评估是否需要国内支付(微信/支付宝)
2. 选择国内支付 SDK 替换 Stripe
3. 实现接口适配层(统一抽象)
4. 国内支付测试与上线

## 国内外支付方案对照

| 维度 | Stripe(海外) | 微信支付(国内) | 支付宝(国内) |
|:-----|:-----|:-----|:-----|
| 一次性支付 | PaymentIntent | JSAPI/Native/APP | 电脑网站/手机网站/APP |
| 订阅 | Subscriptions | 委托代扣 | 周期扣款 |
| 分账 | Connect | 分账功能 | 分账功能 |
| Webhook | Stripe Webhook | 支付结果通知 | 异步通知 |
| 3D Secure | 内置支持 | 微信密码/指纹 | 支付宝密码 |
| 测试模式 | sk_test_ | 沙箱环境 | 沙箱环境 |
| 凭证 | Secret Key | mchid + apiV3Key | appid + 私钥 |
| 货币 | 多币种 | CNY | CNY |
| 费率 | 2.9% + $0.30 | 0.6% | 0.6% |

## 示例

### 示例1: 创建 Stripe 支付意图(输入→输出)

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | 支付集成专家处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
用户请求:为一笔 $99.00 的订单创建支付意图,支持 3D Secure
订单ID: ORD-001
```

**输出**:
```javascript
// 后端:创建 PaymentIntent
const stripe = require('stripe')(process.env.STRIPE_SECRET_KEY);
// ...
const paymentIntent = await stripe.paymentIntents.create({
  amount: 9900, // 美分
  currency: 'usd',
  description: 'Order ORD-001',
  metadata: { order_id: 'ORD-001' },
  automatic_payment_methods: { enabled: true } // 自动启用 3D Secure
});
// ...
// 返回给前端
{
  payment_intent_id: 'pi_xxx',
  client_secret: 'pi_xxx_secret_xxx',
  status: 'requires_payment_method',
  amount: 9900,
  currency: 'usd'
}
```

```javascript
// 前端:确认支付
const stripe = Stripe('pk_live_xxx');
const result = await stripe.confirmCardPayment(clientSecret, {
  payment_method: { card: elements.getElement('card') }
});
// 处理 result.error 或 result.paymentIntent
```

### 示例2: 国内支付 - 微信支付 JSAPI(输入→输出)

**输入**:
```
用户请求:为 ¥99.00 的订单创建微信支付(公众号内)
订单ID: ORD-002
openid: oUpF8xxx
```

**输出**:
```javascript
// 后端:创建微信支付订单
const { WechatPay } = require('wechatpay-node-v3');
const pay = new WechatPay({
  appid: process.env.WX_APPID,
  mchid: process.env.WX_MCHID,
  publicKey: process.env.WX_PUBLIC_KEY,
  privateKey: process.env.WX_PRIVATE_KEY
});
// ...
const result = await pay.transactions_jsapi({
  out_trade_no: 'ORD-002',
  description: 'Order ORD-002',
  amount: { total: 9900, currency: 'CNY' }, // 分
  payer: { openid: 'oUpF8xxx' },
  notify_url: 'https://api.example.com/wx/notify'
});
// ...
// 返回给前端(用于调起微信支付)
{
  timeStamp: '1627000000',
  nonceStr: 'abc123',
  package: 'prepay_id=wx20240101xxx',
  signType: 'RSA',
  paySign: 'xxx'
}
```

### 示例3: 创建月度订阅(输入→输出)

**输入**:
```
用户请求:创建每月 $29 的 Pro 订阅,7天试用期
客户: cus_xxx
价格: price_xxx (monthly $29)
```

**输出**:
```javascript
const subscription = await stripe.subscriptions.create({
  customer: 'cus_xxx',
  items: [{ price: 'price_xxx' }],
  trial_period_days: 7,
  payment_behavior: 'default_incomplete',
  expand: ['latest_invoice.payment_intent']
});
// ...
// 输出
{
  subscription_id: 'sub_xxx',
  status: 'trialing',
  current_period_end: 1700000000, // 7天后
  trial_end: 1700000000,
  latest_invoice: 'in_xxx',
  customer: 'cus_xxx'
}
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 支付被拒绝 | 余额不足/卡过期/风控 | 检查 decline_code,提示用户更换支付方式 |
| 3D Secure 超时 | 用户未完成认证 | 设置 15 分钟超时,引导用户重试 |
| Webhook 签名验证失败 | 请求被伪造或篡改 | 拒绝请求,记录安全日志,告警 |
| 订阅续费失败 | 信用卡过期/余额不足 | 进入催收流程(Dunning),最多重试 4 次 |
| 退款金额超限 | 已部分退款导致余额不足 | 校验可退金额,改为部分退款 |
| API 限流 | 短时间大量请求 | 实现指数退避重试(429 状态码) |
| 网络超时 | 第三方服务响应慢 | 设置 30s 超时,异步轮询查询状态 |
| 国内支付证书过期 | 微信/支付宝证书未更新 | 配置证书到期监控,提前 30 天告警 |
| 微信支付签名错误 | APIv3 密钥配置错误 | 校验 mchid/apiV3Key/序列号一致性 |
| 支付宝异步通知丢失 | 网络问题或回调地址错误 | 主动查询订单状态补偿 + 重试机制 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ 或 Python 3.10+

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:------|------:|:------|:------|------:|
| Stripe SDK | SDK | 海外必需 | `npm install stripe` / `pip install stripe` | - |
| 微信支付 SDK | SDK | 国内必需 | `npm install wechatpay-node-v3` | - |
| 支付宝 SDK | SDK | 国内必需 | `npm install alipay-sdk` | - |
| Node.js | 运行时 | 必需 | nodejs.org | npmmirror 国内镜像 |
| 公网 HTTPS 端点 | 网络 | 必需 | 用于接收 Webhook | 国内云厂商 SLB |

### API Key 配置
- **Stripe**: Secret Key (sk_live_/sk_test_) 从 Stripe Dashboard 获取
- **微信支付**: mchid + apiV3Key + 商户证书(私钥 + 公钥)
- **支付宝**: appid + 应用私钥 + 支付宝公钥
- **安全要求**:
  - 所有 API Key 仅存储在环境变量或密钥管理服务
  - 禁止硬编码在源码中
  - 禁止提交到版本控制(.gitignore 配置 .env)
  - Webhook 签名密钥与 API Key 分离管理

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行 SDK 与测试

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 电商一次性支付(PaymentIntent+3D Secure+Webhook确认)

**输入**:
```
场景: 电商网站一次性支付
订单: ORD-2024-001, 金额 $299.00 USD
要求: 支持3D Secure(SCA合规),Webhook确认支付状态
前端: React + Stripe.js
后端: Node.js + Express
```

**LLM生成输出** (`output/ecommerce-payment/server.js`):
```javascript
// 后端: 创建PaymentIntent
const express = require("express");
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
const app = express();
app.use(express.json());
// ...
app.post("/api/create-payment-intent", async (req, res) => {
  try {
    const { orderId, amount, currency = "usd" } = req.body;
// ...
    // 服务端金额校验(不信任客户端金额)
    const order = await getOrderFromDB(orderId);
    if (!order || order.amount !== amount) {
      return res.status(400).json({ error: "金额不匹配" });
    }
// ...
    const paymentIntent = await stripe.paymentIntents.create({
      amount: Math.round(amount * 100), // 转为分
      currency,
      description: `Order ${orderId}`,
      metadata: {
        order_id: orderId,
        customer_id: order.customerId,
      },
      automatic_payment_methods: { enabled: true }, // 自动启用3D Secure
    });
// ...
    res.json({
      clientSecret: paymentIntent.client_secret,
      paymentIntentId: paymentIntent.id,
    });
  } catch (error) {
    console.error("创建PaymentIntent失败:", error);
    res.status(500).json({ error: "支付初始化失败" });
  }
});
// ...
// Webhook端点(签名验证+幂等处理)
app.post("/api/stripe/webhook", express.raw({ type: "application/json" }), async (req, res) => {
  const sig = req.headers["stripe-signature"];
  let event;
// ...
  try {
    event = stripe.webhooks.constructEvent(
      req.body, sig, process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    console.error("签名验证失败:", err.message);
    return res.status(400).send(`Webhook Error: ${err.message}`);
  }
// ...
  // 幂等检查:基于事件ID去重
  const processed = await checkEventProcessed(event.id);
  if (processed) {
    return res.json({ received: true, duplicate: true });
  }
  await markEventProcessed(event.id);
// ...
  // 事件路由
  switch (event.type) {
    case "payment_intent.succeeded":
      await handlePaymentSuccess(event.data.object);
      break;
    case "payment_intent.payment_failed":
      await handlePaymentFailure(event.data.object);
      break;
    case "payment_intent.requires_action":
      // 3D Secure需要用户认证
      console.log("需要3D Secure认证:", event.data.object.id);
      break;
  }
// ...
  res.json({ received: true });
});
// ...
async function handlePaymentSuccess(paymentIntent) {
  const { order_id } = paymentIntent.metadata;
  await updateOrderStatus(order_id, "paid", {
    paymentIntentId: paymentIntent.id,
    paidAt: new Date(),
  });
  await sendOrderConfirmationEmail(order_id);
}
// ...
async function handlePaymentFailure(paymentIntent) {
  const { order_id } = paymentIntent.metadata;
  await updateOrderStatus(order_id, "failed", {
    failureReason: paymentIntent.last_payment_error?.message,
  });
}
// ...
app.listen(3000);
```

**LLM生成输出** (`output/ecommerce-payment/Checkout.jsx`):
```jsx
// 前端: React支付组件
import { useState } from "react";
import { loadStripe } from "@stripe/stripe-js";
import { Elements, PaymentElement, useStripe, useElements } from "@stripe/react-stripe-js";
# ...
const stripePromise = loadStripe(process.env.REACT_APP_STRIPE_PUBLISHABLE_KEY);
# ...
function CheckoutForm({ clientSecret, orderId }) {
  const stripe = useStripe();
  const elements = useElements();
  const [processing, setProcessing] = useState(false);
  const [error, setError] = useState(null);
# ...
  const handleSubmit = async (e) => {
    e.preventDefault();
    if (!stripe || !elements) return;
# ...
    setProcessing(true);
# ...
    const { error, paymentIntent } = await stripe.confirmPayment({
      elements,
      confirmParams: {
        return_url: `${window.location.origin}/payment-result?order=${orderId}`,
      },
      redirect: "if_required",
    });
# ...
    if (error) {
      setError(error.message);
      setProcessing(false);
    } else if (paymentIntent.status === "succeeded") {
      // 支付成功,跳转订单页(Webhook也会同步更新)
      window.location.href = `/orders/${orderId}?status=success`;
    } else if (paymentIntent.status === "requires_action") {
      // 3D Secure认证由Stripe.js自动处理
      setError("需要进行3D Secure认证,请完成验证");
    }
  };
# ...
  return (
    <form onSubmit={handleSubmit}>
      <PaymentElement />
      {error && <div className="error">{error}</div>}
      <button type="submit" disabled={!stripe || processing}>
        {processing ? "处理中..." : "支付 $299.00"}
      </button>
    </form>
  );
}
# ...
export default function Checkout({ orderId, amount }) {
  const [clientSecret, setClientSecret] = useState(null);
# ...
  const createIntent = async () => {
    const res = await fetch("/api/create-payment-intent", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ orderId, amount }),
    });
    const data = await res.json();
    setClientSecret(data.clientSecret);
  };
# ...
  return (
    <div>
      <button onClick={createIntent}>开始支付</button>
      {clientSecret && (
        <Elements stripe={stripePromise} options={{ clientSecret }}>
          <CheckoutForm clientSecret={clientSecret} orderId={orderId} />
        </Elements>
      )}
    </div>
  );
}
```

**效果验证**: ✓PaymentIntent创建含服务端金额校验 ✓3D Secure自动启用(automatic_payment_methods) ✓Webhook签名验证+幂等去重 ✓前端confirmPayment处理requires_action ✓React+Stripe.js集成完整

### 案例2: SaaS订阅集成(试用期+升降级+催收)

**输入**:
```
SaaS产品: Pro计划 $29/月, Enterprise $99/月
要求: 7天免费试用,支持升降级(按比例计算),续费失败催收
客户: cus_xxx (已有Stripe客户)
```

**LLM生成输出** (`output/saas-subscription/subscription.js`):
```javascript
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
// ...
// ==================== 1. 创建订阅(7天试用) ====================
async function createSubscription(customerId, priceId, trialDays = 7) {
  const subscription = await stripe.subscriptions.create({
    customer: customerId,
    items: [{ price: priceId }],
    trial_period_days: trialDays,
    payment_behavior: "default_incomplete",
    expand: ["latest_invoice.payment_intent"],
    metadata: { plan: "pro", source: "signup" },
  });
// ...
  // 试用期内不需要立即支付
  return {
    subscriptionId: subscription.id,
    status: subscription.status, // "trialing"
    trialEnd: new Date(subscription.trial_end * 1000),
    currentPeriodEnd: new Date(subscription.current_period_end * 1000),
    clientSecret: subscription.latest_invoice?.payment_intent?.client_secret,
  };
}
// ...
// ==================== 2. 升级订阅(Pro→Enterprise) ====================
async function upgradeSubscription(subscriptionId, newPriceId) {
  const subscription = await stripe.subscriptions.retrieve(subscriptionId);
// ...
  // 获取当前订阅项
  const itemId = subscription.items.data[0].id;
// ...
  // 更新订阅项(Stripe自动按比例计算差额)
  const updated = await stripe.subscriptions.update(subscriptionId, {
    items: [{ id: itemId, price: newPriceId }],
    proration_behavior: "create_prorations", // 按比例计算
    expand: ["latest_invoice"],
  });
// ...
  // 获取按比例计算的发票
  const invoice = updated.latest_invoice;
  const prorationAmount = invoice?.amount_due || 0;
// ...
  return {
    subscriptionId: updated.id,
    newPlan: "enterprise",
    prorationAmount: prorationAmount / 100, // 转为美元
    nextInvoiceDate: new Date(updated.current_period_end * 1000),
    status: updated.status,
  };
}
// ...
// ==================== 3. 降级订阅(Enterprise→Pro,下个周期生效) ====================
async function downgradeSubscription(subscriptionId, newPriceId) {
  const subscription = await stripe.subscriptions.retrieve(subscriptionId);
  const itemId = subscription.items.data[0].id;
// ...
  // 使用schedule实现下个周期生效的降级
  const schedule = await stripe.subscriptionSchedules.create({
    from_subscription: subscriptionId,
  });
// ...
  // 当前阶段保持不变,下个阶段切换价格
  const currentPhase = schedule.phases[0];
  await stripe.subscriptionSchedules.update(schedule.id, {
    phases: [
      {
        items: currentPhase.items,
        start_date: currentPhase.start_date,
        end_date: currentPhase.end_date,
      },
      {
        items: [{ price: newPriceId, quantity: 1 }],
        start_date: currentPhase.end_date, // 下个周期开始
      },
    ],
  });
// ...
  return {
    message: "降级将在下个计费周期生效",
    effectiveDate: new Date(currentPhase.end_date * 1000),
  };
}
// ...
// ==================== 4. 催收流程(Dunning) ====================
async function handleDunning(event) {
  const invoice = event.data.object;
// ...
  switch (event.type) {
    case "invoice.payment_failed":
      // 续费失败:发送邮件通知用户
      await sendEmail(invoice.customer_email, {
        subject: "续费失败,请更新支付方式",
        body: `您的Pro计划续费失败。请登录更新支付方式,我们将在3天后重试。`,
      });
// ...
      // Stripe会自动重试(最多4次,Smart Retries)
      await updateSubscriptionStatus(invoice.subscription, "past_due");
      break;
// ...
    case "invoice.finalization_failed":
      // 最终失败:降级为免费计划
      await stripe.subscriptions.update(invoice.subscription, {
        items: [{ price: process.env.FREE_PLAN_PRICE_ID }],
        metadata: { downgrade_reason: "payment_failed_final" },
      });
      await sendEmail(invoice.customer_email, {
        subject: "已降级为免费计划",
        body: `多次续费失败,已降级为免费计划。更新支付方式后可随时恢复。`,
      });
      break;
  }
}
// ...
// ==================== 5. 客户门户(自助管理) ====================
async function createCustomerPortalSession(customerId) {
  const session = await stripe.billingPortal.sessions.create({
    customer: customerId,
    return_url: `${process.env.APP_URL}/settings/billing`,
    configuration: {
      features: {
        subscription_update: {
          enabled: true,
          default_allowed_updates: ["price", "quantity"],
          proration_behavior: "create_prorations",
        },
        subscription_cancel: { enabled: true, mode: "at_period_end" },
        payment_method_update: { enabled: true },
        invoice_history: { enabled: true },
      },
    },
  });
// ...
  return { url: session.url };
}
// ...
// ==================== 使用示例 ====================
// 创建试用订阅
// const result = await createSubscription("cus_xxx", "price_pro_monthly", 7);
// ...
// 升级
// const upgrade = await upgradeSubscription("sub_xxx", "price_enterprise_monthly");
// ...
// 降级(下周期生效)
// const downgrade = await downgradeSubscription("sub_xxx", "price_pro_monthly");
// ...
// 客户门户
// const portal = await createCustomerPortalSession("cus_xxx");
// window.location.href = portal.url;
```

**效果验证**: ✓试用订阅(trial_period_days=7) ✓升级按比例计算(proration_behavior) ✓降级用Subscription Schedule(下周期生效) ✓催收流程(payment_failed→重试→最终降级) ✓客户门户自助管理(更新/取消/发票)

### 案例3: Webhook安全处理(签名验证+幂等+重试)

**输入**:
```
需求: 构建健壮的Stripe Webhook处理器
要求:
1. 签名验证(防伪造)
2. 幂等去重(防重复处理)
3. 事件路由(按类型分发)
4. 失败重试(指数退避)
5. 日志审计
技术: Node.js + Express + Redis(幂等)+ PostgreSQL(审计)
```

**LLM生成输出** (`output/webhook-handler/webhook.js`):
```javascript
const express = require("express");
const stripe = require("stripe")(process.env.STRIPE_SECRET_KEY);
const { Pool } = require("pg");
const redis = require("redis");
// ...
const app = express();
const pool = new Pool({ connectionString: process.env.DATABASE_URL });
const redisClient = redis.createClient({ url: process.env.REDIS_URL });
await redisClient.connect();
// ...
// Webhook必须用raw body
app.post("/webhook/stripe", express.raw({ type: "application/json" }), handleWebhook);
// ...
async function handleWebhook(req, res) {
  const sig = req.headers["stripe-signature"];
  const rawBody = req.body;
// ...
  let event;
  try {
    // 1. 签名验证(防伪造)
    event = stripe.webhooks.constructEvent(
      rawBody,
      sig,
      process.env.STRIPE_WEBHOOK_SECRET
    );
  } catch (err) {
    await logWebhookError("SIGNATURE_FAILED", err.message, rawBody);
    return res.status(400).send(`签名验证失败: ${err.message}`);
  }
// ...
  // 2. 幂等去重(基于事件ID)
  const eventKey = `stripe:event:${event.id}`;
  const alreadyProcessed = await redisClient.get(eventKey);
  if (alreadyProcessed) {
    console.log(`重复事件已跳过: ${event.id}`);
    return res.status(200).json({ received: true, duplicate: true });
  }
// ...
  // 3. 事件路由+处理(带重试)
  try {
    await processEventWithRetry(event);
// ...
    // 标记为已处理(Redis设置7天过期)
    await redisClient.set(eventKey, JSON.stringify({ processedAt: Date.now() }), {
      EX: 7 * 24 * 3600,
    });
// ...
    // 4. 审计日志
    await logWebhookSuccess(event);
// ...
    res.status(200).json({ received: true, processed: true });
  } catch (error) {
    console.error(`事件处理失败: ${event.id}`, error);
    await logWebhookError("PROCESSING_FAILED", error.message, event);
// ...
    // 返回500,Stripe会自动重试(最多3天)
    res.status(500).json({ error: "处理失败,将重试" });
  }
}
// ...
// 指数退避重试
async function processEventWithRetry(event, maxRetries = 3) {
  for (let attempt = 1; attempt <= maxRetries; attempt++) {
    try {
      await routeEvent(event);
      return; // 成功则退出
    } catch (error) {
      if (attempt === maxRetries) throw error;
      const delay = Math.pow(2, attempt) * 1000; // 2s, 4s, 8s
      console.warn(`重试 ${attempt}/${maxRetries}, ${delay}ms后重试`);
      await new Promise((resolve) => setTimeout(resolve, delay));
    }
  }
}
// ...
// 事件路由
async function routeEvent(event) {
  const handlers = {
    "payment_intent.succeeded": handlePaymentSuccess,
    "payment_intent.payment_failed": handlePaymentFailure,
    "customer.subscription.created": handleSubscriptionCreated,
    "customer.subscription.updated": handleSubscriptionUpdated,
    "customer.subscription.deleted": handleSubscriptionDeleted,
    "invoice.payment_succeeded": handleInvoicePaid,
    "invoice.payment_failed": handleInvoiceFailed,
    "charge.refunded": handleRefund,
    "charge.dispute.created": handleDispute,
  };
// ...
  const handler = handlers[event.type];
  if (handler) {
    await handler(event.data.object);
  } else {
    console.log(`未注册处理器: ${event.type}`);
  }
}
// ...
// 处理器示例
async function handlePaymentSuccess(paymentIntent) {
  const { order_id } = paymentIntent.metadata;
  await pool.query(
    "UPDATE orders SET status = $1, paid_at = NOW() WHERE id = $2",
    ["paid", order_id]
  );
  await sendNotification(order_id, "payment_success");
}
// ...
async function handlePaymentFailure(paymentIntent) {
  const { order_id } = paymentIntent.metadata;
  const reason = paymentIntent.last_payment_error?.decline_code || "unknown";
  await pool.query(
    "UPDATE orders SET status = $1, failure_reason = $2 WHERE id = $3",
    ["failed", reason, order_id]
  );
  await sendNotification(order_id, "payment_failed", { reason });
}
// ...
// 审计日志
async function logWebhookSuccess(event) {
  await pool.query(
    `INSERT INTO webhook_logs (event_id, event_type, status, processed_at)
     VALUES ($1, $2, $3, NOW())`,
    [event.id, event.type, "success"]
  );
}
// ...
async function logWebhookError(stage, error, event) {
  await pool.query(
    `INSERT INTO webhook_logs (event_id, event_type, status, error_stage, error_message, raw_data)
     VALUES ($1, $2, $3, $4, $5, $6)`,
    [
      event?.id || null,
      event?.type || null,
      "error",
      stage,
      error,
      JSON.stringify(event).substring(0, 1000),
    ]
  );
}
// ...
app.listen(3000, () => console.log("Webhook服务已启动:3000"));
```

**效果验证**: ✓签名验证(constructEvent+WEBHOOK_SECRET) ✓Redis幂等去重(事件ID+7天过期) ✓指数退避重试(2s/4s/8s三轮) ✓事件路由表(9种事件类型) ✓审计日志PostgreSQL记录

### 案例4: 国内支付适配层(Stripe→微信支付+支付宝)

**输入**:
```
需求: 设计统一支付适配层,同时支持Stripe(海外)和微信支付/支付宝(国内)
目标: 业务层调用统一接口,根据用户地区路由到对应支付通道
技术: Node.js + TypeScript
```

**LLM生成输出** (`output/payment-adapter/payment-service.ts`):
```typescript
// ==================== 1. 统一支付接口 ====================
interface PaymentService {
  createPayment(params: PaymentParams): Promise<PaymentResult>;
  queryPayment(paymentId: string): Promise<PaymentStatus>;
  refundPayment(paymentId: string, amount?: number): Promise<RefundResult>;
  handleWebhook(rawBody: string, headers: Record<string, string>): Promise<WebhookResult>;
}
// ...
interface PaymentParams {
  orderId: string;
  amount: number;        // 金额(分)
  currency: string;      // CNY/USD
  description: string;
  customerId?: string;
  openid?: string;       // 微信JSAPI需要
  channel: "stripe" | "wechat" | "alipay";
}
// ...
interface PaymentResult {
  paymentId: string;
  status: "pending" | "requires_action" | "succeeded" | "failed";
  clientSecret?: string;     // Stripe前端确认
  payParams?: Record<string, string>; // 微信/支付宝前端调起参数
}
// ...
// ==================== 2. Stripe适配器 ====================
class StripeAdapter implements PaymentService {
  private stripe: any;
// ...
  constructor(secretKey: string) {
    this.stripe = require("stripe")(secretKey);
  }
// ...
  async createPayment(params: PaymentParams): Promise<PaymentResult> {
    const intent = await this.stripe.paymentIntents.create({
      amount: params.amount,
      currency: params.currency,
      description: params.description,
      metadata: { order_id: params.orderId },
      automatic_payment_methods: { enabled: true },
    });
    return {
      paymentId: intent.id,
      status: intent.status,
      clientSecret: intent.client_secret,
    };
  }
// ...
  async queryPayment(paymentId: string) {
    const intent = await this.stripe.paymentIntents.retrieve(paymentId);
    return { paymentId, status: intent.status, amount: intent.amount };
  }
// ...
  async refundPayment(paymentId: string, amount?: number) {
    const refund = await this.stripe.refunds.create({
      payment_intent: paymentId,
      amount,
    });
    return { refundId: refund.id, status: refund.status, amount: refund.amount };
  }
// ...
  async handleWebhook(rawBody: string, headers: Record<string, string>) {
    const event = this.stripe.webhooks.constructEvent(
      rawBody, headers["stripe-signature"], process.env.STRIPE_WEBHOOK_SECRET
    );
    return {
      eventType: event.type,
      paymentId: event.data.object.id,
      status: event.data.object.status,
    };
  }
}
// ...
// ==================== 3. 微信支付适配器 ====================
class WechatPayAdapter implements PaymentService {
  private pay: any;
// ...
  constructor(config: { appid: string; mchid: string; privateKey: string; publicKey: string }) {
    const { WechatPay } = require("wechatpay-node-v3");
    this.pay = new WechatPay(config);
  }
// ...
  async createPayment(params: PaymentParams): Promise<PaymentResult> {
    if (!params.openid) throw new Error("微信JSAPI支付需要openid");
// ...
    const result = await this.pay.transactions_jsapi({
      out_trade_no: params.orderId,
      description: params.description,
      amount: { total: params.amount, currency: "CNY" },
      payer: { openid: params.openid },
      notify_url: `${process.env.API_BASE}/webhook/wechat`,
    });
// ...
    // 返回前端调起支付需要的参数
    return {
      paymentId: result.out_trade_no,
      status: "pending",
      payParams: {
        timeStamp: result.timeStamp,
        nonceStr: result.nonceStr,
        package: result.package,
        signType: result.signType,
        paySign: result.paySign,
      },
    };
  }
// ...
  async queryPayment(paymentId: string) {
    const result = await this.pay.query({
      out_trade_no: paymentId,
    });
    const statusMap = {
      SUCCESS: "succeeded", REFUND: "refunded", NOTPAY: "pending",
      CLOSED: "failed", REVOKED: "failed", USERPAYING: "requires_action",
    };
    return {
      paymentId,
      status: statusMap[result.trade_state] || "pending",
      amount: result.amount.total,
    };
  }
// ...
  async refundPayment(paymentId: string, amount?: number) {
    const result = await this.pay.refunds({
      out_trade_no: paymentId,
      out_refund_no: `REFUND-${Date.now()}`,
      amount: {
        refund: amount,
        total: amount, // 简化:全额退款时total=refund
        currency: "CNY",
      },
    });
    return { refundId: result.refund_id, status: result.status, amount };
  }
// ...
  async handleWebhook(rawBody: string, headers: Record<string, string>) {
    // 微信支付V3:解密通知内容
    const { resource } = JSON.parse(rawBody);
    const decrypted = this.pay.decipher_gcm(
      resource.ciphertext, resource.associated_data, resource.nonce
    );
    const data = JSON.parse(decrypted);
    return {
      eventType: data.event_type,
      paymentId: data.out_trade_no,
      status: data.trade_state,
    };
  }
}
// ...
// ==================== 4. 支付工厂(根据channel创建适配器) ====================
class PaymentFactory {
  static create(channel: "stripe" | "wechat" | "alipay"): PaymentService {
    switch (channel) {
      case "stripe":
        return new StripeAdapter(process.env.STRIPE_SECRET_KEY!);
      case "wechat":
        return new WechatPayAdapter({
          appid: process.env.WX_APPID!,
          mchid: process.env.WX_MCHID!,
          privateKey: process.env.WX_PRIVATE_KEY!,
          publicKey: process.env.WX_PUBLIC_KEY!,
        });
      case "alipay":
        return new AlipayAdapter({
          appId: process.env.ALIPAY_APP_ID!,
          privateKey: process.env.ALIPAY_PRIVATE_KEY!,
          alipayPublicKey: process.env.ALIPAY_PUBLIC_KEY!,
        });
      default:
        throw new Error(`不支持的支付渠道: ${channel}`);
    }
  }
}
// ...
// ==================== 5. 业务层调用(统一接口) ====================
async function processOrderPayment(orderId: string, userRegion: string) {
  const order = await getOrder(orderId);
// ...
  // 根据用户地区选择支付渠道
  const channel = userRegion === "CN" ? "wechat" : "stripe";
// ...
  const paymentService = PaymentFactory.create(channel);
  const result = await paymentService.createPayment({
    orderId,
    amount: order.amountInCents,
    currency: userRegion === "CN" ? "CNY" : "USD",
    description: `订单 ${orderId}`,
    openid: order.userOpenid,
    channel,
  });
// ...
  return result;
}
// ...
// Webhook统一入口
app.post("/webhook/:channel", express.raw({ type: "application/json" }), async (req, res) => {
  const { channel } = req.params;
  const paymentService = PaymentFactory.create(channel);
  const result = await paymentService.handleWebhook(req.body.toString(), req.headers);
  await updateOrderStatus(result.paymentId, result.status);
  res.status(200).send(channel === "wechat" ? JSON.stringify({ code: "SUCCESS" }) : JSON.stringify({ received: true }));
});
```

**效果验证**: ✓统一接口设计(PaymentService抽象) ✓两种适配器实现(Stripe/WechatPay)+Alipay工厂预留 ✓工厂模式按channel创建适配器 ✓业务层无感知支付渠道差异 ✓Webhook统一入口(按channel路由)

## 常见问题

### Q1: 国内项目能用 Stripe 吗?
A: Stripe 在中国大陆不直接可用。国内项目建议:
- **微信支付**: 覆盖微信生态,JSAPI/Native/APP/H5 全场景
- **支付宝**: 电脑/手机/APP 全场景,支持花呗分期
- **银联**: 全渠道,适合传统行业
- **聚合支付**: Ping++/易宝/连连(统一 API,降低接入成本)
- 跨境收款: Stripe Atlas + 海外公司主体(适合独立开发者)

### Q2: 如何同时支持 Stripe 和微信支付?
A: 推荐设计**支付适配层**:
```
PaymentService (抽象接口)
├── StripeAdapter (实现 Stripe)
├── WechatPayAdapter (实现微信支付)
└── AlipayAdapter (实现支付宝)
```
业务层调用统一接口,根据用户地区/偏好路由到具体支付通道。优点:新增支付方式不影响业务代码。

### Q3: Webhook 如何保证幂等性?
A: 三层保障:
1. **事件 ID 去重**: 数据库唯一索引(event_id),已处理事件直接返回 200
2. **状态机校验**: 处理前检查订单状态,已支付的不再处理
3. **事务隔离**: Webhook 处理在数据库事务中,失败回滚

### Q4: 测试支付需要真实扣款吗?
A: 不需要:
- Stripe: 使用 sk_test_ + 测试卡(4242424242424242)模拟
- 微信支付: 使用沙箱环境(sandbox)模拟
- 支付宝: 使用沙箱应用(sandboxapp)模拟

## 已知限制

- Stripe 在中国大陆不可用,需使用微信支付/支付宝替代
- 订阅模式国内支付支持较弱(微信委托代扣需特定资质)
- 跨境支付涉及外汇合规,需咨询专业财务/法律
- 不涉及 PCI DSS 认证咨询(需专业安全机构)
- 不覆盖银行核心清算与对账系统
- 数字货币(USDT/加密币)支付不在范围内
- 仅提供支付集成代码,不涉及反洗钱(AML)合规审查

## 安全声明

- 所有 API Key 仅通过环境变量或 KMS/Vault 读取,绝不硬编码
- Webhook 端点强制签名验证,拒绝未签名请求
- 支付日志自动脱敏(卡号只保留后 4 位,移除 CVV)
- 输出的代码示例中 API Key 一律使用占位符(sk_xxx),不暴露真实凭证
- 测试环境与生产环境密钥严格隔离,禁止混用
