# 详细参考 - slack-api

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

### Conversations (Channels)
#### List Channels
```bash
GET /slack/api/conversations.list?types=public_channel,private_channel&limit=100
```

Types: `public_channel`, `private_channel`, `im`, `mpim`

Example:

```bash
maton slack channel list --types public_channel,private_channel --limit 100
```

#### Get Channel Info
```bash
GET /slack/api/conversations.info?channel=C0123456789
```

Example:

```bash
maton slack channel view C0123456789
```

#### Get Channel History
```bash
GET /slack/api/conversations.history?channel=C0123456789&limit=100
```

Example:

```bash
maton slack message list --channel C0123456789 --limit 100
```

With time range:

```bash
GET /slack/api/conversations.history?channel=C0123456789&oldest=1234567890&latest=1234567899
```

Example:

```bash
maton slack message list --channel C0123456789 --oldest 1234567890 --latest 1234567899
```

#### Get Thread Replies
```bash
GET /slack/api/conversations.replies?channel=C0123456789&ts=1234567890.123456
```

Example:

```bash
maton slack message replies --channel C0123456789 --ts 1234567890.123456
```

#### Get Channel Members
```bash
GET /slack/api/conversations.members?channel=C0123456789&limit=100
```

Example:

```bash
maton slack channel members C0123456789 --limit 100
```

#### Create Channel
```bash
POST /slack/api/conversations.create
Content-Type: application/json

{
  "name": "new-channel-name",
  "is_private": false
}
```

Example:

```bash
maton slack channel create --name new-channel-name
```

#### Join Channel
```bash
POST /slack/api/conversations.join
Content-Type: application/json

{
  "channel": "C0123456789"
}
```

Example:

```bash
maton slack channel join C0123456789
```

#### Leave Channel
```bash
POST /slack/api/conversations.leave
Content-Type: application/json

{
  "channel": "C0123456789"
}
```

Example:

```bash
maton slack channel leave C0123456789
```

#### Archive Channel
```bash
POST /slack/api/conversations.archive
Content-Type: application/json

{
  "channel": "C0123456789"
}
```

Example:

```bash
maton slack channel archive C0123456789
```

#### Unarchive Channel
```bash
POST /slack/api/conversations.unarchive
Content-Type: application/json

{
  "channel": "C0123456789"
}
```

Example:

```bash
maton slack channel unarchive C0123456789
```

#### Rename Channel
```bash
POST /slack/api/conversations.rename
Content-Type: application/json

{
  "channel": "C0123456789",
  "name": "new-name"
}
```

Example:

```bash
maton slack channel rename C0123456789 --name new-name
```

#### Set Channel Topic
```bash
POST /slack/api/conversations.setTopic
Content-Type: application/json

{
  "channel": "C0123456789",
  "topic": "Channel topic here"
}
```

Example:

```bash
maton slack channel set-topic C0123456789 --topic 'Channel topic here'
```

#### Set Channel Purpose
```bash
POST /slack/api/conversations.setPurpose
Content-Type: application/json

{
  "channel": "C0123456789",
  "purpose": "Channel purpose here"
}
```

Example:

```bash
maton slack channel set-purpose C0123456789 --purpose 'Channel purpose here'
```

#### Invite to Channel
```bash
POST /slack/api/conversations.invite
Content-Type: application/json

{
  "channel": "C0123456789",
  "users": "U0123456789,U9876543210"
}
```

Example:

```bash
maton slack channel invite C0123456789 --users U0123456789,U9876543210
```

#### Kick from Channel
```bash
POST /slack/api/conversations.kick
Content-Type: application/json

{
  "channel": "C0123456789",
  "user": "U0123456789"
}
```

Example:

```bash
maton slack channel kick C0123456789 --user U0123456789
```

#### Mark Channel Read
```bash
POST /slack/api/conversations.mark
Content-Type: application/json

{
  "channel": "C0123456789",
  "ts": "1234567890.123456"
}
```

Example:

```bash
maton slack channel mark C0123456789 --ts 1234567890.123456
```



### Messages
#### Post Message
```bash
POST /slack/api/chat.postMessage
Content-Type: application/json

{
  "channel": "C0123456789",
  "text": "Hello, world!"
}
```

Example:

```bash
maton slack message send --channel C0123456789 --text 'Hello, world!'
```

With blocks:

```bash
POST /slack/api/chat.postMessage
Content-Type: application/json

{
  "channel": "C0123456789",
  "blocks": [
    {"type": "section", "text": {"type": "mrkdwn", "text": "*Bold* and _italic_"}}
  ]
}
```

Example:

```bash
maton slack message send --channel C0123456789 --blocks '[{"type":"section","text":{"type":"mrkdwn","text":"*Bold* and _italic_"}}]'
```

#### Post /me-style Message
```bash
maton slack message me --channel C0123456789 --text 'is deploying'
```

#### Post Thread Reply
```bash
POST /slack/api/chat.postMessage
Content-Type: application/json

{
  "channel": "C0123456789",
  "thread_ts": "1234567890.123456",
  "text": "This is a reply in a thread"
}
```

Example:

```bash
maton slack message reply --channel C0123456789 --thread-ts 1234567890.123456 --text 'This is a reply in a thread'
```

#### Update Message
```bash
POST /slack/api/chat.update
Content-Type: application/json

{
  "channel": "C0123456789",
  "ts": "1234567890.123456",
  "text": "Updated message"
}
```

Example:

```bash
maton slack message update --channel C0123456789 --ts 1234567890.123456 --text 'Updated message'
```

#### Delete Message
```bash
POST /slack/api/chat.delete
Content-Type: application/json

{
  "channel": "C0123456789",
  "ts": "1234567890.123456"
}
```

Example:

```bash
maton slack message delete --channel C0123456789 --ts 1234567890.123456
```

#### Schedule Message
```bash
POST /slack/api/chat.scheduleMessage
Content-Type: application/json

{
  "channel": "C0123456789",
  "text": "Scheduled message",
  "post_at": 1734567890
}
```

Example:

```bash
maton slack schedule create --channel C0123456789 --text 'Scheduled message' --post-at 1734567890
```

#### List Scheduled Messages
```bash
GET /slack/api/chat.scheduledMessages.list
```

Example:

```bash
maton slack schedule list
```

#### Delete Scheduled Message
```bash
POST /slack/api/chat.deleteScheduledMessage
Content-Type: application/json

{
  "channel": "C0123456789",
  "scheduled_message_id": "Q1234567890"
}
```

Example:

```bash
maton slack schedule delete --channel C0123456789 --id Q1234567890
```

#### Get Permalink
```bash
GET /slack/api/chat.getPermalink?channel=C0123456789&message_ts=1234567890.123456
```

Example:

```bash
maton slack message permalink --channel C0123456789 --message-ts 1234567890.123456
```



### Files
#### List Files
```bash
GET /slack/api/files.list?count=100
```

Filter by channel, user, or file types:

```bash
GET /slack/api/files.list?channel=C0123456789&user=U0123456789&types=images,pdfs
```

Example:

```bash
maton slack file list --count 100
```

```bash
maton slack file list --channel C0123456789 --user U0123456789 --types images,pdfs
```

#### Upload File
```bash
POST /slack/api/files.upload
Content-Type: multipart/form-data

channels=C0123456789
content=file content here
filename=example.txt
title=Example File
```

#### Upload File v2 (Get Upload URL)
```bash
GET /slack/api/files.getUploadURLExternal?filename=example.txt&length=1024
```

#### Complete File Upload
```bash
POST /slack/api/files.completeUploadExternal
Content-Type: application/json

{
  "files": [{"id": "F0123456789", "title": "My File"}],
  "channel_id": "C0123456789"
}
```

Example:

```bash
maton slack file upload --file ./example.txt --channel C0123456789 --title 'My File'
```

#### Delete File
```bash
POST /slack/api/files.delete
Content-Type: application/json

{
  "file": "F0123456789"
}
```

Example:

```bash
maton slack file delete F0123456789
```

#### Get File Info
```bash
GET /slack/api/files.info?file=F0123456789
```

Example:

```bash
maton slack file view F0123456789
```



### Direct Messages
#### Open DM Conversation
```bash
POST /slack/api/conversations.open
Content-Type: application/json

{
  "users": "U0123456789"
}
```

Example:

```bash
maton slack conversation open --users U0123456789
```

For group DM:

```bash
POST /slack/api/conversations.open
Content-Type: application/json

{
  "users": "U0123456789,U9876543210"
}
```

Example:

```bash
maton slack conversation open --users U0123456789,U9876543210
```

#### List DM Channels
```bash
GET /slack/api/conversations.list?types=im
```

Example:

```bash
maton slack channel list --types im
```

#### List Group DM Channels
```bash
GET /slack/api/conversations.list?types=mpim
```

Example:

```bash
maton slack channel list --types mpim
```

#### My Conversations
```bash
GET /slack/api/users.conversations?limit=100
```

Example:

```bash
maton slack conversation list --limit 100
```



### Bookmarks
#### List Bookmarks
```bash
GET /slack/api/bookmarks.list?channel_id=C0123456789
```

Example:

```bash
maton slack bookmark list --channel C0123456789
```

#### Add Bookmark
```bash
POST /slack/api/bookmarks.add
Content-Type: application/json

{
  "channel_id": "C0123456789",
  "title": "Team Handbook",
  "type": "link",
  "link": "https://example.com/handbook"
}
```

Example:

```bash
maton slack bookmark add --channel C0123456789 --title 'Team Handbook' --type link --link https://example.com/handbook
```

#### Edit Bookmark
```bash
POST /slack/api/bookmarks.edit
Content-Type: application/json

{
  "bookmark_id": "Bk0123456789",
  "channel_id": "C0123456789",
  "title": "Updated Title",
  "link": "https://example.com/new"
}
```

Example:

```bash
maton slack bookmark edit --channel C0123456789 --bookmark-id Bk0123456789 --title 'Updated Title' --link https://example.com/new
```

#### Remove Bookmark
```bash
POST /slack/api/bookmarks.remove
Content-Type: application/json

{
  "bookmark_id": "Bk0123456789",
  "channel_id": "C0123456789"
}
```

Example:

```bash
maton slack bookmark remove --channel C0123456789 --bookmark-id Bk0123456789
```



### Reactions
#### Add Reaction
```bash
POST /slack/api/reactions.add
Content-Type: application/json

{
  "channel": "C0123456789",
  "name": "thumbsup",
  "timestamp": "1234567890.123456"
}
```

Example:

```bash
maton slack reaction add --channel C0123456789 --ts 1234567890.123456 --emoji thumbsup
```

#### Remove Reaction
```bash
POST /slack/api/reactions.remove
Content-Type: application/json

{
  "channel": "C0123456789",
  "name": "thumbsup",
  "timestamp": "1234567890.123456"
}
```

Example:

```bash
maton slack reaction remove --channel C0123456789 --ts 1234567890.123456 --emoji thumbsup
```

#### Get Reactions on Message
```bash
GET /slack/api/reactions.get?channel=C0123456789&timestamp=1234567890.123456
```

Example:

```bash
maton slack reaction get --channel C0123456789 --ts 1234567890.123456
```

#### List My Reactions
```bash
GET /slack/api/reactions.list?limit=100
```

Example:

```bash
maton slack reaction list --limit 100
```




## Quick Start
**CLI:**

```bash
maton slack message send --channel C0123456789 --text 'Hello from Maton!'
```

```bash
maton api '/slack/api/chat.postMessage'
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'channel': 'C0123456789', 'text': 'Hello from Maton!'}).encode()
req = urllib.request.Request('https://api.maton.ai/slack/api/chat.postMessage', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

## Authentication
**CLI:**

```bash
maton login                          # Opens browser for API key
maton login --interactive            # Skip browser, paste API key directly
maton whoami                         # Show current auth state
```

**Manual:**

1. Sign in or create an account at [maton.ai](https://maton.ai)
2. Go to [maton.ai/settings](https://maton.ai/settings)
3. Copy your API key
4. Set your API key as `MATON_API_KEY`:

```bash
export MATON_API_KEY="[REDACTED]"
```



---

### List Connections
**CLI:**

```bash
maton connection list slack --status ACTIVE
```

```bash
maton api -X GET /connections -f app=slack -f status=ACTIVE
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections?app=slack&status=ACTIVE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Create Connection
**CLI:**

```bash
maton connection create slack
```

```bash
maton api /connections -f app=slack
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'app': 'slack'}).encode()
req = urllib.request.Request('https://api.maton.ai/connections', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Get Connection
**CLI:**

```bash
maton connection view {connection_id}
```

```bash
maton api /connections/{connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

**Response:**

```json
{
  "connection": {
    "connection_id": "{connection_id}",
    "status": "ACTIVE",
    "creation_time": "2025-12-08T07:20:53.488460Z",
    "last_updated_time": "2026-01-31T20:03:32.593153Z",
    "url": "https://connect.maton.ai/?session_token=...",
    "app": "slack",
    "metadata": {}
  }
}
```

Open the returned `url` in a browser to complete OAuth authorization.



---

### Delete Connection
**CLI:**

```bash
maton connection delete {connection_id}
```

```bash
maton api -X DELETE /connections/{connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
req = urllib.request.Request('https://api.maton.ai/connections/{connection_id}', method='DELETE')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```



---

### Specifying Connection
If you have multiple Slack connections, specify which one to use:

**CLI:**

```bash
maton slack message send --channel C0123456789 --text 'Hello!' --connection {connection_id}
```

```bash
maton api /slack/api/chat.postMessage --connection {connection_id}
```

**Python:**

```bash
python <<'EOF'
import urllib.request, os, json
data = json.dumps({'channel': 'C0123456789', 'text': 'Hello!'}).encode()
req = urllib.request.Request('https://api.maton.ai/slack/api/chat.postMessage', data=data, method='POST')
req.add_header('Authorization', f'Bearer {os.environ["MATON_API_KEY"]}')
req.add_header('Maton-Connection', '{connection_id}')
req.add_header('Content-Type', 'application/json')
print(json.dumps(json.load(urllib.request.urlopen(req)), indent=2))
EOF
```

If you have multiple connections, always specify the connection to ensure requests go to the intended account.



---

### Users
#### List Users
```bash
GET /slack/api/users.list?limit=100
```

Example:

```bash
maton slack user list --limit 100
```

#### Get User Info
```bash
GET /slack/api/users.info?user=U0123456789
```

Example:

```bash
maton slack user view U0123456789
```

#### Get User Presence
```bash
GET /slack/api/users.getPresence?user=U0123456789
```

Example:

```bash
maton slack user presence U0123456789
```

#### Lookup User by Email
```bash
GET /slack/api/users.lookupByEmail?email=user@example.com
```

Example:

```bash
maton slack user lookup --email user@example.com
```



---

### Stars
#### List Stars
```bash
GET /slack/api/stars.list?limit=100
```

Example:

```bash
maton slack star list --limit 100
```

#### Add Star
```bash
POST /slack/api/stars.add
Content-Type: application/json

{
  "channel": "C0123456789",
  "timestamp": "1234567890.123456"
}
```

Example:

```bash
maton slack star add --channel C0123456789 --ts 1234567890.123456
```

#### Remove Star
```bash
POST /slack/api/stars.remove
Content-Type: application/json

{
  "channel": "C0123456789",
  "timestamp": "1234567890.123456"
}
```

Example:

```bash
maton slack star remove --channel C0123456789 --ts 1234567890.123456
```



---

### Pins
#### List Pins
```bash
GET /slack/api/pins.list?channel=C0123456789
```

Example:

```bash
maton slack pin list C0123456789
```

#### Add Pin
```bash
POST /slack/api/pins.add
Content-Type: application/json

{
  "channel": "C0123456789",
  "timestamp": "1234567890.123456"
}
```

Example:

```bash
maton slack pin add --channel C0123456789 --ts 1234567890.123456
```

#### Remove Pin
```bash
POST /slack/api/pins.remove
Content-Type: application/json

{
  "channel": "C0123456789",
  "timestamp": "1234567890.123456"
}
```

Example:

```bash
maton slack pin remove --channel C0123456789 --ts 1234567890.123456
```



---
