# 详细参考 - javascript-skills

> 本文件从SKILL.md拆分而来，包含详细代码示例和扩展章节。

## 代码示例 (javascript)

```javascript
// bad
function fetchData() {
  return getData()
    .then((data) => parseData(data))
    .then((parsed) => validate(parsed))
    .catch((err) => console.error(err));
}

// good
async function fetchData() {
  try {
    const data = await getData();
    const parsed = await parseData(data);
    return validate(parsed);
  } catch (err) {
    console.error(err);
    throw err;
  }
}

// concurrent operations
async function loadDashboard() {
  const [user, posts, notifications] = await Promise.all([
    fetchUser(),
    fetchPosts(),
    fetchNotifications(),
  ]);
  return { user, posts, notifications };
}
```

## 代码示例 (javascript)

```javascript
// bad
function Queue(contents = []) {
  this.queue = [...contents];
}
Queue.prototype.pop = function () {
  return this.queue.pop();
};

// good
class Queue {
  constructor(contents = []) {
    this.queue = [...contents];
  }

  pop() {
    return this.queue.pop();
  }
}

// inheritance
class PeekableQueue extends Queue {
  peek() {
    return this.queue[0];
  }
}
```

## 代码示例 (javascript)

```javascript
// bad
const item = new Object();

// good
const item = {};

// computed property names
const key = 'name';
const obj = { [key]: 'value' };

// method & property shorthand
const name = 'Alice';
const atom = {
  name,
  value: 1,
  addValue(val) {
    return atom.value + val;
  },
};

// shallow copy
const original = { a: 1, b: 2 };
const copy = { ...original, c: 3 };
```

## 代码示例 (javascript)

```javascript
// bad
function getFullName(user) {
  const firstName = user.firstName;
  const lastName = user.lastName;
  return `${firstName} ${lastName}`;
}

// good
function getFullName({ firstName, lastName }) {
  return `${firstName} ${lastName}`;
}

// array destructuring
const [first, , third] = [1, 2, 3];

// multiple return values — use object destructuring
function processInput(input) {
  return { left, right, top, bottom };
}
const { left, top } = processInput(input);
```

## 代码示例 (javascript)

```javascript
// bad
[1, 2, 3].map(function (x) {
  const y = x + 1;
  return x * y;
});

// good
[1, 2, 3].map((x) => {
  const y = x + 1;
  return x * y;
});

// implicit return
[1, 2, 3].map((x) => x * 2);

// multiline implicit return
[1, 2, 3].map((number) => (
  `A long string with the ${number}. It's so long that we don't want it to take up space on the .map line!`
));
```

## 代码示例 (javascript)

```javascript
// bad
const items = getItems(),
  goSportsTeam = true,
  dragonball = 'z';

// good
const items = getItems();
const goSportsTeam = true;
const dragonball = 'z';

// group const then let
const a = 1;
const b = 2;
let c = 3;
let d = 4;

// avoid unary
let count = 0;
count += 1;
```

## 代码示例 (javascript)

```javascript
// named function expression
const short = function longUniqueMoreDescriptiveLexicalFoo() {
  // ...
};

// default parameters last
function handleThings(name, opts = {}) {
  // ...
}

// rest parameters
function concatenateAll(...args) {
  return args.join('');
}

// spread to call
const values = [1, 2, 3];
console.log(Math.max(...values));
```

## 代码示例 (javascript)

```javascript
// bad
const items = new Array();

// good
const items = [];

// convert iterable
const nodes = Array.from(document.querySelectorAll('.item'));
const uniqueValues = [...new Set(arr)];

// array methods
[1, 2, 3].map((x) => x + 1);

[1, 2, 3].map((x) => {
  const y = x + 1;
  return x * y;
});
```

## 代码示例 (javascript)

```javascript
// bad
const utils = require('./utils');
module.exports = utils.fetchData;

// good
import { fetchData } from './utils';
export default fetchData;

// single place import
import { named1, named2 } from 'module';

// multiline
import {
  longNameA,
  longNameB,
  longNameC,
} from 'path/to/module';
```

## 代码示例 (javascript)

```javascript
// bad
if (test)
  return false;

// good
if (test) return false;

if (test) {
  return false;
}

// if/else
if (test) {
  thing1();
} else {
  thing2();
}
```

## 代码示例 (javascript)

```javascript
// bad
function foo(){
  const name='Alice';
}

// good
function foo() {
  const name = 'Alice';
}

// method chaining
$('#items')
  .find('.selected')
  .highlight()
  .end()
  .find('.open')
  .updateCount();
```

## 代码示例 (javascript)

```javascript
// bad
const OBJEcttsssss = {};
function c() {}
const u = new user();

// good
const thisIsMyObject = {};
function calculateTotal() {}
const user = new User();

// constants
export const API_BASE_URL = 'https://api.example.com';
export const MAX_RETRY_COUNT = 3;

// filename examples
// file: makeStyleGuide.js → export default function makeStyleGuide() {}
// file: User.js              → export default class User {}
```

## 代码示例 (javascript)

```javascript
// bad — leading commas
const hero = {
    firstName: 'Ada'
  , lastName: 'Lovelace'
};

// good — trailing commas
const hero = {
  firstName: 'Ada',
  lastName: 'Lovelace',
};

const heroes = [
  'Batman',
  'Superman',
];
```

## 代码示例 (javascript)

```javascript
// bad
throw 'Something went wrong';
throw { message: 'error' };

// good
throw new Error('Something went wrong');

class ValidationError extends Error {
  constructor(message, field) {
    super(message);
    this.name = 'ValidationError';
    this.field = field;
  }
}

throw new ValidationError('Invalid email', 'email');
```

## 代码示例 (javascript)

```javascript
/**
 * Deep clones a plain object or array using structured cloning.
 * Falls back to JSON serialization for environments without structuredClone.
 *
 * @param {Object|Array} source - The value to clone.
 * @returns {Object|Array} A deep copy of the source.
 */
function deepClone(source) {
  if (typeof structuredClone === 'function') {
    return structuredClone(source);
  }

  return JSON.parse(JSON.stringify(source));
}

export default deepClone;
```

## 代码示例 (javascript)

```javascript
// good single line
// This is a comment
const active = true;

/**
 * Multiline comment explaining the function.
 * @param {string} tag - The tag name.
 * @returns {Element} The created element.
 */
function make(tag) {
  return document.createElement(tag);
}

// TODO: implement caching
// FIXME: should not use global state
```

