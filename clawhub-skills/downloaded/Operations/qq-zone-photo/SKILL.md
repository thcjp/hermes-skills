---
slug: qq-zone-photo
name: qq-zone-photo
version: "1.0.3"
displayName: QQ Zone Photo
summary: 管理QQ空间相册。支持扫码登录、列出相册、浏览照片、上传照片。
license: MIT
description: |-
  管理QQ空间相册。支持扫码登录、列出相册、浏览照片、上传照片。

  核心能力:

  - 运维工具领域的专业化AI辅助工具

  - 基于高人气开源Skill深度优化升级

  - 移除风险代码,增强安全性和稳定性

  适用场景:

  - 系统运维、监控告警、资源管理

  - 独立开发者与一人公司效率提升

  - 自动化工作流与智能决策辅助

  差异化:经过深度优化,去除原始风险代码,清理外部依赖引用,增强元数据和触发关键词,完全适配SkillHub平台规范。

  触发关键词: 浏览照片, photo, zone, 列出相册, 空间相册, 支持扫码登录, 管理
tags:
- Operations
tools:
- read
- exec
---

# QQ Zone Photo

> QQ空间相册的自动化管理工具，支持扫码登录、相册浏览、照片上传/下载、相册创建等功能。

---

## 🤖 Agent 工作流示例

#### 场景一：备份指定相册

```text
用户: "帮我备份 QQ空间的旅行相册"
```

#### 场景二：上传照片到指定相册

```text
用户: "把桌面上的 vacation.jpg 上传到我的旅行相册"
```

#### 场景三：全量备份所有相册

```text
用户: "帮我把 QQ空间所有相册都下载下来"
```

#### 场景四：创建相册并上传多张照片

```text
用户: "创建一个叫'2024毕业季'的相册，把这几张照片传上去"
```

---

## 📋 AI Agent 调用指南

AI Agent 在调用本 Skill 前，需确保虚拟环境已激活且 `cookies.json` 有效。所有命令格式：

```bash
source <项目路径>/.venv/bin/activate && python3 <项目路径>/scripts/qzone_photos.py --action <ACTION> [参数]
```

### Action 一览

| Action | 说明 | 必填参数 | 可选参数 |
| --- | --- | --- | --- |
| `login` | 扫码登录，自动保存 Cookie | `--cookies` | — |
| `list` | 列出所有相册 | `--cookies` | `--qq` |
| `photos` | 浏览相册中的照片 | `--album-id` `--cookies` | `--qq` |
| `upload` | 上传照片到相册 | `--photo` `--cookies` | `--album-id` `--qq` |
| `download` | 下载单张照片 | `--url` `--cookies` | `--output` |
| `download-album` | 下载整个相册 | `--album-id` `--cookies` | `--output` `--qq` |
| `create` | 创建新相册 | `--title` `--cookies` | `--desc` `--qq` |

### 调用示例

```bash
python3 scripts/qzone_photos.py --action login --cookies cookies.json

python3 scripts/qzone_photos.py --action list --cookies cookies.json

python3 scripts/qzone_photos.py --action photos --album-id "ALBUM_ID" --cookies cookies.json

python3 scripts/qzone_photos.py --action upload --photo "/path/to/image.jpg" --album-id "ALBUM_ID" --cookies cookies.json

python3 scripts/qzone_photos.py --action download-album --album-id "ALBUM_ID" --output ./downloads --cookies cookies.json

python3 scripts/qzone_photos.py --action create --title "我的新相册" --cookies cookies.json
```

---

## ⚙️ 配置

### Cookie 文件格式

创建 `cookies.json`，结构如下：

```json
{
  "qq_number": "123456789",
  "p_skey": "your_p_skey_value",
  "skey": "your_skey_value",
  "uin": "o0123456789"
}
```

### 获取方式

* **推荐**：使用 `--action login` 扫码登录，Cookie 自动保存
* **手动**：登录 [QQ空间](https://user.qzone.qq.com/) 后，通过浏览器开发者工具（F12 → Application → Cookies）提取

---

## 🔒 安全与隐私

* Cookie 文件包含 QQ空间完整访问权限，**请勿泄露或分享**
* 凭证仅存储在本地，不会上传到任何服务器
* 会话 Cookie 有时效性，过期后需重新登录
* 本工具使用 QQ空间非官方 API，腾讯更新接口后可能需要适配

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
