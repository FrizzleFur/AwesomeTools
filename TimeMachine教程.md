
# Mac 备份工具 Time Machine 使用教程


## 说明

本文转载自[Mac 备份工具 Time Machine 使用教程](https://mp.weixin.qq.com/s?__biz=MzAxNzcwMTA4Ng==&mid=2247485330&idx=1&sn=cb1b1b72f2460b236d24f9e12a02eead&chksm=9be0c623ac974f35649fb0591f287549d2438af9575469374d5b44774f8845324af99a376294#rd)


Time Machine 是 macOS 系统内置的备份工具，它可以为你的 Mac 自动制作过去 24 小时的每小时备份、过去一个月的每日备份以及过去所有月份的每周备份，以便需要时进行数据恢复和查看（ps：如果备份磁盘已满，则最早的备份将被删除，如果不想将整个磁盘用作备份盘，可将磁盘分区，将备份区和其他文件存储区分开），下面我们就来看看如何使用 Time Machine 制作备份以及恢复备份。

如果你平时就养成了定期备份的好习惯，现在就轻松多了，因为 TimeMachine 是增量备份，每次只备份有改动的文件，一般只有第一次备份很费时间，后面的备份就比较快。

## 设置 Time Machine

将外置存储设备（移动硬盘 / 其他形式的网络存储设备：Time Capsule 、macOS Server）连接至 Mac ，系统可能会询问是否要使用该存储设备配合 Time Machine 进行备份，单击「用作备份磁盘」即可；
![](http://oc98nass3.bkt.clouddn.com/15137568585910.jpg)


如果没有弹出如上图所示的询问窗口，可自行打开「系统偏好设置」-「 Time Machine」，单击「选择备份磁盘...」；


选择要用来存储备份的外部磁盘，单击「使用磁盘」，如果要加密备份，可勾选左下角的「加密备份」，然后设置密码即可；
![](http://oc98nass3.bkt.clouddn.com/15137568899499.jpg)

![](http://oc98nass3.bkt.clouddn.com/15137568962036.jpg)


## 使用 Time Machine 进行备份


选择了备份磁盘之后，「自动备份」将被自动勾选，「自动备份」被勾选的情况下，当备份磁盘没有连接 Mac 时，Time Machine 会自动备份到本机磁盘（每小时），这会占据本机磁盘的空间；如果不希望自动备份，可采用手动备份：取消勾选「自动备份」（macOS Sierra）或关闭 Time Machine（OS X El Capitan 或更低版本），勾选「在菜单栏中显示 Time Machine」，单击菜单栏中的 Time Machine 图标，单击「立即备份」即可手动开始备份。首次备份可能需要较长时间，具体取决于备份数据的多少和备份磁盘的写入速度。下次备份只会备份自上次备份以来有变动的文件，因此速度会快很多。

![](http://oc98nass3.bkt.clouddn.com/15137569566966.jpg)
![](http://oc98nass3.bkt.clouddn.com/15137569717105.jpg)


若要查看备份状态，可通过 Time Machine 菜单查看，也可以在 Time Machine 偏好设置页面查看；

![](http://oc98nass3.bkt.clouddn.com/15137569789501.jpg)
![](http://oc98nass3.bkt.clouddn.com/15137570020306.jpg)


若要取消正在进行的备份，单击 Time Machine 菜单中的「跳过此备份」；

![](http://oc98nass3.bkt.clouddn.com/15137570078624.jpg)

若要从备份中排除不需要备份的项目，在 Time Machine 偏好设置页面，单击「选项」，然后单击「+」号并选择要排除的项目，最后单击「存储」即可；

![](http://oc98nass3.bkt.clouddn.com/15137570142713.jpg)

备份完成将收到提醒。

![](http://oc98nass3.bkt.clouddn.com/15137570260280.jpg)

## 从 Time Machine 备份恢复


恢复特定文件

![](http://oc98nass3.bkt.clouddn.com/15137570378027.jpg)


从 Time Machine 菜单中单击「进入 Time Machine」，或者打开「Launchpad」 -「其他 」-「Time Machine」；
![](http://oc98nass3.bkt.clouddn.com/15137570444604.jpg)

前往包含需要恢复的文件所在的文件夹，如果还记得文件被删除前的时间点，可使用屏幕右侧边缘的时间线查看 Time Machine 备份中在该日期和时间的文件；也可点击窗口右边的向上/向下箭头跳至上次窗口内容变化的时间点；还可使用窗口中的搜索栏来查找文件，然后沿时间线移动直到文件出现，文件找到后，选中文件，双击或者按空格键，可快速预览，以确定是你要找的文件，然后单击窗口下方的「恢复」即可恢复所选文件；


![](http://oc98nass3.bkt.clouddn.com/15137570570285.jpg)

##  恢复所有文件



若要恢复 Time Machine 备份中的所有内容，需使用 macOS 的恢复功能：开机或者重启时，立即按住 Command + R 键，直到出现 Apple Logo或旋转的地球，随后将出现如下图所示的“实用工具”窗口，然后选择「从 Time Machine 备份进行恢复」即可；

![](http://oc98nass3.bkt.clouddn.com/15137570821382.jpg)

若要将 Time Machine 备份中的文件、设置和用户帐户拷贝到另一台 Mac，可使用「迁移助理」。
![](http://oc98nass3.bkt.clouddn.com/15137570871940.jpg)



###     删除 Time Machine 备份

说到删除备份，你可能会想：直接通过 Finder 打开备份磁盘，然后将备份文件（夹）移到废纸篓不就可以了？事实上这是行不通的，即使移到了废纸篓，也无法清倒，正确的方法应该是通过 Time Machine 来删除。

#### 删除特定的备份文件

进入 Time Machine ，找到并选中要删除的特定文件，右键呼出菜单，选择「删除XXX的所有备份」并确认即可；
![](http://oc98nass3.bkt.clouddn.com/15137571035860.jpg)

#### 删除整个 Time Machine 备份

![](http://oc98nass3.bkt.clouddn.com/15212009637636.jpg)

![](http://oc98nass3.bkt.clouddn.com/15137571278964.jpg)

进入 Time Machine，打开备份磁盘，进入「Backups.backupdb」 - 「XXX的 Mac。。。」- 「以最近的日期命名的备份文件夹」，选中该文件夹，右键呼出菜单，选择「删除XXX的所有备份」并确认，确认之后可单击窗口下方的「取消」或者键盘左上角的 esc 键，以退出 Time Machine，你将看到备份正在被删除的提示，稍等片刻，备份将被删除；

![](http://oc98nass3.bkt.clouddn.com/15137571368145.jpg)



上述删除操作完成之后，最后再通过 Finder 打开备份硬盘，将 Backups.backupdb 文件夹移到废纸篓，并清倒，这样删除整个 Time Machine 备份的操作就完成了。

![](http://oc98nass3.bkt.clouddn.com/15137571488631.jpg)


为了预防电脑出现意外情况造成数据丢失，建议大家养成定期备份的习惯。




