---
slug: amap-jsapi-skill
name: amap-jsapi-skill
version: "1.1.1"
displayName: Amap Jsapi Skill
summary: 高德地图 JSAPI v2.0 (WebGL) 开发技能。涵盖地图生命周期管理、强制安全配置、3D 视图控制、覆盖物绘制及 LBS 服务集成。
license: MIT-0
description: |-
  高德地图 JSAPI v2。0 (WebGL) 开发技能。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。适用于独立开发者、企业团队和自动化工作流场景。Use when 需要API集成、接口对接、Webhook配置、系统连接时使用。不适用于逆向工程闭源API。
tags: '[''Security'']'
tools:
  - read
  - exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Gaode Map JSAPI - é«å¾·å®æ¹ JavaScript SDK Skill

本指南包含地图初始化、覆盖物、事件、图层等核心模块的 API 说明和代码示例，旨在帮助开发者快速集成高德地图并遵循正确的使用方式。

## 快速开始

### 1. 引入加载器

使用 script 标签加载 loader.js：

```bash
<script src="https://webapi.amap.com/loader.js"></script>
```

### 2. 安全密钥配置 (强制)

**重要**：自 v2.0 起，必须在加载地图前配置安全密钥，否则无法通过鉴权。详情及后端代理示例请参考 [安全策略](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fsecurity.md&ownerHandle=lbs-amap)。

> **安全提示**：安全密钥属于敏感凭据，请通过环境变量 `AMAP_SECURITY_JS_CODE` 传入，禁止在代码中硬编码。生产环境务必使用 `serviceHost` 代理方式，避免前端暴露密钥。

```javascript
// 在调用 AMapLoader.load 前执行
window._AMapSecurityConfig = {
  securityJsCode: process.env.AMAP_SECURITY_JS_CODE, // 通过环境变量安全获取
  // serviceHost: 'https://your-proxy-domain/_AMapService', // 生产环境：建议使用代理转发
};
```

### 3. 初始化地图

```javascript
import AMapLoader from '@amap/amap-jsapi-loader';
AMapLoader.load({
    key: '您的Web端开发者Key', // 必填
    version: "2.0",           // 指定版本
    plugins: ['AMap.Scale', 'AMap.ToolBar'] // 预加载插件
}).then((AMap) => {
    // 可选：设置应用标识，用于 API 调用来源统计
    AMap.getConfig().appname = 'amap-jsapi-skill';

    const map = new AMap.Map('container', {
        viewMode: '3D',       // 开启3D视图
        zoom: 11,             // 初始缩放级别
        center: [116.39, 39.90] // 初始中心点
    });
    map.addControl(new AMap.Scale());
}).catch(e => console.error(e));
```

## 示例

### 地图控制

* **生命周期**：`references/map-init.md` - 掌握 `load`、`Map` 实例创建及 `destroy` 销毁流程。
* **视图交互**：`references/view-control.md` - 控制 `zoom` (缩放)、`center` (平移)、`pitch` (俯仰)、`rotation` (旋转)。

### 覆盖物绘制

* **点标记**：`references/marker.md` - 使用 `Marker` (基础)、`LabelMarker` (海量避让) 标注位置。
* **矢量图形**：`references/vector-graphics.md` - 绘制 `Polyline` (轨迹、线)、`Polygon` (区域、面)、`Circle` (范围、圆)。
* **信息展示**：`references/info-window.md` - 通过 `InfoWindow` 展示详细信息。
* **右键菜单**：`references/context-menu.md` - 自定义地图或覆盖物的右键交互。

### 图层管理

* **基础图层**：`references/layers.md` - 标准、卫星、路网及 3D 楼块图层。
* **自有数据**：`references/custom-layers.md` - 集成 `Canvas`、`WMS/WMTS`, `GLCustomLayer` 地图上叠加 Canvas、WMS图层、 Threejs图层。

### 服务与插件

* **LBS 服务**：
  + `references/geocoder.md` - 地理编码/逆地理编码（地址/坐标互转）。
  + `references/routing.md` - 路径规划（驾车/步行/公交）。
  + `references/search.md` - POI 搜索与输入提示。
* **事件系统**：`references/events.md` - 响应点击、拖拽、缩放等交互事件。

## 最佳实践

1. **安全第一**：生产环境务必使用代理服务器转发 `serviceHost`，避免 `securityJsCode` 泄露。
2. **按需加载**：仅在 `plugins` 中声明需要的插件，减少首屏资源体积。
3. **资源释放**：组件卸载时务必调用 `map.destroy()`，防止 WebGL 上下文内存泄漏。

## API Reference

JSAPI 文档分为以下几个类别：

### [Foundation Classes](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Ffoundation.md&ownerHandle=lbs-amap)

LngLat / Bounds / Pixel / Size

### [Information Window](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Finfo-window.md&ownerHandle=lbs-amap)

InfoWindow

### [Events](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fevents.md&ownerHandle=lbs-amap)

Event

### [Map](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fmap.md&ownerHandle=lbs-amap)

Map / MapsEvent

### [Official Layers](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Flayers-official.md&ownerHandle=lbs-amap)

TileLayer / Traffic / Satellite / RoadNet / Buildings / DistrictLayer / IndoorMap

### [Standard Layers](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Flayers-standard.md&ownerHandle=lbs-amap)

WMS / WMTS / MapboxVectorTileLayer

### [Custom Layers](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Flayers-custom.md&ownerHandle=lbs-amap)

HeatMap / VectorLayer / LabelsLayer / CustomLayer / Flexible / ImageLayer / CanvasLayer / GLCustomLayer

### [Markers](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fmarker.md&ownerHandle=lbs-amap)

Marker / Text / Icon / LabelMarker / ElasticMarker / MarkerCluster / MassMarks / MoveAnimation / AnimationCallback / EasingCallback

### [Context Menu](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fcontext-menu.md&ownerHandle=lbs-amap)

ContextMenu

### [Vector Graphics](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fvector-graphics.md&ownerHandle=lbs-amap)

Polygon / Polyline / BezierCurve / Circle / CircleMarker / Ellipse / Rectangle / GeoJSON

### [Overlay Groups](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Foverlay-group.md&ownerHandle=lbs-amap)

LayerGroup / OverlayGroup

### [Controls](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fcontrols.md&ownerHandle=lbs-amap)

Control / Scale / ToolBar / ControlBar / MapType / HawkEye

### [Tools](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Ftools.md&ownerHandle=lbs-amap)

RangingTool / MouseTool / PolygonEditor / PolylineEditor / CircleEditor / BezierCurveEditor / EllipseEditor / RectangleEditor

### [Services](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fservices.md&ownerHandle=lbs-amap)

WebService / WebServiceCallback

### [Search](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fsearch.md&ownerHandle=lbs-amap)

AutoComplete / AutoCompleteSearchCallback / PlaceSearch / searchCallback / CloudDataSearch / CloudDataSearchCallback

### [Geocoder](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fgeocoder.md&ownerHandle=lbs-amap)

Geocoder / GeocoderCallback / ReGeocoderCallback / convertFrom

### [Routing](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Frouting.md&ownerHandle=lbs-amap)

Driving / DrivingCallback / DrivingResult / DriveStepBasic / DriveStepDetail / TruckDriving / Walking / WalkingCallback / WalkingResult / Transfer / TransferCallback / TransferResult / Riding / RidingCallback / RidingResult / DragRoute / DragRouteTruck / GraspRoad / GraspRoadCallback

### [Other Services](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fservices-other.md&ownerHandle=lbs-amap)

DistrictSearch / Weather / WeatherLiveResult / WeatherForecastResult / StationSearch / LineSearch

### [Geolocation](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fgeolocation.md&ownerHandle=lbs-amap)

Geolocation / GeolocationCallBack / GeolocationResult / CitySearch

### [Common Library](/api/v1/skills/amap-jsapi-skill/file?path=references%2Fapi%2Fcommon.md&ownerHandle=lbs-amap)

GeometryUtil / DomUtil / Browser / Util

## 使用 skills 必须遵循的规范

1. **校验生成代码可用性**：生成代码后必须进行自我校验，确保代码语法正确、逻辑完整且可以正常运行，禁止输出未经验证的代码。
2. **本地文件放置规范**：所有生成的项目文件必须放置在 skill-platform workspace 目录下的 `amap-jsapi/` 文件夹中。文件名统一使用 kebab-case 命名（如 `map-init.html`、`layers-official.html`）。
3. **appname 应用标识（推荐）**：建议在生成地图初始化代码时，在 `AMapLoader.load().then()` 回调中设置应用标识，用于 API 调用来源统计。规则如下：
   * **设置位置**：`AMapLoader.load({...}).then((AMap) => {` 回调内部，`new AMap.Map()` 之前
   * **设置方式**：`AMap.getConfig().appname = 'amap-jsapi-skill';`
   * **代码模板**：

     javascript

     ```
     AMapLoader.load({
       key: '您的Key',
       version: "2.0",
       plugins: [...]
     }).then((AMap) => {
       // 可选：设置应用标识，用于 API 调用来源统计
       AMap.getConfig().appname = 'amap-jsapi-skill';

       const map = new AMap.Map('container', { ... });
     });
     ```
   * **说明**：此设置用于标识 API 调用来源，便于统计分析。开发者可根据需要决定是否保留。

## 如何使用

1. 如果有相近的“场景示例”那么去阅读场景示例，再阅读场景示例中的涉及的类的api文档。再结合描述/场景示例/api 去完成任务。
2. 在最终的完成任务前，检查用的api用法是否符合文档。

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

- 高德地图 JSAPI v2
- 0 (WebGL) 开发技能
- 涵盖地图生命周期管理、强制安全配置、3D 视图控制、覆盖物绘制及 LBS 服务集成
- \n\
  \n触发关键词: 高德地图, map, amap, webgl, 周期管理, é«\x98å¾·å®\x98æ\x96¹, jsapi, sdk

## 适用场景

| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Amap Jsapi Skill？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Amap Jsapi Skill有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
