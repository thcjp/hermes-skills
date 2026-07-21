# 详细参考 - browser-automation-v2-tool-pro

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (python)

```python
import concurrent.futures
import threading

class BatchProcessor:
    """批量URL处理器（专业版）"""

    def __init__(self, max_workers=5, profile_lock=True):
        self.max_workers = max_workers
        self.profile_lock = profile_lock
        self.lock = threading.Lock() if profile_lock else None
        self.results = []
        self.stats = {"success": 0, "failed": 0, "total": 0}

    def process_single(self, url_item):
        """处理单个URL"""
        url = url_item.get("url")
        config = url_item.get("config", {})

        if self.lock:
            with self.lock:
                result = self._fetch_with_lock(url, config)
        else:
            result = self._fetch_with_lock(url, config)

        self.stats["total"] += 1
        if result.get("success"):
            self.stats["success"] += 1
        else:
            self.stats["failed"] += 1

        return {"url": url, "result": result}

    def _fetch_with_lock(self, url, config):
        """带锁保护的页面获取"""
        try:
            cmd = ["node", "multi-pages.js", url, "--config", json.dumps(config)]
            result = subprocess.run(cmd, capture_output=True, text=True, timeout=60)
            if result.returncode == 0:
                return json.loads(result.stdout)
            return {"success": False, "error": result.stderr}
        except Exception as e:
            return {"success": False, "error": str(e)}

    def process_batch(self, url_list):
        """批量处理URL列表"""
        print(f"启动批量处理，共 {len(url_list)} 个URL，并发数 {self.max_workers}")

        with concurrent.futures.ThreadPoolExecutor(max_workers=self.max_workers) as executor:
            futures = [executor.submit(self.process_single, item) for item in url_list]
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                self.results.append(result)
                status = "成功" if result["result"].get("success") else "失败"
                print(f"[{status}] {result['url']}")

        self._print_summary()
        return self.results

    def _print_summary(self):
        """打印处理摘要"""
        print("\n=== 批量处理摘要 ===")
        print(f"总数：{self.stats['total']}")
        print(f"成功：{self.stats['success']}")
        print(f"失败：{self.stats['failed']}")
        print(f"成功率：{self.stats['success']/self.stats['total']*100:.1f}%")

processor = BatchProcessor(max_workers=5, profile_lock=True)
urls = [
    {"url": "https://example.com/1", "config": {"extract": "title"}},
    {"url": "https://example.com/2", "config": {"extract": "price"}},
    {"url": "https://example.com/3", "config": {"extract": "content"}},
]
results = processor.process_batch(urls)
```

## 代码示例 (python)

```python
class AdvancedFormFiller:
    """复杂表单填写器（专业版）"""

    def fill_select(self, url, field_name, value):
        """填写select下拉框"""
        return self._fill_field(url, "select", field_name, value)

    def fill_radio(self, url, field_name, value):
        """填写radio单选"""
        return self._fill_field(url, "radio", field_name, value)

    def check_checkbox(self, url, field_name, checked=True):
        """勾选checkbox"""
        action = "check" if checked else "uncheck"
        return self._fill_field(url, "checkbox", field_name, action=action)

    def upload_file(self, url, field_name, file_path):
        """文件上传"""
        cmd = [
            "node", "fill-form.js", url,
            "--type", "file",
            "--field", field_name,
            "--file", file_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

    def fill_complex_form(self, url, fields):
        """填写复杂表单（多类型字段）"""
        results = []
        for field in fields:
            field_type = field.get("type", "text")
            name = field.get("name")
            value = field.get("value")

            if field_type == "select":
                r = self.fill_select(url, name, value)
            elif field_type == "radio":
                r = self.fill_radio(url, name, value)
            elif field_type == "checkbox":
                r = self.check_checkbox(url, name, value)
            elif field_type == "file":
                r = self.upload_file(url, name, value)
            else:
                r = self._fill_field(url, "text", name, value)

            results.append({"field": name, "success": r})
        return results

    def _fill_field(self, url, field_type, name, value=None, action=None):
        cmd = ["node", "fill-form.js", url, "--type", field_type, "--field", name]
        if value is not None:
            cmd.extend(["--value", str(value)])
        if action:
            cmd.extend(["--action", action])
        result = subprocess.run(cmd, capture_output=True, text=True)
        return result.returncode == 0

filler = AdvancedFormFiller()
fields = [
    {"name": "username", "type": "text", "value": "zhangsan"},
    {"name": "country", "type": "select", "value": "China"},
    {"name": "gender", "type": "radio", "value": "male"},
    {"name": "agree", "type": "checkbox", "value": True},
    {"name": "avatar", "type": "file", "value": "/path/to/avatar.jpg"},
]
results = filler.fill_complex_form("https://example.com/register", fields)
for r in results:
    status = "成功" if r["success"] else "失败"
    print(f"{status} 字段：{r['field']}")
```

## 代码示例 (python)

```python
import time

class CloudflareHandler:
    """Cloudflare绕过处理器（专业版）"""

    def __init__(self, max_wait=60, check_interval=2):
        self.max_wait = max_wait
        self.check_interval = check_interval

    def is_cloudflare_page(self, page_content):
        """检测是否为Cloudflare验证页面"""
        cf_indicators = [
            "Just a moment...",
            "Checking your browser",
            "cf-browser-verification",
            "cf-challenge-running",
            "_cf_chl_opt",
            "Ray ID:"
        ]
        return any(indicator in page_content for indicator in cf_indicators)

    def wait_for_resolution(self, page_handler):
        """等待Cloudflare验证通过"""
        print("[CF] 检测到Cloudflare验证页面，等待通过...")
        start = time.time()
        while time.time() - start < self.max_wait:
            content = page_handler.get_content()
            if not self.is_cloudflare_page(content):
                elapsed = time.time() - start
                print(f"[CF] Cloudflare验证通过，耗时 {elapsed:.1f}s")
                return True
            time.sleep(self.check_interval)
        print(f"[CF] 等待超时（{self.max_wait}s），请检查网络或IP")
        return False

    def auto_bypass(self, url):
        """自动绕过Cloudflare"""
        page = open_page(url)
        content = page.get("content", "")

        if self.is_cloudflare_page(content):
            success = self.wait_for_resolution(page)
            if success:
                return page  # 验证通过，返回真实页面
            return {"success": False, "error": "Cloudflare验证超时"}

        return page  # 非CF页面，直接返回
handler = CloudflareHandler(max_wait=60)
result = handler.auto_bypass("https://protected-site.com")
```

## 代码示例 (python)

```python
class ProfileLock:
    """Profile并发锁（专业版）"""

    def __init__(self, profile_name, timeout=30):
        self.profile_name = profile_name
        self.timeout = timeout
        self.lock_file = f"/tmp/browser_{profile_name}.lock"
        self.held = False

    def acquire(self):
        """获取锁"""
        import time
        start = time.time()
        while time.time() - start < self.timeout:
            try:
                with open(self.lock_file, "x") as f:
                    f.write(str(time.time()))
                self.held = True
                print(f"[LOCK] 已获取profile锁：{self.profile_name}")
                return True
            except FileExistsError:
                print(f"[LOCK] 等待profile释放：{self.profile_name}...")
                time.sleep(1)
        print(f"[LOCK] 获取锁超时：{self.profile_name}")
        return False

    def release(self):
        """释放锁"""
        if self.held:
            import os
            try:
                os.remove(self.lock_file)
                self.held = False
                print(f"[LOCK] 已释放profile锁：{self.profile_name}")
            except FileNotFoundError:
                pass

    def __enter__(self):
        self.acquire()
        return self

    def __exit__(self, *args):
        self.release()

with ProfileLock("company-profile", timeout=30):
    result = subprocess.run(["node", "search-google.js", "查询"])
```

## 代码示例 (python)

```python
class PageExporter:
    """页面导出工具（专业版）"""

    def screenshot(self, url, output_path, full_page=True, format="png"):
        """页面截图"""
        cmd = [
            "node", "screenshot.js",
            "--url", url,
            "--output", output_path,
            "--format", format,
            "--full-page", str(full_page).lower()
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[截图] 已保存：{output_path}")
            return True
        print(f"[截图] 失败：{result.stderr}")
        return False

    def export_pdf(self, url, output_path, format="A4", margin="1cm"):
        """导出PDF"""
        cmd = [
            "node", "export-pdf.js",
            "--url", url,
            "--output", output_path,
            "--format", format,
            "--margin", margin
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        if result.returncode == 0:
            print(f"[PDF] 已保存：{output_path}")
            return True
        print(f"[PDF] 失败：{result.stderr}")
        return False

    def full_export(self, url, base_output):
        """完整导出（截图+PDF）"""
        self.screenshot(url, f"{base_output}.png")
        self.export_pdf(url, f"{base_output}.pdf")

exporter = PageExporter()
exporter.full_export("https://example.com", "./output/report")
```

