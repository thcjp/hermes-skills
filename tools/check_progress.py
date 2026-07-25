#!/usr/bin/env python3
import json
with open('../data/reports/batch_reupload_progress.json', encoding='utf-8') as f:
    data = json.load(f)
success = data.get('success', [])
failed = data.get('failed', [])
print(f'Success: {len(success)}')
print(f'Failed: {len(failed)}')
print(f'Success slugs: {success}')
for f_item in failed:
    print(f'Failed: {f_item}')
