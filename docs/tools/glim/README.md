---
title: "Glim 文件查看指南"
category: "效率"
platforms: ["mac"]
tags: ["文件查看", "Markdown", "JSON", "CSV"]
created: "2026-10-19"
updated: "2026-10-19"
---

# Glim

## 简介

[Glim](https://github.com/NeoPanic/Glim) 是免费、MIT 开源的 macOS 文件查看器。它把 Markdown、PDF、图片、JSON、CSV 和源代码放在同一个文件树与标签工作区中，适合阅读项目文档、数据文件和相关素材。普通 UTF-8 文本支持基础编辑、自动保存和显式保存。

## 功能特点

- Markdown 阅读视图支持 Mermaid 图表和 LaTeX 公式。
- JSON 提供可展开的树；CSV 提供只读表格与源码切换。
- PDF、Office 和图片预览为只读；Office 效果取决于 macOS 提供的预览能力。
- 支持 Apple Silicon 和 Intel Mac。

## 安装指南

1. 打开[最新 Release](https://github.com/NeoPanic/Glim/releases/latest)。
2. Apple M 系列 Mac 选择文件名以 `-macos-arm64.dmg` 结尾的安装包；Intel Mac 选择 `-macos-x86_64.dmg`。芯片类型可在「苹果菜单 → 关于本机」查看。
3. 打开 DMG，将 Glim 拖入 Applications。
4. 当前下载包尚未经过 Apple 公证。如果首次启动被阻止，请按项目的[首次启动说明](https://github.com/NeoPanic/Glim#macos)在「系统设置 → 隐私与安全性」批准打开。

## 使用

1. 启动 Glim，打开需要阅读的文件或本地文件夹。
2. 通过文件侧栏和文档标签查看相关文件。例如，把项目 README、JSON 配置、CSV 数据和截图放在同一工作区。
3. 阅读 Markdown 的渲染内容；需要做小修改时切到源码。PDF、Office 和图片预览不能直接编辑。

## 常见问题

### 为什么不能编辑某些文件？

普通 UTF-8 文本提供基础编辑。文档/图片预览和不支持的文件保持只读；大型或超长行文本可能使用只读分页。完整边界见[格式支持指南](https://github.com/NeoPanic/Glim/blob/main/docs/file-format-support.md)。

### 能替代 IDE、Office 或电子表格编辑器吗？

Glim 主要用于查看内容与做基础文本修改。需要公式重算、复杂排版、表格编辑或开发环境功能时，应使用对应应用。

### 是否完全不联网？

文件读取以本地文件为基础；Markdown 的远程图片和更新检查可能使用网络。不要将其理解为网络隔离工具。

## 相关资源

- [官方仓库与界面截图](https://github.com/NeoPanic/Glim)
- [安装包与发布说明](https://github.com/NeoPanic/Glim/releases/latest)
- [支持格式与限制](https://github.com/NeoPanic/Glim/blob/main/docs/file-format-support.md)
- [MIT 许可证](https://github.com/NeoPanic/Glim/blob/main/LICENSE)

以上说明依据官方仓库、格式指南和发布资产整理；应用行为以项目当前文档为准。
