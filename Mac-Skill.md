### 在`Dock`中隐藏`App`图标

1.右击程序显示包内容。
　　2.在 Contents 文件夹中找到 Info.plist 文件，使用 plist 编辑器打开。
　　3.添加 Application is agent (UIElement) 项，Boolean 值为 Yes。
　　现在程序的图标和菜单就隐藏了，想要恢复请修改回NO。
![](http://oc98nass3.bkt.clouddn.com/2017-08-05-15019044682754.jpg)

参考[MAC系统中如何隐藏Dock上的程序图标_苹果MAC_操作系统_脚本之家](http://www.jb51.net/os/MAC/170274.html)




