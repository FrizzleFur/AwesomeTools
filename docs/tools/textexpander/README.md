# TextExpander

## 简介
TextExpander 是一款强大的文本扩展工具，可以自动将缩写替换为常用的文本片段、代码块、图片等内容，大幅提高文本输入效率。

## 安装
1. 访问 [TextExpander 官网](https://textexpander.com/) 下载最新版本
2. 安装并启动 TextExpander
3. 登录您的账户（可选，用于同步）

## 基本使用

### 1. 创建文本片段
1. 点击菜单栏的 TextExpander 图标
2. 选择 "New Snippet"
3. 输入缩写和扩展内容
4. 设置触发方式（即时或按Tab键）

### 2. 常用片段类型
- 纯文本：简单的文本替换
- 富文本：包含格式的文本
- 图片：插入图片
- 脚本：执行 AppleScript 或 JavaScript
- 剪贴板：插入剪贴板内容

## 高级功能

### 1. 填表功能
使用 `%filltext` 占位符创建可填写的表单：
```
Dear %filltext:name=Name%, 
Thank you for your email about %filltext:name=Subject%.
```

### 2. 变量
使用变量插入动态内容：
- `%|%` - 光标位置
- `%clipboard%` - 剪贴板内容
- `%date%` - 当前日期
- `%time%` - 当前时间

### 3. 分组管理
- 创建不同的分组管理片段
- 使用嵌套子分组
- 为不同应用设置不同的分组

## 常用快捷键
| 功能 | 快捷键 |
|------|--------|
| 显示/隐藏主窗口 | `⌘ + ⌥ + T` |
| 快速输入 | `⌘ + ⌥ + V` |
| 编辑上一个片段 | `⌘ + ⌥ + E` |

## 常见问题

### 1. 中文输入法下无法触发
解决方法：
1. 打开 TextExpander 偏好设置
2. 进入 "Expansion" 标签页
3. 勾选 "Allow expansion within composed characters"

### 2. 同步问题
如果遇到同步问题，可以尝试：
1. 退出 TextExpander
2. 删除 `~/Library/Group Containers/7TPNXN7RE6.com.smileonmymac.textexpander/` 目录
3. 重新登录账户

## 实用技巧

### 1. 代码片段
```javascript
/**
 * %filltext:name=Function Name%
 * @description %filltext:name=Description%
 * @param {%filltext:name=Type%} %filltext:name=param%
 * @returns {%filltext:name=Return Type%}
 */
function %filltext:name=functionName%(%filltext:name=param%) {
    %|%
}
```

### 2. 邮件模板
```
Subject: %filltext:name=Subject%

Hi %filltext:name=Name%,

%|%

Best regards,
[Your Name]
```

## 相关资源
- [TextExpander 官方文档](https://textexpander.com/help/)
- [TextExpander 使用技巧 - 少数派](https://sspai.com/tag/TextExpander)
- [TextExpander 片段库](https://textexpander.com/snippets/)

## 更新日志
- 2023-10-15: 初始文档创建
- 2023-10-16: 添加代码片段和邮件模板示例
