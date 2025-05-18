# Karabiner-Elements

## 简介
Karabiner-Elements 是一个强大的 macOS 键盘自定义工具，允许用户重新映射键盘按键、创建复杂的按键序列，以及为不同设备和应用设置不同的键盘配置。

## 安装
1. 访问 [Karabiner-Elements 官网](https://karabiner-elements.pqrs.org/) 下载最新版本
2. 打开下载的 .dmg 文件
3. 将 Karabiner-Elements 拖到 Applications 文件夹
4. 启动 Karabiner-Elements 并按照提示完成系统权限设置

## 基本配置

### 1. 简单按键映射
1. 打开 Karabiner-Elements
2. 切换到 "Simple Modifications" 标签页
3. 选择目标键盘设备
4. 在 "From key" 列选择要修改的按键
5. 在 "To key" 列选择目标按键

### 2. 常用按键映射示例
| 原按键 | 映射为 | 用途 |
|--------|--------|------|
| Caps Lock | Control | 将大写锁定键改为 Control 键 |
| Right Command | Right Option | 交换右侧 Command 和 Option 键 |
| Fn + Delete | Forward Delete | 实现 Windows 风格的删除键 |

## 高级功能

### 1. 复杂修改 (Complex Modifications)
1. 点击 "Complex Modifications" 标签页
2. 点击 "Add rule" 按钮
3. 选择 "Import more rules from the Internet" 下载更多规则
4. 或手动创建自定义规则

### 2. 常用复杂规则

#### 将右 Command + HJKL 映射为方向键
```json
{
  "title": "Right Command + HJKL to Arrows",
  "rules": [
    {
      "description": "Change right_command+h/j/k/l to arrow keys",
      "manipulators": [
        {
          "type": "basic",
          "from": {
            "key_code": "h",
            "modifiers": {
              "mandatory": ["right_command"]
            }
          },
          "to": [
            {
              "key_code": "left_arrow"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "j",
            "modifiers": {
              "mandatory": ["right_command"]
            }
          },
          "to": [
            {
              "key_code": "down_arrow"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "k",
            "modifiers": {
              "mandatory": ["right_command"]
            }
          },
          "to": [
            {
              "key_code": "up_arrow"
            }
          ]
        },
        {
          "type": "basic",
          "from": {
            "key_code": "l",
            "modifiers": {
              "mandatory": ["right_command"]
            }
          },
          "to": [
            {
              "key_code": "right_arrow"
            }
          ]
        }
      ]
    }
  ]
}
```

## 配置文件位置
Karabiner-Elements 的配置文件位于：
```bash
~/.config/karabiner/karabiner.json
```

## 常见问题

### 1. 修改不生效
1. 确保 Karabiner-Elements 正在运行
2. 检查菜单栏图标是否显示为正常状态
3. 在 "Devices" 标签页确认目标键盘已启用
4. 重启 Karabiner-Elements 服务

### 2. 系统更新后失效
macOS 系统更新后可能需要重新授权辅助功能权限：
1. 打开系统偏好设置 > 安全性与隐私 > 隐私
2. 选择辅助功能
3. 解锁设置
4. 勾选 Karabiner-Elements

## 实用技巧

### 1. 为不同应用设置不同配置
1. 在 "Complex Modifications" 中创建规则
2. 在规则中添加应用条件，例如：
```json
"conditions": [
  {
    "type": "frontmost_application_if",
    "bundle_identifiers": ["^com\.apple\.Terminal$"]
  }
]
```

### 2. 调试配置文件
```bash
# 验证配置文件语法
/Applications/Karabiner-Elements.app/Contents/Library/bin/karabiner_cli --lint

# 重新加载配置
/Applications/Karabiner-Elements.app/Contents/Library/bin/karabiner_cli --reload-configuration
```

## 相关资源
- [Karabiner-Elements 官方文档](https://karabiner-elements.pqrs.org/docs/)
- [Karabiner-Elements 复杂规则库](https://ke-complex-modifications.pqrs.org/)
- [Karabiner-Elements 配置示例](https://github.com/pqrs-org/KE-complex_modifications)

## 更新日志
- 2023-10-15: 初始文档创建
- 2023-10-16: 添加复杂规则示例和调试命令
