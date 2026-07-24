---
slug: web-artifact-studio
name: web-artifact-studio
version: 1.0.1
displayName: Web工件工作室
summary: "React+Tailwind+shadcn构建复杂交互Web工件,状态路由组件全搞定。Web工件工作室——用现代前端技术栈(React/TypeScript/Tailwind CSS/sha"
license: Proprietary
description: Web工件工作室——用现代前端技术栈(React/TypeScript/Tailwind CSS/shadcn/ui)构建复杂的多组件HTML工件。覆盖状态管理、路由、shadcn/ui
  组件组合、打包交付全流程,支持交互式演示、数据仪表盘、表单工作流、组件展示、单页应用原型。触发关键词:Web工件、HTML工件、React组件、Tailwind、shadcn、ui组件、前端工件、交互组件、单页应用、SPA、组件库、Vite
tags:
  - Web工件
  - React组件
  - 前端开发
  - 交互应用
  - shadcn
  - Web开发
  - 前端
  - 开发工具
  - html
  - tsx
  - import
  - react
  - card
tools:
  - read
  - exec
  - write
  - glob
category: "Development"
---
# Web工件工作室

用现代前端技术栈构建复杂的多组件 HTML 工件。当工件需要状态管理、路由或复杂交互时使用,简单单文件 HTML 不在此范畴。支持 Vite 打包与单文件交付两种模式。

## 核心能力

1. **React + TypeScript 工程化**:Vite 脚手架、目录结构规范、TypeScript 类型安全、props 类型定义
2. **shadcn/ui 组件组合**:Button/Card/Dialog/Table/Form/Navigation 等组件快速组合,主题定制
3. **状态管理分层**:useState(局部)/ Context(跨组件)/ Zustand(全局)/ localStorage(持久化)
4. **路由与多页面**:React Router 路由配置、嵌套路由、动态参数、路由守卫
5. **打包与交付**:Vite 单文件打包(内联 JS/CSS)、图片 base64、无外部依赖可移植

## 快速开始

1. 确认运行环境满足依赖说明中的要求
2. 在AI Agent对话中调用本技能,提供必要的输入参数
3. 检查输出结果,根据需要进行后续处理

> 详细的输入输出格式请参考下方章节说明。

## 适用场景

| 场景 | 输入 | 输出 |
|---|---|---|
| 交互式演示 | 演示需求 + 交互逻辑 | React 应用 + 事件处理 + 可点击演示 |
| 数据仪表盘 | 数据源 + 图表需求 + 过滤器 | 状态管理仪表盘 + 图表 + 交互筛选 |
| 表单工作流 | 表单字段 + 校验规则 + 分步 | 多步表单 + 路由 + 状态校验 |
| 组件展示 | 设计系统/组件库 | shadcn/ui 组件预览 + 代码示例 |
| 单页应用原型 | 页面结构 + 路由 | SPA + 路由 + 状态 + 持久化 |

**不适用于**:
- 简单单文件 HTML(无状态/无路由,直接写 HTML 即可)
- 完整生产级 Web 应用(需要后端、数据库、认证等,使用 Next.js/Nuxt)
- 移动端原生 App(使用 React Native/Flutter)
- 桌面应用(使用 Electron/Tauri)
- 静态文档站点(使用 VitePress/Docusaurus)
- 大型电商网站(需要完整架构,非单工件)

## 使用流程

### Step 1: 需求分析
1. **明确工件目标**:展示什么?交互什么?数据从哪来?
2. **复杂度评估**:
   - 简单展示 → 单文件 HTML 即可
   - 需要状态/路由/多组件 → 使用本工作室
3. **技术选型确认**:React 18 + TypeScript + Tailwind + shadcn/ui
4. **交付模式选择**:Vite 多文件 / 单 HTML 文件(内联)

### Step 2: 项目搭建
1. **目录结构**:
## 输入格式
| 参数名 | 类型 | 必填 | 说明 |
|:-----|:-----|:-----|:-----|
| input | string | 是 | Web工件工作室处理的输入数据或指令 |
| options | object | 否 | 附加配置选项,如模式选择、格式偏好等 |
| callback_url | string | 否 | 异步处理完成后的回调通知URL |

   ```
   artifact/
   ├── index.html          # 入口
   ├── src/
   │   ├── main.tsx        # 挂载点
   │   ├── App.tsx         # 根组件
   │   ├── components/      # 业务组件
   │   ├── ui/              # shadcn/ui 组件
   │   ├── hooks/           # 自定义 Hook
   │   ├── lib/             # 工具函数
   │   └── styles/          # 全局样式
   └── package.json
   ```
2. **依赖引入**:React、Tailwind、shadcn/ui、按需引入图表/路由库
3. **构建配置**:Vite 或内联打包

### Step 3: 组件设计
1. **组件拆分**:按职责拆分,单一职责
2. **shadcn/ui 组合**:优先使用 shadcn/ui 组件(Button/Card/Dialog/Table 等)
3. **状态管理**:
   - 局部状态:useState
   - 跨组件:Context 或 Zustand
   - 持久化:localStorage
4. **路由**:React Router(如需多页面)

### Step 4: 样式与交互
1. **Tailwind 优先**:用工具类,少写自定义 CSS
2. **响应式**:移动优先,sm/md/lg/xl 断点
3. **无障碍**:语义化 HTML、ARIA 标签、键盘导航
4. **动效**:CSS transition / Framer Motion(按需)

### Step 5: 打包与交付
1. **构建产物**:单 HTML 文件(内联 JS/CSS)或多文件
2. **资源处理**:图片转 base64 或 CDN
3. **可移植性**:确保工件可独立运行,无外部依赖
4. **验证**:在浏览器中打开测试,确认功能正常

## 设计原则

1. **组件化**:一切皆组件,可复用可组合
2. **类型安全**:TypeScript,props 有类型定义
3. **无障碍优先**:WCAG 2.1 AA 合规
4. **性能考虑**:懒加载、虚拟列表(长数据)
5. **避免过度工程**:工件不是产品,够用即可

## 示例

### 示例1: 数据仪表盘工件(输入→输出)

**输入**:
```
需求: 销售数据仪表盘
数据: JSON 数组(产品/销售额/地区/月份)
功能: 1) 柱状图展示月度销售 2) 表格展示明细 3) 筛选器按地区过滤
交付: 单 HTML 文件
```

**输出**(目录结构 + 关键代码):
```
artifact/
├── index.html
├── src/
│   ├── main.tsx
│   ├── App.tsx              # 主组件 + 状态
│   ├── components/
│   │   ├── SalesChart.tsx   # 图表组件
│   │   ├── DataTable.tsx    # 表格组件
│   │   └── RegionFilter.tsx # 筛选器
│   └── data/sales.json      # 模拟数据
└── package.json
```

```tsx
// App.tsx 核心代码
import { useState, useMemo } from 'react';
import { Card, CardHeader, CardContent } from '@/ui/card';
import { Select, SelectContent, SelectItem } from '@/ui/select';
import { SalesChart } from './components/SalesChart';
import { DataTable } from './components/DataTable';
import salesData from './data/sales.json';
# ...
export default function App() {
  const [region, setRegion] = useState<string>('all');
# ...
  const filteredData = useMemo(() => {
    if (region === 'all') return salesData;
    return salesData.filter(item => item.region === region);
  }, [region]);
# ...
  return (
    <div className="p-6 space-y-6">
      <h1 className="text-2xl font-bold">销售数据仪表盘</h1>
# ...
      <Select value={region} onValueChange={setRegion}>
        <SelectContent>
          <SelectItem value="all">全部地区</SelectItem>
          <SelectItem value="华东">华东</SelectItem>
          <SelectItem value="华北">华北</SelectItem>
        </SelectContent>
      </Select>
# ...
      <Card>
        <CardHeader>月度销售趋势</CardHeader>
        <CardContent>
          <SalesChart data={filteredData} />
        </CardContent>
      </Card>
# ...
      <Card>
        <CardHeader>销售明细</CardHeader>
        <CardContent>
          <DataTable data={filteredData} />
        </CardContent>
      </Card>
    </div>
  );
}
```

### 示例2: 多步表单工件(输入→输出)

**输入**:
```
需求: 用户注册多步表单
步骤: 1)基本信息 2)联系方式 3)确认提交
校验: 必填、邮箱格式、手机号格式
交付: 单 HTML 文件 + 状态持久化(localStorage)
```

**输出**(关键代码):
```tsx
// MultiStepForm.tsx
import { useState } from 'react';
import { Button } from '@/ui/button';
import { Input } from '@/ui/input';
import { Label } from '@/ui/label';
# ...
const STEPS = ['基本信息', '联系方式', '确认提交'];
# ...
export function MultiStepForm() {
  const [step, setStep] = useState(0);
  const [formData, setFormData] = useState(() => {
    const saved = localStorage.getItem('form-data');
    return saved ? JSON.parse(saved) : { name: '', email: '', phone: '' };
  });
# ...
  const updateField = (field: string, value: string) => {
    const newData = { ...formData, [field]: value };
    setFormData(newData);
    localStorage.setItem('form-data', JSON.stringify(newData));
  };
# ...
  const next = () => step < STEPS.length - 1 && setStep(step + 1);
  const prev = () => step > 0 && setStep(step - 1);
# ...
  return (
    <div className="max-w-md mx-auto p-6">
      <div className="flex gap-2 mb-6">
        {STEPS.map((s, i) => (
          <div key={i} className={`flex-1 h-2 rounded ${i <= step ? 'bg-blue-500' : 'bg-gray-200'}`} />
        ))}
      </div>
# ...
      <h2 className="text-xl font-bold mb-4">{STEPS[step]}</h2>
# ...
      {step === 0 && (
        <div className="space-y-4">
          <div>
            <Label>姓名</Label>
            <Input value={formData.name} onChange={e => updateField('name', e.target.value)} />
          </div>
        </div>
      )}
      {step === 1 && (
        <div className="space-y-4">
          <div>
            <Label>邮箱</Label>
            <Input type="email" value={formData.email} onChange={e => updateField('email', e.target.value)} />
          </div>
          <div>
            <Label>手机号</Label>
            <Input value={formData.phone} onChange={e => updateField('phone', e.target.value)} />
          </div>
        </div>
      )}
      {step === 2 && (
        <div className="space-y-2">
          <p>姓名: {formData.name}</p>
          <p>邮箱: {formData.email}</p>
          <p>手机: {formData.phone}</p>
        </div>
      )}
# ...
      <div className="flex justify-between mt-6">
        <Button variant="outline" onClick={prev} disabled={step === 0}>上一步</Button>
        {step < STEPS.length - 1 ? (
          <Button onClick={next}>下一步</Button>
        ) : (
          <Button onClick={() => alert('提交成功!')}>提交</Button>
        )}
      </div>
    </div>
  );
}
```

### 示例3: 单文件交付构建(输入→输出)

**输入**:
```
需求: 将 React 工件打包为单 HTML 文件,无外部依赖
工具: Vite + vite-plugin-singlefile
```

**输出**(配置代码):
```javascript
// vite.config.ts
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { viteSingleFile } from 'vite-plugin-singlefile';
// ...
export default defineConfig({
  plugins: [react(), viteSingleFile()],
  build: {
    target: 'esnext',
    assetsInlineLimit: 100000000, // 100MB,内联所有资源
    cssCodeSplit: false,
    rollupOptions: {
      output: {
        inlineDynamicImports: true,
      },
    },
  },
});
```

```bash
# 构建命令
npm run build
# 输出: dist/index.html (单文件,可直接打开)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---:|---:|---:|
| Node.js 未安装 | 环境缺少 Node.js | 提示安装 Node.js 18+,提供下载链接 |
| npm install 失败 | 网络问题或权限 | 切换国内镜像 `npm config set registry https://registry.npmmirror.com` |
| shadcn/ui 组件缺失 | 未通过 CLI 添加 | 使用 `npx shadcn-ui@latest add button card dialog` 添加 |
| TypeScript 编译错误 | 类型不匹配 | 检查 props 类型定义,使用 `tsc --noEmit` 校验 |
| Vite 构建失败 | 配置错误或依赖冲突 | 检查 vite.config.ts,清理 node_modules 重装 |
| 单文件打包体积过大 | 内联资源过多 | 使用 CDN 加载 React/Tailwind,仅内联业务代码 |
| Tailwind 样式不生效 | 配置错误或 purge 误删 | 检查 tailwind.config.js content 路径 |
| localStorage 数据丢失 | 浏览器隐私模式 | 添加 try-catch,降级为内存状态 |
| 图表库未引入 | 缺少 recharts/echarts | `npm install recharts` 或使用 SVG 手绘 |
| 路由 404 | 直接打开 HTML 文件路由失效 | 使用 HashRouter 替代 BrowserRouter |

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: Node.js 18+ + npm/pnpm

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 | 国内替代 |
|:---:|:---:|:---:|:---:|:---:|
| Node.js 18+ | 运行时 | 必需 | nodejs.org | npmmirror 国内镜像 |
| React 18 | 库 | 必需 | `npm install react react-dom` | npmmirror |
| TypeScript | 库 | 必需 | `npm install -D typescript` | npmmirror |
| Tailwind CSS | 库 | 必需 | `npm install -D tailwindcss` | npmmirror |
| shadcn/ui | 库 | 必需 | `npx shadcn-ui@latest init` | npmmirror |
| Vite | 工具 | 必需 | `npm install -D vite` | npmmirror |
| React Router | 库 | 可选(多页面) | `npm install react-router-dom` | npmmirror |
| Recharts | 库 | 可选(图表) | `npm install recharts` | npmmirror |
| LLM API | API | 必需 | Agent 内置 LLM | 通义/文心/智谱 |

### API Key 配置
- **本Skill无需额外API Key配置**
- **安全要求**:
  - 工件中不硬编码任何 API Key 或敏感凭证
  - 如需调用外部 API,通过环境变量注入(VITE_ 前缀)
  - 构建产物中不包含 .env 文件

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,需 exec 能力运行 npm/Vite 命令

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 销售数据仪表盘(Zustand全局状态+Recharts图表+筛选器)

**输入**:
```
需求: 销售数据仪表盘工件
数据: JSON数组(产品/销售额/地区/月份/同比增长)
功能:
  1) 柱状图展示月度销售趋势
  2) 数据表格展示明细(支持排序)
  3) 地区筛选器+产品筛选器联动
  4) KPI卡片展示总销售额/平均增长率/最高地区
交付: 单HTML文件(Vite打包)
```

**LLM生成输出** (`output/sales-dashboard/src/App.tsx`):
```tsx
import { useState, useMemo } from 'react';
import { create } from 'zustand';
import { BarChart, Bar, XAxis, YAxis, Tooltip, ResponsiveContainer, CartesianGrid } from 'recharts';
import { Card, CardHeader, CardContent, CardTitle } from '@/ui/card';
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from '@/ui/select';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/ui/table';
import salesData from './data/sales.json';
# ...
// Zustand 全局状态
interface DashboardStore {
  region: string;
  product: string;
  setRegion: (r: string) => void;
  setProduct: (p: string) => void;
}
# ...
const useDashboardStore = create<DashboardStore>((set) => ({
  region: 'all',
  product: 'all',
  setRegion: (r) => set({ region: r }),
  setProduct: (p) => set({ product: p }),
}));
# ...
// KPI 卡片组件
function KPICard({ title, value, subtitle }: { title: string; value: string; subtitle: string }) {
  return (
    <Card>
      <CardHeader><CardTitle className="text-sm text-gray-500">{title}</CardTitle></CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{value}</div>
        <div className="text-xs text-gray-400 mt-1">{subtitle}</div>
      </CardContent>
    </Card>
  );
}
# ...
export default function App() {
  const { region, product, setRegion, setProduct } = useDashboardStore();
# ...
  const filteredData = useMemo(() => {
    return salesData.filter(item =>
      (region === 'all' || item.region === region) &&
      (product === 'all' || item.product === product)
    );
  }, [region, product]);
# ...
  // KPI 计算
  const totalSales = filteredData.reduce((sum, d) => sum + d.amount, 0);
  const avgGrowth = filteredData.length > 0
    ? (filteredData.reduce((sum, d) => sum + d.growthRate, 0) / filteredData.length).toFixed(1)
    : '0';
  const topRegion = useMemo(() => {
    const regionMap: Record<string, number> = {};
    filteredData.forEach(d => { regionMap[d.region] = (regionMap[d.region] || 0) + d.amount; });
    return Object.entries(regionMap).sort((a, b) => b[1] - a[1])[0]?.[0] || '-';
  }, [filteredData]);
# ...
  // 图表数据(按月份聚合)
  const chartData = useMemo(() => {
    const monthMap: Record<string, number> = {};
    filteredData.forEach(d => { monthMap[d.month] = (monthMap[d.month] || 0) + d.amount; });
    return Object.entries(monthMap).map(([month, amount]) => ({ month, amount }));
  }, [filteredData]);
# ...
  return (
    <div className="p-6 space-y-6 max-w-6xl mx-auto">
      <h1 className="text-2xl font-bold">销售数据仪表盘</h1>
# ...
      {/* KPI 卡片 */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        <KPICard title="总销售额" value={`¥${totalSales.toLocaleString()}`} subtitle={`${filteredData.length} 条记录`} />
        <KPICard title="平均增长率" value={`${avgGrowth}%`} subtitle="同比" />
        <KPICard title="最高地区" value={topRegion} subtitle="按销售额" />
      </div>
# ...
      {/* 筛选器 */}
      <div className="flex gap-4">
        <Select value={region} onValueChange={setRegion}>
          <SelectTrigger className="w-40"><SelectValue placeholder="选择地区" /></SelectTrigger>
          <SelectContent>
            <SelectItem value="all">全部地区</SelectItem>
            <SelectItem value="华东">华东</SelectItem>
            <SelectItem value="华北">华北</SelectItem>
            <SelectItem value="华南">华南</SelectItem>
          </SelectContent>
        </Select>
        <Select value={product} onValueChange={setProduct}>
          <SelectTrigger className="w-40"><SelectValue placeholder="选择产品" /></SelectTrigger>
          <SelectContent>
            <SelectItem value="all">全部产品</SelectItem>
            <SelectItem value="产品A">产品A</SelectItem>
            <SelectItem value="产品B">产品B</SelectItem>
            <SelectItem value="产品C">产品C</SelectItem>
          </SelectContent>
        </Select>
      </div>
# ...
      {/* 图表 */}
      <Card>
        <CardHeader><CardTitle>月度销售趋势</CardTitle></CardHeader>
        <CardContent>
          <ResponsiveContainer width="100%" height={300}>
            <BarChart data={chartData}>
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis dataKey="month" />
              <YAxis />
              <Tooltip formatter={(v: number) => `¥${v.toLocaleString()}`} />
              <Bar dataKey="amount" fill="#1a56db" radius={[4, 4, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </CardContent>
      </Card>
# ...
      {/* 数据表格 */}
      <Card>
        <CardHeader><CardTitle>销售明细</CardTitle></CardHeader>
        <CardContent>
          <Table>
            <TableHeader>
              <TableRow>
                <TableHead>产品</TableHead>
                <TableHead>地区</TableHead>
                <TableHead>月份</TableHead>
                <TableHead className="text-right">销售额</TableHead>
                <TableHead className="text-right">增长率</TableHead>
              </TableRow>
            </TableHeader>
            <TableBody>
              {filteredData.map((item, i) => (
                <TableRow key={i}>
                  <TableCell>{item.product}</TableCell>
                  <TableCell>{item.region}</TableCell>
                  <TableCell>{item.month}</TableCell>
                  <TableCell className="text-right">¥{item.amount.toLocaleString()}</TableCell>
                  <TableCell className={`text-right ${item.growthRate >= 0 ? 'text-green-600' : 'text-red-600'}`}>
                    {item.growthRate >= 0 ? '+' : ''}{item.growthRate}%
                  </TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </CardContent>
      </Card>
    </div>
  );
}
```

**效果验证**: ✓Zustand全局状态管理(地区+产品双筛选器) ✓useMemo性能优化(筛选/KPI/图表数据缓存) ✓Recharts柱状图含网格/坐标轴/Tooltip ✓3个KPI卡片(总销售/增长率/最高地区) ✓shadcn/ui Table组件展示明细含正负增长率着色 ✓响应式布局(grid-cols-1 md:grid-cols-3)

### 案例2: 多步注册表单(localStorage持久化+Zod校验+进度条)

**输入**:
```
需求: 用户注册多步表单工件
步骤: 1)基本信息(姓名/年龄) 2)联系方式(邮箱/手机) 3)偏好设置(兴趣/通知) 4)确认提交
校验: 必填/邮箱格式/手机号格式/年龄18-100
特性: localStorage自动保存(刷新不丢数据)+进度条+返回上一步
交付: 单HTML文件
```

**LLM生成输出** (`output/multi-step-form/src/MultiStepForm.tsx`):
```tsx
import { useState, useEffect } from 'react';
import { z } from 'zod';
import { Button } from '@/ui/button';
import { Input } from '@/ui/input';
import { Label } from '@/ui/label';
import { Checkbox } from '@/ui/checkbox';
import { Card, CardContent, CardHeader, CardTitle } from '@/ui/card';
# ...
const STEPS = ['基本信息', '联系方式', '偏好设置', '确认提交'] as const;
# ...
// Zod Schema 定义
const formSchema = z.object({
  name: z.string().min(1, '姓名不能为空'),
  age: z.number().int().min(18, '年龄需18岁以上').max(100, '年龄需100岁以下'),
  email: z.string().email('邮箱格式不正确'),
  phone: z.string().regex(/^1[3-9]\d{9}$/, '手机号格式不正确'),
  interests: z.array(z.string()),
  notifications: z.boolean(),
});
# ...
type FormData = z.infer<typeof formSchema>;
type FormErrors = Partial<Record<keyof FormData, string>>;
# ...
const INTEREST_OPTIONS = ['技术', '设计', '产品', '运营', '市场'];
# ...
export function MultiStepForm() {
  const [step, setStep] = useState(0);
  const [errors, setErrors] = useState<FormErrors>({});
  const [submitted, setSubmitted] = useState(false);
# ...
  // localStorage 持久化
  const [formData, setFormData] = useState<FormData>(() => {
    try {
      const saved = localStorage.getItem('registration-form');
      if (saved) {
        const parsed = JSON.parse(saved);
        return { name: '', age: 0, email: '', phone: '', interests: [], notifications: false, ...parsed };
      }
    } catch (e) { /* 隐私模式降级 */ }
    return { name: '', age: 0, email: '', phone: '', interests: [], notifications: false };
  });
# ...
  // 自动保存
  useEffect(() => {
    try {
      localStorage.setItem('registration-form', JSON.stringify(formData));
    } catch (e) { /* 隐私模式降级 */ }
  }, [formData]);
# ...
  const updateField = <K extends keyof FormData>(field: K, value: FormData[K]) => {
    setFormData(prev => ({ ...prev, [field]: value }));
    setErrors(prev => ({ ...prev, [field]: undefined }));
  };
# ...
  const validateStep = (): boolean => {
    const newErrors: FormErrors = {};
    if (step === 0) {
      if (!formData.name) newErrors.name = '姓名不能为空';
      if (formData.age < 18) newErrors.age = '年龄需18岁以上';
      if (formData.age > 100) newErrors.age = '年龄需100岁以下';
    }
    if (step === 1) {
      if (!formData.email) newErrors.email = '邮箱不能为空';
      else if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(formData.email)) newErrors.email = '邮箱格式不正确';
      if (!formData.phone) newErrors.phone = '手机号不能为空';
      else if (!/^1[3-9]\d{9}$/.test(formData.phone)) newErrors.phone = '手机号格式不正确';
    }
    setErrors(newErrors);
    return Object.keys(newErrors).length === 0;
  };
# ...
  const next = () => {
    if (validateStep()) {
      setStep(s => Math.min(s + 1, STEPS.length - 1));
    }
  };
  const prev = () => setStep(s => Math.max(s - 1, 0));
  const handleSubmit = () => {
    const result = formSchema.safeParse(formData);
    if (result.success) {
      setSubmitted(true);
      localStorage.removeItem('registration-form');
    } else {
      setErrors(Object.fromEntries(
        Object.entries(result.error.flatten().fieldErrors).map(([k, v]) => [k, v?.[0]])
      ) as FormErrors);
    }
  };
# ...
  if (submitted) {
    return (
      <Card className="max-w-md mx-auto mt-10">
        <CardContent className="pt-6 text-center space-y-2">
          <div className="text-4xl">✓</div>
          <h2 className="text-xl font-bold">注册成功!</h2>
          <p className="text-gray-500">欢迎, {formData.name}!</p>
          <Button variant="outline" onClick={() => { setSubmitted(false); setStep(0); }}>
            重新填写
          </Button>
        </CardContent>
      </Card>
    );
  }
# ...
  return (
    <div className="max-w-md mx-auto p-6">
      {/* 进度条 */}
      <div className="flex gap-2 mb-8">
        {STEPS.map((s, i) => (
          <div key={i} className="flex-1">
            <div className={`h-2 rounded transition-colors ${i <= step ? 'bg-blue-600' : 'bg-gray-200'}`} />
            <div className={`text-xs mt-1 text-center ${i === step ? 'font-bold text-blue-600' : 'text-gray-400'}`}>
              {i + 1}. {s}
            </div>
          </div>
        ))}
      </div>
# ...
      <Card>
        <CardHeader><CardTitle>{STEPS[step]}</CardTitle></CardHeader>
        <CardContent className="space-y-4">
          {/* Step 0: 基本信息 */}
          {step === 0 && (
            <>
              <div>
                <Label>姓名 *</Label>
                <Input value={formData.name} onChange={e => updateField('name', e.target.value)} />
                {errors.name && <p className="text-red-500 text-sm mt-1">{errors.name}</p>}
              </div>
              <div>
                <Label>年龄 *</Label>
                <Input type="number" value={formData.age || ''} onChange={e => updateField('age', parseInt(e.target.value) || 0)} />
                {errors.age && <p className="text-red-500 text-sm mt-1">{errors.age}</p>}
              </div>
            </>
          )}
# ...
          {/* Step 1: 联系方式 */}
          {step === 1 && (
            <>
              <div>
                <Label>邮箱 *</Label>
                <Input type="email" value={formData.email} onChange={e => updateField('email', e.target.value)} />
                {errors.email && <p className="text-red-500 text-sm mt-1">{errors.email}</p>}
              </div>
              <div>
                <Label>手机号 *</Label>
                <Input value={formData.phone} onChange={e => updateField('phone', e.target.value)} placeholder="13800138000" />
                {errors.phone && <p className="text-red-500 text-sm mt-1">{errors.phone}</p>}
              </div>
            </>
          )}
# ...
          {/* Step 2: 偏好设置 */}
          {step === 2 && (
            <>
              <div>
                <Label>兴趣领域(可多选)</Label>
                <div className="space-y-2 mt-2">
                  {INTEREST_OPTIONS.map(opt => (
                    <div key={opt} className="flex items-center space-x-2">
                      <Checkbox
                        checked={formData.interests.includes(opt)}
                        onCheckedChange={(checked) => {
                          updateField('interests',
                            checked ? [...formData.interests, opt] : formData.interests.filter(i => i !== opt)
                          );
                        }}
                      />
                      <Label>{opt}</Label>
                    </div>
                  ))}
                </div>
              </div>
              <div className="flex items-center space-x-2">
                <Checkbox checked={formData.notifications} onCheckedChange={(c) => updateField('notifications', !!c)} />
                <Label>接收邮件通知</Label>
              </div>
            </>
          )}
# ...
          {/* Step 3: 确认 */}
          {step === 3 && (
            <div className="space-y-2 text-sm">
              <div><span className="text-gray-500">姓名:</span> {formData.name}</div>
              <div><span className="text-gray-500">年龄:</span> {formData.age}</div>
              <div><span className="text-gray-500">邮箱:</span> {formData.email}</div>
              <div><span className="text-gray-500">手机:</span> {formData.phone}</div>
              <div><span className="text-gray-500">兴趣:</span> {formData.interests.join(', ') || '未选择'}</div>
              <div><span className="text-gray-500">通知:</span> {formData.notifications ? '是' : '否'}</div>
            </div>
          )}
# ...
          {/* 导航按钮 */}
          <div className="flex justify-between pt-4">
            <Button variant="outline" onClick={prev} disabled={step === 0}>上一步</Button>
            {step < STEPS.length - 1 ? (
              <Button onClick={next}>下一步</Button>
            ) : (
              <Button onClick={handleSubmit}>提交注册</Button>
            )}
          </div>
        </CardContent>
      </Card>
    </div>
  );
}
```

**效果验证**: ✓4步表单含进度条+步骤标题 ✓localStorage自动保存(刷新不丢数据)+try-catch隐私模式降级 ✓Zod schema校验+逐步校验(validateStep) ✓邮箱/手机号正则校验+年龄范围校验 ✓提交成功清除localStorage+显示成功页 ✓兴趣多选Checkbox+通知开关

### 案例3: 看板任务管理(拖拽+Context状态+路由)

**输入**:
```
需求: Kanban看板任务管理工件
功能:
  1) 三列: 待办/进行中/已完成
  2) 任务卡片支持拖拽移动列
  3) 添加/删除任务
  4) localStorage持久化
  5) 路由: /kanban(看板) + /tasks/:id(详情)
交付: 单HTML文件(HashRouter)
```

**LLM生成输出** (`output/kanban-board/src/App.tsx`):
```tsx
import { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { HashRouter, Routes, Route, useParams, useNavigate, Link } from 'react-router-dom';
import { Button } from '@/ui/button';
import { Input } from '@/ui/input';
import { Card, CardContent, CardHeader, CardTitle } from '@/ui/card';
# ...
type Status = 'todo' | 'doing' | 'done';
interface Task { id: string; title: string; description: string; status: Status; createdAt: string; }
# ...
// Context 状态管理
interface KanbanContextType {
  tasks: Task[];
  addTask: (title: string) => void;
  deleteTask: (id: string) => void;
  moveTask: (id: string, status: Status) => void;
  getTask: (id: string) => Task | undefined;
}
# ...
const KanbanContext = createContext<KanbanContextType | null>(null);
const useKanban = () => useContext(KanbanContext)!;
# ...
function KanbanProvider({ children }: { children: ReactNode }) {
  const [tasks, setTasks] = useState<Task[]>(() => {
    try {
      const saved = localStorage.getItem('kanban-tasks');
      return saved ? JSON.parse(saved) : [];
    } catch { return []; }
  });
# ...
  useEffect(() => {
    try { localStorage.setItem('kanban-tasks', JSON.stringify(tasks)); } catch {}
  }, [tasks]);
# ...
  const addTask = (title: string) => {
    setTasks(prev => [...prev, {
      id: `task-${Date.now()}`, title, description: '', status: 'todo', createdAt: new Date().toISOString(),
    }]);
  };
  const deleteTask = (id: string) => setTasks(prev => prev.filter(t => t.id !== id));
  const moveTask = (id: string, status: Status) =>
    setTasks(prev => prev.map(t => t.id === id ? { ...t, status } : t));
  const getTask = (id: string) => tasks.find(t => t.id === id);
# ...
  return (
    <KanbanContext.Provider value={{ tasks, addTask, deleteTask, moveTask, getTask }}>
      {children}
    </KanbanContext.Provider>
  );
}
# ...
// 看板视图
function KanbanBoard() {
  const { tasks, addTask, deleteTask, moveTask } = useKanban();
  const [newTitle, setNewTitle] = useState('');
  const [draggedId, setDraggedId] = useState<string | null>(null);
# ...
  const columns: { status: Status; label: string; color: string }[] = [
    { status: 'todo', label: '待办', color: 'bg-gray-100' },
    { status: 'doing', label: '进行中', color: 'bg-blue-50' },
    { status: 'done', label: '已完成', color: 'bg-green-50' },
  ];
# ...
  const handleAdd = () => {
    if (newTitle.trim()) { addTask(newTitle.trim()); setNewTitle(''); }
  };
# ...
  const handleDrop = (status: Status) => {
    if (draggedId) { moveTask(draggedId, status); setDraggedId(null); }
  };
# ...
  return (
    <div className="p-6">
      <h1 className="text-2xl font-bold mb-6">任务看板</h1>
# ...
      {/* 添加任务 */}
      <div className="flex gap-2 mb-6">
        <Input value={newTitle} onChange={e => setNewTitle(e.target.value)}
          onKeyDown={e => e.key === 'Enter' && handleAdd()}
          placeholder="输入任务标题..." className="flex-1" />
        <Button onClick={handleAdd}>添加</Button>
      </div>
# ...
      {/* 三列看板 */}
      <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
        {columns.map(col => (
          <div key={col.status}
            className={`${col.color} rounded-lg p-4 min-h-[300px]`}
            onDragOver={e => e.preventDefault()}
            onDrop={() => handleDrop(col.status)}>
            <h2 className="font-bold mb-3">{col.label} ({tasks.filter(t => t.status === col.status).length})</h2>
            <div className="space-y-2">
              {tasks.filter(t => t.status === col.status).map(task => (
                <Card key={task.id} draggable
                  onDragStart={() => setDraggedId(task.id)}
                  className="cursor-move hover:shadow-md transition-shadow">
                  <CardContent className="pt-3 pb-3">
                    <Link to={`/tasks/${task.id}`} className="font-medium hover:text-blue-600">
                      {task.title}
                    </Link>
                    <div className="flex gap-1 mt-2">
                      <Button size="sm" variant="ghost" onClick={() => deleteTask(task.id)}>删除</Button>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
# ...
// 任务详情页
function TaskDetail() {
  const { id } = useParams();
  const { getTask, moveTask, deleteTask } = useKanban();
  const navigate = useNavigate();
  const task = id ? getTask(id) : undefined;
# ...
  if (!task) {
    return <div className="p-6"><p>任务不存在</p><Link to="/kanban"><Button>返回看板</Button></Link></div>;
  }
# ...
  return (
    <div className="p-6 max-w-2xl mx-auto">
      <Link to="/kanban" className="text-blue-600 mb-4 inline-block">← 返回看板</Link>
      <Card>
        <CardHeader><CardTitle>{task.title}</CardTitle></CardHeader>
        <CardContent className="space-y-4">
          <div>
            <span className="text-gray-500 text-sm">创建时间:</span>
            <span className="ml-2">{new Date(task.createdAt).toLocaleString()}</span>
          </div>
          <div>
            <span className="text-gray-500 text-sm">状态:</span>
            <span className="ml-2 font-medium">{task.status === 'todo' ? '待办' : task.status === 'doing' ? '进行中' : '已完成'}</span>
          </div>
          <div className="flex gap-2">
            <Button size="sm" variant="outline" onClick={() => moveTask(task.id, 'todo')}>移到待办</Button>
            <Button size="sm" variant="outline" onClick={() => moveTask(task.id, 'doing')}>移到进行中</Button>
            <Button size="sm" variant="outline" onClick={() => moveTask(task.id, 'done')}>移到已完成</Button>
          </div>
          <Button variant="destructive" size="sm" onClick={() => { deleteTask(task.id); navigate('/kanban'); }}>
            删除任务
          </Button>
        </CardContent>
      </Card>
    </div>
  );
}
# ...
export default function App() {
  return (
    <KanbanProvider>
      <HashRouter>
        <Routes>
          <Route path="/kanban" element={<KanbanBoard />} />
          <Route path="/tasks/:id" element={<TaskDetail />} />
          <Route path="*" element={<KanbanBoard />} />
        </Routes>
      </HashRouter>
    </KanbanProvider>
  );
}
```

**效果验证**: ✓Context+useState状态管理(task CRUD) ✓HTML5拖拽API(draggable+onDragStart+onDrop) ✓HashRouter路由(看板+详情页,兼容单文件) ✓localStorage持久化+try-catch降级 ✓三列看板含任务计数 ✓详情页支持状态移动+删除+返回

### 案例4: shadcn/ui组件展示画廊(代码预览+主题切换)

**输入**:
```
需求: shadcn/ui 组件展示画廊工件
功能:
  1) 展示Button/Input/Card/Dialog/Table/Badge等组件
  2) 每个组件含代码片段(可复制)
  3) 暗色/亮色主题切换
  4) 组件分类导航
交付: 单HTML文件
```

**LLM生成输出** (`output/component-gallery/src/App.tsx`):
```tsx
import { useState } from 'react';
import { Button } from '@/ui/button';
import { Input } from '@/ui/input';
import { Card, CardContent, CardHeader, CardTitle, CardDescription } from '@/ui/card';
import { Badge } from '@/ui/badge';
import { Dialog, DialogContent, DialogTrigger, DialogHeader, DialogTitle } from '@/ui/dialog';
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from '@/ui/table';
# ...
// 代码展示组件
function CodeBlock({ code }: { code: string }) {
  const [copied, setCopied] = useState(false);
  const copy = () => {
    navigator.clipboard.writeText(code);
    setCopied(true);
    setTimeout(() => setCopied(false), 2000);
  };
  return (
    <div className="relative">
      <pre className="bg-gray-900 text-gray-100 p-4 rounded-md text-sm overflow-x-auto">
        <code>{code}</code>
      </pre>
      <button onClick={copy}
        className="absolute top-2 right-2 px-2 py-1 bg-gray-700 text-white rounded text-xs hover:bg-gray-600">
        {copied ? '已复制!' : '复制'}
      </button>
    </div>
  );
}
# ...
// 组件展示卡片
function ComponentShowcase({ title, description, children, code }: {
  title: string; description: string; children: React.ReactNode; code: string;
}) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>{title}</CardTitle>
        <CardDescription>{description}</CardDescription>
      </CardHeader>
      <CardContent className="space-y-4">
        <div className="p-4 border rounded-md bg-gray-50 dark:bg-gray-900 flex flex-wrap gap-3 items-center">
          {children}
        </div>
        <CodeBlock code={code} />
      </CardContent>
    </Card>
  );
}
# ...
export default function App() {
  const [dark, setDark] = useState(false);
# ...
  return (
    <div className={dark ? 'dark' : ''}>
      <div className="min-h-screen bg-white dark:bg-gray-950 text-gray-900 dark:text-gray-100 p-6">
        <div className="flex justify-between items-center mb-8">
          <h1 className="text-2xl font-bold">shadcn/ui 组件画廊</h1>
          <Button variant="outline" onClick={() => setDark(!dark)}>
            {dark ? '☀️ 亮色' : '🌙 暗色'}
          </Button>
        </div>
# ...
        <div className="space-y-6 max-w-4xl mx-auto">
          {/* Button */}
          <ComponentShowcase
            title="Button" description="多种变体与尺寸的按钮组件"
            code={`<Button>默认</Button>\n<Button variant="outline">轮廓</Button>\n<Button variant="destructive">危险</Button>\n<Button size="sm">小</Button>`}>
            <Button>默认</Button>
            <Button variant="outline">轮廓</Button>
            <Button variant="destructive">危险</Button>
            <Button variant="secondary">次要</Button>
            <Button size="sm">小尺寸</Button>
            <Button size="lg">大尺寸</Button>
          </ComponentShowcase>
# ...
          {/* Badge */}
          <ComponentShowcase
            title="Badge" description="标签徽章组件"
            code={`<Badge>默认</Badge>\n<Badge variant="secondary">次要</Badge>\n<Badge variant="destructive">错误</Badge>\n<Badge variant="outline">轮廓</Badge>`}>
            <Badge>默认</Badge>
            <Badge variant="secondary">次要</Badge>
            <Badge variant="destructive">错误</Badge>
            <Badge variant="outline">轮廓</Badge>
          </ComponentShowcase>
# ...
          {/* Input */}
          <ComponentShowcase
            title="Input" description="输入框组件"
            code={`<Input placeholder="请输入..." />\n<Input type="email" placeholder="邮箱" />\n<Input type="password" placeholder="密码" />`}>
            <Input placeholder="默认输入" className="w-48" />
            <Input type="email" placeholder="邮箱" className="w-48" />
            <Input type="password" placeholder="密码" className="w-48" />
          </ComponentShowcase>
# ...
          {/* Dialog */}
          <ComponentShowcase
            title="Dialog" description="对话框/弹窗组件"
            code={`<Dialog>\n  <DialogTrigger asChild>\n    <Button>打开弹窗</Button>\n  </DialogTrigger>\n  <DialogContent>\n    <DialogHeader>\n      <DialogTitle>标题</DialogTitle>\n    </DialogHeader>\n    <p>内容</p>\n  </DialogContent>\n</Dialog>`}>
            <Dialog>
              <DialogTrigger asChild>
                <Button variant="outline">打开弹窗</Button>
              </DialogTrigger>
              <DialogContent>
                <DialogHeader><DialogTitle>弹窗标题</DialogTitle></DialogHeader>
                <p className="text-gray-500">这是一个对话框示例,点击外部或关闭按钮可关闭。</p>
                <div className="flex justify-end gap-2 mt-4">
                  <Button variant="outline">取消</Button>
                  <Button>确认</Button>
                </div>
              </DialogContent>
            </Dialog>
          </ComponentShowcase>
# ...
          {/* Table */}
          <ComponentShowcase
            title="Table" description="数据表格组件"
            code={`<Table>\n  <TableHeader><TableRow><TableHead>姓名</TableHead></TableRow></TableHeader>\n  <TableBody><TableRow><TableCell>张三</TableCell></TableRow></TableBody>\n</Table>`}>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>姓名</TableHead>
                  <TableHead>角色</TableHead>
                  <TableHead>状态</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                <TableRow>
                  <TableCell>张三</TableCell>
                  <TableCell>开发者</TableCell>
                  <TableCell><Badge variant="secondary">在线</Badge></TableCell>
                </TableRow>
                <TableRow>
                  <TableCell>李四</TableCell>
                  <TableCell>设计师</TableCell>
                  <TableCell><Badge variant="outline">离线</Badge></TableCell>
                </TableRow>
              </TableBody>
            </Table>
          </ComponentShowcase>
        </div>
      </div>
    </div>
  );
}
```

**效果验证**: ✓6种shadcn/ui组件展示(Button/Badge/Input/Dialog/Table/Card) ✓每个组件含实时预览+可复制代码块 ✓暗色/亮色主题切换(dark class) ✓CodeBlock组件含clipboard复制+反馈提示 ✓Table中嵌套Badge展示组件组合 ✓响应式flex-wrap布局

## 常见问题

### Q1: 什么时候用单文件 HTML,什么时候用本工作室?
A: 按复杂度判断:
- **单文件 HTML**: 静态展示、简单交互、无状态管理、无路由 → 直接写 HTML
- **Web工件工作室**: 需要状态管理、多组件、路由、复杂数据流 → 使用 React 工程化
- 简单的内容用 React 是过度工程;复杂的内容用纯 HTML 难以维护

### Q2: 如何选择状态管理方案?
A: 按复杂度递增:
- **useState**: 单组件内状态(最简单)
- **Context + useReducer**: 跨组件共享,中等复杂度
- **Zustand**: 全局状态,API 简洁,推荐用于工件
- **Redux Toolkit**: 大型应用,工件不推荐(过度工程)
- **Jotai/Recoil**: 原子化状态,适合细粒度依赖
- 工件推荐:useState + Zustand(全局)+ localStorage(持久化)

### Q3: 单文件打包后体积太大怎么办?
A: 优化策略:
1. **CDN 加载 React/Tailwind**:不内联框架代码,仅内联业务代码
2. **Tree Shaking**:确保 import 具体组件(`import { Button } from 'ui/button'`)
3. **代码分割**:路由级懒加载(React.lazy + Suspense)
4. **压缩**:开启 gzip/brotli 压缩
5. **图片优化**:WebP 格式 + 懒加载
6. **移除未使用依赖**:检查 bundle analyzer

### Q4: 工件能在没有 Node.js 的环境运行吗?
A: 可以,只要打包为单 HTML 文件:
- Vite + vite-plugin-singlefile 打包后,产物是单个 index.html
- 所有 JS/CSS 内联,图片转 base64
- 直接用浏览器打开即可运行,无需 Node.js 或服务器
- 适合分发、嵌入、演示

## 已知限制

- 不适用于完整生产级 Web 应用(需要后端/数据库/认证)
- 单文件打包体积可能较大(React + Tailwind 基础约 200KB+)
- 不涉及 SSR/SSG(使用 Next.js/Nuxt)
- 不覆盖移动端原生 App(使用 React Native/Flutter)
- 不涉及桌面应用(使用 Electron/Tauri)
- 国内安装 npm 依赖可能较慢,建议配置 npmmirror 镜像
- 不涉及复杂的后端 API 开发(仅前端工件)

## 安全声明

- 工件中不硬编码任何 API Key/密码/凭证
- 调用外部 API 时使用环境变量注入(VITE_API_KEY)
- 构建产物(dist/)不包含 .env 文件或敏感配置
- 用户输入需做 XSS 防护(React 默认转义,避免 dangerouslySetInnerHTML)
- 不在工件中存储用户敏感数据(localStorage 仅存非敏感偏好)
- 第三方依赖定期审计(`npm audit`)
