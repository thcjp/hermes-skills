---
slug: csv-handler
name: csv-handler
version: "2.1.0"
displayName: Csv Handler
summary: Handle CSV files from construction software exports. Auto-detect delimiters,
  encodings, and clean...
license: MIT
description: |-
  Handle CSV files from construction software exports。Auto-detect delimiters,
  encodings, and clean。Use when 需要文件处理、文档转换、格式互转、内容提取时使用。不适用于加密文件破解。适用于独立开发者、企业团队和自动化工作流场景。
tags:
- Integrations
tools:
  - - read
- exec
pricing_tier: "L4"
pricing_model: "monthly"
suggested_price: 99.9
---


# Csv Handler

## Overview

CSV is the universal exchange format in construction - from scheduling exports to cost databases. This skill handles encoding issues, delimiter detection, and data cleaning.

## Python Implementation

```python
import pandas as pd
import csv
from typing import Dict, Any, List, Optional, Tuple
from pathlib import Path
from dataclasses import dataclass
import chardet

@dataclass
class CSVProfile:
    """Profile of CSV file."""
    encoding: str
    delimiter: str
    has_header: bool
    row_count: int
    column_count: int
    columns: List[str]

class ConstructionCSVHandler:
    """Handle CSV files from construction software."""

    COMMON_DELIMITERS = [',', ';', '\t', '|']
    COMMON_ENCODINGS = ['utf-8', 'utf-8-sig', 'latin-1', 'cp1252', 'iso-8859-1']

    def __init__(self):
        self.last_profile: Optional[CSVProfile] = None

    def detect_encoding(self, file_path: str) -> str:
        """Detect file encoding."""
        with open(file_path, 'rb') as f:
            raw = f.read(10000)
        result = chardet.detect(raw)
        return result.get('encoding', 'utf-8') or 'utf-8'

    def detect_delimiter(self, file_path: str, encoding: str) -> str:
        """Detect CSV delimiter."""
        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
            sample = f.read(5000)

        # Count occurrences
        counts = {d: sample.count(d) for d in self.COMMON_DELIMITERS}

        # Return most common that appears consistently
        if counts:
            return max(counts, key=counts.get)
        return ','

    def profile_csv(self, file_path: str) -> CSVProfile:
        """Profile CSV file."""
        encoding = self.detect_encoding(file_path)
        delimiter = self.detect_delimiter(file_path, encoding)

        # Read sample
        df = pd.read_csv(file_path, encoding=encoding, delimiter=delimiter,
                         nrows=10, on_bad_lines='skip')

        has_header = not df.columns[0].replace('.', '').replace('-', '').isdigit()

        # Full row count
        with open(file_path, 'r', encoding=encoding, errors='replace') as f:
            row_count = sum(1 for _ in f) - (1 if has_header else 0)

        profile = CSVProfile(
            encoding=encoding,
            delimiter=delimiter,
            has_header=has_header,
            row_count=row_count,
            column_count=len(df.columns),
            columns=list(df.columns)
        )
        self.last_profile = profile
        return profile

    def read_csv(self, file_path: str,
                 encoding: Optional[str] = None,
                 delimiter: Optional[str] = None,
                 clean: bool = True) -> pd.DataFrame:
        """Read CSV with auto-detection."""

        # Auto-detect if not provided
        if encoding is None:
            encoding = self.detect_encoding(file_path)
        if delimiter is None:
            delimiter = self.detect_delimiter(file_path, encoding)

        # Read with error handling
        df = pd.read_csv(
            file_path,
            encoding=encoding,
            delimiter=delimiter,
            on_bad_lines='skip',
            low_memory=False
        )

        if clean:
            df = self.clean_dataframe(df)

        return df

    def clean_dataframe(self, df: pd.DataFrame) -> pd.DataFrame:
        """Clean construction CSV data."""
        # Clean column names
        df.columns = [self._clean_column_name(c) for c in df.columns]

        # Remove empty rows and columns
        df = df.dropna(how='all')
        df = df.dropna(axis=1, how='all')

        # Strip whitespace from strings
        for col in df.select_dtypes(include=['object']):
            df[col] = df[col].str.strip() if df[col].dtype == 'object' else df[col]

        return df

    def _clean_column_name(self, name: str) -> str:
        """Clean column name."""
        if not isinstance(name, str):
            return str(name)

        # Remove special characters, replace spaces
        clean = name.strip().lower()
        clean = clean.replace(' ', '_').replace('-', '_')
        clean = ''.join(c for c in clean if c.isalnum() or c == '_')
        return clean

    def merge_csvs(self, file_paths: List[str],
                   on_column: Optional[str] = None) -> pd.DataFrame:
        """Merge multiple CSV files."""
        dfs = []
        for path in file_paths:
            df = self.read_csv(path)
            df['_source_file'] = Path(path).name
            dfs.append(df)

        if not dfs:
            return pd.DataFrame()

        if on_column and on_column in dfs[0].columns:
            result = dfs[0]
            for df in dfs[1:]:
                result = pd.merge(result, df, on=on_column, how='outer')
            return result

        return pd.concat(dfs, ignore_index=True)

    def split_csv(self, df: pd.DataFrame,
                  group_column: str,
                  output_dir: str) -> List[str]:
        """Split CSV by column values."""
        output_path = Path(output_dir)
        output_path.mkdir(parents=True, exist_ok=True)

        files = []
        for value in df[group_column].unique():
            subset = df[df[group_column] == value]
            filename = f"{group_column}_{value}.csv"
            filepath = output_path / filename
            subset.to_csv(filepath, index=False)
            files.append(str(filepath))

        return files

    def convert_types(self, df: pd.DataFrame,
                      type_map: Dict[str, str] = None) -> pd.DataFrame:
        """Convert column types intelligently."""
        df = df.copy()

        if type_map:
            for col, dtype in type_map.items():
                if col in df.columns:
                    try:
                        df[col] = df[col].astype(dtype)
                    except:
                        pass
        else:
            # Auto-convert
            for col in df.columns:
                # Try numeric
                try:
                    df[col] = pd.to_numeric(df[col])
                    continue
                except:
                    pass

                # Try datetime
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        return df

    def export_csv(self, df: pd.DataFrame,
                   file_path: str,
                   encoding: str = 'utf-8-sig',
                   delimiter: str = ',') -> str:
        """Export DataFrame to CSV."""
        df.to_csv(file_path, encoding=encoding, sep=delimiter, index=False)
        return file_path

class ScheduleCSVHandler(ConstructionCSVHandler):
    """Handler for project schedule CSVs."""

    SCHEDULE_COLUMNS = ['task_id', 'task_name', 'start_date', 'end_date',
                        'duration', 'predecessors', 'resources']

    def parse_schedule(self, file_path: str) -> pd.DataFrame:
        """Parse schedule CSV."""
        df = self.read_csv(file_path)

        # Convert date columns
        for col in df.columns:
            if 'date' in col.lower() or 'start' in col.lower() or 'end' in col.lower():
                try:
                    df[col] = pd.to_datetime(df[col])
                except:
                    pass

        return df

class CostCSVHandler(ConstructionCSVHandler):
    """Handler for cost/estimate CSVs."""

    def parse_costs(self, file_path: str) -> pd.DataFrame:
        """Parse cost CSV."""
        df = self.read_csv(file_path)

        # Find and convert numeric columns
        for col in df.columns:
            if any(word in col.lower() for word in ['cost', 'price', 'amount', 'total', 'qty', 'quantity']):
                df[col] = pd.to_numeric(df[col].replace(r'[\$,]', '', regex=True), errors='coerce')

        return df
```

## Quick Start

```python
handler = ConstructionCSVHandler()

profile = handler.profile_csv("export.csv")
print(f"Encoding: {profile.encoding}, Delimiter: '{profile.delimiter}'")

df = handler.read_csv("export.csv")
print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
```

## 适用场景

### 1. Merge Multiple Exports

```python
files = ["jan_export.csv", "feb_export.csv", "mar_export.csv"]
merged = handler.merge_csvs(files)
```

### 2. Split by Category

```python
handler.split_csv(df, group_column='category', output_dir='./split_files')
```

### 3. Schedule Import

```python
schedule_handler = ScheduleCSVHandler()
schedule = schedule_handler.parse_schedule("p6_export.csv")
```

## Resources

* **DDC Book**: Chapter 2.1 - Structured Data

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

CSV is the universal exchange format in construction - from scheduling exports to cost databases. This skill handles encoding issues, delimiter detection, and data cleaning.

## 示例

### 示例1：基础用法

```
```python
handler = ConstructionCSVHandler()

profile = handler.profile_csv("export.csv")
print(f"Encoding: {profile.encoding}, Delimiter: '{profile.delimiter}'")

df = handler.read_csv("export.csv")
print(f"Loaded {len(df)} rows, {len(df.columns)} columns")
```
```

## 错误处理

| 错误场景 | 原因 | 处理方式 |
|---------|------|---------|
| 配置错误 | 参数缺失或格式错误 | 检查依赖说明中的配置要求 |
| 运行时错误 | 运行环境不满足 | 确认运行环境符合依赖说明 |
| 网络错误 | 连接超时或不可达 | 检查网络连接后重试，参考国内替代方案 |

## 常见问题

### Q1: 如何开始使用Csv Handler？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Csv Handler有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制

- 需要API Key，无Key环境无法使用
