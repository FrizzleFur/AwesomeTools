# Mac的自动化

![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20200201101136.png)


## 常用串联命令

### 管道

管道是 shell 中非常常用的功能之一，它允许不同脚本、命令之间互相传递数据，例如：

```js
ls | grep 'pars'
```

复制代码该命令意思是将 ls 输出的内容传递到 grep 'pars' 命令，grep 会把包含 'pars' 的内容过虑出来。我们再举个栗子，通过 shell 获取 git 仓库里中的当前分支名：

```shell
currentBranch=`git branch | grep "*"`
currentBranch=${currentBranch/* /}
```

### 复制代码重定向

大多数 UNIX 系统命令从终端接受输入并将所产生的输出发送回终端。一个命令通常从一个叫标准输入的地方读取输入，默认情况下是终端。同样，一个命令通常将其输出写入到标准输出，默认情况下也是终端。如果你需要修改输入或输出，就需要使用到重定向功能。




命令 |	说明
 -- | --
command > file  |		将输出重定向到 file。
command < file	 |	将输入重定向到 file。
command >> file	 |	将输出以追加的方式重定向到 file。


输出重定向，指将一条命令的输入位置重新定义，举个例子：
ls > ls.txt

复制代码ls 输出结果应显示在终端，而上面命令将 ls 的输出结果写到 ls.txt 这个文件中。需要注意，用 > 重定向到 ls.txt 文件默认是覆盖的，如果需要用追加的方式写入文件，则需要使用 >>：
pwd >> ls.txt
复制代码输入重定向：
pbcopy < ls.txt


# Mac 自动化脚本


- 将当前`Finder`路径用`iTerm2`打开

```shell
tell application "Finder"
	set pathFile to selection as text
	set pathFile to get POSIX path of pathFile
	--防止目录存在空格跳转不了
	set pathFile to quoted form of pathFile
	set pathFile to "cd " & pathFile
	--set the clipboard to pathFile
	tell application "iTerm"
		create window with default profile
		tell current session of current window
			write text pathFile
		end tell
	end tell
end tell
```

- 将工程用`Xcode`打开，并编译

```shell
tell application "Xcode"
	open "/Users/xxxxx/xxxx/xxxxx/xxxxx.xcworkspace"
	set workspaceDocument to workspace document "xxxxx.xcworkspace"
	repeat 120 times
		if loaded of workspaceDocument is true then
			exit repeat
		end if
		delay 1
	end repeat
	if loaded of workspaceDocument is false then
		error "Xcode workspace did not finish loading within timeout."
	end if
	set actionResult to run workspaceDocument
	repeat
		if completed of actionResult is true then
			exit repeat
		end if
		delay 1
	end repeat
end tell
```




# 参考

* [如何提高工作效率 - 自动化篇 - 掘金](https://juejin.im/post/5bfac61ee51d454af013a900#heading-8)


