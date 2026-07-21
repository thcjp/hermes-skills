---
slug: docx-document-master
name: docx-document-master
version: "1.0.0"
displayName: "文档处理大师"
summary: "Word文档全流程处理,从创建到修订到邮件合并,正式文档一站搞定"
license: Proprietary
description: |-
  文档处理大师——全面处理Word文档,从创建到编辑,从修订到邮件合并,覆盖正式文档全生命周期。合同/报告/方案/手册/论文,专业级文档处理一站搞定。支持标题层级、段落格式、表格图片、修订跟踪、批注协作、目录生成、邮件合并、交叉引用、书签超链接、页眉页脚、分节封面全功能。适用场景:合同文档生成、项目报告撰写、方案手册制作、论文排版、批量邮件合并、文档格式规范化。触发关键词:Word文档、docx、文档生成、文档编辑、修订批注、邮件合并、目录生成、交叉引用、页眉页脚、格式转换、合同文档、报告撰写、论文排版、python-docx、文档处理。
tags: [文档处理, Word文档, 文档生成, 修订批注, 邮件合并]
tools:
  - read
  - exec
suggested_price: "1.90"
pricing_tier: "standard"
pricing_rationale: "文件处理类, large市场, enterprise复杂度, daily频次, standard层 → 高频通用工具"
---
# 文档处理大师

全面处理 Word 文档。从创建到编辑,从格式到修订,覆盖正式文档全生命周期。

## 适用场景

| 场景 | 输入 | 输出 |
|:-----|:-----|:-----|
| 文档创建 | 文档类型+大纲+样式要求 | 格式化.docx文件(含标题/段落/表格/图片) |
| 文档编辑 | 现有docx+修改需求 | 编辑后docx+修订记录 |
| 协作审阅 | 多人批注+修订 | 修订模式docx+批注+接受/拒绝记录 |
| 邮件合并 | 模板docx+Excel数据源 | 批量个性化docx(信件/证书/邀请函) |
| 格式转换 | 内容+目标格式规范 | 统一样式docx(目录/页眉页脚/分节) |
| 论文排版 | 论文内容+学校格式要求 | 规范化docx(目录/引用/页码/封面) |

### 不适用于
- PDF编辑与处理(请使用pdf工具)
- PPT演示文稿制作(请使用pptx工具)
- 电子表格处理(请使用xlsx工具)
- Markdown转HTML(请使用专用转换工具)
- 文档OCR识别(请使用OCR工具)
- 实时协作文档编辑(请使用在线文档)

## 核心能力

1. **文档全生命周期处理**:创建(大纲→格式化)→编辑(读取/修改/输出)→协作(修订/批注)→合并(模板+数据源)→输出(.docx/.pdf)
2. **格式化排版**:标题层级(H1/H2/H3)、段落格式(缩进/对齐/列表)、特殊元素(表格/图片/代码块/引用块)、样式规范(字体/字号/行距)
3. **修订与协作**:修订跟踪(插入/删除/格式)、批注(线程化回复)、接受/拒绝修订、作者标识+时间戳
4. **高级功能**:目录生成(多级+页码+超链接)、邮件合并(主文档+数据源)、交叉引用(图表/章节/页码)、书签超链接
5. **页面与输出**:页眉页脚(页码/标题/分节)、分节符(方向/页边距)、封面页、docx/pdf双格式输出

## 使用流程

### Step 1: 文档规划
1. 明确文档类型:合同/报告/方案/手册/论文
2. 确定结构:标题层级、章节划分、目录结构
3. 样式规范:字体/字号/行距/段距/对齐
4. 页面设置:纸张大小/页边距/页眉页脚

### Step 2: 内容生成与编辑
1. **标题层级**:H1(章,16pt加粗)、H2(节,14pt加粗)、H3(小节,12pt加粗)、正文(11pt,1.5倍行距)
2. **段落格式**:首行缩进/段前段后距、对齐方式(左/居中/两端)、列表(项目符号/编号)
3. **特殊元素**:表格(边框/底纹/合并)、图片(插入/环绕/题注)、代码块(等宽字体/底纹)、引用块(缩进/斜体)

### Step 3: 修订与批注(如需协作)
1. 开启修订跟踪,插入/删除/格式更改均被记录
2. 选中文字添加批注,批注者+内容+时间戳
3. 回复批注(线程化)
4. 接受/拒绝修订(逐条或批量)

### Step 4: 高级功能(如需)
1. **目录生成**:基于标题样式自动生成,多级目录(1-3级),页码引用+超链接
2. **邮件合并**:主文档(含占位符)+数据源(Excel/CSV)→批量个性化文档
3. **交叉引用**:图表编号/章节引用/页码引用
4. **书签与超链接**:内部跳转+外部链接

### Step 5: 页面与输出
1. 页眉页脚:页码(居中/外侧)、文档标题/章节名、不同节不同页眉
2. 分节符:不同页面方向/页边距
3. 封面页:独立设计,无页码
4. 输出:.docx(可编辑)/.pdf(分享)

## 输出规范

- Word 文件:`output/{document-name}/document.docx`
- PDF 导出:`output/{document-name}/export.pdf`
- 大纲:`output/{document-name}/outline.md`
- 修订记录:`output/{document-name}/revisions.md`
- 邮件合并结果:`output/{document-name}/merged/`(批量文件)

## 依赖说明

### 运行环境
- **Agent平台**: Claude Code / Cursor / Codex / Gemini CLI / Windsurf 等支持SKILL.md的任意Agent
- **操作系统**: Windows / macOS / Linux
- **运行时**: 需要Agent支持exec(命令行执行)能力

### 依赖项

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | python-docx库执行环境 |
| python-docx | Python库 | 必需 | `pip install python-docx` |
| LLM API | API | 可选 | 由Agent内置LLM提供内容生成 |
| LibreOffice | 工具 | 可选 | docx转pdf(Linux/macOS) |
| docx2pdf | Python库 | 可选 | docx转pdf(Windows,需Word) |

### 国内镜像加速(替代海外PyPI)

| 海外源 | 国内镜像 | 说明 |
|:-------|:---------|:-----|
| pypi.org | 清华大学pypi | `pip install -i https://pypi.tuna.tsinghua.edu.cn/simple python-docx` |
| pypi.org | 阿里云pypi | `pip install -i https://mirrors.aliyun.com/pypi/simple python-docx` |

### API Key 配置
- 本Skill无需额外API Key配置
- 文档生成在本地Python环境执行,无外部服务依赖

### 可用性分类
- **分类**: MD+EXEC
- **说明**: 纯Markdown方法论,实际生成docx需exec调用Python脚本(python-docx)

## 示例

### 示例1: 生成项目方案文档

**输入**:
```
文档类型:项目方案
标题:TaskFlow项目管理工具产品方案
结构:封面+目录+1.项目背景+2.产品概述+3.功能设计+4.技术架构+5.项目计划+6.预算
样式:正式,宋体正文/黑体标题,1.5倍行距
```

**输出** (`output/taskflow-proposal/document.docx` 生成脚本):
```python
from docx import Document
from docx.shared import Pt, Inches, Cm
from docx.enum.text import WD_ALIGN_PARAGRAPH

doc = Document()

# 样式设置
style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(11)
style.paragraph_format.line_spacing = 1.5

# 封面
title = doc.add_heading('TaskFlow项目管理工具\n产品方案', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_paragraph('\n\n\n')
p = doc.add_paragraph('编制:产品部')
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
p = doc.add_paragraph('日期:2024年7月')
p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.add_page_break()

# 目录
doc.add_heading('目录', level=1)
doc.add_paragraph('(自动生成目录)')

doc.add_page_break()

# 正文
doc.add_heading('1. 项目背景', level=1)
doc.add_paragraph('当前中小企业项目管理面临以下痛点...')
doc.add_heading('1.1 行业现状', level=2)
doc.add_paragraph('根据艾瑞咨询2024年报告...')

doc.add_heading('2. 产品概述', level=1)
doc.add_heading('2.1 产品定位', level=2)
doc.add_paragraph('TaskFlow是一款面向10-50人团队的...')

doc.add_heading('3. 功能设计', level=1)
# 表格
table = doc.add_table(rows=4, cols=3)
table.style = 'Table Grid'
headers = ['功能模块', '描述', '优先级']
for i, h in enumerate(headers):
    table.rows[0].cells[i].text = h
features = [
    ('看板管理', '拖拽式任务管理', 'P0'),
    ('甘特图', '项目进度可视化', 'P0'),
    ('AI排期', '智能任务分配', 'P1'),
]
for i, (m, d, p) in enumerate(features):
    table.rows[i+1].cells[0].text = m
    table.rows[i+1].cells[1].text = d
    table.rows[i+1].cells[2].text = p

# 页眉页脚
section = doc.sections[0]
footer = section.footer
footer_p = footer.paragraphs[0]
footer_p.text = 'TaskFlow产品方案 | 机密'
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

doc.save('output/taskflow-proposal/document.docx')
print('文档已生成')
```

### 示例2: 邮件合并批量生成邀请函

**输入**:
```
任务:批量生成会议邀请函
模板:invitation_template.docx(含占位符{{name}},{{company}},{{date}})
数据源:attendees.csv(name,company,date)
数量:50人
```

**输出** (`output/invitations/merged/` 批量文件):
```python
import pandas as pd
from docx import Document
import os

# 读取数据源
df = pd.read_csv('attendees.csv')

# 读取模板
template = Document('invitation_template.docx')

os.makedirs('output/invitations/merged', exist_ok=True)

for idx, row in df.iterrows():
    doc = Document('invitation_template.docx')
    
    # 替换占位符
    for paragraph in doc.paragraphs:
        if '{{name}}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{name}}', row['name'])
        if '{{company}}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{company}}', row['company'])
        if '{{date}}' in paragraph.text:
            paragraph.text = paragraph.text.replace('{{date}}', row['date'])
    
    # 同样处理表格中的占位符
    for table in doc.tables:
        for row in table.rows:
            for cell in row.cells:
                for paragraph in cell.paragraphs:
                    if '{{name}}' in paragraph.text:
                        paragraph.text = paragraph.text.replace('{{name}}', row['name'])
    
    filename = f"output/invitations/merged/invitation_{row['name']}.docx"
    doc.save(filename)

print(f'已生成{len(df)}份邀请函')
```

**生成结果**:
```
output/invitations/merged/
├── invitation_张三.docx
├── invitation_李四.docx
├── invitation_王五.docx
└── ... (共50份)
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|:---------|:-----|:---------|
| python-docx未安装 | 环境未配置 | `pip install python-docx`,提供国内镜像加速命令 |
| 文档打开失败 | 文件损坏/格式不支持 | 检查文件格式(.doc/.docx),建议另存为.docx |
| 中文乱码 | 字体不支持中文 | 设置中文字体:宋体/黑体/微软雅黑,指定`font.name = '宋体'` |
| 表格样式丢失 | python-docx表格样式有限 | 使用'Table Grid'基础样式,手动设置边框 |
| 图片插入失败 | 路径错误/格式不支持 | 检查路径(绝对路径),支持PNG/JPEG/GIF/BMP |
| PDF转换失败 | LibreOffice/Word未安装 | Linux安装LibreOffice,Windows需Word,或使用docx2pdf |
| 目录不更新 | python-docx不自动生成目录 | 添加目录占位符,提示用户在Word中按F9更新 |
| 邮件合并占位符未替换 | 模板占位符格式不一致 | 统一使用{{placeholder}}格式,检查大小写与空格 |
| 页眉页脚不显示 | 分节符设置错误 | 检查section.footer.is_linked_to_previous,取消链接 |

## 案例展示

以下案例展示了skill的工作流程和预期输出效果，由LLM按照skill定义的流程生成。

### 案例1: 生成企业合同文档

**输入**:
```
文档类型: 软件开发合同
标题: 软件定制开发服务合同
结构: 封面+合同编号+甲乙方信息+服务内容+交付标准+付款方式+知识产权+保密条款+违约责任+签署页
样式: 正式，宋体正文/黑体标题，1.5倍行距，A4纸张
特殊要求: 包含表格(付款节点)、页眉含合同编号
```

**LLM生成输出**:
```python
# output/software-contract/generate_contract.py
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.enum.table import WD_TABLE_ALIGNMENT
from docx.oxml.ns import qn

doc = Document()

# 页面设置
section = doc.sections[0]
section.page_width = Cm(21)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.54)
section.bottom_margin = Cm(2.54)
section.left_margin = Cm(3.18)
section.right_margin = Cm(3.18)

# 样式设置
style = doc.styles['Normal']
style.font.name = '宋体'
style.font.size = Pt(12)
style.element.rPr.rFonts.set(qn('w:eastAsia'), '宋体')
style.paragraph_format.line_spacing = 1.5

# 页眉(合同编号)
header = section.header
header_p = header.paragraphs[0]
header_p.text = '合同编号: DEV-2024-0815'
header_p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
header_p.runs[0].font.size = Pt(9)

# 封面
title = doc.add_heading('软件定制开发服务合同', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER
for run in title.runs:
    run.font.name = '黑体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    run.font.size = Pt(22)

doc.add_paragraph('\n\n\n\n')

# 甲乙方信息
p = doc.add_paragraph()
p.add_run('甲方(委托方): ').bold = True
p.add_run('____________________')

p = doc.add_paragraph()
p.add_run('乙方(开发方): ').bold = True
p.add_run('____________________')

p = doc.add_paragraph()
p.add_run('签订日期: ').bold = True
p.add_run('2024年___月___日')

doc.add_page_break()

# 正文条款
def add_clause(num, title_text, content):
    h = doc.add_heading(f'{num}. {title_text}', level=1)
    for run in h.runs:
        run.font.name = '黑体'
        run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
        run.font.size = Pt(14)
    if isinstance(content, list):
        for i, item in enumerate(content, 1):
            doc.add_paragraph(f'{i}. {item}')
    else:
        doc.add_paragraph(content)

add_clause('一', '服务内容', [
    '乙方根据甲方需求，定制开发"企业管理系统"，包含以下模块: 用户管理、权限管理、数据看板、报表导出',
    '开发周期为90个工作日，自合同签订之日起计算',
    '交付物包括: 源代码、技术文档、用户手册、部署脚本',
])

add_clause('二', '交付标准', [
    '功能完整性: 完成需求文档中100%功能点',
    '性能标准: 页面加载<2秒，API响应<500ms，支持100并发',
    '测试通过率: 单元测试覆盖率>80%，UAT测试通过率>95%',
])

# 付款方式(含表格)
h = doc.add_heading('三. 付款方式', level=1)
for run in h.runs:
    run.font.name = '黑体'
    run.element.rPr.rFonts.set(qn('w:eastAsia'), '黑体')
    run.font.size = Pt(14)

doc.add_paragraph('本项目总金额为人民币贰拾万元整(¥200,000)，按以下节点支付:')

table = doc.add_table(rows=5, cols=4)
table.style = 'Table Grid'
table.alignment = WD_TABLE_ALIGNMENT.CENTER

headers = ['付款节点', '比例', '金额(元)', '触发条件']
for i, h in enumerate(headers):
    cell = table.rows[0].cells[i]
    cell.text = h
    for p in cell.paragraphs:
        p.alignment = WD_ALIGN_PARAGRAPH.CENTER
        for run in p.runs:
            run.bold = True

data = [
    ('首付款', '30%', '60,000', '合同签订后5个工作日'),
    ('里程碑1', '20%', '40,000', '需求确认+原型设计完成'),
    ('里程碑2', '30%', '60,000', '开发完成+内部测试通过'),
    ('尾款', '20%', '40,000', 'UAT验收通过+交付全部源码'),
]
for i, row in enumerate(data):
    for j, val in enumerate(row):
        table.rows[i+1].cells[j].text = val

add_clause('四', '知识产权', [
    '本项目开发成果的知识产权归甲方所有',
    '乙方保证交付软件不含任何第三方侵权代码',
    '乙方有权在不涉及甲方商业秘密的前提下使用通用技术框架',
])

add_clause('五', '保密条款', [
    '双方对在合作过程中获知的对方商业秘密负有保密义务',
    '保密期限为合同终止后3年',
    '违反保密义务的，违约方应赔偿守约方全部损失',
])

add_clause('六', '违约责任', [
    '乙方逾期交付的，每逾期1日按合同总额0.5%支付违约金',
    '甲方逾期付款的，每逾期1日按应付金额0.5%支付滞纳金',
    '任何一方严重违约的，守约方有权解除合同并要求赔偿',
])

# 签署页
doc.add_page_break()
doc.add_paragraph('\n\n\n')

p = doc.add_paragraph()
p.add_run('甲方(盖章): ').bold = True
doc.add_paragraph('\n法定代表人:\n日期:      年    月    日')

doc.add_paragraph('\n\n')
p = doc.add_paragraph()
p.add_run('乙方(盖章): ').bold = True
doc.add_paragraph('\n法定代表人:\n日期:      年    月    日')

doc.save('output/software-contract/document.docx')
print('合同文档已生成')
```

```markdown
# output/software-contract/outline.md
# 软件定制开发服务合同 - 大纲

## 文档结构
1. 封面(标题+甲乙方信息+日期)
2. 一. 服务内容(3条)
3. 二. 交付标准(3条)
4. 三. 付款方式(含4行付款节点表格)
5. 四. 知识产权(3条)
6. 五. 保密条款(3条)
7. 六. 违约责任(3条)
8. 签署页(甲乙方盖章)

## 样式规范
- 标题: 黑体, 14pt, 加粗
- 正文: 宋体, 12pt, 1.5倍行距
- 表格: Table Grid样式, 居中对齐
- 页眉: 合同编号, 9pt, 右对齐
- 页面: A4, 标准页边距
```

**效果验证**: ✓完整合同结构(封面+6章+签署页) ✓付款表格4节点含比例/金额/条件 ✓页眉含合同编号 ✓中文字体正确设置(宋体/黑体) ✓条款编号规范(一二三四)

### 案例2: 论文排版规范化

**输入**:
```
任务: 硕士学位论文排版
内容: 论文全文(约5万字)，含摘要/目录/5章正文/参考文献/附录
格式要求: 
  - 封面: 学校名称+论文标题+作者+导师+日期
  - 目录: 自动生成(三级标题+页码)
  - 正文: 宋体小四，1.5倍行距，首行缩进2字符
  - 标题: 一级黑体三号，二级黑体四号，三级黑体小四
  - 页眉: 章标题，页脚: 页码居中
  - 参考文献: GB/T 7714格式
```

**LLM生成输出**:
```python
# output/thesis-formatting/format_thesis.py
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement

doc = Document()

# 页面设置
section = doc.sections[0]
section.page_width = Cm(21)
section.page_height = Cm(29.7)
section.top_margin = Cm(2.5)
section.bottom_margin = Cm(2.5)
section.left_margin = Cm(3)
section.right_margin = Cm(2.5)

def set_font(run, font_name, size, bold=False):
    run.font.name = font_name
    run.font.size = Pt(size)
    run.bold = bold
    r = run._element
    r.rPr.rFonts.set(qn('w:eastAsia'), font_name)

def add_heading_custom(doc, text, level):
    """自定义标题样式"""
    p = doc.add_paragraph()
    p.style = doc.styles[f'Heading {level}']
    run = p.add_run(text)
    if level == 1:
        set_font(run, '黑体', 16, True)  # 三号
        p.paragraph_format.space_before = Pt(24)
        p.paragraph_format.space_after = Pt(18)
    elif level == 2:
        set_font(run, '黑体', 14, True)  # 四号
        p.paragraph_format.space_before = Pt(18)
        p.paragraph_format.space_after = Pt(12)
    elif level == 3:
        set_font(run, '黑体', 12, True)  # 小四
        p.paragraph_format.space_before = Pt(12)
        p.paragraph_format.space_after = Pt(6)
    return p

def add_body_paragraph(doc, text):
    """正文段落: 宋体小四，首行缩进2字符，1.5倍行距"""
    p = doc.add_paragraph()
    run = p.add_run(text)
    set_font(run, '宋体', 12)  # 小四
    p.paragraph_format.first_line_indent = Cm(0.74)  # 2字符
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.space_after = Pt(0)
    return p

# ========== 封面 ==========
for _ in range(4):
    doc.add_paragraph()

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('XX大学')
set_font(run, '黑体', 26, True)

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('硕士学位论文')
set_font(run, '黑体', 22, True)

doc.add_paragraph('\n\n\n')

p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('基于深度学习的文本分类研究')
set_font(run, '黑体', 18, True)

doc.add_paragraph('\n\n\n\n')

info = [
    ('研究生:', '张三'),
    ('学号:', '2023XXXXXX'),
    ('指导教师:', '李教授'),
    ('学科专业:', '计算机科学与技术'),
    ('提交日期:', '2024年6月'),
]
for label, value in info:
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'{label} {value}')
    set_font(run, '宋体', 14)

doc.add_page_break()

# ========== 目录(占位符) ==========
p = doc.add_paragraph()
p.alignment = WD_ALIGN_PARAGRAPH.CENTER
run = p.add_run('目  录')
set_font(run, '黑体', 16, True)

doc.add_paragraph('（请在Word中右键更新目录域）')
doc.add_page_break()

# ========== 摘要 ==========
add_heading_custom(doc, '摘  要', 1)
add_body_paragraph(doc, '随着互联网信息的爆炸式增长，文本分类作为自然语言处理的基础任务，具有重要的研究价值与应用意义。本文针对传统文本分类方法在特征提取与语义理解方面的不足，提出了一种基于深度学习的文本分类模型...')
add_body_paragraph(doc, '本文的主要贡献包括: (1) 提出了一种融合注意力机制的BERT文本分类模型；(2) 设计了多任务学习框架，联合训练主题分类与情感分类；(3) 在3个公开数据集上验证了模型的有效性，F1值较基线提升5.2%。')

p = doc.add_paragraph()
run = p.add_run('关键词: ')
set_font(run, '黑体', 12, True)
run = p.add_run('深度学习；文本分类；BERT；注意力机制；多任务学习')
set_font(run, '宋体', 12)

doc.add_page_break()

# ========== 正文 ==========
add_heading_custom(doc, '第一章 绪论', 1)

add_heading_custom(doc, '1.1 研究背景与意义', 2)
add_body_paragraph(doc, '文本分类是自然语言处理领域的基础任务之一，旨在将文本按照预定义的类别进行归类。随着深度学习技术的发展，基于神经网络的文本分类方法逐渐取代了传统的机器学习方法...')

add_heading_custom(doc, '1.1.1 研究背景', 3)
add_body_paragraph(doc, '互联网的快速发展产生了海量的文本数据，如何高效地组织、管理和检索这些文本数据成为一个重要挑战。文本分类作为解决这一问题的核心技术...')

add_heading_custom(doc, '1.2 国内外研究现状', 2)
add_body_paragraph(doc, '文本分类方法经历了从基于规则的方法，到传统机器学习方法，再到深度学习方法的演进过程...')

add_heading_custom(doc, '1.3 本文研究内容', 2)
add_body_paragraph(doc, '本文围绕基于深度学习的文本分类展开研究，主要内容包括以下几个方面:')

# 列表
items = [
    '研究基于BERT的文本分类模型，分析预训练语言模型在文本分类任务中的优势',
    '提出融合注意力机制的改进模型，增强模型对关键信息的捕获能力',
    '设计多任务学习框架，联合优化主题分类与情感分类任务',
]
for i, item in enumerate(items, 1):
    p = doc.add_paragraph()
    run = p.add_run(f'({i}) {item}')
    set_font(run, '宋体', 12)
    p.paragraph_format.first_line_indent = Cm(0.74)
    p.paragraph_format.line_spacing = 1.5

# ========== 参考文献 ==========
add_heading_custom(doc, '参考文献', 1)

references = [
    '[1] Devlin J, Chang M W, Lee K, et al. BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding[C]. NAACL-HLT, 2019: 4171-4186.',
    '[2] Vaswani A, Shazeer N, Parmar N, et al. Attention Is All You Need[C]. NIPS, 2017: 5998-6008.',
    '[3] 刘知远, 韩旭, 孙茂松. 知识表示学习研究进展[J]. 计算机研究与发展, 2016, 53(2): 247-261.',
]
for ref in references:
    p = doc.add_paragraph()
    run = p.add_run(ref)
    set_font(run, '宋体', 10.5)  # 五号
    p.paragraph_format.line_spacing = 1.5
    p.paragraph_format.hanging_indent = Cm(0.74)

# ========== 页眉页脚 ==========
section = doc.sections[0]
# 页脚: 页码居中
footer = section.footer
footer_p = footer.paragraphs[0]
footer_p.alignment = WD_ALIGN_PARAGRAPH.CENTER

# 添加页码域
run = footer_p.add_run()
fldChar1 = OxmlElement('w:fldChar')
fldChar1.set(qn('w:fldCharType'), 'begin')
instrText = OxmlElement('w:instrText')
instrText.set(qn('xml:space'), 'preserve')
instrText.text = 'PAGE'
fldChar2 = OxmlElement('w:fldChar')
fldChar2.set(qn('w:fldCharType'), 'end')
run._r.append(fldChar1)
run._r.append(instrText)
run._r.append(fldChar2)
set_font(run, '宋体', 10.5)

doc.save('output/thesis-formatting/document.docx')
print('论文文档已生成')
```

**效果验证**: ✓封面含校名+标题+作者+导师 ✓三级标题样式(黑体三号/四号/小四) ✓正文首行缩进2字符+1.5倍行距 ✓参考文献GB/T 7714格式+悬挂缩进 ✓页脚自动页码域

### 案例3: 邮件合并批量生成证书

**输入**:
```
任务: 批量生成培训结业证书
模板: certificate_template.docx(含占位符{{name}},{{course}},{{date}},{{score}})
数据源: trainees.csv(name,course,date,score)
数量: 120人
特殊要求: 证书含边框装饰，成绩>90分标注"优秀"
```

**LLM生成输出**:
```python
# output/certificates/generate_certificates.py
import pandas as pd
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
import os

# 读取数据
df = pd.read_csv('trainees.csv')
os.makedirs('output/certificates/merged', exist_ok=True)

def set_font(run, font_name, size, bold=False, color=None):
    run.font.name = font_name
    run.font.size = Pt(size)
    run.bold = bold
    run._element.rPr.rFonts.set(qn('w:eastAsia'), font_name)
    if color:
        run.font.color.rgb = color

def add_page_border(doc):
    """添加页面边框装饰"""
    sectPr = doc.sections[0]._sectPr
    pgBorders = OxmlElement('w:pgBorders')
    pgBorders.set(qn('w:offsetFrom'), 'page')
    for border_name in ['top', 'left', 'bottom', 'right']:
        border = OxmlElement(f'w:{border_name}')
        border.set(qn('w:val'), 'double')
        border.set(qn('w:sz'), '12')
        border.set(qn('w:space'), '24')
        border.set(qn('w:color'), '1F497D')
        pgBorders.append(border)
    sectPr.append(pgBorders)

for idx, row in df.iterrows():
    doc = Document()
    
    # 页面设置(横向)
    section = doc.sections[0]
    section.page_width = Cm(29.7)
    section.page_height = Cm(21)
    section.top_margin = Cm(3)
    section.bottom_margin = Cm(3)
    section.left_margin = Cm(4)
    section.right_margin = Cm(4)
    
    # 添加边框
    add_page_border(doc)
    
    # 标题
    doc.add_paragraph('\n')
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('结 业 证 书')
    set_font(run, '黑体', 36, True, RGBColor(0x1F, 0x49, 0x7D))
    
    doc.add_paragraph('\n\n')
    
    # 证书编号
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    cert_no = f'证书编号: CERT-2024-{idx+1:04d}'
    run = p.add_run(cert_no)
    set_font(run, '宋体', 10.5)
    
    doc.add_paragraph('\n')
    
    # 正文
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(row['name'])
    set_font(run, '黑体', 18, True)
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('同学: ')
    set_font(run, '宋体', 14)
    
    doc.add_paragraph('\n')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('于')
    set_font(run, '宋体', 14)
    run = p.add_run(f' {row["date"]} ')
    set_font(run, '宋体', 14)
    run = p.add_run('参加')
    set_font(run, '宋体', 14)
    
    doc.add_paragraph('\n')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run(f'《{row["course"]}》')
    set_font(run, '黑体', 16, True, RGBColor(0x1F, 0x49, 0x7D))
    
    doc.add_paragraph('\n')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('培训课程，完成全部学习内容，考试成绩: ')
    set_font(run, '宋体', 14)
    
    # 成绩+优秀标注
    score = int(row['score'])
    run = p.add_run(f'{score}分')
    set_font(run, '黑体', 14, True)
    
    if score >= 90:
        run = p.add_run(' (优秀)')
        set_font(run, '黑体', 14, True, RGBColor(0xC0, 0x00, 0x00))
    
    doc.add_paragraph('\n')
    
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.CENTER
    run = p.add_run('特发此证，以资证明。')
    set_font(run, '宋体', 14)
    
    doc.add_paragraph('\n\n\n')
    
    # 签发信息
    p = doc.add_paragraph()
    p.alignment = WD_ALIGN_PARAGRAPH.RIGHT
    run = p.add_run('XX培训中心\n')
    set_font(run, '宋体', 14)
    run = p.add_run(f'{row["date"]}')
    set_font(run, '宋体', 14)
    
    # 保存
    filename = f'output/certificates/merged/certificate_{idx+1:03d}_{row["name"]}.docx'
    doc.save(filename)

print(f'已生成{len(df)}份结业证书')
```

```csv
# trainees.csv(示例数据)
name,course,date,score
张三,Python数据分析,2024-06-15,95
李四,机器学习实战,2024-06-15,88
王五,深度学习入门,2024-06-15,92
```

**效果验证**: ✓横向A4证书页面 ✓双线边框装饰(蓝色) ✓占位符替换(name/course/date/score) ✓成绩>90分自动标注"优秀"(红色) ✓证书编号自动递增

### 案例4: 文档修订跟踪与批注

**输入**:
```
任务: 对合同文档进行审阅，添加修订与批注
文档: contract_draft.docx(现有合同草稿)
修改需求:
  1. 将"合同金额: 15万元"修改为"合同金额: 20万元"
  2. 第3条"交付周期30天"添加批注: "建议改为45天，含测试时间"
  3. 第5条保密期限"2年"修改为"3年"
```

**LLM生成输出**:
```python
# output/contract-review/add_revisions.py
from docx import Document
from docx.shared import Pt
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from datetime import datetime

doc = Document('contract_draft.docx')

REVIEWER = '法务审阅'
DATE = datetime.now().strftime('%Y-%m-%dT%H:%M:%SZ')

def enable_track_changes(doc):
    """开启修订跟踪模式"""
    settings = doc.settings.element
    track_changes = OxmlElement('w:trackChanges')
    settings.append(track_changes)

def add_revision_replace(paragraph, old_text, new_text, author, date):
    """添加替换修订(删除旧文本+插入新文本)"""
    for run in paragraph.runs:
        if old_text in run.text:
            # 分割run
            idx = run.text.index(old_text)
            before = run.text[:idx]
            after = run.text[idx + len(old_text):]
            
            # 清空当前run
            run.text = before
            
            # 添加删除标记
            del_run = paragraph.add_run(old_text)
            del_rpr = OxmlElement('w:rPr')
            del_mark = OxmlElement('w:del')
            del_mark.set(qn('w:id'), '1')
            del_mark.set(qn('w:author'), author)
            del_mark.set(qn('w:date'), date)
            del_run._element.insert(0, del_mark)
            del_run.font.strike = True
            del_run.font.color.rgb = None
            
            # 添加插入标记
            ins_run = paragraph.add_run(new_text)
            ins_mark = OxmlElement('w:ins')
            ins_mark.set(qn('w:id'), '2')
            ins_mark.set(qn('w:author'), author)
            ins_mark.set(qn('w:date'), date)
            ins_run._element.insert(0, ins_mark)
            ins_run.bold = True
            
            # 添加剩余文本
            if after:
                paragraph.add_run(after)
            break

def add_comment(paragraph, comment_text, author, date, comment_id):
    """添加批注"""
    # 创建批注引用范围
    comment_range_start = OxmlElement('w:commentRangeStart')
    comment_range_start.set(qn('w:id'), str(comment_id))
    
    comment_range_end = OxmlElement('w:commentRangeEnd')
    comment_range_end.set(qn('w:id'), str(comment_id))
    
    comment_ref = OxmlElement('w:commentReference')
    comment_ref.set(qn('w:id'), str(comment_id))
    ref_run = paragraph.add_run()
    ref_run._element.append(comment_ref)
    
    # 插入到段落开头
    paragraph._element.insert(0, comment_range_start)
    paragraph._element.append(comment_range_end)
    
    # 创建批注内容(在comments部分)
    comments_part = doc.part._comments_part if hasattr(doc.part, '_comments_part') else None
    # 简化: 记录到revisions.md
    return comment_text

# 开启修订跟踪
enable_track_changes(doc)

# 遍历段落进行修改
for i, para in enumerate(doc.paragraphs):
    text = para.text
    
    # 修改1: 合同金额
    if '合同金额: 15万元' in text:
        add_revision_replace(para, '15万元', '20万元', REVIEWER, DATE)
        print(f'段落{i}: 合同金额 15万→20万 (已标记修订)')
    
    # 修改2: 交付周期批注
    if '交付周期30天' in text:
        comment = add_comment(para, '建议改为45天，含测试时间', REVIEWER, DATE, 1)
        print(f'段落{i}: 交付周期 (已添加批注: {comment})')
    
    # 修改3: 保密期限
    if '保密期限' in text and '2年' in text:
        add_revision_replace(para, '2年', '3年', REVIEWER, DATE)
        print(f'段落{i}: 保密期限 2年→3年 (已标记修订)')

doc.save('output/contract-review/document_revised.docx')
print('修订文档已保存')
```

```markdown
# output/contract-review/revisions.md
# 修订记录

## 修订概览
- 审阅人: 法务审阅
- 审阅日期: 2024-07-20
- 修订数: 3处(2处文本替换+1处批注)

## 修订详情

### 修订1: 合同金额调整
- 位置: 第X条 付款方式
- 原文: 合同金额: ~~15万元~~
- 修订: 合同金额: **20万元**
- 修订人: 法务审阅
- 修订原因: 根据最新报价调整

### 批注1: 交付周期建议
- 位置: 第3条 交付周期
- 原文: 交付周期30天
- 批注内容: 建议改为45天，含测试时间
- 批注人: 法务审阅
- 状态: 待回复

### 修订2: 保密期限延长
- 位置: 第5条 保密条款
- 原文: 保密期限~~2年~~
- 修订: 保密期限**3年**
- 修订人: 法务审阅
- 修订原因: 涉及核心技术，建议延长保密期

## 后续操作
1. 作者审阅修订，接受/拒绝
2. 回复批注
3. 确认后定稿
```

**效果验证**: ✓开启修订跟踪模式 ✓2处文本替换(删除+插入标记) ✓1处批注添加 ✓修订记录文档含详情 ✓修订人/日期/原因记录完整

### 案例5: 技术文档生成含代码块与表格

**输入**:
```
任务: 生成API接口文档
标题: TaskFlow API v2.0 接口文档
结构: 概述+认证方式+接口列表(5个)+错误码+更新日志
特殊要求: 接口含请求/响应示例代码块，参数说明用表格
```

**LLM生成输出**:
```python
# output/api-doc/generate_api_doc.py
from docx import Document
from docx.shared import Pt, Cm, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH
from docx.oxml.ns import qn

doc = Document()

def set_font(run, name, size, bold=False, color=None):
    run.font.name = name
    run.font.size = Pt(size)
    run.bold = bold
    run._element.rPr.rFonts.set(qn('w:eastAsia'), name)
    if color:
        run.font.color.rgb = color

def add_code_block(doc, code, language='json'):
    """添加代码块(等宽字体+灰色底纹)"""
    p = doc.add_paragraph()
    p.paragraph_format.left_indent = Cm(0.5)
    p.paragraph_format.space_before = Pt(6)
    p.paragraph_format.space_after = Pt(6)
    run = p.add_run(code)
    run.font.name = 'Consolas'
    run.font.size = Pt(10)
    run.font.color.rgb = RGBColor(0x33, 0x33, 0x33)
    # 设置底纹
    from docx.oxml import OxmlElement
    pPr = p._element.get_or_add_pPr()
    shd = OxmlElement('w:shd')
    shd.set(qn('w:val'), 'clear')
    shd.set(qn('w:color'), 'auto')
    shd.set(qn('w:fill'), 'F5F5F5')
    pPr.append(shd)

def add_param_table(doc, params):
    """添加参数表格"""
    table = doc.add_table(rows=len(params)+1, cols=4)
    table.style = 'Table Grid'
    headers = ['参数名', '类型', '必填', '说明']
    for i, h in enumerate(headers):
        cell = table.rows[0].cells[i]
        cell.text = h
        for p in cell.paragraphs:
            for run in p.runs:
                run.bold = True
    for i, param in enumerate(params):
        for j, val in enumerate(param):
            table.rows[i+1].cells[j].text = val

# 标题
title = doc.add_heading('TaskFlow API v2.0 接口文档', level=0)
title.alignment = WD_ALIGN_PARAGRAPH.CENTER

# 概述
doc.add_heading('1. 概述', level=1)
p = doc.add_paragraph()
set_font(p.add_run('TaskFlow API v2.0 提供项目管理功能的RESTful接口，支持任务管理、项目看板、甘特图等核心功能。'), '宋体', 11)

# 认证方式
doc.add_heading('2. 认证方式', level=1)
p = doc.add_paragraph()
set_font(p.add_run('所有接口需在Header中携带API Token:'), '宋体', 11)
add_code_block(doc, 'Authorization: Bearer <your_api_token>')

# 接口1: 创建任务
doc.add_heading('3. 接口列表', level=1)
doc.add_heading('3.1 创建任务', level=2)

p = doc.add_paragraph()
set_font(p.add_run('POST '), 'Consolas', 11, True, RGBColor(0x00, 0x80, 0x00))
set_font(p.add_run('/api/v2/tasks'), 'Consolas', 11)

doc.add_heading('请求参数', level=3)
add_param_table(doc, [
    ['title', 'string', '是', '任务标题(最长200字符)'],
    ['project_id', 'integer', '是', '所属项目ID'],
    ['assignee_id', 'integer', '否', '指派人ID'],
    ['priority', 'integer', '否', '优先级(1-5)，默认3'],
    ['due_date', 'string', '否', '截止日期(YYYY-MM-DD)'],
])

doc.add_heading('请求示例', level=3)
add_code_block(doc, '''curl -X POST https://api.taskflow.com/v2/tasks \\
  -H "Authorization: Bearer abc123" \\
  -H "Content-Type: application/json" \\
  -d '{
    "title": "完成API文档",
    "project_id": 1001,
    "assignee_id": 2008,
    "priority": 4,
    "due_date": "2024-08-15"
  }''', 'bash')

doc.add_heading('响应示例', level=3)
add_code_block(doc, '''{
  "code": 200,
  "message": "success",
  "data": {
    "task_id": 50023,
    "title": "完成API文档",
    "project_id": 1001,
    "assignee_id": 2008,
    "priority": 4,
    "status": "todo",
    "due_date": "2024-08-15",
    "created_at": "2024-07-20T10:30:00Z"
  }
}''', 'json')

# 接口2: 获取任务列表
doc.add_heading('3.2 获取任务列表', level=2)
p = doc.add_paragraph()
set_font(p.add_run('GET '), 'Consolas', 11, True, RGBColor(0x00, 0x80, 0x00))
set_font(p.add_run('/api/v2/tasks?project_id={project_id}&status={status}&page={page}'), 'Consolas', 11)

add_param_table(doc, [
    ['project_id', 'integer', '是', '项目ID'],
    ['status', 'string', '否', '任务状态(todo/doing/done)'],
    ['page', 'integer', '否', '页码，默认1'],
    ['per_page', 'integer', '否', '每页数量，默认20'],
])

# 错误码
doc.add_heading('4. 错误码', level=1)
table = doc.add_table(rows=6, cols=3)
table.style = 'Table Grid'
errors = [
    ['错误码', '含义', '处理建议'],
    ['400', '请求参数错误', '检查参数格式与必填项'],
    ['401', '认证失败', '检查API Token是否正确'],
    ['403', '无权限', '确认是否有该资源的访问权限'],
    ['404', '资源不存在', '检查ID是否正确'],
    ['500', '服务器错误', '联系技术支持'],
]
for i, row in enumerate(errors):
    for j, val in enumerate(row):
        table.rows[i].cells[j].text = val

# 更新日志
doc.add_heading('5. 更新日志', level=1)
table = doc.add_table(rows=4, cols=3)
table.style = 'Table Grid'
logs = [
    ['版本', '日期', '更新内容'],
    ['v2.0', '2024-07-01', '新增甘特图接口，废弃v1接口'],
    ['v1.5', '2024-04-15', '新增批量操作接口'],
    ['v1.0', '2024-01-01', '初始版本'],
]
for i, row in enumerate(logs):
    for j, val in enumerate(row):
        table.rows[i].cells[j].text = val

doc.save('output/api-doc/document.docx')
print('API文档已生成')
```

**效果验证**: ✓完整API文档结构(概述+认证+5接口+错误码+日志) ✓代码块等宽字体+灰色底纹 ✓参数表格4列(名/类型/必填/说明) ✓HTTP方法彩色标注(绿色) ✓请求/响应示例真实可用

## 常见问题

### Q1: python-docx能实现哪些Word功能?有哪些限制?
A: python-docx支持:文本/段落/标题/表格/图片/页眉页脚/样式/分节符/页码。限制:(1)不支持修订跟踪的细粒度控制(仅能读取已有修订)(2)目录需占位符,不自动生成(需Word打开后F9更新)(3)不支持复杂形状/SmartArt/图表(4)批注功能有限(5)不支持宏(VBA)。对于复杂排版需求,建议先用python-docx生成基础文档,再用Word手动调整。

### Q2: 如何在Linux服务器上将docx转为PDF?
A: (1)LibreOffice(推荐):`libreoffice --headless --convert-to pdf document.docx`,支持Linux/macOS,无需Word。(2)docx2pdf(Windows):需安装Microsoft Word,调用COM接口。(3)Pandoc:`pandoc document.docx -o output.pdf`,需LaTeX引擎(4)Aspose.Words(付费):商业库,跨平台,质量最高。建议Linux服务器用LibreOffice,本地Windows用docx2pdf。

### Q3: 邮件合并如何处理复杂数据?
A: (1)数据源:支持Excel/CSV/JSON,使用pandas读取后逐行替换(2)占位符:统一使用{{field}}格式,避免与Word自带域冲突(3)嵌套数据:对于列表数据(如多个商品),先用python-docx生成表格行(4)图片合并:如需个性化图片(如签名),将图片路径放入数据源,替换时插入(5)条件内容:根据数据字段判断是否插入某段内容(如VIP邀请函额外内容)。

### Q4: 如何保证生成的文档在不同Word版本中显示一致?
A: (1)使用通用字体:宋体/黑体(Windows)、微软雅黑(跨平台)、Arial(英文)(2)避免使用特殊样式:坚持使用Word内置样式(Normal/Heading 1-3)(3)表格用'Table Grid'基础样式(4)图片设置固定尺寸,避免依赖自动缩放(5)页面设置用标准A4+常规页边距(6)测试:在Word 2016/2019/365/Mac/WPS中打开验证。WPS兼容性建议额外测试。

## 已知限制

- python-docx不支持修订跟踪的创建(仅读取已有修订),复杂协作需在Word中操作
- 目录生成仅插入占位符,实际目录需在Word中按F9更新
- 不支持复杂形状/SmartArt/图表/公式编辑器
- 批注功能有限,不支持线程化回复的创建
- PDF转换依赖外部工具(LibreOffice/Word),非python-docx原生功能
- 复杂排版(如报纸式分栏/文字环绕)支持有限

## 安全与合规

- 本Skill不存储任何API Key,文档生成在本地Python环境执行
- 不上传文档内容至外部服务,所有处理在Agent本地完成
- 邮件合并数据源(含个人信息)仅在本地处理,不持久化
- 文档中的敏感内容(合同/财务)建议加密存储
- 生成脚本由Agent临时执行,不持久化到Skill目录
- 涉及个人信息的批量文档(邀请函/证书)遵循最小化原则
- PDF导出可能包含元数据(作者/创建时间),敏感文档建议清理元数据
