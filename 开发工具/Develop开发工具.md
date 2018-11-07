## DevTool

### App

* [图标工场 - 移动应用图标生成工具，一键生成所有尺寸的应用图标](https://icon.wuruihong.com/)
* [图片压缩](https://tinypng.com/) 支持png,  jpg

### JSON

* [Quicktype](https://app.quicktype.io/) // 在线生成属性代码
![](https://i.loli.net/2018/11/02/5bdbea2317a77.jpg)

* [TextLab 1.3.9 代码格式转换工具 程序员必备 - 精品MAC应用分享](http://xclient.info/s/textlab.html?t=7ef276e7445d80b7e0214ef8ad6408fb8bb1743a#versions)

* [JSON Wizard 1.3 JSON数据查看编辑工具 - 精品MAC应用分享](http://xclient.info/s/json-wizard.html?t=7ef276e7445d80b7e0214ef8ad6408fb8bb1743a#versions)
* [jsonEditorOnline](https://jsoneditoronline.org/)


### Debug

1. [Peek](https://github.com/shaps80/Peek)
All new design. Inspect your iOS application at runtime. 
![](http://oc98nass3.bkt.clouddn.com/15219076070141.jpg)
![](http://oc98nass3.bkt.clouddn.com/15219076481398.jpg)

使用快捷键`Ctrl + Cmd + Z`唤起

### 1. [injectionforxcode](https://github.com/johnno1962/injectionforxcode) Injection Plugin for Xcode
### 2. [Xtrace](https://github.com/johnno1962/Xtrace)Trace Objective-C method calls by class or instance
### 3. [UIDebuggingInformationOverlay - Low Level](http://ryanipete.com/blog/ios/swift/objective-c/uidebugginginformationoverlay/)

### Easy APNs Provider
[使用Easy APNs Provider测试推送](http://www.jianshu.com/p/134e3dfd1cdc)

#### 推送消息收不到

>使用的是MiPushSDK，之前打的Release包可以收到推送消息，现在却收不到了。因为是同一个ipa包，排除了代码原因，所以可能是推送证书出了问题。我没有重新申请Push证书，而是将证书的 p12文件重新上传到了小米推送网站上，测试后还是收不到。那么，到底是我的证书问题还是小米推送的问题呢？

Easy APNs Provider - 推送测试工具

这是一个神奇的测试工具，[Mac AppStore免费下载~](https://itunes.apple.com/cn/app/easy-apns-provider/id989622350?mt=1)

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972327165173.jpg)

##### 1、添加Token

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972327333218.jpg)

我试了一下第三种直接发送的，但是要么获取不到，要么一下子获取到几十条，我怎么知道哪个是我的deviceToken呢？果断放弃选择手动获取。

连接真机运行，打Log获取deviceToken

```
#pragma mark 注册通知
- (void)application:(UIApplication *)application didRegisterForRemoteNotificationsWithDeviceToken:(nonnull NSData *)deviceToken
{
    NSLog(@"deviceToken:%@",deviceToken);
}
```
注意：输出的deviceToken是NSData类型的，要的就是这个，别和我刚开始一样手贱转NSString浪费生命啊！

输出的Log如下：
```
deviceToken:<9bf8412c 55df912e 12e689f3 4c4a4c72 361262bb efbdf526 e01ebb6d 223a80c9>
```

把那一串数字字符组合粘贴出来删除空格，然后复制粘贴到手动添加的框里
注：
1、不要token两端的尖括号
2、空格删完之后再添加，那个框框只能放64个字符,多的会自动删除

看起来好简单啊，但是真机运行踩了两个坑，我来填一填。

```
process launch failed
```

Debug环境运行没问题，Release环境会弹出以下提示：


![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972327662520.jpg)

解决：

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972327773139.jpg)
![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972327855649.jpg)


红色箭头指向的那个选项不选中 就可以啦
注：Debug executable 意思是是否可以断点执行，Release模式下不可以打断点，所以这项要勾掉，勾掉之后不会影响Log的输出。

###### 1.1 Log不输出

我Xcode刚升级到8，测试机刚升级到iOS10，然后真机运行的时候发现控制台什么都不输出，我可以确保之前一直有Log显示的，不是我Xcode禁掉了的原因，然后看到了文章Xcode 8解决真机测试Log被屏蔽的问题，这篇文章步骤挺详细的，我就不多写了。

到此，获取Token之后，点击添加，你的Token会显示在待添加的Token一栏，给它添加一个名字，然后点击确认保存。

##### 2、选择证书文件

选择Debug或者Release对应的Push证书。我是到苹果开发者网站上重新下载的，这里注意分清两个模式下的证书就行。

##### 3、连接至苹果推送服务器

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972331045230.jpg)

Debug模式选择sandbox，Release模式选择push
选择完成之后一定要 点击 3.连接至： 这个按钮！
状态栏会提示：

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972331219712.jpg)


这里只能说明连接上push服务器了，虽然身份已验证，但是不能说明你的证书是正确的，只能说证书是有效的。我选择发布环境的推送证书，连接sandbox它会显示h和上面一样的状态，证书是否正确只会在发送推送时验证。

##### 4、 推送负载

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972329040544.jpg)

这个不多说了。

##### 5、发送推送

然后就收到推送了。

![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972328270050.jpg)

如果像我上面举例说的那样选择发布环境的推送证书，连接sandbox，状态栏会显示


![](http://oc98nass3.bkt.clouddn.com/2017-06-12-14972328138602.jpg)

你可以看到错误原因，这是非常不错的一点。

##### 6、点开连接

切换push服务器时最好点击一下。

后续（其实是吐槽~）

通过Easy APNs Provider发送消息，我在Release环境可以收到，说明我的发布证书没问题。但是通过小米推送收不到，然后我就联系了小米客服，他们回馈很快，大概一个小时就回复说检查出来是证书问题，让我重新上传试试。
开篇说过，我重新上传了p12，但是没用。到这里，其实我应该立即用小米推送再测试一下的，如果能收到，就说明是小米的bug。 但是我傻傻的又生成并上传了p12，然后就收到了，至此，我也不能证明是不是小米偷偷改了bug。
我做客户端时，不管是因为服务器挂了还是接口数据格式不对导致解析失败，都弹吐司提示“网络连接失败”，反正不说自己错了。只能说，套路深的难免会进入别人的套路中。

### Tower for mac

Git 工具
[Getting Started with Tower - Tower Help](https://www.git-tower.com/help/mac/first-steps/get-started-with-tower)


![](http://oc98nass3.bkt.clouddn.com/15385864644984.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385864429386.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385864283566.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385864142362.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385863555970.jpg)
![](http://oc98nass3.bkt.clouddn.com/15385863901342.jpg)

#### 设置Diff Tools

[Diff & Merge Tools - Tower Help](https://www.git-tower.com/help/mac/integration/custom-diff-tools)

create a file named "CompareTools.plist" and put it into "~/Library/Application Support/com.fournova.Tower3/CompareTools/".

```
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" 
    "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<array>
    <dict>
        <key>ApplicationIdentifier</key>
        <string>com.madebysofa.Kaleidoscope</string>
        <key>ApplicationName</key>
        <string>Kaleidoscope</string>
        <key>DisplayName</key>
        <string>Kaleidoscope</string>
        <key>LaunchScript</key>
        <string>kaleidoscope.sh</string>
        <key>Identifier</key>
        <string>kaleidoscope</string>
        <key>SupportsMergeTool</key>
        <false/>
        <key>SupportsDiffChangeset</key>
        <true/>
    </dict>
</array>
</plist>
```


#### 配置difftool

我找到了配置它的方法。Kaleidoscope菜单下，有一个名为Integration的链接，它打开了几个版本控制解决方案的配置窗口。
[comparison - Kaleidoscope for git difftool - Super User](https://superuser.com/questions/689853/kaleidoscope-for-git-difftool)
After installing ksdiff clicking on Configure button will add the following lines to your .gitconfig file.

```
git config --global diff.tool kaleidoscope

[diff]
    tool = Kaleidoscope
[difftool "Kaleidoscope"]
  cmd = ksdiff --partial-changeset --relative-path \"$MERGED\" -- \"$LOCAL\" \"$REMOTE\"
[merge]
    tool = Kaleidoscope
[mergetool "Kaleidoscope"]
  cmd = ksdiff --merge --output \"$MERGED\" --base \"$BASE\" -- \"$LOCAL\" --snapshot \"$REMOTE\" --snapshot
  trustExitCode = true
```

then running the following command will open successively each different file


```
git difftool myBranch otherBranch  -y -t Kaleidoscope
```
-y stands to avoid prompting for asking if we want to use Kaleidoscope for difftool for each file. Default answer is "yes".
-t Kaleidoscope is optionnal here as default difftool is already set to Kaleidoscope in our .gitconfig file.

### Gitsome- Git工具

[Gitsome](https://github.com/donnemartin/gitsome)

```
$ gh <command> [param] [options]
```

### Searching Repos

```
$ gh search-repos "created:>=2015-01-01 stars:>=1000 language:python" --sort stars -p
```

### The view command

在搜寻的repo中，查看某一个[#] 是搜索结果列表代号
View the previously listed notifications, pull requests, issues, repos, users etc, with HTML nicely formatted for your terminal, or optionally in your browser:

```
$ gh view [#] [-b/--browser]

```
![](http://oc98nass3.bkt.clouddn.com/2017-08-31-15041463388583.jpg)


### View trending repos:

```
$ gh trending [language] [-w/--weekly] [-m/--monthly] [-d/--devs] [-b/--browser]
```
![](http://oc98nass3.bkt.clouddn.com/2017-08-31-15041463551665.jpg)

### Github命令

```
GitHub Integration Commands Listing

  configure            Configure gitsome.
  create-comment       Create a comment on the given issue.
  create-issue         Create an issue.
  create-repo          Create a repo.
  emails               List all the user's registered emails.
  emojis               List all GitHub supported emojis.
  feed                 List all activity for the given user or repo.
  followers            List all followers and the total follower count.
  following            List all followed users and the total followed count.
  gitignore-template   Output the gitignore template for the given language.
  gitignore-templates  Output all supported gitignore templates.
  issue                Output detailed information about the given issue.
  issues               List all issues matching the filter.
  license              Output the license template for the given license.
  licenses             Output all supported license templates.
  me                   List information about the logged in user.
  notifications        List all notifications.
  octo                 Output an Easter egg or the given message from Octocat.
  pull-request         Output detailed information about the given pull request.
  pull-requests        List all pull requests.
  rate-limit           Output the rate limit.  Not available for Enterprise.
  repo                 Output detailed information about the given filter.
  repos                List all repos matching the given filter.
  search-issues        Search for all issues matching the given query.
  search-repos         Search for all repos matching the given query.
  starred              Output starred repos.
  trending             List trending repos for the given language.
  user                 List information about the given user.
  view                 View the given index in the terminal or a browser.
```


## 图表绘制

[Pluto-Y/iOS-Echarts](https://github.com/Pluto-Y/iOS-Echarts/tree/master/Doc)


![](https://i.loli.net/2018/10/27/5bd3d911ce59d.jpg)


## HTML

[Emmet](https://github.com/sergeche/emmet-sublime)Emmet for Sublime Text http://emmet.io



