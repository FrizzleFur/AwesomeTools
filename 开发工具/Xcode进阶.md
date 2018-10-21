## Xcode进阶



### 快速记录问题

* 使用`#warning `来定义问题，或者todo, fixme等
* 使用`Cmd + 5`切换到issue模板
* `Cmd + Option + J`跳转到fiter过滤，输入`user-defined`就可以查看到


### 快捷键

![](oc98nass3.bkt.clouddn.com/15376702477628.jpg)

![](oc98nass3.bkt.clouddn.com/15376702826707.jpg)
![](oc98nass3.bkt.clouddn.com/15376703183349.jpg)

* 显示注释 `Cmd + Option + /`


### Code Snippet

* My Frame
```objc
frame = CGRectMake(<#CGFloat x#>, <#CGFloat y#>, <#CGFloat width#>, <#CGFloat height#>);
```
![](oc98nass3.bkt.clouddn.com/15376704555901.jpg)


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
![](oc98nass3.bkt.clouddn.com/15376705349709.jpg)


* My Remark

```objc
/** <#remark#> */
```

![](oc98nass3.bkt.clouddn.com/15376706918514.jpg)


## 插件


1. 自动补全 [HHEnumeration-Xcode ](https://github.com/youssman/awesome-xcode-plugins)
[molon/MLAutoReplace: Xcode plugin which help you write code faster.](https://github.com/molon/MLAutoReplace)
2. XAlign
![](https://i.loli.net/2018/10/21/5bcc92d432f92.jpg)

3. [pdcgomes/XCActionBar: "Alfred for Xcode" plugin](https://github.com/pdcgomes/XCActionBar)
![](https://i.loli.net/2018/10/21/5bcc934e71953.gif)

4. [trawor/XToDo: Xcode plugin to collect and list the `TODO`,`FIXME`,`???`,`!!!!`](https://github.com/trawor/XToDo)



## Xocde辅助工具


[List of 8 Best Xcode Developer Tools (2018 Edition)](https://www.flexihub.com/xcode-developer-tools/)

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


## 自动化

[liubobo/automation: code generator](https://github.com/liubobo/automation)