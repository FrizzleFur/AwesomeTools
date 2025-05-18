#!/bin/bash

# 检查文档结构
python3 scripts/validate_docs.py

# 检查 Markdown 格式
if ! command -v markdownlint &> /dev/null; then
    echo "⚠️  markdownlint 未安装，跳过 Markdown 格式检查"
    echo "   安装命令: npm install -g markdownlint-cli"
else
    echo "\n🔍 检查 Markdown 格式..."
    markdownlint "**/*.md" --ignore node_modules
fi

echo "\n✅ 检查完成"
