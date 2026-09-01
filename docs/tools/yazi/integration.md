# Yazi 工作流集成指南

> 基准版本：yazi v26.8.15（2026-08-15）| 环境示例：macOS + WezTerm + zsh

## Shell wrapper：退出时自动 cd

### 问题

yazi 作为 TUI 子进程运行，直接 `yazi` 启动，退出后 shell 仍停留在启动时的目录。官方方案是 `y` wrapper（推荐日常都用 `y` 替代 `yazi`）：

1. wrapper 创建临时文件 → 2. 以 `--cwd-file` 启动 yazi → 3. yazi 退出时把最终目录写入文件 → 4. wrapper 读取并 `cd` → 5. 清理临时文件

### zsh 配置（官方原版）

```zsh
# ~/.zshrc — yazi 官方 wrapper
function y() {
	local tmp cwd
	tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	command yazi "$@" --cwd-file="$tmp"
	IFS= read -r -d '' cwd < "$tmp"
	[ "$cwd" != "$PWD" ] && [ -d "$cwd" ] && builtin cd -- "$cwd" || builtin true
	command rm -f -- "$tmp"
}
```

要点：`command yazi` 防函数自递归；`IFS= read -r -d ''` 容忍含空格/换行的路径；`builtin cd --` 防目录名被解析为选项。

### 防嵌套增强版

在 yazi 内按 `:` 打开的 shell 里再敲 `y` 属于嵌套场景（那层 shell 退出后 cd 本就被丢弃）：

```zsh
function y() {
	if [[ -n "$YAZI_LEVEL" ]]; then
		command yazi "$@"   # 嵌套环境：只打开，不做目录回写
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

`YAZI_LEVEL` 是 yazi 自动维护的嵌套深度计数器（源码验证：每次 yazi 启动 +1，被子 shell 继承）。旧配置里的 `YAZI_LEVEL_ONE` 变量在 v26 源码中已不存在，属废弃机制。

### 配套键位

| 键 | 行为 |
|---|---|
| `q` | `quit`——写回 cwd-file，退出后 shell 跟随 |
| `Q` | `quit --no-cwd-file`——不写回，shell 原地不动 |

## zoxide 集成：与 shell 共享目录数据库

yazi 内置 zoxide 插件（默认键 `Z`），是 zoxide CLI 的前端，**与 shell 侧共享同一个数据库**——在 shell 里 `cd` 过的目录，yazi 里按 `Z` 就能跳到；反过来 yazi 里的跳转也能反哺数据库。

两步配置：

```zsh
# 第一步：shell 侧初始化 zoxide
eval "$(zoxide init zsh)"
```

```lua
-- 第二步：~/.config/yazi/init.lua — 让 yazi 的跳转也写入数据库
require("zoxide"):setup {
	update_db = true,  -- 每次 cd 时向 zoxide 数据库写入当前目录
}
```

细节：候选面板带 `ls` 目录预览、自动排除当前目录；`YAZI_ZOXIDE_OPTS` 环境变量可覆盖 fzf 界面参数。

## fzf / fd / ripgrep 组合

全部为**内置键位**，零胶水配置：

| 按键 | 动作 | 依赖 |
|---|---|---|
| `z` | fzf 浏览文件树，跳转或多选 | fzf ≥ 0.53 |
| `Z` | zoxide 按历史跳目录 | zoxide |
| `s` | 按文件名递归搜索 | fd |
| `S` | 按内容搜索 | ripgrep |
| `f` | 内置智能过滤 | — |

结果路由：单个目录 → `cd`；单个文件 → `reveal`（定位显示）；多个 → 进入多选状态。

**定制 fzf 列表来源**（yazi 内按 `z` 同样生效，因继承 shell 环境）：

```zsh
export FZF_DEFAULT_COMMAND="fd --type f --hidden --exclude .git"
```

**smart-filter 增强**（可选）：官方插件的过滤支持"唯一命中目录自动进入、提交即打开"，绑定到 `F` 与内置 `f` 共存：

```bash
ya pkg add yazi-rs/plugins:smart-filter
```

```toml
# keymap.toml
[[mgr.prepend_keymap]]
on   = "F"
run  = "plugin smart-filter"
desc = "Smart filter"
```

## 图片预览：终端适配

yazi 按 `$TERM` / `$TERM_PROGRAM` 自动探测协议（优先级：Kgp → Iip → KgpOld → Sixel → Überzug++ → Chafa），**无需手动配置**。

### macOS 各终端适配表

| 终端 | 协议 | 状态 |
|---|---|---|
| **WezTerm** | **Iip（iTerm2 内联协议）** | ✅ 原生支持，零配置 |
| iTerm2 | Iip | ✅ 原生支持，零配置 |
| kitty (≥ 0.28) | Kgp | ✅ 原生支持 |
| Ghostty | Kgp | ✅ 原生支持 |
| Warp / VSCode 终端 | Iip | ✅ 支持 |
| Alacritty | 无 | ❌ macOS 下只能降级 Chafa 字符画 |

**WezTerm 专项**：官方矩阵明确走 iTerm2 内联协议（Iip），开箱即用；WezTerm 自身的 Sixel 仅实验性、Kitty graphics 无独立文档页，Iip 即当前最佳路径。验证：`ya env` 输出中 `Adapter.matches: Iip` 即正确。

### tmux 内使用

`~/.tmux.conf` 开启透传三件套，改完重启 tmux：

```tmux
set -g allow-passthrough on
set -ga update-environment TERM
set -ga update-environment TERM_PROGRAM
```

## 其他实用集成

### 代码高亮与 bat

v26 内置 syntect 语法高亮，文本/代码预览默认带高亮，**bat 非必需**。想用 bat 的主题与参数，走官方 `piper` 插件：

```bash
ya pkg add yazi-rs/plugins:piper
```

```toml
# yazi.toml
[plugin]
prepend_previewers = [
	{ mime = "text/*", run = "piper bat --color=always --style=numbers,header" },
]
```

### 预览增强依赖（可选安装）

```bash
brew install ffmpeg sevenzip jq poppler resvg imagemagick
```

视频缩略图 / 归档预览解压 / JSON / PDF / SVG / 字体图标各对应其一。

### 垃圾桶

内置 `trash` crate 实现系统级回收站，macOS 下 `d` 直接进 **Finder 废纸篓**，无需 trash-cli；`g⇒t` 进回收站管理，`D` 才是永久删除。

## WezTerm + zsh 完整工作流（本指南参考环境的组装清单）

```zsh
# ~/.zshrc — 一套完整的现代终端文件管理工作流
eval "$(zoxide init zsh)"                          # 1. zoxide 数据库（yazi 与 shell 共享）
export FZF_DEFAULT_COMMAND="fd --type f --hidden --exclude .git"   # 2. fzf 列表来源

function y() {                                     # 3. 官方 wrapper（退出自动 cd）
	local tmp cwd
	tmp="$(mktemp -t "yazi-cwd.XXXXXX")"
	command yazi "$@" --cwd-file="$tmp"
	IFS= read -r -d '' cwd < "$tmp"
	[ "$cwd" != "$PWD" ] && [ -d "$cwd" ] && builtin cd -- "$cwd" || builtin true
	command rm -f -- "$tmp"
}
```

```bash
# 4. yazi 侧：插件 + 主题一键复现
ya pkg install   # 按 ~/.config/yazi/package.toml 装齐（详见配置指南）
```

装齐后：`y` 启动 → `Z` 跳历史目录 → `z` 模糊找文件 → `s`/`S` 递归搜索 → `q` 退出落回目标目录——全程手不离键盘。
