# 工具-VSCode


## 快捷键


### 常用

* `Cmd + Shift + .`, 显示TOC， Breadcrumbs
* `Ctrl + Shift + Tab`, 快速打开最近使用的文件列表

* `Cmd + 0` 定位文件到目录
* `Cmd + Shift + K` 删除当前行
* `Cmd + X` 剪切当前行
* `Cmd + U` 光标恢复到上次位置
* `Cmd + D` 复制光标到附近的相同单词
* `Cmd + K + F/0~6` fold
* `Cmd + Shift + O` 搜索符号，添加`:`进行分类
* `Cmd + P` 打开最近浏览文件列表, 选中后可添加`Ctrl + G`到指定行号
* `Option + Shift + F` 格式化当前doc
* `Ctrl + J` 合并代码行
* `Ctrl` + ` 打开terminal.
* `Ctrl + Shift + T`  Re-open a Closed Editor
* `Ctrl + Shift + D`  重复行  not worked


## Tool

* CSS Peek
  * Peek or Jump to a CSS definition directly from HTML, just like in Brackets!
* Markdown All in One
  * All-in-one markdown plugin (keyboard shortcuts, table of contents, auto preview, list editing and more)
* [markdown-markmap](https://github.com/phoihos/vscode-markdown-markmap)
  * Markdown 思维导图预览支持，在 VS Code 内置的 Markdown 预览中将 Markdown 可视化为思维导图。支持使用 ```markmap 代码块创建思维导图，支持语法高亮、链接、样式、代码块、数学公式（Katex）等。可配置缩放和颜色属性。
* [markmap-vscode](https://github.com/markmap/markmap-vscode)
  * 官方 markmap VSCode 扩展，将 Markdown 文件转换为交互式思维导图。支持实时预览、分屏视图、导出为 HTML/PNG/SVG 等格式。使用 ```markmap 代码块或直接预览 Markdown 文件。基于 markmap-lib，支持折叠/展开分支、自定义主题。
* [vscode-markmap-universe](https://github.com/markmap-universe/vscode-markmap-universe)
  * markmap universe 扩展，提供增强的 markmap 功能和工具集合。扩展了官方 markmap 的能力，提供更多定制选项和生产力功能。
* [Markdown Preview Enhanced](https://github.com/shd101wyy/vscode-markdown-preview-enhanced)
  * 被誉为 "BEST" 的 Markdown 预览扩展之一。支持自动滚动同步、数学公式排版（MathJax）、Mermaid、PlantUML、Pandoc、PDF 导出、代码块执行、演示文稿编写等强大功能。快捷键：`cmd-k v` 侧边预览，`cmd-shift-v` 打开预览。
* Instant Markdown
* Bookmarks
  * mark and jump
* Paste JSON as Code
  - Interactively generate types and (de-)serialization code from JSON, JSON Schema, and TypeScript
  - Paste JSON/JSON Schema/TypeScript as code
* Todo Tree
  * This extension quickly searches (using ripgrep) your workspace for comment tags like TODO and FIXME, and displays them in a tree view in the explorer pane. Clicking a TODO within the tree will open the file and put the cursor on the line containing the TODO.
* Better Align
* Dash
* 掘金
  * ![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20210112081551.png)
* 韭菜盒子
  * ![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20210112081702.png)
* 前端盒子
  * ![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20210112081732.png)
* LeetCode
  * ![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20210112082248.png)

* [Reference Search View](https://marketplace.visualstudio.com/items?itemName=ms-vscode.references-view) 列出所有引用
* [Visual Studio IntelliCode](https://marketplace.visualstudio.com/items?itemName=VisualStudioExptTeam.vscodeintellicode) Smart Coding for TS plugin.

![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20200618172438.png)



## Flutter配置

--flavor

```dart
{
    "name": "Flutter",
    "request": "launch",
    "type": "flutter",
    "args": [
        "--flavor",
        "app1"
    ]
}
```


## Ref

* [awesome-vscode](https://viatsko.github.io/awesome-vscode/) 🎨 A curated list of delightful VS Code packages and resources.