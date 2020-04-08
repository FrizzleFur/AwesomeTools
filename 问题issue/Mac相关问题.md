
## 桌面图片不显示


desktop文件夹里有东西，但是桌面不显示，而且无法拖动任何文件到桌面。 苹果官网社区上有人问这个问题，奇怪但是没有人回答。 出现这个问题的原因是：一些破解软件修改了系统配置造成的。 如何解决不显示保存到Mac 桌面的文件的问题呢？
 打开终端，输入： defaults write com.apple.finder CreateDesktop -bool true; killall Finder 然后问题就解决了

```linux
defaults write com.apple.finder CreateDesktop -bool true; killall Finder
```