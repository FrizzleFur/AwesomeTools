## Xcode进阶

### 代码段 Snippet

* My Frame

```objc

frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);
```
![](https://oc98nass3.bkt.clouddn.com/15376704555901.jpg)


* My Lines Remark

```objc

/**
 * <#remark#>
 *
 * @param <#param#>
 */

```

![](oc98nass3.bkt.clouddn.com/15376705248064.jpg)

* My Property

```objc
property (nonatomic, <#type#>) <#className#> *propertyName;/**< <#remark#> */

```

****

![](oc98nass3.bkt.clouddn.com/15376705349709.jpg)

* My Remark

```
/** <#remark#> */

```

![](oc98nass3.bkt.clouddn.com/15376706918514.jpg)


### 快速记录问题

* 使用`#warning `来定义问题，或者todo, fixme等
* 使用`Cmd + 5`切换到issue模板
* `Cmd + Option + J`跳转到fiter过滤，输入`user-defined`就可以查看到

### 快捷键

![](http://oc98nass3.bkt.clouddn.com/15376702477628.jpg)

![](oc98nass3.bkt.clouddn.com/15376702826707.jpg)
![](oc98nass3.bkt.clouddn.com/15376703183349.jpg)

* 显示注释 `Cmd + Option + /`
* 
#### 1. Open Quickly

相信大家都熟悉 `⌘ + ⌥ + O` ，但是你知道怎么在辅助编辑器中打开吗？按住`Alt + Enter`， enjoy~

#### 2. 交换上下行代码：  `⌘ + ⌥ + [` or `⌘ + ⌥ + ]`

#### 3. To jump to the definition. 光标所在处`⌘ + ⌃ + J`
或者在辅助编辑器中打开

#### 4.切换多个编辑器焦点：

 `⌘ + J`
 
#### 5. 文件切换

* ⌃+1 - Related items menu that shows files related to what you are currently working on
* ⌃+2 - Previous and next buttons to navigate 
between your most recent files
The rest of the jump bar consists of heierarchial navigation with each level given a separate shortcut.
* ⌃+4 - Project level navigation
* ⌃+5 - Switch between header and implementation files
* ⌃+6 - Navigation within a file   

#### 6. 在辅助编辑器中跳转到变量的定义： `⌘ + Alt` + 鼠标点击对应变量名
     
#### 7. 在点击文件名时候，按住`Alt`将让文件在辅助编辑器中打开

#### 8. 在光标位置显示Help: `⌃ + ⌘ + ⇧ + /`

#### 9. Filter in Navigator  
本来热键是`⌘ + ⌥ + J`,发现貌似不起作用，就改成`⌘ + ⌥ + O`


## Xcode插件

### 插件路径


```
 ~/Library/Application\ Support/Developer/Shared/Xcode/Plug-ins/
```

### 常用插件

1. 自动补全 [HHEnumeration-Xcode ](https://github.com/youssman/awesome-xcode-plugins)
[molon/MLAutoReplace: Xcode plugin which help you write code faster.](https://github.com/molon/MLAutoReplace)
2. XAlign
![](https://i.loli.net/2018/10/21/5bcc92d432f92.jpg)

3. [pdcgomes/XCActionBar: "Alfred for Xcode" plugin](https://github.com/pdcgomes/XCActionBar)
![](https://i.loli.net/2018/10/21/5bcc934e71953.gif)

4. [trawor/XToDo: Xcode plugin to collect and list the `TODO`,`FIXME`,`???`,`!!!!`](https://github.com/trawor/XToDo)



### XCode9 安装 alcatraz

XCode8以后，Apple修改了XCode插件签名规则，要使用alcatraz需要update_xcode_plugins进行一次unsign操作。

步骤如下：

#### alcatraz

1.  删除alcatraz

```
rm -rf ~/Library/Application\ Support/Developer/Shared/Xcode/Plug-ins/Alcatraz.xcplugin
rm -rf ~/Library/Application\ Support/Alcatraz/

```

1.  安装alcatraz

```
curl -fsSL https://raw.github.com/supermarin/Alcatraz/master/Scripts/install.sh | sh

```

#### update_xcode_plugins

```
sudo gem install -n /usr/local/bin update_xcode_plugins

```

```
 update_xcode_plugins

```

```
update_xcode_plugins --unsign

```

遇到y/n，选择y

```
update_xcode_plugins --install-launch-agent

```
提示是否加载plugin，选择load bundles
提示签名，输入系统密码即可。
正常的话，能够看到package manager了



## Xcode辅助工具


* [youssman/awesome-xcode-plugins: Awesome Xcode plugins to rocket your productivity :)](https://github.com/youssman/awesome-xcode-plugins)
* [List of 8 Best Xcode Developer Tools (2018 Edition)](https://www.flexihub.com/xcode-developer-tools/)

1. XcodeWay
XcodeWay
This Xcode source editor extension offers easy access to a number of places you may need for your project. The tool provides you with an additional menu in Xcode and lets you go to various locations, which is extremely helpful during Xcode app development. For example, you can open Finder to the Project folder, Provisioning Profiles, DeviceSupport, CodeSnippets Folder, Themes, and more. Also, it will help you easily check and open GitHub page for the project repository in your default browser. And if, while working on a file, you find that any destination is missing, you can add it and submit a pull request.

2. FlexiHub
FlexiHub is an efficient software solution designed to redirect iOS devices over the network. This reliable app will become a great addition to Xcode iOS development tools allowing accessing iPhones, iPads, or iPods from any network computer, which makes it possible to test and debug iOS apps remotely. FlexiHub is able to virtualize USB devices and forward them across LAN, Ethernet, WIFi, or the Internet quickly and securely.

FlexiHub	
FlexiHub 
Windows, macOS, Linux, Android 
4.8 Rank based on 78+ users
Sign up for a free FlexiHub account below. Test the app for free for 7 days.

 FlexiHub
3. PlayAlways

PlayAlways is one of Xcode development tools that allows creating iOS or macOS Swift playgrounds. Thanks to this menubar app, you’ll be able to create iOS, macOS or tvOS playgrounds with nothing more than a couple of clicks or keyboard shortcut just after you have specified the path of where you want to save them. The solution also comes with Xcode extension which helps create a playground from Swift code that you've currently selected. This significantly simplifies testing your ideas in Swift before using them in your projects.

4. Import

It’s not uncommon that developers need to add an import module but scrolling up seems to be just a waste of time. In this case, a good idea will be to use Import - a simple Xcode source editor extension. This tool will help you in your Xcode app development by offering you a simple keyboard shortcut and menu item to move any import from a selected line to the required position at your file’s top.

5. Injection
Injection


[iOS 自定义代码段模板（CodeSnippets）和文件模板 (.xctemplate) - 简书 - iOS - 掘金](https://juejin.im/entry/58bed7f3570c3500622f9401#2.%E8%87%AA%E5%AE%9A%E4%B9%89%E6%96%87%E4%BB%B6%E6%A8%A1%E6%9D%BF)



### iOS代码自动化工具

[liubobo/automation: code generator](https://github.com/liubobo/automation)


### 代码片段

`code snippets`坐标位于Xcode整个界面的右下角,也可以通过快捷键`cmd + ctrl + opt + 2`调用.

#### OC

#### Swift

[burczyk/XcodeSwiftSnippets: Swift 4 code snippets for Xcode](https://github.com/burczyk/XcodeSwiftSnippets)


## 问题

### Xcode链接iphone一直闪断

![](http://oc98nass3.bkt.clouddn.com/15326666022413.jpg)
![](http://oc98nass3.bkt.clouddn.com/15326666332024.jpg)

发现一个Xcode链接iphone一直闪断的问题，提示说软件下载更新才能连接，但是下载失败，还以为是数据线接触不良或者是Xcode版本不支持，后来发现开启省电模式就可以了。
[A software update is required to connect to your iOS device / iPhone - Ask Different](https://apple.stackexchange.com/questions/327310/a-software-update-is-required-to-connect-to-your-ios-device-iphone)

The problem can be fixed by installing XCode beta.
This error occurs when the version of macOS (and iTunes) running on the computer is not compatible with the version of iOS on the device you're trying to connect.

Normally, updating the macOS to its current version will solve the problem. However, this won't work if the iOS device is running a newer beta version, and the Mac is not.


## 关于使用Clang(LLVM)将OC文件转为C/C++文件报错的问题

> main.m:9:9: fatal error: 'UIKit/UIKit.h' file not found
> #import <UIKit/UIKit.h>

> 1 error generated.

> clang -x objective-c -rewrite-objc -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk xxx.m

> //__weak修饰变量，需要告知编译器使用ARC环境及版本号否则会报错，添加说明
> -fobjc-arc -fobjc-runtime=ios-8.0.0

> xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc -fobjc-arc -fobjc-runtime=ios-8.0.0 main.m


⌘⌥⌃+J.


## xcode 10, Command CodeSign failed with a nonzero exit code

[ios - xcode 10, Command CodeSign failed with a nonzero exit code - Stack Overflow](ios - xcode 10, Command CodeSign failed with a nonzero exit code - Stack Overflow)
```
Open keychain access.
Lock the 'login' keychain.
Unlock it, enter your PC account password.
Clean and Build project

```

## xcode 打开工程就崩溃意外退出

有时候因为个人项目配置问题，打开就崩溃

第一步 找到工程文件

![](https://i.loli.net/2018/11/22/5bf631023dab8.jpg)

第二步，找到project.xcworkspace文件

![](https://i.loli.net/2018/11/22/5bf631062e62b.jpg)

第三步： 删除xcuserdata文件夹中的一些个人配置

![](https://i.loli.net/2018/11/22/5bf631a652170.jpg)

我这边是打开了很多tab崩溃，删除的是`UserInterfaceState.xcuserstate`即可
![](https://i.loli.net/2018/11/22/5bf631f369dc2.jpg)

##  xcode启动模拟器无限等待中

[iOS 11][Xcode 9] launch, install, start hangs Simulator #209

```
Due to quirks (most likely Simulator bugs) in the Simulator launching on both Xcode 8 and 9, there is no common code to have it launch successfully on both Xcodes. Through experimenting, I have found these to be most reliable:

Xcode 9:

killall Simulator
xcrun simctl boot <device_id>
open `xcode-select -p`/Applications/Simulator.app
Xcode 8:

killall Simulator
xcrun simctl shutdown booted
xcrun instruments -w <device_id>

```

[[iOS 11][Xcode 9] launch, install, start hangs Simulator · Issue #209 · ios-control/ios-sim](https://github.com/ios-control/ios-sim/issues/209)


## 多个项目切换快捷键

`Cmd + ~`

##  Xcode 编辑iOS版本支持

1. [iOS-DeviceSupport](https://github.com/iGhibli/iOS-DeviceSupport)
2. [Yatko/iOS-device-support-files: iOS 12 not supported by Xcode 9.4 : Could not locate device support files](https://github.com/Yatko/iOS-device-support-files)

## 参考

1. [Injection：iOS热重载背后的黑魔法 - iOS - 掘金](https://juejin.im/entry/5b1f4c5f5188257d7c35e9d9)