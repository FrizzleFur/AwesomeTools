## Mermaid


### 用 mermaid 画甘特图


2016.08.29 16:48* 字数 822 阅读 366评论 0喜欢 4
今天发现了一个比较好用的画甘特图/流程图的工具：mermaid，官方的介绍是：

“Generation of diagram and flowchart from text in a similar manner as markdown”。
我说好是因为对程序员好，支持命令行操作并且是开源的，貌似还可以整合进 Markdown，不过我没找到相关的案例。

使用在线工具绘制

mermaid 提供了一个在线编辑器，可以迅速在线作图，下面是官方的 demo

sequenceDiagram
A->> B: Query
B->> C: Forward query
Note right of C: Thinking...
C->> B: Response
B->> A: Forward response
生成的效果是这样的:


mermaid-01.png
再来一个甘特图的:

gantt
dateFormat  YYYY-MM-DD
title Shop项目交付计划

section 里程碑 0.1 
数据库设计          :active,    p1, 2016-08-15, 3d
详细设计            :           p2, after p1, 2d

section 里程碑 0.2
后端开发            :           p3, 2016-08-22, 20d
前端开发            :           p4, 2016-08-22, 15d

section 里程碑 0.3
功能测试            :       p6, after p3, 5d
上线               :       p7, after p6, 2d
交付               :       p8, afterp7, 2d
生成的效果:


mermaid-02.jpeg
画甘特图可以参考官方的 Gantt语法文档。

使用命令行绘制

由于 mermaid 使用 nodejs 写的，所以需要 node 环境，这个不多说，根据自己的平台安装好 node 即可。
安装 mermaid 一行命令搞定:


```
npm install -g phantomjs && npm install -g  mermaid
```

完成之后，就可以使用命令行了。
先新建一个文本文件，我们这里就来展示一个甘特图，所以命名 demo.gantt，当然，文件名随意起就好。demo.gantt 文件内容就用上面的甘特图的例子，然后使用命令：

mermaid demo.gantt -w 1920 -s -p -o images
就可以在 images 目录下生成两个文件，一个是 PNG 图片，另一个是 SVG 矢量图。

可以用 mermaid -h 命令查看帮助，这里我贴上刚刚那条命令里用到的参数:

-s --svg       输出 SVG 替代 PNG（试验性的功能）。
-p --png       如果选择保存 SVG，那么加上这个选项可以同时保存 PNG。
-o --outputDir 保存文件的目录（如果不存在会自动创建），默认 `cwd`。
-w --width     生成的 PNG 图片宽度。
整合进 Markdown

事实上，已经有一些类似的工具被整合进 Markdown 了，比如著名的在线 Markdown 编辑器 马克飞象 采用了 flowchart.js 作为流程图引擎，但貌似这个 flowchart 是不支持 gantt 的，所以这里我也用不上。

至于 mermaid，由于我没有找到相关的案例，所以目前只能采用生成图片插入正文或者用在线编辑器生成链接插入这两种办法。

今天无意中在 V2EX 上看到一个帖子: 一款很坂本的 Presentation 工具，无意中发现这个 用 Markdown 编写简洁优美的演示文稿 的工具使用了 mermaid 作为流程图、甘特图的解析器。如果你要在 Markdown 中整合 mermaid，可以参考这个项目 vortex。

一些问题

当然，在使用过程中也发现了一些问题，最大的一个就是甘特图日期中的假期排除。

由于我们每周一般只工作 5 天，所以这时候我要在甘特图中排除周末两天（计算工期需要），当然，如果可能，最好支持法定节假日。

然而官方文档中并没有提及这个功能，所以我找了一下，看到官方 issues 列表中已经有人提过了：Gnatt Chart exclude weekends，作者回应说 mermaid 是使用 d3js 渲染的，所以应该是可以实现这个功能的。

不过貌似要靠我们自己了。。。因为作者的最后一句话是:

Good luck! If you find a solution please post it here for reference.
等我解决这个问题吧~ 😂😂😂


### 参考

[用 mermaid 画甘特图](http://www.jianshu.com/p/8475b09853f0)

