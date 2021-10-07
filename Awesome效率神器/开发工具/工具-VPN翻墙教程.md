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

## SS Mac客户端

### Mac客户端

[ShadowsocksX](https://github.com/shadowsocks/ShadowsocksX-NG/releases/)    🚀

### iOS客户端

[herzmut/shadowsocks-iOS: Fork of shadowsocks/shadowsocks-iOS](https://github.com/herzmut/shadowsocks-iOS))

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

[注册站点](https://github.com/selierlin/Share-SSR-V2ray/blob/master/1-share-ssr-v2ray.md)

以下为需要注册的站点（机场），通过机场中免费或付费的套餐，再配合工具即可科学上网。具体使用注册后机场中都会有提供教程，或者可查看本文档中的教程。

有的机场刚刚开的，会员人数不多的，网站域名奇葩的，不建议大家充值过长的套餐，在充值前可以加入机场的官方群或者TG群组

名称	试用天数	注册登录	需要翻墙	备注
中信加速器	无	✅	❌	速度延迟稳定，每月签到能有3G左右，送500M邀请码：XYKZ9
极客云	无	✅	❌	注册送10G
西部世界	6	✅	❌	验证邮箱送会员，推荐
筋斗云(飞速云)	30	✅	❌	注册送500M，每天签到最高送200M
优云666	无	✅	✅	注册送10G，每日签到送1-7G流量
速蛙云	1	✅	❌	注册送1天会员，速度快，小流量年费套餐性价比高
iKuuu	无限	✅	✅	每月50G
在人间	无	✅	❌	无试用，节点质量高且不满意可全额退
Mianna	无	✅	❌	百来节点在线，无试用，备选付费方案
BITEB	7	✅	❌	注册送7天100G，不验证邮箱
魔戒	无	✅	❌	1元套餐10流量不限时间
小白云	无	✅	❌	注册送100G及三个免费节点，套餐最低5元/月，备选
蒲云	无	✅	❌	注册送100G，40+服务器，月费5元

## Chacha-20加密

1. 链接主机

```
// 切换到本地root
sudo su - 
// ssh链接origin,注意是ssh端口
ssh root@IP地址 -p ssh端口
```
同样的，如果是第一次连接，需要你保存VPS的签名密钥，输入yes保存即可。之后是输入SSH密码，在输入的时候界面不会显示，输入完毕后直接回车即可，如果IP地址、SSH端口、SSH密码都正确，则会出现连接成功的标志。


* [搬瓦工(bandwagonhost)后台管理VPS&安全设置 - 老高的技术博客](https://blog.phpgao.com/bandwagonhost_vps_panel.html)
* [给远程服务器设置SSH Key免密码登录 - 搬瓦工 - SegmentFault 思否](https://segmentfault.com/a/1190000015362485)
* [Windows/Mac/Linux如何SSH远程连接/登陆搬瓦工 - 搬瓦工优惠网](https://www.bwgyhw.cn/bandwagonhost-ssh-login/)



## IP被封

首先是检测你搬瓦工IP的可用性，首先是检测你搬瓦工IP的可用性：登陆搬瓦工官网（https://bwh8.net），选择My Services，然后选择被墙的服务，进入KiwiVM Control。之后进入这个检测网址：https://kiwivm.64clouds.com/main-exec.php?mode=blacklistcheck，点击Test Main IP后，搬瓦工会帮你检测你的IP的可用性（是否被GFW封禁），并返回给你结果：


* [Just My Socks 详细图文购买教程 - 搬瓦工 JMS](https://bwgjms.com/post/how-to-buy-justmysocks/)
* [搬瓦工IP被封后，后台自助付费更换新IP教程（仅需8美元）-Bandwagonhost中文网](https://www.bandwagonhost.net/1312.html)<https://bwh88.net/ipchange.php>
* [搬瓦工IP被封 搬瓦工免费更换被封IP 每10周免费更换一次 - 搬瓦工优惠网](https://www.bwgyhw.cn/bandwagonhost-change-ip-free/)
* [网站端口扫描结果](http://tool.chinaz.com/port/)


## 参考

1. [Overview · Surge Manual](https://manual.nssurge.com/) 官方文档
2. [ConnersHua/Profiles: Surge、Shadowrocket、Pepi(ShadowRay)、Kitsunebi、Postern 配置规则文件](https://github.com/ConnersHua/Profiles)
3. [成功自由地飞翔在了墙外](https://hzy.pw/p/1999)
4. [Rules lhie1 · Fndroid/jsbox_script Wiki](https://github.com/Fndroid/jsbox_script/wiki/Rules-lhie1)
5. [lhie1/Rules: Rules / 规则：Surge / Shadowrocket / Quantumult](https://github.com/lhie1/Rules)
6. [Surge更新规则很麻烦？我给做了个脚本！ - 少数派](https://sspai.com/post/45373#%E4%B8%8D%E7%9F%A5%E9%81%93%E6%98%AF%E7%97%9B%E7%82%B9%E8%BF%98%E6%98%AF%E7%97%92%E7%82%B9)
## 封IP了
8. [再也不怕SS服务器被封IP了 | 一个你](https://www.yigeni.com/not-afraid-of-the-ss-server-is-blocked-ip/)



