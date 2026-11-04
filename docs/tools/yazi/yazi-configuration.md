# Yazi 配置与定制指南

> 基准版本：yazi v26.8.15（2026-08-15）| 所有配置写法均为现行版本语法（`[mgr]`、`ya pkg` 等）

## 配置文件体系

配置目录：`~/.config/yazi/`（Windows：`%AppData%\yazi\config\`）

| 文件 | 职责 |
|---|---|
| `yazi.toml` | **行为**：布局、排序、打开器规则、预览、任务调度 |
| `theme.toml` | **外观**：配色、图标、文件类型样式、状态栏 |
| `keymap.toml` | **键位**：8 个交互层的按键绑定 |
| `init.lua` | Lua 初始化脚本（插件 setup 等） |
| `package.toml` | 包管理锁定文件（`ya pkg` 自动维护） |

核心设计思想——**稀疏覆盖**：内置默认配置随发布版打包，用户配置**只写想改的字段**即可，无需复制全量默认文件。规则类配置（`open`/`icon`/`previewer` 等）统一支持三种粒度：

```toml
rules         = [ ... ]   # 整体替换默认规则（慎用，会丢掉官方后续新增的默认规则）
prepend_rules = [ ... ]   # 插队默认之前，优先级更高（推荐）
append_rules  = [ ... ]   # 垫底默认之后（推荐做兜底）
```

**最佳实践**：定制优先用 `prepend_*` / `append_*`，避免整体 `rules` 替换导致官方升级新增的默认规则被丢失。

多套配置并存试用：`YAZI_CONFIG_HOME=~/.config/yazi-alt yazi`。

## yazi.toml 详解

### `[mgr]`：主界面（注意不是旧名 `[manager]`）

```toml
[mgr]
ratio          = [1, 4, 3]        # 三栏布局：父目录/当前/预览
sort_by        = "natural"        # none/mtime/btime/extension/alphabetical/natural/size/random
sort_dir_first = true             # 目录排前
linemode       = "none"           # 行模式：size/mtime/permissions/owner（装 git.yazi 后还有 git）
show_hidden    = false
scrolloff      = 5                # 光标距边缘保持行数
```

### `[opener]` 与 `[open]`：打开器规则体系

两段分工：`[opener]` **定义**打开器（怎么执行），`[open]` **分配**打开器（什么文件用哪个）。

```toml
[opener]
edit = [
  { run = '$EDITOR "$@"', desc = "Edit", block = true, for = "unix" },
]
view = [
  { run = 'open -a Preview "$@"', desc = "预览.app", for = "macos" },
]

[open]
prepend_rules = [
  { mime = "image/*", use = ["view", "open"] },  # use 数组：第一个是默认，其余进 o 菜单
]
```

打开器条目字段：`run` 命令模板、`desc` 描述、`block` 阻塞运行（适合交互式程序如 vim）、`orphan` 脱离进程存活（适合 GUI 程序）、`for` 平台限定。

**占位符**：`%s` 全部选中项路径、`%S` URL 形式、`%s1` 第 1 个选中项、`%d` 目录名、`%%` 字面 `%`。

三条关键语义：

1. **优先级 = 列表顺序**：prepend 在前、默认居中、append 在后，首条命中即生效
2. **append 的通配兜底优先于官方默认兜底**——官方原文保证，这正是"万物兜底进某编辑器"方案的原理（见下方案例 1）
3. glob 默认不区分大小写，要区分加 `\s` 前缀

### `[preview]`：预览区

| 选项 | 默认 | 说明 |
|---|---|---|
| `wrap` | `"no"` | 文本预览是否换行 |
| `max_width` / `max_height` | `600` / `900` | 图片预览最大像素，**修改后必须 `ya cache clear`** |
| `image_filter` | `"triangle"` | 缩放滤波：nearest < triangle < catmull-rom < lanczos3 |
| `cache_dir` | 系统缓存目录 | 系统缓存重启会清空，要持久化设绝对路径 |

### `[tasks]`：任务调度

**v26.5.6 起 `micro_workers` / `macro_workers` 已移除**，改为细粒度 worker：`file_workers`、`plugin_workers`、`fetch_workers` 等。旧教程写法在 v26 直接失效，一般用默认值即可。

## keymap.toml 覆盖机制

详见[快捷键参考的自定义章节](yazi-keybindings.md#自定义键位keymaptoml)。核心记忆点：

- `prepend_keymap` 覆盖默认（高优先级）/ `append_keymap` 新增（低优先级），两者互斥不可混用
- 禁用默认键：`run = "noop"`
- 配置保存自动热加载

## 插件生态最佳实践

### 包管理器 `ya pkg`（旧命令 `ya pack` 已弃用）

```bash
ya pkg add yazi-rs/plugins:smart-enter   # 安装（单仓多包用冒号）
ya pkg list                              # 列出已装
ya pkg upgrade                           # 全部升级（升级 yazi 后必做）
ya pkg delete yazi-rs/plugins:smart-enter
ya pkg install                           # 新机器按 package.toml 一键装齐
```

安装结果写入 `package.toml`（含 `rev`/`hash` 锁定），包本体落在 `plugins/<name>.yazi/`。把 `rev` 写成 `"=c591a36"`（等号前缀）可钉版本阻止升级漂移。

### 推荐插件（官方 yazi-rs/plugins，共 19 个）

| 插件 | 用途 |
|---|---|
| `smart-enter` | `l` 键合一：目录则进入、文件则打开 ⭐ 新手必装 |
| `smart-filter` | 增强过滤：连续过滤、唯一命中目录自动进入、提交即打开 |
| `smart-paste` | 粘贴到悬停目录（悬停文件则粘当前目录） |
| `jump-to-char` | Vim 式 `f<char>` 按首字符跳转 |
| `git` | 文件列表 linemode 显示 Git 状态（需 `linemode = "git"`） |
| `mount` | 磁盘挂载/卸载/弹出管理器 |
| `piper` | 任意 shell 命令作为预览器（如 `glow` 渲染 md、`bat` 高亮） |
| `diff` | 选中 vs 悬停文件 diff，可生成补丁 |
| `full-border` / `toggle-pane` | 四周边框美化 / 三栏显隐切换 |
| `mactag` | macOS Finder 文件标签读写（仅 macOS） |

社区精选：[dedukun/bookmarks.yazi](https://github.com/dedukun/bookmarks.yazi)（Vi 式书签，要求 v25.4.8+）等。

**三条最佳实践**：
1. 插件只保证兼容**最新版** yazi——升级 yazi 后记得 `ya pkg upgrade`
2. 绑定插件键位一律用 `prepend_keymap`，避免与默认键冲突时沉默失效
3. 社区插件安装前确认其 README 标注的最低 yazi 版本

### 插件开发入口

每个插件是 `<name>.yazi/` 目录，入口 `main.lua`；调试用 `YAZI_LOG=debug yazi`，日志在 `~/.local/state/yazi/yazi.log`。

## 主题定制（Flavor 机制）

Flavor = 预制主题包（`flavor.toml` 配色 + `tmtheme.xml` 代码高亮），与插件共用 `ya pkg` 包管理器：

```bash
ya pkg add yazi-rs/flavors:catppuccin-mocha
```

官方托管：`catppuccin` 四口味、`dracula`；社区 30+：tokyo-night、kanagawa、gruvbox、rose-pine、nord 等（见 [yazi-rs/flavors](https://github.com/yazi-rs/flavors)）。

启用与覆盖（`theme.toml`）：

```toml
[flavor]
dark  = "catppuccin-mocha"
light = "catppuccin-latte"    # v26.8.15 起支持跟随终端自动暗/亮切换
```

**官方语义**：用户的 `theme.toml` 与 flavor 的 `flavor.toml` **自动合并，用户永远优先**。因此最佳实践是——`theme.toml` 保持"只放 `[flavor]` + 想覆盖的小块"，不要全量复制样式。注意启用 flavor 后 `syntect_theme` 失效（代码高亮固定用 flavor 自带的 `tmtheme.xml`）。

## 实战案例（提炼自真实生产配置）

### 案例 1：`url = "*"` 万物兜底进 VS Code

思路：把"打开"统一收敛到一个编辑器，只有明确更强的规则（图片/PDF、压缩包、音视频）插队；兜底靠官方"append 通配压默认通配"语义。

```toml
# yazi.toml
[opener]
vscode  = [{ run = 'open -a "Visual Studio Code" %s', desc = "VS Code", for = "macos" }]
preview = [{ run = 'open -a Preview %s', desc = "预览.app", for = "macos" }]

[open]
prepend_rules = [
  # 图片 / PDF → 预览.app（右侧面板预览不受影响，此处只管"打开"动作）
  { mime = "image/*", use = ["preview", "open"] },
  { mime = "application/pdf", use = ["preview", "open"] },
  # 压缩包 / 音视频 → 保持官方默认（解压 / 播放）
  { mime = "application/{zip,rar,7z*,tar,gzip,xz,zstd,bzip*,lzma,compress,archive,cpio,arj,xar,ms-cab*}", use = ["extract", "reveal"] },
  { mime = "{audio,video}/*", use = ["play", "reveal"] },
  # 其余一切（md/txt/源码/json/无扩展名...）→ VS Code；按 O 仍可自选
  { url = "*", use = ["vscode", "open", "reveal"] },
]
```

跨平台使用需补 `for = "linux"` 条目（如 `xdg-open`）。

### 案例 2：smart-enter + prepend_keymap

```toml
# keymap.toml
# 默认 l/<Right> 只绑 enter（仅进目录），文件上无反应；
# smart-enter 让 l 在目录上=进入、文件上=按 opener 规则打开
[mgr]
prepend_keymap = [
  { on = "l",       run = "plugin smart-enter", desc = "进入目录或打开文件" },
  { on = "<Right>", run = "plugin smart-enter", desc = "进入目录或打开文件" },
]
```

必须 `prepend_keymap`（首条匹配机制下才能接管默认 `l`）；大写 `L`（历史前进）不受影响。**键位定制三件套**：keymap.toml + 插件 + opener 规则，一个键的增强同时涉及覆盖机制与打开器链路，是理解 yazi 定制体系的最佳入门案例。

### 案例 3：主题三件套

```toml
# theme.toml — 主体交给 flavor，只精准覆盖小块
[flavor]
dark  = "catppuccin-mocha"
light = "catppuccin-mocha"

[app]
overall = { bg = "#1e1e2e" }     # 整体背景

[mgr]
cwd = { fg = "#94e2d5" }          # 路径颜色
```

配合 `package.toml`（`ya pkg` 自动维护、锁定 rev/hash）纳入 dotfiles，新机器 `ya pkg install` 一键复现全部插件与主题。

## 版本时效：v25 → v26 破坏性变更

旧教程/旧配置迁移必读（完整逐版本清单见官方 [CHANGELOG](https://github.com/sxyazi/yazi/blob/main/CHANGELOG.md)）：

| 旧写法 | 现写法 | 弃用起点 |
|---|---|---|
| `[manager]` | `[mgr]` | v25.5.28 |
| `ya pack -a <pkg>` | `ya pkg add <pkg>` | v25.5.28 |
| `yazi --debug` | `ya env` | v26.8.15 帮助文本标注 |
| `yazi --clear-cache` | `ya cache clear` | 同上 |
| `shell "cmd %s"` | `shell -- cmd %s` | v25.2.7 |
| 插件入口 `init.lua` | `main.lua` | v25.2.7 |
| 默认 `z`=zoxide / `Z`=fzf | **互换**：`Z`=zoxide / `z`=fzf | v25.4.8 |
| `micro_workers` / `macro_workers` | 细粒度 worker | v26.5.6 移除 |
| 默认 `t`（新建标签页） | chord `t⇒t`（新建）/ `t⇒r`（重命名） | v26.5.6 |

v26.8.15 新增亮点：拖放（DnD）、**系统回收站**、批量新建、帮助菜单升级为命令面板、输入历史、暗/亮主题自动切换、`H/M/L` 视口级光标移动。

**检查旧资料时**：见到 `[manager]`、`ya pack`、`shell "..."` 即可判定为过期教程。程序内以 `~` 帮助菜单显示的实际值为最终裁决。
