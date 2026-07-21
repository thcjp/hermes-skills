# 详细参考 - javascript-sdk

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (typescript)

```typescript
import { tool, string, number, appTool } from '@inferencesh/sdk';

// Define tools
const calculator = tool('calculate')
  .describe('Perform a calculation')
  .param('expression', string('Math expression'))
  .build();

const imageGen = appTool('generate_image', 'infsh/flux-schnell@latest')
  .describe('Generate an image')
  .param('prompt', string('Image description'))
  .build();

// Create agent
const agent = client.agent({
  core_app: { ref: 'infsh/claude-sonnet-4@latest' },
  system_prompt: 'You are a helpful assistant.',
  tools: [calculator, imageGen],
  temperature: 0.7,
  max_tokens: 4096
});

const response = await agent.sendMessage('What is 25 * 4?');
```

## 代码示例 (typescript)

```typescript
import { internalTools } from '@inferencesh/sdk';

const config = internalTools()
  .plan()
  .memory()
  .webSearch(true)
  .codeExecution(true)
  .imageGeneration({
    enabled: true,
    appRef: 'infsh/flux@latest'
  })
  .build();

const agent = client.agent({
  core_app: { ref: 'infsh/claude-sonnet-4@latest' },
  internal_tools: config
});
```

## 代码示例 (typescript)

```typescript
import {
  string, number, integer, boolean,
  enumOf, array, obj, optional
} from '@inferencesh/sdk';

const name = string('User\'s name');
const age = integer('Age in years');
const score = number('Score 0-1');
const active = boolean('Is active');
const priority = enumOf(['low', 'medium', 'high'], 'Priority');
const tags = array(string('Tag'), 'List of tags');
const address = obj({
  street: string('Street'),
  city: string('City'),
  zip: optional(string('ZIP'))
}, 'Address');
```

## 代码示例 (typescript)

```typescript
// From file path (Node.js)
import { readFileSync } from 'fs';
const response = await agent.sendMessage('What\'s in this image?', {
  files: [readFileSync('image.png')]
});

// From base64
const response = await agent.sendMessage('Analyze this', {
  files: ['data:image/png;base64,iVBORw0KGgo...']
});

// From browser File object
const input = document.querySelector('input[type="file"]');
const response = await agent.sendMessage('Describe this', {
  files: [input.files[0]]
});
```

## 代码示例 (typescript)

```typescript
// Start new session
const result = await client.run({
  app: 'my-app',
  input: { action: 'init' },
  session: 'new',
  session_timeout: 300  // 5 minutes
});
const sessionId = result.session_id;

// Continue in same session
const result2 = await client.run({
  app: 'my-app',
  input: { action: 'process' },
  session: sessionId
});
```

## 代码示例 (typescript)

```typescript
const agent = client.agent({
  core_app: { ref: 'infsh/claude-sonnet-4@latest' },
  skills: [
    {
      name: 'code-review',
      description: 'Code review guidelines',
      content: '# Code Review\n\n1. Check security\n2. Check performance...'
    },
    {
      name: 'api-docs',
      description: 'API documentation',
      url: 'https://example.com/skills/api-docs.md'
    }
  ]
});
```

## 代码示例 (typescript)

```typescript
// Basic upload
const file = await client.uploadFile('/path/to/image.png');

// With options
const file = await client.uploadFile('/path/to/image.png', {
  filename: 'custom_name.png',
  contentType: 'image/png',
  public: true
});

const result = await client.run({
  app: 'image-processor',
  input: { image: file.uri }
});
```

## 代码示例 (typescript)

```typescript
const agent = client.agent('my-team/support-agent@latest');

// Send message
const response = await agent.sendMessage('Hello!');
console.log(response.text);

// Multi-turn conversation
const response2 = await agent.sendMessage('Tell me more');

// Reset conversation
agent.reset();

// Get chat history
const chat = await agent.getChat();
```

## 代码示例 (typescript)

```typescript
import type {
  TaskDTO,
  ChatDTO,
  ChatMessageDTO,
  AgentTool,
  TaskStatusCompleted,
  TaskStatusFailed
} from '@inferencesh/sdk';

if (result.status === TaskStatusCompleted) {
  console.log('Done!');
} else if (result.status === TaskStatusFailed) {
  console.log('Failed:', result.error);
}
```

## 代码示例 (typescript)

```typescript
import { RequirementsNotMetException, InferenceError } from '@inferencesh/sdk';

try {
  const result = await client.run({ app: 'my-app', input: {...} });
} catch (e) {
  if (e instanceof RequirementsNotMetException) {
    console.log('Missing requirements:');
    for (const err of e.errors) {
      console.log(`  - ${err.type}: ${err.key}`);
    }
  } else if (e instanceof InferenceError) {
    console.log('API error:', e.message);
  }
}
```

