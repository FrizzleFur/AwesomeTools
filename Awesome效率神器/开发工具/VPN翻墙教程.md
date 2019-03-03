# VPN翻墙教程

## Shadowsocks

### Shadowsocks全局模式与VPN的区别

VPN控制的是你电脑的整个网络，只要需要连接到互联网的流量都会经过vpn。

你的IP会被更换为VPN的IP。连接VPN只需要知道IP和账号密码。

Shadowsocks的全局模式，是设置你的系统代理的代理服务器，使你的所有http/socks数据经过代理服务器的转发送出。而只有支持socks5或者使用系统代理的软件才能使用Shadowsocks（一般的浏览器都是默认使用系统代理）。

经过代理服务器的IP会被更换。连接Shadowsocks需要知道IP、端口、账号密码和加密方式。但是Shadowsocks因为可以自由换端口，所以定期换端口就可以有效避免IP被封！

### Shadowsocks全局模式与PAC模式的区别

上面已经解释了Shadowsocks的全局模式，而PAC模式就是会在你连接网站的时候读取PAC文件里的规则，来确定你访问的网站有没有被墙，如果符合，那就会使用代理服务器连接网站，而PAC列表一般都是从GFWList更新的。GFWList定期会更新被墙的网站（不过一般挺慢的）。

简单地说，在全局模式下，所有网站默认走代理。而PAC模式是只有被墙的才会走代理，推荐PAC模式，如果PAC模式无法访问一些网站，就换全局模式试试，一般是因为PAC更新不及时（也可能是GFWList更新不及时）导致的。

还有，说一下Chrome不需要Proxy SwitchyOmega和Proxy SwitchySharp插件，这两个插件的作用就是，快速切换代理，判断网站需不需要使用某个代理的（ss已经有pac模式了，所以不需要这个）。如果你只用shadowsocks的话，就不需要这个插件了！

![](https://i.imgur.com/0GYaET6.png)

### SS PAC规则

* 通配符支持，如 *.example.com/* 实际书写时可省略 * 如 .example.com/ 意即 *.example.com/*
* 正则表达式支持，以\开始和结束， 如 \[\w]+:\/\/example.com\
* 例外规则 @@，如 @@*.example.com/* 满足@@后规则的地址不使用代理
* 匹配地址开始和结尾 |，如 |http://example.com、example.com| 分别表示以 http://example.com 开始和以 example.com 结束的地址
* || 标记，如 ||example.com 则 http://example.com 、https://example.com 、http://www.example.com、ftp://example.com 等地址均满足条件，只用于匹配地址开头
* 注释 ! 如 ! Comment
* 分隔符^，表示除了字母、数字或者 _ - . % 之外的任何字符。如 http://example.com^ ，http://example.com/ 和 http://example.com:8000/ 均满足条件，而 http://example.com.ar/ 不满足条件

### SS Mac客户端

[ShadowsocksX](https://github.com/shadowsocks/ShadowsocksX-NG/releases/)    🚀


## Surge网络请求过滤神器

## 配置

参考

* [Surge更新规则很麻烦？我给做了个脚本！ - 少数派](https://sspai.com/post/45373)
* [Surge/Shadowrocket/Pepi/Kitsunebi/Postern 规则配置文件 2018.5 – 神机](Surge/Shadowrocket/Pepi/Kitsunebi/Postern 规则配置文件 2018.5 – 神机)


## JS脚本

1. [Rules lhie1 · Fndroid/jsbox_script Wiki](https://github.com/Fndroid/jsbox_script/wiki/Rules-lhie1)
2. [XinSSS/Conf-for-Surge-Shadowrocket: Surge Shadowrocket conf](https://github.com/XinSSS/Conf-for-Surge-Shadowrocket)
3. [lhie1/Rules: Rules / 规则：Surge / Shadowrocket / Quantumult](https://github.com/lhie1/Rules)

#### JSBox

```
Surge：https://xteko.com/redir?name=Rules-lhie1&url=https://raw.githubusercontent.com/Fndroid/jsbox_script/master/Rules-lhie1/.output/Rules-lhie1.box
```


#### 客户端（有“R”标示表示支持 SSR）：

```
• iOS

Surge：https://appsto.re/cn/D0Q_9.i

Shadowrocket (R)：https://appsto.re/cn/UDjM3.i

Quantumult（R）：https://itunes.apple.com/us/app/quantumult/id1252015438?mt=8

• Android

ShadowsocksR (R)：http://omgib13x8.bkt.clouddn.com/ssr-android.apk

Postern (R)：http://www.tunnel-workshop.com

• macOS

ShadowsocksX：http://omgib13x8.bkt.clouddn.com/ss-mac.zip

ShadowsocksX-R (R)：http://omgib13x8.bkt.clouddn.com/ssr-mac.dmg

Flora：https://github.com/huacnlee/flora-kit

Specht Lite：https://github.com/zhuhaow/SpechtLite/releases

Surge：http://nssurge.com

• Windows

Shadowsocks：http://omgib13x8.bkt.clouddn.com/ss-win.zip

ShadowsocksR (R)：http://omgib13x8.bkt.clouddn.com/ssr-win.7z

• 路由器固件

老毛子：http://www.right.com.cn/forum/thread-161324-1-1.html

梅林：http://koolshare.cn/thread-133873-1-1.html

```

### Rules-lhie1脚本使用手册

入门使用
节点导入
脚本拥有强大的节点识别能力，当前版本的剪贴板识别可以识别批量的Shadowsocks链接（ss://xxx）、**Surge格式链接**以及托管链接，方便进行导入。

同时，可以在脚本中对节点进行删除、重命名和设置为特殊代理操作，需要根据个人需求操作，自行尝试即可。


## Shadowsocks免费账号 

*[Shadowsocks免费账号](https://github.com/Alvin9999/new-pac/wiki/ss%E5%85%8D%E8%B4%B9%E8%B4%A6%E5%8F%B7)
* [freeSS](https://get.ss8.fun/)
* [freess](https://github.com/max2max/freess)

打开[portfolio-preview](https://ss.freess.org/#portfolio-preview) ,然后你会看到这个界面

随便点一个地址,然后会弹出个二维码，像下面这样，注意右上角，点那个纸飞机，找到那个从屏幕上扫描二维码，注意要选那个**自动代理模式**，windows 的就选 **系统代理模式**

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15343299529861.jpg)
ss 备用网址,如果上面的二维码扫了不能用，试试下面这些
* [freeSS](https://get.ss8.fun/)

## 参考

1. [Overview · Surge Manual](https://manual.nssurge.com/) 官方文档
2. [ConnersHua/Profiles: Surge、Shadowrocket、Pepi(ShadowRay)、Kitsunebi、Postern 配置规则文件](https://github.com/ConnersHua/Profiles)
3. [成功自由地飞翔在了墙外](https://hzy.pw/p/1999)
4. [Rules lhie1 · Fndroid/jsbox_script Wiki](https://github.com/Fndroid/jsbox_script/wiki/Rules-lhie1)
5. [lhie1/Rules: Rules / 规则：Surge / Shadowrocket / Quantumult](https://github.com/lhie1/Rules)
6. [Surge更新规则很麻烦？我给做了个脚本！ - 少数派](https://sspai.com/post/45373#%E4%B8%8D%E7%9F%A5%E9%81%93%E6%98%AF%E7%97%9B%E7%82%B9%E8%BF%98%E6%98%AF%E7%97%92%E7%82%B9)


