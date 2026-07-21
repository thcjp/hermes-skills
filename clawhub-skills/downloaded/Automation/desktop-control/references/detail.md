# 详细参考 - desktop-control

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

### Mouse Functions
#### `move_mouse(x, y, duration=0, smooth=True)`
Move mouse to absolute screen coordinates.

**Parameters:**

* `x` (int): X coordinate (pixels from left)
* `y` (int): Y coordinate (pixels from top)
* `duration` (float): Movement time in seconds (0 = instant, 0.5 = smooth)
* `smooth` (bool): Use bezier curve for natural movement

**Example:**

```python
dc.move_mouse(1000, 500)

dc.move_mouse(1000, 500, duration=1.0)
```

#### `move_relative(x_offset, y_offset, duration=0)`
Move mouse relative to current position.

**Parameters:**

* `x_offset` (int): Pixels to move horizontally (positive = right)
* `y_offset` (int): Pixels to move vertically (positive = down)
* `duration` (float): Movement time in seconds

**Example:**

```python
dc.move_relative(100, 50, duration=0.3)
```

#### `click(x=None, y=None, button='left', clicks=1, interval=0.1)`
Perform mouse click.

**Parameters:**

* `x, y` (int, optional): Coordinates to click (None = current position)
* `button` (str): 'left', 'right', 'middle'
* `clicks` (int): Number of clicks (1 = single, 2 = double)
* `interval` (float): Delay between multiple clicks

**Example:**

```python
dc.click()

dc.click(500, 300, clicks=2)

dc.click(button='right')
```

#### `drag(start_x, start_y, end_x, end_y, duration=0.5, button='left')`
Drag and drop operation.

**Parameters:**

* `start_x, start_y` (int): Starting coordinates
* `end_x, end_y` (int): Ending coordinates
* `duration` (float): Drag duration
* `button` (str): Mouse button to use

**Example:**

```python
dc.drag(100, 100, 500, 500, duration=1.0)
```

#### `scroll(clicks, direction='vertical', x=None, y=None)`
Scroll mouse wheel.

**Parameters:**

* `clicks` (int): Scroll amount (positive = up/left, negative = down/right)
* `direction` (str): 'vertical' or 'horizontal'
* `x, y` (int, optional): Position to scroll at

**Example:**

```python
dc.scroll(-5)

dc.scroll(10)

dc.scroll(5, direction='horizontal')
```

#### `get_mouse_position()`
Get current mouse coordinates.

**Returns:** `(x, y)` tuple

**Example:**

```python
x, y = dc.get_mouse_position()
print(f"Mouse is at: {x}, {y}")
```



### Keyboard Functions
#### `type_text(text, interval=0, wpm=None)`
Type text with configurable speed.

**Parameters:**

* `text` (str): Text to type
* `interval` (float): Delay between keystrokes (0 = instant)
* `wpm` (int, optional): Words per minute (overrides interval)

**Example:**

```python
dc.type_text("Hello World")

dc.type_text("Hello World", wpm=60)

dc.type_text("Hello World", interval=0.1)
```

#### `press(key, presses=1, interval=0.1)`
Press and release a key.

**Parameters:**

* `key` (str): Key name (see Key Names section)
* `presses` (int): Number of times to press
* `interval` (float): Delay between presses

**Example:**

```python
dc.press('enter')

dc.press('space', presses=3)

dc.press('down')
```

#### `hotkey(*keys, interval=0.05)`
Execute keyboard shortcut.

**Parameters:**

* `*keys` (str): Keys to press together
* `interval` (float): Delay between key presses

**Example:**

```python
dc.hotkey('ctrl', 'c')

dc.hotkey('ctrl', 'v')

dc.hotkey('win', 'r')

dc.hotkey('ctrl', 's')

dc.hotkey('ctrl', 'a')
```

#### `key_down(key)` / `key_up(key)`
Manually control key state.

**Example:**

```python
dc.key_down('shift')
dc.type_text("hello")  # Types "HELLO"
dc.key_up('shift')

dc.key_down('ctrl')
dc.click(100, 100)
dc.click(200, 100)
dc.key_up('ctrl')
```



### Screen Functions
#### `screenshot(region=None, filename=None)`
Capture screen or region.

**Parameters:**

* `region` (tuple, optional): (left, top, width, height) for partial capture
* `filename` (str, optional): Path to save image

**Returns:** PIL Image object

**Example:**

```python
img = dc.screenshot()

dc.screenshot(filename="screenshot.png")

img = dc.screenshot(region=(100, 100, 500, 300))
```

#### `get_pixel_color(x, y)`
Get color of pixel at coordinates.

**Returns:** RGB tuple `(r, g, b)`

**Example:**

```python
r, g, b = dc.get_pixel_color(500, 300)
print(f"Color at (500, 300): RGB({r}, {g}, {b})")
```

#### `find_on_screen(image_path, confidence=0.8)`
Find image on screen (requires OpenCV).

**Parameters:**

* `image_path` (str): Path to template image
* `confidence` (float): Match threshold (0-1)

**Returns:** `(x, y, width, height)` or None

**Example:**

```python
location = dc.find_on_screen("button.png")
if location:
    x, y, w, h = location
    dc.click(x + w//2, y + h//2)
```

#### `get_screen_size()`
Get screen resolution.

**Returns:** `(width, height)` tuple

**Example:**

```python
width, height = dc.get_screen_size()
print(f"Screen: {width}x{height}")
```



