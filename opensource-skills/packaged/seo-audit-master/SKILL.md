---
slug: seo-audit-master
name: seo-audit-master
version: 1.0.1
displayName: SEO审计大师
summary: 全站SEO体检:技术内容架构链接四维度审计,输出可执行优化清单
license: Proprietary
description: SEO审计大师——对网站执行全面SEO审计,覆盖技术SEO+内容SEO+架构验证+链接分析四维度。输出按优先级排序的可执行优化清单,支持Google与百度双搜索引擎,适用于上线前体检、排名下降诊断、新站优化、竞品对比、迁移检查场景。触发关键词:SEO审计、SEO诊断、技术SEO、内容SEO、SEO优化、网站审计、搜索引擎优化、索引、可抓取性、结构化数据、百度SEO、Google
  SEO
tags:
- SEO优化
- 网站审计
- 搜索引擎优化
- 技术SEO
- 流量增长
tools:
- read
- exec
# 定价元数据
suggested_price: "9.9 CNY/per_use"
pricing_tier: "L1-入门级"
pricing_model: "per_use"
tools: ["read", "exec", "glob", "grep"]
tags: "工具,效率,自动化"
---
# SEO审计大师

对网站执行全面 SEO 审计。从技术到内容,从架构到链接,输出可执行的优化清单。支持 Google 与百度双引擎,兼顾海外与国内搜索引擎优化。

## 核心能力

1. **技术 SEO 审计**:可抓取性、索引状态、Core Web Vitals、移动适配、HTTPS 安全检查
2. **内容 SEO 审计**:关键词覆盖、标题描述、内容质量、图片优化、重复内容检测
3. **架构与链接审计**:结构化数据(JSON-LD)、内部链接结构、URL 规范化、外链质量分析
4. **双引擎适配**:Google Search Console + 百度站长平台 + 搜狗站长平台
5. **优化清单输出**:按 Critical/Important/Suggested 三级优先级输出可执行修复步骤

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 全站审计 | 网站域名、sitemap、访问日志 | SEO 审计报告 + 按优先级排序的问题清单 |
| 排名下降诊断 | 域名、下降时间段、目标关键词 | 排名下降原因分析 + 恢复建议 |
| 新站优化 | 新站 URL、目标市场(国内/海外) | SEO 基础配置清单 + 内容策略 |
| 竞品对比 | 自有域名 + 竞品域名列表 | SEO 差距分析 + 赶超路径 |
| 迁移检查 | 迁移前后 URL 映射表 | 301 重定向方案 + 索引完整性验证 |

**不适用于**:
- 黑帽 SEO 与刷排名(仅支持白帽合规优化)
- SEM 竞价广告投放(专注于自然搜索优化)
- APP ASO 应用商店优化(专注于网页 SEO)
- 社交媒体运营(虽有关联,但非核心)
- 实时排名监控(需配合站长平台 API 长期追踪)

## 使用流程

### Step 1: 确定审计范围
1. 输入目标网站域名(如 https://example.com)
2. 确认目标搜索引擎(国内:百度/搜狗/360;海外:Google/Bing)
3. 确认审计深度(全站/核心页面/特定目录)
4. 收集辅助资料(sitemap.xml、robots.txt、访问日志)

### Step 2: 技术 SEO 审计
1. **可抓取性检查**:robots.txt 配置、爬虫权限、noindex/nofollow 标签
2. **索引状态**:已索引页面数 vs 总页面数、重复页面、canonical 问题
3. **页面速度**:Core Web Vitals(LCP/CLS/INP)、TTFB/FCP、移动端速度
4. **移动适配**:响应式设计、移动友好性、视口配置
5. **HTTPS 安全**:SSL 证书、混合内容检查

### Step 3: 内容 SEO 审计
1. **关键词分析**:目标关键词排名、覆盖缺口、长尾机会
2. **标题与描述**:title 标签、meta description、H1-H6 层级
3. **内容质量**:深度、关键词密度(1-2%)、LSI 语义词、新鲜度
4. **图片优化**:alt 文本、文件大小、WebP 格式

### Step 4: 架构与链接审计
1. **结构化数据**:JSON-LD schema、富媒体资格、错误检查
2. **内部链接**:链接结构、锚文本、孤立页面、点击深度
3. **URL 结构**:规范化、长度、层级、重定向链
4. **外链分析**:反链数量/质量、锚文本分布、有毒链接

### Step 5: 输出优化清单
1. 按 Critical/Important/Suggested 三级优先级排序
2. 每个问题附具体修复步骤与代码示例
3. 标注预期收益与实施难度
4. 生成可跟踪的实施清单

## 双引擎适配说明

| 维度 | Google | 百度 |
|:-----|:-----|:-----|
| 站长平台 | Google Search Console | 百度搜索资源平台 |
| 索引查询 | `site:domain.com` | `site:domain.com` |
| 提交入口 | sitemap 提交 + URL 检查 | 链接提交 + 主动推送 |
| 速度指标 | Core Web Vitals | 百度移动友好度 |
| 结构化数据 | JSON-LD 优先 | JSON-LD + 微数据 |
| 关键词工具 | Google Keyword Planner | 百度指数 + 百度关键词规划师 |

## 审计检查清单(核心)

- [ ] robots.txt 配置正确
- [ ] sitemap.xml 完整并已提交
- [ ] 所有重要页面已索引
- [ ] canonical 标签正确
- [ ] Core Web Vitals 全部达标(LCP<2.5s/CLS<0.1/INP<200ms)
- [ ] 移动友好
- [ ] HTTPS 无混合内容
- [ ] title/meta description 完整
- [ ] H1 唯一且含关键词
- [ ] 结构化数据无错误
- [ ] 内部链接结构合理
- [ ] 无孤立页面
- [ ] 无重复内容
- [ ] 图片有 alt 文本

## 示例

### 示例1: 全站 SEO 审计(输入→输出)

**输入**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|---:|---:|---:|---:|
| input | string | 是 | SEO审计大师处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

```
网站: https://shop.example.com
搜索引擎: 百度 + Google
深度: 全站(约 500 页)
关注点: 商品页索引、移动端速度
```

**输出**(seo-audit.md 片段):
```markdown
## SEO 审计报告
# ...
### 站点概况
- 总页面数: 487
- 已索引(百度): 312 (64%)
- 已索引(Google): 401 (82%)
- Core Web Vitals 通过率: 73%
# ...
### Critical 问题(3项)
1. [Critical] 商品页缺少 canonical 标签
   - 影响: 175 个商品页存在重复内容
   - 修复: 在 `<head>` 添加 `<link rel="canonical" href="https://shop.example.com/product/{id}" />`
# ...
2. [Critical] 移动端 LCP 超标(4.8s,应 <2.5s)
   - 影响: 移动端排名下降
   - 修复: 1) 首屏图片懒加载;2) 关键 CSS 内联;3) 图片转 WebP
# ...
3. [Critical] sitemap.xml 缺失
   - 影响: 爬虫无法发现新页面
   - 修复: 生成 sitemap.xml 并提交至百度/Google
# ...
### Important 问题(5项)
4. [Important] 38% 页面 title 重复
5. [Important] 商品图片缺少 alt 文本
6. [Important] 结构化数据错误(JSON-LD 缺少 price 字段)
...
# ...
### Suggested 建议(8项)
...
# ...
### 预期收益
- 修复 Critical 后预计索引覆盖率提升至 90%+
- 移动端排名预计提升 20-30%
```

### 示例2: 新站 SEO 基础配置(输入→输出)

**输入**:
```
新站: https://blog.example.com
目标市场: 国内(百度为主)
CMS: WordPress
```

**输出**(recommendations.md 片段):
```markdown
## 新站 SEO 基础配置清单
# ...
### 1. 站长平台注册
- [ ] 注册百度搜索资源平台(ziyuan.baidu.com)
- [ ] 添加站点并验证所有权
- [ ] 提交 sitemap.xml
- [ ] 开启主动推送 API
# ...
### 2. robots.txt 配置
```
User-agent: *
Allow: /
Disallow: /wp-admin/
Disallow: /wp-includes/
Sitemap: https://blog.example.com/sitemap.xml
```
# ...
### 3. 基础 SEO 插件配置
- 安装 Yoast SEO 或 Rank Math
- 启用 XML sitemap 自动生成
- 配置面包屑导航
- 启用结构化数据(Article schema)
# ...
### 4. 内容策略
- 首月发布 10+ 篇高质量原创文章(>1500字)
- 每篇文章聚焦 1 个主关键词 + 3-5 个长尾词
- 内链密度:每篇 3-5 个内链
- 图片全部添加 alt 文本
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---:|:---:|:---:|
| 网站无法访问 | DNS 解析失败或服务器宕机 | 检查域名状态与服务器健康,待恢复后重试 |
| 站长平台 API 超时 | 国内访问 Google Search Console 较慢 | 切换至百度搜索资源平台 API,或使用代理 |
| sitemap.xml 缺失 | 站点未生成 sitemap | 提供在线生成工具建议(xml-sitemaps.com)或脚本生成 |
| 索引数据为空 | 新站尚未被收录 | 提交至百度/Google 站长平台,等待 1-2 周 |
| 结构化数据校验失败 | JSON-LD 格式错误或字段缺失 | 使用 Schema.org Markup Validator 修正 |
| robots.txt 阻止爬虫 | 配置错误屏蔽了重要目录 | 检查 Disallow 规则,确保 /、/product/ 等允许 |
| Core Web Vitals 数据缺失 | 站点流量过低无 CrUX 数据 | 使用 Lighthouse 本地测试替代 |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:------|------:|:------|:------|------:|
| LLM API | API | 必需 | Agent 内置 LLM 提供分析 | 通义千问/文心一言/智谱 |
| Google Search Console | API | 可选 | 需要 Google 账号验证 | 百度搜索资源平台 |
| Lighthouse | 工具 | 可选 | `npm install -g lighthouse` | PageSpeed Insights 国内镜像 |
| WebSearch | 工具 | 可选 | Agent 内置联网搜索 | 百度搜索 + Bing 国内版 |

### API Key 配置
- **本Skill无需额外API Key配置**
- **站长平台访问**: 用户需自行注册百度/Google 站长平台并验证站点所有权
- **安全要求**: 如使用站长平台 API,token 仅存储在环境变量,不写入输出文件

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行 Lighthouse 等工具

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 电商网站全站SEO审计(百度+Google双引擎)

**输入**:
```
网站: https://shop.example.com
搜索引擎: 百度 + Google
深度: 全站(约500页)
关注点: 商品页索引、移动端速度、结构化数据
辅助资料: sitemap.xml已提供, robots.txt已配置
```

**LLM生成输出** (`output/shop-seo/seo-audit.md`):
```markdown
# SEO审计报告 - shop.example.com
# ...
## 站点概况(补充)
| 指标 | 数值 | 评价 |
|---:|:---|---:|
| 总页面数 | 487 | - |
| 已索引(百度) | 312 (64%) | 需提升 |
| 已索引(Google) | 401 (82%) | 良好 |
| Core Web Vitals通过率 | 73% | 需提升 |
| 移动友好性 | 通过 | 良好 |
| HTTPS | 已启用 | 良好 |
| sitemap.xml | 已提交 | 良好 |
# ...
## 问题清单(按优先级排序)
# ...
### Critical(3项)
# ...
#### 1. [Critical] 175个商品页缺少canonical标签
- **影响**: 商品页存在URL参数变体(?color=red&size=L),导致重复内容,百度判定为重复页面拒绝索引
- **位置**: 所有 `/product/{id}` 页面
- **检测方法**: `curl -s https://shop.example.com/product/123 | grep canonical` 返回空
- **修复方案**:
```html
<!-- 在每个商品页<head>中添加 -->
<link rel="canonical" href="https://shop.example.com/product/{id}" />
```
- **预期收益**: 百度索引覆盖率从64%提升至85%+
- **实施难度**: 低(模板修改)
# ...
#### 2. [Critical] 移动端LCP超标(4.8s,目标<2.5s)
- **影响**: Google移动端排名下降,百度移动友好度评分降低
- **根因**: Hero Banner图片3.2MB JPEG未压缩,CSS渲染阻塞1.2s
- **修复方案**:
```html
<!-- 1. 图片转WebP+懒加载 -->
<picture>
  <source srcset="/banner.webp" type="image/webp">
  <img src="/banner.jpg" alt="首页Banner" width="1920" height="600"
       loading="lazy" fetchpriority="high">
</picture>

<!-- 2. 关键CSS内联,非关键CSS异步加载 -->
<style>/* 首屏关键CSS(约15KB) */</style>
<link rel="preload" href="/css/main.css" as="style"
      onload="this.rel='stylesheet'">
```
- **预期收益**: LCP从4.8s降至2.2s,移动端排名提升20-30%
- **实施难度**: 中
# ...
#### 3. [Critical] sitemap.xml不完整
- **影响**: 爬虫无法发现新增的120个商品页
- **当前状态**: sitemap仅包含367个URL,缺少120个新商品页
- **修复方案**:
```bash
# 自动生成完整sitemap
npx next-sitemap --config sitemap.config.js
# 或使用脚本从数据库生成
python generate_sitemap.py --db sqlite:///products.db --output public/sitemap.xml
```
- **预期收益**: 120个新页面被百度/Google发现并索引
- **实施难度**: 低
# ...
### Important(5项)
# ...
#### 4. [Important] 38%页面title标签重复
- **影响**: 百度无法区分页面主题,影响关键词排名
- **示例**: 175个商品页title均为"商品详情 - 某某商城"
- **修复方案**:
```javascript
// Next.js动态title示例
export async function generateMetadata({ params }) {
  const product = await getProduct(params.id);
  return {
    title: `${product.name} - 价格¥${product.price} | 某某商城`,
    description: `购买${product.name},正品保障,${product.price}元起,支持7天无理由退换。`,
  };
}
```
# ...
#### 5. [Important] 商品图片缺少alt文本
- **影响**: 图片搜索无法索引,无障碍体验差
- **修复方案**: 为所有商品图片添加alt属性: `alt="{商品名称} - {商品规格}"`
# ...
#### 6. [Important] 结构化数据缺少price字段
- **影响**: 搜索结果无法显示价格富媒体,点击率降低15-20%
- **修复方案**:
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org/",
  "@type": "Product",
  "name": "无线蓝牙耳机",
  "image": ["https://shop.example.com/product/123/1.jpg"],
  "description": "高品质无线蓝牙耳机,降噪功能",
  "offers": {
    "@type": "Offer",
    "price": "299.00",
    "priceCurrency": "CNY",
    "availability": "https://schema.org/InStock"
  }
}
</script>
```
# ...
#### 7. [Important] 内部链接结构不合理
- **影响**: 重要商品页点击深度>4,爬虫难以发现,权重传递不足
- **修复方案**: 在首页和分类页添加热门商品链接,确保所有页面点击深度≤3
# ...
#### 8. [Important] robots.txt阻止了JS/CSS文件
- **影响**: 百度爬虫无法渲染页面,影响JS生成内容的索引
- **修复方案**:
```
User-agent: *
Allow: /
Allow: /css/
Allow: /js/
Disallow: /admin/
Sitemap: https://shop.example.com/sitemap.xml
```
# ...
### Suggested(8项)
9. 商品页面包屑导航缺少结构化数据(BreadcrumbList)
10. 部分页面meta description超过160字符
11. URL层级过深(/category/subcategory/product/variant)
12. 缺少404页面优化(无搜索建议)
13. 未配置Open Graph标签(影响社交分享)
14. 页面加载时无骨架屏(CLS=0.15)
15. 未使用hreflang(如有多语言需求)
16. 百度主动推送API未配置
# ...
## 预期收益汇总
| 修复阶段 | 预期效果 | 时间 |
|:------:|--------|:-------|
| 修复Critical(3项) | 索引覆盖率64%→90%,移动排名+30% | 1周 |
| 修复Important(5项) | 点击率+20%,关键词排名+15% | 2周 |
| 修复Suggested(8项) | 用户体验提升,长尾流量+10% | 4周 |
```

**效果验证**: ✓双引擎索引数据对比(百度64%/Google82%) ✓Critical/Important/Suggested三级优先级 ✓每个问题含影响+修复代码+预期收益 ✓结构化数据JSON-LD示例 ✓robots.txt配置修正

### 案例2: 排名下降原因诊断(百度排名骤降)

**输入**:
```
网站: https://blog.example.com
问题: 3个月内百度自然流量下降45%
下降时间: 2024年6月15日开始
目标关键词: "Python教程"从第3页降至第8页
近期变更: 5月底网站从HTTP迁移到HTTPS
```

**LLM生成输出** (`output/blog-diagnosis/ranking-drop.md`):
```markdown
# 排名下降诊断报告 - blog.example.com
# ...
## 下降概况
| 指标 | 下降前(5月) | 下降后(7月) | 变化 |
|----|:--:|---:|----|
| 百度自然流量 | 12,000/天 | 6,600/天 | -45% |
| "Python教程"排名 | 第3页 | 第8页 | -5页 |
| 索引页面数 | 320 | 285 | -35页 |
| 移动端收录 | 280 | 210 | -25% |
# ...
## 原因分析
# ...
### 根因1: HTTPS迁移未正确配置301重定向(权重损失)
- **严重程度**: Critical
- **证据**:
  - 旧HTTP页面返回200而非301(部分页面)
  - 百度站长平台显示大量"抓取异常"
  - 外链仍指向HTTP URL,权重未传递
- **诊断命令**:
```bash
# 检查301重定向
curl -I http://blog.example.com/python-tutorial/
# 预期: 301 Moved Permanently → https://blog.example.com/python-tutorial/
# 实际: 200 OK (未重定向!)

# 检查重定向链
curl -sIL http://blog.example.com/python-tutorial/ | grep -i "location\|HTTP"
```
- **修复方案**:
```nginx
# Nginx配置: HTTP强制301到HTTPS
server {
    listen 80;
    server_name blog.example.com;
    return 301 https://$server_name$request_uri;
}
```
- **预期恢复**: 修复后2-4周内排名逐步恢复
# ...
### 根因2: 迁移后canonical标签指向HTTP版本
- **严重度**: High
- **证据**: 检查页面源码发现:
```html
<!-- 错误:canonical指向HTTP -->
<link rel="canonical" href="http://blog.example.com/python-tutorial/" />
```
- **影响**: 百度认为HTTPS页面是HTTP页面的重复内容,降低HTTPS页面权重
- **修复方案**:
```html
<!-- 修正:canonical指向HTTPS -->
<link rel="canonical" href="https://blog.example.com/python-tutorial/" />
```
# ...
### 根因3: sitemap.xml未更新为HTTPS URL
- **严重度**: Medium
- **证据**: sitemap.xml中所有URL仍为HTTP
- **影响**: 百度爬虫优先抓取HTTP URL,发现301后重新抓取HTTPS,浪费抓取配额
- **修复方案**:
```bash
# 更新sitemap中的URL为HTTPS
sed -i 's/http:\/\//https:\/\//g' public/sitemap.xml
# 重新提交至百度站长平台
curl -H "Content-Type: text/plain" --data-urlencode "sitemap=https://blog.example.com/sitemap.xml" "https://ziyuan.baidu.com/ping?site=https://blog.example.com&resource_name=sitemap"
```
# ...
### 根因4: 百度主动推送API未更新
- **严重度**: Low
- **证据**: 推送API中URL仍为HTTP格式
- **修复方案**: 更新推送脚本中的URL为HTTPS格式
# ...
## 恢复计划
# ...
### 第一周(紧急修复)
1. [P0] 修复301重定向(Nginx配置)
2. [P0] 修正所有canonical标签为HTTPS
3. [P1] 更新sitemap.xml为HTTPS URL并重新提交
# ...
### 第二周(验证)
4. [P1] 百度站长平台提交"抓取诊断",验证HTTPS页面可正常抓取
5. [P1] 检查索引覆盖率变化(预期:285→320恢复)
6. [P2] 监控关键词排名变化
# ...
### 第三-四周(观察)
7. [P2] 持续监控自然流量恢复情况
8. [P2] 如未恢复,检查是否有其他因素(内容质量/外链/算法更新)
# ...
## 预期恢复时间线
| 时间节点 | 预期状态 |
|----|----|
| 修复后1周 | 百度重新抓取HTTPS页面,索引开始恢复 |
| 修复后2周 | 索引页面数恢复至300+,关键词排名回升 |
| 修复后4周 | 自然流量恢复至下降前80-90% |
| 修复后8周 | 完全恢复(需外链权重传递到位) |
# ...
## 教训总结
HTTPS迁移SEO检查清单:
- [ ] 301重定向全部配置正确(无遗漏页面)
- [ ] canonical标签更新为HTTPS
- [ ] sitemap.xml更新为HTTPS URL
- [ ] 百度/Google站长平台重新提交sitemap
- [ ] 主动推送API更新URL格式
- [ ] 外链联系更新(尽可能让外链指向HTTPS)
- [ ] 旧HTTP域名301保持至少6个月
```

**效果验证**: ✓根因定位精确(301未配置+canonical错误+sitemap未更新) ✓诊断命令可执行(curl验证) ✓恢复计划含时间线预期 ✓修复方案含Nginx配置代码 ✓迁移检查清单可复用

### 案例3: 新站SEO基础配置(百度为主)

**输入**:
```
新站: https://blog.example.com
目标市场: 国内(百度为主)
CMS: WordPress
内容方向: 技术博客(Python/Java/DevOps)
目标: 3个月内百度收录100+页面
```

**LLM生成输出** (`output/new-blog-seo/recommendations.md`):
```markdown
# 新站SEO基础配置清单 - blog.example.com
# ...
## 1. 百度站长平台配置
# ...
### 1.1 注册与验证
- [ ] 注册百度搜索资源平台(ziyuan.baidu.com)
- [ ] 添加站点 https://blog.example.com
- [ ] 完成所有权验证(推荐HTML标签验证)
- [ ] 选择站点类型(普通网站)
# ...
### 1.2 链接提交配置
```php
// WordPress主动推送插件代码(functions.php)
add_action("publish_post", "baidu_push");
function baidu_push($post_id) {
    $url = get_permalink($post_id);
    $api = "http://data.zz.baidu.com/urls?site=blog.example.com&token=YOUR_TOKEN";
    $ch = curl_init();
    curl_setopt($ch, CURLOPT_URL, $api);
    curl_setopt($ch, CURLOPT_POST, true);
    curl_setopt($ch, CURLOPT_POSTFIELDS, $url);
    curl_setopt($ch, CURLOPT_HTTPHEADER, ["Content-Type: text/plain"]);
    curl_exec($ch);
}
```
# ...
### 1.3 sitemap提交
- [ ] 安装Yoast SEO插件,自动生成sitemap
- [ ] 在百度站长平台提交: https://blog.example.com/sitemap_index.xml
# ...
## 2. robots.txt配置
```
User-agent: *
Allow: /
Disallow: /wp-admin/
Disallow: /wp-includes/
Disallow: /wp-content/cache/
Allow: /wp-content/uploads/

# 百度爬虫
User-agent: Baiduspider
Allow: /

Sitemap: https://blog.example.com/sitemap_index.xml
```
# ...
## 3. 基础SEO插件配置(Yoast SEO)
# ...
### 3.1 全局设置
- [ ] 标题模板: `%%title%% %%page%% - %%sitename%%`
- [ ] Meta描述模板: `%%excerpt%%`
- [ ] 开启XML sitemap
- [ ] 开启面包屑导航
# ...
### 3.2 内容类型设置
| 内容类型 | 是否索引 | 显示日期 | sitemap |
|:-----|:-----|:-----|:-----|
| 文章(post) | 是 | 是 | 包含 |
| 页面(page) | 是 | 否 | 包含 |
| 分类 | 是 | 否 | 包含 |
| 标签 | 否(内容少时) | 否 | 视情况 |
# ...
## 4. 结构化数据配置
# ...
### 4.1 Article Schema(文章)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "Python装饰器完全指南",
  "author": { "@type": "Person", "name": "作者名" },
  "datePublished": "2024-07-20",
  "dateModified": "2024-07-20",
  "image": "https://blog.example.com/python-decorator.jpg",
  "publisher": {
    "@type": "Organization",
    "name": "技术博客",
    "logo": { "@type": "ImageObject", "url": "https://blog.example.com/logo.png" }
  },
  "mainEntityOfPage": { "@type": "WebPage", "@id": "https://blog.example.com/python-decorator" }
}
</script>
```
# ...
### 4.2 Breadcrumb Schema(面包屑)
```html
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    { "@type": "ListItem", "position": 1, "name": "首页", "item": "https://blog.example.com/" },
    { "@type": "ListItem", "position": 2, "name": "Python", "item": "https://blog.example.com/python/" },
    { "@type": "ListItem", "position": 3, "name": "装饰器指南" }
  ]
}
</script>
```
# ...
## 5. 内容策略(前3个月)
# ...
### 第1月: 基础内容建设
| 周 | 发布计划 | 关键词 | 字数 |
|---:|---:|---:|---:|
| 1 | 3篇Python入门教程 | Python安装/变量/数据类型 | 2000+ |
| 2 | 3篇Python进阶 | Python装饰器/生成器/异常处理 | 2500+ |
| 3 | 2篇Java基础 | Java环境搭建/基础语法 | 2000+ |
| 4 | 2篇DevOps入门 | Docker入门/CI/CD概念 | 2500+ |
# ...
### 关键词策略
| 主关键词 | 搜索量(百度指数) | 竞争度 | 目标排名 |
|:---:|:---:|:---:|:---:|
| Python教程 | 8,000 | 高 | 前3页(3月内) |
| Python入门 | 5,000 | 中 | 前2页(2月内) |
| Java教程 | 6,000 | 高 | 前3页(3月内) |
| Docker入门 | 3,000 | 中 | 前2页(2月内) |
# ...
### 长尾关键词策略
- 每篇主文章配套3-5篇长尾内容(如"Python列表去重的5种方法")
- 长尾词搜索量低但竞争小,容易获得排名
- 目标:3个月内覆盖200+长尾关键词
# ...
## 6. 内链策略
- 每篇文章包含3-5个内链(指向相关文章)
- 使用关键词作为锚文本(非"点击这里")
- 分类页链接所有该分类下的文章
- 首页展示最新10篇文章+热门文章
# ...
## 7. 技术SEO检查清单
- [ ] HTTPS证书有效(无混合内容)
- [ ] 移动端响应式设计
- [ ] LCP < 2.5s(图片WebP+缓存)
- [ ] CLS < 0.1(图片指定尺寸)
- [ ] INP < 200ms(避免长任务)
- [ ] 固定链接结构: /%category%/%postname%/
- [ ] 404页面含搜索建议
- [ ] 图片全部有alt文本
# ...
## 8. 监控指标
| 指标 | 工具 | 频率 | 目标(3月) |
|:------|------:|:------|:------|
| 百度收录量 | site:blog.example.com | 每周 | 100+ |
| 百度索引量 | 百度站长平台 | 每周 | 100+ |
| 关键词排名 | 百度搜索手动查 | 每周 | 前3页 |
| 自然流量 | 百度统计 | 每日 | 500+/天 |
| 抓取频次 | 百度站长平台 | 每周 | 50+/天 |
```

**效果验证**: ✓百度站长平台完整配置(验证+推送+sitemap) ✓WordPress Yoast SEO配置 ✓Article+Breadcrumb双重结构化数据 ✓3个月内容发布计划(按周) ✓关键词策略含百度指数+竞争度

### 案例4: 竞品SEO差距分析

**输入**:
```
自有域名: https://my-shop.com
竞品: https://competitor-a.com, https://competitor-b.com
行业: 在线教育平台
目标: 识别SEO差距,制定赶超路径
```

**LLM生成输出** (`output/competitor-analysis/gap-analysis.md`):
```markdown
# SEO竞品差距分析报告
# ...
## 1. 三方对比概览
| 指标 | my-shop.com | competitor-a | competitor-b | 差距 |
|---:|:---|---:|---:|:---|
| 百度收录 | 156 | 892 | 645 | -736 / -489 |
| Google收录 | 203 | 1,150 | 780 | -947 / -577 |
| 预估自然流量 | 2,000/月 | 45,000/月 | 28,000/月 | -43,000 / -26,000 |
| 关键词覆盖 | 320 | 2,800 | 1,600 | -2,480 / -1,280 |
| 外链数量 | 45 | 1,200 | 680 | -1,155 / -635 |
| Core Web Vitals | 60%通过 | 95%通过 | 80%通过 | -35% / -20% |
# ...
## 2. 差距分析
# ...
### 2.1 技术SEO差距
| 维度 | my-shop.com | competitor-a | 优先级 |
|:------:|--------|:-------|:------:|
| 页面速度(LCP) | 4.2s | 1.8s | P0 |
| 移动适配 | 基本响应式 | AMP+响应式 | P1 |
| 结构化数据 | 无 | Course+FAQ+Review | P1 |
| sitemap | 部分完整 | 完整+自动更新 | P2 |
| 内链结构 | 扁平(1层) | 层级(3层+面包屑) | P2 |
# ...
### 2.2 内容SEO差距
| 维度(续)| my-shop.com | competitor-a | 优先级 |
|----|:--:|---:|----|
| 总内容量 | 156篇 | 892篇 | P0 |
| 平均字数 | 800字 | 2,500字 | P0 |
| 关键词覆盖 | 320个 | 2,800个 | P0 |
| 长尾词覆盖 | 50个 | 1,500个 | P1 |
| 内容更新频率 | 2篇/周 | 10篇/周 | P1 |
| 原创比例 | 70% | 95% | P1 |
# ...
### 2.3 关键词差距(Top 50差距关键词)
| 关键词 | 竞品A排名 | 我方排名 | 月搜索量 | 赶超难度 |
|----|----|----|----|----|
| Python在线课程 | 第1页第3位 | 未排名 | 8,000 | 中(需10篇+内容) |
| Java培训 | 第1页第5位 | 第5页 | 6,500 | 高(需50+外链) |
| 编程入门 | 第1页第2位 | 第3页第8位 | 12,000 | 中(内容优化) |
| 在线编程学习 | 第1页第4位 | 未排名 | 4,500 | 低(新内容即可) |
| 算法教程 | 第1页第6位 | 第4页 | 3,200 | 中(需深度内容) |
# ...
## 3. 赶超路径(6个月计划)
# ...
### 第1-2月: 技术SEO修复(基础)
- [P0] 修复Core Web Vitals(LCP 4.2s→2.0s)
- [P0] 添加Course结构化数据
- [P1] 优化内链结构(3层+面包屑)
- [P1] 完善sitemap自动更新机制
- 预期: 技术SEO评分从60%提升至90%
# ...
### 第3-4月: 内容建设(核心)
- [P0] 每周发布10篇深度文章(2500字+)
- [P0] 覆盖Top 50差距关键词中的20个
- [P1] 每篇文章配套3-5篇长尾内容
- [P1] 优化已有156篇内容的深度和关键词
- 预期: 关键词覆盖320→800,收录156→400
# ...
### 第5-6月: 外链建设(加速)
- [P0] 获取30+高质量教育类外链
- [P1] 与5+教育博客建立内容合作
- [P1] 发布2篇行业研究报告(吸引自然外链)
- [P2] 优化社交媒体分享(Open Graph标签)
- 预期: 外链45→200,自然流量2,000→8,000/月
# ...
## 4. 6个月预期效果
| 指标 | 当前 | 6月后预期 | 竞品A差距 |
|:-----|:-----|:-----|:-----|
| 百度收录 | 156 | 500+ | 缩小至1:1.8 |
| 关键词覆盖 | 320 | 1,200+ | 缩小至1:2.3 |
| 自然流量 | 2,000/月 | 10,000+/月 | 缩小至1:4.5 |
| 外链数量 | 45 | 250+ | 缩小至1:4.8 |
```

**效果验证**: ✓三方对比数据完整(收录/流量/关键词/外链) ✓技术SEO+内容SEO双维度差距 ✓Top 50差距关键词清单 ✓6个月赶超路径(技术→内容→外链) ✓每阶段含预期效果量化

## 常见问题

### Q1: 国内项目应该优先优化百度还是 Google?
A: 取决于目标用户:
- 面向国内用户:优先百度(80%份额),兼顾搜狗/360/神马
- 面向海外用户:优先 Google,兼顾 Bing
- 双市场:技术 SEO 基础(速度/移动端/HTTPS)通用,内容与关键词分别优化

### Q2: Core Web Vitals 指标具体要求是什么?
A: 
- LCP(最大内容绘制): < 2.5s
- CLS(累积布局偏移): < 0.1
- INP(交互到下一次绘制): < 200ms
- TTFB(首字节时间): < 800ms
- FCP(首次内容绘制): < 1.8s

### Q3: 如何快速提升百度收录?
A: 1) 注册百度搜索资源平台;2) 提交 sitemap;3) 使用主动推送 API(新内容立即推送);4) 发布高质量原创内容;5) 获取高质量外链;6) 优化移动端体验。

### Q4: 网站迁移后如何保持 SEO 权重?
A: 1) 制定 URL 301 重定向映射表;2) 迁移前在 Google Search Console 提交地址更改;3) 迁移后立即提交新 sitemap;4) 监控索引覆盖率 2-4 周;5) 修复 404 错误;6) 保持旧域名 301 至少 6 个月。

## 已知限制

- 无法获取实时排名数据(需配合站长平台 API 或第三方排名工具)
- 国内访问 Google Search Console 较慢,建议优先使用百度搜索资源平台
- Core Web Vitals 数据依赖 CrUX 报告,低流量站点可能无数据
- 不能自动修复问题,仅输出修复建议(需开发者执行)
- 不覆盖黑帽 SEO 检测(关键词堆砌、隐藏文本等基础检测除外)
- SEM 竞价广告优化不在范围内

## 安全声明

- 站长平台 API token 仅在内存中使用,不写入日志或输出文件
- 网站访问日志分析时自动脱敏用户 IP(只保留前 3 段)
- 输出的审计报告不包含任何敏感凭证信息
