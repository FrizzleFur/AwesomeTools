# 自定义搜索

# 站在 Google 巨人的肩膀上，打造一个信息搜集的利器

09月18日

[![Bestony](https://cdn.sspai.com/2017/09/17/0e4fbebd5468b85aa6be5d7c42221f51.jpg?imageMogr2/quality/95/thumbnail/!60x60r/gravity/Center/crop/60x60)](https://sspai.com/user/769301) 

#### [Bestony](https://sspai.com/user/769301)

#### 责编: [文刀漢三](https://sspai.com/user/136)

目录

1.  [搜索巨人的利器 —— Custom Search Engine](https://sspai.com/post/47192#%E6%90%9C%E7%B4%A2%E5%B7%A8%E4%BA%BA%E7%9A%84%E5%88%A9%E5%99%A8%20%E2%80%94%E2%80%94%20Custom%20Search%20Engine)
2.  [创建一个你自己的搜索引擎](https://sspai.com/post/47192#%E5%88%9B%E5%BB%BA%E4%B8%80%E4%B8%AA%E4%BD%A0%E8%87%AA%E5%B7%B1%E7%9A%84%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E)
3.  [初级玩法：美化你的搜索引擎](https://sspai.com/post/47192#%E5%88%9D%E7%BA%A7%E7%8E%A9%E6%B3%95%EF%BC%9A%E7%BE%8E%E5%8C%96%E4%BD%A0%E7%9A%84%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E)
4.  [中级玩法：优化搜索结果](https://sspai.com/post/47192#%E4%B8%AD%E7%BA%A7%E7%8E%A9%E6%B3%95%EF%BC%9A%E4%BC%98%E5%8C%96%E6%90%9C%E7%B4%A2%E7%BB%93%E6%9E%9C)
5.  [高级玩法：自定义你的搜索引擎](https://sspai.com/post/47192#%E9%AB%98%E7%BA%A7%E7%8E%A9%E6%B3%95%EF%BC%9A%E8%87%AA%E5%AE%9A%E4%B9%89%E4%BD%A0%E7%9A%84%E6%90%9C%E7%B4%A2%E5%BC%95%E6%93%8E)
6.  [总结](https://sspai.com/post/47192#%E6%80%BB%E7%BB%93)

为了在最短时间内找到自己想看的书，我一般会在网络上搜索这本书的书评。然而一本好书的书评有很多，因此如何更加精准地搜索书评，就成为了我的一个需求。

为此，我构建了一个搜索引擎，可以进行**一站式搜索多个网站的书评，实现了快速的信息搜集**。利用它的原理，我们也可以用它来搜索影评、App 测评、音乐评论等内容。今天，我想将这个工具介绍给你，希望它能帮助你更好地做信息搜集。

![同时搜索多个网站的书评](https://cdn.sspai.com/2018-10-02-qtpry.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1 "同时搜索多个网站的书评")

同时搜索多个网站的书评

## 搜索巨人的利器 —— Custom Search Engine

我使用的工具是来自搜索巨人 Google 提供的自定义搜索引擎 Google Custom Search Engine （中文名：Google 自定义搜索）。这个工具可以帮助我们建设一个专属于我们自己的搜索引擎，帮助我们搜索特定几个网站上的内容，优化我们的搜索体验。比如在上面的书评搜索中，我就将内容的来源限制在了我认为几个书评写的不错的地方，比如豆瓣书评、简书等几个网站。

![null](https://cdn.sspai.com/2018-10-02-bmiro.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

## 创建一个你自己的搜索引擎

注：在开始下面的操作步骤前，请确保你已经注册并登录了 Google 账户，且能顺畅访问。

想要创建一个搜索引擎，首先你需要登录 Google 自定义搜索的控制。访问 [https://cse.google.com/cse/all](https://cse.google.com/cse/all "https://cse.google.com/cse/all") ，你会看到这样的界面。

![null](https://cdn.sspai.com/2018-10-02-f8vq0.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

点击上方的 「Add」，或左侧的「新增搜索引擎」，进入到搜索引擎的创建界面。

![null](https://cdn.sspai.com/2018-10-02-Screen%20Shot%202018-10-02%20at%205.49.13%20PM.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

在新增搜索引擎的界面中输入你需要搜索内容的网站、设置搜索引擎界面的语言以及搜索引擎的名称。在点击「创建按钮」，即可成功创建一个搜索引擎。

![null](https://cdn.sspai.com/2018-10-02-yanqu.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

创建完成后，你会看到创建成功的提示，此时你可以点击「公开网址」来访问你的搜索引擎，查看具体的效果。

![null](https://cdn.sspai.com/2018-10-02-phk9g.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

此时的搜索引擎已经可以用了，但是非常得丑，不过不用担心，接下来我们来美化它。

## 初级玩法：美化你的搜索引擎

好看的东西总是能够让我们心旷神怡，接下来我们就来将刚刚非常丑的搜索引擎变得好看起来。

回到自定义搜索控制台，找到我们刚刚创建的搜索引擎，点击搜索引擎的名称，进入到搜索引擎的设置页面，点击左侧的列表中的「外观」，进入到外观设置的界面。

![null](https://cdn.sspai.com/2018-10-02-t0xg1.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

并在外观设置中切换 tab 到 「主题背景」

![null](https://cdn.sspai.com/2018-10-02-i5hhz.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

在主题背景中， Google 为你内置了一些不错的样式，我推荐你试试其中的「**闪亮主题**」：

![null](https://cdn.sspai.com/2018-10-02-hrn8f.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

在闪亮主题中，你可以得到一个蓝灰色背景以及包含了外部纹理的搜索引擎，同时，在搜索结果中，鼠标指向的项目还可以获得一个高亮显示。设置后，你可以回到之前打开的搜索引擎界面刷新一下，看看最新的效果。

但是目前这个界面依然略显单薄，我们可以给他加上我们自己的 Logo。将 Tab 切换到「**自定义**」。

![null](https://cdn.sspai.com/2018-10-02-8ehke.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

在下方的设置项目中，找到「**徽标**」，设置徽标图片的地址并保存。

![null](https://cdn.sspai.com/2018-10-02-jteoi.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

然后回到我们之前打开的搜索引擎界面，查看加入 Logo 后的效果。

![null](https://cdn.sspai.com/2018-10-02-7w9rm.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

你还可以隐藏掉搜索框内的 Google 的标示

![null](https://cdn.sspai.com/2018-10-02-7aq5q.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

在自定义 Tab 中找到 **Google 品牌信息**，将该选项设置为停用 Google 品牌信息即可。

![null](https://cdn.sspai.com/2018-10-02-wf84x.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

展示效果如下：

![null](https://cdn.sspai.com/2018-10-02-0uuh0.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

## 中级玩法：优化搜索结果

目前我们的搜索引擎已经能看了，但是在内容上还不够精准，接下来我们来优化一下内容，让它更好好用。

### 1\. 置顶结果

如果这个搜索引擎不止你在使用，还有朋友、同事在使用，你可以将**一些内容置顶在搜索结果内容的顶部，以达到提醒他们的目的**。

在搜索引擎控制台中，点击左侧的「**搜索功能**」，然后点击顶部的「**置顶结果**」，进入到置顶结果的界面。

![null](https://cdn.sspai.com/2018-10-02-mvqyn.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

接下来我们来试着将少数派的官网置顶在结果中：

1.  点击**启用置顶**右侧的开关，来开启功能。
2.  点击下方的「添加」，来新增一条置顶信息。

![null](https://cdn.sspai.com/2018-10-02-qh254.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

设置完置顶信息的内容后，可以回到之前打开的搜索引擎界面，输入刚刚设置的关键词，就可以看到置顶的内容了，置顶的内容还会默认高亮，提醒搜索者。

![null](https://cdn.sspai.com/2018-10-02-560rc.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

### 2\. 优化

优化可以为我们的搜索加入一个新的关键词，来帮助我们更简单的进行内容的筛选，减少输入的成本。比如，加入新的优化关键词「豆瓣」，这样搜索结果就既包含了我想要搜的关键词，还会包含豆瓣，从而让内容的来源更加的精准。特别是你同时搜索多个网站时，可以借助这个功能来切分不同网站的内容，更加精准的查看内容。

切换到优化 Tab：

![null](https://cdn.sspai.com/2018-10-02-o92mc.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

点击下方的添加，来添加一个新的优化词。

![null](https://cdn.sspai.com/2018-10-02-lsvgv.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

这样，在搜索结果时，你就得到了一个新的 tab ，来区分包含了特定关键词的内容。

![null](https://cdn.sspai.com/2018-10-02-lskpw.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

### 3\. 自动填充

如果你的搜索引擎是特定的行业引擎，你搜索的关键词可能经常使用同一个，在这种情况下，你可以借助自动填充关键词来优化效果。

切换到自动填充 Tab，并点击下方的按钮打开自动填充功能。

![null](https://cdn.sspai.com/2018-10-02-m9vxa.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

然后点击下方的添加按钮，即可添加新的自动填充的关键词。

![null](https://cdn.sspai.com/2018-10-02-5t5dq.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

添加完成后，需要等几个小时，就可以在搜索引擎界面中测试效果了。

### 4\. 同义词

如果你的搜索引擎需要提供给不同层次的人来搜索，比如高级工程师、中级工程师、初级工程师等，在使用时，你可能会发现他们对于同一个词的描述不尽相同，但你可以借助搜索引擎自带的同义词功能来帮助他们优化搜索的结果。

将上方的 Tab 切换为「**同义词**」

![null](https://cdn.sspai.com/2018-10-02-zu4e7.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

并点击下方的「添加」，来添加新的同义词

![null](https://cdn.sspai.com/2018-10-02-n3w8g.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

稍等片刻，就可以在搜索引擎界面测试了。

![null](https://cdn.sspai.com/2018-10-02-j2ejj.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

## 高级玩法：自定义你的搜索引擎

除了上述简单的玩法，你可能还希望得到更好看的效果，比如在上面的介绍中我所展示的那样。这样可能你需要使用一些代码的技巧。不过，别担心，我已经帮你写好了一个示例代码，你只需要复制我的代码，然后，修改其中的部分参数即可。

在本地新建一个文件，名字叫 `index.html`，然后访问 ：[https://github.com/bestony/sspai-cse/blob/master/index.html](https://github.com/bestony/sspai-cse/blob/master/index.html "https://github.com/bestony/sspai-cse/blob/master/index.html")，将其中的代码复制到本地，粘贴进行 `index.html` 中，

然后回到搜索引擎的设置页面，找到其中的搜索引擎 ID，复制这个 ID， 回到 `index.html` 中，

![null](https://cdn.sspai.com/2018-10-02-kn87o.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

找到下面这行代码，替换其中的 `cx` 的值，就完成了基本的配置。

```
// 下方的 cx 的值替换为你的搜索引擎 ID ，可以在搜索引擎-设置-基本设置中获取。
var cx = '015460718854873601070:ygsbxzbiph8';

```

然后，将 index.html 拖到浏览器中打开，就可以看到如前面展示的效果了。
此外，如果你使用我这个模板，我为你推荐一些设置，可以帮助你得到更好的体验效果：

*   在外观设置中，将布局修改为「**全宽**」
*   在主题背景中，切换为「**经典**」
*   在自定义设置中，关闭 Google 徽标展示
*   在自定义设置中，将「搜索框」中的边框颜色设置为「** 3079ed**」
*   在自定义设置中，将「搜索按钮」中的边框颜色设置为「** 3079ed**」，背景颜色设置为「**4d90fe**」。
*   在自定义设置中，将「优化」中的边框颜色设置为「**3079ed**」。

完成上述设置后，刷新一下页面，你看到的效果就是这样的了。

![null](https://cdn.sspai.com/2018-10-02-kjs5r.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

最后，我还在代码中为你指示了一些可以修改的内容，供你自己自定义，构建真正属于你自己的搜索引擎。

![null](https://cdn.sspai.com/2018-10-02-2opk1.jpg?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1)

## 总结

Google 自定义搜索是一个非常不错的工具，它能够帮助我们更好地完成信息搜索的功能。**借助 Google 强大的搜索机制，我们可以根据自己的需求，来自定义和增强搜索引擎的能力，让搜索引擎更符合我们自己的需要。**

随着我们使用得越多，添加的搜索网站越多，我们就越能够获得一个更加精准的搜索引擎。你可以将其应用在一些特定领域或者内容的搜索上，比如电子书搜索、电影搜索、音乐搜索、书评搜索等等，相信会给你带来更好的搜索体验。


## 参考

1. [站在 Google 巨人的肩膀上，打造一个信息搜集的利器 - 少数派](https://sspai.com/post/47192)
