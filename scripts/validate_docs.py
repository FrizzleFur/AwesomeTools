#!/usr/bin/env python3
"""
验证文档结构和格式的工具脚本
"""
import os
import re
from pathlib import Path

def check_markdown_file(file_path):
    """检查Markdown文件的基本格式"""
    required_sections = [
        r'^##\s+简介',
        r'^##\s+安装指南',
        r'^##\s+使用',
        r'^##\s+常见问题'
    ]
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        missing_sections = []
        for section in required_sections:
            if not re.search(section, content, re.MULTILINE):
                missing_sections.append(section)
                
        if missing_sections:
            print(f"⚠️  文件 {file_path} 缺少以下必要部分:")
            for section in missing_sections:
                print(f"  - {section}")
            return False
            
        return True
    except Exception as e:
        print(f"❌ 检查文件 {file_path} 时出错: {e}")
        return False

def check_directory_structure():
    """检查目录结构"""
    required_dirs = [
        'docs',
        'docs/categories',
        'docs/templates',
        'docs/tools'
    ]
    
    missing_dirs = []
    for dir_path in required_dirs:
        if not os.path.exists(dir_path):
            missing_dirs.append(dir_path)
    
    if missing_dirs:
        print("❌ 缺少以下目录:")
        for dir_path in missing_dirs:
            print(f"  - {dir_path}")
        return False
    return True

def main():
    print("🔍 开始验证文档结构...")
    
    # 检查目录结构
    if not check_directory_structure():
        print("❌ 目录结构检查未通过")
        return 1
    
    print("✅ 目录结构检查通过")
    
    # 检查工具文档
    print("\n🔍 检查工具文档...")
    tool_docs_dir = Path('docs/tools')
    has_errors = False
    
    for tool_dir in tool_docs_dir.iterdir():
        if not tool_dir.is_dir():
            continue
            
        readme_path = tool_dir / 'README.md'
        if not readme_path.exists():
            print(f"❌ 工具 {tool_dir.name} 缺少 README.md 文件")
            has_errors = True
            continue
            
        if not check_markdown_file(str(readme_path)):
            has_errors = True
    
    if not has_errors:
        print("✅ 所有工具文档检查通过")
    
    return 1 if has_errors else 0

if __name__ == "__main__":
    exit(main())
