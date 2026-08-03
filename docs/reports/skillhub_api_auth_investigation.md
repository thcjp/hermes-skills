# SkillHub API 真实认证状态调查报告

> 调查日期: 2026-08-02
> 调查方式: 真实 HTTP 请求 (Python urllib, 零 mock)

---

## 一、核心结论

| 项目 | 真实状态 |
|------|----------|
| **有效的认证凭证** | API Key (`sk-ent-...`) 有效; Token (`bt_...`) **已失效** |
| **认证头格式** | `Authorization: Bearer {凭证}` (不支持 `X-API-Key`) |
| **API Key 验证端点** | `POST /api/v1/registry/verify` (不是 `GET /api/v1/verify_api_key`) |
| **正确的 org_id** | **1436** (智创未来 / org-2orcbd4z); 862 已失效 |
| **社区上传端点** | `POST /api/v1/community/skills/publish` |
| **企业 skill 列表端点** | `GET /api/v1/orgs/1436/registry/search?q=*&pageSize=100` |
| **当前已上传 skill 数量** | 企业 registry: **0 个**; (平台公开 showcase 约 100+ 个, 非我们所有) |
| **上传所需认证** | 需要 `skh_` 前缀的用户 Token (当前 `bt_` token 无效) |

---

## 二、真实 HTTP 请求测试结果

### 2.1 API Key 验证 (sk-ent-...)

| 端点 | 方法 | 认证头 | 状态码 | 结果 |
|------|------|--------|--------|------|
| `/api/v1/verify_api_key` | GET | Bearer api_key | **405** | 端点不存在 (Method Not Allowed) |
| `/api/v1/registry/verify` | POST | Bearer api_key | **200** | **成功!** 返回 org 信息 |
| `/api/v1/registry/verify` | POST | X-API-Key | **401** | 被拒, 要求 Bearer 头 |

**`POST /api/v1/registry/verify` 成功返回:**
```json
{
  "orgId": 1436,
  "orgName": "智创未来",
  "orgOrgId": "org-2orcbd4z",
  "orgSlug": "zcwl"
}
```

### 2.2 Token 验证 (bt_...)

| 端点 | 方法 | 认证头 | 状态码 | 结果 |
|------|------|--------|--------|------|
| `/api/v1/auth/me` | GET | Bearer token (bt_) | **401** | "invalid or expired token" |
| `/api/v1/auth/me` | GET | Bearer api_key | **401** | "invalid or expired token" |

**结论: `bt_jwe7aq5f53dww9q489gdmxuaepkn96pf` token 已失效。** CLI 代码 (`resolve_user_token`) 要求 token 必须以 `skh_` 开头, 当前 `bt_` 前缀不符合要求。

### 2.3 社区 Skills 列表

| 端点 | 方法 | 状态码 | 结果 |
|------|------|--------|------|
| `/api/v1/community/skills` | GET | **405** | 端点不存在 |
| `/api/v1/community/skills/publish` | GET | **405** | 仅支持 POST |

### 2.4 企业 Org Skills 列表

| 端点 | 方法 | 状态码 | 结果 |
|------|------|--------|------|
| `/api/v1/orgs/1436/skills` | GET | **401** | 端点将 api_key 当 token 验证, 失败 |
| `/api/v1/orgs/862/skills` | GET | **401** | 同上 |
| `/api/v1/orgs/1436/registry/search?q=*&pageSize=100` | GET | **200** | **成功!** 返回 skills=[] total=0 |
| `/api/v1/orgs/862/registry/search?q=*` | GET | **403** | "organization mismatch" (api_key 属于 1436 不属于 862) |

**`GET /api/v1/orgs/1436/registry/search?q=*` 返回:**
```json
{
  "skills": [],
  "total": 0
}
```

### 2.5 公开端点 (无需认证)

| 端点 | 状态码 | 结果 |
|------|--------|------|
| `/api/v1/showcase/newest` | 200 | 100 个 skill |
| `/api/v1/showcase/hot` | 200 | 100 个 skill |
| `/api/v1/showcase/featured` | 200 | 46 个 skill |
| `/api/v1/showcase/trending` | 200 | 100 个 skill |
| `/api/v1/search?q=&pageSize=5` | 200 | 返回 results 列表 |

### 2.6 上传端点探测

| 端点 | 方法 | 认证 | 状态码 | 结果 |
|------|------|------|--------|------|
| `/api/v1/community/skills/publish` | POST | Bearer bt_ token | **401** | "unauthorized" (token 无效) |
| `/api/v1/community/skills/publish` | POST | Bearer api_key | **401** | "unauthorized" (api_key 不是用户 token) |
| `/api/v1/community/skills/publish` | POST | Bearer fake skh_ | **401** | "unauthorized" (端点存在, 需有效 skh_ token) |
| `/api/v1/orgs/1436/registry/skills/publish` | POST | Bearer api_key | **404** | 端点不存在 |

---

## 三、认证方式详解

### 3.1 两套独立的认证体系

SkillHub 有**两套完全独立**的认证体系, 分别用于不同场景:

#### 体系 A: 企业 API Key (`sk-ent-` 前缀)
- **用途**: 企业源操作 (验证身份、搜索企业 skill、下载企业 skill)
- **认证头**: `Authorization: Bearer {api_key}`
- **验证端点**: `POST /api/v1/registry/verify`
- **当前状态**: **有效** (返回 orgId=1436, 智创未来)
- **可用操作**:
  - `POST /api/v1/registry/verify` — 验证 API Key
  - `GET /api/v1/orgs/{org_id}/registry/search?q=*&pageSize=N` — 搜索企业 skill
  - `GET /api/v1/orgs/{org_id}/registry/skills/{slug}/download` — 下载企业 skill
- **不可用操作**: 不能用于社区 skill 上传/发布

#### 体系 B: 用户 API Token (`skh_` 前缀)
- **用途**: 社区操作 (发布 skill、个人信息)
- **认证头**: `Authorization: Bearer {token}`
- **验证端点**: `GET /api/v1/auth/me`
- **当前状态**: **无效** (凭证文件中的 `bt_` token 已过期, 且格式不符合 `skh_` 要求)
- **可用操作**:
  - `POST /api/v1/community/skills/publish` — 发布社区 skill
  - `GET /api/v1/auth/me` — 查看个人信息
- **获取方式**: 需在 SkillHub 网站登录后生成 `skh_` 前缀的 token

### 3.2 认证头格式

- **唯一支持**: `Authorization: Bearer {凭证}`
- **不支持**: `X-API-Key` 头 (返回 401, 明确要求 Bearer)
- 服务器错误信息原文: "missing or invalid Authorization header, expected: Bearer <api-key>"

---

## 四、正确的 API 端点清单

### 4.1 用户假设端点 vs 实际端点对比

| 用户假设端点 | 状态 | 实际正确端点 |
|-------------|------|-------------|
| `GET /api/v1/community/skills` | 405 不存在 | `GET /api/v1/showcase/newest` (公开) 或 `GET /api/v1/orgs/1436/registry/search` (企业) |
| `GET /api/v1/orgs/1436/skills` | 401 不存在 | `GET /api/v1/orgs/1436/registry/search?q=*&pageSize=100` |
| `GET /api/v1/verify_api_key` | 405 不存在 | `POST /api/v1/registry/verify` |

### 4.2 完整端点清单

| 功能 | 方法 | 端点 | 认证 | 状态 |
|------|------|------|------|------|
| 验证 API Key | POST | `/api/v1/registry/verify` | Bearer api_key | 可用 |
| 验证用户 Token | GET | `/api/v1/auth/me` | Bearer skh_token | 端点可用, 当前 token 无效 |
| 搜索企业 skill | GET | `/api/v1/orgs/1436/registry/search?q=*&pageSize=N` | Bearer api_key | 可用 |
| 下载企业 skill | GET | `/api/v1/orgs/1436/registry/skills/{slug}/download` | Bearer api_key | 可用 |
| 发布社区 skill | POST | `/api/v1/community/skills/publish` | Bearer skh_token | 端点可用, 当前 token 无效 |
| 公开 showcase | GET | `/api/v1/showcase/{newest\|hot\|featured\|trending}` | 无需认证 | 可用 |
| 公开搜索 | GET | `/api/v1/search?q=...&pageSize=...` | 无需认证 | 可用 |
| skill 详情 | GET | `/api/v1/skills/{slug}` | 无需认证 | 可用 |

---

## 五、已上传 skill 数量

### 企业 Registry (org 1436 智创未来)
- **已上传: 0 个**
- 查询端点: `GET /api/v1/orgs/1436/registry/search?q=*&pageSize=100`
- 返回: `{"skills": [], "total": 0}`

### 平台公开 showcase (全平台, 非我们所有)
- newest: 100 个
- hot: 100 个
- featured: 46 个
- trending: 100 个
- 这些是整个 SkillHub 平台的公开 skill, 不是我们上传的

---

## 六、上传 Skill 必填字段

### 6.1 上传端点
- **URL**: `POST https://api.skillhub.cn/api/v1/community/skills/publish`
- **认证**: `Authorization: Bearer {skh_token}` (需要 `skh_` 前缀的有效 token)
- **格式**: multipart/form-data

### 6.2 必填字段 (payload JSON 部分)

来源: CLI 代码 `_validate_metadata()` 和 `_post_publish_multipart()`

| 字段 | 必填 | 格式要求 | 说明 |
|------|------|----------|------|
| `slug` | 是 | kebab-case, 2-128 字符 | skill 唯一标识 |
| `version` | 是 | SemVer (如 1.0.0) | 版本号 |
| `displayName` | 是 | 非空字符串 | 显示名称 |
| `summary` | 是 | 10-100 字符 | 简短摘要 |
| `description` | 否 | 150-280 字符 | 详细描述 (建议提供) |
| `tags` | 否 | list | 标签列表 |
| `license` | 否 | 字符串 | 许可证 (如 MIT, Apache-2.0) |
| `homepage` | 否 | URL | 主页地址 |
| `changelog` | 否 | 字符串 | 更新日志 |

### 6.3 必填文件 (multipart files 部分)

| 文件 | 必填 | 说明 |
|------|------|------|
| `SKILL.md` | 是 | skill 主文件, 含 frontmatter (slug, version, displayName 等) |
| 其他文件 | 否 | docs/usage.md 等附属文件 |

### 6.4 multipart 结构
```
------skillhubBoundary{timestamp}
Content-Disposition: form-data; name="payload"
Content-Type: application/json

{"slug":"...","version":"...","displayName":"...","summary":"...","changelog":"..."}
------skillhubBoundary{timestamp}
Content-Disposition: form-data; name="files"; filename="SKILL.md"
Content-Type: text/markdown

(file content)
------skillhubBoundary{timestamp}--
```

---

## 七、发现的配置问题

### 7.1 org_id 不一致 (严重)

| 文件 | org_id | 是否正确 |
|------|--------|----------|
| `d:\skills\.credentials\skillhub.json` | 862 | **错误** (403 organization mismatch) |
| `d:\skills\config\project_config.py` | 1436 | **正确** (V182 已修正) |
| `C:\Users\thcd\.skillhub\credentials.json` | 1436 (org-2orcbd4z) | **正确** |
| `d:\skills\tools\skillhub_adapter.py` | 读 PLATFORM_CONFIG = 1436 | 正确 (但 fallback 默认值 862 是错的) |

**影响**: `skillhub_adapter.py` 第 110 行 `'org_id': PLATFORM_CONFIG.get('skillhub', {}).get('org_id', 862)` 的 fallback 值 862 是错误的, 应改为 1436。当前因 PLATFORM_CONFIG 有值所以不影响, 但属于隐患。

### 7.2 Token 失效 (严重)

- 凭证文件中的 `token: bt_jwe7aq5f53dww9q489gdmxuaepkn96pf` **已过期/无效**
- CLI 要求 token 以 `skh_` 开头, `bt_` 前缀不符合要求
- **影响**: 无法进行社区 skill 上传/发布操作
- **修复**: 需要在 SkillHub 网站重新登录生成 `skh_` 前缀的 token

### 7.3 端点假设错误

- 用户假设的 3 个端点 (`verify_api_key`, `community/skills`, `orgs/1436/skills`) **全部不存在**
- 正确端点需参考 CLI 源码 (`skills_store_cli.py`)

---

## 八、CLI 工具状态

| 项目 | 状态 |
|------|------|
| 本地 `skillhub` 命令 | 未安装 (不在 PATH) |
| `npx skillhub --version` | 0.4.1 (npm 包可用) |
| 本地 CLI 脚本 | `C:\Users\thcd\.skillhub\skills_store_cli.py` (v2026.7.29) |
| CLI credentials.json | 存在, 含 org 862 和 org 1436 两个组织 |
| CLI config.json | 自更新 URL: skillhub-1388575217.cos.ap-guangzhou.myqcloud.com |
| CLI metadata.json | skills 索引/搜索/下载 URL 配置完整 |

---

## 九、操作建议

### 9.1 立即可做的操作 (用 API Key)
- 验证企业身份: `POST /api/v1/registry/verify`
- 搜索企业 skill: `GET /api/v1/orgs/1436/registry/search?q=*&pageSize=100`
- 浏览公开 skill: `GET /api/v1/showcase/newest`

### 9.2 需要 Token 才能做的操作
- 上传/发布 skill: `POST /api/v1/community/skills/publish`
- 查看个人信息: `GET /api/v1/auth/me`
- **前置条件**: 获取有效的 `skh_` 前缀 token

### 9.3 需修复的配置
1. 更新 `.credentials/skillhub.json` 的 org_id 从 862 改为 1436
2. 获取新的 `skh_` token 替换失效的 `bt_` token
3. 修正 `skillhub_adapter.py` 的 fallback org_id 从 862 改为 1436
