---
title: "Visual Studio Code 使用指南"
category: "开发"
platforms: ["windows", "mac", "linux"]
tags: ["编辑器", "开发工具", "IDE"]
created: "2023-01-01"
updated: "2023-05-18"
---

# Visual Studio Code

## 简介

Visual Studio Code（简称 VS Code）是微软开发的免费、开源的现代化轻量级代码编辑器，支持几乎所有主流的开发语言。它内置了 Git 版本控制功能，并拥有丰富的扩展生态系统，可以通过安装扩展来支持新的语言、主题、调试器等。

## 安装指南

### Windows

1. 访问 [VS Code 官网](https://code.visualstudio.com/)
2. 下载 Windows 安装包
3. 运行安装程序并按照提示完成安装

### Mac

```bash
# 使用 Homebrew 安装
brew install --cask visual-studio-code
```

### Linux

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install code

# Fedora
sudo dnf install code
```

## 快捷键

### 通用快捷键

| 操作 | Windows 快捷键 | Mac 快捷键 | 说明 |
|------|--------------|-----------|------|
| 打开命令面板 | `Ctrl + Shift + P` | `⌘ + Shift + P` | 显示所有命令 |
| 快速打开文件 | `Ctrl + P` | `⌘ + P` | 快速打开文件 |
| 打开终端 | `Ctrl + `` | `Ctrl + `` | 打开集成终端 |
| 切换侧边栏 | `Ctrl + B` | `⌘ + B` | 显示/隐藏侧边栏 |
| 格式化代码 | `Shift + Alt + F` | `⇧ + ⌥ + F` | 格式化当前文档 |

### 编辑快捷键

| 操作 | Windows 快捷键 | Mac 快捷键 | 说明 |
|------|--------------|-----------|------|
| 复制行 | `Shift + Alt + ↑/↓` | `⇧ + ⌥ + ↑/↓` | 向上/下复制当前行 |
| 移动行 | `Alt + ↑/↓` | `⌥ + ↑/↓` | 向上/下移动当前行 |
| 删除行 | `Ctrl + Shift + K` | `⌘ + ⇧ + K` | 删除当前行 |
| 跳转到定义 | `F12` | `F12` | 跳转到定义 |
| 查看引用 | `Shift + F12` | `⇧ + F12` | 查看所有引用 |

## 使用技巧

### 1. 多光标编辑

按住 `Alt` 键（Mac 上是 `⌥`）并点击要编辑的多个位置，可以同时在这些位置进行编辑。

### 2. 命令面板

使用 `Ctrl + Shift + P`（Mac 上是 `⌘ + Shift + P`）打开命令面板，可以执行任何 VS Code 支持的命令。

### 3. 集成终端

VS Code 内置了终端，支持 PowerShell、Command Prompt、Git Bash 等。使用 `Ctrl + `` 快速打开/关闭终端。

### 4. 代码片段

创建自定义代码片段：
1. 打开命令面板
2. 输入 "Configure User Snippets"
3. 选择语言
4. 添加自定义代码片段

## 推荐扩展

- **ESLint** - JavaScript 代码检查
- **Prettier** - 代码格式化
- **GitLens** - Git 增强功能
- **Live Server** - 本地开发服务器
- **REST Client** - 测试 HTTP 请求
- **Docker** - Docker 容器管理
- **Python** - Python 语言支持

## 常见问题

### 1. VS Code 启动慢

**解决方案**：
1. 禁用不需要的扩展
2. 在设置中关闭自动更新
3. 禁用文件监听

### 2. 终端无法使用

**解决方案**：
1. 检查终端路径设置
2. 更新 VS Code 到最新版本
3. 在设置中指定终端路径

## 相关资源

- [官方网站](https://code.visualstudio.com/)
- [GitHub 仓库](https://github.com/microsoft/vscode)
- [官方文档](https://code.visualstudio.com/docs)
- [VS Code 快捷键大全](https://code.visualstudio.com/shortcuts/keyboard-shortcuts-windows.pdf)

## 更新日志

- 2023-05-18: 创建文档
- 2023-01-15: 更新了快捷键和扩展推荐
