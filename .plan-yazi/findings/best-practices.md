# Yazi 配置体系与定制最佳实践 — 调研底稿

> **调研基准**: yazi v26.8.15（2026-08-15 发布，本机 Homebrew 安装版实测）
> **调研日期**: 2026-09-01
> **调研方式**: 官方文档（yazi-rs.github.io）+ 官方插件/主题仓库 + CHANGELOG 逐版本核对 + 本机二进制与真实配置验证
> **用途**: 撰写中文使用指南的底稿，所有结论均标注来源；撰写正式文档时可按需裁剪

---

## 目录

1. [配置文件体系总览](#1-配置文件体系总览)
2. [yazi.toml 详解](#2-yazitoml-详解)
3. [keymap.toml 覆盖机制](#3-keymaptoml-覆盖机制)
4. [插件生态最佳实践](#4-插件生态最佳实践)
5. [主题定制与 Flavor 机制](#5-主题定制与-flavor-机制)
6. [本机配置实战案例提炼](#6-本机配置实战案例提炼)
7. [版本时效注意：v25 → v26 破坏性变更](#7-版本时效注意v25--v26-破坏性变更)
8. [来源清单](#8-来源清单)

---

## 1. 配置文件体系总览

### 1.1 文件清单与职责划分

Yazi 官方口径的"三大配置文件"（来源：[Configuration Overview](https://yazi-rs.github.io/docs/configuration/overview)，v26.8.15）：

| 文件 | 职责 | 位置（macOS/Linux） |
|---|---|---|
| `yazi.toml` | **行为配置**：布局、排序、打开器规则、预览、任务调度 | `~/.config/yazi/yazi.toml` |
| `theme.toml` | **外观配置**：配色、图标、文件类型样式、状态栏 | `~/.config/yazi/theme.toml` |
| `keymap.toml` | **键位配置**：8 个交互层的按键绑定 | `~/.config/yazi/keymap.toml` |

除三大件外，实际生态中还会出现的文件：

| 文件 | 职责 | 备注 |
|---|---|---|
| `init.lua` | Lua 初始化脚本，用于插件 setup 等 | 用户级；**注意与插件内部的 `main.lua` 区分**（见 4.3） |
| `package.toml` | **包管理锁定文件**，由 `ya pkg` 自动维护 | 记录已装插件/flavor 的 `use`/`rev`/`hash`（见 4.2） |
| `vfs.toml` | 虚拟文件系统（VFS）配置，SFTP 等 remote provider | **v25.12.29 引入 VFS**；v26.8.15 将 `[services.domain]` 改名 `[sftp.domain]`（来源：CHANGELOG） |

Windows 路径为 `%AppData%\yazi\config\`（来源同上）。

### 1.2 配置目录切换

导出 `YAZI_CONFIG_HOME` 环境变量即可切换整套配置目录，官方示例：

```sh
YAZI_CONFIG_HOME=~/.config/yazi-alt yazi
```

适合"多套配置并存试用"的场景（来源：Configuration Overview）。

### 1.3 覆盖合并语义（最重要的设计）

官方原文（Configuration Overview，译文）：

> "你配置文件中的选项会覆盖默认值。Yazi 已在发布版中内置了默认配置，所以**不需要完整复制默认文件**，除非你想彻底替换。"

- 用户配置是**稀疏覆盖**：只写想改的字段，其余字段自动落到内置默认（preset 源码在 `shipped` 分支 `yazi-config/preset/`）。
- 规则类配置（`open`、`icon`、`previewer`、`preloader` 及 `theme.toml` 中的 `filetype`/`icon` 规则）支持三种粒度：
  - `rules = [...]` / `dirs = [...]` 等：**整体替换**默认规则；
  - `prepend_rules` / `prepend_*`：**插队到默认规则之前**（优先级更高）；
  - `append_rules` / `append_*`：**垫底到默认规则之后**（优先级更低）。
  - 官方原文："They are also available for open, icon, previewer, and preloader rules."（同上来源）

**最佳实践**：定制优先用 `prepend_*`/`append_*`，避免整体 `rules = [...]` 导致官方后续新增的默认规则（如 v26 新增的 trash/vfs 规则）被自己覆盖丢失。

---

## 2. yazi.toml 详解

来源：[yazi.toml Reference](https://yazi-rs.github.io/docs/configuration/yazi)（v26.8.15）+ 默认值取自官方 preset 文件 `yazi-default.toml`（`shipped` 分支，v26.8.15 对应版本）。

### 2.1 `[mgr]`：管理器主区（v25.5.28 起为 `[mgr]`，旧名 `[manager]` 已弃用）

| 选项 | 默认值 | 说明 |
|---|---|---|
| `ratio` | `[1, 4, 3]` | 三栏布局比例：父目录/当前目录/预览，按 1/8、4/8、3/8 分配；某栏设 `0` 可隐藏，至少一栏非零 |
| `sort_by` | `"alphabetical"` | 可选 `none`/`mtime`/`btime`/`extension`/`alphabetical`/`natural`/`size`/`random` |
| `sort_sensitive` | `false` | 排序是否区分大小写 |
| `sort_reverse` | `false` | 反转排序方向 |
| `sort_dir_first` | `true` | 目录排前 |
| `sort_translit` | `false` | 音译排序（如 `Â`→`A`），仅 `sort_by = "natural"` 时生效 |
| `sort_fallback` | `"alphabetical"` | **v26.5.6 新增**，控制并列时的兜底排序 |
| `linemode` | `"none"` | 行模式；可 `"size"`/`"mtime"`/`"permissions"`/`"owner"`，装 `git.yazi` 后还有 `"git"` |
| `show_hidden` | `false` | 显示隐藏文件 |
| `show_symlink` | `true` | 符号链接后显示目标路径 |
| `scrolloff` | `5` | 光标距边缘保持行数 |
| `mouse_events` | `["click", "scroll", "drag"]` | 鼠标事件 |

### 2.2 `[opener]` 与 `[open]`：打开器规则体系

**`[opener]` 定义"打开器"**，每个打开器是若干"命令条目"的数组，Yazi 按当前 OS 取匹配条目。条目字段：

| 字段 | 说明 |
|---|---|
| `run` | 命令模板，支持占位符（见下表） |
| `desc` | 描述，显示在 `o` 打开菜单与帮助里 |
| `block` | 阻塞运行：切到备用屏幕，适合交互式程序（如 vim） |
| `orphan` | 进程脱离 Yazi 存活，适合 GUI 程序 |
| `for` | 限定 OS：`unix`/`macos`/`linux`/`windows`/`android` |

**占位符**（yazi.toml 文档原文核对）：

| 占位符 | 含义 |
|---|---|
| `%s` | **全部选中项的路径**（官方 preset 同款用法） |
| `%S` | 全部选中项的 URL 形式 |
| `%s1`/`%S1` | 第 1 个选中项的路径/URL（`%sN` 泛化） |
| `%d` / `%D` | 全部选中项的目录名（路径/URL 形式），`%dN` 泛化 |
| `%%` | 字面 `%` 本身 |

**`[open]` 决定"什么文件用哪个打开器"**，规则字段 `url`（对路径做 glob）、`mime`（对 MIME 做 glob）、`use`（打开器名，可数组）：

```toml
[open]
prepend_rules = [ ... ]   # 插队默认规则之前，优先级最高
rules         = [ ... ]   # 整体替换默认规则（慎用）
append_rules  = [ ... ]   # 垫底默认规则之后
```

三条官方语义（yazi.toml 文档原文核对）：

1. **优先级 = 列表顺序**：prepend 在最前、默认居中、append 在最后，自上而下首条命中即生效。
2. **append 兜底优先于默认兜底**："append_rules 中的通配规则将始终优先于默认的通配兜底规则"——即自己的 `url = "*"` 兜底能压过官方 `url = "*"` 兜底，这正是"万物兜底进某编辑器"方案的原理。
3. **glob 默认不区分大小写**；要区分大小写加 `\s` 前缀。
4. `use` 为数组时多个打开器被合并进菜单：直接打开走第一个；按 `o`（或 `open --interactive`）弹出"打开方式"菜单自选。

**官方默认 `[open].rules` 关键内容**（preset 核对，v26.8.15）：目录→edit/reveal；文本→edit/reveal；图片→open/reveal；音视频→play/reveal；代码→edit/reveal；压缩包→extract/reveal；空文件→edit；VFS 缺失/过期→download；**兜底 `url = "*"` → open/reveal**。

**官方默认打开器**：`edit`（`$EDITOR`，block）、`open`（macOS 用 `open %s`，Linux 用 `xdg-open %s1`）、`reveal`（macOS 用 `open -R %s1`）、`extract`（`ya pub extract --list %s`）、`play`、`download`、`trash`（v26 新增）。

### 2.3 `[preview]`：预览区

| 选项 | 默认值 | 说明 |
|---|---|---|
| `wrap` | `"no"` | 文本预览换行 `"yes"`/`"no"` |
| `tab_size` | `2` | Tab 宽度 |
| `max_width` / `max_height` | `600` / `900` | 图片预览最大像素；**修改后必须 `ya cache clear`**（文档原文强调） |
| `cache_dir` | `""`（系统缓存目录） | 系统缓存目录**重启会被清空**；要持久化设绝对路径 |
| `image_delay` | `30` | 发送图片数据前等待毫秒数 |
| `image_filter` | `"triangle"` | 缩放滤波：`nearest` < `triangle` < `catmull-rom` < `lanczos3`（由快/糙到慢/精） |
| `image_quality` | `75` | 压缩质量，取值 50–90 |
| `ueberzug_scale` / `ueberzug_offset` | `1` / `[0,0,0,0]` | Überzug++ 尺寸偏移补偿（修其计算 bug，如 2x 缩放的 Wayland/Hyprland 设 0.5） |

注意：**本版本文档已无 `sixel_fraction`**（v25.5.28 移除）。

### 2.4 图片预览协议（自动探测，来源：[Image Preview](https://yazi-rs.github.io/docs/image-preview)）

Yazi 按**自上而下的优先级**自动选择协议，探测依据 `$TERM`、`$TERM_PROGRAM`、`$XDG_SESSION_TYPE`（不要覆盖这些变量）：

1. **Kgp** Kitty unicode placeholders —— kitty (>= 0.28.0)、Ghostty
2. **Iip** Inline images —— iTerm2、WezTerm、Warp、Tabby、VSCode、Bobcat
3. **KgpOld** Kitty 旧协议 —— Konsole（tmux 下不可用）
4. **Sixel** —— foot、Windows Terminal、st（sixel patch）、Black Box
5. **Überzug++**（X11/Wayland 窗口协议）—— 其余终端兜底；Wayland 仅 Hyprland/Sway/Niri/Wayfire
6. **Chafa** ASCII/字符画兜底 —— 需 Chafa >= 1.16.0

验证当前生效协议：`ya env` 查看 `Adapter.matches` 字段（本机可用）。

tmux 使用三件套（官方配方）：

```
set -g allow-passthrough on
set -ga update-environment TERM
set -ga update-environment TERM_PROGRAM
```

macOS 常用终端（iTerm2/WezTerm/Ghostty/kitty）均在第一梯队支持。

### 2.5 `[tasks]`：任务调度

**v26.5.6 起 `micro_workers`/`macro_workers` 已移除**，改为细粒度 worker：`file_workers`、`plugin_workers`、`fetch_workers`、`preload_workers`、`process_workers`；另有 `bizarre_retry`（怪异失败重试上限）、`image_alloc`（单图解码内存上限，`0` 不限）、`image_bound`（`[宽, 高]` 像素上限，`0` 不限）、`suppress_preload`。旧教程里的 `micro_workers` 写法在 v26 会失效。

### 2.6 其余段落（速览）

- `[plugin]`：注册 `previewers`/`preloaders`/`fetchers`/`spotters` 规则（见 4.4）。
- `[input]`/`[confirm]`/`[pick]`：各输入/确认/选择组件的位置（`origin` + `offset` 四元组）与标题定制；`[input]` 有 `cursor_blink`，并支持按场景微调（`cd_origin`、`rename_title` 等）。
- `[which]`：快捷键提示面板，v26.8.15 起可配 `border`。

---

## 3. keymap.toml 覆盖机制

来源：[keymap.toml Reference](https://yazi-rs.github.io/docs/configuration/keymap)（v26.8.15）。

### 3.1 八个交互层

`[mgr]`（文件列表主层）、`[tasks]`、`[spot]`（spot 信息面板）、`[pick]`、`[input]`、`[confirm]`、`[cmp]`（补全）、`[help]`。注意 `[manager]` 旧名已弃用（同 2.1）；`[which]` 不是键位层，只是 UI 组件。

### 3.2 绑定条目结构

```toml
{ on = "l",                run = "plugin smart-enter",     desc = "进入目录或打开文件" },
{ on = [ "g", "d" ],       run = "arrow top",              desc = "跳到顶部" },      # chord 前缀键
{ on = "<C-S-b>",          run = [ "act1", "act2" ],       desc = "多动作" },        # 动作数组顺序执行
{ on = "x",                run = "shell -- trash-put %s",  desc = "移入回收站", for = "macos" },
```

- `on`：单键字符串或键序列数组（数组即 chord，如 `[ "g", "d" ]`，长度不限）。
- `run`：单个动作或动作数组。
- `desc`：显示于帮助/`which` 面板。
- `for`：可选 OS 限定（v25.4.8 新增），`linux`/`macos`/`windows`/`android`/`unix`。

**键记法**：修饰键 `<S-…>`(Shift)、`<C-…>`(Ctrl)、`<A-…>`(Alt)、`<D-…>`(Cmd/Win/Super，需 CSI u 支持)；特殊键 `<Space>`、`<Tab>`、`<Enter>`、`<Esc>`、`<F1>`–`<F19>` 等。注意：未开 CSI u 时 `<Tab>`/`<C-i>`、`<Enter>`/`<C-m>` 在协议层不可区分。

### 3.3 prepend_keymap vs append_keymap（核心语义）

官方原文（译文核对）：

> "prepend 插入到默认键位之前，append 插入之后。由于 Yazi 执行**第一个匹配**的按键规则，因此 **prepend 的优先级总是高于默认，append 总是低于默认**。"

- 两者互斥：同一层只能用其中一个，不能同时写（TOML 也不允许同名键）。
- 被遮蔽的默认规则**并没有被删除**，只是永远轮不到执行。要"显式禁用"某默认键，用 `run = "noop"`（按下不触发任何动作，且不会出现在 which 面板）。
- `keymap = [...]`（不带前缀）= **全量替换**该层所有默认键位，慎用。

### 3.4 `run` 的三种写法

| 类型 | 语法 | 示例 |
|---|---|---|
| 内置命令 | `命令 [参数]` | `arrow 5`、`quit --no-cwd-file`、`arrow top`、`tab_switch 2 --relative` |
| 插件 | `plugin <名> [-- 参数]` | `plugin smart-enter`、`plugin mount`、`plugin jump-to-char -- f` |
| Shell | `shell [--block|--orphan|--interactive] -- <命令原文>` | `shell --block -- tar -xvf %s` |

`--` 之后的内容按**原文**处理，无需转义（v25.2.7 引入，官方推荐写法）。键位上下文占位符与 opener 类似且更丰富：`%h` 悬停项、`%s` 全部选中、`%sN`、`%d`/`%dN` 目录名、`%y`/`%yN` 已剪切/复制项、`%tX` 其他标签页，以及对应大写的 URL 形式（`%H`/`%S`/`%D`/`%Y`/`%TX`）；`%%` 转义。v26.8.15 另新增实验性 `%y/%Y/%t/%T` 系列。

**v26.5.6 起**允许在键位里跨层调用其他组件的动作（如在 `[input]` 层调用 `[mgr]` 的命令）。

---

## 4. 插件生态最佳实践

### 4.1 包管理器 `ya pkg`（v25.5.28 起 `ya pack` 弃用）

本机 v26.8.15 二进制实测子命令（`ya pkg --help`）：

| 命令 | 作用 |
|---|---|
| `ya pkg add <owner>/<repo>` | 安装；单仓多包用冒号 `ya pkg add yazi-rs/plugins:smart-enter` |
| `ya pkg delete ...` | 卸载（语法同 add，可一次多个） |
| `ya pkg install` | 新机器上按锁定文件 `package.toml` 一键装齐 |
| `ya pkg list` | 列出已管理的包 |
| `ya pkg upgrade` | 升级全部（v25.12.29 起支持只升级指定包） |

实用细节（来源：[CLI 文档](https://yazi-rs.github.io/docs/cli) + CHANGELOG v26.5.6）：

- **钉版本**：`package.toml` 中把 `rev` 写成 `"=c591a36"`（等号前缀）可阻止升级漂移。
- `ya pkg --discard`（v26.5.6 新增）：丢弃对已装包的本地改动（比如你手改过插件源码想还原）。
- `yazi` 与 `ya` **版本必须完全一致**（官方 CLI 文档原文强调）。
- 安装结果写入 `~/.config/yazi/package.toml`，包本体落在 `~/.config/yazi/plugins/<name>.yazi/` 或 `flavors/<name>.yazi/`。

### 4.2 `package.toml` 结构（本机实测样例）

```toml
[[plugin.deps]]
use = "yazi-rs/plugins:smart-enter"
rev = "c591a36"                                   # 锁定的 commit
hash = "187cc58ba7ac3befd49c342129e6f1b6"         # 内容校验

[[flavor.deps]]
use = "yazi-rs/flavors:catppuccin-mocha"
rev = "20b47bf"
hash = "ce320f877fe709b189433941aba747c4"
```

**最佳实践**：把 `~/.config/yazi` 整个目录纳入 dotfiles 管理，`package.toml` + `ya pkg install` 即可在新机器复现全部插件与主题。

### 4.3 插件目录结构

每个插件是一个 kebab-case 命名、以 `.yazi` 结尾的目录，至少含 `main.lua`（入口，v25.2.7 起取代旧名 `init.lua`）、`README.md`、`LICENSE`（本机 `~/.config/yazi/plugins/smart-enter.yazi/` 实测正是这三件）。插件系统 async-first：带 `--- @sync entry` / `--- @sync peek` 注解的是同步插件；预览器需实现 `peek`/`seek`，预加载器需实现 `preload`（返回布尔决定是否重试）。调试：`YAZI_LOG=debug yazi` + `ya.dbg()`，日志在 `~/.local/state/yazi/yazi.log`。

### 4.4 官方插件清单（yazi-rs/plugins，共 19 个，来源：仓库 README）

**文件操作与导航类**：

| 插件 | 用途 |
|---|---|
| `smart-enter` | 光标在目录上=进入、在文件上=按 opener 规则打开，一键两用（官方 README：`ya pkg add yazi-rs/plugins:smart-enter`） |
| `smart-filter` | 更聪明的过滤：连续过滤、唯一目录自动进入、回车直接打开 |
| `smart-paste` | 粘贴到悬停的目录（悬停文件则粘到当前目录） |
| `jump-to-char` | Vim 式 `f<char>`：跳到下一个以指定字符开头的文件名 |
| `visual-pivot` | 可视模式中把光标跳到选区另一端且保持选中 |
| `bookmarks`（社区 dedukun/bookmarks.yazi） | Vi 式书签标记，`''` 回到上一位置（社区插件，README 注明要求 yazi v25.4.8+） |

**信息显示类**：

| 插件 | 用途 |
|---|---|
| `git` | 文件列表 linemode 显示 Git 状态（需 `linemode = "git"`） |
| `vcs-files` | 搜索视图里展示 Git 变更文件清单 |
| `mount` | 磁盘/分区挂载、卸载、弹出管理器（官方，v25.2.7 随版本发布） |
| `piper` | 把任意 shell 命令的输出作为预览器（如 `glow` 渲染 md、`bat` 渲染任意文件） |
| `diff` | 选中文件 vs 悬停文件做 diff，可生成实时补丁并复制 |
| `mime-ext` | 用扩展名替代内建 `file(1)` 判定 MIME，提速 |
| `zoom` | 预览图片放大/缩小（v25.12.29 特性配套官方插件） |

**外观类**：

| 插件 | 用途 |
|---|---|
| `full-border` | 四周完整边框美化 |
| `toggle-pane` | 切换父目录/当前/预览三栏的显示、隐藏、最大化（取代社区旧款 max-preview/hide-preview） |
| `no-status` | 移除状态栏 |
| `mactag` | macOS 文件标签读写（macOS 专属） |
| `term-cwd` | 通过 OSC 通知终端当前目录（影响终端标题等） |
| `types` | Lua API 类型定义，插件开发辅助 |

**最佳实践**：
1. 插件只保证与最新版 yazi 兼容（官方 README 原文警告），升级 yazi 后记得 `ya pkg upgrade`。
2. 绑定插件键位一律用 `prepend_keymap`，避免与默认冲突时沉默失效。
3. 社区插件（bookmarks、sudo、fzf 类等）安装前确认其 README 标注的最低 yazi 版本。

---

## 5. 主题定制与 Flavor 机制

来源：[theme.toml Reference](https://yazi-rs.github.io/docs/configuration/theme) 与 [Flavors Overview](https://yazi-rs.github.io/docs/flavors/overview)（均为 v26.8.15 文档）。

### 5.1 Flavor = 预制主题包

- 位置：`~/.config/yazi/flavors/<name>.yazi/`；结构：`flavor.toml`（与用户 theme.toml 同格式）+ `tmtheme.xml`（代码高亮配色）+ `README.md` + `preview.png` + 双 LICENSE。
- 启用：`theme.toml` 中

```toml
[flavor]
dark  = "catppuccin-mocha"
light = "catppuccin-latte"    # 也可 dark/light 同名
```

v26.8.15 新增**跟随终端自动暗/亮切换**（CHANGELOG #4196），配 dark/light 双值即可自动切换。

### 5.2 覆盖优先级（关键）

官方原文（Flavors Overview，译文）：

> "Yazi 会自动把用户的 theme.toml 与 flavor 的 flavor.toml 合并，**用户的永远优先于 flavor**。"

配套警告：

> "确保你的 theme.toml 里除了 `[flavor]` 之外不要写别的东西，**除非你就是想覆盖某些样式**。"

由此形成的最佳实践：装了 flavor 后，用户 `theme.toml` 保持"只放想覆盖的小块"（如本机覆盖 `[app] overall` 背景与 cwd 颜色）；注意 `syntect_theme` 在启用 flavor 后**无效**——flavor 固定使用自带的 `tmtheme.xml`（theme.toml 文档原文）。

- 未被任何一方定义的样式落到内置 preset。
- `filetype`/`icon` 规则同样支持 `prepend_*`/`append_*`（Configuration Overview 明示适用于 open/icon/previewer/preloader 规则；theme.toml 文档确认 icon 的 globs/dirs/files/exts/conds 可整体替换）。

### 5.3 官方与社区 Flavor（来源：yazi-rs/flavors README）

- **官方托管（yazi-rs/flavors）**：`catppuccin-mocha` / `catppuccin-latte` / `catppuccin-frappe` / `catppuccin-macchiato`、`dracula`。
- **社区（README 精选）**：`tokyo-night`（BennyOe）、`kanagawa` / `kanagawa-dragon` / `kanagawa-lotus` / `kanagawa-paper`、`gruvbox-dark` / `gruvbox-light` / `gruvbox-material`、`everforest-medium`、`rose-pine` 系列、`nord`、`ayu-dark`、`flexoki-dark/light`、`monokai`、`bluloco-dark/light` 等 30+。
- 安装语法：`ya pkg add yazi-rs/flavors:catppuccin-mocha`（flavor 与插件共用同一包管理器）。
- 官方提示：使用前确认 flavor 与你的 yazi 版本兼容；可用 `taplo check --schema https://yazi-rs.github.io/schemas/theme.json flavor.toml` 校验配置（Flavors Overview 原文）。

### 5.4 theme.toml 主要段落速览

`[mode]`（normal/select/unset 各 main/alt 配色）、`[mgr]`（cwd、find 高亮、四色 marker、count、border）、`[tabs]`（active/inactive）、`[status]`（分隔符 `sep_left/sep_right`、权限色、进度条、`overall` 整体背景）、`[indicator]`（parent/current/preview 指示条）、`[spot]`/`[input]`/`[pick]`/`[confirm]`/`[cmp]`/`[tasks]`/`[which]`/`[help]`/`[notify]`、`[filetype].rules`（mime/url/is 匹配 + fg/bg/bold/italic）、`[icon]`（五级规则：globs→dirs→files→exts→conds；globs 最慢、后四者启动时编译为 HashMap O(1) 查找）。v26.8.15 起 `[help]` 段字段改名：`on`→`chord`、`run`+`desc`→`action`，`footer` 移除。

---

## 6. 本机配置实战案例提炼

以下示例由本机生产配置（`~/.config/yazi/`，yazi 26.8.15，作者 mike，2026-08-26/31 落地并持续使用）改写为通用版本，**灵感来源注明为真实生产配置**。

### 案例 1：`url = "*"` 万物兜底进 VS Code（yazi.toml）

思路：把"打开"统一收敛到一个编辑器，只有明确更强的规则（图片/PDF→预览.app、压缩包→解压、音视频→播放器）插队；兜底规则利用"append_rules 通配优先于默认通配"的官方语义压过官方 `url = "*"`。

```toml
# yazi.toml — 打开器规则（灵感来源：本机真实生产配置）
# 占位符 %s = 全部选中项路径（与官方 preset 同款用法）
# prepend_rules 插队在默认规则前；列表顺序即优先级；url="*" 为万物兜底
[opener]
vscode = [
  { run = 'open -a "Visual Studio Code" %s', desc = "VS Code", for = "macos" },
]
preview = [
  { run = 'open -a Preview %s', desc = "预览.app", for = "macos" },
]

[open]
prepend_rules = [
  # 图片 / PDF → 预览.app（右侧面板预览不受影响，这里只管"打开"动作）
  { mime = "image/*", use = ["preview", "open"] },
  { mime = "application/pdf", use = ["preview", "open"] },
  # 压缩包 → 保持官方默认（解压），不进 VS Code
  { mime = "application/{zip,rar,7z*,tar,gzip,xz,zstd,bzip*,lzma,compress,archive,cpio,arj,xar,ms-cab*}", use = ["extract", "reveal"] },
  # 音视频 → 保持官方默认（系统播放器）
  { mime = "{audio,video}/*", use = ["play", "reveal"] },
  # 其余一切（md/txt/无扩展名/源码/json/...）→ VS Code；按 o 仍可自选系统默认
  { url = "*", use = ["vscode", "open", "reveal"] },
]
```

要点：`use` 数组第一个是双击/l 键的默认动作，其余进 `o` 菜单；`for = "macos"` 限定平台，跨平台需补 `for = "linux"` 条目（如 `xdg-open`）。

### 案例 2：smart-enter + prepend_keymap（keymap.toml）

```toml
# keymap.toml — 官方 smart-enter 插件（灵感来源：本机真实生产配置）
# 默认 l/<Right> 只绑 enter（仅进目录），在文件上无反应；
# smart-enter 让 l 在目录上=进入、文件上=按 opener 规则打开
[mgr]
prepend_keymap = [
  { on = "l",       run = "plugin smart-enter", desc = "进入目录或打开文件" },
  { on = "<Right>", run = "plugin smart-enter", desc = "进入目录或打开文件" },
]
```

要点：必须 `prepend_keymap`——prepend 优先级高于默认的首条匹配机制（见 3.3），才能让插件接管默认的 `l`；大写 `L`（forward 历史前进）不受影响。

### 案例 3：主题三件套（package.toml + theme.toml）

```toml
# theme.toml — Catppuccin Mocha（灵感来源：本机真实生产配置）
[flavor]
dark  = "catppuccin-mocha"
light = "catppuccin-mocha"

# 以下是"有意覆盖 flavor"的小块：整体背景与 cwd 颜色
[app]
overall = { bg = "#1e1e2e" }

[mgr]
cwd = { fg = "#94e2d5" }
```

```toml
# package.toml — 由 ya pkg 自动维护，纳入 dotfiles 即可复现
[[plugin.deps]]
use = "yazi-rs/plugins:smart-enter"
rev = "c591a36"
hash = "187cc58ba7ac3befd49c342129e6f1b6"

[[flavor.deps]]
use = "yazi-rs/flavors:catppuccin-mocha"
rev = "20b47bf"
hash = "ce320f877fe709b189433941aba747c4"
```

要点：体现 5.2 的官方语义——`theme.toml` 大体只有 `[flavor]`，另写两个小块做精准覆盖；代码高亮色由 flavor 自带 `tmtheme.xml` 接管（本机另存 `Catppuccin-mocha.tmTheme` 是未装 flavor 时代的旧产物，启用 flavor 后 `syntect_theme` 实际失效，可清理）。

---

## 7. 版本时效注意：v25 → v26 破坏性变更

> 旧教程/旧配置迁移必读。来源：官方 [CHANGELOG](https://github.com/sxyazi/yazi/blob/main/CHANGELOG.md) 逐版本核对 + 本机 26.8.15 二进制 `--help` 实测。

### v25.x 系列

| 版本 | 变更 | 影响 |
|---|---|---|
| v25.2.7 | 插件入口 `init.lua`→`main.lua`；`shell`/`plugin` 命令引入 `--` 原文标记 | 旧插件写法需升级；复杂命令不再要转义 |
| v25.2.26 | theme `[completion]`→`[cmp]`；`separator_open/close`→`sep_left/sep_right` | 旧 theme.toml 迁移点 |
| v25.4.8 | 默认键 `z`（zoxide 跳转）与 `Z`（fzf 搜索）**互换**；previewer 同步改 `@sync peek` 注解 | 按旧文档写 z/Z 脚本会反 |
| **v25.5.28** | **`[manager]` 弃用改 `[mgr]`**；**`ya pack` 弃用改 `ya pkg`**；`tab_active/tab_inactive` 移入新 `[tabs]`；`tab_width`、`sixel_fraction` 移除 | **最重要迁移点**；官方 README 注明包管理器 `ya pkg` 于 v25.5.31 正式引入 |

### v25 → v26 之间的功能分水岭

| 版本 | 变更 | 影响 |
|---|---|---|
| v25.12.29（2025-12-29） | **引入虚拟文件系统（VFS）与远程文件管理**，新增配置文件 `vfs.toml`；`[app].overall` 整体背景色；预览缩放 | 主题文件里出现 `vfs/*`、`trash/**` 等新 MIME 属正常 |
| v26.1.x | VFS 支持外部命令预览器；压缩包树状预览、支持 `.tar.gz` 等 | — |
| v26.5.6 | **Lua 升 5.5**；`micro_workers`/`macro_workers` 移除改细粒度 workers；`title_format` 移除；默认 `t` 改为 chord `t⇒t`（新建 tab）、`t⇒r`（重命名 tab）；fetcher 规则 `id`→`group`；新增 `sort_fallback`、`app:theme` 主题热重载、`ya exec` | 旧 `[tasks]` 配置与 `t` 键位教程失效 |

### v26.8.15（当前基准版）

新增：拖放（DnD）、**回收站（trash bin）**、批量创建（bulk create）、帮助菜单升级为命令面板、输入历史、自动暗/亮主题切换、自定义 VFS provider、`H/M/L` 视口级光标移动、输入移动新 gait（`fine`/`lean`/`wide`，见 keymap.toml 的 `[gait]` 段）。

改名/弃用：`copy dirname`→`copy dirpath`；`backward --far`/`forward --far`→`backward wide`/`forward wide`；theme `[help]` 的 `on`→`chord`、`run/desc`→`action`；`<BackTab>`→`<S-Tab>`；vfs.toml `[services.domain]`→`[sftp.domain]`；`archive://` 不再内建（改由插件注册）。

### CLI 弃用（本机 v26.8.15 二进制 `yazi --help` 原文验证）

| 旧写法 | 现写法 | 帮助文本原文 |
|---|---|---|
| `yazi --clear-cache` | **`ya cache clear`** | "Clear the cache directory (deprecated, use `ya cache clear`)" |
| `yazi --debug` | **`ya env`** | "Print debug information (deprecated, use `ya env`)" |
| `ya pack -a <pkg>` | **`ya pkg add <pkg>`** | v25.5.28 起弃用 |

### 撰写指南时的措辞建议

- 一律写 `[mgr]` 而非 `[manager]`；一律 `ya pkg` 而非 `ya pack`。
- 提"清空预览缓存"时写 `ya cache clear`，并注明改 `max_width/max_height` 后必须执行。
- 插件清单以官方 19 个为"官方"口径，社区插件单独标注来源仓库与最低版本要求。
- 标注"本文基于 yazi v26.8.15"，并提示 `[manager]`/`ya pack`/`--clear-cache` 是旧版写法，便于读者自查旧资料。

---

## 8. 来源清单

**官方文档（均为 v26.8.15 对应版本页）**

- 配置总览：https://yazi-rs.github.io/docs/configuration/overview
- yazi.toml：https://yazi-rs.github.io/docs/configuration/yazi
- keymap.toml：https://yazi-rs.github.io/docs/configuration/keymap
- keymap [gait]：https://yazi-rs.github.io/docs/configuration/keymap-gait
- theme.toml：https://yazi-rs.github.io/docs/configuration/theme
- 插件概览：https://yazi-rs.github.io/docs/plugins/overview
- Flavor 概览：https://yazi-rs.github.io/docs/flavors/overview
- 图片预览：https://yazi-rs.github.io/docs/image-preview
- CLI（ya pkg 语法）：https://yazi-rs.github.io/docs/cli

**官方仓库**

- 插件（19 个官方插件与安装语法）：https://github.com/yazi-rs/plugins
- 主题（官方 flavor 清单）：https://github.com/yazi-rs/flavors
- CHANGELOG（v25.2.7 – v26.8.15 逐版本核对）：https://github.com/sxyazi/yazi/blob/main/CHANGELOG.md
- 默认 preset（默认值出处，`shipped` 分支）：https://raw.githubusercontent.com/sxyazi/yazi/shipped/yazi-config/preset/yazi-default.toml
- 社区书签插件（README 注明要求 v25.4.8+）：https://github.com/dedukun/bookmarks.yazi

**本机实测**

- yazi 26.8.15（Homebrew 2026-08-15），`ya pkg --help` / `ya cache --help` / `yazi --help` / `ya --help` 原始输出
- `~/.config/yazi/{yazi.toml, keymap.toml, package.toml, theme.toml}`（2026-08-26/31 落地的生产配置）与 `~/.config/yazi/plugins/smart-enter.yazi/` 目录结构
