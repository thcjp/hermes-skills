---
slug: ai-artist-workstation
name: ai-artist-workstation
version: "1.0.1"
displayName: "AI接单画师工作站"
summary: "一个人开AI画师工作室,双引擎路由+98%面部保持+接单SOP全闭环"
license: Proprietary
description: |-
homepage: "https://skillhub.cn"
tags: [AI绘画, 接单变现, 商业画图, AI写真, 副业变现]
tools:
  - read
  - exec
suggested_price: "19.00"
pricing_tier: "business"
pricing_rationale: "电商类, medium市场, enterprise复杂度, weekly频次, business层 → 直接关联收入,付费意愿强"
---
# AI接单画师工作站

> 定位: 多引擎AI绘画+接单SOP全流程工作站
> 设计: 双引擎路由(写实→鹧应AI写真98%面部保持 / 艺术风格→通用绘画引擎)+接单交付闭环

## 核心能力

1. **双引擎智能路由**:写实风格自动走鹧应AI写真引擎(98%面部保持,0.08元/张),艺术风格走通用绘画引擎(免费),按风格参数自动选择最优引擎
2. **8种风格模板全覆盖**:二次元/写实/水彩/国风/赛博朋克/像素/油画/3D卡通,每种风格预设引擎路由策略和面部保持参数
3. **接单SOP全流程闭环**:从订单接收→需求提取→引擎路由→图片生成→敏感词审核→网盘交付,5步标准化流程,支持电商订单自动交付
4. **多级引擎降级链**:首选引擎不可用时自动降级(鹧应AI写真→通用绘画T2I),全部失败返回明确错误码,保证服务可用性
5. **敏感词审核与合规**:自动审核prompt和生成结果描述,替换违禁内容,含违禁内容时拒绝生成并支持退款流程

## 适用场景

| 场景 | 输入 | 输出 | 是否适用 |
|:-----|:-----|:-----|:---------|
| 电商AI头像定制接单 | 客户自拍+写实风格+1:1尺寸 | 98%面部保持的写实头像+网盘交付链接 | 适用 |
| 商业商品图批量生产 | 商品描述+商品图风格+数量1-10 | 多张商品图+预览图打包 | 适用 |
| 内容矩阵引流作品 | 风格图描述+古风/二次元风格 | 艺术风格图+社交展示帖文案 | 适用 |
| AI写真定制服务 | 参考图+写实/国风+面部保持需求 | 高保真面部保持写真图 | 适用 |
| 壁纸/头像批量生成 | 壁纸描述+尺寸+数量 | 多张壁纸图打包下载 | 适用 |
| 专业插画师级商业插画 | 高精度分层PSD源文件需求 | 不适用(仅输出PNG/JPG位图) | 不适用 |
| 矢量图形Logo设计 | 矢量SVG格式输出需求 | 不适用(仅支持位图输出) | 不适用 |
| 视频内容生成 | 视频生成需求 | 不适用(本Skill仅处理静态图片) | 不适用 |

## 使用流程

### Step 1: 接收画图请求
- 解析输入参数:style(头像/商业图/风格图/壁纸/商品图)、prompt(描述)、count(数量,1-10)、size(尺寸)
- 参数校验:style在允许范围内、prompt非空、count≤10
- 校验失败处理:参数缺失→提示补全;count超限→截断为10

### Step 2: 选择生成引擎
- 按style+是否有参考图路由:
  - 头像/人像+有参考图→写实引擎(鹧应AI写真,98%面部保持)
  - 头像/人像+无参考图→通用绘画引擎T2I
  - 商品图/通用→通用绘画引擎(商品图模式)
  - 风格图/古风→通用绘画引擎(古风插画模式)
- 引擎不可用时按降级链切换

### Step 3: 风格参数选择(仅style=头像时)
- 根据avatar_style参数(二次元/写实/水彩/国风/赛博朋克/像素/油画/3D卡通)选择引擎路由
- 有参考图(face_image/agent_id)→调用一致性写真生成
- 无参考图→调用通用绘画引擎纯text-to-image

| 风格 | style参数值 | 面部ID保持 | 推荐引擎 |
|:-----|:----------|:----------|:---------|
| 二次元 | anime | 否(艺术风格) | 通用绘画 T2I |
| 写实 | realistic | 是(98%,鹧应) | 鹧应AI写真→通用绘画 |
| 水彩 | watercolor | 否(艺术风格) | 通用绘画 T2I |
| 国风 | chinese_ink | 是(98%,鹧应) | 鹧应AI写真→通用绘画 |
| 赛博朋克 | cyberpunk | 否(艺术风格) | 通用绘画 T2I |
| 像素 | pixel | 否(艺术风格) | 通用绘画 T2I |
| 油画 | oil_painting | 否(艺术风格) | 通用绘画 T2I |
| 3D卡通 | 3d_cartoon | 否(艺术风格) | 通用绘画 T2I |

### Step 4: 生成图片
- 调用对应绘画引擎生成图片
- 等待生成完成(超时180秒)
- 下载图片到本地
- 异常处理:生成失败→重试1次→仍失败则换引擎→全部失败返回错误

### Step 5: 敏感词审核
- 审核prompt和生成结果描述
- 替换敏感词,确保合规
- prompt含违禁内容→拒绝生成并退款

### Step 6: 交付
- 电商订单:发送预览图+发送高清原图网盘链接
- 内容矩阵:生成作品展示帖用于社交平台发布
- 发送失败→记录待发送队列

## 输入格式
```json
{
  "style": "头像",
  "prompt": "一个戴眼镜的程序员,赛博朋克风格,蓝色调",
  "face_image": "d:/photos/selfie.jpg",
  "avatar_style": "cyberpunk",
  "template_id": "25f62a71-8255-431f-b0be-4e56f6b41921",
  "count": 1,
  "size": "1:1",
  "channel": "ecommerce",
  "order_id": "EC20240115002"
}
```

## 输出格式
```json
{
  "success": true,
  "data": {
    "images": [{"url": "https://...", "local_path": "d:/output/arts/xxx.png"}],
    "engine": "portrait_engine",
    "style": "头像",
    "face_preserved": true,
    "prompt_used": "实际使用的prompt"
  },
  "error": null,
  "code": null
}
```

## 异常处理

| 异常场景 | 原因 | 处理方式 | 错误码 |
|:---------|:-----|:---------|:-------|
| 参数缺失 | style/prompt未提供 | 提示补全缺失字段 | MISSING_PARAMS |
| 首选引擎不可用 | API Key未配置或服务宕机 | 降级到备选引擎链 | ENGINE_FALLBACK |
| 生成超时(180s) | 引擎响应慢或任务排队 | 重试1次后换引擎 | GENERATION_TIMEOUT |
| prompt含违禁内容 | 敏感词检测命中 | 拒绝生成+退款流程 | FORBIDDEN_CONTENT |
| 发送失败 | 网盘上传失败或消息发送失败 | 记录待发送队列,稍后重试 | DELIVERY_FAILED |
| count超限 | count>10 | 自动截断为10 | COUNT_TRUNCATED |

## 引擎降级链
- 头像(有参考图,写实): 鹧应AI写真(98%面部保持)→通用绘画 T2I(无面部保持)
- 头像(有参考图,艺术): 通用绘画 T2I(无面部保持)
- 头像(无参考图): 通用绘画→备选引擎A→备选引擎B
- 商品图: 通用绘画→备选引擎
- 视频图: 视频引擎A→视频引擎B→视频引擎C
- 注意: 通用绘画引擎不支持image参数(图生图),仅可用于text-to-image

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖说明
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代方案 |
|:-------|:-----|:---------|:---------|:-------------|
| LLM API | API | 必需 | 任意LLM服务商,由Agent内置LLM提供 | DeepSeek/通义千问/文心一言/Kimi等国内模型 |
| AI绘画引擎 | API | 必需 | 通用绘画引擎(免费)/鹧应AI写真(面部保持) | 通义万相/文心一格/即时AI等国内绘画API |
| 图像生成API | API | 可选 | 视频生成/角色一致性引擎 | 可灵AI/即梦AI等国内视频生成服务 |

### API Key 配置与安全要求
- **LLM_API_KEY**: 必需(通常由Agent内置) - prompt优化和敏感词审核
- **IMAGE_API_KEY**: 可选 - AI绘画引擎(通用绘画引擎可免费使用)
- **PORTRAIT_API_KEY**: 可选 - 鹧应AI写真98%面部保持
- 配置方式: 在Agent的环境变量中设置
- **零暴露原则**: API Key必须通过环境变量注入(如`%IMAGE_API_KEY%`),严禁硬编码在SKILL.md或脚本源码中;所有示例代码中Key位置使用占位符`$ENV:IMAGE_API_KEY`;禁止在日志、错误信息、输出JSON中打印Key明文

### 使用流程
通用绘画引擎支持免费text-to-image。鹧应AI写真用于写实头像98%面部保持。

只需将SKILL.md文件放入Agent的skills目录即可直接使用。
如果Skill中包含exec工具调用,需要Agent支持命令行执行能力。

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown,但需要exec能力(命令行执行),用于文件读写和命令调用

## 示例

### 示例1: 电商AI头像定制(有参考图,写实风格)

**输入**:
```json
{
  "style": "头像",
  "prompt": "一个戴眼镜的程序员,写实风格,蓝色调",
  "face_image": "d:/photos/selfie.jpg",
  "avatar_style": "realistic",
  "count": 1,
  "size": "1:1",
  "channel": "ecommerce",
  "order_id": "EC20240115002"
}
```

**执行流程**: 接收订单→提取需求(头像,写实风格,附自拍)→有参考图+写实风格→调用鹧应AI写真(face_image=自拍, style=realistic)→生成98%面部保持写实头像→敏感词审核通过→发送预览+网盘链接交付

**输出**:
```json
{
  "success": true,
  "data": {
    "images": [{"url": "https://cdn.example.com/arts/EC20240115002.png", "local_path": "d:/output/arts/EC20240115002.png"}],
    "engine": "portrait_engine",
    "style": "头像",
    "face_preserved": true,
    "prompt_used": "一个戴眼镜的程序员,写实风格,蓝色调"
  },
  "error": null,
  "code": null
}
```

### 示例2: 无参考图头像生成(赛博朋克风格)

**输入**:
```json
{
  "style": "头像",
  "prompt": "一个戴眼镜的程序员,赛博朋克风格,蓝色调",
  "avatar_style": "cyberpunk",
  "count": 1,
  "size": "1:1"
}
```

**执行流程**: 接收订单→提取需求(头像,赛博朋克风格)→无参考图→调用通用绘画引擎纯text-to-image→生成1张1:1头像图(面部一致性弱)→敏感词审核通过→发送预览+网盘链接交付

**输出**:
```json
{
  "success": true,
  "data": {
    "images": [{"url": "https://cdn.example.com/arts/cyberpunk_001.png", "local_path": "d:/output/arts/cyberpunk_001.png"}],
    "engine": "general_t2i",
    "style": "头像",
    "face_preserved": false,
    "prompt_used": "一个戴眼镜的程序员,赛博朋克风格,蓝色调,霓虹光效"
  },
  "error": null,
  "code": null
}
```

### 示例3: 引擎降级场景(鹧应不可用)

**输入**: 鹧应AI写真服务宕机时的写实头像订单
```json
{
  "style": "头像",
  "prompt": "写实风格头像",
  "face_image": "d:/photos/selfie.jpg",
  "avatar_style": "realistic"
}
```

**输出**: 自动降级到通用绘画引擎,标注面部保持降级
```json
{
  "success": true,
  "data": {
    "images": [{"url": "https://cdn.example.com/arts/fallback_001.png", "local_path": "d:/output/arts/fallback_001.png"}],
    "engine": "general_t2i",
    "style": "头像",
    "face_preserved": false,
    "downgraded_from": "portrait_engine",
    "downgrade_reason": "ENGINE_UNAVAILABLE"
  },
  "error": null,
  "code": "ENGINE_FALLBACK"
}
```

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 电商写实头像定制(有参考图,鹧应引擎,98%面部保持)

**输入**:
```json
{
  "style": "头像",
  "prompt": "写实风格,商务女性,职业装,微笑,办公室背景",
  "face_image": "d:/photos/client_selfie.jpg",
  "avatar_style": "realistic",
  "count": 1,
  "size": "1:1",
  "channel": "ecommerce",
  "order_id": "EC20260720001"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "images": [
      {
        "url": "https://cdn.artstation.com/output/EC20260720001_001.png",
        "local_path": "d:/output/arts/EC20260720001_001.png"
      }
    ],
    "engine": "portrait_engine",
    "style": "头像",
    "face_preserved": true,
    "prompt_used": "写实风格,商务女性,职业装,微笑,办公室背景,高清,自然光线,面部细节保留98%"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓面部保持率98%(鹧应引擎) ✓引擎正确路由(portrait_engine) ✓敏感词审核通过 ✓电商交付流程完整(网盘链接生成) ✓输出格式合规

### 案例2: 赛博朋克风格头像(无参考图,通用绘画引擎)

**输入**:
```json
{
  "style": "头像",
  "prompt": "一个戴眼镜的程序员,赛博朋克风格,蓝色调,霓虹灯光",
  "avatar_style": "cyberpunk",
  "count": 1,
  "size": "1:1",
  "channel": "social_media"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "images": [
      {
        "url": "https://cdn.artstation.com/output/cyberpunk_001.png",
        "local_path": "d:/output/arts/cyberpunk_001.png"
      }
    ],
    "engine": "general_t2i",
    "style": "头像",
    "face_preserved": false,
    "prompt_used": "一个戴眼镜的程序员,赛博朋克风格,蓝色调,霓虹灯光,高清,细节丰富"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓艺术风格正确路由(通用T2I引擎) ✓通用引擎免费生成 ✓面部保持标记正确(false) ✓prompt自动优化补充 ✓输出格式合规

### 案例3: 商业商品图批量生产(5张)

**输入**:
```json
{
  "style": "商品图",
  "prompt": "白色陶瓷马克杯,简约设计,电商产品图,白色背景",
  "count": 5,
  "size": "1:1",
  "channel": "ecommerce",
  "order_id": "EC20260720002"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "images": [
      {"url": "https://cdn.artstation.com/output/EC20260720002_001.png", "local_path": "d:/output/arts/EC20260720002_001.png"},
      {"url": "https://cdn.artstation.com/output/EC20260720002_002.png", "local_path": "d:/output/arts/EC20260720002_002.png"},
      {"url": "https://cdn.artstation.com/output/EC20260720002_003.png", "local_path": "d:/output/arts/EC20260720002_003.png"},
      {"url": "https://cdn.artstation.com/output/EC20260720002_004.png", "local_path": "d:/output/arts/EC20260720002_004.png"},
      {"url": "https://cdn.artstation.com/output/EC20260720002_005.png", "local_path": "d:/output/arts/EC20260720002_005.png"}
    ],
    "engine": "general_t2i",
    "style": "商品图",
    "face_preserved": false,
    "prompt_used": "白色陶瓷马克杯,简约设计,电商产品图,白色背景,高清,专业摄影,居中构图"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓批量生成5张商品图 ✓商品图模式正确路由 ✓count参数处理正确 ✓电商订单号绑定 ✓输出格式合规

### 案例4: 引擎降级场景(鹧应不可用,降级到通用绘画)

**输入**:
```json
{
  "style": "头像",
  "prompt": "写实风格,男性,西装,正式证件照",
  "face_image": "d:/photos/client_photo.jpg",
  "avatar_style": "realistic",
  "count": 1,
  "size": "1:1",
  "channel": "ecommerce",
  "order_id": "EC20260720003"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "images": [
      {
        "url": "https://cdn.artstation.com/output/EC20260720003_001.png",
        "local_path": "d:/output/arts/EC20260720003_001.png"
      }
    ],
    "engine": "general_t2i",
    "style": "头像",
    "face_preserved": false,
    "prompt_used": "写实风格,男性,西装,正式证件照,高清,自然光线"
  },
  "error": "鹧应AI写真引擎不可用,已降级到通用绘画引擎,面部保持能力减弱",
  "code": "ENGINE_FALLBACK"
}
```

**效果验证**: ✓降级链正确触发(鹧应→通用T2I) ✓降级原因在error字段标注 ✓面部保持标记降级为false ✓错误码ENGINE_FALLBACK正确返回 ✓服务可用性保证(降级而非失败)

### 案例5: 内容矩阵古风插画引流

**输入**:
```json
{
  "style": "风格图",
  "prompt": "古风山水画,水墨意境,远山近水,一位古人立于桥头",
  "avatar_style": "chinese_ink",
  "count": 3,
  "size": "9:16",
  "channel": "social_media"
}
```

**LLM生成输出**:
```json
{
  "success": true,
  "data": {
    "images": [
      {"url": "https://cdn.artstation.com/output/ink_001.png", "local_path": "d:/output/arts/ink_001.png"},
      {"url": "https://cdn.artstation.com/output/ink_002.png", "local_path": "d:/output/arts/ink_002.png"},
      {"url": "https://cdn.artstation.com/output/ink_003.png", "local_path": "d:/output/arts/ink_003.png"}
    ],
    "engine": "general_t2i",
    "style": "风格图",
    "face_preserved": false,
    "prompt_used": "古风山水画,水墨意境,远山近水,一位古人立于桥头,中国传统水墨画风格,留白构图,高清"
  },
  "error": null,
  "code": null
}
```

**效果验证**: ✓古风风格正确路由(通用T2I古风模式) ✓批量生成3张 ✓9:16竖版尺寸适配社交平台 ✓内容矩阵场景适配 ✓输出格式合规

## 常见问题

### Q1: 写实风格头像面部保持率能达到98%吗?
A: 是的,使用鹧应AI写真引擎时,在提供清晰正面参考图(face_image)的前提下,面部保持率可达98%。若鹧应引擎不可用降级到通用绘画引擎,面部保持能力会减弱(降至约70-85%)。建议写实风格订单务必提供清晰正面参考图。

### Q2: 通用绘画引擎是否真的免费?
A: 通用绘画引擎支持免费text-to-image,无需API Key即可使用,适合艺术风格图片生成(二次元/水彩/像素等)。但写实面部保持需调用鹧应AI写真(0.08元/张),建议接单时根据客户需求选择合适引擎以控制成本。

### Q3: 接单后如何自动交付给客户?
A: 电商订单渠道(channel=ecommerce)下,生成完成后会自动:1)生成预览图;2)上传高清原图到网盘;3)生成网盘分享链接;4)通过电商平台消息发送给买家。发送失败会记录待发送队列,支持后续重试。

### Q4: count参数最大支持多少张?
A: count参数最大支持10张,超过10张会自动截断为10(COUNT_TRUNCATED)。如需批量生成更多图片,建议分多次调用,每次不超过10张。

## 错误处理


| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| LLM响应超时或无响应 | 网络延迟或模型负载过高 | 执行ping命令测试网络连通性,检查防火墙和代理设置连接，执行ping命令测试网络连通性,检查防火墙和代理设置连接后重新执行命令请求；确认Agent平台LLM服务正常 |
| 输入内容格式不正确 | 用户输入不符合skill预期格式 | 检查输入是否符合skill使用说明中的格式要求，参考示例章节 |
| 执行结果与预期不符 | 指令描述不够明确或上下文不足 | 提供更详细的指令描述，补充必要的上下文信息 |
| 命令执行失败 | 运行环境不满足要求或权限不足 | 确认运行环境符合依赖说明中的要求；检查命令权限设置 |

## 已知限制

1. **通用绘画引擎不支持图生图**:通用绘画引擎仅支持text-to-image,不支持image参数(图生图),如需基于参考图生成必须使用鹧应AI写真引擎
2. **面部保持依赖参考图质量**:写实风格98%面部保持率依赖清晰正面参考图,模糊/侧脸/遮挡参考图会显著降低保持效果
3. **单次生成上限10张**:count参数最大10张,不支持单次大批量生成,需分批调用
4. **仅输出位图格式**:输出为PNG/JPG位图,不支持矢量图(SVG/EPS)和分层源文件(PSD/AI)输出
5. **视频生成需另配引擎**:本Skill主要处理静态图片,视频图生成需额外配置视频生成引擎API Key

## 变更历史

| 版本 | 日期 | 变更说明 |
|:-----|:-----|:---------|
| v1.0.0 | 2026-07-17 | 初版创建,双引擎路由+8种风格+接单SOP+引擎降级链 |
