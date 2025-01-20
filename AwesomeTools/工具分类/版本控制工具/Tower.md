# Tower

## 简介
Tower 是一个强大的Git图形界面工具，适用于macOS系统。它提供了直观的界面来管理Git仓库，简化了Git操作流程。

## 主要功能
- 可视化分支管理
- 提交历史查看
- 文件差异比较
- 合并冲突解决
- 远程仓库管理
- 支持Git Flow工作流

## 安装方法
1. 访问[Tower官网](https://www.git-tower.com/)下载安装包
2. 安装完成后启动Tower
3. 添加Git仓库进行管理

## 配置Diff工具
1. 创建配置文件 CompareTools.plist
2. 保存到路径：~/Library/Application Support/com.fournova.Tower3/CompareTools/
3. 配置文件内容：
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <dict>
        <key>ApplicationIdentifier</key>
        <string>com.madebysofa.Kaleidoscope</string>
        <key>ApplicationName</key>
        <string>Kaleidoscope</string>
        <key>DisplayName</key>
        <string>Kaleidoscope</string>
        <key>LaunchScript</key>
        <string>kaleidoscope.sh</string>
        <key>Identifier</key>
        <string>kaleidoscope</string>
        <key>SupportsMergeTool</key>
        <false/>
        <key>SupportsDiffChangeset</key>
        <true/>
    </dict>
</array>
</plist>
```

## 参考
[Tower官方文档](https://www.git-tower.com/help/mac/first-steps/get-started-with-tower)
