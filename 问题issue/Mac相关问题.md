
## 桌面图片不显示


desktop文件夹里有东西，但是桌面不显示，而且无法拖动任何文件到桌面。 苹果官网社区上有人问这个问题，奇怪但是没有人回答。 出现这个问题的原因是：一些破解软件修改了系统配置造成的。 如何解决不显示保存到Mac 桌面的文件的问题呢？
 打开终端，输入： defaults write com.apple.finder CreateDesktop -bool true; killall Finder 然后问题就解决了

```linux
defaults write com.apple.finder CreateDesktop -bool true; killall Finder
```



## 修复TNT和谐软件闪退问题
   
因为Apple苹果公司删除了TNT的证书，所以在2019年7月12日后软件都不能运行了，临时的解决办法，就是自己签名，具体往下看。

准备工作
安装xcode
安装xCode，你可以在App Store中下载安装，并且至少运行一次。

安装Command Line Tools 工具
打开终端工具输入如下命令：
xcode-select --install
弹出后选择继续安装。

签名
打开终端工具输入并执行如下命令：
codesign --force --deep --sign - /Applications/name.app

注意后面的文件路径，你可以打开访达找到应用程序，找到要签名的软件，直接拖入 终端 界面，即可自动生成路径。

