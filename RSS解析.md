# RSS

### 用 TINY TINY RSS 自建 RSS 服务

## [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#1-%E5%AF%BC%E8%A8%80)1\. 导言

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#11-%E4%B8%BA%E4%BB%80%E4%B9%88%E8%A6%81%E8%80%83%E8%99%91%E8%87%AA%E5%B7%B1%E6%90%AD%E5%BB%BA-rss-%E6%9C%8D%E5%8A%A1)1.1 为什么要考虑自己搭建 RSS 服务

Google Reader 在 2013 年的下线似乎标志着 RSS 黄金时代的结束。在那之后，虽然陆续出现过很多替代品，但 RSS 的地位已经被无限刷新的信息流、算法推荐等新技术逐渐取代了。

不过，尽管小众，RSS 仍然是不少极客用户获取信息的首选。的确，如果对信息来源要求苛刻且善加维护，RSS 仍然是高效获取信息的不二选择。当然，为了充分发挥 RSS 的优势，一个好用的 RSS 服务也是很重要的。但是，「好」的标准又是什么呢？

在多年日常将 RSS 作为主要信息来源之一、并尝试了多种主流的 RSS 服务之后，我认为**一个合格的 RSS 服务应当满足下列要求：**

1.  同步及时；
2.  订阅源管理便捷、支持导入/导出；
3.  设计简洁、适合阅读、可定制；
4.  客户端支持全面；
5.  可自定过滤规则。

对于上述需求中的前几项，目前常见的 RSS 服务各有侧重。例如，最常见的 Feedly 在界面美观程度上较为突出，而 Inoreader 则在订阅源的管理上功能更为全面等，但并不存在一个全能选手。而至于最后一项需求，即自定规则对文章进行过滤，这些主流服务就显得特别「吝啬」了，要么不提供这样的功能，要么作为收费服务额外提供。

![Feedly 和 Inoreader 的功能界面](https://i.loli.net/2017/10/16/59e4426432675.png)Feedly 和 Inoreader 的功能界面

这当然可以理解：过滤功能需要占用额外的计算资源，这对原本就属小众的 RSS 服务来说是一笔不小的额外开销。但即便如此，仅仅为了实现这样一个并不算复杂的需求，而每月花数美元的价格（Inoreader 高级版年费为 30 美元），未免让人感到有些不值得。

相比之下，虚拟服务器如今已经卖到了白菜价。国外主流的平价主机商在竞争压力下，纷纷推出了低至 5 美元甚至 2.5 美元月付的计划；而国内的互联网大厂则在「云计算」的热潮中，竞相对自家的「云主机」进行优惠促销，其中面向学生的优惠往往可低至 10 元。这就在价格上追平甚至优惠于上述 RSS 服务的定价。

更何况，一台服务器运行的是完整的 Linux 操作系统，其功能用途远不止于搭建 RSS 服务一项，在类似的价格下，性价比可谓完胜；对于注重隐私的用户来说，自建服务附带地带来的安全性也是附加值之一。可见，用订阅 RSS 高级服务的费用投资一台虚拟服务器并自己实现类似功能是非常可行的选择——这正是我们今天的主题。

（关于主机服务商的选择，本文无意讨论，网络上有很多评测信息可供参考，请根据自己的需求和网络环境选择。**主机的内存最好在 512 MB 以上，且必须采用 KVM 架构。**如果你订阅的国外 RSS 源偏多，请注意国内主机的网络可能不能胜任。）

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#12-%E4%B8%BA%E4%BB%80%E4%B9%88%E9%80%89%E6%8B%A9-docker-%E4%B8%8B%E7%9A%84-tiny-tiny-rss)1.2 为什么选择 DOCKER 下的 TINY TINY RSS

如果要为了实现 RSS 功能而自己从头造一个轮子，那必然是一个不现实也不经济的选择。事实上，开源社区已经为我们提供了许多现成的解决方案，只要选择一个并将其安装到主机上，即可快速搭建起自己的 RSS 服务。目前，比较完善、处于活跃开发状态的开源方案当属 [Tiny Tiny RSS](https://tt-rss.org/)，它基本满足了前面提到的各项鉴别标准，后文也将以其为例演示。

关于安装方式，固然可以选择像对待普通 Linux 软件那样直接安装，官方对此也提供了较为详细的文档，但本文更推荐使用 **Docker 镜像方式**安装 Tiny Tiny RSS。

如果你还不了解 [Docker](https://www.docker.com/)，可以简单将其理解为一种模块化的安装方式：它既具有虚拟机方式安装软件的一些长处，如对安装和卸载对宿主系统影响小、软件之间相对隔离、安全性佳等，又保留了普通方式安装软件的优点，如资源消耗较小、软件间通信较为方便等。因此，Docker 方式安装是软件「尝鲜」相当合适的选择。另外，如果你是 iOS 用户，更有 [HyperApp](https://itunes.apple.com/us/app/hyperapp-docker-automation-ssh-terminal/id1179750280?mt=8) 这样便捷的可视化工具辅助 Docker 环境的配置和管理。

## [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#2-%E5%AE%89%E8%A3%85)2\. 安装

用 Docker 方式安装 Tiny Tiny RSS 需要的软件条件是：

*   **Docker CE：**用于提供 Docker 运行环境。
*   **PostgreSQL/MySQL 数据库：**用于存储 RSS 服务运行所需的记录。Tiny Tiny RSS 的作者推荐优先选用 PostgreSQL，以获得更好的性能。
*   **Tiny Tiny RSS 本身**

需要指出的是，Linux 下安装软件的途径是相当灵活的，在软件源、发行版本、使用命令乃至前后顺序上都有不同程度自由裁量的空间。因此，下面的安装步骤仅为示例，目的是用最少的步骤实现安装，并假定读者和笔者一样，理解浅显的 Linux 命令含义、但并不熟悉复杂或具体的技术细节。

首先，SSH 到你的主机，安装 Docker 环境：

```
$ curl https://get.docker.io/ | sh

```

* 如果你的主机位于国内，则使用上述脚本安装 Docker 可能较慢。为此，可以换用 DaoCloud 提供的、换用了国内镜像的安装脚本：

```
$ curl -sSL https://get.daocloud.io/docker | sh

```

之后，安装一个 PostgreSQL 的 Docker 镜像：

```
$ docker run -d --name ttrssdb nornagon/postgres

```

(请注意上述 PostgreSQL 镜像并非官方提供，在此选用的原因是其预先配置好了可以直接配合下述 Tiny Tiny RSS 镜像使用的数据库环境，无须进一步设置。)

最后，安装 Tiny Tiny RSS 本身的 Docker 镜像：

```
$ docker run -d --link ttrssdb:db -p 80:80 -e SELF_URL_PATH=http://example.org/ttrss fischerman/docker-ttrss

```

上述命令中的一些关键部分：

*   `-p 80:80`：该参数表明，将该容器内应用的 80 端口（冒号后）映射到主机的 80 端口（冒号前）上。如果你的主机还需运行其他 80 端口的服务（如博客建站），则应将冒号前的值改为一个未被占用的端口。例如，`-p 8080:80` 将启用主机的 8080 端口。
*   `-e SELF_URL_PATH=http://example.org/ttrss` ：该参数表明，该 Tiny Tiny RSS 应用将可从 `http://example.org/ttrss` 访问。如果你在上一步保持了默认的端口设置，则直接将上述网址换为你主机的 IP 地址（或解析至该主机的域名）即可，否则，应在地址之后进一步表明使用的端口，如：`http://xxx.xxx.xxx.xxx:8080`。

## [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#3-%E5%9F%BA%E6%9C%AC%E4%BD%BF%E7%94%A8)3\. 基本使用

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#31-%E5%88%9D%E6%AC%A1%E9%85%8D%E7%BD%AE)3.1 初次配置

安装完成后，访问在上述步骤中设置的网址，即可进入 Tiny Tiny RSS 的 Web 界面。系统默认的管理员账号是 `admin`，密码是 `password`。

![Tiny Tiny RSS 主界面](https://i.loli.net/2017/10/16/59e442640a360.png)Tiny Tiny RSS 主界面

登录后，首先点击 右上角的 **Actions…** > **Preferences…** 进入设置页面，进行一些基本配置。

![Tiny Tiny RSS 设置界面](https://i.loli.net/2017/10/16/59e44263bed2b.png)Tiny Tiny RSS 设置界面

*   Personal data / Authentication 板块：登录后应立即在此**设置新密码**。
*   Preference 板块：
    *   Default feed update interval：设置刷新订阅源的时间间隔，应根据自己查看 RSS 的频率和服务器的性能合理安排。考虑到 RSS 一般无须即时性，一般最短 30 分钟的间隔足矣。
    *   Enable API access：提供第三方 RSS 客户端支持，**务必勾选**。
    *   Language：语言设置，其中包括简体中文，但翻译质量和完成度均不佳，故本文仍以英文界面为准。
    *   Purge articles after this number of days：在指定日期后清除缓存的文章。考虑到目前主流主机服务均以小容量 SSD 存储为主，应合理设置此处期间，以避免占用过多空间，如 30 日。
    *   Time zone：设置时区，国内一般设为 **Asia/Shanghai** 即可。
    *   Combined feed display：设置阅读界面布局。默认为两栏式，点击文章列表中的标题后，全文将在标题下展开。如习惯 Reeder 一类传统 RSS 客户端的三栏式布局，取消该项勾选。

完成后，点击页面底部的 **Save configuration** 保存配置。

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#32-%E5%AF%BC%E5%85%A5-%E6%B7%BB%E5%8A%A0%E5%92%8C%E7%AE%A1%E7%90%86%E8%AE%A2%E9%98%85)3.2 导入、添加和管理订阅

如果你之前使用过其他 RSS 服务，那么直接将订阅源导入即可。方法是：在之前的 RSS 服务后台找到导出为 XML/OPML 的选项，然后在 Tiny Tiny RSS 中进入设置的 **Feeds** 标签页下的 **OPML** 板块，选择相应文件导入即可。原有的文件夹结构会被保留。

导入后，可在 **Feeds** 标签页管理订阅源。Tiny Tiny RSS 提供的管理选项非常详尽，并可以通过拖动来实现排序、分类操作。点击某个订阅源，可以打开更详尽的设置选项。其中比较实用的功能包括自定义订阅源名称、更新频率等。

![Tiny Tiny RSS 的订阅管理](https://i.loli.net/2017/10/16/59e4426406e03.png)Tiny Tiny RSS 的订阅管理

此外，Tiny Tiny RSS 还提供了一些用于辨识订阅源「健康度」的实用功能。如果有某些订阅源无法连接或长期不更新，那么订阅页面中会分别多出 **Feed with errors** 和 **Inactive feeds** 的选项，点击即可查看这些订阅源的出错记录或最后更新时间，并直接批量退订。

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#33-%E6%96%87%E7%AB%A0%E8%BF%87%E6%BB%A4)3.3 文章过滤

如前所述，强大的过滤功能是促使笔者转投 Tiny Tiny RSS 的首要动力，也是高效处理大量 RSS 订阅源的重要工具之一。Tiny Tiny RSS 的过滤功能分为**匹配**和**动作**两个环节，即先根据一定的规则筛出特定文章，然后自动对其实行某种处理。前后两个环节都是可以高度自定义的。

在设置页面中，点击 **Filters** 标签即可进入过滤设置。首先通过 **Create filter** 按钮新建一个过滤器。弹出的窗口中，**Caption** 部分用于指定规则的名称，**Match** 部分用于设置匹配规则，而 **Apply actions** 部分则指对被匹配的文章应采取何种操作。

点击 **Match** 部分的 **Add** 按钮即可添加匹配规则。你可以指定匹配标题、全文还是两者均匹配，每个匹配规则适用于哪些订阅源。匹配规则支持正则表达式，例如，如果想过滤英文科技博客中常见的赞助广告，那么可以在过滤规则中填入 `(S|s)opnsor`，这样含有「sponsor」或「Sponsor」的结果都会被匹配。同一个过滤器中可以容纳多个匹配规则，多个规则间默认是相「与」的关系，如果想改为「或」的关系，则须勾选窗口下方的 **Match any rule**。

![Tiny Tiny RSS 的过滤设置](https://i.loli.net/2017/10/16/59e44263efdcd.png)Tiny Tiny RSS 的过滤设置

对于被筛出的文章，可以选择的操作很多，如标为已读、完全忽略、打上星标等等，并且可以同时适用多个操作。一个比较有趣的操作是 **Publish article**，它会将文章发布到一个 RSS 源中（该 RSS 地址可在 **Feeds** 选项卡的 **Published & shared articles**区域看到）。进而，结合 IFTTT、即刻等支持检测特定 RSS 源更新的服务，就可实现**特定主题实时推送**、自动发送到稍后读等高级功能。

![用 IFTTT 即时推送 Tiny Tiny RSS 筛选出的主题](https://i.loli.net/2017/10/16/59e44263c308b.png)用 IFTTT 即时推送 Tiny Tiny RSS 筛选出的主题

不过，过滤功能是比较消耗资源的，如果设置过多的过滤条件，可能给你的主机带来较大压力，因此不应滥用该功能。换个角度来说，当你发现自己将精力不成比例地花在过滤功能上、而非静心阅读文章上时，**最应该做的应该不是继续调试过滤、而是清理订阅源。**

## [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#4-%E7%94%A8%E6%8F%92%E4%BB%B6%E6%B7%BB%E5%8A%A0%E4%B8%BB%E9%A2%98-%E5%85%A8%E6%96%87%E8%BE%93%E5%87%BA%E5%92%8C%E5%A4%9A%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%94%AF%E6%8C%81)4\. 用插件添加主题、全文输出和多客户端支持

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#41-%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98)4.1 安装主题

前面提到，RSS 服务质量的衡量尺度之一即是界面的设计水平。在这方面，Tiny Tiny RSS 只能说是基本合格：其界面虽然功能全面、且总体上可称之为简洁明了，但细看还是给人一种开源软件常有的「未经打磨」之感。好在 Tiny Tiny RSS 的界面完全基于 CSS，可自行定制或导入主题，这就为「美容」提供了可能。

Tiny Tiny RSS 用户社区产生的主题并不多，但也有不乏几个完成度较高的，如[仿 Feedly](https://github.com/levito/tt-rss-feedly-theme) 和[仿 Google Reader](https://github.com/naeramarth7/clean-greader) 的两个主题。下面以前者为例演示如何安装。

首先获取主题文件：

```
$ wget https://github.com/levito/tt-rss-feedly-theme/archive/master.zip

```

然后解压缩该主题[[1]](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#fn1)：

```
$ unzip master.zip

```

由于我们的 Tiny Tiny RSS 运行在相对隔离的 Docker 环境中，因此不能像平时那样直接用 `cp` 命令拷贝文件。为此，首先执行：

```
$ docker ps

```

终端将返回当前运行的 Docker 容器列表。我们找到 IMAGE 一列为「fischerman/docker-ttrss」的那行记录，记下同行中 CONTAINER ID 列下的内容。

![找到 Tiny Tiny RSS 的 Container ID](https://i.loli.net/2017/10/16/59e44263d10a2.png)找到 Tiny Tiny RSS 的 Container ID

然后，用 `docker cp` 命令将上述主题文件拷贝到容器中：

```
$ docker cp tt-rss-feedly-theme-master/feedly.css [[CONTAINER ID]]:/var/www/themes
$ docker cp tt-rss-feedly-theme-master/feedly [[CONTAINER ID]]:/var/www/themes

```

请注意将上面命令中的 `[[CONTAINER ID]]` 替换为你在上一步中获得的内容。

这时，我们就可以在 Preference 页面的 Theme 选项中看到 `feedly.css` 了。本文截图中的界面均为该主题的效果。

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#42-%E9%85%8D%E7%BD%AE-rss-%E5%85%A8%E6%96%87%E8%BE%93%E5%87%BA)4.2 配置 RSS 全文输出

很多网站之所以不欢迎 RSS，一个主要的原因就是提供 RSS 会**分走主站的流量**；因此，一些网站即便保留了 RSS 订阅源，也做得十分「不情不愿」，只「抠门」地给出前两三段的内容，要看全文还得跳转到网站才行。这显然会破坏 RSS 的阅读体验。于是，获取全文的功能就显得十分必要了；很多 RSS 服务或客户端也将其作为 Premium 订阅的卖点之一。不过，通过 Tiny Tiny RSS，我们同样可以免费实现这一效果。

事实上，Tiny Tiny RSS 原本已经内置了基于 Readability 的全文输出服务，但可惜这家服务在前段时间已经跑路，关闭了 API 接口，我们只能另请高明。目前，比较好的替代方案是 [Mercury](https://mercury.postlight.com/web-parser/)，这也是 Reeder、Unread 等主流 RSS 阅读器在近期更新中改用的方案。

首先，Mercury 的全文输出服务是免费的，但需要配合 API 密钥使用，这可以在[注册](https://mercury.postlight.com/web-parser/)后在其网站的 Web Parser 页面看到。

接着，为 Tiny Tiny RSS 安装[全文输出插件](https://github.com/WangQiru/mercury_fulltext_for_tt-rss)，其方法与安装主题完全相同[[2]](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#fn2)：

```
$ git clone https://github.com/WangQiru/mercury_fulltext.git
$ docker cp mercury_fulltext [[CONTAINER ID]]:/var/www/plugins

```

安装后，到 Tiny Tiny RSS 的设置页面中启用名为 **mercury_fulltext** 的插件。这时，在设置页面的 **Feeds** 选项卡下，就会多出一个该插件的设置区域。我们将之前获得的 Mercury API 密钥填入文本框中，并点击 **Save** 保存配置。

![Mercury 的设置](https://i.loli.net/2017/10/16/59e44263d1d61.png)Mercury 的设置

完成上述准备工作后，就可以针对特定的订阅源启用全文输出了。方法是：在订阅源管理中，点击需要获取全文的订阅源，在弹出的 **Edit Feed** 对话框中，勾选 **Plugins** 选项卡中的 **Get fulltext via Mercury Parser**。

该插件的效果如下（The Verge）：

![全文输出 The Verge 的效果](https://i.loli.net/2017/10/16/59e4426406e1e.png)全文输出 The Verge 的效果

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#43-%E8%AE%A9%E6%9B%B4%E5%A4%9A%E5%AE%A2%E6%88%B7%E7%AB%AF%E6%94%AF%E6%8C%81-tiny-tiny-rss)4.3 让更多客户端支持 TINY TINY RSS

在 RSS 的使用体验中，客户端是十分重要的一环；缺少第三方客户端支持的 RSS 服务注定只能是「孤家寡人」。然而，作为一个小众的开源软件，Tiny Tiny RSS 在这方面显然不能与那些商业服务相比。主流的客户端软件中，只有 Fiery Feed 提供了对 Tiny Tiny RSS 的原生支持。

好在开放的插件系统这时再次发挥了作用。借助第三方插件，Tiny Tiny RSS 可以将自己模拟为另一个自建 RSS 工具——Fever，而后者的客户端支持更为全面，包括 Reeder、Unread 等。[[3]](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#fn3)

第一步仍然是安装插件：

```
$ git clone https://github.com/rannen/tinytinyrss-fever-plugin.git
$ docker cp fever [[CONTAINER ID]]:/var/www/plugins

```

安装后，在 Tiny Tiny RSS 的设置页面启用名为 **fever** 的插件。保存后，再次进入设置时，**Preference** 选项卡下会多出一个名为 **Fever Emulation** 的板块。在该板块的文本框中，设置一个专用于该插件的密码，然后点击 **Save**。该文本框下方同时给出了一个**独立的服务器地址**，其格式类似于 `http://rss.example.org/plugins/fever/`。将其记下以备后用。

![在 Reeder 中配置 Tiny Tiny RSS](https://i.loli.net/2017/10/16/59e44263f2840.png)在 Reeder 中配置 Tiny Tiny RSS

这时，在 Reeder 等 app 中，只要在添加 RSS 账号时选择 Fever，在服务器地址栏填入上述地址，即可配合这些你惯用的 app 使用 Tiny Tiny RSS 了；文件夹、标为已读、星标等功能均被良好支持。

![在 Reeder 中使用 Tiny Tiny RSS 的效果](https://i.loli.net/2017/10/16/59e4426ca61a6.png)在 Reeder 中使用 Tiny Tiny RSS 的效果

### [](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#5-%E6%80%BB%E7%BB%93)5\. 总结

以上就是使用 Tiny Tiny RSS 自建 RSS 服务的全过程。可以看出，虽然听起来很 geeky，但实际操作比想象的简单很多，稍微熟悉后不到半个小时就可架起服务并使用。从我两个月的使用体验看，它基本已经完全代替了之前对 Feedly 和 Inoreader 的需求，且无论是灵活性还是性价比都是第三方服务无法比拟的。

当然，一旦涉及到这种 DIY 操作，总是要回应的质疑是：这么做值得吗？毕竟，「RSS 已死」不是什么新鲜论调了。这么说的人中，有的是 RSS 曾经的忠实用户，感慨曾经活跃的第三方软件和服务逐渐冷却；有的是新世代新闻、阅读服务的开发者，鄙弃 RSS 的老旧和刻板。

然而，RSS 说到底是一个**协议**。而协议只在一种情况下可以被宣告死亡：再也没有人使用的时候。诚然，如果只论 RSS 最「原教旨」的形态，其占有率确实几乎可以忽略不计了；但当下那些看起来更「现代」的资讯工具，尽管可以在界面、交互上不断翻新，但其本质仍然是一个时间线上的信息流，其中每篇内容包含的要素仍然是标题、时间、正文等 RSS 已经涵盖的要素。易言之，它们归根结底都是 RSS 的衍生物。从这个角度看，RSS 没有死、也不会死。

必须承认，新技术加持下的现代工具在配置和使用上都远比 RSS 来得便利和舒适。但，在获得便利的同时，你也将选择的权利让渡给了机器，将偏好和隐私让渡给了第三方；在追求舒适的另一面，是被无限信息流淹没的宝贵时间，和被算法推荐不断强化的「回音壁」效应。相反，RSS 是有限的，因此也是克制的；是刻板的，因此也是高效的；是不智能的，因此也是包容的。

在今天，坚持使用 RSS，能让你真正认真思考自己对信息的需求，在喧闹而充满误导和诱惑的信息海洋中守住自己对信息获取的控制权；而自建 RSS 服务，则是维护这种控制权的终极途径。

* * *

1.  有的系统可能没有安装 `unzip` 命令，这时可先运行 `apt-get unzip` 安装该功能。 [↩︎](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#fnref1)

2.  要运行 `git` 命令，你的主机需要先安装 `git`；如果运行时提示未安装，请使用 `apt-get git -all` 命令来安装。 [↩︎](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#fnref2)

3.  遗憾的是，Fever 也在去年圣诞节前夜[跑路](https://shauninman.com/archive/2016/12/24/goodbye_mint_goodbye_fever)了，这也是它没有成为本文主角的原因。 [↩︎](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/#fnref3)
## 参考

1. [用 Tiny Tiny RSS 自建 RSS 服务 · Neverland](http://cyhsu.xyz/2017/10/16/use-ttrss-to-build-a-self-hosted-rss-service/)
2. [如何搭建属于自己的 RSS 服务，高效精准获取信息 - 少数派](https://sspai.com/post/41302#3.1%20%E5%AE%89%E8%A3%85%E4%B8%BB%E9%A2%98)
3. [论 RSS 的「复兴」 - 少数派](https://sspai.com/post/43998)