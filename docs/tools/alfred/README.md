# Alfred

> 一个强大的 macOS 生产力工具，通过快速启动、文件搜索和工作流自动化提升效率

## 基本信息

| 项目 | 详情 |
|------|------|
| **官方网站** | [alfredapp.com](https://www.alfredapp.com/) |
| **价格** | 免费版 / Powerpack 付费版 |
| **适用平台** | macOS |
| **分类** | [效率工具](/docs/categories/productivity.md) / [启动器](#) |

## 简介

Alfred 是 Mac 上最强大的效率工具之一，它是一个功能强大的启动器，可以快速启动应用程序、搜索文件、执行系统命令等。通过其强大的工作流功能，可以极大地提高工作效率。

## 功能特点

- **快速启动**：瞬间启动应用、文件和搜索
- **文件导航**：快速查找和操作文件
- **剪贴板历史**：记录和管理剪贴板内容
- **工作流**：创建自动化任务和集成
- **自定义搜索**：创建自定义网络搜索
- **系统命令**：快速执行系统操作
- **扩展性强**：支持丰富的插件和主题

## 安装指南

### 系统要求
- macOS 10.12 或更高版本
- 推荐使用 Alfred Powerpack 以获得完整功能

### 安装步骤
1. 访问 [Alfred 官网](https://www.alfredapp.com/) 下载最新版本
2. 将 Alfred 拖拽到 Applications 文件夹
3. 启动 Alfred 并完成初始设置
4. (可选) 安装 Powerpack 解锁高级功能

### 快速开始
1. 设置热键：`⌘ + Space` (默认)
2. 开始输入应用名称或命令
3. 按 `↩` 执行操作

## 主要功能

### 1. 快速启动应用
- 使用 `⌘ + Space` 打开 Alfred
- 输入应用名称的前几个字母即可快速启动应用

### 2. 文件搜索
- 输入 `find` 或 `open` 加文件名进行搜索
- 使用 `in` 在特定文件夹中搜索

### 3. 计算器
- 直接输入数学表达式进行计算
- 支持单位转换（如 `10 USD to CNY`）

### 4. 剪贴板历史
- `⌘ + ⌥ + C` 打开剪贴板历史
- 支持查看和搜索历史剪贴板内容

### 5. 工作流（Workflows）
Alfred 最强大的功能之一，可以创建自动化工作流：
- 自定义搜索
- 系统命令
- 脚本执行
- API 集成

## 常用快捷键
| 功能 | 快捷键 |
|------|--------|
| 打开 Alfred | `⌘ + Space` |
| 打开文件搜索 | `⌘ + ⌥ + Space` |
| 打开剪贴板历史 | `⌘ + ⌥ + C` |
| 清空剪贴板历史 | `⌘ + ⌥ + ⌫` |

## 进阶使用

### 自定义搜索
1. 打开 Alfred 设置
2. 进入 Features > Web Search
3. 点击 "Add Custom Search"
4. 配置搜索 URL 和关键词

### 创建简单工作流
1. 打开 Alfred 设置 > Workflows
2. 点击 "+" 创建新工作流
3. 添加输入、处理和输出步骤
4. 保存并测试

## 常见问题

### 1. 如何重置 Alfred 设置？
```bash
defaults delete com.runningwithcrayons.alfred
```

### 2. 如何备份 Alfred 设置？
Alfred 的设置默认保存在 `~/Library/Application Support/Alfred` 目录下。

## 相关工具

### 集成推荐
- [Karabiner-Elements](../karabiner-elements/README.md) - 键盘自定义工具，可与 Alfred 配合使用
- [TextExpander](../textexpander/README.md) - 文本扩展工具，与 Alfred 的剪贴板功能互补
- [Things 3](../things3/README.md) - 任务管理工具，可通过 Alfred 快速添加任务

## 相关资源

### 官方资源
- [Alfred 官方文档](https://www.alfredapp.com/help/)
- [Alfred 工作流库](https://www.alfredworkflows.com/)
- [Alfred 论坛](https://www.alfredforum.com/)

### 学习资源
- [Alfred 使用技巧 - 少数派](https://sspai.com/tag/Alfred)
- [Alfred 工作流开发指南](https://www.alfredapp.com/help/workflows/)
- [Awesome Alfred Workflows](https://github.com/alfred-workflows/awesome-alfred-workflows)

## 许可证

Alfred 是 [Running with Crayons Ltd](https://www.alfredapp.com/) 的注册商标。

## 更新日志

### 5.0 (2023-09-01)
- 新增：工作流调试器
- 改进：更快的文件搜索
- 修复：多个稳定性问题

### 4.6 (2023-06-15)
- 新增：支持 macOS 13 Ventura
- 改进：剪贴板历史管理
- 优化：内存使用效率


