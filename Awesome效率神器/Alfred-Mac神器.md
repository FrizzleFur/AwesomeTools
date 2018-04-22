# Alfred 

![image](http://upload-images.jianshu.io/upload_images/225323-9241e9deef92a341.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

`Alfred` 就是 `Mac` 上最强大的工具台，一个图形化的终端，只有你想不到，没有它做不到。
 
## Alfred功能特性

![image](http://upload-images.jianshu.io/upload_images/225323-3c6ac45878576561.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

Alfred包含了系统的命令，比如重启、锁定、睡眠等。最常用重启 restart。

![image.png](http://upload-images.jianshu.io/upload_images/225323-ab4eab6746203c55.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

* 默认结果 ：当您搜索时没有在关键字前添加搜索词的前提下呈现给您的默认结果。它们默认包含您的应用程序，联系人和首选项，但您可以修改这些以适应您自己的需要。
![](http://oc98nass3.bkt.clouddn.com/15237815699394.png)

* 文件搜索
* 网络搜索
* 计算器
* 字典
* 联系人
* 剪贴板历史
* 片段和文本扩展
* iTunes迷你播放器
* 的1Password
* 系统命令
* 终端

### Alfred搜索

Alfred 有些通用的设置基本都是关于文件操作的：搜索，拷贝路径，预览，在Finder中显示等

#### 默认搜索

![](http://oc98nass3.bkt.clouddn.com/15237822861872.jpg)
![](http://oc98nass3.bkt.clouddn.com/15237829348244.jpg)

#### 网页搜索

1. 根据常用网站的`API`，自定义web搜索
![](http://oc98nass3.bkt.clouddn.com/15234355436697.jpg)

![](http://oc98nass3.bkt.clouddn.com/15237822067498.jpg)

![](http://oc98nass3.bkt.clouddn.com/15237822507084.jpg)

2. 搜索浏览器书签，我主要使用`Chrome`所以这边搜索的是`Chrome`的标签
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
![](http://oc98nass3.bkt.clouddn.com/15194620385807.jpg)
还提供了`in`、`find`、`open`命令，`in`可以在文件中查找内容，╮(✪ω✪)╭这不就是finder的搜索吗？
`find`查找文件所在目录，`open`打开文件

可以设置模糊搜索`Fuzzy Search`， 建议打开使用方向键切换文件层次，灰常方便， 而且，直接可以使用`previous`或者`⌘ + ⌥ + /`来调起之前的文件路径~

当然，你还可以通过`⌥ + ⇣/⇡`来选择多个常用路径╮(✪ω✪)╭，然后使用`⌥ + <-`进行处理（打开,删除,拷贝路径等），或者`⌥ + ->`删除路径

选择文件后，可以通过`Shfit`预览~

![image](http://upload-images.jianshu.io/upload_images/225323-7935c99c626172b6.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)


### 本地文件操作

定位到所需文件后，我们往往需要对其做进一步处理，在回车打开文件前，不妨先按下 ⌥Option + ⌘Command + \，你会发现 Alfred 已经为你准备了解压、复制、分享、查重等数项常用操作，不用在 Finder 中翻来翻去了。
![](http://oc98nass3.bkt.clouddn.com/15237811350855.png)


### 黏贴板

对于一些文案在App间频繁的切换的需求，`Alfred`提供了实用的黏贴板功能：
我设置的快捷键为：`⌘ + ⌥ + C`

Alfred的剪贴板扩展支持所有类型文件的复制历史保存，从文字到 Doc 文档，从 Gif 图片到 .dmg 文件，你的所有复制历史都会被忠实的记录下来。

### Snippets

对于一些经常在登录网址时候需要输入的信息可以利用`Alfred`的Snippets,比如邮箱，电话等
我设置的快捷键：`⌘ + ⌥ + S`

附注：之前用过`Paster`相当于`Alfred`的这2个功能

## 强大的Workflow

Alfred真正强大之处是它的核心思想：把重复的工作抽象成一个`Workflow`,作为一个`Workflow`,一些开发者不断开发出一些常用的，解决他们自身需求的`Workflow`，可以说极大的方便了我们这些用户，这里给出我一些常用的吧。

![image](http://upload-images.jianshu.io/upload_images/225323-6e18493c6db67bb7.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

我使用的`Workflow`列表：

#### Alfred Workflow Pool

1. [Alfred-fixum](https://github.com/deanishe/alfred-fixum/releases/tag/v0.6) OSX 10.12.6提升了安全性，一些旧的`WorkFlow`需要更新

2. [Packal——Alfred Workflows](http://www.packal.org/) WorkFlow Pool [packal-workflow-search](http://www.packal.org/workflow/packal-workflow-search)

3. [Alfred-Workflows-Zhihu](https://zhuanlan.zhihu.com/AlfredWorkflow)

4. [Top-workflow](https://github.com/zhaocai/alfred2-top-workflow) Mac Helper, better than kill-process; Use  -c, -m, -i, glance，结合快捷键，爽到爆~[Mac10.13后问题的解决](https://github.com/zhaocai/alfred2-top-workflow/issues/19)

5. [Markdown-img-upload](https://github.com/tiann/markdown-img-upload): markdown图片实用工具，Save your time

6. [Copy-Path](https://github.com/hzlzh/Alfred-Workflows/raw/master/Downloads/Copy-Path.alfredworkflow) 获取文件路径，可以使用HotKeys，有了它再也不用很傻的把文件拖到终端了 = =

7. [Last-changed-files](https://github.com/hzlzh/AlfredWorkflow.com/blob/master/Downloads/Workflows/Last-changed-files.alfredworkflow) 经常来回打开文件，要重复的去找，现在这活交给你啦~

 8. [o3o](http://link.zhihu.com/?target=http%3A//workflow.buddysoft.cn/2016/05/06/workflow)怎么能少了表情包呢？颜文字╮(✪ω✪)╭
 
9. [斗图神器](https://github.com/KilluaChen/Dou-figure-alfred-workflow)

10. [Dash Alfred Plugin](https://github.com/omz/Dash-Plugin-for-Xcode) 

11. [Douban](http://link.zhihu.com/?target=http%3A//workflow.buddysoft.cn/2016/04/29/workflow)快速搜索豆瓣的电影、书籍和音乐

12. [Github Search](http://www.packal.org/workflow/github-search) Search Github

13. [V2EX.alfredworkflow](https://github.com/hzlzh/Alfred-Workflows/raw/master/Downloads/V2EX.alfredworkflow) V2EX.alfredworkflow

14.  [StackOverflow Search](http://www.packal.org/workflow/stackoverflow-search) 程序员必备，虽然没怎么用 = = 

15.  [AkikoZ/alfred-web-search-suggest: Alfred search suggest workflow for various popular websites.](https://github.com/AkikoZ/alfred-web-search-suggest/releases)Alfred Web Search Suggest 知乎淘宝常用搜索Workflow

16. [alfred-mweb-workflow](https://github.com/tianhao/alfred-mweb-workflow)搜索、打开MWeb 内部文档和外部文档

### 其它细节功能

#### 计算器

计算器大概是启动器应用们的标配功能了，Alfred 也不例外。只需键入算式，Alfred 就会直接给出正确答案，直观快捷。支持完善的函数语法.

![](http://oc98nass3.bkt.clouddn.com/15237811833233.png)

#### 系统命令

Alfred集成了系统命令。
![](http://oc98nass3.bkt.clouddn.com/15238122248019.png)

而有了 `Alfred`，你就可以通过简单几个字符执行系统命令。ejectall 帮助你弹出所有挂载卷宗、forcequit 可以强制退出指定 App，sleepdisplays 则能在不睡眠的情况下关闭屏幕。

![](http://oc98nass3.bkt.clouddn.com/15238125152699.jpg)

### 其它贴心细节

你可以按下 `⌘Command + L` 居中放大显示结果，方便视力障碍者.
![](http://oc98nass3.bkt.clouddn.com/15238127081328.jpg)


## 使用Alfred

最方便的使用就是设置`double ⌘`唤起`Alfred`啦~
![image](http://upload-images.jianshu.io/upload_images/225323-376fbeab62b6fb09.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

### 使用情况

`Alfred`提供了使用频率的报表，可以看到使用`Alfred`的频率
![image](http://upload-images.jianshu.io/upload_images/225323-9ba66d965b5acd3a.jpg?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)

## 常见问题

1. [和谐版的Alfred 3 在每次开机后，都会提示“是否允许访问通讯录”的弹窗，让人不胜其烦。](http://xclient.info/a/761216bf-0737-5592-0ba8-8fbc5f31b3e6.html?_=75ebe0a762462e5265640b26094a4fdb)

Solution: 打开终端（或iTerm2）

```
sudo codesign -f -d -s - /Applications/Alfred\ 3.app/Contents/Frameworks/Alfred\ Framework.framework/Versions/A/Alfred\ Framework
```

2. [Top-workflow](https://github.com/zhaocai/alfred2-top-workflow) Doesn't work on OSX 10.13 #19

Solution: 
下载fixed[Top.Processes.v2.2.alfredworkflow](https://github.com/singhprd/alfred2-top-workflow/releases/download/v2.2/Top.Processes.v2.2.alfredworkflow)
参考[Mac10.13后问题的解决](https://github.com/zhaocai/alfred2-top-workflow/issues/19)

## 参考文章（TODO）

*  [Alfred Features](https://www.alfredapp.com/help/features/)

*  [总是在 Mac 「装机必备」看到的搜索利器 Alfred，究竟是怎么用的？| 新手问号 - 少数派](https://sspai.com/post/43973)



