# ParallelsDesktop



## 卸载


很多同学在安装[parallels desktop 12破解版](http://www.macappstore.net/parallels-desktop-12-po-jie/)后显示还是需要激活，是因为之前安装了parallels desktop 12 试用版卸载不干净，parallels desktop授权许可文件没有删除，所以安装了破解版后还是需要激活。

完全卸载parallels desktop 12 试用版步骤如下：

1、注销已登陆的parallels帐号；

2、要完全卸载parallels desktop 12 试用版，推荐使用[AppCleaner](http://macappstore.net/appcleaner/)

![11.png](https://www.macappstore.net/d/file/tips/2015/12-25/a2acfb5f7241139cb8aa8604d90cca0b.png)

3、打开终端.app，输入以下命令然后按回车键：

```
sudo rm -rf /Users/**这里改成你的系统用户名**/Library/Preferences/com.parallel*

sudo rm -rf /Users/**这里改成****你的系统用户名**/Library/Parallels

sudo rm -rf /private/var/db/Parallels

sudo rm -rf /Library/Logs/parallels*

sudo rm -rf /Library/Preferences/Parallels

sudo  rm -rf  /private/var/.Parallels_swap
```


## 参考

1. [parallels desktop 12 试用版完全卸载方法 - MacAppStore.net](https://www.macappstore.net/tips/parallels-desktop-uninstall/)



