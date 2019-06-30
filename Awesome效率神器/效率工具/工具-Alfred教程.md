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
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15234355436697.jpg)
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303521078999.jpg)

2. 可以搜索浏览器标签，我主要使用`Chrome`所以这边搜索的是`Chrome`的标签
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15234354592741.jpg)

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

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15194620236262.jpg)

有了`Alfred`，不用去到桌面用鼠标打开`finder`啦，勾选快速搜索文件选项，唤起`Alfred`，输入`~`或者空格就可以输入文件路径了，会给出智能匹配提示。

还提供了`in`、`find`、`open`命令，`in`可以在文件中查找内容，╮(✪ω✪)╭这不就是`Finder`的搜索吗？

`find`查找文件所在目录，`open`打开文件

可以设置模糊搜索`Fuzzy Search`， 建议打开使用方向键切换文件层次，灰常方便， 而且，直接可以使用`previous`或者`⌘ + ⌥ + /`来调起之前的文件路径~

当然，你还可以通过`⌥ + ⇣/⇡`来选择多个常用路径╮(✪ω✪)╭，然后使用`⌥ + <-`进行处理（打开,删除,拷贝路径等），或者`⌥ + ->`删除路径

![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190630084707.png)

##### 历史访问路径

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303486401472.jpg)

##### 文件缓存操作

```
⌥ + ↑to add a file to the buffer.
⌥ + ↓to add a file and move to the next selection.
⌥ + ← to remove the last item from the buffer.
⌥ + → to action all items in the buffer.
```
可能需同时对多个文件进行操作，可以选中文件，按住`⌥ + ↓`添加预选文件。
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303488549111.jpg)

可以通过`⌥ + →`进入批量操作菜单

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303488091520.jpg)

我的文件多选操作设置：
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303499082641.jpg)

定位到所需文件后，我们往往需要对其做进一步处理，在回车打开文件前，不妨先按下 `⌥ + ⌘ + \`，你会发现 Alfred 已经为你准备了解压、复制、分享、查重等数项常用操作，不用在 Finder 中翻来翻去了。



##### 文件快速预览

选择文件后，可以通过`Shfit`预览~

![image](http://upload-images.jianshu.io/upload_images/225323-7935c99c626172b6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

有一个小技巧就是，按住`⌘`可以查看文件路径，使用`⌘ + ↓`和`⌘ + ↑`可以不断切换文件层级

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303491154189.jpg)

### 黏贴板

对于一些文案在App间频繁的切换的需求，`Alfred`提供了实用的黏贴板功能：
我设置的快捷键为：`⌘ + ⌥ + C`
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303511047989.jpg)

Alfred的剪贴板扩展支持所有类型文件的复制历史保存，从文字到 Doc 文档，从 Gif 图片到 .dmg 文件，你的所有复制历史都会被忠实的记录下来。

#### 清空黏贴板

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303510082640.jpg)

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
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303417306027.jpg)

效果如下：
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303436476949.gif)

参考[Snippets and Text Expansion - Alfred Help and Support](https://www.alfredapp.com/help/features/snippets/#dynamic)

##### 使用好的代码段扩展

* Use non-word keywords to avoid unexpected expansion; Don't use the keyword date to paste the date, otherwise every time you try to type it's a date!, you'll find yourself saying it's a 01/06/16! as your snippet auto-expands.
* Start all your snippets with the same non-alphanumeric character, such as an exclamation mark, colon or semi-colon. (e.g. !office). Use collection-wide prefixes and suffixes to do this.
* Use unusual capitalisation (Alfred will respect the capitalisation you set, e.g. officE)
* Use double characters (e.g. ttime)

#### 代码段触发器

注意: 此功能是在Alfred V3.4 中添加的, 因此您需要使用3.4 或更高的代码段触发器。
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303438547666.png)


参考[Snippet Triggers - Alfred Help and Support](https://www.alfredapp.com/help/workflows/triggers/snippet/)

### 使用情况

`Alfred`提供了使用频率的报表，可以看到使用`Alfred`的频率
![image](http://upload-images.jianshu.io/upload_images/225323-9ba66d965b5acd3a.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 自定义主题

[主题](http://www.packal.org/theme-list)
1. [VVV Dark Solarized (Compact) (Gray) | Packal](http://www.packal.org/theme/vvv-dark-solarized-compact-gray)
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303474708329.jpg)

2. [Nazar | Packal](http://www.packal.org/theme/nazar)
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303476287649.jpg)

### Large Type

使用`⌘ + L`放大搜索框🔍中的结果，使您可以在屏幕上显示大字符的文本

### 启用终端

如果您经常需要启动终端或 shell 命令, 您可以这样做从Alfred内部这样启动
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303533225729.png)

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

![Alfred3Setting-Terminal](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/Alfred3Setting-Terminal.png)

参考[Terminal and Shell - Alfred Help and Support](https://www.alfredapp.com/help/features/terminal/)

### 计算器

计算器大概是启动器应用们的标配功能了，Alfred 也不例外。只需键入算式，Alfred 就会直接给出正确答案，直观快捷。支持完善的函数语法.

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15237811833233.png)

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

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303453477490.jpg)

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
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303494502622.jpg)

#### 斗图神器 

收集了成千上万的撕逼斗图表情包，在这里你可以快速找到想要的表情[KilluaChen/Dou-figure-alfred-workflow: 斗图神器 收集了成千上万的撕逼斗图表情包，在这里你可以快速找到想要的表情](https://github.com/KilluaChen/Dou-figure-alfred-workflow)

##### 下载

[下载斗图神器](https://github.com/KilluaChen/Dou-figure-alfred-workflow)

![CmdTap_和_Alfred_Preferences](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/CmdTap_和_Alfred_Preferences.png)

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
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15305378386470.jpg)


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
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15303401675170.jpg)

1. 卸载重装破解的Alfred3,发现在`/Users/michaelmao/Library/`中多了一个`Application`文件，我觉得是CODE Keygen产生的文件，尝试删除。
2. 尝试拖入Workflow到`plugins`文件夹
3. 打开`license.plist`文件和`Alfred.alfredpreference`文件
4. 重启Alfred3, it worked~ 斗图的Workflow也可以正常使用了。

5. Alfred打不开：重签名
```
codesign --sign - --force --deep /Applications/Alfred\ 3.app 
codesign --sign - --force --deep /Applications/Alfred\ 3.app/Contents/Preferences/Alfred\ Preferences.app
```


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



 [](http://louiszhai.github.io/) 

# [路易斯](http://louiszhai.github.io/)

坚持原著, 深度思考, 力求简单通俗叙事

*   [主页](http://louiszhai.github.io/)
*   [所有文章](http://louiszhai.github.io/archives/)

[github](https://github.com/Louiszhai "github") [rss](http://louiszhai.github.io/atom.xml "rss")

[CSS](http://louiszhai.github.io/tags/CSS/)[JavaScript](http://louiszhai.github.io/tags/JavaScript/)[JavaScript Canvas](http://louiszhai.github.io/tags/JavaScript-Canvas/)[JavaScript Chrome-Extension](http://louiszhai.github.io/tags/JavaScript-Chrome-Extension/)[Tool](http://louiszhai.github.io/tags/Tool/)[Web](http://louiszhai.github.io/tags/Web/)[XSS](http://louiszhai.github.io/tags/XSS/)[css](http://louiszhai.github.io/tags/css/)[javascript](http://louiszhai.github.io/tags/javascript/)

[阮一峰的网络日志](http://www.ruanyifeng.com/blog/) [张鑫旭-鑫空间-鑫生活](http://www.zhangxinxu.com/wordpress/category/js/) [尤雨溪主页](http://evanyou.me/)

[2018-05-31](http://louiszhai.github.io/2018/05/31/alfred/)

# Alfred神器使用手册

*   [Tool](http://louiszhai.github.io/tags/Tool/)

目录

1.  [如何安装alfred](http://louiszhai.github.io/2018/05/31/alfred/#%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85alfred)
2.  [一个例子说明为什么要用alfred](http://louiszhai.github.io/2018/05/31/alfred/#%E4%B8%80%E4%B8%AA%E4%BE%8B%E5%AD%90%E8%AF%B4%E6%98%8E%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E7%94%A8alfred)
3.  [alfred能做什么？](http://louiszhai.github.io/2018/05/31/alfred/#alfred%E8%83%BD%E5%81%9A%E4%BB%80%E4%B9%88%EF%BC%9F)
    1.  [1.应用搜索](http://louiszhai.github.io/2018/05/31/alfred/#1-%E5%BA%94%E7%94%A8%E6%90%9C%E7%B4%A2)
    2.  [2\. 文件或目录搜索](http://louiszhai.github.io/2018/05/31/alfred/#2-%E6%96%87%E4%BB%B6%E6%88%96%E7%9B%AE%E5%BD%95%E6%90%9C%E7%B4%A2)
    3.  [3\. 文本内容搜索](http://louiszhai.github.io/2018/05/31/alfred/#3-%E6%96%87%E6%9C%AC%E5%86%85%E5%AE%B9%E6%90%9C%E7%B4%A2)
    4.  [4\. 标记搜索](http://louiszhai.github.io/2018/05/31/alfred/#4-%E6%A0%87%E8%AE%B0%E6%90%9C%E7%B4%A2)
    5.  [5\. 快捷网页搜索](http://louiszhai.github.io/2018/05/31/alfred/#5-%E5%BF%AB%E6%8D%B7%E7%BD%91%E9%A1%B5%E6%90%9C%E7%B4%A2)
    6.  [6\. 书签搜索](http://louiszhai.github.io/2018/05/31/alfred/#6-%E4%B9%A6%E7%AD%BE%E6%90%9C%E7%B4%A2)
    7.  [7\. 计算器](http://louiszhai.github.io/2018/05/31/alfred/#7-%E8%AE%A1%E7%AE%97%E5%99%A8)
    8.  [8\. 词典搜索](http://louiszhai.github.io/2018/05/31/alfred/#8-%E8%AF%8D%E5%85%B8%E6%90%9C%E7%B4%A2)
    9.  [9\. 通讯录搜索](http://louiszhai.github.io/2018/05/31/alfred/#9-%E9%80%9A%E8%AE%AF%E5%BD%95%E6%90%9C%E7%B4%A2)
    10.  [10\. 剪切板搜索](http://louiszhai.github.io/2018/05/31/alfred/#10-%E5%89%AA%E5%88%87%E6%9D%BF%E6%90%9C%E7%B4%A2)
    11.  [14\. 系统常用命令快捷操作](http://louiszhai.github.io/2018/05/31/alfred/#14-%E7%B3%BB%E7%BB%9F%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%E5%BF%AB%E6%8D%B7%E6%93%8D%E4%BD%9C)
    12.  [15.直接唤起指定终端并执行命令](http://louiszhai.github.io/2018/05/31/alfred/#15-%E7%9B%B4%E6%8E%A5%E5%94%A4%E8%B5%B7%E6%8C%87%E5%AE%9A%E7%BB%88%E7%AB%AF%E5%B9%B6%E6%89%A7%E8%A1%8C%E5%91%BD%E4%BB%A4)
    13.  [小结](http://louiszhai.github.io/2018/05/31/alfred/#%E5%B0%8F%E7%BB%93)
4.  [alfred workflow](http://louiszhai.github.io/2018/05/31/alfred/#alfred-workflow)
    1.  [常用的workflow](http://louiszhai.github.io/2018/05/31/alfred/#%E5%B8%B8%E7%94%A8%E7%9A%84workflow)
    2.  [workflow是什么](http://louiszhai.github.io/2018/05/31/alfred/#workflow%E6%98%AF%E4%BB%80%E4%B9%88)
    3.  [如何创建第一个workflow](http://louiszhai.github.io/2018/05/31/alfred/#%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E7%AC%AC%E4%B8%80%E4%B8%AAworkflow)
    4.  [workflow支持什么功能](http://louiszhai.github.io/2018/05/31/alfred/#workflow%E6%94%AF%E6%8C%81%E4%BB%80%E4%B9%88%E5%8A%9F%E8%83%BD)
    5.  [哪些语言能编写workflow](http://louiszhai.github.io/2018/05/31/alfred/#%E5%93%AA%E4%BA%9B%E8%AF%AD%E8%A8%80%E8%83%BD%E7%BC%96%E5%86%99workflow)
    6.  [workflow的不足](http://louiszhai.github.io/2018/05/31/alfred/#workflow%E7%9A%84%E4%B8%8D%E8%B6%B3)
    7.  [我的一些心得](http://louiszhai.github.io/2018/05/31/alfred/#%E6%88%91%E7%9A%84%E4%B8%80%E4%BA%9B%E5%BF%83%E5%BE%97)
5.  [为什么会有这篇文章](http://louiszhai.github.io/2018/05/31/alfred/#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E6%9C%89%E8%BF%99%E7%AF%87%E6%96%87%E7%AB%A0)

我曾经耗费巨大的精力，试图在计算机的使用效率上找到一条优化的捷径，一直以来都收效甚微。直到遇上 alfred，它强大的工作流机制，**彻底解决了输入输出的痛点，极大的减少了程序之间的切换成本和重复按键成本**，这才让我明白，原来计算机可以这么玩。

神奇的魔法帽，alfred 初印象。

![](http://louiszhai.github.io/docImages/alfred/alfred-icon.png)

### [](http://louiszhai.github.io/2018/05/31/alfred/#%E5%A6%82%E4%BD%95%E5%AE%89%E8%A3%85alfred "如何安装alfred")如何安装alfred

首先可以从 [alfred官网](https://www.alfredapp.com/) 自行下载安装，免费用户可以使用除 workflow 以外的其它功能，如需使用 workflow，则需要购买Powerpack。

不建议：自行搜索破解版，或者点个喜欢，留下邮箱找我要…

### [](http://louiszhai.github.io/2018/05/31/alfred/#%E4%B8%80%E4%B8%AA%E4%BE%8B%E5%AD%90%E8%AF%B4%E6%98%8E%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E7%94%A8alfred "一个例子说明为什么要用alfred")一个例子说明为什么要用alfred

以前，使用mac查询一个单词，或者翻译一个单词，我们要么经历五步：

1.  手动打开浏览器
2.  进入谷歌首页
3.  选中输入框
4.  输入或粘贴查询单词，然后空格并加上”翻译” 两个字，然后再回车
5.  等待浏览器展示查询结果;

要么经历四步：

1.  打开翻译应用(比如自带词典)
2.  输入或粘贴查询单词
3.  翻译应用输出查询结果
4.  查询过后，一般都需要Cmd+Q退出应用（或者Cmd+H隐藏词典，亦或Cmd+Tab切换回上一个应用）

查询单词这个场景中，我们至少需要兴师动众，切换或打开一个应用两次，定位输入框一次，输入或复制粘贴一次。且查询结果页也会挡住当前的工作区，使得我们分心，甚至忘记自己刚刚在做啥，总之，体验极不流畅。

alfred 工作流正是为了解决这个问题而设计的。使用 [`有道词典`](https://github.com/Louiszhai/tool/blob/master/workflow/youdao.alfredworkflow?raw=true) workflow，**最快只需两次按键便可查询单词**. 举个栗子🌰：为了查询单词 “workflow”，我会选中单词所在区域，然后按住 Option+Y 键(我已将有道翻译的快捷键设置为 Option+Y)，单词查询结果就出来了，不需要切换应用，同时查询结果也较少的挡住工作区。如下所示：

![](http://louiszhai.github.io/docImages/alfred/alfred-youdao.png)

两次按键就能查询单词，这么好的应用为何不用呢？

### [](http://louiszhai.github.io/2018/05/31/alfred/#alfred%E8%83%BD%E5%81%9A%E4%BB%80%E4%B9%88%EF%BC%9F "alfred能做什么？")alfred能做什么？

对于一个刚刚听说alfred的新手来说，迫切想知道的莫过于了解它能做什么？据我所知，公开的 alfred workflow 至少有 500+，有心网友甚至罗列了一张 [表格][[http://www.alfredworkflow.com/]来管理它，表格的每一行都解锁了一项](http://www.alfredworkflow.com/]%E6%9D%A5%E7%AE%A1%E7%90%86%E5%AE%83%EF%BC%8C%E8%A1%A8%E6%A0%BC%E7%9A%84%E6%AF%8F%E4%B8%80%E8%A1%8C%E9%83%BD%E8%A7%A3%E9%94%81%E4%BA%86%E4%B8%80%E9%A1%B9) alfred 技能（注意并非所有的 workflow 都支持最新的 alfred 3.6.1版本）。你可以下载并免费使用其中任何一个 workflow，甚至，还可以基于一些不错的 workflow 样本，加入创意，改造成属于自己的 workflow（前提是已获得 powerpack license）。

默认情况下，alfred 至少能胜任 15 项工作：

1.  应用搜索
2.  文件或目录搜索
3.  文本内容搜索
4.  标记搜索
5.  快捷网页搜索
6.  书签搜索
7.  计算器
8.  词典搜索
9.  通讯录搜索
10.  剪切板搜索
11.  代码片段搜索
12.  iTunes管理
13.  1Password搜索
14.  系统常用命令快捷操作
15.  直接唤起指定终端并执行命令

获得 powerpack license 的 alfred 将获得强大的 workflows 功能，后续将专门讲解。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#1-%E5%BA%94%E7%94%A8%E6%90%9C%E7%B4%A2 "1.应用搜索")1.应用搜索

输入应用名，列出本地安装的所有相关应用，可以快速唤起。

![](http://louiszhai.github.io/docImages/alfred/alfred-app-search.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#2-%E6%96%87%E4%BB%B6%E6%88%96%E7%9B%AE%E5%BD%95%E6%90%9C%E7%B4%A2 "2\. 文件或目录搜索")2\. 文件或目录搜索

输入 find 或 open 命令，以及待搜索的文件或目录名，列出磁盘中的相关文件，可以快速定位 finder，相当于一个简易的 EasyFind。

![alfred-find](http://louiszhai.github.io/docImages/alfred/alfred-find.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#3-%E6%96%87%E6%9C%AC%E5%86%85%E5%AE%B9%E6%90%9C%E7%B4%A2 "3\. 文本内容搜索")3\. 文本内容搜索

输入 in 命令，以及待搜索的文本，列出磁盘中包含该文本的相关文件，可以快速定位文件，相当于简易的终端 find 命令。

![alfred-in](http://louiszhai.github.io/docImages/alfred/alfred-in.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#4-%E6%A0%87%E8%AE%B0%E6%90%9C%E7%B4%A2 "4\. 标记搜索")4\. 标记搜索

输入 tags 命令，以及待搜索的标记颜色中文名称，列出打上相应标记的目录，可以快速定位标记目录。

![alfred-tags](http://louiszhai.github.io/docImages/alfred/alfred-tags.png)

以上 2、3、4 展示的搜索能力，仅仅是 alfred 提供的冰山一角的小功能（对应于 alfred preferences 面板（`Cmd+,`唤起）— features 栏— file search 功能，如下图所示），理论上可以进行全盘搜索，但由于性能原因，截止 alfred 3.6.1，默认至多展示前40个搜索结果。

![alfred-features](http://louiszhai.github.io/docImages/alfred/alfred-features.png)

对于通常的搜索而言，完全没必要进行全盘搜索，因此只将当前用户目录加进去即可，请参考下图添加用户目录：

![alfred-default-results](http://louiszhai.github.io/docImages/alfred/alfred-default-results.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#5-%E5%BF%AB%E6%8D%B7%E7%BD%91%E9%A1%B5%E6%90%9C%E7%B4%A2 "5\. 快捷网页搜索")5\. 快捷网页搜索

alfred 可以非常方便的打开指定网页（alfred preferences 面板— features 栏— web search），这是一个非常贴心的小功能。默认情况下，alfred 自带了 wiki、twitter、ebay、bing、gmail、yahoo、linkedin、youtube、facebook 等几十种网站的链接，你可以输入关键字如『wiki』空格后再输入搜索内容，最后再回车打开 wiki 网站，如下所示：

![alfred-wiki](http://louiszhai.github.io/docImages/alfred/alfred-wiki.png)

也可以点击此处右下角『Add Custom Search』按钮新增你常用的网页搜索，如下所示：

![alfred-web-search](http://louiszhai.github.io/docImages/alfred/alfred-web-search.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#6-%E4%B9%A6%E7%AD%BE%E6%90%9C%E7%B4%A2 "6\. 书签搜索")6\. 书签搜索

书签搜索是 alfred3.x 版本中新加的功能，方便用户在浏览器的大量书签中快速搜索。

![alfred-web-bookmarks](http://louiszhai.github.io/docImages/alfred/alfred-web-bookmarks.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#7-%E8%AE%A1%E7%AE%97%E5%99%A8 "7\. 计算器")7\. 计算器

alfred 默认提供计算的能力，如下所示。

![alfred-calculator](http://louiszhai.github.io/docImages/alfred/alfred-calculator.png)

输入`=`，还能进行复杂运算，如下。

![alfred-calculator02](http://louiszhai.github.io/docImages/alfred/alfred-calculator02.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#8-%E8%AF%8D%E5%85%B8%E6%90%9C%E7%B4%A2 "8\. 词典搜索")8\. 词典搜索

实际上，自带的词典搜索功能不是很理想，建议搭配 `有道词典` workflow一起使用。

![alfred-dictionary](http://louiszhai.github.io/docImages/alfred/alfred-dictionary.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#9-%E9%80%9A%E8%AE%AF%E5%BD%95%E6%90%9C%E7%B4%A2 "9\. 通讯录搜索")9\. 通讯录搜索

alfred 还可以用来搜索通讯录中的联系人，如下所示。

![](http://louiszhai.github.io/docImages/alfred/alfred-contacts.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#10-%E5%89%AA%E5%88%87%E6%9D%BF%E6%90%9C%E7%B4%A2 "10\. 剪切板搜索")10\. 剪切板搜索

剪切板的管理也是 alfred 的一大亮点，如下所示。

![afred-clipboard](http://louiszhai.github.io/docImages/alfred/alfred-clipboard.png)

如此一来，拷贝多段内容就变得非常容易，借助 alfred，可以在一处连续拷贝，然后另一处连续粘贴，避免了频繁切换应用带来的操作疲劳；同时之前复制过的文本或图片，也不用担心过会找不到。

1.  代码片段搜索，相对 aText 来说，感觉不是特别方便，略过（aText 是 mac 下输入增强工具，输入关键字，自动补全文本）。

2.  iTunes管理使用得不多，略过。

3.  1Password由于未安装，也略过。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#14-%E7%B3%BB%E7%BB%9F%E5%B8%B8%E7%94%A8%E5%91%BD%E4%BB%A4%E5%BF%AB%E6%8D%B7%E6%93%8D%E4%BD%9C "14\. 系统常用命令快捷操作")14\. 系统常用命令快捷操作

通过 alfred 可以快捷地操作系统锁屏、关机、重启、休眠等十几种指令，非常便捷。对于强迫症用户来说，唤起屏保、休眠、清空垃圾篓、退出应用等指令可能较为常用。

![alfred-system](http://louiszhai.github.io/docImages/alfred/alfred-system.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#15-%E7%9B%B4%E6%8E%A5%E5%94%A4%E8%B5%B7%E6%8C%87%E5%AE%9A%E7%BB%88%E7%AB%AF%E5%B9%B6%E6%89%A7%E8%A1%8C%E5%91%BD%E4%BB%A4 "15.直接唤起指定终端并执行命令")15.直接唤起指定终端并执行命令

通过 alfred 可以直接唤起终端窗口，并执行命令，如下所示。

![](http://louiszhai.github.io/docImages/alfred/alfred-shell.png)

以上，Application 若选择『Custom』选项，下方再贴如下一段 applescript 代码，便可以直接在 **iTerm** 中执行命令。

```
on alfred_script(q)
    tell application "iTerm"
        set _length to count window
    if _length = 0 then
        create window with default profile
    end if
    set aa to (get miniaturized of current window)
    if aa then
        set miniaturized of current window to false
    end if
    set bb to (get visible of current window)
    if bb is false then
        set visible of current window to true
    end if
    set cc to frontmost
    if cc is false then
        activate
    end if
        (*if _length = 0 then*)
            set theResult to current tab of current window
        (*else
            set theResult to (create tab with default profile) of current window
        end if*)
        write session of theResult text q
end tell
end alfred_script

```

#### [](http://louiszhai.github.io/2018/05/31/alfred/#%E5%B0%8F%E7%BB%93 "小结")小结

至此 alfred 的 Features 面板功能介绍完毕。alfred 设置界面一共包含10个面板，还有9个面板如下所示：

1.  General（通用，用于设置是否开机启动，及设置唤起快捷键，通常设置为 `Alt+Space` 即可）
2.  Workflows（工作流）
3.  Appearance（外观，用于设置 alfred 输入窗口的外观、字体、颜色等）
4.  Advanced（高级）
5.  Remote（远程，用于远程管理，这意味着你需要在 App Store 购买一个 Alfred Remote 的app，然后便可以在手机上远程操作 mac）
6.  Powerpack（许可证，购买 powerpack 的用户便可以使用 workflow 功能）
7.  Usage（使用统计）
8.  Help（帮助，提供快速上手文档、使用文档、反馈bug、用户论坛等链接）
9.  Update（更新日志，可查看更新日志及更新到最新版）

Appearance 面板除了设置输入窗口的外观外，还有一些外观相关的设置，在这里可以设置默认展示行数等。

![](http://louiszhai.github.io/docImages/alfred/alfred-appearance-options.png)

Advanced 面板包含了一些高级设置，如下所示。

![](http://louiszhai.github.io/docImages/alfred/alfred-advanced.png)

Usage 面板包含了你使用 alfred 的数据统计，如下所示。

![](http://louiszhai.github.io/docImages/alfred/alfred-usage.png)

由此可见，几乎我每天都会用 alfred，3年来总计使用3W+次，平均每天使用27.8次，剔除节假日，工作日每天平均使用次数高达40+次，可以说，alfred 极大的方便了我的工作和生活。

### [](http://louiszhai.github.io/2018/05/31/alfred/#alfred-workflow "alfred workflow")alfred workflow

基本功能介绍完了，终于，我们要一窥 alfred 的核心功能— workflow。工作流可谓是 alfred 最强大的功能，它是秒杀其他效率应用的核心技术，也是最吸引我的地方。

唯有掌握工作流，mac 才能真正起飞。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#%E5%B8%B8%E7%94%A8%E7%9A%84workflow "常用的workflow")常用的workflow

欲了解工作流，先从常用的 workflow 开始，下面简单展示一些典型。

ip查询

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-ip.png)

指定 qq 好友聊天

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-qq.png)

指定微信好友聊天

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-wx.png)

印象笔记搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-en.png)

百度地图搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-bmap.png)

点评搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-dp.png)

豆瓣电影搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-movie.png)

豆瓣书籍搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-book.png)

知乎日报

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-zh.png)

水木清华社区搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-sm.png)

php api 搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-php.png)

jquery api 搜索

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-jq.png)

快递查询

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-kd.png)

finder 设置

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-finder.png)

举例就到这了，另外，这里有我的一些 [afred workflows](https://github.com/Louiszhai/alfred-workflows)，欢迎试玩。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#workflow%E6%98%AF%E4%BB%80%E4%B9%88 "workflow是什么")workflow是什么

你可能很好奇，上面这些 workflow，都是怎么开发的呢？别急，稳住慢慢来。

先问一个问题，什么是工作流？

我们都知道，任何微小的工作，都可以拆分成多个步骤，这些步骤顺序相连，依次进行，最终输出成果，有些步骤可能存在多个分支，并且最终输出多个成果。**这些步骤依次执行，并且向后传递阶段性信息的流，就是工作流**。现实生活中的工作流可能更为复杂，但本质还是如此。正是基于这种现实背景，alfred 从 2.0 版本起加入了 workflow，普通的 workflow 如下所示。

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-yd.png)

这个工作流包含三个步骤：① 查询单词—> ② 格式化输出—> ③ 复制到剪切板。

`yd`是唤起该工作流的命令，输入`yd`，然后空格，接着输入待查询的单词，`script Filter`便开始执行，最终输出查询结果列表（图片见文章开头例子），至此，工作流的步骤①查询单词部分完成。

我们注意到，图中有两条数据流连线，第一条包含节点，这意味着，节点处需要等待用户操作（点击）才能继续下去。一旦用户点击列表项，后续流程②格式化输出，将直接执行，紧接着其后续流程③复制到剪切板也将顺序执行，最终单词查询结果复制到剪切板，工作流结束。

实际上，上图中包含节点的数据流连线，点击时还可指定相应的辅助键，辅助键可选 `none`、`ctrl`、`alt`、`cmd`、`fn`、`shift`之一，默认为 `none`，即无须辅助键。指定辅助键的好处在于，不同的辅助键，可以触发不同的后续流程，如上图则只设计一个后续流程（即②格式化输出流程）。设置辅助键的界面如下所示，可以指定相应提示，以及流程执行时是否关闭 alfred 窗口。

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-modifier.png)

#### [](http://louiszhai.github.io/2018/05/31/alfred/#%E5%A6%82%E4%BD%95%E5%88%9B%E5%BB%BA%E7%AC%AC%E4%B8%80%E4%B8%AAworkflow "如何创建第一个workflow")如何创建第一个workflow

是不是跃跃欲试了，来创建第一个 workflow 吧。

1.  首先，打开 alfred preferences 设置界面，选中第三个面板 Workflows。

2.  点击面板底部左侧的 `+` 按钮，选择 Blank Workflow。

    ![](http://louiszhai.github.io/2018/05/31/alfred/alfred-workflow-create.gif)

3.  补全 workflow 相关信息，最后点 `Create` 按钮保存，如下所示。

    ![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-first.png)

4.  于是第一个空的 workflow 创建好了，接下来我们来搭建一个 google 搜索的工作流，通过这个工作流，我们能快速的选中文本然后使用 google 搜索该文本，不妨参考以下步骤。

    1）新增热键：右键 - Triggers-Hotkey。

    2）热键设置面板中：Hotkey 设置为 `Alt+G`（快捷键必须以 `Ctrl`、`Alt`、`Shift` 或 `Cmd` 开始，而 `Alt` 键很少被软件占用，推荐作为 alfred 的常用修饰键）；Argument 选择『Selection in macOS』（意味着 mac 任何应用选中的文本都会通过 alfred 传给后面的流程），然后保存。

    4）热键保存后，继续添加google搜索的流程：右键 - Actions - Open URL。

    5）Open URL 设置面板中：URL 设置为 `https://www.google.com/search?q={query}`，{query} 即热键流程中选中的文本（alfred 中，流程通过 {query} 关键字接收前面传递过来的参数），然后保存。

    6）最后，将热键流程和 Open URL 流程连线，至此，google 搜索的工作流完成。

    你还可参考如下图示。

    ![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-create-triggers.gif)

是不是非常简单？到目前为止，完全不需要编程基础。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#workflow%E6%94%AF%E6%8C%81%E4%BB%80%E4%B9%88%E5%8A%9F%E8%83%BD "workflow支持什么功能")workflow支持什么功能

截止到 v3.6.1 版本，workflow 支持 Triggers、Inputs、Actions、Utilities（alfred3.x新增）、Outputs 共5项主要功能，如下所示。

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-menu.png)

这5项功能一共包含39个组件。其中

*   输入包含 Triggers（触发器）和 Inputs（输入触发）；Triggers 中的流程可以触发 Inputs 的流程，反之则不行，同时它们都可以触发其它后续流程。
*   输出即 Outputs，包含了通知，放大展示、复制到剪切板，写入文本、播放声音、触发其它流程等。
*   中间 Actions 包含打开文件、在 finder 中展示文件、唤起 app、打开 web search、打开 URL、执行系统命令、执行 iTunes 命令、执行脚本、执行 applescript 脚本、在终端中执行命令等。
*   Utilities 包含了一些公共组件，如变量设置、json 配置、过滤、转换、替换、延时、debug 等。

以上，Hotkey、Keyword、Script Filter 是常用的输入组件，Open URL、Run Script 是高频的 Action 组件，Post Notification、Copy to Clipboard 是受欢迎的输出组件，而 Arg and Vars、Filter、Delay、Debug 是贴心的公共组件。

合理搭配相应的组件，我们就能像搭乐高积木一样搭建 workflow。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#%E5%93%AA%E4%BA%9B%E8%AF%AD%E8%A8%80%E8%83%BD%E7%BC%96%E5%86%99workflow "哪些语言能编写workflow")哪些语言能编写workflow

你可能会说没有编程的 workflow 有什么意思，是的，alfred 除了使用可视化组件，简化搭建 workflow 的难度外，还内置了多种语言支持。我们不需要关心语言之间的交互细节，只需要使用它们接收输入，提供输出，其它事情统统交给 alfred。

目前，我们可以直接使用如下8种语言编写脚本：

*   bash
*   zsh
*   php
*   ruby
*   python
*   perl
*   applescript
*   javascript

你没看错，javascript 也是默认支持的（jser要疯狂了）。除了上述8种语言外，通过bash或zsh，一样可以唤起其它语言，如 java、c、go 等等。

实际上，python 可能是 alfred workflow 中最常用的编程语言，前人编写了大量的 python 脚本，都可以在 alfred 中大放光彩。

请注意，以上编程语言可以在这两个组件中使用：① Inputs -> Script Filter、② Actions -> Run Script。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#workflow%E7%9A%84%E4%B8%8D%E8%B6%B3 "workflow的不足")workflow的不足

本文聊了这么多，workflow的优势就不多说了。

很明显，workflow 不是万能的，很多场景，v3.6.1 的 alfred 还覆盖不到。比如说：

1.  无法监听用户操作，自动录入工作流。对于大多数人来说，编码创造工作流的成本太高，alfred 若能监听一段时间用户操作，将之转换成工作流，无疑工作流入门成本会大幅度降低，同时也能弥补 applescript 语言的不足（未提供 applescript 接口的应用几乎无法编程），当然这个要求很高，比如说alfred可能需要获取输入时光标所在的屏幕位置，被操作应用的坐标、宽高以及输入源（键盘、鼠标等）的操作等。
2.  没有可视化的组件界面，相比 v2.x 版本而言，v3.x 版本中操作依然停留在文本输入输出上，若能多些可视化组件，比如图片展示，图文混排等，那么编程的空间将更大。
3.  不支持常驻窗口，且常驻窗口上可以二次编程。若能在常驻窗口上放置 todolist、便签，以及监听股票走势等等，那么，几乎就能面向 alfred 开发小程序了。
4.  不支持触摸板手势或 touchbar 直接唤起工作流，手势输入或 touchbar 的玩法很多，创意也很多，有很大的想象空间。

当然，可能还有更多更好的 idea，现如今的 alfred 暂不支持，欢迎在评论区回复交流，一起畅想 alfred 的未来。

#### [](http://louiszhai.github.io/2018/05/31/alfred/#%E6%88%91%E7%9A%84%E4%B8%80%E4%BA%9B%E5%BF%83%E5%BE%97 "我的一些心得")我的一些心得

最后，谈谈我开发 alfred workflow 的一些心得。

**关于调试：**

alfred 流程报错不会有通知和提示，因此一旦 workflow 没有按照你的期望提供输出，那就要注意了，打开 debug 窗口，或引入 Utilities -> Debug 组件，看看有没有异常输出。

alfred 虽然支持多种语言的执行，但执行过程中无法单步 debug，这给调试带来了挑战。所以，开发 workflow 时需要及时的进行单元测试，待部分功能完善后，再进行后续开发，避免陷入根据错误输出无法第一时间定位问题的窘境。

**关于alfred选项列表输出：**

我们提供输入，往往是为了获取输出列表，然后选择列表中的一项，执行后续流程。如下所示，列表中的 9 项即**选项列表**。

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-list.png)

实际上，选项列表对应一个 xml 配置，工作流中只需输出配置好的 xml 即可，请参考如下格式。

```
<?xml version="1.0"?>
<items>
    <item uid="" arg="https://www.google.com/search?q={query}&amp;safe=off">
        <title>谷歌一下 {query}</title>
        <subtitle>副标题</subtitle>
        <icon>google-icon.png</icon>
    </item>
    ...
</items>

```

以上，arg 即往后传递的参数，title 标签内填写标题，subtitle 标签内填写副标题，icon 标签内填写当前选项的图标。然后直接使用 shell 的 echo 打印以上 xml，即可输出以上选项列表。

xml 中如果包含链接，则 `&` 需要替换为 `&amp;`。

**关于选项列表多次输出&流程间调用：**

很多时候，一次输入可能不够，若需要多次输入信息，又该如何实现呢？不妨参考如下两种方案：

1.  选项列表的输出依赖 Inputs -> Script Filter 组件，若流程中包含多次输入，顺序引入多个 Script Filter 组件即可。

2.  若需要唤起 ① 其它分支流程（同一个 workflow 不同流程）、② 其它 workflow 中的流程（跨 workflow 调用）或 ③ 回到当前流程源头（重复执行、直到退出），则可给需要唤起的流程头部插入 Triggers -> External 组件，然后该组件所在流程便可通过 applescript 脚本唤起。applescript 脚本如下所示：

    ```
    tell application "Alfred 3" to run trigger "action" in workflow "com.louis.alfred.CRUD_Module" with argument "test"

    ```

    这段代码的意思是：让 Alfred 3 应用，带上参数 “test”，去打开 Bundle Id为 “com.louis.alfred.CRUD_Module” 的 workflow 中名称为 “action” 的触发器所在流程。

以上，方案1实现简单，不可复用；方案2实现略复杂，优点是可复用。你可以稍微感受下我之前写的一个CRUD的workflow（主流程使用了 24 个组件），其中 6 次依赖 External 组件串起流程（见图中红色下划线标出部分）。

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-CRUD.png)

该 CRUD 的 workflow 使用非常简单，如下演示了新增流程去打开 iTerm 并执行 `ll` 命令的过程。

![](http://louiszhai.github.io/docImages/alfred/alfred-workflow-CRUD.gif)

**注意事项：**

根据我的经验，workflow 开发中还需注意以下几点：

*   流程中的节点往后传递参数非常简单，只需往控制台输出即可。但须注意，多个控制台输出会合并到一起，因此除了往后传递参数外，其他情况下都不要往控制台打印文本。通常控制台输出会包含换行符，为避免换行符带来干扰，推荐使用 `echo -n`（bash） 或 `sys.stdout.write`（python）；直接执行 js 时，方法内部的return 即往后传递参数，此时 `console.log` 输出到控制台并不合法。
*   开发中容易出现 utf-8 编码的问题，建议编程中少用或不用中文注释，或者重载 utf-8 编码（python）。
*   如果需要携带参数，去唤起其它应用，applescript 会是个不错的选择。

### [](http://louiszhai.github.io/2018/05/31/alfred/#%E4%B8%BA%E4%BB%80%E4%B9%88%E4%BC%9A%E6%9C%89%E8%BF%99%E7%AF%87%E6%96%87%E7%AB%A0 "为什么会有这篇文章")为什么会有这篇文章

到这，文章就快结束了，从 2015 年 3 月 28 日 接触 alfred 起，我便迷上了它的超强工作流。alfred 几乎可以做任何自动化工作流的事情（只要能用代码描述这个工作流就行），它彻底改变了我对 mac 的认知。此后，我曾多次向团队同学安利并分享它的神奇之处，他们鼓励我开一个在线直播，有偿分享，但对我而言，能写一篇介绍它的文章，几乎是我的荣幸！最后，写得不好的地方欢迎批评斧正，感谢您的阅读！

* * *

