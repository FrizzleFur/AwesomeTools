# Awesome工具

[TOC]

> 在工作中，现在公司大多数使用MacBook进行办公，不仅仅是MacBook设计简洁，方便携带，OS X上有一些很多优秀的开发者，经过长期的开发迭代，有一些很Nice的效率工具，能够给你平常的工作和开发提速。神器很多，这里就介绍几款我效率工具箱中平常使用最多的几款工具吧。
![](http://oc98nass3.bkt.clouddn.com/15161925609832.png)

## Todo

 * [ ] Keyboard Maestro设置文件存放规则
 * [ ] Quip的功能详细介绍
 * [x] 整理文档的App
 * [x] `Mweb`的Mac和iOS之间同步 （`2018-03-05`完成同步，设置好文档库）
 * [x] `Alfred3`功能详细介绍 （`2018-06-30`完成同步，设置好文档库）
 * [x] [定期自动云备份 macOS 软件列表，维护一份属于自己的必备 App 清单 - 少数派](https://sspai.com/post/43265)

## Alfred 

`Alfred` 就是 `Mac` 上最强大的工具台，一个图形化的终端，只有你想不到，没有它做不到。

![image](http://upload-images.jianshu.io/upload_images/225323-9241e9deef92a341.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

详情请查看 [Alfred教程](https://github.com/FrizzleFur/AwesomeTools/blob/master/Awesome%E6%95%88%E7%8E%87%E7%A5%9E%E5%99%A8/Alfred%E6%95%99%E7%A8%8B.md)
 
## Aria2

[itgoyo/Aria2: 支持迅雷、百度云无限制超速下载，另外附带Tampermonkey、Proxyee-down教程。从此云端女友从不断线，有了这个它，忘掉那个她!](https://github.com/itgoyo/Aria2#webui-aria2)
堪比迅雷的下载神器，破解百度云的下载速度很好用
![](http://oc98nass3.bkt.clouddn.com/15343353123639.jpg)

 [Aria2](https://bbs.feng.com/read-htm-tid-10895696.html)

### BaiduExporter

![](http://oc98nass3.bkt.clouddn.com/15343352496848.jpg)

[BaiduExporter.crx](https://github.com/acgotaku/BaiduExporter/blob/master/BaiduExporter.crx)
![](http://oc98nass3.bkt.clouddn.com/15233734067615.jpg)
![](http://oc98nass3.bkt.clouddn.com/15233734324565.jpg)

### Aria2+Chrome+BaiduExporter破解百度云下载速度

需要搭配[BaiduExporter](https://github.com/acgotaku/BaiduExporter)

[YAAW-for-Chrome](https://github.com/acgotaku/YAAW-for-Chrome)Yet Another Aria2 Web Frontend in pure HTML/CSS/Javascirpt http://binux.github.io/yaaw/demo/

然后在所有的下载链接上右键选择ARIA2 RPC进行下载就可以了。

##### 参考Aria2

[Aria2+YAAW+Tampermonkey下载百度云文件](http://www.51yimo.com/2018/01/04/aria2-yaaw/)
[Mac 上有什么比较好用的下载工具？ - 知乎](https://www.zhihu.com/question/19552868)

#### 百度云大文件链接

1. 安装油猴插件（插件商店搜索`Tampermonkey`并安装）
2. 安装`EX-百度云盘`油猴脚本([EX-百度云盘](https://greasyfork.org/zh-CN/scripts/26638-ex-%E7%99%BE%E5%BA%A6%E4%BA%91%E7%9B%98))
3. 百度云盘中的页面中会多一个`EX-下载`的选项
4. 这时在`EX-下载`的下拉菜单中的`普通下载`右键还不能将任务发送aria2进行下载，需要将文件共享。
5. 在共享页面的`EX-下载`的菜单中选择`普通下载`后，Chrome就可以下载大文件了。然后在下载的链接上右击，选择`ARIA2-RPC`就可以了。
6. 按照上边的Aria2 Web可以查看下载的文件和进度。


### 下载路径配置

#### 方法 1

* 在`StartAria2c.sh`文件中修改, 我尝试在`Aria2.conf`文件中修改，无效。
![](http://oc98nass3.bkt.clouddn.com/15233766309641.jpg)

* `StartAria2c.sh`文件路径 `~/Library/Application Support/com.Aria2GUI/sh/`
但是重启`Aria2`后，下载路径会reset所以建议使用方法2

#### 方法 2

* [请问如何将aria2gui的下载路径改成移动硬盘 · Issue #27 · yangshun1029/aria2gui](https://github.com/yangshun1029/aria2gui/issues/27)

![step1](http://oc98nass3.bkt.clouddn.com/15233769519238.jpg)

![step2](http://oc98nass3.bkt.clouddn.com/15233769336959.jpg)

当然浏览器重启后也会reset插件的下载路径 。。。

### axel

Axel — Light command line download accelerator for Linux and Unix
[axel-download-accelerator/axel: light command line download accelerator](https://github.com/axel-download-accelerator/axel)

### proxyee-down

[proxyee-down-org/proxyee-down: http下载工具，基于http代理，支持多连接分块下载](https://github.com/proxyee-down-org/proxyee-down)

## Bee For mac

[Bee: GitHub Issues made Simpler, Faster and Fun](https://www.neat.io/bee/github-issues-client.html)

Bee 是Mac上一款优秀的`Github Issue`跟踪软件，可以将日常的任务放入`Github Issue`中，使用Bee进行管理。

### Bee的功能feature

* Beautiful UI界面简洁
* View relevant issues only，提供过滤
* Images in issues and comments are viewed with Quicklook. 图片提供预览
* Linked Issues 
* Issue Short List 
* Timesheets提供工作的计时
* Markdown Editor 也是一个Markdown编辑器，可以直接使用Markdown编辑

### Bee的快捷键

![](http://oc98nass3.bkt.clouddn.com/15217922741672.jpg)

## Bilibili-mac-client

[流媒体NB工具](http://vp-hub.eqoe.cn/)
[typcn/bilibili-mac-client](https://github.com/typcn/bilibili-mac-client)
[Bilibili-mac-client FAQ](http://vp-hub.eqoe.cn/faq.html)

*  点击屏幕顶部菜单栏中的 Bilibili - 设置 可以调整弹幕速度，弹幕字体大小，透明度，画质，下载格式等选项
* 点击 设置 - 弹幕屏蔽 可以对弹幕进行关键词屏蔽，也可以使用智能屏幕模式，一键屏蔽吵架，剧透等弹幕
*  点击浏览器右上角的菜单 刷新/复制当前页面地址，可以查看历史记录
*  播放器控制条右边的视频时长，点击可以切换到 Buffer 大小，再次点击切换回视频时长
*  点击播放器控制条空白区域可以拖动，支持拖动到窗口外面
*  将字幕文件拖动到窗口上可以加载字幕 
*  空格暂停/播放，上下调整音量，左右调整进度， 按 J 切换字幕，S 键截图
* "," 和 "." 逐帧播放，"[" 和 "]" 变速播放，"L" AB 循环，Shift+L 洗脑循环
* "Z" 和 "X" 调整字幕延迟， F 键窗口置顶， CMD+F 键全屏
* 另外，你可以通过 Input.conf 来自定义快捷键

#### 使用说明

* 点击屏幕顶部菜单栏中的 Bilibili - 设置 可以调整弹幕速度，弹幕字体大小，透明度，画质，下载格式等选项
* 点击 设置 - 弹幕屏蔽 可以对弹幕进行关键词屏蔽，也可以使用智能屏幕模式，一键屏蔽吵架，剧透等弹幕
* 点击浏览器右上角的菜单 刷新/复制当前页面地址，可以查看历史记录
* 播放器控制条右边的视频时长，点击可以切换到 Buffer 大小，再次点击切换回视频时长
* 点击播放器控制条空白区域可以拖动，支持拖动到窗口外面
* 将字幕文件拖动到窗口上可以加载字幕
默认快捷键
* 空格暂停/播放，上下调整音量，左右调整进度， 按 J 切换字幕，S 键截图
* "," 和 "." 逐帧播放，"[" 和 "]" 变速播放，"L" AB 循环，Shift+L 洗脑循环
* "Z" 和 "X" 调整字幕延迟， F 键窗口置顶， CMD+F 键全屏
* 另外，你可以通过 Input.conf 来自定义快捷键
已知重要问题
全屏时发热剧增 --- 这是一个苹果 OpenGL 驱动的 BUG ，可以到设置中开启全屏 BUG Workaround 以解决（需要 2.46 或更高）
硬解在部分情况下不生效 --- 苹果的硬解是单实例的，同时只能有一个程序在播放一个视频，如果有其他的程序（例如浏览器 HTML5 视频）在使用硬解，请先退出它们（macOS 10.12 已支持多实例）
播放中途切换显卡崩溃 --- 这是一个苹果 OpenGL 驱动的 BUG，没有任何办法 Workaround
多显示器在播放器加载完成前全屏会跳出且无控制条 --- 还在想办法，可以先等视频加载完再全屏
如果下载功能无法正常使用
1. 确保已经放到 /Applications 文件夹 2. 请先播放任意视频，然后退出并重新打开软件再试
如何播放下载的多段视频
您可以使用鼠标框选，或者按住 Shift 选择所有的视频片段，软件会自动将其作为一个视频播放。
视频提示盗链或无法解析
如果您遇到盗链提示，请立即升级软件到最新版本，如果已经是最新版本，退出并重新打开软件则会自动更新解析模块。
还不行的话，请点击帮助 -> 反馈，或者给我发邮件，我将在 24 小时内修复并发布更新
如何使用别的浏览器？
目前支持使用 Chrome 作为浏览器，扩展地址 https://chrome.google.com/webstore/detail/njfkchgcdllehlpohbhmfjbcojolkafa/
使用过程中请确保客户端处于开启状态，可以把客户端自带的浏览器窗口关掉，但是不要退出程序
如何看优酷，乐视等视频？
点击客户端最上方的“新建标签”按钮（小方块），然后选择相应的网站，点击安装即可
海外用户如何开启类似 Unblock youku 的功能
打开设置，在 IP 伪造中输入一个中国 IP ，或者在下拉框选择一个内置好的 IP 地址，如果在换 P 的过程中出现版权提示，点击左上角的刷新按钮即可继续观看。
点击更新提示错误，或更新后无法打开
请先从官网 http://bilimac.eqoe.cn 手动下载最新版并覆盖，如果还不行，请反馈，联系方式在页面底部。
点击播放或下载按钮没有反应
软件需要 23336 和 23330 端口来进行通讯，请先升级到最新版本，如果最新版本也不行，请确认没有被占用或拦截。
如果端口正常，但是依然没有反应，则可能是 Hosts 中的默认内容被删除过，在 /etc/hosts 中加入 127.0.0.1 localhost 即可
发热过高，如何开启增强硬解
点击左上角的 “Bilibili” 然后点击设置，在启用 VT 硬解引擎前面打上对勾即可，观看 4K 视频仅占 10% CPU，但是可能导致弹幕 FPS 降低一点，请根据实际情况选择。
看不到任何弹幕
首先确保软件已经安装在 Applications 文件夹，然后打开 “终端” 输入 rm -rf /Users/Shared/.fc ，重启软件点击任意视频播放，然后等几分钟即可，如果仍然有问题，请联系开发者进行反馈。
弹幕 FPS 低 闪瞎狗眼
由于硬解模式下渲染引擎有一些问题，请打开 设置-> 一般设置，取消勾选 “启用增强硬解模式” ，弹幕即可增加到 60 FPS 以上。
部分视频打开必崩溃
如果网页可以正常播放，可能是视频源 CDN 的问题，请过一会再试，如果问题一直存在，请联系开发者。
使用时出现崩溃
一旦崩溃，请点击“报告”按钮，然后复制框内的所有内容，发邮件给我 ，我将尝试进行处理。
更多
想不出来了，还有问题请联系我（PS：如果有任何想要的功能，请到 GitHub 提出，只要可以实现，有时间我就会去增加）

## Boostnote

[Boostnote：为程序员量身定做的笔记应用](https://www.waerfa.com/boostnote-review)

> Boostnote 是一款专门为程序员朋友量身打造的笔记软件，除了日常笔记记录，最大的用处就是帮你记录无数的代码资源，你甚至可以以一个单个笔记为单位，在里面创建多个 Tab，以组成一个独立的 Code 项目。软件支持收藏、标签、分组、搜索、栏目切换等笔记应用应有的功能。

在笔记编辑区底部，你可以快速选择代码书写环境、选择缩进操作方式以及字号。

### Boostnote 官网

Boostnote 使用 Electron、React + Redux、Webpack、CSSModules 等最新技术开发，支持 Latex 这样的小众语法格式。用户在分组下新建笔记时有 Markdown 和 Snippet 两种模式可选，Markdown 模式下会自动支持各种 MD 语法以及 Latex 格式，而 Snippet 模式则会为用户提供 N 多种代码书写环境。

### 分组存储笔记很有趣

Boostnote 设立了名为「Storage」的笔记分组功能，未来版本还会加入 Google Drive、Dropbox 的云目录分组功能。

### UI 自定义让你的桌面更加丰富多彩

软件提供了黑白两色主题，并有数十种文本配色可选，你还能设置文本的字体、字号、行距、预览切换方式、Keymap 以及预览窗口的样式自定义。

### Dev Track

独有的 Dev Track 功能可以让你在笔记中列出自己的开发进度列表，每完成一项功能挑勾后即代表对应进度已完成，上方的进度栏还能同步显示进度比例，非常的 Geek。
 
### Finder Popup

除了主窗口，Boostnote 还独立配备了一个 Finder Popup 窗口，供用户直接在应用内查找历史文档。同时你还能通过「收藏」、「分组」等条件事先过滤一下文档

### 快速拷贝代码

Boostnote 支持快速拷贝代码到剪贴板帮助程序员提高工作效率。

## Chrome

发现Chrome的拓展除了
```
chrome://extensions/
```
还有个
```
chrome://apps/
```

## CmdTap

破解代码

```objc
def md5(str):
    import hashlib
    import types
    if type(str) is types.StringType:
        m = hashlib.md5()
        m.update(str)
        return m.hexdigest()
    else:
        return ''
 
email = "mac@apple.com"
 
m = md5(md5(email)[0:10]).upper()
key = m[5:8]+'-'+ m[8:11]+'-'+m[11:14]+'-'+m[14:17]
 
print key
```



```
ffur@apple.com
90B-915-B69-15A
```

参考  [飘云阁(PYG官方论坛) CmdTap | 任务切换器增强 for Mac | 算法分析及注册码一枚 - Powered by Discuz!](http://www.chinapyg.com/thread-83080-4-1.html)


##  DayOne

现在Dayone付费订阅制了，下载`V2.1.8`的版本进行同步。
[Day One 2 for Mac 2.1.8 激活版 - 最优秀的日记软件](https://www.waitsun.com/day-one-2-1-8.html#downlink)

早期的 Day One 是我在 Mac 上最喜欢的软件，没有之一，尽管有家庭共享，我还是单独买了４套，结果我一买，它很快就升级了，非常令人无语。新版本令我非常失望，幸好还有老版本。
我们厌恶订阅：
　　但老版本的 DayOne 好多甚多，App 我个人非常喜欢买断，而不是订阅，日常用到的有200-400种，大多使用频率很低，如果订阅，则会像吸血鬼一样成为负担，我认为任何软件的订阅其重要性永远比不上水、电这些基本生存需要，既然不在一个等级，就不能使用同样的对待方式。买断的就不用考虑使用频率了（当然，我也被很多 App 伤害过，Mindnode 刚买网两套就重新付费了，Ulysess 300元左右，买过不久就免费加付费订阅了等等）。
一代瑕不掩瑜：
　　Day One 一代的安全问题是存盘文件未加密，而不是在哪存储的问题，一代使用的是 iCloud ，至少空间还掌握在用户自己手里，论厂商，苹果比 DayOne 可靠多了，有些私密的照片我用 Day One 2 也都是不敢开启同步的。iCloud 尽管免费的只有5G，其实大多够用。现在 iPhone 都是256G 了，备份到 iCloud 根本不够用，如果如苹果所说，照片存到 iCloud 相册不计空间，照片流不计空间，APP 仅仅备份“布局视图”（大家可以理解为快捷方式和排列位置），都需要重新下载，那根本不会占用什么空间，可是备份起来还是需要几个 GB，我很怀疑苹果到底干了什么。我干脆备份到 Mac ，且关闭 Mac 把桌面放到 iCloud 的做法，iCloud 只保留常用软件的交付物，5GB 空间绰绰有余。Day One 目前也就500MB 左右，还够用好多年。

之前是软件收费，现在改成软件免费，账号付费了，所以这个版本没用了，因为你自己的账号没付费，就不能同步。2.1.8还属于软件付费的版本，所以可以同步。看看站长新版有办法没有。

##  Due

[5 个 Due 的使用技巧和心得 - 少数派](https://sspai.com/post/30471)
Due 最大的亮点就是可以不断地提醒你直至任务完成。听起来有点类似闹钟，不过它并不像闹钟那样持续响铃，而是每隔一段时间就提醒你一次，间隔可以在一分钟到一小时之间设置。

 Due确实帮助我完成了很多事情, 而是人们总会因为各种各样的原因忘记或错过一些事情，Due 的重复提醒则在这里起到了很大的作用。经过一段时间的使用，我总结了 5 个使用技巧和心得与大家分享。

### 1. 在任务名称里输入电话号码

比如你可以添加一个内容为 联系李小明 186-0000-0000 的任务，当你将这个任务标记完成时，Due 会弹出这样的界面：
![](https://cdn.sspai.com/attachment/origin/2015/08/02/270941.png?origin?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)
选择 呼叫 186-0000-0000 可以直接拨通李小明的电话，选择 发信息给 186-0000-0000则会弹出编写短信的界面。

更进一步的用法：如果你对 iOS 的 URL Scheme 稍微有所了解，就会知道打电话的 URL Scheme 是 tel://。所以我们可以添加一个 打电话给李小明 tel://186-0000-0000 的任务，当任务标记完成时，就会弹出只有「拨打电话」一个按钮的菜单。同理添加 发信息给李小明 sms://186-0000-0000 的任务就只会弹出发送短信的菜单。

### 2. 用换行作为备注

有时候我们的任务不只是一句话，我们会需要给任务添加一些备注，比如 打电话给李小明，关于周末聚会的事情，吃饭唱 K 或者游泳烧烤。这个时候我们就可以用「换行」来分隔任务本身和备注内容，变成：
![](http://oc98nass3.bkt.clouddn.com/15063942473742.jpg)
打电话给李小明

当然你不换行也不是不行，只是我认为换行后可以让我们更直观地区分任务本身和备注内容。不过需要注意的是，Due 的主界面最多只能显示三行内容，超过三行的必须点进任务详情才能查看。

### 3. 设置不同的重复提醒时间(小睡功能)

不同的任务有不同的紧急程度，所以应当设置不同的重复提醒时间（小睡功能）。

对于一些紧急程度不是很高的任务，尽量把重复提醒时间设置得长一点，否则会因为过分打扰而觉得烦躁。比如我有一个叫 记账 的任务，会在每天晚上十点三十分的时候提醒我。我一般在这个时间点后不会有消费，隔天记账的话容易忘。但我也不是说非得在十点三十分的时候记账，因为对于我来说只要在今天结束前记好账就好了。有可能十点三十分的时候我刚好在忙，又或者当时没注意到提醒通知。所以我将重复提醒时间设置为 三十分钟，这样我在十二点前就能获得四次的提醒（一直忽略或者错过的情况下），提醒次数刚好，也不至于过烦。

### 4. 协调好 Due 与其它任务管理软件

我在之前两篇测评中 [1] 都讨论过 Due 无法单独成为一个任务管理软件的原因，[2] 所以对于要将任务放到 Due 还是其它任务管理软件，必须有一个非常明确的区分规则。Due 的特点**是必须给任务设置提醒时间，并且提醒功能极其强大**。**所以我的区分规则是：在提醒来之前，我完全不需要关心这件事，也不需要在提醒之前完成这件事。这样的任务，我会放到 Due 里。**

你最好也有自己的区分规则，尽量简单，不要让自己产生过多的犹豫。

### 5. 使用中文自然语句输入
在之前发布的 2.0.2 版本中，Due 终于支持了中文的「相对时间」自然语句。比如你可以用中文输入**三小时后**打电话给李小明，Due 就会自动将提醒时间设置到三小时后，非常方便。

需要注意的是，中文自然语句输入只在中文系统下生效。如果将 iOS 系统语言设置为英文的话，「相对时间」的中文自然语句会失效，「绝对时间」则不会。

## Eudic 欧陆词典

最好使用老版本`V 3.5.4 `

```
/Users/michaelmao/Library/Preferences/com.eusoft.eudic.plist
/users/用户名/Library/Preferences/com.eusoft.eudic.plist
```
MAIN_TimesLeft 参数 改为 `820711`

可以通过账户登录来同步手机端的学习记录，很Nice~有条件的还是支持一下吧。

本人的一些配置（调教）：
![](http://oc98nass3.bkt.clouddn.com/15159839251696.jpg)
![](http://oc98nass3.bkt.clouddn.com/15159839872215.jpg)
![](http://oc98nass3.bkt.clouddn.com/15159840462422.jpg)
![](http://oc98nass3.bkt.clouddn.com/15237711172483.jpg)

### 延长试用期

建议官网下载最新版本

1. 找到 plist文件

![](http://oc98nass3.bkt.clouddn.com/15133950232119.jpg)

2. 设置 两个参数
    - plist 文件用编辑器打开即可。
    - MAIN_TimesLeft 参数 改为 `820711`
    - MAIN_ProductID 参数 任意填写
    - 保存 即可

3. 锁定plist 文件

右键显示 简介 锁定 文件
![](http://oc98nass3.bkt.clouddn.com/15160009301637.jpg)

4. 重启词典

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/225323-e430da409396a3a2.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/225323-03766669485a6314.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

![Paste_Image.png](http://upload-images.jianshu.io/upload_images/225323-9e740dce186adb81.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
## Gmail

[收发Gmail 必学12招，善用邮件分类、前端管理当Gmail 达人 - 简书](http://www.jianshu.com/p/4807f87ee1a5)

##  F.lux

Mac上的一款护眼软件，还有独特的`Darkroom`模式

![](http://oc98nass3.bkt.clouddn.com/15303515515539.jpg)

## HomeBrew

[Brew](https://brew.sh/)
[brew和brew cask有什么区别？](https://zhidao.baidu.com/question/396566841548150965.html)

* brew主要用来下载一些不带界面的命令行下的工具和第三方库来进行二次开发
* brew cask主要用来下载一些带界面的应用软件，下载好后会自动安装，并能在mac中直接运行。

* 使用举个例子，brew install curl可以安装curl第三方库，这样你在开发时就可以使用它的库来进行开发brew cask install chrome可以安装谷歌浏览器应用程序，可直接运行brew偏管理第三方库和命令行工具方面的东东

* brew cask可以看作是苹果官方app store的补充，是一个众多贡献者们维护的非苹果官方软件商店，你也可以在这里下mac软件用一些免费好用的mac软件没有在苹果官方app store商店上架，我们就可以在brew cask中下载。如果我要下载10个免费小软件，而这些软件没有在苹果商店上架，我们不需要一个一个去谷歌它们的官方网站，再去这些软件的官网去下载，我们统一在brew cask中下载。

* 使用brew cask来进行包管理还有一个好处，这10个免费软件如果自身不带升级功能，但现在它们有更新，我只能去官网重新下载？不，直接在brew cask里就可以统一升级。这也是你问的那句“为何网路上跟推荐用brew cask呢？”的原因。

* 如果安装mac图形界面软件，推荐先在苹果官方商店里搜索下载，没有的话去brew cask试试，如果还没有，只能去这个软件的官方网站去下载了。

* brew 装的主要是 command line tool。brew cask装的大多是有gui界面的app以及驱动，brew cask是brew的一个官方源。二者并无竞争关系，所以也不存在你说的更推荐brew cask。brew装的东西比较偏向开发，而brew cask装的东西会相对生活化一些。

## Karabiner-Elements

### Karabiner-Elements 改建

Karabiner-Elements 允许你设置多个 Profile（配置），每个 Profile 里可以有不同的键位，从而适应各异的任务。点击菜单栏图标还能快速切换配置文件，非常方便。

![](http://oc98nass3.bkt.clouddn.com/15305186914657.png)

### 与 Keyboard Maestro 的联动

实例：Hyper 键与 Keyboard Maestro 的联动

### Karabiner参考

1. 官方文档: [Manual - Karabiner - Software for macOS](https://pqrs.org/osx/karabiner/document.html)
2. [让键盘变成你想要的样子：改键利器 Karabiner-Elements - 少数派](https://sspai.com/post/42921)
3. [Control + Option + Shift + Command：带你玩转 macOS 的修饰键 - 少数派](https://sspai.com/post/39331)

### Karabiner 安装问题

现在`Karabiner-Elements`已经支持10.13了

在初次安装`Karabiner-Elements`后注意允许系统载入`Karabiner-Elements`。

![](http://oc98nass3.bkt.clouddn.com/15307715640054.jpg)
并且在设置的`安全性与隐私`中添加`Karabiner-Elements`
![](http://oc98nass3.bkt.clouddn.com/15307753758191.jpg)

注意: 设置好键位后可能遇到没有立即生效的问题，重启Mac就可以了，具体原因尚不清楚。

## Keyboard Maestro

[Keyboard Maestro](http://www.keyboardmaestro.com/main/)

> 宏（Macro，港澳台作巨集），是一种批量处理的称谓。
> 计算机科学里的宏是一种抽象（Abstraction），它根据一系列预定义的规则替换一定的文本模式。绝大多数情况下，「宏」这个词的使用暗示着将小命令或动作转化为一系列指令。

那么 Keyboard Maestro（下文简称 KM）属于什么类型的软件？我个人偏向于把它视作一个增强型 Automator。大家看截图也能发现，它的用户界面同 Automator 相似，也是传统的三栏式设计，从左到右依次是「Action 类别 > Action 名称 > Action 编辑」的有序区域切割，让用户能比较舒适地进行操作。

管理方面，KM 主要分为三个选项：+ 添加、- 删除、√ 允许/禁止。在第一次启动软件的时候，KM 会给出一个示例教程，教你去执行这三个操作，读者届时尝试的时候，只需按照提示完成所有步骤，就能大致有个「操作」的概念了。

此外，还有两个关于 KM 的名词需要大家掌握。一个叫 Macro 宏文件，我们可以将它理解为独立的 Workflow 工作流程，例如，打开 Finder 就是一个工作流程，只是概念上它仅有一个步骤罢了。另外一个名词叫做 Action 行为，例如，执行一段 AppleScript 脚本语言，或是点击一个 Button 按钮，都属于「行为」的一种。Macro 与 Action 的关系为父与子，Macro 为父，由其子 Action 组成，并最终以 Macro 的命名区分，通过用户拟定的 Trigger 触发，并按照有序的 Script 脚本语法特性，执行所有的 Action 行为。

![1](http://oc98nass3.bkt.clouddn.com/1.jpg)

比如我之前用`karabiner-Elements`的时候，把Mac的`F10`的静音键盘改成了默认的`F10`，就无法静音了。则可以用`Keyboard Maestro`添加一个覆盖快捷键

![](http://oc98nass3.bkt.clouddn.com/15305168306061.jpg)

使用过`Keyboard Maestro`后，我们需要经常问自己: 我在 Mac 上经常重复的事情是什么？有没有办法把它分解成一步步动作？这些动作有没有可能通过 `Keyboard Maestro` 来实现？

1. [Keyboard Maestro 入门指南 - 少数派](https://sspai.com/post/36442#01)
2. [Keyboard Maestro 和它的 Macro 们丨2016 与我的数字生活 - 少数派](https://sspai.com/post/37708#%E5%89%8D%E8%A8%80)
3. [Keyboard Maestro 和它的 Macro 们 | 2016与我的数字生活 - 少数派](https://sspai.com/post/36707)
[Keyboard Maestro 奇巧淫技之定期运行 - 少数派](https://sspai.com/post/43320)
3. [利用 Keyboard Maestro 做轻量级的网速监控小脚本 - 少数派](https://sspai.com/post/44793)
4. [Keyboard Maestro 小试牛刀——自动转移指定文件夹至移动硬盘 - 少数派](https://sspai.com/post/43334)
5. [我如何用 Keyboard Maestro 替代 TextExpander - 少数派](https://sspai.com/post/39495#%E5%85%B6%E5%AE%83%E5%B8%B8%E7%94%A8%E6%93%8D%E4%BD%9C)

### 快速打开常用App

对于常驻后台的 App：
 ⌥ + 字母 快捷键，精准定位到每个 App（这里替代了 Manico 和 Snap 的功能），使用习惯后，快、准且不打断思路。
 
![](http://oc98nass3.bkt.clouddn.com/15305213939492.jpg)

### 打开特定的 Finder 目录：

### 并行使用

习惯用「键盘快捷键」这块功能的用户还要留意，Keyboard Maestro 不存在「按键重叠导致失效」这一说，因为它会自动将同一快捷键下的所有 Macro 都归纳至一个独立的窗口中，用户在敲击键盘快捷键时，这个窗口就会显示，然后再按照排列顺序，点击数字键就可以运行对应的 Macro。而不是像很多快速启动类应用那样，同时执行该快捷键下的所有功能。

### Alfred插件调用

1. [Alfred-maestro:](https://github.com/iansinnott/alfred-maestro) An Alfred workflow to execute Keyboard Maestro macros.
Type km followed by the name of any of your defined macros.

## IINA

[IINA](https://lhc70000.github.io/iina/zh-cn/)

通过 Homebrew Cask 安装:`brew cask install iina`

![](http://oc98nass3.bkt.clouddn.com/15161588048779.jpg)
![](http://oc98nass3.bkt.clouddn.com/15161588526427.jpg)

##  iTerm2

[Features - iTerm2 - macOS Terminal Replacement](https://iterm2.com/features.html)

iTerm2 是 MAC 下最好的终端工具。可以简单的认为，iTerm2 是配置完毕开箱即用的 tmux。但 tmux 有以下一些缺点：

* 查找 terminal 的输出历史内容需要切换到 vim 模式。在该模式下复制使用的是 vim 的查找，增加了认知负担；
* 和各种工具兼容性比较差，尤其是 vim 和 emacs 的 powerline；
* 自有样式，与系统的样式冲突。

iTerm2 的一些特色功能如下：

## option + left←（左箭头） 跨单词移动光标的教程

方法一：

首先，打开iTerm2的Preferences设置：
然后，选择相应的Profile（默认为Default），选择“Keys”选项卡，然后可以在Key Mappings看到option+←和option+→这两组快捷键用作了其他功能，这里我们只需要重新绑定新的映射即可（下图是已经绑定之后的新映射）。
![](oc98nass3.bkt.clouddn.com/15380112903232.jpg)
![](oc98nass3.bkt.clouddn.com/15380112409124.jpg)

分别修改option+←和option+→的映射如下图所示，选择Action为“Send Escape Sequence”，然后输入“b”和“f”即可。

参考 [Mac下iTerm2光标按照单词快速移动设置 - CSDN博客](https://blog.csdn.net/skyyws/article/details/78480132)

方法二： 
~~在 `~/.zshrc` 中增加以下两行指令：~~
不适用,废弃，会影响输入
```
bindkey "[D" backward-word
bindkey "[C" forward-word
```

### 热键窗口

注册一个热键，当您在另一个应用程序中时，它会将iTerm2置于前台。终端永远是一个关键的压力。您可以选择让热键打开一个专用窗口。这为您提供了一个随时可用的终端（如Visor，Guake或Yakuake）。
![](http://oc98nass3.bkt.clouddn.com/15307837500327.jpg)

在这里设置

![](http://oc98nass3.bkt.clouddn.com/15307911440344.jpg)

比如我配置的一个HotKey

![](http://oc98nass3.bkt.clouddn.com/15307913354099.jpg)

### 标签变色

iTerm2 的标签的颜色会变化，以指示该 tab 当前的状态。当该标签有新输出的时候，标签会变成洋红色；新的输出长时间没有查看，标签会变成红色。可在设置中关掉该功能。

### 智能选中

在 iTerm2 中，双击选中，三击选中整行，四击智能选中（智能规则可配置），可以识别网址，引号引起的字符串，邮箱地址等。（很多时候双击的选中就已经很智能了）

在 iTerm2 中，选中即复制。即任何选中状态的字符串都被放到了系统剪切板中。

### 粘贴历史记录

粘贴历史记录可让您重新访问最近复制或粘贴的文本。您甚至可以选择将历史记录保存到磁盘，以免永远丢失。

![](http://oc98nass3.bkt.clouddn.com/15307836006100.jpg)

### 无鼠标复制

使用“查找”功能开始搜索文本。按Tab键将选择范围扩展到右侧，或按shift键将选择范围扩展到左侧。 Option-enter粘贴当前匹配。

![](http://oc98nass3.bkt.clouddn.com/15307836058319.jpg)

### 巧用 Command 键

按住⌘键:

可以拖拽选中的字符串；
点击 url：调用默认浏览器访问该网址；
点击文件：调用默认程序打开文件；
如果文件名是filename:42，且默认文本编辑器是 Macvim、Textmate或BBEdit，将会直接打开到这一行；
点击文件夹：在 finder 中打开该文件夹；
同时按住option键，可以以矩形选中，类似于vim中的ctrl v操作。
Meta 键
在emacs中，meta键的使用非常频繁，而 OSX 系统没有提供meta键。在 iTerm2 中可以选择左右两个的Option键作为meta键。官方推荐的配置如下图所示。右Option键依然是 OSX 的默认功能（输入特殊字符）。

![](http://oc98nass3.bkt.clouddn.com/15236296756727.jpg)

[你应该知道的 iTerm2 使用方法--MAC终端工具](http://wulfric.me/2015/08/iterm2/)


## 跨单词移动光标
Mac os中，zsh + iTerm2 中 设置 option + left←（左箭头） 跨单词移动光标的教程
在 ~/.zshrc 中增加以下两行指令：
直接输入命令
```
bindkey "[D" backward-word
bindkey "[C" forward-word
```

### 快捷命令

| 说明 | 快捷键 |
| --- | --- |
| 新建标签 | command + t |
| 关闭标签 | command + w |
| 切换标签 | command + 数字 command + 左右方向键 |
| 切换全屏 | command + enter |
| 查找 | command +f |
| 垂直分屏 | command + d |
| 水平分屏 | command + shift + d |
| 切换屏幕 | command + option + 方向键 command + [ 或 command + ] |
| 查看历史命令 | command + ; |
| 查看剪贴板历史 | command + shift + h |
| 清除当前行 | ctrl + u |
| 到行首 | ctrl + a |
| 到行尾 | ctrl + e |
| 前进后退 | ctrl + f/b (相当于左右方向键) |
| 上一条命令 | ctrl + p |
| 搜索命令历史 | ctrl + r |
| 删除当前光标的字符 | ctrl + d |
| 删除光标之前的字符 | ctrl + h |
| 删除光标之前的单词 | ctrl + w |
| 删除到文本末尾 | ctrl + k |
| 交换光标处文本 | ctrl + t |
| 清屏1 | command + r |
| 清屏2 | ctrl + l |

####  Mac搭配SSR客户端实现终端走代理

有时候你会发现git clone非常慢，或者brew install非常慢，但是你明明开了代理，即使设置全局代理也不行，那是因为终端或者iTerm2默认是不走代理的，

##### 切换镜像源方法

借用豆瓣的镜像源：

```
pip install {PACKAGE_NAME} -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com
```

如果还有权限问题就加上`sudo`

##### 配置方法

这个时候，解决方法如下：
终端输入

```
    // 让终端走代理，前提是你购买了SSR服务，或者自己搭建了SSR服务
    // 这里的1087是大多数使用 ShadowsocksX-NG 版本 1.4.3-R8 (3) 的端口
    // 少部分使使用其他版本的需要注意修改下
    ➜  ~ export http_proxy=http://127.0.0.1:1087;export https_proxy=http://127.0.0.1:1087;
    // 输入下面命令如果没什么信息输出，则开启成功
    ➜  ~ curl pub.dartlang.org

```

如果想每次开机启动，那么执行如下面命令

```
   ➜  ~ open -e .bash_profile

```

打开文件后，将下面的命令复制到 .bash_profile 里面

```
   # iTerm2 proxy
   export http_proxy=http://127.0.0.1:1087
   export https_proxy=http://127.0.0.1:1087

```

然后再执行

```
  ➜  ~ source ~/.bash_profile
```


I was just trying to do exactly the same :-). Here you go, using AppleScript and bit of bash if you like.

```
--this goes inside for example bgImgIterm.scpt--
tell application "iTerm2"
  tell current session of current window
    set background image to "/path/to/img/img.jpg" 
  end tell
end tell
then you can run it inside bash like

```

```
#!/bin/bash
osascript /path/to/scpt/bgImgIterm.scpt

```
[terminal - iTerm2 (OS X) change background image for current window from shell? - Super User](https://superuser.com/questions/1068105/iterm2-os-x-change-background-image-for-current-window-from-shell/1128149#1128149)

### iTerm2参考

1. [Features - iTerm2 - macOS Terminal Replacement](https://iterm2.com/features.html)
2. [MAC上iTerm 2安装与使用 - 掘金](https://juejin.im/post/5a815edd5188251c85636034)
3. [iTerm2 指南 | 小土刀](https://wdxtub.com/2016/03/20/iterm2-guide/)
 
## LaunchCenterPro

[iOS 8 Widget Customisations using Launcher | MacRumors Forums](https://forums.macrumors.com/threads/ios-8-widget-customisations-using-launcher.1782093/)

### 自定义iOS11设置的UrlSchemes

> Unfortunately, Apple blocked apps from opening the Settings app to specific settings (such as WiFi, Hotspot, Battery, etc.). We’ve requested that Apple re-enable these shortcuts, but it’s unlikely they will.

### PWA

PWA（Progressive Web Apps）是由 Google 提出的下一代 Web 应用模型，让你能在网页中获得不亚于原生 App 的体验。目前，包括 iOS、Android、Chrome、Firefox 等在内的各主流平台均已添加了相关支持。

如果你经常访问的网站支持 PWA 技术，添加到 Launchpad 后就与普通应用无异，不会显示地址栏、工具按钮等，且能即时推送通知，轻量简洁。

据我所知，国内目前支持 PWA 的主流服务有 [微博](https://m.weibo.cn/beta "微博")、[豆瓣](https://m.douban.com/ "豆瓣")、[哔哩哔哩](https://m.bilibili.com/ "哔哩哔哩")、[腾讯新闻](https://xw.qq.com/ "腾讯新闻")、[饿了么](https://h5.ele.me/ "饿了么")、[飞猪](https://h5.m.taobao.com/trip/home-pwa/index.html "飞猪")、[百度糯米](https://mdianying.baidu.com/ "百度糯米")、[百度天气](https://weatherpwa.baidu.com/ "百度天气") 等。关于国外服务的适配情况，你可以参照 GitHub 的 [awesome-pwa](https://github.com/hemanth/awesome-pwa "awesome-pwa") 项目。

#### Chrome配置PWA

首先更新你的Chrome版本到64或以上。

然后在地址栏输入`chrome://flags`，找到`Desktop PWAs`的选项将其`Enabled`了，然后Chrome会提示你重启浏览器。
![](http://oc98nass3.bkt.clouddn.com/15238171164510.jpg)

## Moke

[最纯粹的微博体验：墨客 2 评测](https://sspai.com/post/25701)

### Moke feature

* 没有weibo的广告和垃圾推荐
* 多种主题
* 图片模式
* 手势操作支持，左右短滑动进行转发和评论，左右长滑进行查看转发和评论
* 多账号切换
* 「全部微博、原创微博、图片微博」三种模式下进行切换
* 发布微博，下拉关闭键盘⌨️，进入预览模式
* 长按展开表情按钮可以连续输入多个表情
* 长按用户头像可以私信，拷贝昵称和`@`操作
* 长按微博可以进行分享
* 搜索：进入搜索后输入一个关键词，应用会优先将已加载的微博列表中，符合关键词的结果实时显示出来


墨客一直都遵从着苹果官方的交互规范，这在新的墨客2 中体现得更加淋漓尽致。于是新版彻底摒弃了墨客1 中的底栏滑动返回，全面采用 iOS 7 标准的边缘滑动返回。其他几处新增的交互操作中也都使用了 iOS 默认的交互方式，所以无论你是新用户还是老用户，都能很快适应。即便你是啥都不懂的小白，墨客2 适时出现的操作提示，能很好地手把手教你上手它。这种边用边熟悉的教学方式，要比一股脑一下子全部塞给你更加容易记住。

![](http://oc98nass3.bkt.clouddn.com/15308640901607.png)

## Mubu 幕布


### 幕布快捷键

![](http://oc98nass3.bkt.clouddn.com/15358997976218.jpg)

![](http://oc98nass3.bkt.clouddn.com/15358998067113.jpg)

## Mweb

[Mweb](http://www.mweb.im/)

![](http://oc98nass3.bkt.clouddn.com/15194631251558.jpg)

在Mac上无疑是`markdown`书写的利器，搭配上图床和快捷键，让你的文章书写的非常好看。

Mac下有外部模式和文档库模式
![](http://oc98nass3.bkt.clouddn.com/15194631444347.jpg)

`Mweb`也推出了iOS版本，样式主题很好看
![](http://oc98nass3.bkt.clouddn.com/15194631548163.jpg)

`Tomorrow`的主题很好看
![](http://oc98nass3.bkt.clouddn.com/15194631656182.jpg)

###  Mweb For Mac

![](http://oc98nass3.bkt.clouddn.com/15301825676551.jpg)

#### Mweb3.0 For Mac 快速定位焦点
 
1. 最新V3.1.1版本是通过快捷键 `⌘ + ⇧ + F` 把焦点切换至搜索框（外部模式切换到目录树）。只记这一个，基本就可以在 `目录树 - 列表 - 编辑器` 这三处随意切换了。
这是因为，在搜索框按 `Tab 键` 可以切换到编辑器，按 `向下键` 可以切换到列表。焦点在列表时，按 `向左键` 切换到目录树，`向右键` 切换到编辑器；焦点在目录树时，可以按 `向右键` 切换到列表。另外切换 Tabs 可以使用 `⌃ + ⇥` 键，`⌘ + ⇧ + [` or `⌘ + ⇧ +]` 键，切换 Tab时焦点会切到编辑器。目录树可以使用Enter键控制展开和收缩。

2. 另外还有快速搜索是 `⌘ + O`，外部模式没有搜索框时，可以使用这个来进行搜索。

3. 有个小技巧，如果文章Markdown太长，**可以通过Mweb的目录进行定位**, 可以使用`⌘ + 7`调起目录，然后输入目录对应的搜字母，使用上下进行切换。

### Mweb Alfred WorkFlow

[alfred-mweb-workflow](https://github.com/tianhao/alfred-mweb-workflow)搜索、打开MWeb 内部文档和外部文档

### MWeb问题

1. 图片无法预览

Q：最近版本的`Mweb`在图片成功上传的图床后，无法预览
A: 检查后发现，上传成功后的url需要添加`http://`协议才行。
于是我把图床的默认域名添加上`http://`
![](http://oc98nass3.bkt.clouddn.com/15383768466706.jpg)


### 常用快捷键（整理）

#### 模式

 名称 | 快捷键
 --- | ---
1.  外部模式      |      `⌘ + E`
2.  文档库模式     |     `⌘ + L`

#### 编辑器

 名称 | 快捷键
 --- | --- 
3.  切换主题        |       `⌘ + ⌥ + L`
4.  显示编辑器       |       `⌘ + 1`
5.  显示文件夹目录   |       `⌘ + 2`
6.  文档预览        |      `⌘ + 4`
7.  文档目录        |      `⌘ + 7`
8.  文档属性        |      `⌘ + 8`
9.  文档导出        |      `⌘ + 9`
10. 标签切换        |      `⌘ + ⇧ + { or }`
11. 焦点于编辑器     |      `⌘ + ⇧ + E`
12. 焦点于搜索框     |      `⌘ + ⇧ + F`

#### 文本编辑

 名称 | 快捷键
 --- | ---
13. 行内代码      |         `⌘ + K`
14. 代码块        |        `⌘ + ⇧ + K`
15. 设置标题      |         `⌃ + 1~6`
16. 无序列表      |         `⌃ + U`
17. 加粗          |       `⌘ + B`
18. 高亮          |       `⌘ + =`
19. 注释          |       `⌘ + /`
20. 注释More      |       `⌘ + .`
21. 新段落        |        `⌘ + ↵`
22. 表格          |       `⌃ + ⇧ + T`
23. 引用          |       `⇧ + ⌘ + B`
24. 表情符号       |      `⌃ + ⌘ + 空格`

#### 图片链接

 名称 | 快捷键
 --- | ---
22. 添加图片    |     `⌃ + ⇧ + I`
23. 上传图片    |       `⌘ + ⌥ + I`
24. 链接       |     `⌃ + ⇧ + L`
25. 表格       |      `⌃ + ⇧ + T`


### `Markdown`空格和换行

在用Markdown有时候需要额外添加空格和换行,怎么办呢？使用`Html`的代码吧。

* 换行
`&nbsp;`
`<br />`
*  空格
`&emsp;`


### Mweb参考文档： 

* [MWeb 3.0 测试版终于发布了！欢迎大家试用！](http://zh.mweb.im/mweb3.0-on-test.html)
* [Mweb使用文档 - MWeb](http://zh.mweb.im/docs.html)
* [Mweb-iOS使用文档 ](http://zh.mweb.im/introducing-mweb-for-ios.html)

## Reeder

### Reeder快捷键

![](http://oc98nass3.bkt.clouddn.com/15304367190074.jpg)
![](http://oc98nass3.bkt.clouddn.com/15304367388538.jpg)

 命令 | 说明 
 --- | --- 
⌘ ，      | Preferences...
⌥ ⇧ ⌘ 9   | Add to Things
⌃ ⌥ ⇧ ⌘ C | Convert Text to Simplified Chinese
 ⌘ ，      | Preferences...
⌥ ⇧ ⌘ 9   | Add to Things
 ⇧ ⌘ Y | Make New Sticky note


## Rime

> 有关“Rime鼠须管”输入法，在各类MAC相关的论坛上都能看到“神级输入法”这样标题的推荐，必须承认仅仅就速度这个角度来说，确是非常优秀，输入过程非常流畅毫无卡钝，当然做为开源软件，作者的思路应该是：字库无需非常庞大，字库是靠用户用自己的输入习惯来“养成”的。

### Rime安装

[Github开源地址](https://link.jianshu.com?t=https://github.com/lotem/squirrel)

Rime 官网：[http://rime.im/](https://link.jianshu.com?t=http://rime.im/)

或者可以去官网下载 Homebrew Cask 来安装(我就是用这个来安装的)

```
brew cask install squirrel

```

ps:刚安装好，拼音输入是繁体的，在终端 Iterm 按组合键 Ctrl+` 呼出输入法方案选单（如下），切换为「汉字」就可以输入简体了

#### 配置

数据文件位置

> 共享资料夹：”/Library/Input Methods/Squirrel.app/Contents/SharedSupport/”
> 用户资料夹：”~/Library/Rime/”

用户资料夹内的文件说明如下

> 〔全局设定〕 default.yaml
> 〔发行版设定〕 weasel.yaml
> 〔预设输入方案副本〕 <方案标识>.schema.yaml
> ※〔安装信息〕 installation.yaml
> ※〔用户状态信息〕 user.yaml
> 编译输入方案所产生的二进制文件：

> 〔Rime 棱镜〕 <方案标识>.prism.bin
> 〔Rime 固态词典〕 <词典名>.table.bin
> 〔Rime 反查词典〕 <词典名>.reverse.bin
> 记录用户写作习惯的文件：

> ※〔用户词典〕 <词典名>.userdb.kct
> ※〔用户词典快照〕 <词典名>.userdb.txt、<词典名>.userdb.kct.snapshot 见于同步文件夾
> 以及用户自己设定的：

※〔用户对全局设定的定制信息〕 default.custom.yaml
※〔用户对预设输入方案的定制信息〕 <方案标识>.custom.yaml
※〔用户自制输入方案〕及配套的词典源文件
注：以上标有「※ 号」和「粗体」的文件，包含用户资料，您在清理文件时要注意备份！

### 双拼

[和我们一起学双拼，码字再快一点 - 少数派](https://sspai.com/post/40883)



## ShadowSocket

打开[portfolio-preview](https://ss.freess.org/#portfolio-preview) ,然后你会看到这个界面

随便点一个地址,然后会弹出个二维码，像下面这样，注意右上角，点那个纸飞机，找到那个从屏幕上扫描二维码，注意要选那个**自动代理模式**，windows 的就选 **系统代理模式**

![](http://oc98nass3.bkt.clouddn.com/15343299529861.jpg)
ss 备用网址,如果上面的二维码扫了不能用，试试下面这些
* [freeSS](https://get.ss8.fun/)

## SimpleRead 简悦

`Chrome`的阅读模式
[simpread](https://github.com/kenshin/simpread/wiki)    
![](http://oc98nass3.bkt.clouddn.com/15303554126923.jpg)


### 阅读模式与聚焦模式

![](http://oc98nass3.bkt.clouddn.com/15303549034647.jpg)

* 阅读模式:独有功能，自动提取适配页面的标题、描述、正文、媒体等资源。支持临时阅读模式. TXT阅读模式.主动适配模式.智能适配模式.论坛类页面/分页。

* 聚焦模式:高亮鼠标所在的文章段落，不改变当前页面的结构，适合未适配的网站。

### 连接工具

* 支持下载HTML . PDF . Markdown . PNG . Epub到本地以及发送到Kindle。
* 支持输出到Dropbox，印象笔记. Evernote . Onenote . Google云端硬盘。
* 发送页面链接到Pocket . Instapaper . Linnk, 详细请看这里[授权服务 · Kenshin/simpread Wiki](https://github.com/Kenshin/simpread/wiki/%E6%8E%88%E6%9D%83%E6%9C%8D%E5%8A%A1)

![](http://oc98nass3.bkt.clouddn.com/15303548876578.jpg)

### 站点编辑器

站点编辑器.站点适配源.站点管理器
页面上任意元素均可隐藏，更支持编程，详细请看站点编辑器
更灵活、社区化的多种站点适配源。
内置了站点管理器，方便管理全部的适配站点。

[站点编辑器 · Kenshin/simpread Wiki](https://github.com/Kenshin/simpread/wiki/%E7%AB%99%E7%82%B9%E7%BC%96%E8%BE%91%E5%99%A8)

## Steward

[Steward 简介](http://oksteward.com/steward-document-zh/plugins/browser/Top%20Sites.html)

说到启动器，最有名的当属 Mac 上的神器 Alfred ，以及 Windows 上的 Wox。那什么是启动器呢，它是由一个命令输入框，以及一个查询结果下拉列表组成。只需要一个命令就能让电脑去完成一系列操作，如同你的管家一样，自然是很多人心目中的神器。

比如我输入 Chrome 然后回车，启动器会自动帮我找到 Chrome 并打开它；又如遇到命令 yd steward 后，启动器立刻去查询有道词典然后把 管家 的释义列出来。

而 Steward 便是 Chrome 浏览器里的类 Alfred 启动器，在某些方面甚至是 Alfred Plus。

v3.1.2到来的 random 插件，看似不起眼，却使 Steward 超越了传统的「New Tab」类扩展，新标签不再仅仅只是一个花瓶，比如它可以同时扮演 TodoList、书签管理、背单词等角色。

![Steward 功能图示](http://oc98nass3.bkt.clouddn.com/15130587658701.png)
Steward 是个人的第一个开源项目，因而从开源社区学习到了很多东西。

技术栈：Webpack + Vue2，当然也有 jQuery、pinyin 这样的库
设计：不懂设计，怎么办呢？设置页面用的 ElementUI，图标大都来自 iconfont.cn
产品：从简悦以及其它一些优秀的开源项目学习了怎么维护一个产品。当然目前 Steward 还做得不够

##  Sublime Text 3 

1. [Sublimetext-markdown-preview:](https://github.com/revolunet/sublimetext-markdown-preview)
2. [SublimeText-Markdown/MarkdownEditing.](https://github.com/SublimeText-Markdown/MarkdownEditing#package-control): Powerful Markdown package for Sublime Text with better syntax understanding and good color schemes

[Sublime Text 3 for Mac 安装和插件配置说明 – 老柴的宅](http://chaishiwei.com/blog/892.html)

### 主要快捷键

``⌘ + ⇧ + P`

刚才已经介绍过了，打开 Package Control 命令面板，支持模糊搜索。

`⌘ + P`

根据文件名打开文件。比如想打开`~/Sites/index.html`，你只要在输入框中输入`~/Sites/index.html`即可，支持模糊匹配，比如~/index。

`⌘ + R`

查找函数。比如输入log，能找到所有名带 log 的方法，输入 loginout，则能定位到 loginout()。输入框中自动出现的 @ 符号，就是要匹配方法的意思。

定位到行：`⌘ + G`，或`⌘ + P`后，在框中输入:行数，如:58，则要跳转到58行去。

查找标识:`⌘ + P`后，#标识。

`⌘ + D`

同时修改多个相同代码。先选中一段要修改的代码，然后`⌘ + D`，会向下连选相同的那段代码，重复，直到满意为止。虽然「查找/替换」功能可以做到同样的效果，不过此种操作方法更直观和可控。

`⌘ + F`

查找搜索。这个就不多介绍了吧：

回车查找下一个，`⇧ + ↵`，查找上一个。
`⌘ + H`，查找替换。
`⌘ + ⇧ + F`，可以叫全项目查找，就是在当前打开的项目中，根据所输入的字符进行查找搜索。

#### 基本编辑（Basic Editing）

```
⇣⇡⇠⇢ 就是 ⇣⇡⇠⇢，不是 KJHL。

⌘ Command() 
⌃ Control 
⌥ Option(alt) 
⇧ Shift 
⇪ Caps Lock(大写) 
fn 功能键就是fn 
↩︎ return/↵
```

`⌃ + ↩︎ or ↩︎` 当前行下面新增一行然后跳至该行； 
`⌃ + ⇧ + ↩︎` 当前行上面增加一行并跳至该行； 
`⌥ + ⇠/⇢` 进行逐词移动，相应的； 
`⌥ + ⇧ + ⇠/⇢` 进行逐词选择； 
`⌘ + ⇣/⇡` 移动到首行/尾行； 
`⌘ + U` 返回到历史光标位置(撤销)； 
`⌃ + M` 可以快速的在起始括号和结尾括号间切换； 
`⌃ + ⇧ + M` 则可以快速选择括号间的内容； 
`⌃ + ⇧ + J` 对于缩进型语言(例如Python)则可以使用； 
`⌃ + ⌘ + D` 复制整行；

选择（Selecting）
`⌘ + D` 选择当前光标所在的词并高亮该词出现的所有位置； 
再次 `⌘ + D` 选择该词出现的下一个位置； 
使用 `⌘ + U` 进行回退，使用Esc退；

`⌘ + K + K` 从光标处删除到行末尾； 
`⌃ + K` 同上 `⌘ + KK`

进行同时编辑，`⌃ + ⇧ + L` 可以将光标移动到每行的结束

`⌘ + ⇧ + ⇠` 选择光标到这一行第一个字符出现的位置 
`⌃ + ⇧ + A` 选择光标到这一行最前面的(包括缩进)位置

代码展开
`⌃ + K0` 代码展开

改为大写或者小写
`⌃ + KL` 改为小写 
`⌃ + UK` 改为大写

合并
`⌘ + J` 可以把当前选中区域合并为一行

跳转指定行
`⌃ + G `然后输入行号以跳转到指定行：

组合跳转
`⌘ + P` 我们可以进行后续输入以跳转到更精确的位置： 
`@` 符号跳转：输入 @symbol 跳转到symbol符号所在的位置 
 `#` 关键字跳转：输入 #keyword 跳转到keyword所在的位置 
`:` 行号跳转：输入 :12 跳转到文件的第12行。

启动终端(Terminal插件)
`⌃ + ⌘ + T`

设置启动 iTerm 
打开配置文件 `preferences > Package Setting > Terminal > Setting - Default `
设置 "terminal": "iTerm.sh"

默认打开侧边栏
`⌘(⌃) + k -> b`。 

### 安装Package Control插件

[Mac OS上sublime text 3的安装与配置 - tabalt的博客](http://tabalt.net/blog/install-sublime-text-3-on-mac/)

安装`Package Control`是扩展你的sublime的第一步，可以通过Package Control很方便的安装其他插件。最简单的安装方式是按 ⌃ + ` ，然后在下方弹出的输入框中输入如下代码并回车：

```
  import urllib.request,os,hashlib; h = '2915d1851351e5ee549c20394736b442' + '8bc59f460fa1548d1514676163dafc88'; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); by = urllib.request.urlopen( 'http://packagecontrol.io/' + pf.replace(' ', '%20')).read(); dh = hashlib.sha256(by).hexdigest(); print('Error validating download (got %s instead of %s), please try manual install' % (dh, h)) if dh != h else open(os.path.join( ipp, pf), 'wb' ).write(by)
```
不出意外的话，`Package Control`就会安装成功。如果你不知道是否安装成功，可以查看是否存在菜单 `Preferences > Package Control`，存在则已经正确安装；或者按`⇧ + ⌘ + p`。 如果你的版本不是 3，或者安装有问题，可以查看Package Control的官网上的安装教程：
[Installation - Package Control](https://sublime.wbond.net/installation)  
Manual
If for some reason the console installation instructions do not work for you (such as having a proxy on your network), perform the following steps to manually install Package Control:

* Click the Preferences > Browse Packages… menu
* Browse up a folder and then into the Installed Packages/ folder
* Download Package Control.sublime-package and copy it into the Installed Packages/ directory
* Restart Sublime Text

### 安装`markdown preview`插件

`markdown preview`是sublime下预览markdown文件的插件，按`⇧ + command + p`打开我们前面安装的Package Control插件的面板，输入install然后回车，在弹出的面板输入markdown preview再回车，即可完成安装。
安装`SidebarEnhancements`插件
`SidebarEnhancements`是增强侧边栏的插件，安装方法同上。

## Surfingkeys

> [Surfingkeys](https://chrome.google.com/webstore/detail/surfingkeys/gfbliohnnapiefjpjlpjnehglfpaknnc)是Chrome上的一个神器，开发者将Chrome上常用的操作封装成快捷键，使用后，感觉比[Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en)还要好用。
> Map your keys for web surfing, expand your browser with javascript and keyboard.

文档：[Surfingkeys/README_CN.md at master · brookhong/Surfingkeys](https://github.com/brookhong/Surfingkeys/blob/master/README_CN.md)

Surfingkeys有三种模式：normal，visual和insert。

* Normal mode，默认模式,当你打开一个页面时，自动进入该模式。通过函数mapkey添加的所有按键都只在这种模式下有用。
* Visual mode，用于选中文本，以及各种针对选中文本的操作
* Insert mode，当输入焦点定位到各类输入框时（无论你是通过i或f选择定位还是鼠标点击定位的），就进入该模式。 通过函数imapkey添加的所有按键都只在这种模式下有用。

### 可视模式

可视模式步骤：

1. 通过`v`进入可视模式,确认你能看到`Caret`提示和光标
2. 选择切入文本, 使用`j` `k` `h` `l` `b` `w``0` `$`试试移动光标。
3. 通过`v`进行选择文本
4. 其实选择文本可以通过`ymv`进行多个文本的复制

*   `zz` 让光标位于窗口中间行。
*   `f` 往前查找下一个字符。
*   `F` 往后查找下一个字符。
*   `;` 重复最后的`f`/`F`操作。
*   `,` 反向重复最后的`f`/`F`操作。


 名称 | 快捷键 
  :-: | :-: 
进入可视模式，并全选指定文本 |  zv
选择复制多个指定文本 | ymv
选择复制指定文本 | yv
切换可视模式 | v
恢复可视模式 | V
跳到行首 | 0
前进一个字符 | l
后退一个字符 | h
下一行 | j
上一行 | k
前进一个单词 | w
前进一个单词 | e
后退一个单词 | b
前进一个句子 | )
后退一个句子 | (
前进一个段落 | }
后退一个段落 | {
跳到行尾 | $
跳到页面结尾 | G
跳到页面开头 | gg
跳到页面结尾 |  o
点击光标下的元素 | <'Enter'>
把光标所在的位置放在屏幕中间 | zz
选中一个单词(w)／行(l)／句子(s)／段落(p) | V
复制一个单词(w)／行(l)／句子(s)／段落(p) | y
往上20行 | <'Ctrl-u'>
向下20行 | <'Ctrl-d'>
| **查找** |  |
在当前页查找 | /
在当前页查找选中文本 | *
下一处 | n
上一处 | N
查找光标下的单词 | *
重复相应的f/F | ;
往前查找字符 | f
往后查找字符 | F
反向重复相应的f/F | ,
| **其他** |  |
电脑语音阅读选中文本 | gr
翻译光标下的单词 | q

### 插入模式

 名称 | 快捷键 
  :-: | :-: 
把光标放到行尾 | <Ctrl-e>
把光标放到行首 | <Ctrl-f>
删除光标前的所有字符 | <Ctrl-u>
把光标往后移一个单词 | <Alt-b>
把光标往前移一个单词 | <Alt-f>
删除光标前一个单词 | <Alt-w>
删除光标后一个单词 | <Alt-d>
退出插入模式 | <Esc>
输入字符表情: | <Ctrl-'>
给当前输入加双引号 | <Ctrl-'>
打开VIM编辑器编辑当前输入 | <Ctrl-i>
给当前输入加双引号 | <Ctrl-'>

### 普通模式

| 名称 | 快捷键 |
| :-: | :-: |
| **打开连接** |  |
| 在新标签页后台打开链接 | gf |
| 在新标签页打开多个链接 | cf |
| 在新标签页打开链接 | af |
| 打开链接，如果拨号键有重叠按SHIFT | f |
|  打开文字中的超级链接  | O |
| 打开选中的网址或系统剪贴板里的网址 | cc |
| 复制链接 | ya |
| 复制当前页标题 | yl |
| 选择复制制定文本 | yv|
| 复制当前地址 | yy |
| 当前页后退 | S | 
| 当前页前进 | D | 
| 刷新当前页 | r | 
| 跳到当前地址的根路径 | gU |
| **标签页** |  |
| 跳到最早的那个标签页 | gT |
| 跳到最新的那个标签页 | gt |
| 选择标签页 | T |
| 复制当前标签页 | yt |
| 打开新标签 | on |
| 把当前标签页移入新窗口 | W |
|  往左移动当前标签页 | << |
| 往右移动当前标签页 |  >> |
| **搜索** |  | 
| 打开网页 | t | 
| 打开搜索栏查找当前标签页访问过的所有网址 | H | 
|  跳到第一个输入框 | gi |
| **文本** |  |
| 用stackoverflow搜索选中文本 | ss |
| 用百度搜索选中文本 | sb |
| 用谷歌搜索选中文本 | sg |
| **滚动** |  |
| 切换滚动目标 |  |
| 滚到最上边 | gg |
| 滚到最下边 | G |
| **其他** |  |
| 用谷歌翻译选中文本 | ;t |
|  电脑语音阅读选中文本或剪贴板里的文本  | gr |
| 删除30天前的所有访问历史记录  | ;dh | 
| 截屏 | yg | 
| 截长屏 | yG | 
| 退出Chrome | ZQ |
| 保存会话并退出 | ZZ |
| 恢复最近一次会话 | ZR |
| 显示最近一次操作 | sql |
| 重复最近一次操作 | . |
| **Chrome内置功能** |  |
| 打开收藏夹 | gb |
| 打开下载 | gd |
| 打开历史记录 |  gh |
打开扩展 | ge |

非常高效有木有，心里禁不住为作者喝彩，感谢作者~
还有可视模式，和插入模式，还没有深入的使用

### 打开连接

默认的拨号键有asdfgqwertzxcvb，如果按了一个非拨号键，会自动退出拨号。下面的设置可以改成右手习惯：

```
Hints.characters = 'yuiophjklnm'; // for right hand

```

**当拨号盘有重叠上，可以按Shift翻转重叠的拨号盘。按住空格键可隐藏拨号盘，松开恢复。**

### vim编辑器

用vim编辑器编辑textarea


## Surge

参考[Surfingkeys-Chrome神器](https://github.com/FrizzleFur/AwesomeTools/blob/master/Awesome%E6%95%88%E7%8E%87%E7%A5%9E%E5%99%A8/Surge%E7%BD%91%E7%BB%9C%E8%AF%B7%E6%B1%82%E8%BF%87%E6%BB%A4%E7%A5%9E%E5%99%A8.md)

## Tampermonkey 油猴

1. [简书实时生成侧边目录 - CSDN博客](https://blog.csdn.net/Wonder233/article/details/78558307)

查看简书文章页面的源码，可以发现所有的标题行都放在h1,h2,h3,h4,h5,h6 标签内，所以将页面设计成在文章左侧插入列表, 按标题层级进行缩进，点击进行跳转。 
将下面的代码贴进编辑器即可。

![](http://oc98nass3.bkt.clouddn.com/15234427040981.jpg)

```
// ==UserScript==
// @name         简书目录
// @description:zh-cn 自动生成简书目录
// @namespace    http://www.jianshu.com/u/c887880e8f06
// @version      1.0
// @description  create content
// @author       Wonder233
// @match        http://www.jianshu.com/p/*
//// @require      http://code.jquery.com/jquery-latest.js
// @grant        none
// ==/UserScript==
var menuIndex = 0; //初始化标题索引

// 在侧边栏中添加目录项
function appendMenuItem(tagName,id,content){
    console.log(tagName+" "+tagName.substring(1));
    let paddingLeft = tagName.substring(1) * 30; //添加标题缩进
    $('#menu_nav_ol').append('<li class="' + id +'" style="padding-left: '+ paddingLeft +'px;"><b>' + content + '</b></li>');
}

(function() {
    'use strict';
    // 使文章区域宽度适配屏幕
    let wider = $('.note').width() - 400;
    let oriWidth = $('.post').width();
    console.log(wider);
    console.log(oriWidth);
    if (wider < oriWidth){
       wider = oriWidth;
    }
    // 适配宽度
    $('.post').width(wider);

    // 保存标题元素
    let titles = $('body').find('h1,h2,h3,h4,h5,h6');
    if(titles.length === 0){
        return;
    }
    // 将文章内容右移
    $('.post').css('padding-left','200px');
    // 在 body 标签内部添加 aside 侧边栏,用于显示文档目录
    let contentHeight = window.innerHeight; //设置目录高度
    let asideContent = '<aside id="sideMenu" style="position: fixed;padding: 80px 15px 20px 15px;top: 0;left: 0;margin-bottom:20px;background-color: #eee;background-color: #eee;z-index: 810;overflow: scroll;max-height:'+contentHeight+'px;min-height:'+contentHeight+'px;min-width:350px;max-width:350px;"><h2>目录<h2></aside>';
    $('.show-content').prepend(asideContent);
    $('#sideMenu').append('<ol id="menu_nav_ol" style="list-style:none;margin:0px;padding:0px;">');// 不显示 li 项前面默认的点标志, 也不使用默认缩进

    // 遍历文章中的所有标题行, 按需添加id值, 并增加记录到目录列表中
    titles.each(function(){
          let tagName = $(this)[0].tagName.toLocaleLowerCase();
          let content = $(this).text();
          // 若标题的id不存在,则使用新id
          let newTagId =$(this).attr('id');
          if(!$(this).attr('id')){
              newTagId = 'id_'+menuIndex;
              $(this).attr('id',newTagId);
              menuIndex++;
          }
          if(newTagId !=='id_0') //忽略标题
              appendMenuItem(tagName,newTagId,content);
    });

    $('#sideMenu').append('</ol>');
    // 绑定目录li点击事件,点击时跳转到对应的位置
    $('#menu_nav_ol li').on('click',function(){
        let targetId = $(this).attr('class');
        $("#"+targetId)[0].scrollIntoView(true);
    });
})();
```
## TextExpander

[TextExpander](http://smilesoftware.com/TextExpander/index.html) 已算是 Mac 平台必装的一款效率类软件，它能将那些需要重复输入的内容（Content）保存，并给其预设一个缩写词（Abbreviation），当下次需要时，你只需输入设定好的缩写词就会自动展开缩写词，获得完整的文本内容。而 [Markdown](http://zh.wikipedia.org/wiki/Markdown) 这种轻量级的「标记语言」也越来越多的被写作爱好者、撰稿者广泛使用。

TextExpander>首选项>同步>“TextExpander 5（Dropbox使用同步）。”
退出TextExpander
再次运行TEIMPrefsetter
将中文删除即可。
![](http://oc98nass3.bkt.clouddn.com/15077128291686.jpg)

![](http://oc98nass3.bkt.clouddn.com/15077128657833.jpg)
这时再运行 TEIMPrefSetter.app 便不会再报错，删除 zh-中文这项，保存，重新运行 TextExpander 就 OK 了。

1. [Five Ways to Automate Your Day One Journal with TextExpander | Day One](http://dayoneapp.com/2017/01/five-ways-to-automate-your-day-one-journal-with-textexpander/)

![](http://oc98nass3.bkt.clouddn.com/15182603864500.jpg)

![](http://oc98nass3.bkt.clouddn.com/15182604041517.jpg)

## Things3

### Things3的Mac快捷键

#### Create new items

| 快捷键| 说明|
| --- | --- |
| ⌘ Cmd + N | Create a new to-do |
| Space | Create a new to-do below selection |
| ⌘ Cmd + V | Paste plain text to create new to-dos |
| ⌘ Cmd + ⇧ Shift + C | Create a checklist in an open to-do |
| ⌘ Cmd + ⇧ Shift + N | Create a new heading in a project |
| ⌘ Cmd + ⌥ Opt + N | Create a new project |
| Ctrl + Space | Open [Quick Entry](https://support.culturedcode.com/customer/portal/articles/2803569#quickly-add-new-to-dos) |
| ⌥ Opt + Ctrl + Space | Open [Quick Entry with Autofill](https://support.culturedcode.com/customer/portal/articles/2803569#changing-the-keyboard-shortcut-for-quick-entry) |

#### Edit items

| 快捷键| 说明|
| --- | --- |
| ↩ Return | Open a to-do or project |
| ⌘ Cmd + ↩ Return | Save and close |
| Esc | Save and close |
| ⌘ Cmd + D | Duplicate a to-do or project |
| ⌘ Cmd + C | Copy a to-do or project |
| ⌘ Cmd + V | Paste a to-do or project |
| ⌘ Cmd + . | **Complete selected items** |
| ⌘ Cmd + ⌥ Opt + . | **Cancel selected items** |
| Delete | Delete selected items |
| ⌘ Cmd + L | **Move completed to Logbook** |

#### Select items

| 快捷键| 说明|
| --- | --- |
| ↑ | Select item above |
| ↓ | Select item below |
| ⇧ Shift + ↑ | Extend selection upwards |
| ⇧ Shift + ↓ | Extend selection downwards |
| ⌥ Opt + ⇧ Shift + ↑ | Extend selection to the top |
| ⌥ Opt + ⇧ Shift + ↓ | Extend selection to the bottom |
| ⌘ Cmd + A | Select everything |

#### Move items

| 快捷键| 说明|
| --- | --- |
| ⌘ Cmd + ⇧ Shift + M | Move selection to another list |
| ⌘ Cmd + ⌥ Opt + V | Move copied to-dos and projects |
| ⌘ Cmd + ↑ | Move selection up |
| ⌘ Cmd + ↓ | Move selection down |
| ⌘ Cmd + ⌥ Opt + ↑ | Move selection to top of list |
| ⌘ Cmd + ⌥ Opt + ↓ | Move selection to bottom of list |

#### Edit dates

| 快捷键| 说明|
| --- | --- |
| ⌘ Cmd + S | Show Jump Start |
| ⌘ Cmd + T | Start Today |
| ⌘ Cmd + E | Start This Evening |
| ⌘ Cmd + R | Start Anytime |
| ⌘ Cmd + O | Start Someday |
| Ctrl + ] | Start date +1 day (Help) |
| Ctrl + [ | Start date -1 day (Help) |
| Ctrl + ⇧ Shift + ] | Start date + 1 week (Help) |
| Ctrl + ⇧ Shift + [ | Start date - 1 week (Help) |
| ⌘ Cmd + ⇧ Shift + D | Direct access to set a Deadline |
| Ctrl + . | Deadline +1 day |
| Ctrl + , | Deadline -1 day |
| Ctrl + ⇧ Shift + > | Deadline +1 week (Help) |
| Ctrl + ⇧ Shift + < | Deadline -1 week (Help) |
| ⌘ Cmd + ⇧ Shift + R | Make to-do or project repeating |

#### Control windows

| 快捷键| 说明|
| --- | --- |
| ⌘ Cmd + Ctrl + N | Open new window |
| ⌘ Cmd + ⇧ Shift + ` | Cycle through open windows |
| ⌘ Cmd + W | Close current window |
| ⌘ Cmd + ⌥ Opt + W | Close all windows |
| ⌘ Cmd + / | Hide or show sidebar |
| ⌘ Cmd + ⌥ Opt + T | Hide or show toolbar |
| ⌘ Cmd + Ctrl + F | Full screen |

#### Navigate

| 快捷键| 说明|
| --- | --- |
| ⌘ Cmd + 1 | Go to Inbox |
| ⌘ Cmd + 2 | Go to Today |
| ⌘ Cmd + 3 | Go to Upcoming |
| ⌘ Cmd + 4 | Go to Anytime |
| ⌘ Cmd + 5 | Go to Someday |
| ⌘ Cmd + 6 | Go to Logbook |
| ⌘ Cmd + ⇧ Shift + L | Show to-do in list |
| → | Enter a selected project |
| ← | Return to previous list |
| ⌥ Opt + ↑ | Scroll to top |
| ⌥ Opt + ↓ | Scroll to bottom |
| ⌘ Cmd + ⌥ Opt + Ctrl + ↑ | **Navigate up in the sidebar** |
| ⌘ Cmd + ⌥ Opt + Ctrl + ↓ | **Navigate down in the sidebar** |

#### Search 

| 快捷键| 说明|
| --- | --- |
| any key | Start typing to begin a search |
| ⌘ Cmd + F | Find |

#### Tags

| 快捷键| 说明|
| --- | --- |
| To assign a shortcut to a tag, open the tag window, click into the square to the right of the tag’s name and press any key.  |
| ⌘ Cmd + Ctrl + T | Open tag window |
| Esc | Close tag window |
| ⌘ Cmd + ⇧ Shift + T | Direct access to add a tag |
| Ctrl + shortcut | Toggle a tag for selected to-do |
| ⌥ Opt + Ctrl + shortcut | Filter for a tag |
| ⌘ Cmd + click any tag | Select multiple tags |
| Ctrl + Esc | Destroy previous filter |

#### Links 

| 快捷键| 说明|
| --- | --- |
| ⌘ Cmd + ⌥ Opt + ↩ Return | Open a link |


### Things3参考文章

1. [Keyboard Shortcuts for iPad - Things Support - Cultured Code](https://support.culturedcode.com/customer/portal/articles/2939808)

## Thor

由于我们默认的过滤器为全局抓包，所以抓包记录会包含所有抓取的数据。如下图所示，示例为抓取网站视频。

![](http://oc98nass3.bkt.clouddn.com/15308406866068.jpg)

其中可以看到很多内容，以上图示例说明一下：

* 链接：抓取的链接地址最直观的显示出来。
* POST或者GET：属于HTTP响应方式。HTTP响应方式有多种，例如POST、GET、HEAD、PUT、DELETE等等，假如我们需要抓包下载资源，需要从GET当中寻找。
* Weibo 7402：这一栏为User-Agent ，用户代理标识，用来显示用户通过何种方式来进行网络连接；
* [200]：为响应状态码，在Thor内便于识别。
* 10:14:30.887：为链接的具体时间
* ↓1.13KB ↑636kb ：为接收和发送的数据

### 过滤器

![](http://oc98nass3.bkt.clouddn.com/15308740122619.jpg)

### 常用的HTTP方法

* GET： 用于请求访问已经被URI（统一资源标识符）识别的资源，可以通过URL传参给服务器。
* POST：用于传输信息给服务器，主要功能与GET方法类似。
* PUT： 传输文件，报文主体中包含文件内容，保存到对应URI位置。
* HEAD： 获得报文首部，与GET方法类似，只是不返回报文主体，一般用于验证URI是否有效。
* DELETE：删除文件，与PUT方法相反，删除对应URI位置的文件。
* OPTIONS：查询相应URI支持的HTTP方法。
* PATCH：是对PUT方法的补充，用来对已知资源进行局部更新

### Thor参考

1. [Thor 新手教程（一）](https://mp.weixin.qq.com/s?__biz=MzI2NjY1MTMyMA==&mid=2247486833&idx=1&sn=c58c290c67e08eecee7887c773de76a5&chksm=ea8b9ea6ddfc17b08f35b42d73ec53c0b9bf0880514d6de5005ed5d87d2dab28f5e4b09735de&scene=21#wechat_redirect)

2. [Thor 新手教程（二）](https://mp.weixin.qq.com/s?__biz=MzI2NjY1MTMyMA==&mid=2247486842&idx=1&sn=6979c7c8d779f39fe59b0174efee8472&chksm=ea8b9eadddfc17bb35cec57e79fc050335eff5ffa262adfde97d54b932edd799d6f5e7408488&scene=21#wechat_redirect)

3. [Thor/README-zh-Hans.md at master · PixelCyber/Thor](https://github.com/PixelCyber/Thor/blob/master/README-zh-Hans.md)

4. [使用Thor抓包查看软件URL Scheme](https://www.worthfo.com/p/847548/)

5. [攻略教程之Thor的使用教程](https://www.weibo.com/ttarticle/p/show?id=2309404191223412872402)

6. [使用Thor抓包查看软件URL Scheme](https://www.worthfo.com/p/847548/)

7. [利用 Thor 实现在 iOS 上抓取百度云资源下载地址 - 少数派](https://sspai.com/post/39325)

### Stream抓取Response body

不清楚为什么Thor貌似没有响应体，新出的`Stream`可以，虽然简陋了一些

[Stream](https://itunes.apple.com/cn/app/stream/id1312141691?mt=8)

## Thunder for iOS

迅雷APP (iOS) 由于政策原因一直未在 App Store 上架，提供一个安装迅雷APP链接:

> [https://eric.ming-x.com/~tmp/ios_xunlei.html](https://eric.ming-x.com/~tmp/ios_xunlei.html)

#### 注意

*   该页面需使用系统自带的 Safari 浏览器打开
*   下载后不要立即打开，打开系统设置→通用→设备管理→选择『信任』，这样就完成了安装。

如果你正在使用电脑查看此文章，可以打开 iOS 系统自带的相机APP，对准以下二维码，根据提示完成安装，效果一样。

![](http://oc98nass3.bkt.clouddn.com/15308606870414.jpg)

参考[迅雷Beta (iOS) 内测版下载安装方法 - 简书](https://www.jianshu.com/p/f4757cfd82f8)

##  TotalFinder

[TotalFinder Compatibility](https://totalfinder.binaryage.com/compatibility)

注意最新的`10.12`和`10.13`安装时，需要在启动终端中修改系统的安全性才能安装。

这里提供一个注册码：

```
Name: Kevin Kelley
Key:  GAWAE-FBZK3-X4M62-5L9UJ-JLGUL-A6LCG-MBLQT-S9HQC-CRN99-JC7GB-FRFDZ-WCDYZ-DFPRA-5LD2R-CLLM
```

OS X 10.13 (High Sierra)install the latest version, but needs a system tweak

In the window that opens, type `csrutil disable` and press return. This turns off System Integrity Protection so that TotalFinder can be installed.

To do this, reboot and hold Command+R until the Apple logo appears once more. Go to Utilities->Terminal and type `csrutil enable` and press return. Reboot, and you are done.

## Trailer

教程


## Tower for mac

Git 工具
[Getting Started with Tower - Tower Help](https://www.git-tower.com/help/mac/first-steps/get-started-with-tower)


![](http://oc98nass3.bkt.clouddn.com/15385864644984.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385864429386.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385864283566.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385864142362.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385863555970.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385863901342.jpg)

### 设置Diff Tools
[Diff & Merge Tools - Tower Help](https://www.git-tower.com/help/mac/integration/custom-diff-tools)

## 1PassWord

[1Password for Mac 使用指南](https://jbguide.me/2014/09/03/1password-35/)

![](http://oc98nass3.bkt.clouddn.com/2017-08-07-15020711016494.jpg)

## 2Do的简单任务

![](http://oc98nass3.bkt.clouddn.com/2017-08-15-15027911951283.jpg)

### 2Do参考文章

[2Do 的简单任务 – Cheng – Medium](https://medium.com/@scomper/2do-%E7%9A%84%E7%AE%80%E5%8D%95%E4%BB%BB%E5%8A%A1-5e34fce73020)

## iOS 

### Xcode

#### Xcode链接iphone一直闪断

![](http://oc98nass3.bkt.clouddn.com/15326666022413.jpg)
![](http://oc98nass3.bkt.clouddn.com/15326666332024.jpg)

发现一个Xcode链接iphone一直闪断的问题，提示说软件下载更新才能连接，但是下载失败，还以为是数据线接触不良或者是Xcode版本不支持，后来发现开启省电模式就可以了。
[A software update is required to connect to your iOS device / iPhone - Ask Different](https://apple.stackexchange.com/questions/327310/a-software-update-is-required-to-connect-to-your-ios-device-iphone)

```
The problem can be fixed by installing XCode beta.
This error occurs when the version of macOS (and iTunes) running on the computer is not compatible with the version of iOS on the device you're trying to connect.

Normally, updating the macOS to its current version will solve the problem. However, this won't work if the iOS device is running a newer beta version, and the Mac is not.
```


#### 关于使用Clang(LLVM)将OC文件转为C/C++文件报错的问题

```objc

main.m:9:9: fatal error: 'UIKit/UIKit.h' file not found
#import <UIKit/UIKit.h>
    ^
1 error generated.
```

```objc
clang -x objective-c -rewrite-objc -isysroot /Applications/Xcode.app/Contents/Developer/Platforms/iPhoneSimulator.platform/Developer/SDKs/iPhoneSimulator.sdk xxx.m

//__weak修饰变量，需要告知编译器使用ARC环境及版本号否则会报错，添加说明
-fobjc-arc -fobjc-runtime=ios-8.0.0

xcrun -sdk iphoneos clang -arch arm64 -rewrite-objc -fobjc-arc -fobjc-runtime=ios-8.0.0 main.m
```

### 下载软件

* Valley [![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://www.appvalley.vip/#) 
* tweakbox [![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://www.tweakboxapp.com/)
* panda helper [![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](http://m.pandahelp.vip/regular)
3. Pin。Pin里面是有Valley，它可以下载接近2000多个APP。有付费软件，付费游戏，破解版的社交平台软件和游戏。内容简单，没有广告，不过不能自定义搜索，只能自己一个个翻。而且是英文界面，你必须得找到你所要的软件的英文名字。
3款软件版界面都比网页版简洁，但是前两款有广告。前两个已经介绍过了所以直接就介绍panda helper这款。

4. 网页内安装下载
[![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://next.tweakboxapp.com/) 这个软件类似Valley。他里面的软件跟Valley差不多，也是2000来个，进入网页后，找到APPS这个选项，点一下就进入APP软件的里面了，然后找到 tweaked APPs这个是搜索软件，因为是英文界面，你需要找到你所要下载的软件的英文名字。你也可以在Appstore Apps里面找软件，基本上Valley差不多的软件。网页版无广告，等下介绍软件版
```
Valley jse://run?file=APPValley.js 
```

6. workflow规则
[![](https://h5.sinaimg.cn/upload/2015/09/25/3/timeline_card_small_web_default.png)网页链接](https://workflow.is/workflows/5b681575dd944fca911d697d651cfadd)
里面包含了上面网页安装方法的3款软件

参考[攻略教程之免费下载付费软件](https://m.weibo.cn/status/4180725890666373?)


### Safari问题

* 设置Safari默认搜索为baidu

发现以前设置的地区是米国，所以在iOS的Safari搜索引擎设置中没有找到baidu.
切换回中国🇨🇳就可以了。
![](http://oc98nass3.bkt.clouddn.com/15308987115979.jpg)

* Safari的阅读模式

发现Safari的阅读模式每次都自动进入，发现是长按可以唤起菜单设置的。
![](http://oc98nass3.bkt.clouddn.com/15308987360120.jpg)


# 常见问题

### 终端 命令行中文件路径有空格怎么办？

如： 
```
sudo rm -rf "/Library/Input Methods/Squirrel.app" 
```
加上双引号就行


## “XXX.app”已损坏，打不开。 您应该将它移到废纸篓

1. 在Mac电脑安装App提示App已损坏”xxxx已损坏，打不开。您应该推出磁盘映像”解决办法解决方案

方法：打开电脑的系统偏好设置-->安全与隐私，如图下如果没有第三项“任何来源”这个选项，就要打开终端运行：`sudo spctl --master-disable` ，重新进入"安全与隐私"就会出现打开的选项

![](http://oc98nass3.bkt.clouddn.com/15161963030407.jpg)
```
//先禁止
sudo spctl --master-disable
//后恢复
sudo spctl --master-enable
```

## Snap和Chrome的标签问题

`2018-03-14`在升级`MacOS high sierra`后,很多老的软件出现问题，今天出现之前安装的`Chrome`在使用snap切换的时候，每次会出新的tap页，因为我在mac上分了多个deskTop，这样每次来回切换`Chrome`的时候就会弹出很多的tab,增加了`Chrome`的内存消耗，还非常不方便，我还以为是snap的问题，后面想升级下`Chrome`，最后发现**把`Chrome`从Dock中移除并退出重新打开**，这种问题就解决了。可能是MacOS的问题吧。

## Github Desktop问题

本来我是不想把`Github Desktop`加进来的，没想到它今天抽了一个错误，为了记录一下我还是写一下。

报的错误：
![](http://oc98nass3.bkt.clouddn.com/15303368203935.jpg)

估计是钥匙串的访问权限问题
找到一篇文章：[GitHub Desktop was unable to store the account token in the keychain · Issue #4614 · desktop/desktop](https://github.com/desktop/desktop/issues/4614)
![](http://oc98nass3.bkt.clouddn.com/15303369966352.jpg)
参考[desktop/known-issues.md at master · desktop/desktop](desktop/known-issues.md at master · desktop/desktop)

## MicroSoft Word 弹窗问题

在Mac上使用word过程中，有时候经常出现这种弹窗:

![](http://oc98nass3.bkt.clouddn.com/15294901445351.jpg)
![](http://oc98nass3.bkt.clouddn.com/15294901483362.jpg)

这是模板的问题，在设置中找到模板文件路径

![](http://oc98nass3.bkt.clouddn.com/15294900549396.jpg)

![](http://oc98nass3.bkt.clouddn.com/15294900170729.jpg)

删除这个文件，然后重启Word,这个文件会重新生成。（估计模板文件出了问题）

参考[Word 无法打开现有共用模板 (Normal.dotm)](https://bbs.feng.com/read-htm-tid-10206026.html)

# 参考资料

## 开发工具

1. 学习资源大全
[Awesome](https://github.com/sindresorhus/awesome)

2. iOS资源大全中文版
[iOS资源大全中文版](https://love2.io/@ayamefing/doc/awesome-ios-cn/README.md)

3. iOS资源大全
[AwesomeiOS](http://awesomeios.com/)

4. iOS，App内存泄漏检查
[Tencent/OOMDetector](https://github.com/Tencent/OOMDetector): OOMDetector is a memory monitoring component for iOS which provides you with OOM monitoring, memory allocation monitoring, memory leak detection and other functions.

## `Alfred`参考资料

1. [OS X 效率启动器 Alfred 详解与使用技巧 - 少数派](https://sspai.com/post/27900)
2. [使用 AppleScript、Tags 和 Alfred 重新打造文件管理和搜索系统 - 少数派](https://sspai.com/post/42859)
3. [从零开始学习 Alfred：基础功能及设置 - 少数派](https://sspai.com/post/32979)
4. [它已不仅仅是一款 Mac 效率启动器：Alfred 3.0 新版详解 - 少数派](https://sspai.com/post/34468)
5. [使用 Alfred 提高你的工作效率 | Matrix 精选 - 少数派](https://sspai.com/post/35927)

## `TextExpander`参考资料

1. [解决中文输入法无法调用 TextExpander 6 的问题丨一日一技 - 少数派](https://sspai.com/post/35502)

2. [解决 TextExpander 5 在中文环境下输入问题](https://medium.com/@oscargong1995/%E8%A7%A3%E5%86%B3-textexpander-5-%E5%9C%A8%E4%B8%AD%E6%96%87%E7%8E%AF%E5%A2%83%E4%B8%8B%E8%BE%93%E5%85%A5%E9%97%AE%E9%A2%98-e0a2237e2609)
 
## 其他

* [少数派幕后](https://sspai.com/tag/%E5%B9%95%E5%90%8E)
* [小众软件](https://www.appinn.com/)
* [从事产品经理 3 年，我用这 8 款应用打造高效产品工作流 - 少数派](https://sspai.com/post/41918)