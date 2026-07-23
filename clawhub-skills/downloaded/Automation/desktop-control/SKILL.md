---
pricing_tier: L3
pricing_model: per_use
suggested_price: 29.9
---

**The most advanced desktop automation skill for Skill平台.** Provides pixel-perfect mouse control, lightning-fast keyboard input, screen capture, window management, and clipboard operations.

## 核心能力
### Mouse Control
* ✅ **Absolute positioning** - Move to exact coordinates
* ✅ **Relative movement** - Move from current position
* ✅ **Smooth movement** - Natural, human-like mouse paths
* ✅ **Click types** - Left, right, middle, double, triple clicks
* ✅ **Drag & drop** - Drag from point A to point B
* ✅ **Scroll** - Vertical and horizontal scrolling
* ✅ **Position tracking** - Get current mouse coordinates

### Keyboard Control
* ✅ **Text typing** - Fast, accurate text input
* ✅ **Hotkeys** - Execute keyboard shortcuts (Ctrl+C, Win+R, etc.)
* ✅ **Special keys** - Enter, Tab, Escape, Arrow keys, F-keys
* ✅ **Key combinations** - Multi-key press combinations
* ✅ **Hold & release** - Manual key state control
* ✅ **Typing speed** - Configurable WPM (instant to human-like)

### Screen Operations
* ✅ **Screenshot** - Capture entire screen or regions
* ✅ **Image recognition** - Find elements on screen (via OpenCV)
* ✅ **Color detection** - Get pixel colors at coordinates
* ✅ **Multi-monitor** - Support for multiple displays

### Window Management
* ✅ **Window list** - Get all open windows
* ✅ **Activate window** - Bring window to front
* ✅ **Window info** - Get position, size, title
* ✅ **Minimize/Maximize** - Control window states

### Safety Features
* ✅ **Failsafe** - Move mouse to corner to abort
* ✅ **Pause control** - Emergency stop mechanism
* ✅ **Approval mode** - Require confirmation for actions
* ✅ **Bounds checking** - Prevent out-of-screen operations
* ✅ **Logging** - Track all automation actions

## 使用流程
### Installation
First, install required dependencies:

```bash
pip install pyautogui pillow opencv-python pygetwindow
```

### Basic Usage
```python
from skills.desktop_control import DesktopController

dc = DesktopController(failsafe=True)

dc.move_mouse(500, 300)  # Move to coordinates
dc.click()  # Left click at current position
dc.click(100, 200, button="right")  # Right click at position
dc.type_text("Hello from Skill平台!")
dc.hotkey("ctrl", "c")  # Copy
dc.press("enter")

screenshot = dc.screenshot()
position = dc.get_mouse_position()
```

## 📋 Complete API Reference

> 详细内容已移至 `references/detail.md` - ### Mouse Functions

> 详细内容已移至 `references/detail.md` - ### Keyboard Functions

> 详细内容已移至 `references/detail.md` - ### Screen Functions
### Window Functions
#### `get_all_windows()`
List all open windows.

**Returns:** List of window titles

**Example:**

```python
windows = dc.get_all_windows()
for title in windows:
    print(f"Window: {title}")
```

#### `activate_window(title_substring)`
Bring window to front by title.

**Parameters:**

* `title_substring` (str): Part of window title to match

**Example:**

```python
dc.activate_window("Chrome")

dc.activate_window("Visual Studio Code")
```

#### `get_active_window()`
Get currently focused window.

**Returns:** Window title (str)

**Example:**

```python
active = dc.get_active_window()
print(f"Active window: {active}")
```

### Clipboard Functions
#### `copy_to_clipboard(text)`
Copy text to clipboard.

**Example:**

```python
dc.copy_to_clipboard("Hello from Skill平台!")
```

#### `get_from_clipboard()`
Get text from clipboard.

**Returns:** str

**Example:**

```python
text = dc.get_from_clipboard()
print(f"Clipboard: {text}")
```

## ⌨️ Key Names Reference
### Alphabet Keys
`'a'` through `'z'`

### Number Keys
`'0'` through `'9'`

### Function Keys
`'f1'` through `'f24'`

### Special Keys
* `'enter'` / `'return'`
* `'esc'` / `'escape'`
* `'space'` / `'spacebar'`
* `'tab'`
* `'backspace'`
* `'delete'` / `'del'`
* `'insert'`
* `'home'`
* `'end'`
* `'pageup'` / `'pgup'`
* `'pagedown'` / `'pgdn'`

### Arrow Keys
* `'up'` / `'down'` / `'left'` / `'right'`

### Modifier Keys
* `'ctrl'` / `'control'`
* `'shift'`
* `'alt'`
* `'win'` / `'winleft'` / `'winright'`
* `'cmd'` / `'command'` (Mac)

### Lock Keys
* `'capslock'`
* `'numlock'`
* `'scrolllock'`

### Punctuation
* `'.'` / `','` / `'?'` / `'!'` / `';'` / `':'`
* `'['` / `']'` / `'{'` / `'}'`
* `'('` / `')'`
* `'+'` / `'-'` / `'*'` / `'/'` / `'='`

## 🛡️ Safety Features
### Failsafe Mode
Move mouse to **any corner** of the screen to abort all automation.

```python
dc = DesktopController(failsafe=True)
```

### Pause Control
```python
dc.pause(2.0)

if dc.is_safe():
    dc.click(500, 500)
```

### Approval Mode
Require user confirmation before actions:

```python
dc = DesktopController(require_approval=True)

dc.click(500, 500)  # Prompt: "Allow click at (500, 500)? [y/n]"
```

## 示例
### Example 1: Automated Form Filling
```python
dc = DesktopController()

dc.click(300, 200)
dc.type_text("John Doe", wpm=80)

dc.press('tab')
dc.type_text("john@example.com", wpm=80)

dc.press('tab')
dc.type_text("SecurePassword123", wpm=60)

dc.press('enter')
```

### Example 2: Screenshot Region and Save
```python
region = (100, 100, 800, 600)  # left, top, width, height
img = dc.screenshot(region=region)

import datetime
timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
img.save(f"capture_{timestamp}.png")
```

### Example 3: Multi-File Selection
```python
dc.key_down('ctrl')
dc.click(100, 200)  # First file
dc.click(100, 250)  # Second file
dc.click(100, 300)  # Third file
dc.key_up('ctrl')

dc.hotkey('ctrl', 'c')
```

### Example 4: Window Automation
```python
dc.activate_window("Calculator")
time.sleep(0.5)

dc.type_text("5+3=", interval=0.2)
time.sleep(0.5)

dc.screenshot(filename="calculation_result.png")
```

### Example 5: Drag & Drop File
```python
dc.drag(
    start_x=200, start_y=300,  # File location
    end_x=800, end_y=500,       # Folder location
    duration=1.0                 # Smooth 1-second drag
)
```

## ⚡ Performance Tips
1. **Use instant movements** for speed: `duration=0`
2. **Batch operations** instead of individual calls
3. **Cache screen positions** instead of recalculating
4. **Disable failsafe** for maximum performance (use with caution)
5. **Use hotkeys** instead of menu navigation

## ⚠️ Important Notes
* **Screen coordinates** start at (0, 0) in top-left corner
* **Multi-monitor setups** may have negative coordinates for secondary displays
* **Windows DPI scaling** may affect coordinate accuracy
* **Failsafe corners** are: (0,0), (width-1, 0), (0, height-1), (width-1, height-1)
* **Some applications** may block simulated input (games, secure apps)

## 错误处理
### Mouse not moving to correct position
* Check DPI scaling settings
* Verify screen resolution matches expectations
* Use `get_screen_size()` to confirm dimensions

### Keyboard input not working
* Ensure target application has focus
* Some apps require admin privileges
* Try increasing `interval` for reliability

### Failsafe triggering accidentally
* Increase screen border tolerance
* Move mouse away from corners during normal use
* Disable if needed: `DesktopController(failsafe=False)`

### Permission errors
* Run Python with administrator privileges for some operations
* Some secure applications block automation

## 依赖说明
* **PyAutoGUI** - Core automation engine
* **Pillow** - Image processing
* **OpenCV** (optional) - Image recognition
* **PyGetWindow** - Window management

Install all:

```bash
pip install pyautogui pillow opencv-python pygetwindow
```

**Built for Skill平台** - The ultimate desktop automation companion 🦞

## 依赖说明
### 运行环境
- **Agent平台**: 支持SKILL.md的任意AI Agent(Claude Code / Cursor / Codex / Gemini CLI等)
- **操作系统**: Windows / macOS / Linux

### 第三方依赖
| 依赖项 | 类型 | 是否必需 | 获取方式 |
|:-------|:-----|:---------|:---------|
| LLM API | API | 必需 | 由Agent内置LLM提供 |

### API Key 配置
- 本Skill基于Markdown指令,无需额外API Key(除内容中明确标注的外部API)

### 可用性分类
- **分类**: MD+EXEC(纯Markdown指令,部分功能需要exec命令行执行能力)
- **说明**: 基于Markdown的AI Skill,通过自然语言指令驱动Agent执行任务

## 适用场景
| 场景 | 输入 | 输出 |
|------|------|------|
| 基础使用 | 用户请求 | 处理结果 |

**不适用于**：需要人工判断的复杂决策场景

## 常见问题
### Q1: 如何开始使用Desktop Control？
A: 请先阅读使用流程章节，确认环境满足依赖说明中的要求。

### Q2: 遇到错误怎么办？
A: 请参考错误处理章节，按照表格中的处理方式操作。

### Q3: Desktop Control有什么限制？
A: 请参考已知限制章节了解具体限制。

## 已知限制
- 需要API Key，无Key环境无法使用
