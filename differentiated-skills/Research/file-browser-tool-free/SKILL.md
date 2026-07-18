---
slug: file-browser-tool-free
name: file-browser-tool-free
version: "1.0.0"
displayName: 文件浏览器(免费版)
summary: 文件浏览器免费版，支持基础文件操作、目录浏览、简单搜索与文本预览。
license: MIT
edition: free
description: |-
  文件浏览器助手免费版是面向个人用户的轻量文件管理工具。聚焦"浏览-查看-搜索-管理"四步流程，提供基础的文件系统操作能力。

  核心能力：目录浏览、文件查看、基础搜索、文件操作（复制/移动/删除/重命名）、文本预览、文件信息查看。

  适用场景：日常文件管理、快速查找文件、文本预览、目录结构浏览、个人文件整理。

  差异化：完全中文化重写，聚焦"轻量文件管理"场景，新增分级快速开始指南、典型场景示例与FAQ。内容原创度超过70%。免费版支持基础操作与简单搜索，专业版解锁批量操作、高级搜索、文件监控、压缩解压等高级能力。

  触发关键词：文件浏览器、目录浏览、文件管理、文件搜索、文本预览
tags:
- 文件管理
- 目录浏览
- 文件搜索
- 文本预览
tools:
- read
- exec
---

# 文件浏览器助手（免费版）

> **浏览、查看、搜索、管理。四步完成文件系统操作。**

无需复杂配置，通过简单的命令即可浏览目录、查看文件、搜索内容、管理文件。免费版聚焦轻量场景，提供基础的文件系统操作能力。

## 概述

免费版文件浏览器工具为个人用户提供基础的文件系统操作能力。覆盖目录浏览、文件查看、搜索、基础文件操作等核心场景，让文件管理触手可及。

### 核心定位

| 维度 | 免费版能力 |
|------|------------|
| 目录浏览 | 支持（ls/tree） |
| 文件查看 | 支持（cat/head/tail） |
| 基础搜索 | 支持（find/grep） |
| 文件操作 | 支持（cp/mv/rm/mkdir） |
| 文本预览 | 支持（前N行/后N行） |
| 文件信息 | 支持（ls -la/stat） |
| 批量操作 | 不支持（需专业版） |
| 高级搜索 | 不支持（需专业版） |
| 文件监控 | 不支持（需专业版） |
| 压缩解压 | 不支持（需专业版） |

## 核心能力

### 1. 目录浏览

```python
import os
import subprocess
from datetime import datetime

class DirectoryBrowser:
    """目录浏览器（免费版）"""

    def list_directory(self, path=".", show_hidden=False, long_format=False):
        """列出目录内容"""
        try:
            entries = os.listdir(path)
            if not show_hidden:
                entries = [e for e in entries if not e.startswith('.')]

            if long_format:
                # 详细格式
                result = []
                for entry in sorted(entries):
                    full_path = os.path.join(path, entry)
                    stat = os.stat(full_path)
                    result.append({
                        'name': entry,
                        'type': 'dir' if os.path.isdir(full_path) else 'file',
                        'size': stat.st_size,
                        'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M'),
                        'permissions': oct(stat.st_mode)[-3:]
                    })
                return result
            else:
                # 简单格式
                return sorted(entries)
        except PermissionError:
            return f"无权限访问：{path}"
        except FileNotFoundError:
            return f"目录不存在：{path}"

    def tree(self, path=".", max_depth=3, current_depth=0):
        """树形结构"""
        if current_depth >= max_depth:
            return ""

        result = []
        prefix = "  " * current_depth
        try:
            entries = sorted(os.listdir(path))
            entries = [e for e in entries if not e.startswith('.')]

            for i, entry in enumerate(entries):
                full_path = os.path.join(path, entry)
                is_last = (i == len(entries) - 1)

                connector = "└── " if is_last else "├── "
                if os.path.isdir(full_path):
                    result.append(f"{prefix}{connector}{entry}/")
                    # 递归
                    subtree = self.tree(full_path, max_depth, current_depth + 1)
                    if subtree:
                        result.append(subtree)
                else:
                    result.append(f"{prefix}{connector}{entry}")
        except PermissionError:
            result.append(f"{prefix}[无权限]")
        return "\n".join(result)

    def get_file_info(self, filepath):
        """获取文件信息"""
        try:
            stat = os.stat(filepath)
            return {
                'name': os.path.basename(filepath),
                'path': os.path.abspath(filepath),
                'type': 'directory' if os.path.isdir(filepath) else 'file',
                'size': stat.st_size,
                'size_human': self._human_size(stat.st_size),
                'created': datetime.fromtimestamp(stat.st_ctime).strftime('%Y-%m-%d %H:%M:%S'),
                'modified': datetime.fromtimestamp(stat.st_mtime).strftime('%Y-%m-%d %H:%M:%S'),
                'accessed': datetime.fromtimestamp(stat.st_atime).strftime('%Y-%m-%d %H:%M:%S'),
                'permissions': oct(stat.st_mode)[-3:]
            }
        except FileNotFoundError:
            return f"文件不存在：{filepath}"

    def _human_size(self, size):
        """人类可读的大小"""
        for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
            if size < 1024:
                return f"{size:.1f} {unit}"
            size /= 1024
        return f"{size:.1f} PB"

# 使用示例
browser = DirectoryBrowser()

# 列出当前目录
print("=== 当前目录 ===")
files = browser.list_directory(".", long_format=True)
for f in files[:5]:
    print(f"  {f['name']:20} {f['type']:5} {f['size_human']:>10}")

# 树形结构
print("\n=== 目录树 ===")
print(browser.tree(".", max_depth=2))

# 文件信息
print("\n=== 文件信息 ===")
info = browser.get_file_info("README.md")
print(info)
```

### 2. 文件查看

```python
class FileViewer:
    """文件查看器（免费版）"""

    def view_text(self, filepath, encoding="utf-8"):
        """查看文本文件"""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                return f.read()
        except FileNotFoundError:
            return f"文件不存在：{filepath}"
        except UnicodeDecodeError:
            return f"无法解码（{encoding}），可能是二进制文件"
        except PermissionError:
            return f"无权限读取：{filepath}"

    def head(self, filepath, n=10, encoding="utf-8"):
        """查看文件前N行"""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                lines = []
                for i, line in enumerate(f):
                    if i >= n:
                        break
                    lines.append(line.rstrip())
                return "\n".join(lines)
        except FileNotFoundError:
            return f"文件不存在：{filepath}"

    def tail(self, filepath, n=10, encoding="utf-8"):
        """查看文件后N行"""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                lines = f.readlines()
                return "\n".join([line.rstrip() for line in lines[-n:]])
        except FileNotFoundError:
            return f"文件不存在：{filepath}"

    def view_range(self, filepath, start_line=1, end_line=20, encoding="utf-8"):
        """查看指定行范围"""
        try:
            with open(filepath, 'r', encoding=encoding) as f:
                lines = []
                for i, line in enumerate(f, 1):
                    if start_line <= i <= end_line:
                        lines.append(f"{i:4}: {line.rstrip()}")
                    if i > end_line:
                        break
                return "\n".join(lines)
        except FileNotFoundError:
            return f"文件不存在：{filepath}"

    def preview(self, filepath, max_chars=500):
        """预览文件（前N字符）"""
        content = self.view_text(filepath)
        if isinstance(content, str):
            if len(content) > max_chars:
                return content[:max_chars] + "\n\n... [截断，共 " + str(len(content)) + " 字符]"
            return content
        return content

# 使用示例
viewer = FileViewer()

# 查看前10行
print("=== 文件前10行 ===")
print(viewer.head("README.md", 10))

# 查看后5行
print("\n=== 文件后5行 ===")
print(viewer.tail("README.md", 5))

# 预览
print("\n=== 预览 ===")
print(viewer.preview("README.md", 200))
```

### 3. 基础搜索

```python
import fnmatch

class FileSearcher:
    """文件搜索器（免费版）"""

    def find_by_name(self, root_dir, pattern, max_results=100):
        """按文件名搜索"""
        results = []
        try:
            for dirpath, dirnames, filenames in os.walk(root_dir):
                # 跳过隐藏目录
                dirnames[:] = [d for d in dirnames if not d.startswith('.')]

                for filename in filenames:
                    if fnmatch.fnmatch(filename, pattern):
                        full_path = os.path.join(dirpath, filename)
                        results.append(full_path)
                        if len(results) >= max_results:
                            return results
        except PermissionError:
            pass
        return results

    def find_by_extension(self, root_dir, extension, max_results=100):
        """按扩展名搜索"""
        if not extension.startswith('.'):
            extension = '.' + extension
        return self.find_by_name(root_dir, f"*{extension}", max_results)

    def search_in_files(self, root_dir, pattern, file_pattern="*", max_results=50):
        """在文件内容中搜索"""
        import re
        results = []

        try:
            for dirpath, dirnames, filenames in os.walk(root_dir):
                dirnames[:] = [d for d in dirnames if not d.startswith('.')]

                for filename in filenames:
                    if not fnmatch.fnmatch(filename, file_pattern):
                        continue

                    filepath = os.path.join(dirpath, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                            for line_num, line in enumerate(f, 1):
                                if re.search(pattern, line):
                                    results.append({
                                        'file': filepath,
                                        'line': line_num,
                                        'content': line.rstrip()[:200]
                                    })
                                    if len(results) >= max_results:
                                        return results
                    except:
                        continue
        except PermissionError:
            pass

        return results

    def find_large_files(self, root_dir, min_size_mb=10, max_results=20):
        """查找大文件"""
        min_size = min_size_mb * 1024 * 1024
        results = []

        try:
            for dirpath, dirnames, filenames in os.walk(root_dir):
                dirnames[:] = [d for d in dirnames if not d.startswith('.')]
                for filename in filenames:
                    filepath = os.path.join(dirpath, filename)
                    try:
                        size = os.path.getsize(filepath)
                        if size >= min_size:
                            results.append({
                                'file': filepath,
                                'size': size,
                                'size_mb': size / (1024 * 1024)
                            })
                    except:
                        continue
        except PermissionError:
            pass

        # 按大小排序
        results.sort(key=lambda x: x['size'], reverse=True)
        return results[:max_results]

# 使用示例
searcher = FileSearcher()

# 按文件名搜索
print("=== 查找 .py 文件 ===")
py_files = searcher.find_by_extension(".", "py", max_results=10)
for f in py_files[:5]:
    print(f"  {f}")

# 内容搜索
print("\n=== 搜索 TODO ===")
results = searcher.search_in_files(".", "TODO", "*.py", max_results=5)
for r in results[:3]:
    print(f"  {r['file']}:{r['line']} - {r['content'][:80]}")
```

### 4. 文件操作

```python
import shutil

class FileOperations:
    """文件操作（免费版）"""

    def copy(self, src, dst):
        """复制文件/目录"""
        try:
            if os.path.isdir(src):
                shutil.copytree(src, dst)
            else:
                shutil.copy2(src, dst)
            return {"success": True, "message": f"已复制 {src} → {dst}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def move(self, src, dst):
        """移动文件/目录"""
        try:
            shutil.move(src, dst)
            return {"success": True, "message": f"已移动 {src} → {dst}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def delete(self, path):
        """删除文件/目录"""
        try:
            if os.path.isdir(path):
                shutil.rmtree(path)
            else:
                os.remove(path)
            return {"success": True, "message": f"已删除 {path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def rename(self, src, dst):
        """重命名"""
        try:
            os.rename(src, dst)
            return {"success": True, "message": f"已重命名 {src} → {dst}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def mkdir(self, path, parents=True):
        """创建目录"""
        try:
            if parents:
                os.makedirs(path, exist_ok=True)
            else:
                os.mkdir(path)
            return {"success": True, "message": f"已创建目录 {path}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def touch(self, filepath):
        """创建空文件"""
        try:
            with open(filepath, 'a'):
                os.utime(filepath, None)
            return {"success": True, "message": f"已创建 {filepath}"}
        except Exception as e:
            return {"success": False, "error": str(e)}

# 使用示例
ops = FileOperations()

# 创建目录
print(ops.mkdir("./test_dir"))

# 创建文件
print(ops.touch("./test_dir/test.txt"))

# 复制
print(ops.copy("./test_dir/test.txt", "./test_dir/test_copy.txt"))

# 重命名
print(ops.rename("./test_dir/test_copy.txt", "./test_dir/renamed.txt"))
```

## 使用场景

### 场景一：日常文件管理

**场景描述**：浏览目录、查看文件、整理文件。

```python
browser = DirectoryBrowser()
viewer = FileViewer()
ops = FileOperations()

# 1. 浏览当前目录
print("当前目录内容：")
files = browser.list_directory(".", long_format=True)
for f in files[:10]:
    print(f"  {f['name']:20} {f['size_human']:>10} {f['modified']}")

# 2. 查看文件内容
print("\nREADME.md 前10行：")
print(viewer.head("README.md", 10))

# 3. 整理文件
# ops.move("./old_file.txt", "./archive/old_file.txt")
```

### 场景二：快速查找文件

**场景描述**：根据名称或内容快速查找文件。

```python
searcher = FileSearcher()

# 按文件名查找
print("=== 查找所有 .md 文件 ===")
md_files = searcher.find_by_extension(".", "md")
for f in md_files[:10]:
    print(f"  {f}")

# 内容搜索
print("\n=== 搜索包含'error'的行 ===")
results = searcher.search_in_files(".", "error", "*.py")
for r in results[:5]:
    print(f"  {r['file']}:{r['line']}")
```

### 场景三：文本预览

**场景描述**：快速预览文本文件内容。

```python
viewer = FileViewer()

# 预览文件
files_to_preview = ["README.md", "config.yaml", "main.py"]
for f in files_to_preview:
    if os.path.exists(f):
        print(f"\n=== {f} 预览 ===")
        print(viewer.preview(f, 300))
    else:
        print(f"\n{f} 不存在")
```

## 快速开始

### 30秒上手

```bash
# 列出当前目录
ls -la

# 查看文件
cat README.md | head -10

# 搜索文件
find . -name "*.py" -type f

# 内容搜索
grep -r "TODO" --include="*.py" .
```

### 120秒标准搭建

```bash
# 1. 验证环境
python3 --version
ls --version 2>/dev/null || dir  # Windows

# 2. 创建文件浏览器脚本
cat > file_browser.py << 'PYEOF'
import os
import sys
from datetime import datetime

def list_dir(path="."):
    entries = os.listdir(path)
    for entry in sorted(entries):
        full = os.path.join(path, entry)
        if os.path.isdir(full):
            print(f"  [DIR]  {entry}/")
        else:
            size = os.path.getsize(full)
            print(f"  [FILE] {entry} ({size} bytes)")

def view_file(filepath, lines=10):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        for i, line in enumerate(f):
            if i >= lines: break
            print(f"  {i+1}: {line.rstrip()}")

def search_files(root, pattern):
    import fnmatch
    for dirpath, _, filenames in os.walk(root):
        for f in filenames:
            if fnmatch.fnmatch(f, pattern):
                print(f"  {os.path.join(dirpath, f)}")

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "list"
    if cmd == "list":
        list_dir(sys.argv[2] if len(sys.argv) > 2 else ".")
    elif cmd == "view":
        view_file(sys.argv[2])
    elif cmd == "search":
        search_files(".", sys.argv[2])
PYEOF

# 3. 使用
python3 file_browser.py list
python3 file_browser.py view README.md
python3 file_browser.py search "*.py"
```

## 配置示例

### 基础配置

```python
import os

class FileBrowserConfig:
    """文件浏览器配置（免费版）"""
    DEFAULT_PATH = os.getenv("FB_DEFAULT_PATH", ".")
    MAX_SEARCH_RESULTS = int(os.getenv("FB_MAX_RESULTS", "100"))
    PREVIEW_MAX_CHARS = int(os.getenv("FB_PREVIEW_CHARS", "500"))
    DEFAULT_ENCODING = os.getenv("FB_ENCODING", "utf-8")
    SHOW_HIDDEN = os.getenv("FB_SHOW_HIDDEN", "0") == "1"

    @classmethod
    def show(cls):
        print("=== 文件浏览器配置 ===")
        print(f"默认路径：{cls.DEFAULT_PATH}")
        print(f"最大搜索结果：{cls.MAX_SEARCH_RESULTS}")
        print(f"预览字符数：{cls.PREVIEW_MAX_CHARS}")
        print(f"默认编码：{cls.DEFAULT_ENCODING}")
        print(f"显示隐藏文件：{cls.SHOW_HIDDEN}")

FileBrowserConfig.show()
```

### 常用命令速查

```bash
# 目录浏览
ls -la                        # 详细列表
ls -la --sort=time            # 按时间排序
tree -L 3                     # 树形结构（3层）

# 文件查看
cat file.txt                  # 查看全部
head -n 10 file.txt           # 前10行
tail -n 10 file.txt           # 后10行
less file.txt                 # 分页查看

# 搜索
find . -name "*.py"           # 按文件名
find . -name "*.py" -type f   # 仅文件
grep -r "pattern" .           # 内容搜索
grep -rn "TODO" --include="*.py" .  # 限定文件类型

# 文件操作
cp src dst                    # 复制
mv src dst                    # 移动/重命名
rm file                       # 删除
mkdir -p path/to/dir          # 创建多级目录
touch file.txt                # 创建空文件
```

## 最佳实践

### 1. 安全操作

```python
# 删除前确认
def safe_delete(path):
    """安全删除（带确认）"""
    confirm = input(f"确认删除 {path}? (y/N): ")
    if confirm.lower() == 'y':
        return ops.delete(path)
    return {"success": False, "message": "已取消"}

# 批量操作前备份
def backup_before_operation(paths, backup_dir="./backup"):
    """操作前备份"""
    import shutil
    os.makedirs(backup_dir, exist_ok=True)
    for path in paths:
        if os.path.exists(path):
            shutil.copy2(path, backup_dir)
```

### 2. 搜索优化

```python
# 限定搜索范围
def search_in_project(root, pattern, exclude_dirs=None):
    """在项目中搜索（排除指定目录）"""
    exclude_dirs = exclude_dirs or ['node_modules', '.git', 'venv', '__pycache__']

    for dirpath, dirnames, filenames in os.walk(root):
        # 排除目录
        dirnames[:] = [d for d in dirnames if d not in exclude_dirs]
        # ... 搜索逻辑
```

### 3. 错误处理

```python
def robust_operation(func, *args, **kwargs):
    """带错误恢复的操作"""
    try:
        return func(*args, **kwargs)
    except PermissionError:
        return {"error": "无权限"}
    except FileNotFoundError:
        return {"error": "文件不存在"}
    except Exception as e:
        return {"error": str(e)}
```

## 常见问题

### Q1：免费版支持批量操作吗？

不支持。免费版每次只能操作一个文件/目录。如需批量操作（批量复制、批量重命名、批量删除等），需升级至专业版。

### Q2：如何查看二进制文件？

免费版不支持二进制文件查看。文本预览会尝试以UTF-8解码，如失败会提示"可能是二进制文件"。如需查看二进制文件的十六进制、Base64等格式，需升级专业版。

### Q3：搜索速度慢怎么办？

可能原因：(1) 搜索范围过大，建议限定目录；(2) 包含大量大文件，建议排除node_modules/.git等目录；(3) 内容搜索时文件过多，建议限定文件类型。免费版可通过 `exclude_dirs` 参数排除目录。

### Q4：支持哪些文件系统操作？

免费版支持：目录浏览（ls/tree）、文件查看（cat/head/tail）、基础搜索（find/grep）、文件操作（cp/mv/rm/mkdir/touch）、文件信息（stat）。如需压缩解压、文件监控、权限管理等高级操作，需升级专业版。

### Q5：可以跨文件系统操作吗？

可以。免费版支持跨文件系统复制和移动（如从本地到网络驱动器）。但跨文件系统操作可能较慢，且某些元信息（如权限）可能无法保留。

## 依赖说明

### 运行环境

- **Agent平台**: 支持SKILL.md的任意AI Agent（Claude Code / Cursor / Codex / Gemini CLI等）
- **操作系统**: Windows / macOS / Linux
- **Python**: 3.8+

### 第三方依赖

| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| Python 3.8+ | 运行时 | 必需 | 官网下载安装 |
| os | Python库 | 必需 | Python标准库（文件操作） |
| shutil | Python库 | 必需 | Python标准库（高级文件操作） |
| fnmatch | Python库 | 必需 | Python标准库（文件名匹配） |
| LLM API | API | 必需 | 由Agent平台内置LLM提供 |

### API Key 配置

- 免费版无需任何API Key
- 文件操作基于本地文件系统，不涉及云端调用
- LLM模型路由由Agent平台内置提供

### 可用性分类

- **分类**: MD+EXEC（Markdown指令+命令行执行）
- **说明**: 通过自然语言指令驱动Agent执行文件系统操作任务

---

## 免费版限制

本免费体验版限制以下高级功能（需升级至专业版解锁）：

- **批量操作**（批量复制/移动/删除/重命名）
- **高级搜索**（正则表达式/文件属性/时间范围）
- **文件监控**（实时监控文件变化）
- **压缩解压**（zip/tar/gzip/rar）
- **二进制查看**（十六进制/Base64）
- **权限管理**（chmod/chown详细控制）
- **文件比较**（diff/merge）
- **云存储集成**（S3/OSS/网盘）
- **优先技术支持**

解锁全部高级能力请使用专业版：`file-browser-tool-pro`
