# 定期自动云备份 macOS 软件列表，维护一份属于自己的必备 App 清单

## 原理

分别获取各个途径的Apps,写入到文件中，然后通过读取文件进行安装。

## BackupAppList

看一下我做的`BackupAppList`的Macro.

![BackupAppList1](http://oc98nass3.bkt.clouddn.com/BackupAppList1.jpg)
![BackupAppList2](http://oc98nass3.bkt.clouddn.com/BackupAppList2.jpg)

## Todo

就需要添加2个事情：

1. 添加备份日志
2. 添加确认Trigger，方便确认后再进行安装
3. [狡兔三窟——云备份软件列表与相应配置，补充 Time Machine](https://sspai.com/post/43479)



本文分为 备份软件列表 和 备份配置文件 两部分。其中，Mackup 备份配置文件的原理为：将配置文件转移到iCloud、Dropbox、Google Drive 等云同步文件夹以实现备份和同步，在配置文件的原来位置生成一个软链接（相当于贴一张写有新位置的告示），从而让软件读取到新位置的配置。这种情况下，如果你删除了云同步文件夹中的配置文件，就什么都没有了！就什么都没有了！就什么都没有了！而且，mackup支持备份的软件有限（可自己配置以支持更多软件）。所以，小白慎用！感觉挺鸡肋的。



[![涔C](https://cdn.sspai.com/2018/06/15/66eceba0642e3493a7c9b7d5570654e3.jpg?imageMogr2/quality/95/thumbnail/!60x60r/gravity/Center/crop/60x60)](https://sspai.com/user/742287) 

#### [涔C](https://sspai.com/user/742287)

每个人都会积累一套自己习惯使用的 App。如果平时习惯使用 Time Machine 备份，那么在重装系统时，直接用它还原倒是一个不错的办法，不必再手动安装一个个 App。但是有些时候，我们可能想要一个更加「干净」的新系统，此时就需要依次手动安装。这显然不是个高效、省心的方法，可能还需要一个个回忆之前用的 App。这时候，我们往往希望有一份属于自己的 App 清单，最好还能在重装时一键安装，省心省力。

本文受到 [给 Mac 优雅地一键「装机」](https://sspai.com/post/43239 "给 Mac 优雅地一键「装机」") 启发，内容分为两个部分：

*   通过简单的设置，做到 **定期自动云备份** macOS 软件列表
*   使用列表文件，「一键」安装大部分软件

## 一、备份

一般而言，macOS 中软件来源及其安装位置有以下几种：

*   Mac App Store 安装，位置：/Applications
*   手动下载安装，位置：/Applications
*   Homebrew 安装，位置：/usr/local/Cellar，主要是一些命令行工具
*   Homebrew Cask 安装，位置：/usr/local/Caskroom，主要是各种普通软件，如 Alfred、Steam 等

还有一些软件会安装在用户目录下Applications的文件夹中（/Users/xx/Applications），如 Steam 中下载的游戏。这些一般不需要备份。

这些七零八落的软件，手动备份列表是很麻烦的。而且，我们可能经常安装或删除一些软件，需要定期更新软件列表。所以，最好能够定期自动备份，并且是保存在云上，保证数据安全。而要保存在云上，macOS 自带的 iCloud 显然是比较好的选择。

macOS 上的定期任务，我一般使用 Keyboard Maestro 配置。

首先，新建一个任务（Macro），设置时间触发器：

![时间触发器](https://cdn.sspai.com/2018/02/12/5868ef2eee3f30342e9b8c33d8296d58.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1 "时间触发器")

时间触发器

加入一个 Execute Shell Script 动作，在其中写入内容：

```
# All Apps
ls -lh /Applications > ~/Library/Mobile\ Documents/com~apple~CloudDocs/AppList/All_AppList

# MAS Apps
/usr/local/bin/mas list > ~/Library/Mobile\ Documents/com~apple~CloudDocs/AppList/MAS_AppList

# brew Apps
/usr/local/bin/brew list > ~/Library/Mobile\ Documents/com~apple~CloudDocs/AppList/Brew_AppList

# brew cask Apps
/usr/local/bin/brew cask list > ~/Library/Mobile\ Documents/com~apple~CloudDocs/AppList/BrewCask_AppList

```

其中，以 # 开头的是说明性文字，不会运行

![Execute Shell Script](https://cdn.sspai.com/2018/02/12/a82e173a893185c7da9946e6a1fee524.png?imageView2/2/w/1120/q/90/interlace/1/ignore-error/1 "Execute Shell Script")

Execute Shell Script

**注意：**

1.  为了维护 iCloud 中的文件整洁，我将 App 列表文件保存在 iCloud 下的 AppList 文件夹中。如果你也如此，则需要先**手动新建 AppList 文件夹**。
2.  路径`~/Library/Mobile\ Documents/com~apple~CloudDocs`中的`空格`之前都需要加上`\`斜杠。

简单解释下上述几条命令：

### 第一条

命令 `ls -lh /Applications > xxx/xxx`（为了简洁，列表文件路径用 xxx/xxx 代替），生成`/Applications文件夹中的所有软件列表`，其内容类似于：

```
drwxr-xr-x   3 xx     staff    96B Dec 13 19:14 iMazing.app
drwxr-xr-x   3 xx     staff    96B Nov  4 15:25 iStat Menus.app
drwxr-xr-x   3 xx     staff    96B Nov 22 20:57 iTerm.app
drwxr-xr-x@  3 root   wheel    96B Jan 28 19:19 iTunes.app
drwxr-xr-x   3 root   admin    96B Jan 19 19:08 nextcloud.app
drwxr-xr-x@  3 xx     staff    96B Oct 24 17:04 unetbootin.app

```

其中，第三列为 App 文件所属的用户，最后一列为 App 名称。主要分为两类：

*   大多数 App 文件的用户为你的用户名 xx，表示该行的软件是我们手动下载安装的。
*   少部分为 root，表示该软件为 系统软件（如 iTunes），或是一些以 .pkg 文件安装的软件（如 nextcloud）。

在我们之后参考这份软件列表时，需要区分上述几种软件，所以此处直接生成了这份信息较为丰富和杂乱的列表。

此外，如果你想要一份比较干净的 App 列表，可以运行：

`ls -1 /Applications > xxx/xxx`

其结果类似于：

```
iMazing.app
iStat Menus.app
iTerm.app
iTunes.app
nextcloud.app
unetbootin.app

```

如果你想要去掉其中的 .app 文件后缀名，则可运行：

`ls -1 /Applications | sed 's/\.app//g' > xxx/xx`

其结果为：

```
iMazing
iStat Menus
iTerm
iTunes
nextcloud
unetbootin

```

### 第二条

命令 `/usr/local/bin/mas list > xxx/xxx`，生成来自 Mac App Store 的 app 列表，其结果为：

```
1058273036 Polarr Photo Editor Pro (4.4.2)
 Install macOS High Sierra (13302)
1153157709 Speedtest (1.3)
451108668 QQ (6.3.1)

```

其中，第一列为 App 的 ID，第二列为名称，最后的括号中是版本号。

注意，当你下载了 Install macOS High Sierra 之类的 macOS 安装 app 后，运行第二条命令时，生成的文件中会混有 `Install macOS High Sierra (13302)` 之类的内容。**想必你并不需要它，及时删除。**

### 第三条

命令 `/usr/local/bin/brew list > xxx/xxx`，生成 Homebrew 安装的命令行工具列表，其结果类似于：

```
webp
wget
x264
xvid

```

每行一个工具名。

### 第四条

命令 `/usr/local/bin/brew cask list > xxx/xxx`，生成 Homebrew Cask 安装的普通软件列表，其结果类似于：

```
steam
iina
alfred

```

每行一个 App 名。

## 二、自动安装

需要说明的是，第一行命令生成的`所有软件列表`，鱼龙混杂，需要你自己挑选并安装。

后面几种可以自动安装。但是，在安装前，你应该检查列表文件，去除一些不再需要的 App，确保内容无误。

终端中运行：

```
# 进入 iCloud 中的 AppList 文件夹
cd  ~/Library/Mobile\ Documents/com\~apple\~CloudDocs/AppList

# 安装 Homebrew 和 MAS
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
brew install mas

# 生成 MAS_AppList 安装命令
cat AppList/MAS_AppList | sed "s/(.*)//g" | sed -Ee 's/([0-9]+) (.+)/mas install \1 #\2/g' > ~/Desktop/AppInstaller

# 生成 Brew_AppList 安装命令
echo "\nbrew install $(cat AppList/Brew_AppList | tr '\n' ' ')" >> ~/Desktop/AppInstaller

# 生成 BrewCask_AppList 安装命令
echo "\nbrew cask install $(cat AppList/BrewCask_AppList | tr '\n' ' ')" >> ~/Desktop/AppInstaller

# 开始安装
chmod +x ~/Desktop/AppInstaller
~/Desktop/AppInstaller

```

完毕。

## 参考 
1. [狡兔三窟——云备份软件列表与相应配置，补充 Time Machine](https://sspai.com/post/43479)