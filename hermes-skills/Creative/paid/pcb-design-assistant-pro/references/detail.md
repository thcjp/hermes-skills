# 详细参考 - pcb-design-assistant-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (javascript)

```javascript
// PCB布局配置
const pcbConfig = {
  board: {
    shape: "rectangular",
    width: 100,  // mm
    height: 80,
    layers: 4,   // 4层板
    stackup: ["signal", "gnd", "pwr", "signal"]
  },
  placement: {
    mode: "hybrid",  // auto | manual | hybrid
    constraints: {
      "U1": {x: 25, y: 40, rotation: 0},      // MCU居中
      "J1": {x: 5, y: 40, side: "top"},        // USB-C左侧
      "U2": {x: 75, y: 40}                     // LDO右侧
    }
  },
  routing: {
    width: {signal: 0.2, power: 0.5, ground: 0.6},  // mm
    via: {diameter: 0.6, drill: 0.3},
    strategy: "preferred_direction",  // top:horizontal, bottom:vertical
    differential_pairs: [
      {nets: ["USB_DP", "USB_DM"], width: 0.2, gap: 0.15}
    ]
  }
};

await eda.pcb.layout(pcbConfig);
```

## 代码示例 (javascript)

```javascript
const project = await pcbAssistant.createProject({
  name: "Product_v1",
  config: "project_config.yaml"  // 含完整设计规范
});

// 1. 多页原理图
await pcbAssistant.schematic.design(project.id);

// 2. PCB布局布线
await pcbAssistant.pcb.layout(project.id, "hybrid");
await pcbAssistant.pcb.route(project.id, "diff_aware");

// 3. DRC + ERC
const drc = await pcbAssistant.pcb.runDRC(project.id, {strict: true});
const erc = await pcbAssistant.erc.check(project.id, {include: ["si", "pi", "emc"]});

// 4. BOM生成
const bom = await pcbAssistant.bom.generate(project.id, {check_stock: true});

// 5. 打板文件
await pcbAssistant.export.manufacturing(project.id, {jlcpcb_compatible: true});

// 6. 一键下单（可选）
if (project.config.auto_order) {
  await pcbAssistant.bom.orderToLCSC(project.id);
}
```

## 代码示例 (text)

```text
┌─────────────────────────────────────────────────────────────────┐
│              PCB设计助手专业版 (PCB DESIGN ASSISTANT PRO)         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐          │
│  │  桥接层       │  │  EDA API层    │  │  设计层       │          │
│  │  BRIDGE      │  │  EDA API     │  │  DESIGN      │          │
│  │              │  │              │  │              │          │
│  │  MCP工具协议 │→ │  元件库搜索  │→ │  拓扑选型    │          │
│  │  API桥接回退 │  │  元件放置    │  │  网表命名    │          │
│  │  状态检查    │  │  连线绘制    │  │  页面布局    │          │
│  └──────────────┘  │  PCB布局     │  │  验证检查    │          │
│                    │  DRC检查     │  │              │          │
│                    └──────────────┘  └──────────────┘          │
│                                                                 │
│  ┌──────────────────────────────────────────────────────┐       │
│  │              高级能力层 (PRO ONLY)                    │       │
│  │                                                      │       │
│  │  多页原理图 | PCB布局布线 | DRC检查 | 多层板设计      │       │
│  │  自定义库   | 设计复用   | 扩展ERC | BOM下单         │       │
│  │  Gerber输出 | 版本管理   | 差异对比                  │       │
│  └──────────────────────────────────────────────────────┘       │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

## 代码示例 (javascript)

```javascript
const project = await pcbAssistant.createProject({
  name: "STM32_Dev_Board",
  pages: [
    {name: "power", template: "usb_c_5v"},
    {name: "mcu", template: "stm32f103"},
    {name: "interface", template: "uart_usb"}
  ],
  pcb: {
    size: {width: 100, height: 80},
    layers: 4,
    stackup: "standard_4l"
  }
});

// 自动布局+布线
await pcbAssistant.pcb.autoLayout(project.id);
await pcbAssistant.pcb.autoRoute(project.id, {strategy: "preferred_direction"});

// DRC检查
const drc = await pcbAssistant.pcb.runDRC(project.id, {strict: true});
if (drc.errors > 0) {
  await pcbAssistant.pcb.fixIssues(project.id, drc.details);
}
```

## 代码示例 (javascript)

```javascript
// 生成BOM
const bom = await eda.bom.generate({
  format: "xlsx",
  include: ["lcsc_id", "name", "value", "package", "quantity", "stock", "price"],
  check_stock: true,
  preferred_vendor: "lcsc"
});

// 输出
// BOM.xlsx:
// | 编号 | 立创编号 | 名称    | 值   | 封装    | 数量 | 库存  | 单价  |
// |------|----------|---------|------|---------|------|-------|-------|
// | 1    | C8734    | STM32F103| -   | LQFP48  | 1    | 12000 | 6.8   |
// | 2    | C1234    | 电阻    | 10k  | 0603    | 5    | 99999 | 0.01  |

// 一键下单至立创
await eda.bom.orderToLCSC({
  bom_id: bom.id,
  shipping: "standard",
  payment: "existing_account"
});
```

## 代码示例 (javascript)

```javascript
// 创建自定义元件
await eda.library.createPart({
  name: "MyModule_A",
  category: "module",
  footprint: {
    pads: [
      {name: "VCC", x: 0, y: 0, shape: "rect", width: 1.5, height: 0.8},
      {name: "GND", x: 0, y: 2.54, shape: "rect", width: 1.5, height: 0.8},
      {name: "OUT", x: 0, y: 5.08, shape: "rect", width: 1.5, height: 0.8}
    ],
    outline: {x: -2, y: -2, width: 4, height: 10}
  },
  symbol: {
    pins: [
      {name: "VCC", x: 0, y: 0, length: 5},
      {name: "GND", x: 0, y: -5, length: 5},
      {name: "OUT", x: 10, y: -2.5, length: 5}
    ]
  }
});
```

## 代码示例 (yaml)

```yaml
stackup:
  layer1: {type: signal, name: top, copper: 35um}
  layer2: {type: gnd, name: gnd, copper: 35um}
  layer3: {type: pwr, name: pwr, copper: 35um}
  layer4: {type: signal, name: bottom, copper: 35um}
  prepreg: {thickness: 0.2mm, material: "FR-4"}

stackup_6l:
  layer1: {type: signal, name: top}
  layer2: {type: gnd, name: gnd2}
  layer3: {type: signal, name: sig3}
  layer4: {type: signal, name: sig4}
  layer5: {type: gnd, name: gnd5}
  layer6: {type: signal, name: bottom}

impedance:
  usb_90ohm: {layer: top, width: 0.2, gap: 0.15}
  ethernet_100ohm: {layer: sig3, width: 0.18, gap: 0.18}
```

## 代码示例 (javascript)

```javascript
// 生成打板文件包
await eda.export.manufacturing({
  output_dir: "./manufacturing/",
  files: [
    "gerber_top.gbr",
    "gerber_bottom.gbr",
    "gerber_gnd.gbr",
    "gerber_pwr.gbr",
    "gerber_silk_top.gbr",
    "gerber_silk_bottom.gbr",
    "gerber_mask_top.gbr",
    "gerber_mask_bottom.gbr",
    "drill.txt",
    "pick_place.csv",
    "bom.xlsx"
  ],
  jlcpcb_compatible: true  // 生成嘉立创可直接下单的文件包
});
```

## 代码示例 (text)

```text
library/templates/
├── mcu_minimum/
│   ├── stm32f103/        # STM32F103最小系统模板
│   ├── esp32/            # ESP32最小系统模板
│   └── rp2040/           # RP2040最小系统模板
├── power/
│   ├── usb_c_5v/         # USB-C 5V供电模板
│   ├── ldo_3v3/          # 3.3V LDO模板
│   └── dcdc_12v/         # 12V DC-DC模板
├── interface/
│   ├── uart_usb/         # UART转USB模板
│   ├── ethernet/         # 以太网模板
│   └── can_bus/          # CAN总线模板
└── rf/
    ├── ble_antenna/      # BLE天线模板
    └── wifi_antenna/     # WiFi天线模板
```

## 代码示例 (javascript)

```javascript
// 执行DRC检查
const drcResult = await eda.pcb.runDRC({
  rules: "jlcpcb_default",  // 或自定义规则集
  strict: true
});

// 输出示例
// {
//   "errors": 0,
//   "warnings": 3,
//   "details": [
//     {"type":"silkscreen_overlap", "loc":[25.4,30.2], "severity":"warning"},
//     {"type":"via_drill_small", "loc":[40.1,50.3], "severity":"warning"}
//   ]
// }
```

## 代码示例 (yaml)

```yaml
project:
  name: Industrial_Gateway
  pages: [power, mcu, ethernet, cellular, isolation]
  pcb:
    size: {width: 120, height: 100}
    layers: 4
    stackup: "industrial_4l"
  rules:
    drc: "jlcpcb_industrial"
    erc: ["si", "pi", "emc", "thermal"]
  templates:
    - stm32f103
    - ethernet_lan8720
    - sim7600ce
```

## 代码示例 (yaml)

```yaml
project:
  name: IoT_WiFi_BLE
  pcb:
    layers: 6
    stackup: "high_speed_6l"
    impedance:
      wifi_50ohm: {layer: top, width: 0.2}
      usb_90ohm: {layer: top, width: 0.2, gap: 0.15}
  rf:
    antenna: "pcb_trace"
    matching_network: true
  erc:
    include: ["si", "emc"]
    si_rules: ["length_match", "stub_check"]
```

### 完整搭建（<300秒）
全流程：设计→布局→DRC→BOM→下单：

```javascript
const project = await pcbAssistant.createProject({
  name: "Product_v1",
  config: "project_config.yaml"  // 含完整设计规范
});

// 1. 多页原理图
await pcbAssistant.schematic.design(project.id);

// 2. PCB布局布线
await pcbAssistant.pcb.layout(project.id, "hybrid");
await pcbAssistant.pcb.route(project.id, "diff_aware");

// 3. DRC + ERC
const drc = await pcbAssistant.pcb.runDRC(project.id, {strict: true});
const erc = await pcbAssistant.erc.check(project.id, {include: ["si", "pi", "emc"]});

// 4. BOM生成
const bom = await pcbAssistant.bom.generate(project.id, {check_stock: true});

// 5. 打板文件
await pcbAssistant.export.manufacturing(project.id, {jlcpcb_compatible: true});

// 6. 一键下单（可选）
if (project.config.auto_order) {
  await pcbAssistant.bom.orderToLCSC(project.id);
}
```



