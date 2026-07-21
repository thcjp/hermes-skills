# 详细参考 - markdown-exporter

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

### md_to_docx - Convert Markdown to DOCX
Converts Markdown text to DOCX format file.

**Usage:**
```bash
markdown-exporter md_to_docx <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output DOCX file path

**Options:**
- `--template` - Path to DOCX template file (optional)
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_docx /path/input.md /path/output.docx
   ```
   This converts the entire Markdown file to a DOCX document.

2. **With custom template**:
   ```bash
   markdown-exporter md_to_docx /path/input.md /path/output.docx --template /path/template.docx
   ```
   This uses a custom DOCX template for styling.

3. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_docx /path/input.md /path/output.docx --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

Converts Markdown tables to XLSX format with multiple sheets support.

**Usage:**
```bash
markdown-exporter md_to_xlsx <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output XLSX file path

**Options:**
- `--force-text` - Convert cell values to text type (default: True)
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx
   ```
   This converts all tables in the input Markdown file to an XLSX workbook, with each table on a separate sheet.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

3. **With force-text disabled**:
   ```bash
   markdown-exporter md_to_xlsx /path/input.md /path/output.xlsx --force-text False
   ```
   This allows Excel to automatically determine cell types.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.



### md_to_json - Convert Markdown Tables to JSON
Converts Markdown tables to JSON or JSONL format file.

**Usage:**
```bash
markdown-exporter md_to_json <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output JSON file path

**Options:**
- `--style` - JSON output style: `jsonl` (default) or `json_array`
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion (JSONL format)**:
   ```bash
   markdown-exporter md_to_json /path/input.md /path/output.json
   ```
   This converts tables to JSON Lines format (one JSON object per line).

2. **Convert to JSON array**:
   ```bash
   markdown-exporter md_to_json /path/input.md /path/output.json --style json_array
   ```
   This converts tables to a single JSON array of objects.

3. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_json /path/input.md /path/output.json --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

Converts Markdown text to XML format file.

**Usage:**
```bash
markdown-exporter md_to_xml <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output XML file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_xml /path/input.md /path/output.xml
   ```
   This converts the entire Markdown file to an XML document.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_xml /path/input.md /path/output.xml --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.



### md_to_csv - Convert Markdown tables to CSV
Converts Markdown tables to CSV format file.

**Usage:**
```bash
markdown-exporter md_to_csv <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output CSV file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_csv /path/input.md /path/output.csv
   ```
   This converts all tables in the input Markdown file to CSV format.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_csv /path/input.md /path/output.csv --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

Converts Markdown text to PDF format with support for Chinese, Japanese, and other languages.

**Usage:**
```bash
markdown-exporter md_to_pdf <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output PDF file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_pdf /path/input.md /path/output.pdf
   ```
   This converts the entire Markdown file to a PDF document.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_pdf /path/input.md /path/output.pdf --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.



### md_to_latex - Convert Markdown Tables to LaTeX
Converts Markdown tables to LaTeX format file.

**Usage:**
```bash
markdown-exporter md_to_latex <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path containing tables
- `output` - Output LaTeX file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_latex /path/input.md /path/output.tex
   ```
   This converts all tables in the input Markdown file to LaTeX format.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_latex /path/input.md /path/output.tex --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.

Converts Markdown text to HTML format file.

**Usage:**
```bash
markdown-exporter md_to_html <input> <output> [options]
```

**Arguments:**
- `input` - Input Markdown file path
- `output` - Output HTML file path

**Options:**
- `--strip-wrapper` - Remove code block wrapper if present

**Examples:**

1. **Basic conversion**:
   ```bash
   markdown-exporter md_to_html /path/input.md /path/output.html
   ```
   This converts the entire Markdown file to an HTML document.

2. **With code block wrapper removal**:
   ```bash
   markdown-exporter md_to_html /path/input.md /path/output.html --strip-wrapper
   ```
   This removes any code block wrappers (```) before processing the Markdown.

**Sample Markdown Input:**
Use the "Basic Text and Tables" example from the [Sample Markdown Inputs - Basic Text and Tables](#basic-text-and-tables) section below.



