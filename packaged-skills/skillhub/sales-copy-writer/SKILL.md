---
slug: sales-copy-writer
name: sales-copy-writer
version: 1.0.1
displayName: "卖货文案手"
summary: "文案干瘪没转化?FAB卖点+6种情绪钩子+4种CTA,一键生成高转化卖货文案。卖货文案手是一款高转化卖货文案生成工具,解决文案干瘪无转化痛点. 基于FAB法则提炼卖点,结合6种情绪钩子与4种"
license: Proprietary
description: |-
  卖货文案手是一款高转化卖货文案生成工具,解决文案干瘪无转化痛点.
  基于FAB法则提炼卖点,结合6种情绪钩子与4种CTA话术,5平台风格自动适配.
  核心能力:
  - FAB法则卖点提炼
  - 6种情绪钩子生成
  - 4种CTA话术注入
  - 5平台风格自动适配
homepage: ""
tags:
  - 卖货文案
  - 营销转化
  - 电商带货
  - 副业工具
  - 工具
  - 效率
  - 自动化
  - 写作
  - 电商
  - 通信
  - 邮件
  - AI代理
  - cta
  - fab
  - topic
  - platform
  - hook_type
tools:
  - read
  - exec
  - write
category: "Automation"
---
# 卖货文案手

解决内容营销中"文案干瘪无转化"的核心痛点,基于FAB法则+情绪钩子+CTA话术生成高转化卖货文案.
## 付费版专享能力

| 能力 | 免费版 | 付费版 |
|---|---|---|
| 基础功能 | 支持 | 支持 |
| 卖货文案手一键生成 | 不支持 | 支持 |
| 高级参数配置与自定义规则 | 不支持 | 支持 |
| 批量任务编排与队列管理 | 不支持 | 支持 |
| 结果导出与多格式转换 | 不支持 | 支持 |
| 实时状态监控与异常告警 | 不支持 | 支持 |

## 核心能力

1. **FAB法则卖点提炼**: Feature(特性)+Advantage(优势)+Benefit(利益)三段式提炼3-5个核心卖点,逻辑清晰有说服力
2. **6种情绪钩子生成**: pain_resonance(痛点共鸣)/curiosity_suspense(好奇悬念)/urgency(紧迫感)/social_proof(社交证明)/contrast(对比反差)/authority(权威背书),按场景智能选择
3. **4种CTA话术注入**: follow(关注)/dm(私信)/order(下单)/group(加群),匹配不同转化目标
4. **5平台风格自动适配**: 小红书活泼种草/抖音口语化/公众号深度种草/微博简洁观点/电商促转化,自动调整字数与风格
5. **活动促销文案**: 结合紧迫感和社交证明,生成限时活动文案

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 新品上市推广 | topic+brand_info+platform | FAB卖点+情绪钩子+平台适配文案+CTA |
| 直播带货预热 | topic+platform=douyin+hook_type=urgency | 抖音口语化文案+紧迫感钩子+下单CTA |
| 电商详情页优化 | topic+platform=ecommerce+cta_type=order | 卖点突出文案+促转化CTA |
| 社交媒体种草 | topic+platform=xiaohongshu+hook_type | 小红书活泼种草文案+私信/关注CTA |

**不适用于**: 品牌长文PR稿件(>2000字)、B2B白皮书/行业报告、纯品牌故事(无产品卖点)、海外平台(Instagram/TikTok国际版)、负面营销/竞品攻击文案.
## 使用流程

1. **环境准备**: 确认Agent支持exec工具,配置 `LLM_API_KEY`(必需,通常由Agent内置),纯LLM驱动无额外API依赖
2. **卖点提炼(FAB法则)**: 接收 `topic`(必填)和 `brand_info`(可选),用LLM提炼3-5个FAB结构化卖点;品牌信息缺失→生成无品牌版本标注warning
3. **情绪钩子生成**: 根据 `hook_type` 选择钩子类型生成框架;钩子类型无效→默认pain_resonance
4. **平台适配+CTA注入**: 根据 `platform` 调整文案风格和字数,根据 `cta_type` 注入对应CTA话术;平台不支持→降级通用文案,CTA无效→默认follow
5. **输出完整文案**: 整合卖点+情绪钩子+平台适配文案+CTA,输出结构化结果

## 输入格式

| 字段 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| topic | string | 是 | 内容主题/产品名称 |
| brand_info | string | 否 | 品牌信息(品牌名+slogan) |
| platform | string | 是 | 目标平台(xiaohongshu/douyin/wechat/weibo/ecommerce) |
| hook_type | string | 否 | 情绪钩子类型,默认pain_resonance |
| cta_type | string | 否 | CTA类型,默认follow |

## 输出格式

输出结构化结果: `selling_points[]`(FAB卖点数组)+`hook`(情绪钩子)+`adapted_content`(平台适配完整文案)+`cta`(CTA话术),外层含 `success`/`error`/`code` 字段.

## 案例展示

### 案例1: 电商详情页护肤品精华液（社交证明+下单CTA）

**输入关键字段**: topic="烟酰胺精华液", platform="ecommerce", hook_type="social_proof", cta_type="order"

**LLM生成输出关键片段**:
- **FAB卖点**: 5%高浓度烟酰胺(业内公认有效美白浓度→28天提亮肤色);玻尿酸+神经酰胺复配(美白同时修护屏障→敏感肌也能用);第三方机构功效检测(93%受试者28天提亮→有数据支撑)
- **情绪钩子**(social_proof): "10万+真实用户回购,小红书精华液排行榜TOP3,93%受试者28天肉眼可见提亮——不是精华液选不起,而是瓷肌研更有性价比。"
- **CTA**(order): "限时活动价89元(原价159元),前500名送同款旅行装,点击立即下单!"

**效果验证**: FAB结构完整 / 卖点有数据支撑 / 社交证明钩子有力 / 电商风格促转化 / CTA紧迫感强

### 案例2: 抖音限时促销健身课（紧迫感+下单CTA）

**输入关键字段**: topic="21天在家健身课", platform="douyin", hook_type="urgency", cta_type="order"

**LLM生成输出关键片段**:
- **FAB卖点**: 每天15分钟(比去健身房省2小时→宝妈上班族都能坚持);AI动作纠错(实时纠正→不用请私教);21天见效(5万+学员验证→腰围平均-3cm)
- **情绪钩子**(urgency): "今晚12点涨价!最后3小时59元,明天恢复199元,夏天都快过完了你还在等什么?"
- **CTA**(order): "左下角小黄车,最后3小时59元,抢到就是赚到!"

**效果验证**: FAB卖点直击痛点 / 紧迫感钩子制造焦虑 / 抖音口语化风格 / CTA下单引导+紧迫感

## 示例代码

### 1. 调用输入（JSON）

生成电商详情页护肤品文案的完整输入参数：

```json
{
  "topic": "烟酰胺精华液",
  "brand_info": "瓷肌研 | 专注成分护肤",
  "platform": "ecommerce",
  "hook_type": "social_proof",
  "cta_type": "order"
}
```

### 2. 结构化输出（JSON）

技能返回FAB卖点、情绪钩子、平台适配文案与CTA话术：

```json
{
  "success": true,
  "code": 0,
  "error": null,
  "data": {
    "selling_points": [
      {
        "feature": "5%高浓度烟酰胺",
        "advantage": "业内公认有效美白浓度",
        "benefit": "28天提亮肤色"
      },
      {
        "feature": "玻尿酸+神经酰胺复配",
        "advantage": "美白同时修护屏障",
        "benefit": "敏感肌也能用"
      },
      {
        "feature": "第三方机构功效检测",
        "advantage": "93%受试者28天提亮",
        "benefit": "有数据支撑更可信"
      }
    ],
    "hook": "10万+真实用户回购，小红书精华液排行榜TOP3，93%受试者28天肉眼可见提亮——不是精华液选不起，而是瓷肌研更有性价比。",
    "adapted_content": "瓷肌研烟酰胺精华液，5%黄金浓度科学提亮。玻尿酸+神经酰胺复配，美白同时修护屏障，敏感肌也能安心用。第三方机构检测，93%受试者28天肉眼可见提亮。",
    "cta": "限时活动价89元(原价159元)，前500名送同款旅行装，点击立即下单！"
  }
}
```

### 3. 多平台批量生成（Python）

对同一产品生成5平台风格文案并按平台分类输出：

```python
import json

def generate_multi_platform(topic, brand_info, hook_type, cta_type):
    """对同一产品生成5平台风格文案矩阵"""
    platforms = ["xiaohongshu", "douyin", "wechat", "weibo", "ecommerce"]
    results = {}
    for platform in platforms:
        payload = {
            "topic": topic,
            "brand_info": brand_info,
            "platform": platform,
            "hook_type": hook_type,
            "cta_type": cta_type,
        }
        # 调用卖货文案手技能（由 Agent LLM 执行）
        output = call_skill("sales-copy-writer", payload)
        results[platform] = {
            "content": output["data"]["adapted_content"],
            "cta": output["data"]["cta"],
            "word_count": len(output["data"]["adapted_content"]),
        }
    return results

# 示例：为新品上市生成全平台文案矩阵
matrix = generate_multi_platform(
    topic="便携式果汁杯",
    brand_info="鲜生活 | 随身榨汁",
    hook_type="urgency",
    cta_type="order",
)
print(json.dumps(matrix, ensure_ascii=False, indent=2))
```

### 4. FAB卖点提炼Prompt模板

LLM执行卖点提炼时的结构化提示模板：

```text
【任务】基于FAB法则提炼产品核心卖点
【产品】{topic}
【品牌】{brand_info}
【平台】{platform}

【输出要求】生成3-5个FAB结构化卖点：
- Feature(特性)：产品客观属性，如成分/规格/工艺
- Advantage(优势)：特性带来的差异化优势
- Benefit(利益)：用户最终获得的可感知利益

【示例】
- Feature: 5%高浓度烟酰胺
- Advantage: 业内公认有效美白浓度
- Benefit: 28天提亮肤色
```

## 异常处理

| 异常场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 主题为空 | 未提供topic参数 | 返回success=false, error="主题不能为空",无法降级 |
| 平台不支持 | platform不在5个支持范围内 | 降级为通用文案模板,标注warning |
| 钩子/CTA类型无效 | hook_type/cta_type不在支持范围 | 默认使用pain_resonance/follow,标注warning |
| LLM调用失败 | LLM服务不可用或超时 | 返回success=false, error="文案生成LLM调用失败" |
| LLM_API_KEY未配置 | 环境变量缺失 | 返回error,提示配置环境变量 |

## 依赖说明

- **运行环境**: Windows/macOS/Linux,需Agent支持exec能力
- **依赖项**: LLM API(必需,由Agent内置,国内可用通义千问/文心一言/智谱GLM/DeepSeek等)
- **API Key配置**: LLM_API_KEY通过环境变量注入,严禁硬编码
- **可用性分类**: MD+EXEC

## 常见问题

### Q1: 如何开始使用?
A: 两步启动:(1)将SKILL.md放入Agent的skills目录;(2)确认环境变量已配置LLM_API_KEY。调用时传入topic(必填)和platform(必填)即可,其他参数可选。纯LLM驱动无额外API依赖.

### Q2: 6种情绪钩子如何选择?
A: 按场景选择:痛点共鸣(通用)/好奇悬念(新品黑科技)/紧迫感(限时促销)/社交证明(成熟产品)/对比反差(性价比突出)/权威背书(专业度高如教育医疗).

### Q3: 5平台风格有什么区别?
A: 小红书活泼种草(emoji丰富,300-500字)、抖音口语化(前3秒强hook,50-100字)、微信公众号深度种草(800-1500字)、微博简洁观点(话题标签,140字内)、电商卖点突出促转化(200-400字)。选择平台后自动调整文案风格和字数.

## 安全

### API Key 零暴露原则
- LLM_API_KEY必须通过Agent环境变量注入,严禁在SKILL.md/配置文件/代码中硬编码
- 本SKILL.md不包含任何真实或示例API Key,所有引用均使用 `$env:LLM_API_KEY` 占位
- exec工具记录日志时自动过滤含"key"/"token"/"secret"字段

### 内容安全
- **广告合规**: 自动过滤虚假宣传/绝对化用语(最/第一/唯一)/医疗承诺
- **平台规范**: 适配各平台广告规范,小红书避免硬广、抖音避免违禁词、电商遵守广告法
- **版权提示**: 文案为原创,引用他人案例/数据需标注来源,商业使用前建议查重

## 已知限制

- **平台覆盖**: 仅支持5个国内平台,不支持Instagram/TikTok国际版/LinkedIn等海外平台
- **字数控制**: LLM生成字数可能偏离建议范围(±15%),需人工微调
- **卖点准确性**: FAB卖点基于LLM理解,可能与产品实际参数有偏差,发布前需人工核对
- **多语言**: 仅支持中文文案生成,不支持英文/其他语种
- **合规限制**: 不生成虚假宣传/绝对化用语/医疗承诺,但平台规则可能更新,发布前建议复核
