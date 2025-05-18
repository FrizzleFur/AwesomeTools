#!/usr/bin/env python3
"""
Awesome Tools 文档迁移工具

将旧版文档迁移到新的文档结构中
"""
import os
import shutil
from datetime import datetime

def create_tool_doc(tool_name, category, source_file, target_dir):
    """创建工具文档"""
    os.makedirs(target_dir, exist_ok=True)
    
    # 读取源文件内容
    with open(source_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 创建元数据
    metadata = f"""---
title: "{tool_name} 使用指南"
category: "{category}"""
    
    # 自动检测平台
    platforms = []
    if 'windows' in content.lower():
        platforms.append('windows')
    if 'mac' in content.lower() or 'osx' in content.lower():
        platforms.append('mac')
    if 'linux' in content.lower() or 'ubuntu' in content.lower() or 'debian' in content.lower():
        platforms.append('linux')
    
    if not platforms:
        platforms = ['windows', 'mac', 'linux']
    
    metadata += f"\nplatforms: {platforms}"
    
    # 添加标签
    tags = [tag.lower() for tag in category.split()]
    if tool_name.lower() not in tags:
        tags.append(tool_name.lower())
    
    metadata += f"\ntags: {tags}"
    
    # 添加日期
    today = datetime.now().strftime('%Y-%m-%d')
    metadata += f"\ncreated: \"{today}\"\nupdated: \"{today}\"\n---\n\n"
    
    # 写入新文件
    with open(os.path.join(target_dir, 'README.md'), 'w', encoding='utf-8') as f:
        f.write(metadata + content)
    
    print(f"已创建: {os.path.join(target_dir, 'README.md')}")

def main():
    # 示例：迁移 VSCode 文档
    # create_tool_doc(
    #     "Visual Studio Code",
    #     "开发",
    #     "../Awesome效率神器/开发工具/工具-VSCode.md",
    #     "./tools/vscode"
    # )
    
    # 添加更多迁移任务...
    pass

if __name__ == "__main__":
    main()
