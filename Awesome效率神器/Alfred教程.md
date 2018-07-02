## Alfred教程

![image](http://upload-images.jianshu.io/upload_images/225323-9241e9deef92a341.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

`Alfred` 就是 `Mac` 上最强大的工具台，一个图形化的终端，只有你想不到，没有它做不到。
 
### Alfred的使用

最方便的使用就是设置`double ⌘`唤起`Alfred`啦~＼（＾ ＾）／

![image](http://upload-images.jianshu.io/upload_images/225323-376fbeab62b6fb09.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### Alfred功能特性

![image](http://upload-images.jianshu.io/upload_images/225323-3c6ac45878576561.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Alfred包含了系统的命令，比如重启、锁定、睡眠等。最常用重启 restart。

![image.png](http://upload-images.jianshu.io/upload_images/225323-ab4eab6746203c55.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* Alfred一个很重要的命令操作就是：`↑`，可以调用上次的历史命令！

### Alfred搜索

`Alfred`的通用的设置基本都是关于文件操作的：搜索，拷贝路径，预览，在Finder中显示等

#### 网页搜索

##### 自定义web搜索

1. 利用常用网站的`API`可以自定义web搜索.
![](http://oc98nass3.bkt.clouddn.com/15234355436697.jpg)
![](http://oc98nass3.bkt.clouddn.com/15303521078999.jpg)

2. 可以搜索浏览器标签，我主要使用`Chrome`所以这边搜索的是`Chrome`的标签
![](http://oc98nass3.bkt.clouddn.com/15234354592741.jpg)

##### 十款常用搜索引擎的 URL 规则

| 网站名称 | 搜索 URL |
| --- | --- |
| 少数派 | [https://sspai.com/search/article?q={query}](https://sspai.com/search/article?q={query}) |
| 百度 | [https://www.baidu.com/s?wd={query}](https://www.baidu.com/s?wd={query}) |
| 知乎 | [https://www.zhihu.com/search?q={query}](https://www.zhihu.com/search?q={query}) |
| 豆瓣全站 | [https://www.douban.com/search?q={query}](https://www.douban.com/search?q={query}) |
| 豆瓣电影 | [https://movie.douban.com/subject_search?search_text={query}](https://movie.douban.com/subject_search?search_text={query}) |
| 简书 | [https://www.jianshu.com/search?q={query}](https://www.jianshu.com/search?q={query}) |
| 微博 | [https://s.weibo.com/weibo/{query}](https://s.weibo.com/weibo/%7Bquery%7D) |
| 微信文章 | [http://weixin.sogou.com/weixin?type=2&query={query}](http://weixin.sogou.com/weixin?type=2&query={query}) |
| 优酷 | [https://www.soku.com/search_video/q_{query}](https://www.soku.com/search_video/q_%7Bquery%7D) |
| 爱奇艺 | [https://so.iqiyi.com/so/q_{query}](https://so.iqiyi.com/so/q_%7Bquery%7D) |
| 哔哩哔哩 | [https://search.bilibili.com/all?keyword={query}](https://search.bilibili.com/all?keyword={query}) |
| 中文维基百科 | [https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=Alfred](https://zh.wikipedia.org/w/index.php?cirrusUserTesting=control-explorer-i&search=Alfred) |
| 百度百科 | [https://baike.baidu.com/search/none?word={query}&pn=0&rn=10&enc=utf8](https://baike.baidu.com/search/none?word={query}&pn=0&rn=10&enc=utf8) |
| 萌娘百科 | [https://zh.moegirl.org/index.php?search={query}](https://zh.moegirl.org/index.php?search={query}) |
| 淘宝 | [https://s.taobao.com/search?q={query}](https://s.taobao.com/search?q={query}) |
| 京东 | [https://search.jd.com/Search?keyword={query}](https://search.jd.com/Search?keyword={query}) |
| 什么值得买 | [http://search.smzdm.com/?s={query}](http://search.smzdm.com/?s={query}) |
| GitHub | [https://github.com/search?q={query}](https://github.com/search?q={query}) |
| Stack Overflow | [https://www.stackoverflow.com/search?q={query}](https://www.stackoverflow.com/search?q={query}) |

####  一键打开多个网站查询你输入的内容。

比如我要同时在 少数派 和 利器 检索Alfred，先确定两个网站的查询URL，分别是 https://sspai.com/search/article?q={query} 和 https://www.google.com/search?sitesearch=liqi.io&q={query} ，然后在Alfred的Workflows中添加一个Templates，选择Web And URLs，然后设置一个关键词，比如 “sapp”，最后加入两个Actions，类型选Open URL即可

#### 文件搜索

![](http://oc98nass3.bkt.clouddn.com/15194620236262.jpg)

有了`Alfred`，不用去到桌面用鼠标打开`finder`啦，勾选快速搜索文件选项，唤起`Alfred`，输入`~`或者空格就可以输入文件路径了，会给出智能匹配提示。

还提供了`in`、`find`、`open`命令，`in`可以在文件中查找内容，╮(✪ω✪)╭这不就是`Finder`的搜索吗？

`find`查找文件所在目录，`open`打开文件

可以设置模糊搜索`Fuzzy Search`， 建议打开使用方向键切换文件层次，灰常方便， 而且，直接可以使用`previous`或者`⌘ + ⌥ + /`来调起之前的文件路径~

当然，你还可以通过`⌥ + ⇣/⇡`来选择多个常用路径╮(✪ω✪)╭，然后使用`⌥ + <-`进行处理（打开,删除,拷贝路径等），或者`⌥ + ->`删除路径

##### 历史访问路径

![](http://oc98nass3.bkt.clouddn.com/15303486401472.jpg)

##### 文件缓存操作

```
⌥ + ↑to add a file to the buffer.
⌥ + ↓to add a file and move to the next selection.
⌥ + ← to remove the last item from the buffer.
⌥ + → to action all items in the buffer.
```
可能需同时对多个文件进行操作，可以选中文件，按住`⌥ + ↓`添加预选文件。
![](http://oc98nass3.bkt.clouddn.com/15303488549111.jpg)

可以通过`⌥ + →`进入批量操作菜单

![](http://oc98nass3.bkt.clouddn.com/15303488091520.jpg)

我的文件多选操作设置：
![](http://oc98nass3.bkt.clouddn.com/15303499082641.jpg)

定位到所需文件后，我们往往需要对其做进一步处理，在回车打开文件前，不妨先按下 `⌥ + ⌘ + \`，你会发现 Alfred 已经为你准备了解压、复制、分享、查重等数项常用操作，不用在 Finder 中翻来翻去了。

##### 文件快速预览

选择文件后，可以通过`Shfit`预览~

![image](http://upload-images.jianshu.io/upload_images/225323-7935c99c626172b6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

有一个小技巧就是，按住`⌘`可以查看文件路径，使用`⌘ + ↓`和`⌘ + ↑`可以不断切换文件层级

![](http://oc98nass3.bkt.clouddn.com/15303491154189.jpg)

### 黏贴板

对于一些文案在App间频繁的切换的需求，`Alfred`提供了实用的黏贴板功能：
我设置的快捷键为：`⌘ + ⌥ + C`
![](http://oc98nass3.bkt.clouddn.com/15303511047989.jpg)

Alfred的剪贴板扩展支持所有类型文件的复制历史保存，从文字到 Doc 文档，从 Gif 图片到 .dmg 文件，你的所有复制历史都会被忠实的记录下来。

#### 清空黏贴板

![](http://oc98nass3.bkt.clouddn.com/15303510082640.jpg)

### 代码片段

> Boost your productivity by using snippets to save your frequently used text clips

对于一些经常在登录网址时候需要输入的信息可以利用`Alfred`的Snippets,比如邮箱，电话等等。
我设置的快捷键：`⌘ + ⌥ + S`

附注：之前用过`Paster`相当于`Alfred`的这2个功能

#### 包括动态和游标占位符

使用内置格式的动态占位符
* The date in long format: `{date:long}`
* The time 10 minutes 30 seconds ago: `{time -10m -30s:long}`
* The second item in your clipboard: `{clipboard:1}` (0 represents the latest item, 1 the next item down, and so on)

如果需要告诉`alfred`您希望光标移动到的位置, 请将 {cursor} 添加到代码段文本中。

#### 使用代码段自动扩展

Aflred3可以将Snippets应用于Mac全局文本，需要设置
![](http://oc98nass3.bkt.clouddn.com/15303417306027.jpg)

效果如下：
![](http://oc98nass3.bkt.clouddn.com/15303436476949.gif)

参考[Snippets and Text Expansion - Alfred Help and Support](https://www.alfredapp.com/help/features/snippets/#dynamic)

##### 使用好的代码段扩展

* Use non-word keywords to avoid unexpected expansion; Don't use the keyword date to paste the date, otherwise every time you try to type it's a date!, you'll find yourself saying it's a 01/06/16! as your snippet auto-expands.
* Start all your snippets with the same non-alphanumeric character, such as an exclamation mark, colon or semi-colon. (e.g. !office). Use collection-wide prefixes and suffixes to do this.
* Use unusual capitalisation (Alfred will respect the capitalisation you set, e.g. officE)
* Use double characters (e.g. ttime)

#### 代码段触发器

注意: 此功能是在Alfred V3.4 中添加的, 因此您需要使用3.4 或更高的代码段触发器。
![](http://oc98nass3.bkt.clouddn.com/15303438547666.png)


参考[Snippet Triggers - Alfred Help and Support](https://www.alfredapp.com/help/workflows/triggers/snippet/)

### 使用情况

`Alfred`提供了使用频率的报表，可以看到使用`Alfred`的频率
![image](http://upload-images.jianshu.io/upload_images/225323-9ba66d965b5acd3a.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 自定义主题

[主题](http://www.packal.org/theme-list)
1. [VVV Dark Solarized (Compact) (Gray) | Packal](http://www.packal.org/theme/vvv-dark-solarized-compact-gray)
![](http://oc98nass3.bkt.clouddn.com/15303474708329.jpg)

2. [Nazar | Packal](http://www.packal.org/theme/nazar)
![](http://oc98nass3.bkt.clouddn.com/15303476287649.jpg)

### Large Type

使用`⌘ + L`放大搜索框🔍中的结果，使您可以在屏幕上显示大字符的文本

### 启用终端

如果您经常需要启动终端或 shell 命令, 您可以这样做从Alfred内部这样启动
![](http://oc98nass3.bkt.clouddn.com/15303533225729.png)

####  配置iTerm2

1. [stuartcryan/custom-iterm-applescripts-for-alfred: Custom iTerm Applescripts for Alfred](https://github.com/stuartcryan/custom-iterm-applescripts-for-alfred)

iTerm2版本大于V3.1.1的使用下面的命令获取脚本

```
curl --silent 'https://raw.githubusercontent.com/stuartcryan/custom-iterm-applescripts-for-alfred/master/custom_iterm_script_iterm_2.9.applescript' | pbcopy
```

得到如下所示的脚本

```
-- This is v0.7 of the custom script for AlfredApp for iTerm 3.1.1+
-- created by Sinan Eldem www.sinaneldem.com.tr

on alfred_script(q)
	if application "iTerm2" is running or application "iTerm" is running then
		run script "
			on run {q}
				tell application \"iTerm\"
					activate
					try
						select first window
						set onlywindow to true
					on error
						create window with default profile
						select first window
						set onlywindow to true
					end try
					tell the first window
						if onlywindow is false then
							create tab with default profile
						end if
						tell current session to write text q
					end tell
				end tell
			end run
		" with parameters {q}
	else
		run script "
			on run {q}
				tell application \"iTerm\"
					activate
					try
						select first window
					on error
						create window with default profile
						select first window
					end try
					tell the first window
						tell current session to write text q
					end tell
				end tell
			end run
		" with parameters {q}
	end if
end alfred_script
```

![Alfred3Setting-Terminal](http://oc98nass3.bkt.clouddn.com/Alfred3Setting-Terminal.png)

参考[Terminal and Shell - Alfred Help and Support](https://www.alfredapp.com/help/features/terminal/)

### 计算器

计算器大概是启动器应用们的标配功能了，Alfred 也不例外。只需键入算式，Alfred 就会直接给出正确答案，直观快捷。支持完善的函数语法.

![](http://oc98nass3.bkt.clouddn.com/15237811833233.png)

### 强大的`Workflow`

`Alfred`真正强大之处是它的核心思想：把重复的工作抽象成一个`Workflow`,作为一个`Workflow`,一些开发者不断开发出一些常用的，解决他们自身需求的`Workflow`，可以说极大的方便了我们这些用户，这里给出我一些常用的吧。

![image](http://upload-images.jianshu.io/upload_images/225323-6e18493c6db67bb7.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

重点介绍几个Workflow

* [Alfred-fixum](https://github.com/deanishe/alfred-fixum/releases/tag/v0.6)更新一些旧的`WorkFlow`需要
* [Packal——Alfred Workflows](http://www.packal.org/workflow/packal-workflow-search) WorkFlow Pool 
* [Top-workflow](https://github.com/zhaocai/alfred2-top-workflow) Mac Helper, better than kill-process; Use  -c, -m, -i, glance，结合快捷键，

#### Alfred-fixum

Alfred-fixum可以说是Workflow的Manager了，监测和更新Workflow

一些旧的`WorkFlow`可以通过[Alfred-fixum](https://github.com/deanishe/alfred-fixum/releases/tag/v0.6) 进行更新。

![](http://oc98nass3.bkt.clouddn.com/15303453477490.jpg)

贴心的提供了控制台的log入口：
```
15:50:24 fixum.py:341 INFO     [!!] workflow "Gank" is using outdated version (1.17.2) of Alfred-Workflow
15:50:24 fixum.py:193 INFO         updating "Gank" ...
15:50:24 fixum.py:199 INFO         installed new version of Alfred-Workflow
15:50:24 fixum.py:353 INFO     
15:50:25 fixum.py:373 INFO     [DONE] updated 1 workflow(s) with a newer version of Alfred-Workflow
```

#### Packal —— Workflows

Search Packal.org from the comfort of Alfred
什么是 Packal？简而言之，它就是一个集成了 Workflows 工作流程和 Themes 主题的平台。由于它专为 Alfred 服务，所以相关开发者会更加选择在这里发布自己的作品（及更新），用户也能获得最新的插件版本，而不是被动地关注来源地。因此建议每位 Alfred 用户都使用 Packal。

Packal Workflow 的作用就是帮助用户直接在 Alfred 中快速搜索，代替了「打开浏览器 - 输入网址 - 输入关键词 - 搜索」的过程。对于这类操作方式，笔者习惯将它们成为「代步工具」。另外，你也可以用 Packal Updater 时刻保持其它的 Workflows 处于最新版本

[deanishe/alfred-packal-search: Search Packal.org's collection of Alfred workflows from Alfred](https://github.com/deanishe/alfred-packal-search)最新[Packal-Search-1.4.1.alfredworkflow](https://github.com/deanishe/alfred-packal-search/blob/master/Packal-Search-1.4.1.alfredworkflow)

##### 用法

*   `packal workflows [query]` — View/search for workflows by name/category/author/tag

    *   `↩` — Open workflow page on Packal.org in your browser
    *   `⌘+↩` — View/search workflows by the same author
*   `packal tags [query]` — View/search workflow tags

    *   `↩` or `⇥` — View/search workflows with selected tag
*   `packal categories [query]` — View/search workflow categories

    *   `↩` or `⇥` — View/search workflows in selected category
*   `packal authors [query]` — View/search workflow authors

    *   `↩` or `⇥` — View/search workflows by selected author
    *   `⌘+↩` — Add this author to the status blacklist. This means workflows by this author won't be shown in the update status list. Useful for hiding your own workflows, which you presumably don't update via Packal.
*   `packal versions [query]` — View/search OS X versions and compatible workflows

    *   `↩` or `⇥` — View/search workflows compatible with selected OS X version
*   `packal status` — Show a list of workflows that are out-of-date (❗) or are available on Packal.org, but were installed from elsewhere (❓)

#### Top-workflow

[Top-workflow](https://github.com/zhaocai/alfred2-top-workflow) Mac Helper, better than kill-process; Use  -c, -m, -i, glance，结合快捷键

The initial motive of this workflow is to avoid frequent visits to the Activity Monitor when the fan goes loud. Now it has been evolved with two major features:
![](http://oc98nass3.bkt.clouddn.com/15303494502622.jpg)

#### 斗图神器 

收集了成千上万的撕逼斗图表情包，在这里你可以快速找到想要的表情[KilluaChen/Dou-figure-alfred-workflow: 斗图神器 收集了成千上万的撕逼斗图表情包，在这里你可以快速找到想要的表情](https://github.com/KilluaChen/Dou-figure-alfred-workflow)

##### 下载

[下载斗图神器](斗图神器.alfredworkflow)

![CmdTap_和_Alfred_Preferences](http://oc98nass3.bkt.clouddn.com/CmdTap_和_Alfred_Preferences.png)

##### 检索

检索关键字: `dt`

检索快捷键:`Option+Shift+D`

下载所有图片关键字: `dadt` ,近10个进程同时下载(慎用!会造成服务器压力)

>  第一次检索的关键字只会显示第一页预览,搜过的关键字图片会自动缓

##### 查阅

查看已下载图片数:`ls ~/Pictures/.DouTu | wc -w`


##### 配置

图片默认保存在`~/Pictures/.DouTu/`下面,不要了可以直接删掉`rm -rf ~/Pictures/.DouTu`

想修改图片保存路径可以修改`src/Base.php`文件中的第`33`行

修改为
```
cp $1 ~/Desktop/斗图神器.jpg
```

### Workflow补充

1. [Github Search](http://www.packal.org/workflow/github-search) Search Github

2. [V2EX.alfredworkflow](https://github.com/hzlzh/Alfred-Workflows/raw/master/Downloads/V2EX.alfredworkflow) V2EX.alfredworkflow

3. [vino-workflows/V2ex.alfredworkflow at master · wuchangfeng/vino-workflows](https://github.com/wuchangfeng/vino-workflows/blob/master/v2ex/V2ex.alfredworkflow)

4. [alfred-mweb-workflow](https://github.com/tianhao/alfred-mweb-workflow)搜索、打开MWeb 内部文档和外部文档

5. [Menu Search - Share your Workflows - Alfred App Community Forum](https://www.alfredforum.com/topic/10231-faster-menu-search/)

需要在安全性设置的隐私中添加`Alfred`.
![](http://oc98nass3.bkt.clouddn.com/15305378386470.jpg)


### 制作Workflow

[vino-workflows/VinoGank.alfredworkflow at master · wuchangfeng/vino-workflows](https://github.com/wuchangfeng/vino-workflows/blob/master/gank/VinoGank.alfredworkflow)

[Workflows - Alfred Help and Support](https://www.alfredapp.com/help/workflows/)

参考 [如何去写一个第三方的 workflow](https://allenwu.itscoder.com/how-to-write-a-workflow-for-mac)

### Alfred常见问题

#### 1. 通讯录提示

[和谐版的Alfred 3 在每次开机后，都会提示“是否允许访问通讯录”的弹窗，让人不胜其烦。](http://xclient.info/a/761216bf-0737-5592-0ba8-8fbc5f31b3e6.html?_=75ebe0a762462e5265640b26094a4fdb)

打开终端（或iTerm2）

```
sudo codesign -f -d -s - /Applications/Alfred\ 3.app/Contents/Frameworks/Alfred\ Framework.framework/Versions/A/Alfred\ Framework
```

#### 2. Top-workflow 问题

Top-workflow Doesn't work on OSX 10.13 #19
解决方法：
[Top-workflow](https://github.com/zhaocai/alfred2-top-workflow) 
下载fixed[Top.Processes.v2.2.alfredworkflow](https://github.com/singhprd/alfred2-top-workflow/releases/download/v2.2/Top.Processes.v2.2.alfredworkflow)
参考[Mac10.13后问题的解决](https://github.com/zhaocai/alfred2-top-workflow/issues/19)


#### 3. Workflow版本太低

 使用WorkFLow报问题`Incompatible Python workflow library`
 需要更新Workflow
 使用[Alfred Fixum](https://github.com/deanishe/alfred-fixum)更新`Workflow`
 
```
Incompatible Python workflow library
Due to an incompatibility between macOS 10.12.4+ and a 3rd party library, Alfred-Workflow, Alfred 3.4.1+ doesn't load workflows containing older, affected versions of this library.

Disabling these workflows prevents the incompatibility from causing high CPU usage.
```

#### 4. 存放路径问题：

Alfred从2升级到3，一些`Workflow`报错
```
mkdir: /Users/USERNAME/Library/Application Support/Alfred 2/Workflow Data: No such file or directory
```

解决方法:
新建数据和缓存目录

```
mkdir -p "$HOME/Library/Application Support/Alfred 2/Workflow Data/"
mkdir -p "$HOME/Library/Caches/com.runningwithcrayons.Alfred-2/Workflow Data/"
```

参考 [`No such file or directory` when running the updater · Issue #9 · shawnrice/packal-updater](https://github.com/shawnrice/packal-updater/issues/9)

#### 5.Cracked Alfred Workflow 不工作

破解后的Alfred3安装Workflow后，发现hotkey和keyword失效，无法召唤Workflow。(T＿T)

解决方法:
虽然侥幸解决了但是未发现原理,记录一下操作：
![](http://oc98nass3.bkt.clouddn.com/15303401675170.jpg)

1. 卸载重装破解的Alfred3,发现在`/Users/michaelmao/Library/`中多了一个`Application`文件，我觉得是CODE Keygen产生的文件，尝试删除。
2. 尝试拖入Workflow到`plugins`文件夹
3. 打开`license.plist`文件和`Alfred.alfredpreference`文件
4. 重启Alfred3, it worked~ 斗图的Workflow也可以正常使用了。

### 参考 

1. [Incompatible Python workflow library](https://www.alfredapp.com/help/troubleshooting/incompatible-python-workflow-library/)
2. [Alfred Fixum](https://github.com/deanishe/alfred-fixum)
3. [KilluaChen/Dou-figure-alfred-workflow: 斗图神器 收集了成千上万的撕逼斗图表情包，在这里你可以快速找到想要的表情](https://github.com/KilluaChen/Dou-figure-alfred-workflow)
4. [OS X 效率启动器 Alfred 详解与使用技巧 - 少数派](https://sspai.com/post/27900)
5. [使用 AppleScript、Tags 和 Alfred 重新打造文件管理和搜索系统 - 少数派](https://sspai.com/post/42859)
6. [从零开始学习 Alfred：基础功能及设置 - 少数派](https://sspai.com/post/32979)
7. [它已不仅仅是一款 Mac 效率启动器：Alfred 3.0 新版详解 - 少数派](https://sspai.com/post/34468)
8. [使用 Alfred 提高你的工作效率 ](https://sspai.com/post/35927)

## Todo

- [ ] 制作Workflow