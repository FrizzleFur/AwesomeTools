# Window10安装教程


安装Win10的话将镜像放在外置硬盘上，然后使用Mac的BootCamp安装，安装并不难，网上教程也很多这里主要说一下安装后的驱动问题，包括Wifi选项无法出现等等。


### 查看是否是驱动问题

1. 找到控制面板的设备管理器
![](http://oc98nass3.bkt.clouddn.com/15256834642664.jpg)

2. 如果设备图表中有黄色的感叹号，说明对应的驱动还未安装。

![](http://oc98nass3.bkt.clouddn.com/15256835173432.jpg)

### 解决驱动


驱动其实在使用BootCamp时会去下载驱动，就在`OSXRESERVED`盘里

![](http://oc98nass3.bkt.clouddn.com/15256835862755.jpg)


这里需要在安装Win10的之前先找到`OSXRESERVED`盘里的AppleSSD64里面的文件夹，安装好里面的驱动。
 
![](http://oc98nass3.bkt.clouddn.com/15256836025370.jpg)

等驱动安装完成后再安装BootCamp盘里的 Win10。

![](http://oc98nass3.bkt.clouddn.com/15256837461138.jpg)

最后进入Win10后在`OSXRESERVED`盘里会出现`setup`的快捷方式，点击安装，就会将对应的驱动进行安装
![](http://oc98nass3.bkt.clouddn.com/15256837955116.jpg)



### Windows  10 下载

【64位简体中文专业/家庭版】
文件名：cn_windows_10_multi-edition_version_1709_updated_sept_2017_x64_dvd_100090804.iso
SHA1：`9306895149F9328CDB77FF28368F83EE984BDC30`
文件大小：4.42GB
下载地址：

```
ed2k://|file|cn_windows_10_multi-edition_version_1709_updated_sept_2017_x64_dvd_100090804.iso|4740610048|37051C54894776826823DAEBDD03F1DC|/
```

####    秘钥

```
W269N-WFGWX-YVC9B-4J6C9-T83GX
```

## 参考

1. [直接下载：Windows 10正式版官方原版镜像！-Windows 10,正式版,官方,原版,ISO,镜像,下载-驱动之家](http://news.mydrivers.com/1/440/440540.htm)

