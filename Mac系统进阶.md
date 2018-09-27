# Mac Operation System 进阶

## 技巧

### 统计该目录下所有文件的占用

打开终端，键入`sudo du -sh *`，按下回车后系统就会自动统计该目录下所有文件的占用情况，一般等待一两分钟后就能得到结果了。

### 迁移助理

使用“迁移助理”将您的所有文稿、应用、用户帐户和设置从一台电脑拷贝到另一台新 Mac 上。
[如何将内容移至新 Mac - Apple 支持](https://support.apple.com/zh-cn/ht204350)
使用“迁移助理”将您的所有文稿、应用、用户帐户和设置从一台电脑拷贝到另一台新 Mac 上。
![](http://oc98nass3.bkt.clouddn.com/15305817383130.jpg)

###  隐藏dock栏的图标

方法一：

打开Finder，左侧选择应用程序，右键点击你想要隐藏的软件，显示包内容-Contents，编辑 Info.plist文件，在<dict></dict>之间加入以下参数：

```
<key>LSUIElement</key>
 <string>1</string>
 ```

![](oc98nass3.bkt.clouddn.com/15375172104519.jpg)

![](oc98nass3.bkt.clouddn.com/15375171990328.jpg)

方法二：

使用[GhostTile – 隐藏 Dock 中不想看见的图标 - 数码荔枝](https://www.lizhi.io/review/72551612)



## Mac快捷键

[Mac 键盘快捷键](https://support.apple.com/zh-cn/HT201236)

### 剪切、拷贝、粘贴和其他常用快捷键

|           快捷键           | 描述 |
| :-: | :-: |
| Command-X | **剪切**所选项并拷贝到剪贴板。 |
| Command-C | 将所选项**拷贝**到剪贴板。这同样适用于“访达”中的文件。
 |
| Command-V | 将剪贴板的内容**粘贴**到当前文稿或应用中。这同样适用于“访达”中的文件。 |
| Command-Z | **撤销**前一个命令。随后您可以按 Command-Shift-Z 来**重做**，从而反向执行撤销命令。在某些应用中，您可以撤销和重做多个命令。 |
| Command-A | **全选**各项。 |
| Command-F | **查找**文稿中的项目或打开“查找”窗口。 |
| Command-G | **再次查找**：查找之前所找到项目出现的下一个位置。要查找出现的上一个位置，请按 Command-Shift-G。 |
| Command-H | **隐藏**最前面的应用的窗口。要查看最前面的应用但隐藏所有其他应用，请按 Command-Option-H。 |
| Command-M | 将最前面的窗口**最小化**至“程序坞”。要最小化最前面的应用的所有窗口，请按 Command-Option-M。 |
| Command-N | **新建：**打开一个新文稿或窗口。 |
| Command-O | **打开**所选项，或打开一个对话框以选择要打开的文件。 |
| Command-P | **打印**当前文稿。 |
| Command-S | **存储**当前文稿。 |
| Command-W | **关闭**最前面的窗口。要关闭应用的所有窗口，请按下 Command-Option-W。 |
| Command-Q | **退出**应用。 |
| Option-Command-Esc | **强制退出**：选择要[强制退出](https://support.apple.com/zh-cn/HT201276)的应用。或者，按住 Command-Shift-Option-Esc 3 秒钟来仅强制最前面的应用退出。 |
| Command–空格键 | **“聚焦”**：显示或隐藏 [“聚焦”](https://support.apple.com/zh-cn/HT201744) 搜索栏。要从“访达”窗口执行“聚焦”搜索，请按 Command–Option–空格键。如果您[使用多个输入源](https://support.apple.com/kb/PH21564?locale=zh_CN)以便用不同的语言键入内容，这些快捷键会[更改输入源而非显示“聚焦”](https://support.apple.com/kb/PH21554?locale=zh_CN)。 |
| 空格键 | **快速查看**：使用[快速查看](https://support.apple.com/zh-cn/HT201067)来预览所选项。 |
| Command-Tab | **切换应用**：在打开的应用中切换到下一个最近使用的应用。 |
| Shift-Command-波浪号 (~) | **切换窗口**：切换到最前端应用中下一个最近使用的窗口。 |
| Shift-Command-3 | **屏幕快照**：拍摄整个屏幕的屏幕快照。[了解更多屏幕快照快捷键](https://support.apple.com/zh-cn/HT201361)。 |
| Command-逗号 (,) | **偏好设置**：打开最前面的应用的偏好设置。 |

### “访达”快捷键

|           快捷键           | 描述 |
| :-: | :-: |
| Command-D | 复制所选文件。 |
| Command-E | 推出所选磁盘或宗卷。 |
| Command-F | 在“访达”窗口中开始“聚焦”搜索。 |
| Command-I | 显示所选文件的“显示简介”窗口。 |
| Shift-Command-C | 打开“电脑”窗口。 |
| Shift-Command-D | 打开“桌面”文件夹。 |
| Shift-Command-F | 打开“我的所有文件”窗口。 |
| Shift-Command-G | 打开“前往文件夹”窗口。 |
| Shift-Command-H | 打开当前 macOS 用户帐户的个人文件夹。 |
| Shift-Command-I | 打开 [iCloud 云盘](https://support.apple.com/zh-cn/HT201104)。 |
| Shift-Command-K | 打开“网络”窗口。 |
| Option-Command-L | 打开“下载”文件夹。 |
| Shift-Command-O | 打开“文稿”文件夹。 |
| Shift-Command-R | 打开“隔空投送”窗口。 |
| Shift-Command-T | 将所选的“访达”项目添加到“程序坞”（OS X Mountain Lion 或更低版本） |
| Control-Shift-Command-T | 将所选的“访达”项目添加到“程序坞”（OS X Mavericks 或更高版本） |
| Shift-Command-U | 打开“实用工具”文件夹。 |
| Option-Command-D | 显示或隐藏 [“程序坞”](https://support.apple.com/zh-cn/HT201730)。即使您未在“访达”窗口中，这个快捷键通常也有效。 |
| Control-Command-T | 将所选项添加到边栏（OS X Mavericks 或更高版本）。 |
| Option-Command-P | 隐藏或显示“访达”窗口中的路径栏。 |
| Option-Command-S | 隐藏或显示“访达”窗口中的边栏。 |
| Command–斜线 (/) | 隐藏或显示“访达”窗口中的状态栏。 |
| Command-J | 显示“显示”选项。 |
| Command-K | 打开“连接服务器”窗口。 |
| Command-L | 为所选项制作替身。 |
| Command-N | 打开一个新的“访达”窗口。 |
| Shift-Command-N | 新建文件夹。 |
| Option-Command-N | 新建智能文件夹。 |
| Command-R | 显示所选替身的原始文件。 |
| Command-T | 在当前“访达”窗口中有单个标签页开着的状态下显示或隐藏标签页栏。 |
| Shift-Command-T | 显示或隐藏“访达”标签页。 |
| Option-Command-T | 在当前“访达”窗口中有单个标签页开着的状态下显示或隐藏工具栏。 |
| Option-Command-V | 移动：将剪贴板中的文件从原始位置移动到当前位置。 |
| Option-Command-Y | 显示所选文件的[快速查看](https://support.apple.com/zh-cn/HT201067)幻灯片显示。 |
| Command-Y | 使用“快速查看”预览所选文件。 |
| Command-1 | 以图标方式显示“访达”窗口中的项目。 |
| Command-2 | 以列表方式显示“访达”窗口中的项目。 |
| Command-3 | 以分栏方式显示“访达”窗口中的项目。  |
| Command-4 | 以封面流方式显示“访达”窗口中的项目。 |
| Command–左中括号 ([) | 前往上一文件夹。 |
| Command–右中括号 (]) | 前往下一文件夹。 |
| Command–上箭头 | 打开包含当前文件夹的文件夹。 |
| Command–Control–上箭头 | 在新窗口中打开包含当前文件夹的文件夹。 |
| Command–下箭头 | 打开所选项。 |
| Command–“调度中心” | 显示桌面。即使您未在“访达”窗口中，这个快捷键也有效。 |
| Command–调高亮度 | 开启或关闭[目标显示器模式](https://support.apple.com/zh-cn/HT204592)。 |
| Command–调低亮度 | 当 Mac 连接到多个显示器时打开或关闭显示器镜像功能。 |
| 右箭头 | 打开所选文件夹。这个快捷键仅在列表视图中有效。 |
| 左箭头 | 关闭所选文件夹。这个快捷键仅在列表视图中有效。 |
| Option-连按 | 在单独的窗口中打开文件夹，并关闭当前窗口。 |
| Command-连按 | 在单独的标签页或窗口中打开文件夹。 |
| Command-Delete | 将所选项移到废纸篓。 |
| Shift-Command-Delete | 清倒废纸篓。 |
| Option-Shift-Command-Delete | 清倒废纸篓而不显示确认对话框。 |
| Command-Y | 使用“快速查看”预览文件。 |
| Option–调高亮度 | 打开“显示器”偏好设置。这个快捷键可与任一亮度键搭配使用。 |
| Option–“调度中心” | 打开“调度中心”偏好设置。 |
| Option–调高音量 | 打开“声音”偏好设置。这个快捷键可与任一音量键搭配使用。 |
| _按住 Command 键拖移_ | 将拖移的项目移到其他宗卷或位置。拖移项目时指针会随之变化。 |
| _按住 Option 键拖移_ | 拷贝拖移的项目。拖移项目时指针会随之变化。 |
| _按住 Option-Command 键拖移_ | 为拖移的项目制作替身。拖移项目时指针会随之变化。 |
| _按住 Option 键点按开合三角_ | 打开所选文件夹内的所有文件夹。这个快捷键仅在列表视图中有效。 |
| _按住 Command 键点按窗口标题_ |

## Xcode

### Xcode链接iphone一直闪断

![](http://oc98nass3.bkt.clouddn.com/15326666022413.jpg)
![](http://oc98nass3.bkt.clouddn.com/15326666332024.jpg)

发现一个Xcode链接iphone一直闪断的问题，提示说软件下载更新才能连接，但是下载失败，还以为是数据线接触不良或者是Xcode版本不支持，后来发现开启省电模式就可以了。
[A software update is required to connect to your iOS device / iPhone - Ask Different](https://apple.stackexchange.com/questions/327310/a-software-update-is-required-to-connect-to-your-ios-device-iphone)

```
The problem can be fixed by installing XCode beta.
This error occurs when the version of macOS (and iTunes) running on the computer is not compatible with the version of iOS on the device you're trying to connect.

Normally, updating the macOS to its current version will solve the problem. However, this won't work if the iOS device is running a newer beta version, and the Mac is not.
```


#### 关于使用Clang(LLVM)将OC文件转为C/C++文件报错的问题

```objc

main.m:9:9: fatal error: 'UIKit/UIKit.h' file not found
#import <UIKit/UIKit.h>
    ^
1 error generated.
```

```objc
clang -x objective-c -rewrite-objc -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk xxx.m

//__weak修饰变量，需要告知编译器使用ARC环境及版本号否则会报错，添加说明
-fobjc-arc -fobjc-runtime=ios-8.0.0

xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc -fobjc-arc -fobjc-runtime=ios-8.0.0 main.m
```

### 下载软件

* Valley [![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://www.appvalley.vip/#) 
* tweakbox [![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://www.tweakboxapp.com/)
* panda helper [![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](http://m.pandahelp.vip/regular)
3. Pin。Pin里面是有Valley，它可以下载接近2000多个APP。有付费软件，付费游戏，破解版的社交平台软件和游戏。内容简单，没有广告，不过不能自定义搜索，只能自己一个个翻。而且是英文界面，你必须得找到你所要的软件的英文名字。
3款软件版界面都比网页版简洁，但是前两款有广告。前两个已经介绍过了所以直接就介绍panda helper这款。

4. 网页内安装下载
[![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://next.tweakboxapp.com/) 这个软件类似Valley。他里面的软件跟Valley差不多，也是2000来个，进入网页后，找到APPS这个选项，点一下就进入APP软件的里面了，然后找到 tweaked APPs这个是搜索软件，因为是英文界面，你需要找到你所要下载的软件的英文名字。你也可以在Appstore Apps里面找软件，基本上Valley差不多的软件。网页版无广告，等下介绍软件版
```
Valley jse://run?file=APPValley.js 
```

6. workflow规则
[![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://workflow.is/workflows/5b681575dd944fca911d697d651cfadd)
里面包含了上面网页安装方法的3款软件

参考[攻略教程之免费下载付费软件](https://m.weibo.cn/status/4180725890666373?)


### Safari问题

* 设置Safari默认搜索为baidu

发现以前设置的地区是米国，所以在iOS的Safari搜索引擎设置中没有找到baidu.
切换回中国🇨🇳就可以了。
![](http://oc98nass3.bkt.clouddn.com/15308987115979.jpg)

* Safari的阅读模式

发现Safari的阅读模式每次都自动进入，发现是长按可以唤起菜单设置的。
![](http://oc98nass3.bkt.clouddn.com/15308987360120.jpg)


# 常见问题



##  Mac：解决修改用户名导致的管理员丢失


MAC OS怎样将普通成员改为管理员？
1、先按住command+s，再按开机键。

2、需先登录进系统，才能输入终端命令。

```
/sbin/mount -uaw 
rm var/db/.applesetupdone 
reboot 
```
![](oc98nass3.bkt.clouddn.com/15380565196686.jpg)

* reboot完成后，创建一个新的用户，按照提示操作。
* 新用户创建后，打开系统偏好设置-用户与群组
* 点击原来的普通用户，右侧有个“允许用户管理这台电脑”，打勾
* 然后重启。
* 这样就可以以管理员的身份登录到你原来的系统，再把刚新创建的管理员账户删除就可以了。

### 正确修改MAC用户名
1.选择用户与群组

![](https://img-blog.csdn.net/20171115150546465?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3VqYWtm/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center) 

2.把锁打开

![](https://img-blog.csdn.net/20171115150902713?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3VqYWtm/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center) 

3.添加一个管理员账号，1.点击加号 2.账号选择管理员 3.创建用户

![](https://img-blog.csdn.net/20171115151132221?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3VqYWtm/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center) 

4.退出登录  然后选择你刚才添加的管理员账号再来到用户与群组的界面

![](https://img-blog.csdn.net/20171115151306805?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3VqYWtm/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center) 

5.鼠标右键，选择高级选项。

![](https://img-blog.csdn.net/20171115151605005?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3VqYWtm/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center) 

6.然后修改，再切换账户就可以了

![](https://img-blog.csdn.net/20171115151922142?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvd3VqYWtm/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center) 


## 参考

1. [Mac：解决修改用户名导致的管理员丢失](https://www.jianshu.com/p/4e96a1b4d12d)
2. [MAC OS怎样将普通成员改为管理员？ - 知乎](https://www.zhihu.com/question/30071627)
3. [Mac电脑修改用户名丢失管理员权限问题修复 - CSDN博客](https://blog.csdn.net/wujakf/article/details/78539329)
4. [正确修改MAC用户名 - CSDN博客](https://blog.csdn.net/wujakf/article/details/78540794)


##  终端 命令行中文件路径有空格怎么办？

如： 
```
sudo rm -rf "/Library/Input Methods/Squirrel.app" 
```
加上双引号就行


## “XXX.app”已损坏，打不开。 您应该将它移到废纸篓

1. 在Mac电脑安装App提示App已损坏”xxxx已损坏，打不开。您应该推出磁盘映像”解决办法解决方案

方法：打开电脑的系统偏好设置-->安全与隐私，如图下如果没有第三项“任何来源”这个选项，就要打开终端运行：`sudo spctl --master-disable` ，重新进入"安全与隐私"就会出现打开的选项

![](http://oc98nass3.bkt.clouddn.com/15161963030407.jpg)
```
//先禁止
sudo spctl --master-disable
//后恢复
sudo spctl --master-enable
```

## Snap和Chrome的标签问题

`2018-03-14`在升级`MacOS high sierra`后,很多老的软件出现问题，今天出现之前安装的`Chrome`在使用snap切换的时候，每次会出新的tap页，因为我在mac上分了多个deskTop，这样每次来回切换`Chrome`的时候就会弹出很多的tab,增加了`Chrome`的内存消耗，还非常不方便，我还以为是snap的问题，后面想升级下`Chrome`，最后发现**把`Chrome`从Dock中移除并退出重新打开**，这种问题就解决了。可能是MacOS的问题吧。

## Github Desktop问题

本来我是不想把`Github Desktop`加进来的，没想到它今天抽了一个错误，为了记录一下我还是写一下。

报的错误：
![](http://oc98nass3.bkt.clouddn.com/15303368203935.jpg)

估计是钥匙串的访问权限问题
找到一篇文章：[GitHub Desktop was unable to store the account token in the keychain · Issue #4614 · desktop/desktop](https://github.com/desktop/desktop/issues/4614)
![](http://oc98nass3.bkt.clouddn.com/15303369966352.jpg)
参考[desktop/known-issues.md at master · desktop/desktop](desktop/known-issues.md at master · desktop/desktop)

## MicroSoft Word 弹窗问题

在Mac上使用word过程中，有时候经常出现这种弹窗:

![](http://oc98nass3.bkt.clouddn.com/15294901445351.jpg)
![](http://oc98nass3.bkt.clouddn.com/15294901483362.jpg)

这是模板的问题，在设置中找到模板文件路径

![](http://oc98nass3.bkt.clouddn.com/15294900549396.jpg)

![](http://oc98nass3.bkt.clouddn.com/15294900170729.jpg)

删除这个文件，然后重启Word,这个文件会重新生成。（估计模板文件出了问题）

参考[Word 无法打开现有共用模板 (Normal.dotm)](https://bbs.feng.com/read-htm-tid-10206026.html)



## 参考

1. [MAC 如何隐藏dock栏上你不想看见的图标 - CSDN博客](https://blog.csdn.net/FungLeo/article/details/52262315)