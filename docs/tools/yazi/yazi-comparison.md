# Yazi 同类工具对比与选型

> 基准时间：2026-09-01 | 版本数据来自各项目官方仓库

## 对比总表

| 维度 | yazi (Rust) | ranger (Python) | lf (Go) | nnn (C) |
|------|-------------|-----------------|---------|---------|
| 性能 | Rust + tokio 全异步 IO，预览/搜索不阻塞 UI | Python 同步 IO，大目录与预览易卡 UI | 原生二进制，异步 IO | 极致精简：~150KB 二进制，<3.5MB 常驻内存 |
| 图片预览 | 原生多协议自动探测（Kgp/Iip/Sixel/Chafa），**WezTerm/iTerm2/kitty 开箱即用** | w3m/iterm2/ueberzug/kitty 需 rc.conf 配置，macOS 体验一般 | 预览脚本机制，需自配社区方案 | 核心无内置，靠 preview-tui 插件 |
| 插件生态 | 官方 19 插件 + Lua API，`ya pkg` 包管理器 | Python 插件，存量丰富但维护放缓 | shell 命令即扩展 | shell 插件 + patch 框架，量大碎片 |
| 配置语言 | TOML 三大件 + Lua | Python（rc.conf） | shell（lfrc） | 0-config + 环境变量 |
| zoxide/fzf/fd/rg | **内置插件级集成**（Z/z/s/S 默认键位） | 需插件/自配 | lfrc 调外部命令 | 插件联动 |
| 回收站 | **内置**（macOS 进 Finder 废纸篓） | 依赖外部 trash 工具 | 非内置 | 非内置 |
| 平台 | Linux / macOS / Windows | Linux / macOS（Windows 实验性） | Linux / macOS / BSD / Windows | 极广（含 Termux/Cygwin） |
| 上手成本 | 中（默认键位即主力，进阶靠 Lua） | 中高（Python 配置栈） | 低中（shell 思维） | 低（但定制上限低） |

> 澄清：常被一起提到的 "Files"（files.community）是 **Windows 平台**的 GUI 文件管理器，与终端 TUI 不同赛道。macOS 下与 yazi 定位最近的 GUI 参照是 Finder + Quick Look。

## 选型结论

### 什么场景选 yazi

1. **Rust 全家桶技术栈**：Wezterm + Helix + yazi + zoxide/fzf/fd/ripgrep——同一技术哲学，yazi 是文件管理器的自然拼图，且是其中唯一原生异步 IO 的现代 TUI 文件管理器
2. **图片预览刚需 + macOS**：唯一对 WezTerm 提供开箱即用 iTerm2 内联协议预览的主流 TUI，零配置即得
3. **目录跳转密集型工作流**：zoxide（数据库互通）+ fzf + fd/rg 四件套内置，与 shell 侧工具共享数据
4. **想要插件化又不想写 Python/shell**：Lua 插件 + TOML 配置，官方插件仓库质量高
5. **安全删除习惯**：原生系统回收站，`d`/`D` 语义分明

### 什么场景考虑替代品

| 场景 | 推荐 | 理由 |
|---|---|---|
| 极端轻量/资源受限（路由器、Termux、老机器） | nnn | 150KB 二进制、0-config，资源占用无对手 |
| 深度 shell 哲学：一切皆外部命令 | lf | 配置即 shell 脚本，server/client 架构多实例远程管理是独有优势 |
| 已有大量 ranger 自定义资产 | ranger 留守 | 迁移成本高于收益（但 ranger 维护放缓是长期风险） |
| Windows 首要平台 | yazi（条件苛刻）或 Files | yazi 需 WT 1.22+/WezTerm nightly；GUI 倾向选 Files |
| 终端是 Alacritty 且图片预览是硬需求 | 先换 WezTerm/kitty/Ghostty | Alacritty 不支持任何图像协议，yazi 也救不了 |

### 一句话结论

**2026 年新装终端环境，yazi 是默认答案**——异步架构解决了 ranger 时代的卡顿痛点，内置集成消灭了 lf/nnn 式的胶水配置成本；它的短板（插件版本耦合、Windows 终端要求高）都是新项目快速迭代期的正常代价。只在"极致轻量"或"存量 Python 资产"两个场景下，nnn/ranger 仍是更优解。

## 参考

- [yazi 官方仓库](https://github.com/sxyazi/yazi) · [ranger](https://github.com/ranger/ranger) · [lf](https://github.com/gokcehan/lf) · [nnn](https://github.com/jarun/nnn)
- [返回 Yazi 使用指南](README.md)
