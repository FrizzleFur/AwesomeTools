---
title: "Yazi 使用指南"
category: "开发"
platforms: ["windows", "mac", "linux"]
tags: ["文件管理器", "命令行", "终端", "Rust"]
created: "2026-09-01"
updated: "2026-09-01"
---

# Yazi 终端文件管理器

> 🦦 基于 Rust 的极速终端文件管理器：全异步 I/O、内置图片预览、zoxide/fzf/fd/rg 原生集成，"Rust 全家桶"里文件管理的最后一块拼图。

## 基本信息

| 项目 | 详情 |
|------|------|
| **官方网站** | [yazi-rs.github.io](https://yazi-rs.github.io/) |
| **开源仓库** | [sxyazi/yazi](https://github.com/sxyazi/yazi) |
| **开源协议** | MIT |
| **最新版本** | v26.8.15（2026-08-15，本文调研基准版本） |
| **适用平台** | macOS / Linux / Windows |
| **价格** | 免费开源 |
| **分类** | [开发工具 / 终端](/docs/categories/development.md) |

## 简介

Yazi（鸭子，中文"鸭"的拼音）是一款用 Rust 编写的终端文件管理器，核心卖点是**完全异步**：所有 I/O 操作异步执行，CPU 任务多线程分布，大目录浏览、文件搜索、图片预览均不阻塞界面。

与传统的 ranger 相比，它把现代终端工具链（zoxide、fzf、fd、ripgrep）做成了**内置插件级集成**——`Z` 键跳目录、`z` 键模糊找文件、`s`/`S` 键按名/按内容搜索，全部开箱即用，与 shell 侧工具共享同一套数据库，零胶水配置。

### 核心特性

- 🚀 **全异步架构**：tokio 驱动，预览/搜索/复制互不阻塞，任务面板（`w`）实时看进度
- 🖼️ **多协议图片预览**：Kitty / iTerm2 内联 / Sixel / Chafa 自动探测，WezTerm、iTerm2 零配置开箱即用
- 🧰 **工具链原生集成**：zoxide（目录跳转）、fzf（模糊搜索）、fd/ripgrep（递归搜索）内置键位直达
- 🏷️ **多标签页**：跨标签共享 yank 状态，双目录对拷丝滑
- 🔄 **批量操作**：可视模式多选、`$EDITOR` 批量重命名、批量新建
- 🗑️ **系统回收站**：`d` 删除进系统废纸篓（macOS 进 Finder 废纸篓），`D` 才是永久删除
- 🎨 **主题生态**：官方 flavor 机制（Catppuccin/Dracula/Gruvbox 等 30+），`ya pkg` 一键安装
- 🧩 **Lua 插件系统**：官方 19 个插件 + 活跃社区，统一包管理

> 📖 本指南基于 v26.8.15 实测撰写（2026-09-01）。Yazi 迭代较快，个别键位以程序内 `~` 帮助菜单为准。旧教程常见写法（`[manager]`、`ya pack`、`yazi --debug`）均已弃用，详见[常见问题](#常见问题)。

## 安装指南

### macOS（Homebrew，推荐）

```bash
brew install yazi
brew install ffmpeg sevenzip jq poppler fd ripgrep fzf zoxide imagemagick font-symbols-only-nerd-font
```

第一条装主程序，第二条装**可选预览依赖**（视频缩略图 / 归档 / JSON / PDF / SVG / 字体图标），按需取舍。

### Linux

```bash
# Arch Linux
pacman -S yazi
# 或 AUR 开发版
yay -S yazi-git
```

其余发行版见[官方安装文档](https://yazi-rs.github.io/docs/installation)（提供 cargo、snap、flatpak、Nix 等方式）。

### Windows

```powershell
winget install sxyazi.yazi
# 或
scoop install yazi
```

> Windows 终端要求较苛刻（Windows Terminal 1.22+ / WezTerm nightly 等），图片预览体验不如 macOS/Linux。

### 从源码编译

```bash
# 需 Rust 1.82+（cargo install 或 clone 后 make build）
cargo install --locked yazi-fm yazi-cli
```

### 验证安装

```bash
yazi --version   # 确认版本
ya env           # 环境诊断（v26 起 yazi --debug 已废弃，改用 ya env）
```

### 建议配置 shell wrapper

退出 yazi 后让 shell 自动 `cd` 到 yazi 当前目录——官方推荐用 `y` 函数替代裸 `yazi` 启动，配置方法见[工作流集成](yazi-integration.md#shell-wrapper退出时自动-cd)。

## 使用

### 快速上手（30 秒入门）

```bash
y ~        # 用 wrapper 启动（推荐），或直接 yazi
```

记住 6 个键就能干活：

| 按键 | 动作 |
|------|------|
| `j` / `k` | 上下移动（Vim 风格） |
| `l` | 进入目录（装 smart-enter 插件后文件上也表示打开，见下） |
| `h` | 返回上级 |
| `Space` | 选中文件 |
| `q` | 退出（wrapper 下会 cd 到 yazi 所在目录） |
| `~` | 随时打开帮助菜单（列出当前界面全部键位） |

> ⚠️ **新手第一坑**：默认 `l` 只绑"进入目录"，光标在**文件**上按 `l` 无反应；打开文件要用 `o` 或 `Enter`。官方 `smart-enter` 插件可把 `l` 增强为"目录则进入、文件则打开"，强烈推荐，见[配置指南](yazi-configuration.md#案例-2smart-enter--prepend_keymap)。

### 完整快捷键体系

- **[快捷键完整参考](yazi-keybindings.md)**：主界面 9 大分组 + 7 个弹层上下文共 254 条默认键位，附实战场景与自定义方法

### 配置与定制

- **[配置与定制指南](yazi-configuration.md)**：`yazi.toml` / `theme.toml` / `keymap.toml` 三大配置详解、插件生态、flavor 主题、真实生产配置案例

### 工作流集成

- **[工作流集成指南](yazi-integration.md)**：shell wrapper、zoxide 数据库互通、fzf/fd/rg 组合、图片预览终端适配（WezTerm 专项）

### 选型对比

- **[同类工具对比与选型](yazi-comparison.md)**：yazi vs ranger vs lf vs nnn 全维度对比，什么场景选什么

### 日常高频工作流示例

```text
找文件      z（fzf 模糊跳转）/ s（fd 按名搜）/ S（rg 按内容搜）
批量重命名   v 进入可视模式选择 → r → 在 $EDITOR 里逐行改名 → 保存退出
双目录对拷   t⇒t 开新标签页 → 标签 1 按 y 复制 → ] 切标签 → p 粘贴
看大文件    J / K 滚动预览内容（列表光标不动）
查文件信息   Tab 弹出文件元数据面板（大小/权限/mime）
清磁盘      ,⇒S 按大小降序 → 定位大文件 → d 进回收站
```

## 常见问题

### Q1：按 `l` 打不开文件？
默认 `l` 仅绑定"进入目录"（`enter`），光标在文件上时无反应。打开文件用 `o`（按规则打开）或 `Enter`，或安装官方 `smart-enter` 插件统一语义（[配置指南](yazi-configuration.md#案例-2smart-enter--prepend_keymap)）。

### Q2：老教程里的 `[manager]`、`ya pack`、`yazi --debug` 都报错/失效？
均为旧版写法，v25.5.28 起已弃用。现行写法：

| 旧写法 | 现写法 |
|--------|--------|
| `[manager]` | `[mgr]` |
| `ya pack -a <pkg>` | `ya pkg add <pkg>` |
| `yazi --debug` | `ya env` |
| `yazi --clear-cache` | `ya cache clear` |
| `shell "cmd %s"` | `shell -- cmd %s`（`--` 分隔） |
| `micro_workers`/`macro_workers` | `file_workers` 等细粒度 worker |

完整迁移清单见[配置指南版本时效章节](yazi-configuration.md#版本时效v25--v26-破坏性变更)。

### Q3：图片预览不显示？
三步排查：① `ya env` 确认 `Adapter.matches` 检测到协议；② 确认终端支持（WezTerm/iTerm2/kitty/Ghostty 均开箱即用，**Alacritty 不支持任何图像协议**）；③ tmux 内需开启透传（`allow-passthrough on`）。详见[集成指南图片预览章节](yazi-integration.md#图片预览终端适配)。

### Q4：删除的文件去哪了？能恢复吗？
`d` 是**移入系统回收站**（macOS 进 Finder 废纸篓，无需安装 trash-cli），`g⇒t` 可进回收站管理；`D` 才是永久删除（有确认框）。

### Q5：换了新电脑，插件和主题怎么一键恢复？
把 `~/.config/yazi` 整个目录纳入 dotfiles。`package.toml` 锁定了插件/主题的 commit，新机器执行 `ya pkg install` 即可一键装齐（详见[配置指南](yazi-configuration.md#插件生态最佳实践)）。

### Q6：`ya pkg upgrade` 之后插件报错？
官方警告：**插件只保证与最新版 yazi 兼容**。yazi 与 `ya` 版本必须完全一致，升级 yazi 后记得同步 `ya pkg upgrade`。若手改过插件源码，用 `ya pkg --discard` 还原。

## 相关链接

- [官方文档](https://yazi-rs.github.io/docs/quick-start)
- [官方插件仓库](https://github.com/yazi-rs/plugins)
- [官方主题仓库](https://github.com/yazi-rs/flavors)
- [AwesomeTools 清单条目](../../../AwesomeTools清单.md)
