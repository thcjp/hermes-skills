# 详细参考 - file-browser-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import re
import os
from datetime import datetime, timedelta

class AdvancedFileSearcher:
    """高级文件搜索器（专业版）"""

    def search_by_regex(self, root_dir, pattern, file_pattern="*", max_results=100):
        """正则表达式搜索文件名"""
        compiled = re.compile(pattern)
        results = []

        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in filenames:
                if compiled.search(filename):
                    full_path = os.path.join(dirpath, filename)
                    results.append(full_path)
                    if len(results) >= max_results:
                        return results
        return results

    def search_by_attributes(self, root_dir, **kwargs):
        """按文件属性搜索"""
        min_size = kwargs.get('min_size', 0)
        max_size = kwargs.get('max_size', float('inf'))
        modified_after = kwargs.get('modified_after')
        modified_before = kwargs.get('modified_before')
        extensions = kwargs.get('extensions', [])
        owner = kwargs.get('owner')

        results = []

        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in filenames:
                full_path = os.path.join(dirpath, filename)
                try:
                    stat = os.stat(full_path)

                    if not (min_size <= stat.st_size <= max_size):
                        continue

                    if extensions:
                        ext = os.path.splitext(filename)[1].lower()
                        if ext not in extensions:
                            continue

                    mtime = datetime.fromtimestamp(stat.st_mtime)
                    if modified_after and mtime < modified_after:
                        continue
                    if modified_before and mtime > modified_before:
                        continue

                    results.append({
                        'path': full_path,
                        'size': stat.st_size,
                        'modified': mtime.strftime('%Y-%m-%d %H:%M:%S'),
                        'permissions': oct(stat.st_mode)[-3:]
                    })
                except:
                    continue

        return results

    def search_content_advanced(self, root_dir, pattern, **kwargs):
        """高级内容搜索"""
        file_pattern = kwargs.get('file_pattern', '*')
        case_sensitive = kwargs.get('case_sensitive', False)
        whole_word = kwargs.get('whole_word', False)
        max_results = kwargs.get('max_results', 100)
        context_lines = kwargs.get('context_lines', 0)

        flags = 0 if case_sensitive else re.IGNORECASE
        if whole_word:
            pattern = r'\b' + pattern + r'\b'
        compiled = re.compile(pattern, flags)

        results = []

        for dirpath, dirnames, filenames in os.walk(root_dir):
            dirnames[:] = [d for d in dirnames if not d.startswith('.')]
            for filename in filenames:
                if not fnmatch.fnmatch(filename, file_pattern):
                    continue

                filepath = os.path.join(dirpath, filename)
                try:
                    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                        lines = f.readlines()
                        for i, line in enumerate(lines):
                            if compiled.search(line):
                                result = {
                                    'file': filepath,
                                    'line': i + 1,
                                    'content': line.rstrip()[:200]
                                }
                                if context_lines > 0:
                                    start = max(0, i - context_lines)
                                    end = min(len(lines), i + context_lines + 1)
                                    result['context'] = ''.join(lines[start:end])
                                results.append(result)
                                if len(results) >= max_results:
                                    return results
                except:
                    continue

        return results

    def search_duplicates(self, root_dir, method="hash"):
        """查找重复文件"""
        import hashlib

        files_by_size = {}
        for dirpath, _, filenames in os.walk(root_dir):
            for f in filenames:
                filepath = os.path.join(dirpath, f)
                try:
                    size = os.path.getsize(filepath)
                    if size not in files_by_size:
                        files_by_size[size] = []
                    files_by_size[size].append(filepath)
                except:
                    continue

        duplicates = []
        for size, files in files_by_size.items():
            if len(files) < 2:
                continue

            hashes = {}
            for filepath in files:
                try:
                    with open(filepath, 'rb') as f:
                        h = hashlib.md5(f.read()).hexdigest()
                    if h not in hashes:
                        hashes[h] = []
                    hashes[h].append(filepath)
                except:
                    continue

            for h, group in hashes.items():
                if len(group) > 1:
                    duplicates.append({
                        'hash': h,
                        'size': size,
                        'files': group
                    })

        return duplicates

searcher = AdvancedFileSearcher()

print("=== 查找以数字开头的文件 ===")
results = searcher.search_by_regex(".", r"^\d+", max_results=10)
for r in results[:5]:
    print(f"  {r}")

print("\n=== 查找最近7天修改的大文件 ===")
recent = datetime.now() - timedelta(days=7)
results = searcher.search_by_attributes(
    ".",
    min_size=1024*1024,  # 至少1MB
    modified_after=recent
)
for r in results[:5]:
    print(f"  {r['path']} ({r['size']/1024/1024:.1f}MB)")
```

## 代码示例 (python)

```python
import os
import shutil
import concurrent.futures
import threading

class BatchFileOperations:
    """批量文件操作（专业版）"""

    def __init__(self, max_workers=5):
        self.max_workers = max_workers
        self.lock = threading.Lock()
        self.stats = {"success": 0, "failed": 0, "total": 0}

    def batch_copy(self, src_dst_pairs):
        """批量复制"""
        return self._batch_operation(src_dst_pairs, "copy")

    def batch_move(self, src_dst_pairs):
        """批量移动"""
        return self._batch_operation(src_dst_pairs, "move")

    def batch_delete(self, paths):
        """批量删除"""
        return self._batch_operation([(p, None) for p in paths], "delete")

    def batch_rename(self, src_dst_pairs):
        """批量重命名"""
        return self._batch_operation(src_dst_pairs, "rename")

    def _batch_operation(self, pairs, operation):
        """批量操作执行"""
        self.stats = {"success": 0, "failed": 0, "total": 0}
        results = []

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = {
                executor.submit(self._single_operation, src, dst, operation): (src, dst)
                for src, dst in pairs
            }

            for future in concurrent.futures.as_completed(futures):
                src, dst = futures[future]
                try:
                    result = future.result()
                    results.append({"src": src, "dst": dst, "result": result})
                    with self.lock:
                        self.stats["total"] += 1
                        if result.get("success"):
                            self.stats["success"] += 1
                        else:
                            self.stats["failed"] += 1
                except Exception as e:
                    results.append({"src": src, "dst": dst, "result": {"error": str(e)}})
                    with self.lock:
                        self.stats["failed"] += 1

        self._print_summary(operation)
        return results

    def _single_operation(self, src, dst, operation):
        """单文件操作"""
        try:
            if operation == "copy":
                if os.path.isdir(src):
                    shutil.copytree(src, dst)
                else:
                    shutil.copy2(src, dst)
            elif operation == "move":
                shutil.move(src, dst)
            elif operation == "delete":
                if os.path.isdir(src):
                    shutil.rmtree(src)
                else:
                    os.remove(src)
            elif operation == "rename":
                os.rename(src, dst)
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def _print_summary(self, operation):
        print(f"\n=== 批量{operation}摘要 ===")
        print(f"总数：{self.stats['total']}")
        print(f"成功：{self.stats['success']}")
        print(f"失败：{self.stats['failed']}")

batch = BatchFileOperations(max_workers=5)

copy_pairs = [
    ("./file1.txt", "./backup/file1.txt"),
    ("./file2.txt", "./backup/file2.txt"),
    ("./file3.txt", "./backup/file3.txt"),
]
results = batch.batch_copy(copy_pairs)

import os
files = os.listdir("./old_files")
rename_pairs = [
    (f"./old_files/{f}", f"./new_files/{f.replace('old_', 'new_')}")
    for f in files if f.startswith("old_")
]
batch.batch_rename(rename_pairs)
```

## 代码示例 (python)

```python
import zipfile
import tarfile
import gzip

class CompressionManager:
    """压缩解压管理器（专业版）"""

    def zip_files(self, files, output_path, compression=zipfile.ZIP_DEFLATED):
        """压缩为ZIP"""
        with zipfile.ZipFile(output_path, 'w', compression) as zf:
            for file in files:
                if os.path.exists(file):
                    if os.path.isdir(file):
                        for root, _, filenames in os.walk(file):
                            for f in filenames:
                                full = os.path.join(root, f)
                                arcname = os.path.relpath(full, os.path.dirname(file))
                                zf.write(full, arcname)
                    else:
                        zf.write(file, os.path.basename(file))
        print(f"已创建压缩包：{output_path}")

    def unzip(self, zip_path, extract_dir):
        """解压ZIP"""
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(extract_dir)
        print(f"已解压到：{extract_dir}")

    def tar_files(self, files, output_path, mode='w:gz'):
        """打包为tar.gz/tar.bz2"""
        with tarfile.open(output_path, mode) as tf:
            for file in files:
                if os.path.exists(file):
                    tf.add(file, os.path.basename(file))
        print(f"已创建tar包：{output_path}")

    def untar(self, tar_path, extract_dir):
        """解压tar包"""
        with tarfile.open(tar_path, 'r:*') as tf:
            tf.extractall(extract_dir)
        print(f"已解压到：{extract_dir}")

    def gzip_file(self, filepath, output_path=None):
        """Gzip压缩单个文件"""
        if output_path is None:
            output_path = filepath + '.gz'

        with open(filepath, 'rb') as f_in:
            with gzip.open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"已压缩：{output_path}")

    def gunzip(self, gz_path, output_path=None):
        """Gzip解压"""
        if output_path is None:
            output_path = gz_path[:-3] if gz_path.endswith('.gz') else gz_path + '.out'

        with gzip.open(gz_path, 'rb') as f_in:
            with open(output_path, 'wb') as f_out:
                shutil.copyfileobj(f_in, f_out)
        print(f"已解压：{output_path}")

    def list_archive(self, archive_path):
        """列出压缩包内容"""
        if archive_path.endswith('.zip'):
            with zipfile.ZipFile(archive_path, 'r') as zf:
                return zf.namelist()
        elif archive_path.endswith(('.tar.gz', '.tar', '.tar.bz2')):
            with tarfile.open(archive_path, 'r:*') as tf:
                return tf.getnames()
        return []

compressor = CompressionManager()

compressor.zip_files(["./file1.txt", "./file2.txt"], "./archive.zip")

print("压缩包内容：")
for f in compressor.list_archive("./archive.zip"):
    print(f"  {f}")

compressor.unzip("./archive.zip", "./extracted")
```

## 代码示例 (python)

```python
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class FileMonitor:
    """文件监控器（专业版）"""

    def __init__(self):
        self.observer = Observer()
        self.handlers = []

    def watch(self, path, callback=None, recursive=True):
        """监控目录变化"""
        handler = ChangeHandler(callback)
        self.observer.schedule(handler, path, recursive=recursive)
        self.handlers.append(handler)
        print(f"已开始监控：{path}")

    def start(self):
        """启动监控"""
        self.observer.start()
        print("文件监控已启动...")

    def stop(self):
        """停止监控"""
        self.observer.stop()
        self.observer.join()
        print("文件监控已停止")

class ChangeHandler(FileSystemEventHandler):
    """变化处理器"""

    def __init__(self, callback=None):
        self.callback = callback
        self.changes = []

    def on_created(self, event):
        self._handle("created", event)

    def on_deleted(self, event):
        self._handle("deleted", event)

    def on_modified(self, event):
        self._handle("modified", event)

    def on_moved(self, event):
        self._handle("moved", event)

    def _handle(self, action, event):
        change = {
            'action': action,
            'path': event.src_path,
            'is_directory': event.is_directory,
            'timestamp': datetime.now().isoformat()
        }
        if hasattr(event, 'dest_path'):
            change['dest_path'] = event.dest_path

        self.changes.append(change)
        print(f"[{change['timestamp']}] {action}: {event.src_path}")

        if self.callback:
            self.callback(change)

monitor = FileMonitor()
monitor.watch("./important_dir", recursive=True)

def on_change(change):
    if change['action'] == 'deleted':
        print(f"告警：文件被删除 - {change['path']}")

monitor.watch("./important_dir", callback=on_change)
```

## 代码示例 (python)

```python
import difflib

class FileComparator:
    """文件比较器（专业版）"""

    def compare_text(self, file1, file2):
        """比较两个文本文件"""
        with open(file1, 'r', encoding='utf-8', errors='ignore') as f:
            lines1 = f.readlines()
        with open(file2, 'r', encoding='utf-8', errors='ignore') as f:
            lines2 = f.readlines()

        diff = difflib.unified_diff(
            lines1, lines2,
            fromfile=file1, tofile=file2,
            lineterm=''
        )
        return '\n'.join(diff)

    def compare_directories(self, dir1, dir2):
        """比较两个目录"""
        files1 = set(os.listdir(dir1))
        files2 = set(os.listdir(dir2))

        only_in_1 = files1 - files2
        only_in_2 = files2 - files1
        common = files1 & files2

        different = []
        for f in common:
            path1 = os.path.join(dir1, f)
            path2 = os.path.join(dir2, f)
            if os.path.isfile(path1) and os.path.isfile(path2):
                if not self._files_equal(path1, path2):
                    different.append(f)

        return {
            'only_in_dir1': list(only_in_1),
            'only_in_dir2': list(only_in_2),
            'different': different,
            'common': list(common)
        }

    def _files_equal(self, file1, file2):
        """判断文件是否相同"""
        import hashlib
        h1 = hashlib.md5(open(file1, 'rb').read()).hexdigest()
        h2 = hashlib.md5(open(file2, 'rb').read()).hexdigest()
        return h1 == h2

    def generate_diff_report(self, file1, file2):
        """生成差异报告"""
        diff = self.compare_text(file1, file2)
        return f"=== 差异报告 ===\n文件1：{file1}\n文件2：{file2}\n\n{diff}"

comparator = FileComparator()

diff = comparator.compare_text("file_v1.txt", "file_v2.txt")
print(diff[:500])

result = comparator.compare_directories("./dir1", "./dir2")
print(f"仅在dir1：{result['only_in_dir1']}")
print(f"仅在dir2：{result['only_in_dir2']}")
print(f"有差异：{result['different']}")
```

