# yazi 与终端工作流集成调研底稿

> 调研基线: yazi v26.8.15 (Homebrew 2026-08-15, macOS aarch64, 本机 `yazi --version` 实测确认)
> 本机终端环境: Wezterm + zsh
> 调研日期: 2026-09-01
> 信息来源原则: 一手来源优先——官方文档、官方仓库 v26.8.15 tag 源码、官方文档仓库 versioned_docs/version-26.8.15；issue/PR 均标注状态。全文来源 URL 见文末清单。

---

## 1. Shell wrapper 核心模式：退出 yazi 时 shell 自动 cd

### 1.1 问题与原理

yazi 作为 TUI 程序在子进程中运行，退出后 shell 停留在启动 yazi 时的目录。官方方案是 `y` shell wrapper（quick-start 建议用 `y` 替代 `yazi` 启动）：

1. wrapper 先用 `mktemp` 创建临时文件；
2. 以 `--cwd-file="$tmp"` 参数启动 yazi；
3. yazi 退出时把最终所在目录写入该文件；
4. wrapper 读取文件内容，若与当前 `$PWD` 不同且是有效目录则 `cd`；
5. 删除临时文件。

配套默认键位（v26.8.15 `keymap-default.toml` 源码验证）：
- `q` = `quit`——写入 cwd-file，退出后 shell 跟随 yazi 内的目录；
- `Q` = `quit --no-cwd-file`——不写入，退出后 shell 原地不动。

### 1.2 zsh 完整可复制配置（官方原版）

```zsh
# ~/.zshrc — yazi 官方 zsh wrapper（v26.8.15 quick-start 原样）
function y() {
	local tmp cwd
	tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	command yazi "$@" --cwd-file="$tmp"
	IFS= read -r -d '' cwd < "$tmp"
	[ "$cwd" != "$PWD" ] && [ -d "$cwd" ] && builtin cd -- "$cwd" || builtin true
	command rm -f -- "$tmp"
}
```

要点：
- `command yazi` 绕过函数名递归（防 wrapper 自调用）；
- `IFS= read -r -d ''` 按 NUL 读整行，容忍含换行/空格的路径；
- `builtin cd --` 用 `--` 防止目录名被解析为 cd 选项；
- `|| builtin true` 保证目录无效时不因 `&&` 链短路返回非零。

### 1.3 YAZI_LEVEL 与防嵌套说明

- **YAZI_LEVEL 是 yazi 自动维护的嵌套深度计数器**。源码验证（v26.8.15 `yazi-dds/src/lib.rs`）：每次 yazi 启动时执行 `YAZI_LEVEL = 旧值 + 1`（无值则从 0 起）。该变量被 yazi 派生的子进程继承（如 yazi 内 `:` 执行 `shell --interactive`/`shell --block` 时派生的 shell）。
- **注意**：wrapper 所在的外层 shell 不会看到这个变量——它只存在于 yazi 进程及其子进程环境中。
- **防嵌套实践**（基于上述源码行为的社区做法，当前 v26.8.15 官方文档已不再收录此段，如实用）：

```zsh
# 防嵌套版：在 yazi 内按 : 打开的 shell 中再敲 y 时，跳过 cd 逻辑
# （那层 shell 退出后 cd 本就会被丢弃，读取 cwd-file 反而制造混乱）
function y() {
	if [[ -n "$YAZI_LEVEL" ]]; then
		command yazi "$@"   # 嵌套环境中：只打开，不做目录回写
		return
	fi
	local tmp cwd
	tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	command yazi "$@" --cwd-file="$tmp"
	IFS= read -r -d '' cwd < "$tmp"
	[ "$cwd" != "$PWD" ] && [ -d "$cwd" ] && builtin cd -- "$cwd" || builtin true
	command rm -f -- "$tmp"
}
```

- **关于 YAZI_LEVEL_ONE**：早期 yazi 文档/社区配置中出现过以 `YAZI_LEVEL_ONE` 记录最外层目录的 wrapper 方案。经全量检索，v26.8.15 源码中已不存在该变量（`grep -rn LEVEL_ONE` 零命中），属已废弃机制。当前官方唯一推荐 `--cwd-file` 方案，本身对多层嵌套天然安全：每层 wrapper 只消费自己创建的那份临时文件。

---

## 2. zoxide 集成：内置插件与数据库联动

### 2.1 联动模型（v26.8.15 源码验证）

yazi 内置 zoxide 插件（preset plugin，无需安装），默认键位 `Z`。它是 zoxide CLI 的前端，**与 shell 侧 zoxide 共享同一个数据库**（`$XDG_DATA_HOME/zoxide/zoxide.db`，默认 `~/.local/share/zoxide/zoxide.db`）：

- 读取：按 `Z` 时执行 `zoxide query -i --exclude <当前目录>` 进入交互模式（内部调用 fzf 展示候选）；
- 回写：`init.lua` 中开启 `update_db` 后，订阅 yazi 的 `cd` 事件，每次目录变更异步执行 `zoxide add <cwd>`。

### 2.2 配置（两步）

```zsh
# 第一步：shell 侧初始化 zoxide（建立并积累目录历史数据库）
eval "$(zoxide init zsh)"
```

```lua
-- 第二步：~/.config/yazi/init.lua — 让 yazi 里的跳转也反哺数据库
require("zoxide"):setup {
	update_db = true,  -- 每次 cd 时向 zoxide 数据库写入当前目录
}
```

`update_db` 说明来自官方 builtins 文档（v26.8.15）：Add the path to zoxide database whenever you change CWD。

### 2.3 行为细节与自定义入口

- yazi 会检测数据库是否为空，为空时弹通知提示先在 shell 里用 zoxide 积累历史；
- 候选面板默认带 `ls` 目录预览（fzf preview-window），并自动排除当前目录；
- fzf 界面参数注入顺序：`$FZF_DEFAULT_OPTS` → yazi 内置默认项 → `$YAZI_ZOXIDE_OPTS`（**用户自定义覆盖入口**，源码 `zoxide.lua` 的 `M.options()`）；
- 相关 issue：#2659（update_db 功能来源，closed）、#3940（插件与原版 zoxide 行为差异，closed）、#4214（为插件增加写库选项的 PR，open）、#3239（希望暴露内置 fzf 预设供替换，closed）。

---

## 3. fzf / fd / ripgrep 组合

### 3.1 内置键位总览（v26.8.15 默认键位源码验证）

| 按键 | 动作 | 依赖 |
|------|------|------|
| `z` | `plugin fzf`——fzf 浏览文件/目录树，跳转或选中 | fzf (>= 0.53.0) |
| `Z` | `plugin zoxide`——按历史目录跳转 | zoxide（内部用 fzf） |
| `s` | `search --via=fd`——按文件名递归搜索 | fd |
| `S` | `search --via=rg`——按文件内容搜索 | ripgrep |
| `Ctrl-s` | `escape --search`——取消进行中的搜索 | — |
| `f` | `filter --smart`——内置智能过滤 | — |
| `/` / `?` | `find --smart` 正/反向查找 | — |
| `g␣` | 交互式提示 cd / reveal | — |

### 3.2 内置 fzf 插件行为（源码验证）

- 以 `-m` 多选模式在当前 cwd 下运行 fzf；已选中文件会作为初始候选喂给 fzf；
- 结果路由：单个目录 → `cd`；单个文件 → `reveal`（定位显示）；多个 → 写入多选状态（toggle_all）；
- **文件列表来源由 fzf 自己决定**：未设 `FZF_DEFAULT_COMMAND` 时用 fzf 内置 walker（新版 fzf 自带目录遍历，含隐藏/忽略规则感知）；自定义示例：

```zsh
# ~/.zshrc — 用 fd 定制 fzf 列表来源（yazi 内按 z 同样生效，因继承 shell 环境）
export FZF_DEFAULT_COMMAND="fd --type f --hidden --exclude .git"
```

- 已知边界：插件暂不支持透传 `--walker` 参数（issue #2715, open）与 fzf 选项配置化（PR #2716, open），列表定制统一走 `FZF_DEFAULT_COMMAND`；
- macOS 已知问题 #4053（交互程序在 Mac 上异常，closed，v26.8.15 前后已修复，遇类似问题先升级 yazi）。

### 3.3 smart-filter：内置版与插件版

- **内置**：v26.8.15 默认键位 `f` 即 `filter --smart`（连续过滤、渐进缩小列表，官方内置无需安装）；
- **插件增强版** `smart-filter.yazi`（官方插件仓库）：在过滤基础上提供"自动进入唯一命中目录、提交时直接打开文件"等行为，安装 `ya pkg add yazi-rs/plugins:smart-filter` 后绑定到 `F`（与内置 `f` 共存不冲突）：

```toml
# ~/.config/yazi/keymap.toml
[[mgr.prepend_keymap]]
on   = "F"
run  = "plugin smart-filter"
desc = "Smart filter"
```

---

## 4. 图片预览：macOS 各终端适配（WezTerm 专项）

### 4.1 yazi 的协议适配器（v26.8.15 官方 image-preview 文档）

yazi 按 `$TERM`、`$TERM_PROGRAM`、`$XDG_SESSION_TYPE` 自动检测并按优先级选择协议，无需手动配置。适配器清单：

| 适配器 | 协议 | 备注 |
|--------|------|------|
| Kgp | Kitty unicode placeholders | 需终端为最新版 |
| KgpOld | Kitty 旧协议 | tmux 下不可用 |
| Iip | iTerm2 内联图像协议 | iTerm2/WezTerm 等 |
| Sixel | Sixel | tmux/Zellij 见 4.4 |
| X11 / Wayland | 窗口系统协议 | 需 Überzug++（Linux） |
| Chafa | ASCII/Unicode 字符画 | 最终兜底，需 Chafa >= 1.16.0 |

验证命令：`ya env`，输出中 `Adapter.matches` 即当前检测到的协议（也可 `yazi --debug` 查看完整环境报告）。

### 4.2 各终端适配表（macOS 视角）

| 终端 | 采用协议 | macOS 状态 | 配置要点 |
|------|----------|-----------|----------|
| **WezTerm** | **Iip（iTerm2 内联协议）** | 原生支持，零配置 | 无需任何配置；见 4.3 |
| iTerm2 | Iip | 原生支持，零配置 | — |
| kitty (>= 0.28) | Kgp | 原生支持 | 图标异常时改用官方 flavor（yazi-rs/flavors） |
| Ghostty | Kgp | 原生支持 | — |
| Alacritty | 无原生图像协议 | 不可用 | X11/Wayland 下才可能走 Überzug++（Linux 方案），macOS 下只能降级 Chafa |
| Warp | Iip | 支持（官方标注 macOS/Linux only） | — |
| VSCode 集成终端 | Iip | 支持 | 无 `ioctl` 像素尺寸上报，需配 `preview.max_width/max_height` |

### 4.3 WezTerm 专项说明（本机主力环境）

- **yazi 侧**：官方 image-preview 矩阵明确 WezTerm → Iip（iTerm2 内联协议），状态"内置"，即 v26.8.15 下 Wezterm + zsh 环境图片预览开箱即用，无需改 `yazi.toml`；
- **WezTerm 侧协议现状**（WezTerm 官方文档核验）：
  - iTerm2 兼容图像协议：完整支持（自带 `wezterm imgcat` 命令，20220319 版本起；多路复用会话下图像支持尚不完整）；
  - Kitty graphics protocol：features 页列有 "Kitty graphics support"，但官方文档未提供独立的协议子集/限制说明页（yazi 也未对 WezTerm 启用 Kgp 检测）；
  - Sixel：实验性（experimental，自 20200620 构建起），非默认推荐路径；
- **结论**：Wezterm 下无需也无法（无配置项）切换协议，yazi 自动走 iTerm2 内联协议即为当前最佳路径；`ya env` 确认 `Adapter.matches: Iip` 即配置正确。

### 4.4 tmux / Zellij 注意

- tmux 需在 `~/.tmux.conf` 开启透传：

```tmux
set -g allow-passthrough on
set -ga update-environment TERM
set -ga update-environment TERM_PROGRAM
```

改完重启：`tmux kill-server && tmux || tmux`。若想走 Sixel 需编译期 `--enable-sixel`；
- Zellij 仅支持 Kitty 旧协议与 Sixel，其 Sixel 实现有性能问题（卡顿/撕裂），图片预览需求强建议在复用器外运行 yazi。

---

## 5. 其他实用集成

### 5.1 bat 代码高亮预览

- **内置高亮已够用**：v26.8.15 内置 syntect 5.3.0 语法高亮（源码 Cargo.toml 验证），文本/代码预览默认即带高亮，bat 非必需；
- **想用 bat 的主题与参数**：通过官方插件 `piper.yazi`（把任意 shell 命令管道为预览器）：

```sh
ya pkg add yazi-rs/plugins:piper
```

```toml
# ~/.config/yazi/yazi.toml
[plugin]
prepend_previewers = [
	{ mime = "text/*", run = "piper bat --color=always --style=numbers,header" },
]
```

- 官方推荐安装的预览类依赖（installation 文档）：`ffmpeg`（视频缩略图）、`sevenzip`（归档预览/解压）、`jq`（JSON）、`poppler`（PDF）、`resvg`（SVG）、`imagemagick`（Font/HEIC/JPEG XL）。

### 5.2 chafa

官方兜底图像适配器：无像素级协议可用时（如 Alacritty）降级为 Chafa 字符画预览，要求 Chafa >= 1.16.0。WezTerm 用户不需要它，仅作极端环境兜底。

### 5.3 archivemount

官方 resources.md 收录社区插件 `AnirudhG07/archivemount.yazi`（依赖 [archivemount](https://github.com/cybernoid/archivemount)，把归档挂载为目录进出浏览）。注意：官方 installation 文档的归档方案是 7-Zip（预览与解压），archivemount 属社区补充，Linux 支持成熟、macOS 需通过源码/brew 安装 archivemount 本体。

### 5.4 垃圾桶（无需 trash-cli）

- yazi 内置 `trash` crate 5.2.6 实现系统级回收站（源码 Cargo.toml 验证），macOS 下 `d` 删除直接进 Finder 废纸篓，**无需安装 trash-cli**；
- 默认键位：`d` = `remove`（进回收站），`D` = `remove --permanently`（永久删除）。

### 5.5 官方插件生态速览（ya pkg 包管理器，v25.5.31 引入）

安装格式：`ya pkg add yazi-rs/plugins:<name>`。与本主题相关的官方插件：

| 插件 | 用途 |
|------|------|
| smart-filter | 增强过滤（连续过滤/自动进入唯一目录/提交即打开） |
| jump-to-char | Vim 式 `f<char>` 按首字符跳转 |
| piper | 任意 shell 命令作为预览器（bat 集成入口） |
| mount | 磁盘挂载/卸载/弹出的挂载管理器 |
| git | 文件列表 linemode 显示 git 状态 |
| mactag | macOS Finder 标签读写（仅 macOS） |
| term-cwd | 向终端发送 OSC cwd 通知（WezTerm 标签页标题跟随） |
| smart-enter | 打开文件与进入目录合一按键 |
| diff | 对比选中与悬停文件并生成补丁 |
| mime-ext | 用扩展名数据库替代 file(1) 提升 mime 判速 |

---

## 6. 同类工具对比表

| 维度 | yazi (Rust) | ranger (Python) | lf (Go) | nnn (C) |
|------|-------------|-----------------|---------|---------|
| 最新稳定版 | 26.8.15 (2026-08-15) | 1.9.4（发布节奏慢） | 持续滚动发布 | 滚动发布 |
| 性能 | Rust + async（tokio），异步 IO，预览/搜索不阻塞 UI | Python，同步 IO，大目录与预览易阻塞 UI | 原生二进制，**异步 IO**（官方特性列表明确） | 极致精简：~150KB 二进制，<3.5MB 常驻内存 |
| 图片预览 | 原生多协议：Kgp/KgpOld/Itp(iTerm2)/Sixel/Überzug++/Chafa，自动检测，**WezTerm 开箱即用** | w3m(默认)/iterm2/sixel/ueberzug/kitty（rc.conf `preview_images_method`），X11 依赖重，macOS 体验一般 | 预览脚本机制，社区方案支持 sixel/kitty/iterm/ueberzug/chafa，需自配 | 核心无内置，靠 preview-tui 等插件（sixel/kitty），配置成本高 |
| 插件生态 | 官方插件仓库（20+），Lua 插件 API，`ya pkg` 包管理器，插件文档/类型定义齐全 | Python 插件系统，历史存量丰富但维护放缓 | shell 命令即扩展（设计哲学：非特性靠外部工具） | shell 插件仓库 + patch 框架，量大但碎片 |
| 配置语言 | TOML（yazi.toml/keymap.toml/theme.toml）+ Lua（init.lua/插件） | Python（rc.conf + Python 插件） | shell（lfrc） | 无配置文件（0-config）+ 环境变量 + shell 插件 |
| zoxide/fzf/fd/rg | 内置插件级集成（z/Z/s/S 默认键位） | 需插件/自配 | 自配（lfrc 调外部命令） | 插件（如 zoxide.zsh 联动） |
| 回收站删除 | 内置（trash crate，macOS 进 Finder 废纸篓） | 依赖外部 trash 工具配置 | 非内置（shell 命令自配） | 非内置 |
| 平台支持 | Linux / macOS / Windows | Linux / macOS（Windows 实验性） | Linux / macOS / BSD / Windows | 极广：Linux/macOS/BSD/Termux/Haiku/WSL/Cygwin |
| 上手成本 | 中（默认键位即主力，进阶靠 Lua） | 中高（Python 配置栈） | 低中（shell 思维） | 低（0-config 但定制上限低） |

**关于 Files.app 的说明**：调研发现"Files"（files.community）是 **Windows 平台**的开源现代文件管理器（官方使命"to build the best file manager for Windows"），并非 macOS 工具；macOS 的对应物是系统 Finder（GUI）及 Commander One / Fileside 等双栏 GUI。它们与终端 TUI 工具不属于同一赛道，本表不纳入横向对比；若需 GUI 参照，macOS 下与 yazi 定位最近的是 Finder + Quick Look 的组合。

---

## 7. 选型结论

### 7.1 什么场景选 yazi（本机即此场景）

- **Rust 全家桶技术栈**（本机 Wezterm + zsh 已具备）：Wezterm（Rust）+ Helix（Rust）+ yazi（Rust）+ zoxide/fzf/fd/ripgrep/bat——同一技术哲学，yazi 是该栈中文件管理器的自然拼图，且是其中唯一原生异步 IO 的现代 TUI 文件管理器；
- **图片预览刚需 + macOS + WezTerm**：yazi 是唯一对 WezTerm 提供开箱即用 iTerm2 内联协议预览的主流 TUI（对比表第 3 行），零配置即得；
- **目录跳转密集型工作流**：内置 zoxide（DB 互通）+ fzf（z）+ fd/rg（s/S）四件套开箱即用，与 shell 侧工具共享数据，无需胶水配置；
- **需要插件化扩展又不愿写 Python/shell**：Lua 插件 + TOML 配置，官方插件仓库质量高、`ya pkg` 统一管理；
- **安全删除习惯**：原生系统回收站支持，`d`/`D` 语义分明。

### 7.2 什么场景考虑替代品

- **极端轻量/资源受限**（路由器、Termux、老机器）：选 nnn——150KB 二进制、0-config，资源占用无对手；
- **深度 shell 哲学偏好**：一切皆外部命令、配置即 shell 脚本——选 lf（异步 IO + server/client 架构，多实例远程管理是独有优势）；
- **存量 Python 配置资产 / w3m 老终端**：已有大量 ranger 自定义且迁移成本高时可留守；
- **Windows 首要平台**：yazi v26 支持 Windows 但终端条件苛刻（仅 WezTerm nightly/WT 1.22+/Bobcat），GUI 倾向则 Files（files.community）是 Windows 端选择；
- **Alacritty 用户**：macOS 下无像素级图片预览可用（Alacritty 不支持任何图像协议），yazi 只能降级 Chafa 字符画，若图片预览是硬需求建议先换 WezTerm/kitty/Ghostty。

---

## 8. 来源清单

### 官方文档（v26.8.15 版本化内容经 docs 仓库 versioned_docs 交叉核对）
- yazi quick-start（shell wrapper）: https://yazi-rs.github.io/docs/quick-start
- yazi FAQ: https://yazi-rs.github.io/docs/faq
- yazi image-preview: https://yazi-rs.github.io/docs/image-preview
- yazi installation（可选依赖与 Homebrew 命令）: https://yazi-rs.github.io/docs/installation
- yazi builtins 插件文档（zoxide update_db）: https://yazi-rs.github.io/docs/plugins/builtins

### 源码（v26.8.15 tag，本地浅克隆核验）
- 仓库: https://github.com/sxyazi/yazi/tree/v26.8.15
- 默认键位: `yazi-config/preset/keymap-default.toml`
- zoxide 插件: `yazi-plugin/preset/plugins/zoxide.lua`（query/add、YAZI_ZOXIDE_OPTS）
- fzf 插件: `yazi-plugin/preset/plugins/fzf.lua`（-m、cd/reveal/toggle_all 路由）
- YAZI_LEVEL: `yazi-dds/src/lib.rs`（启动时 +1）
- trash 依赖 / syntect 依赖: `yazi-fs/Cargo.toml`（trash 5.2.6）、`Cargo.toml`（syntect 5.3.0）

### issue / PR（sxyazi/yazi）
- #2659 zoxide 插件应随 cd 写库（closed）: https://github.com/sxyazi/yazi/issues/2659
- #3940 zoxide.lua 与原版行为差异（closed）: https://github.com/sxyazi/yazi/issues/3940
- #4214 zoxide 插件写库新选项 PR（open）: https://github.com/sxyazi/yazi/pull/4214
- #3239 暴露内置 zoxide fzf 预设（closed）: https://github.com/sxyazi/yazi/issues/3239
- #2715 fzf 插件透传 --walker（open）: https://github.com/sxyazi/yazi/issues/2715
- #2716 fzf 选项配置化 PR（open）: https://github.com/sxyazi/yazi/pull/2716
- #4053 macOS 交互程序异常（closed）: https://github.com/sxyazi/yazi/issues/4053

### 官方插件与生态
- yazi-rs/plugins 官方插件仓库: https://github.com/yazi-rs/plugins
- smart-filter: https://github.com/yazi-rs/plugins/tree/main/smart-filter.yazi
- piper: https://github.com/yazi-rs/plugins/tree/main/piper.yazi
- archivemount.yazi（社区）: https://github.com/AnirudhG07/archivemount.yazi
- 官方 flavors 主题: https://github.com/yazi-rs/flavors
- zoxide（数据库路径）: https://github.com/ajeetdsouza/zoxide

### WezTerm
- features 页（iTerm2 协议/Kitty graphics/Sixel experimental）: https://wezterm.org/features.html
- iTerm Image Protocol（imgcat）: https://wezterm.org/imgcat.html

### 同类工具
- ranger 1.9.4 README: https://github.com/ranger/ranger
- ranger rc.conf（preview_images_method）: https://github.com/ranger/ranger/blob/master/ranger/config/rc.conf
- lf README / doc: https://github.com/gokcehan/lf
- nnn README: https://github.com/jarun/nnn
- Files（files.community，Windows 平台确认）: https://files.community / https://github.com/files-community/files
