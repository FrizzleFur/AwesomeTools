## Shadowrocket


[一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略 | 很文博客](https://www.hinwen.com/3662.html)

**二，全局路由的策略**

小火箭拥有四种全局路由策略：配置、代理、直连、场景。下面一一介绍。
![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828704-9165-bathx6srt.jpg)

**1，配置**

选用配置（规则）方法来进行连接。可以根据不同的规则，使网络连接在自己定制的“规则”范围内进行。例如可以分流（例如国内IP直连，国外网站自动走代理），例如可以去除广告。小火箭的配置和节点是分开的，这一点很方便。

（1）添加配置
小火箭支持从URL或者.conf文件方式，还有云端导入。

A. 从URL添加配置

小火箭——配置——点击右上角的“+”号，弹出对话框输入（粘贴）配置地址，然后可以在远程文件处，看到刚刚下载的远程文件，点击，弹出选项中选择使用配置，该配置就会添加到“远程文件”列表上方的“本地文件”列表当中，选择就可以使用了。

注意：在配置的“本地文件”中，前面的黄色小圆点表示默认配置，后面的打钩符号，表示正在使用。
![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828705-7898-eixza8f1l.jpg)

在远程文件点击该配置，可以对配置进行预览，使用和复制网址。在本地文件中，点击配置文件，可以编辑配置，改名，导出等操作。

1.  Tips
2.  推荐的配置
3.  lhie1的Shadowrocket规则：
4.  https://raw.githubusercontent.com/lhie1/Surge/master/Shadowrocket.conf
5.  说明：目前比较主流小火箭规则，长期维护更新，所有国内网站直线连接，国外常用网站加速，解决本地 DNS 可能带来的干扰，屏蔽部分应用程序的广告，屏蔽部分运营商劫持网页，屏蔽常用网站广告、其他流媒体网站广告。
6.  逗比极客surge规则：
7.  精简规则
8.  https://raw.githubusercontent.com/tudi1909/Surge_rules/master/iOS_S.conf
9.  全能规则
10.  https://raw.githubusercontent.com/tudi1909/Surge_rules/master/iOS.conf
11.  说明：小火箭兼容Surge规则，逗比极客规则并没有小火箭专版，所以在使用上，导入规则后，需要手动去除添加进来的节点信息。

B. conf文件方式导入

小火箭也支持从conf文件为后缀名的配置文件导入，如下图所示，打开conf文件，选择拷贝至小火箭。小火箭兼容Surge规则。如果导入的是Surge配置文件，会提示是否保存配置文件当中的节点，建议选择否。导入后在配置中“本地文件”可以看到。
![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828705-2348-3xipbyy3t.jpg)

C. 从云端导入

小火箭支持从云端导入配置，在配置界面可以看到，支持从 iCloud或者其他网盘方式导入。 
![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828707-8752-9zqc2gmjt.jpg)

在配置界面，也可以对配置进行上传，编辑等等。

（2）编辑配置

点击已经导入本地文件的配置，可以对配置进行编辑。
![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828707-8357-adro226nd.jpg)

可以按分类编辑，也可以纯文本编辑。适合对规则有一定了解的朋友。![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828707-6394-53mparmeh.jpg)

（3）更新配置

配置的更新，适合以URL方式导入的规则。可以在配置——远程文件处，点击所选远程文件网址，弹出菜单选择使用配置，重新导入配置，就是该远程文件最新的配置了。无需理会节点问题。 

**2，代理**

即为全部网络连接使用代理进行，Proxy，就是我们所说的全局代理。

**3，直连**

直接访问网络，Direct，并不使用科学上网连接。

**4，场景**

根据不同使用场合自动切换相关配置，支持使用不同的Urltest测速分组和Conf配置文件。这个是小火箭特有的厉害之处。根据设置的场景，可以切自动切换节点或者配置。例如，我可以设置一个场景，网络切换到公司WIFI，可以使小火箭自动切换到直连状态。

位置在首页——全局路由——场景。

### Shadowrocket-ADBlock-Rules

[最完善的 iOS 翻墙规则](https://github.com/h2y/Shadowrocket-ADBlock-Rules)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E5%9B%BD%E5%86%85%E5%A4%96%E5%88%92%E5%88%86--%E5%B9%BF%E5%91%8A)国内外划分 + 广告

国内外划分，对中国网站直连，外国网站代理。包含广告过滤。国外网站总是走代理，对于某些港澳台网站，速度反而会比直连更快。

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_cnip_ad.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_cnip_ad.conf)

[![二维码](https://camo.githubusercontent.com/dab6e9fa13c649841771856bb579364f77c5b9ef/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f636e69705f61642e706e67)](https://camo.githubusercontent.com/dab6e9fa13c649841771856bb579364f77c5b9ef/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f636e69705f61642e706e67)

## 黑名单过滤 + 广告

黑名单中包含了境外网站中无法访问的那些，对不确定的网站则默认直连。

*   代理：被墙的网站（GFWList）
*   直连：正常的网站
*   包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist_ad.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist_ad.conf)

[![二维码](https://camo.githubusercontent.com/5a5e348eecdbf6ed8c04199cc4726535a2b95c56/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f62616e6c6973745f61642e706e67)](https://camo.githubusercontent.com/5a5e348eecdbf6ed8c04199cc4726535a2b95c56/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f62616e6c6973745f61642e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E7%99%BD%E5%90%8D%E5%8D%95%E8%BF%87%E6%BB%A4--%E5%B9%BF%E5%91%8A)白名单过滤 + 广告

白名单中包含了境外网站中可以访问的那些，对不确定的网站则默认代理。

*   直连：top500 网站中可直连的境外网站、中国网站
*   代理：默认代理其余的所有境外网站
*   包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist_ad.conf)

[![二维码](https://camo.githubusercontent.com/624743e0cb21dc2ffc2002076428bfdf74262bd9/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f77686974656c6973745f61642e706e67)](https://camo.githubusercontent.com/624743e0cb21dc2ffc2002076428bfdf74262bd9/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f77686974656c6973745f61642e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E9%BB%91%E5%90%8D%E5%8D%95%E8%BF%87%E6%BB%A4)黑名单过滤

现在很多浏览器都自带了广告过滤功能，而广告过滤的规则其实较为臃肿，如果你不需要全局地过滤 App 内置广告和视频广告，可以选择这个不带广告过滤的版本。

*   代理：被墙的网站（GFWList）
*   直连：正常的网站
*   不包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_banlist.conf)

[![二维码](https://camo.githubusercontent.com/0d5ab95b2bc3465807d1a04c8ed58da6e3909cbc/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f62616e6c6973742e706e67)](https://camo.githubusercontent.com/0d5ab95b2bc3465807d1a04c8ed58da6e3909cbc/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f62616e6c6973742e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E7%99%BD%E5%90%8D%E5%8D%95%E8%BF%87%E6%BB%A4)白名单过滤

现在很多浏览器都自带了广告过滤功能，而广告过滤的规则其实较为臃肿，如果你不需要全局地过滤 App 内置广告和视频广告，可以选择这个不带广告过滤的版本。

*   直连：top500 网站中可直连的境外网站、中国网站
*   代理：默认代理其余的所有境外网站
*   不包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_top500_whitelist.conf)

[![二维码](https://camo.githubusercontent.com/5fc33dc7e604912114527718f41406c5e9b1bbfc/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f77686974656c6973742e706e67)](https://camo.githubusercontent.com/5fc33dc7e604912114527718f41406c5e9b1bbfc/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f746f703530305f77686974656c6973742e706e67)


## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E5%9B%BD%E5%86%85%E5%A4%96%E5%88%92%E5%88%86)国内外划分

国内外划分，对中国网站直连，外国网站代理。不包含广告过滤。国外网站总是走代理，对于某些港澳台网站，速度反而会比直连更快。

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_cnip.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_cnip.conf)

[![二维码](https://camo.githubusercontent.com/ee1329b63fefa051e3baa12b4c4b7febe62365fd/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f636e69702e706e67)](https://camo.githubusercontent.com/ee1329b63fefa051e3baa12b4c4b7febe62365fd/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f636e69702e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E7%9B%B4%E8%BF%9E%E5%8E%BB%E5%B9%BF%E5%91%8A)直连去广告

如果你想将 SR 作为 iOS 全局去广告工具，这个规则会对你有所帮助。

*   直连：所有请求
*   包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_direct_banad.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_direct_banad.conf)

[![二维码](https://camo.githubusercontent.com/b4541c720bbec612677f1c22c72efb25b83077d0/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f6469726563745f62616e61642e706e67)](https://camo.githubusercontent.com/b4541c720bbec612677f1c22c72efb25b83077d0/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f6469726563745f62616e61642e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E4%BB%A3%E7%90%86%E5%8E%BB%E5%B9%BF%E5%91%8A)代理去广告

如果你想将 SR 作为 iOS 全局去广告 + 全局翻墙工具，这个规则会对你有所帮助。

*   直连：局域网请求
*   代理：其余所有请求
*   包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_proxy_banad.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_proxy_banad.conf)

[![二维码](https://camo.githubusercontent.com/d810eb98113c5c2de43d3e82b4a1b5604f750c01/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f70726f78795f62616e61642e706e67)](https://camo.githubusercontent.com/d810eb98113c5c2de43d3e82b4a1b5604f750c01/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f70726f78795f62616e61642e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E5%9B%9E%E5%9B%BD%E8%A7%84%E5%88%99)回国规则

提供给海外华侨使用，可以回到墙内，享受国内的一些互联网服务。

*   直连：国外网站
*   代理：中国网站
*   不包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_backcn.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_backcn.conf)

[![二维码](https://camo.githubusercontent.com/a8163129e6210ad5eca054f443635d9fe3ca9941/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f6261636b636e2e706e67)](https://camo.githubusercontent.com/a8163129e6210ad5eca054f443635d9fe3ca9941/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f6261636b636e2e706e67)

## [](https://github.com/h2y/Shadowrocket-ADBlock-Rules#%E5%9B%9E%E5%9B%BD%E8%A7%84%E5%88%99--%E5%B9%BF%E5%91%8A)回国规则 + 广告

提供给海外华侨使用，可以回到墙内，享受国内的一些互联网服务。

*   直连：国外网站
*   代理：中国网站
*   包含广告过滤

规则地址：[https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_backcn_ad.conf](https://raw.githubusercontent.com/h2y/Shadowrocket-ADBlock-Rules/master/sr_backcn_ad.conf)

[![二维码](https://camo.githubusercontent.com/2d5e9512c21cd525473a5255dc56e62880a8108c/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f6261636b636e5f61642e706e67)](https://camo.githubusercontent.com/2d5e9512c21cd525473a5255dc56e62880a8108c/68747470733a2f2f63646e2e7261776769742e636f6d2f6832792f536861646f77726f636b65742d4144426c6f636b2d52756c65732f6d61737465722f6669677572652f73725f6261636b636e5f61642e706e67)


### **1，免费节点获取**


```
https://workflow.is/workflows/838f38ed3dd04caab31871a8aaeb5056

```
**，[小火箭](https://www.hinwen.com/tag/%e5%b0%8f%e7%81%ab%e7%ae%ad/ "查看与 小火箭 相关的文章")相关Workflow流程**

有了小火箭，最重要的还是要有节点才行。使用Workflow的小火箭免费节点获取，可以轻松获取节点。

**1，免费节点获取**
![一次讲透：IOS翻墙利器“小火箭（Shadowrocket）”上手、进阶、配合Workflow获取免费节点攻略](https://img.hinwen.com/hw-files/2017/06/1496828725-3408-jn830s0mh.jpg)

最新免费节点获取，6月1日更新。从FreeSS和shadowsocks8获取免费节点。新增Ishadowx网站9个节点，目前流程总共18个免费节点，更多选择了。是目前免费节点获取类Workflow流程节点最丰富的了。因为每天网站都会更换节点密码，所以节点失效，请重新获取。

## 参考

* [老高推荐的VPS - 老高的技术博客](https://blog.phpgao.com/vpses.html)
