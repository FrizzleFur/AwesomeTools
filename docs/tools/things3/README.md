# Things 3

## 简介
Things 3 是一款优雅而强大的任务管理应用，专为 macOS 和 iOS 设计。它采用 GTD (Getting Things Done) 方法，帮助用户高效管理任务和项目。

## 安装
1. 从 Mac App Store 或 [Things 官网](https://culturedcode.com/things/) 下载
2. 安装并启动应用
3. 创建免费账户或登录现有账户（用于多设备同步）

## 核心概念

### 1. 收件箱 (Inbox)
- 收集所有新任务的地方
- 快速添加任务，稍后整理
- 使用 `⌘ + N` 快速添加任务

### 2. 项目 (Projects)
- 组织相关任务的容器
- 支持顺序或并行任务
- 可以设置项目截止日期和备注

### 3. 区域 (Areas)
- 组织项目的分类
- 例如：工作、个人、学习等
- 帮助保持任务分类清晰

### 4. 标签 (Tags)
- 为任务添加自定义标签
- 支持多标签
- 可以按标签筛选任务

## 常用快捷键

### 创建新项目
| 操作 | 快捷键 |
|------|--------|
| 新建待办事项 | `⌘ + N` |
| 新建项目 | `⌘ + ⌥ + N` |
| 快速添加 | `Ctrl + Space` |
| 快速添加（自动填充） | `⌥ + Ctrl + Space` |

### 编辑项目
| 操作 | 快捷键 |
|------|--------|
| 保存并关闭 | `⌘ + ↩` 或 `Esc` |
| 复制项目 | `⌘ + D` |
| 标记为完成 | `⌘ + .` |
| 取消完成 | `⌘ + ⌥ + .` |
| 删除 | `Delete` |
| 移动到日志 | `⌘ + ⌥ + L` |

### 导航
| 操作 | 快捷键 |
|------|--------|
| 收件箱 | `⌘ + 1` |
| 今天 | `⌘ + 2` |
| 计划 | `⌘ + 3` |
| 随时 | `⌘ + 4` |
| 某天 | `⌘ + 5` |
| 日志 | `⌘ + 6` |
| 显示在列表中 | `⌘ + ⌥ + L` |

## 高级功能

### 1. 快速添加
1. 使用 `Ctrl + Space` 打开快速添加
2. 输入任务名称
3. 使用 `#` 添加项目，`@` 添加标签，`!` 设置优先级
4. 按 `Enter` 保存

### 2. 重复任务
1. 创建任务时，点击日历图标
2. 选择"重复"
3. 设置重复频率（每天、每周、每月等）
4. 设置结束条件（如有需要）

### 3. 任务模板
1. 创建包含占位符的任务
2. 使用 `%` 标记占位符，如：`给 %name% 发邮件`
3. 复制任务时，系统会提示输入占位符的值

## 实用技巧

### 1. 邮件到 Things
1. 转发邮件到您的 Things 邮箱地址
2. 邮件主题将成为任务标题
3. 邮件正文将作为任务备注
4. 在 Things 设置 > Things Cloud > Mail to Things 中查找您的个人邮箱地址

### 2. URL Scheme
Things 3 支持 URL Scheme，可以从其他应用快速添加任务：
```
things:///add?title=任务标题&notes=任务备注&when=today
```

### 3. 与日历集成
1. 在 Things 设置 > 日历事件中启用"显示日历事件"
2. 选择要显示的日历
3. 日历事件将显示在"今天"和"计划"视图中

## 常见问题

### 1. 如何备份数据？
Things 3 使用 iCloud 自动同步数据。要手动备份：
1. 退出 Things 3
2. 备份 `~/Library/Group Containers/JLMPQHK86H.com.culturedcode.ThingsMac/` 目录

### 2. 如何迁移到新 Mac？
1. 在新 Mac 上安装 Things 3
2. 使用相同的 Apple ID 登录
3. 数据将通过 iCloud 自动同步

## 相关资源
- [Things 3 官方帮助](https://support.culturedcode.com/customer/en/portal/topics/939118-things-3/)
- [Things 3 快捷键参考](https://support.culturedcode.com/customer/en/portal/articles/2803569-things-for-mac-keyboard-shortcuts)
- [Things 3 使用技巧 - 少数派](https://sspai.com/tag/Things3)

## 更新日志
- 2023-10-15: 初始文档创建
- 2023-10-16: 添加快捷键和高级功能说明
