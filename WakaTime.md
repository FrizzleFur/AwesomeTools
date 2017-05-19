# WakaTime


> 作为一名开发，代码的输入量是一个重要的指标，如何检查自己每天花了多少时间在写代码上呢？有款叫`WakaTime` 可以很好的与编译器集成，统计你的敲代码的时间。╮(✪ω✪)╭

[WakaTime For Xcode](https://wakatime.com/help/plugins/xcode)

退出`Xcode`进程，
在终端安装命令：

`curl -fsSL https://raw.githubusercontent.com/wakatime/xcode-wakatime/master/install.sh | sh`

![](http://oc98nass3.bkt.clouddn.com/2017-05-19-14951627801266.jpg)

`Xcode`会弹出加载插件的提示，点击`Load Bundles`
![](http://www.skyfox.org/wp-content/uploads/2016/03/A1375B86-B39C-4898-B19D-65B50B8FC652.jpg)
然后提示输入`WakaTime`的APIkey,在个人账号信息中。
![](http://oc98nass3.bkt.clouddn.com/2017-05-19-14951629506636.jpg)


### 3rd Party Integrations

![](http://oc98nass3.bkt.clouddn.com/2017-05-19-14951633105350.jpg)

后面数据积累多后，可以考虑链接[Timely](https://timelyapp.com/)和[Zenobase](https://zenobase.com/)来进行分析
![](http://oc98nass3.bkt.clouddn.com/2017-05-19-14951633593320.jpg)

[Zenobase](https://zenobase.com/)
![](http://oc98nass3.bkt.clouddn.com/2017-05-19-14951634226176.jpg)

### WakaTime FAQ

一、WakaTime精确度如何

1. 当你开始编辑一个文件, WakaTime开始计时;
2. 计时器停止当你到达你AFK的超时设置。当你去AFK，WakaTime倒计时器到时间你最后编辑的文件。
3. 切换到编辑不同文件时计时器也停止。在这种情况下，WakaTime节省时间从你开始编辑原始文件，当你切换到新文件。时间是重置，我们开始在步骤1与新文件。
二、How are projects created? 

WakaTime creates projects for you automatically, using one of these methods.

This means you don’t manually create projects.

Instead, use your IDE like normal and projects are created automatically in the background.

We work hard to keep WakaTime completely passive, so it never gets in your way.

三、如何设置，修改项目名称？
WakaTime recognizes the project’s name one of four ways:

Revision control software (Ex: Git, Mercurial, or Subversion):

To set the project name for a folder, go to that folder in a terminal and type:

git init

Files inside that folder will be assigned to a project with that folder’s name.

* only renames projects for new coding activity

Create a .wakatime-project file inside your project directory. Type the project name as the first line of this file and WakaTime will use that project name for all files inside this directory.

* only renames projects for new coding activity

Adding the project directory to your ~/.wakatime.cfg file under the [projectmap] section.

* only renames projects for new coding activity

As a last resort use custom rules:
![](https://wakatime.com/static/img/custom_rules_for_projects.png)
* Warning: this will rename projects from past coding activity. Use with caution!

四、我可以删除项目吗？

要删除项目，首先删除使用编码活动删除工具的[编码活动](https://wakatime.com/code-delete-tool).

![](http://oc98nass3.bkt.clouddn.com/2017-05-19-14951650055930.jpg)

After removing the project’s coding activity, you can delete the project from the project’s dashboard. A project dashboard without coding activity will have a “trash icon” in the top right corner.

To exclude projects in the future, add the project’s path to your `$HOME/.wakatime.cfg` file under the exclude setting.


## 参考

[WakaTime Help](https://wakatime.com/help/getting-started/faq)




