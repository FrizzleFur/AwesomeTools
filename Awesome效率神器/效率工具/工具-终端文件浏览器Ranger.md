# 工具-终端文件浏览器Ranger

##常用快捷键


q ： 退出 ranger
R : 重新刷新目录
S : 执行 shell 命令
: 或者 ; : 控制台
W : 显示日志
k : 向上
j : 向下
h : 向左
l : 向右
g : 到顶部
G : 到底部
J : 半页向下
K : 半页向上
gh : 相当于 cd ~
ge : 相当于 cd /etc
gu : cd /usr
dd : 剪切
yy : 复制
pp : 粘贴

File Operations
Shortcut	Description
<Enter>	Open
r	open file with
z	toggle settingS
o	change sort order
zh	view hidden files
cw	rename current file
yy	yank / copy
dd	cut
pp	paste
/	search for files :search
n	next match
N	prev match
<delete>	Delete

[ranger-cheatsheet.md](https://gist.github.com/heroheman/aba73e47443340c35526755ef79647eb)

## 自定义配置

[config/rc.conf](https://github.com/ranger/ranger/blob/master/ranger/config/rc.conf)

## bookmark 操作

- 这个 bookmark 功能很不错，可以非常快速地回到某一个目录

- m+键 定义一个目录的 bookmark 的键，例如：ma 或者 ma

- um+键 取消定义一个目录的 bookmark 的键，例如：ma 或者 ma

- '+键 跳回到定义目录的 bookmark，例如：'a

- draw_bookmarks 命令用来查看已经定义了哪些 bookmark 键

(可以定义常用路径来增加range的熟练程度)

### 常用命令：


![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20220913110625.png)


## 工具

- 安装图片预览：[preview images using kitty #1549](https://github.com/ranger/ranger/issues/1549)


Im on MacOs, miniconda3 python 3.7.2, and also tried with brew python 3.7.3
pip install pillow ranger-fm
in ~/.config/ranger/rc.conf i have set preview_images true and set preview_images_method kitty

if I useset preview_images_method iterm2 and iterm2 terminal images appear as broken



## 参考


[ranger 工具的使用](https://www.52gvim.com/post/ranger-tool-usage)
