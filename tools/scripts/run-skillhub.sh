#!/bin/bash
# SkillHub CLI 运行器 (通过文件中转输出,绕过 PowerShell/Bash stdout 兼容问题)
# 输出写入固定文件,由 PowerShell 端读取

export PATH="$HOME/.local/bin:$PATH"
OUTPUT_FILE="/d/skills/.skillhub-credentials/last-output.txt"

# Run the skillhub command and capture output to file
skillhub "$@" > "$OUTPUT_FILE" 2>&1
EXIT_CODE=$?

# Also append exit code to the file
echo "" >> "$OUTPUT_FILE"
echo "[EXIT_CODE:$EXIT_CODE]" >> "$OUTPUT_FILE"

exit $EXIT_CODE
