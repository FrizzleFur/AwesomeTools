# Yazi 快捷键体系调研底稿

> **调研基准**: yazi v26.8.15(Homebrew,2026-08-15 发布)| **调研日期**: 2026-09-01
> **信息来源**: 官方文档(quick-start / configuration/keymap)+ GitHub 官方仓库 `yazi-config/preset/keymap-default.toml`(v26.8.15 tag,与 main 分支 diff 确认完全一致)+ 本机 `~/.config/yazi/` 实测配置
> **用途**: 中文使用指南撰写底稿。数字统计口径见文末「附:统计口径」。

---

## 一、总览

Yazi 的快捷键按**上下文(context)分层**,共 9 个层,每层有独立键位表:

| 上下文层 | 默认键位数 | 说明 |
|---|---|---|
| `[mgr]` | 116 | 文件管理主界面(日常操作 95% 在此层) |
| `[tasks]` | 12 | 任务管理面板(w 唤出) |
| `[spot]` | 15 | 文件信息弹层(Tab 唤出) |
| `[pick]` | 10 | 选择列表弹窗(如多 opener 选择) |
| `[input]` | 68 | 输入框(重命名/新建/查找等,vim 风格编辑) |
| `[confirm]` | 12 | 确认对话框(如删除确认) |
| `[cmp]` | 11 | 自动补全组件(如 cd 路径补全) |
| `[help]` | 10 | 帮助菜单(~ 或 F1 唤出) |
| **合计** | **254** | — |

主界面(`[mgr]`)116 条键位按功能分为 9 组,下文逐一展开。

---

## 二、主界面快捷键分组(mgr 层,116 条)

### 1. 导航移动(约 22 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `k` / `↑` | 上移光标 | Vim 风格 |
| `j` / `↓` | 下移光标 | |
| `h` / `←` | 返回上级目录 | `leave` |
| `l` / `→` | 进入光标所在目录 | `enter`(仅目录;文件上默认无反应,见「本机定制」smart-enter) |
| `H` | 历史后退 | `back`,目录浏览历史 |
| `L` | 历史前进 | `forward` |
| `gg`(两键序列) | 跳到列表顶部 | `arrow top` |
| `G` / `<Home>`/`<End>` 组合 | 跳到底部 | `arrow bot` |
| `<C-u>` | 上翻半页 | `arrow -50%` |
| `<C-d>` | 下翻半页 | `arrow 50%` |
| `<C-b>` / `<PageUp>` | 上翻一页 | `arrow -100%` |
| `<C-f>` / `<PageDown>` | 下翻一页 | `arrow 100%` |
| `<S-PageUp>` / `<S-PageDown>` | 上/下翻半页 | 备用键 |
| `K` | 预览面板上滚 5 单位 | `seek -5`(滚动预览内容而非列表) |
| `J` | 预览面板下滚 5 单位 | `seek 5` |
| `z` | **fzf 跳转** | `plugin fzf`:按名字模糊跳到任意文件/目录(全盘) |
| `Z` | **zoxide 跳转** | `plugin zoxide`:按访问频率跳到目录 |
| `g⇒h` | 回到主目录 | `cd ~` |
| `g⇒c` | 跳到 `~/.config` | |
| `g⇒d` | 跳到 `~/Downloads` | |
| `g⇒t` | 跳到回收站 | `plugin trash` |
| `g⇒Space` | **交互式跳转** | `cd --interactive`:带补全的路径输入 |
| `g⇒f` | 跟随符号链接 | `follow` |

**实战场景 A — 大仓定位文件**: 忘了文件在哪,直接按 `z` 输入文件名片段(需安装 fzf),yazi 调 fzf 从全盘候选中模糊匹配并 cd 过去;日常目录往返用 `Z`(zoxide,按访问频次排序)。

**实战场景 B — 预览长文本**: 光标停在 README.md 上,右侧预览只显示开头;按 `J`/`K` 滚动预览内容,列表光标不动——`seek` 与 `arrow` 是两个独立维度。

### 2. 选择(6 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `<Space>` | 切换当前项选中态 | `toggle` + 光标下移一步,可连续按批量选 |
| `<C-a>` | 全选 | `toggle_all --state=on` |
| `<C-r>` | **反选全部** | `toggle_all`(含已选/未选互换) |
| `v` | 进入可视模式(选择模式) | `visual_mode`,类似 Vim 的行选 |
| `V` | 进入可视模式(**反选方向**) | `visual_mode --unset` |
| `<Esc>` | 退出可视模式 / 清空选择 / 取消搜索 | 通用退出键 |

**实战场景 — 可视模式批量选择**: 光标移到目标区间起点按 `v` 进入可视模式,`j`/`G` 移动到区间终点(移动过程中经过的文件全部进入选中态),然后直接按 `d` 删除或 `y` 复制。想排除某段则用 `V` 起步。

### 3. 文件操作(约 30 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `y` | 复制(yank)选中项 | `yank`,进入 yank 状态 |
| `x` | 剪切(yank --cut)选中项 | |
| `p` | 粘贴 | `paste` |
| `P` | 粘贴(目标存在则覆盖) | `paste --force` |
| `Y` / `X` | 取消 yank 状态 | `unyank` |
| `d` | **移入回收站** | `remove`(macOS/Windows 走系统回收站,Linux 走 FreeDesktop 规范) |
| `D` | **永久删除** | `remove --permanently`(有确认框) |
| `a` | 新建文件/目录 | `create`:输入名以 `/` 结尾即建目录 |
| `A` | **批量新建** | `bulk_create`(多行编辑) |
| `r` | 重命名 | `rename --cursor=before_ext`,光标默认停在扩展名前;多选时进入 **$EDITOR 批量重命名** |
| `;` | 运行 shell 命令 | `shell --interactive`,以 `%s` 占位选中项 |
| `:` | 运行 shell 命令(阻塞) | `shell --block --interactive`,直到命令结束才回 yazi |
| `-` | 建符号链接(绝对路径) | `link`,对 yank 中的文件操作 |
| `_` | 建符号链接(相对路径) | `link --relative` |
| `<C-->` | 建硬链接 | `hardlink` |
| `c⇒c` | 复制文件完整路径 | `copy path` |
| `c⇒C` | 复制文件 URL | `copy url` |
| `c⇒d` | 复制所在目录路径 | `copy dirpath` |
| `c⇒D` | 复制目录 URL | `copy dirurl` |
| `c⇒f` | 复制文件名 | `copy filename` |
| `c⇒n` | 复制不含扩展名的文件名 | `copy name_without_ext` |
| `m⇒s` / `m⇒p` / `m⇒b` / `m⇒m` / `m⇒o` / `m⇒n` | 切换列表行显示模式 | 大小 / 权限 / 出生时间 / 修改时间 / 所有者 / 无 |

**实战场景 A — 批量重命名流程**: 选中多个文件(可视模式或 Space 逐个)→ 按 `r` → yazi 调起 `$EDITOR`(如 Vim/VS Code)列出所有文件名 → 逐行改名、保存退出 → yazi 批量执行。比 shell 循环直观,且改坏可从任务面板看到失败项。

**实战场景 B — 复制路径进剪贴板**: 按 `cc` 拿绝对路径粘进终端/文档;按 `cf` 只拿文件名。写文档引用文件时高频使用。

**实战场景 C — 用 shell 加工选中项**: 选中 3 个图片文件,按 `;` 输入 `sips -Z 800 %s`(macOS 缩图),yazi 将选中路径替换进 `%s` 后台执行,`w` 面板看进度。

### 4. 打开与外部调用(4 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `o` | 按打开器规则打开选中项 | `open`,走 `yazi.toml` 的 `[open]` 规则链 |
| `O` | **交互式打开** | `open --interactive`:弹列表人工选择用哪个 opener |
| `<Enter>` | 打开选中项 | 与 `o` 同为 `open` |
| `<S-Enter>` | 交互式打开 | 与 `O` 同(部分终端不支持) |

**关键语义辨析**(新手最易混):
- `l` = **进入**目录(`enter`),只对目录生效,光标在文件上默认**无反应**;
- `o` / `<Enter>` = **打开**(`open`),目录则进入、文件则交给 opener 规则;
- 本机已用 smart-enter 插件把 `l` 增强为「目录则进入、文件则打开」,消除了这个心智负担(见第四节)。

**实战场景 — 临时换打开方式**: 默认规则把 `.md` 交给 VS Code,偶尔想用系统预览看一眼 → 按 `O` 从弹出的 opener 列表里选,无需改配置。本机 `yazi.toml` 中 `url="*"` 兜底规则使所有文本类文件默认进 VS Code,图片/PDF 进预览.app,压缩包走内置解压。

### 5. 搜索与过滤(7 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `/` | 增量查找(向后) | `find --smart`:输入子串,当前目录内高亮匹配并跳转 |
| `?` | 增量查找(向前) | `find --previous --smart` |
| `n` / `N` | 下一个/上一个匹配项 | `find_arrow`(复用上次查找词) |
| `f` | **实时过滤** | `filter --smart`:输入即过滤,列表只留匹配项;清空或再按恢复 |
| `s` | **按名搜索**(需 fd) | `search --via=fd`:递归子目录搜索,结果可交互跳转 |
| `S` | **按内容搜索**(需 ripgrep) | `search --via=rg`:全文搜索 |
| `<C-s>` | 取消进行中的搜索 | `escape --search` |

**三者辨析**: `/` 是「当前列表内定位」;`f` 是「当前列表实时筛选视图」;`s`/`S` 是「跨目录递归搜索」(异步,`w` 面板可看进度,找到后 `cd` 过去)。另有 `z`(fzf)承担「模糊跳任意路径」。

**实战场景 — 在当前目录筛出所有 .ts 文件**: 按 `f` 输入 `ts`,列表实时只剩匹配项,批量 Space 选中后 `y` 复制,再 `<Esc>` 清过滤粘贴到别处。跨目录找则按 `s`。

### 6. 视图控制(约 20 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `.` | **切换隐藏文件可见性** | `hidden toggle` |
| `<Tab>` | **弹出文件信息面板(spot)** | `spot`:展示文件元数据(大小/权限/mime/图片信息等),`<Tab>` 或 `<Esc>` 关闭 |
| `,⇒m` / `,⇒M` | 按修改时间排序 / 反向 | 排序同时切 linemode 到 mtime |
| `,⇒b` / `,⇒B` | 按出生时间排序 / 反向 | |
| `,⇒e` / `,⇒E` | 按扩展名排序 / 反向 | |
| `,⇒a` / `,⇒A` | 按字母序排序 / 反向 | |
| `,⇒n` / `,⇒N` | 按自然序排序 / 反向 | `foo2.jpg` 排在 `foo10.jpg` 前 |
| `,⇒s` / `,⇒S` | 按大小排序 / 反向 | 同时切 linemode 到 size |
| `,⇒r` | 随机排序 | |
| `m⇒*` 系列 | 行显示模式切换 | 见第 3 组(与排序联动) |

> 注: v26 系列中 `<Tab>` 已是 **spot 文件信息弹层**(quick-start 表述为 "Show the file information"),并非「预览切换」;预览面板始终显示在右侧,滚动用 `J`/`K`(见第 1 组 seek)。

**实战场景 — 找出目录里最占空间的文件**: 按 `,⇒S` 按大小降序 + linemode 自动切到 size 显示字节数,一眼定位;配合 `g⇒t` 还能进回收站清理。

### 7. 多标签页(约 16 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `t⇒t` | 在当前目录新建标签页 | `tab_create --current` |
| `t⇒r` | 重命名当前标签页 | `tab_rename --interactive` |
| `1` ~ `9` | 切换到第 N 个标签页 | `tab_switch N` |
| `[` / `]` | 上一个/下一个标签页 | 相对切换 |
| `{` / `}` | 与上/下一个标签页**交换位置** | `tab_swap` |
| `<C-c>` | 关闭当前标签页 | `close`:最后一个标签页则退出程序 |

**实战场景 — 双目录对拷**: `t⇒t` 开第二个标签切到目标目录,回到标签 1 选中文件 `y`,按 `]` 切到标签 2 按 `p` 粘贴。yank 状态跨标签页共享。

### 8. 任务管理(1 条入口)

| 按键 | 动作 | 说明 |
|---|---|---|
| `w` | 打开任务管理面板 | `tasks:show` |

面板内键位(`[tasks]` 层,12 条):`<Esc>`/`w`/`<C-c>` 关闭;`j`/`k` 移动;`<Enter>` 查看任务详情输出(inspect);`x` 取消任务。

**实战场景 — 后台复制大文件不阻塞**: `p` 粘贴 10GB 目录立即返回继续浏览(异步任务),按 `w` 查看进度,失败任务标红;按 `<Enter>` 看 stderr 定位原因,`x` 取消卡住的任务。

### 9. 帮助与退出(7 条)

| 按键 | 动作 | 说明 |
|---|---|---|
| `q` | 退出并回写 CWD | `quit`:配合 shell 包装函数 `y`,退出后 shell cd 到 yazi 所在目录 |
| `Q` | 退出且**不**回写 CWD | `quit --no-cwd-file` |
| `<C-c>` | 关闭当前标签页(最后一个则退出) | `close` |
| `<C-z>` | 挂起进程回 shell | `suspend`,做完事 `fg` 返回 |
| `~` / `<F1>` | 打开帮助菜单 | `help`:列出当前上下文全部键位,是最权威的随时可查手册 |
| `<Esc>` | 退出可视模式/清选择/取消搜索/关闭弹层 | 通用退出 |

**实战 — 忘记键位时**: 任何界面按 `~`,帮助菜单按上下文列出当前层全部键位与 desc;它读的就是 `keymap.toml` 的实际生效值,定制过的键也会如实显示。

---

## 三、其他上下文层键位概要

### `[spot]` 文件信息弹层(15 条)
`<Tab>`/`<Esc>` 关闭;`j`/`k` 滚动行;`h`/`l` **切换到上一个/下一个文件**(swipe,连续查看多个文件属性);`cc` 复制当前单元格内容;`~` 帮助。

### `[input]` 输入框(68 条)
完整的 Vim 风格行编辑器,是 yazi 键位数最多的一层:
- 模式: `i` 插入 / `a` 追加 / `v` 可视选择 / `r` 替换单字符 / `I` `A` 行首尾插入
- 移动: `h`/`l` 字符、`b`/`w`/`e` 词(大写为 WORD)、`0`/`$`/`^` 行首尾、`<C-a>`/`<C-e>` 
- 删除: `<Backspace>`/`<C-h>` 前删、`<C-d>`/`<Delete>` 后删、`d` 剪切选区、`D`/`C` 剪到行尾、`x` 删单字符
- 剪贴板: `y` 复制、`p`/`P` 粘贴、`<C-u>`/`<C-k>` 删到行首/尾、`<C-w>` 删前一个词
- 撤销: `u` 撤销、`<C-r>` 重做、`u`/`U` 在可视模式下转小写/大写
- 历史: `k`/`j` 或 `↑`/`↓` 或 `<C-p>`/`<C-n>` 翻输入历史

### `[confirm]` 确认框(12 条)
`y`/`<Enter>` 确认、`n`/`<Esc>`/`<C-c>` 取消、`j`/`k` 滚动长文本。

### `[pick]` 选项列表(10 条)
`<Enter>` 提交、`<Esc>`/`<C-c>` 取消、`j`/`k` 移动。(交互式打开 `O` 的 opener 选择即此层)

### `[cmp]` 补全(11 条)
`<Tab>` 接受补全、`<Enter>` 补全并提交、`<C-p>`/`<C-n>` 或 `<A-j>`/`<A-k>` 或 `↑`/`↓` 选项间移动。

---

## 四、键位机制:keymap.toml 覆盖语义

### 4.1 三个属性,三种优先级

每个上下文层(如 `[mgr]`)有且仅可用其一的三个属性:

| 属性 | 优先级 | 语义 |
|---|---|---|
| `prepend_keymap` | **高于**默认 | 插队到默认键位**之前**。yazi 取第一个匹配键执行,所以 prepend 能**覆盖**默认键 |
| (默认 `keymap`) | 中 | 不写用户配置时使用内置 preset |
| `append_keymap` | **低于**默认 | 追加到默认键位**之后**,只能新增键,不能覆盖 |
| `keymap = [...]` | **替换** | 直接覆盖该层**全部**默认键位,只保留自己写的(慎用,一般不需要) |

官方文档原文要点:*"Prepend inserts before the default keybindings, while append inserts after them. Since Yazi selects the first matching key to run, prepend always has a higher priority than default, and append always has a lower priority than default."*

> ⚠️ TOML 语法限制: 同一层内 `prepend_keymap = [...]` 与 `[[mgr.append_keymap]]` 两种写法**不能混用**(TOML 不允许对同一 key 先用内联表再用表数组)。要么全用 `[mgr] prepend_keymap = [...]` 风格,要么全用 `[[mgr.prepend_keymap]]` 风格。

### 4.2 配置文件位置与热加载

- 用户配置: `~/.config/yazi/keymap.toml`(Windows: `%AppData%\yazi\config\keymap.toml`)
- 内置默认: 仓库 `yazi-config/preset/keymap-default.toml`(每个用户键位表都是「用户 prepend/append + 内置 preset」合并后的结果)
- 修改保存后 **自动热加载**,无需重启

### 4.3 键位表示法(Key notation)

- 普通键: `a`-`z`、`A`-`Z`、`<Space>`、`<Enter>`、`<Tab>`、`<Esc>`、`<Backspace>`、`<Delete>`、方向键 `<Left>` `<Right>` `<Up>` `<Down>`、`<Home>` `<End>`、`<PageUp>` `<PageDown>`、`<F1>`-`<F19>`
- 修饰键前缀: `<S-…>` Shift、`<C-…>` Ctrl、`<A-…>` Alt/Meta、`<D-…>` Command/Win/Super
- 组合示例: `<C-a>` = Ctrl+a;`<C-S-b>` 或 `<C-B>` = Ctrl+Shift+b
- 序列键: `on` 写成数组即按键序列,如 `on = ["g", "g"]` = `gg`;单键即字符串 `on = "G"`
- 多动作: `run` 可以是数组,依次执行,如默认 `<Space>` 绑 `["toggle", "arrow 1"]`(选中并下移)
- 平台条件: 条目可加 `for = "unix" | "windows" | "macos" | "linux"`,同一键在不同平台绑不同动作
- 禁用某键: `run = "noop"`(数组形式 `run = ["noop"]` 亦可,但数组只能有一个元素且必须是 noop)
- **终端兼容性三个注意点**:
  1. `<D-…>` 需终端支持 CSI u 键盘协议;
  2. macOS 无 Alt 键,`<A-…>` 需在终端里把 Option 映射为 Alt;
  3. 传统键盘协议下 `<Tab>`≡`<C-i>`、`<Enter>`≡`<C-m>`,要区分需终端启用 CSI u。

### 4.4 官方推荐覆盖模式速查(节选自文档 tips)

- 覆盖 `g⇒d` 指向自己的目录: `[[mgr.prepend_keymap]]` + `on = ["g","d"]` + `run = "cd ~/dev"`
- 禁用 `g⇒c`: `run = "noop"`
- 自定义回收站命令(macOS 无原生 trash 时旧方案): `run = "shell -- trash-put %s"`(**v26 注意**: `shell` 命令参数已改用 `--` 分隔符写法 `shell -- trash-put %s`,旧文档的 `shell "trash-put %s"` 写法已废弃)

---

## 五、本机已有定制案例(可直接引用进指南)

**文件**: `~/.config/yazi/keymap.toml`(2026-08-26 配置)

```toml
[mgr]
prepend_keymap = [
  { on = "l",       run = "plugin smart-enter", desc = "进入目录或打开文件" },
  { on = "<Right>", run = "plugin smart-enter", desc = "进入目录或打开文件" },
]
```

**效果**: 光标在目录上按 `l` → 进入目录;在文件上按 `l` → 按 opener 规则打开(等价于 `o`)。

**原理与官方默认的对比**:
- 官方默认 `l` 只绑 `enter`(仅目录有效),文件上无反应;打开文件必须用 `o`/`<Enter>`
- smart-enter 是官方插件仓库 `yazi-rs/plugins` 中的 `smart-enter` 插件(本机 `package.toml` 记录: `use = "yazi-rs/plugins:smart-enter"`, rev `c591a36`),插件内部判断 hovered 项类型后分流执行 `enter` 或 `open`
- 用 **`prepend_keymap`** 覆盖默认 `l`——正是 4.1 节「prepend 高优先级覆盖默认键」的标准用法
- 大写 `L`(历史前进)保持默认未动

**配套定制**(同目录 `yazi.toml`,影响 `o`/`l` 打开行为): `[open] prepend_rules` 中 `url="*"` 万物兜底 → 除压缩包/音视频外一律交给 VS Code,图片/PDF 交预览.app。因此本机按 `l` 打开 `.md` 的实际效果是「VS Code 打开」。

**指南引用建议**: smart-enter 是「yazi 键位定制三件套(keymap.toml + 插件 + opener 规则)」的最佳示例——一个键的增强同时涉及 4.1 节的覆盖机制与打开器规则,适合作为定制章节的开篇案例。

---

## 六、版本时效标注(调研时点: 2026-09-01,基准 v26.8.15)

1. **`yazi --debug` 已废弃**: 本机实测输出提示 *"has been deprecated, use `ya env` instead"*。排查环境问题请用 `ya env`。(写指南时环境诊断章节用 `ya env`)
2. **`shell` 命令语法**: 官方 keymap 文档已将 `shell "cmd %s"` 写法标注为废弃,新写法 `shell -- cmd %s`(用 `--` 分隔)。
3. **`<Tab>` = spot 文件信息弹层**(非预览切换);v26 的预览常驻右侧,滚动用 `J`/`K`。
4. **Android 平台** `remove` 仅支持 `--permanently`(无回收站概念)——通用性说明,macOS 指南可忽略。
5. v26.8.15 tag 的 keymap-default.toml 与 GitHub main 分支**完全一致**(diff 验证),即文档所述键位即为当前最新稳定版行为,无版本漂移。
6. Yazi 迭代较快,指南成文时建议以 `~` 帮助菜单内实际值为最终裁决。

---

## 七、来源清单

| 来源 | URL | 用途 |
|---|---|---|
| 官方文档 Quick Start(键位总表) | https://yazi-rs.github.io/docs/quick-start/ | 分组框架、入门键位 |
| 官方文档 Configuration: Keymap | https://yazi-rs.github.io/docs/configuration/keymap/ | 覆盖机制、键位表示法、命令参数语义 |
| 官方仓库默认键位 preset | https://raw.githubusercontent.com/sxyazi/yazi/v26.8.15/yazi-config/preset/keymap-default.toml | 全部 254 条键位逐一核对(v26.8.15 tag) |
| 本机配置 | `~/.config/yazi/keymap.toml`、`package.toml`、`yazi.toml`;`yazi --version` | smart-enter 案例、opener 案例、版本确认 |

---

## 附: 统计口径

- 「默认键位数」= `keymap-default.toml`(v26.8.15)各上下文层 keymap 数组中 `on` 条目数(Python 解析统计): mgr 116 / tasks 12 / spot 15 / pick 10 / input 68 / confirm 12 / cmp 11 / help 10 = **254**。
- 分组表内「约 N 条」含同一动作的多键绑定(如 `k` 与 `↑` 记 2 条)与序列键(`gg` 记 1 条);分组数字之和略大于 116 是因为 `m⇒*`/`c⇒*`/`,⇒*` 序列键在不同分组视角下有交叉归类,撰写正式指南时以官方 `~` 帮助菜单展示为准。
