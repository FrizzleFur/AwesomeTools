
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



## 修复打开app，「已损坏，无法打开。 你应该将它移到废纸篓。」 问题

方式一： （最新os会报错： Globally disabling the assessment system needs to be confirmed in System Settings.）
```
sudo spctl --master-disable
```
严格按照顺序操作：

打开系统设置
在系统设置中，导航至“隐私和安全”。让窗口在后台保持打开状态
打开终端（作为单独的窗口）。不要关闭系统设置
在终端中，运行“sudo spctl --master-disable”-->输入密码-->单击 Enter
在系统设置中，退出“隐私和安全”页面（例如 - 单击“锁屏”），然后返回“隐私和安全”
在系统设置 --> 隐私和安全页面 --> 向下滚动到底部 --> 选择“允许应用程序来自” --> 选择“任何地方”（现在会出现该选项） --> 输入密码

![image](https://github.com/user-attachments/assets/d863413b-9b74-46d2-957e-0c672d1ca24c)


方式二：

```
xattr -cr /Applications/xxx.app
```

⚙️ 移除隔离属性 运行 xattr -cr /Applications/xxx.app 会递归地删除指定应用程序的所有扩展属性，通常用于移除来自不受信任来源的隔离标记。
🔍 解决应用无法打开的问题 如果应用因为隔离而无法打开，可以通过命令删除隔离属性，以解决此类问题。
🔒 签名和验收 在macOS中，未签名的应用可以通过右键点击并选择“打开”来允许运行，这有助于绕过安全限制。 
