# 工具-Vim


 时间 |  备注
 --- | --- 
`2018-07-13` | 深入学习VIM，整理教程

## TODO
* [ ] vim实操工作流
    * 快速替换多行文本 [上古神奇Vim](https://www.bilibili.com/video/av55498503)
    * 剪切，粘贴


## 什么是Vim？

Vim是从`vi`发展出来的一个文本编辑器。代码补完、编译及错误跳转等方便编程的功能特别丰富，在程序员中被广泛使用。

简单的来说， `vi`是老式的字处理器，不过功能已经很齐全了，但是还是有可以进步的地方。 `vim`则可以说是程序开发者的一项很好用的工具。

连`vim`的官方网站 ([http://www.vim.org](http://www.vim.org/)) 自己也说`vim`是一个程序开发工具而不是文字处理软件。
![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190712154316.png)
![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190712154341.png)

`vim`键盘图：

![](https://i.loli.net/2019/01/14/5c3be14c0fdab.jpg)

## Vim编辑器

相信没有用过Linux的同学在看一些段子的时候都会看到过两个编辑器：

* vim
* emacs

下面我们学习如何简单使用vi。vi 是 “Visual interface” 的简称，它可以执行输出、删除、查找、替换、块操作等众多文本操作，而且**用户可以根据自己的需要对其进行定制，这是其他编辑程序所没有的**。

* vi可以看做成我们Windows下的记事本
* vim 即 Vi IMproved，vi 克隆版本之一

使用Vi来编辑文件：

![使用Vi来编辑文件](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295536612775.jpg)

Vi有三种模式：

![Vi有三种模式](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295534530042.jpg)


## 1.1 普通模式

* `G`用于直接跳转到文件尾
* `ZZ`用于存盘退出Vi
* `ZQ`用于不存盘退出Vi
* `/和？`用于查找字符串
* `n`继续查找下一个
* `yy`复制一行
* `p`粘帖在下一行，P粘贴在前一行
* `dd`删除一行文本
* `x`删除光标所在的字符
* `u`取消上一次编辑操作（undo）


## 1.2 插入模式

在 Normal 模式下输入插入命令 `i、 a 、 o`进入insert模式。用户输入的任何字符都被vim**当做文件内容保存起来**，并将其显示在屏幕上。
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15311962564268.jpg)

* 在文本输入过程中，若想回到Normal模式下，按 Esc 键即可。

## 1.3 命令行模式

Normal 模式下，用户按冒号 `:`即可进入 Command 模式，此时 vim 会在显示窗口的最后一行 (屏幕的最后一行) 显示一个 “:” 作为 Command 模式的提示符，等待输入命令。

* q 退出程序
* w 保存文件
* `:w` 保存当前编辑文件，但并不退出
* `:w` newfile 存为另外一个名为 “newfile” 的文件
* `:wq` 用于存盘退出Vi
* `:q!` 用于不存盘退出Vi
* `:q`用于直接退出Vi （未做修改）

**设置Vi环境:**

* :set autoindent 缩进,常用于程序的编写
* :set noautoindent 取消缩进
* :set number 在编辑文件时显示行号
* :set nonumber 不显示行号
* :set tabstop=value 设置显示制表符的空格字符个数
* :set 显示设置的所有选项
* :set all 显示所有可以设置的选项

## vi/vim 按键说明

除了上面简易范例的 i, Esc, :wq 之外，其实 vim 还有非常多的按键可以使用。

### 第一部份：一般模式可用的光标移动、复制粘贴、搜索替换等

| 移动光标的方法 | 说明 |
| --- | --- |
| h 或 向左箭头键(←) | **光标向左移动一个字符** |
| j 或 向下箭头键(↓) | **光标向下移动一个字符** |
| k 或 向上箭头键(↑) | **光标向上移动一个字符** |
| l 或 向右箭头键(→) | **光标向右移动一个字符** |
| **如果你将右手放在键盘上的话，你会发现 hjkl 是排列在一起的，因此可以使用这四个按钮来移动光标。 如果想要进行多次移动的话，例如向下移动 30 行，可以使用 "30j" 或 "30↓" 的组合按键， 亦即加上想要进行的次数(数字)后，按下动作即可！** |
| [Ctrl] + [f] | **屏幕『向下』移动一页，相当于 [Page Down]按键 (常用)** |
| [Ctrl] + [b] | **屏幕『向上』移动一页，相当于 [Page Up] 按键 (常用)** |
| [Ctrl] + [d] | 屏幕『向下』移动半页 |
| [Ctrl] + [u] | 屏幕『向上』移动半页 |
| + | 光标移动到非空格符的下一行 |
| - | 光标移动到非空格符的上一行 |
| n<space> | **那个 n 表示『数字』，例如 20 。按下数字后再按空格键，光标会向右移动这一行的 n 个字符。例如 20<space> 则光标会向后面移动 20 个字符距离。** |
| 0 或功能键[Home] | **这是数字『 0 』：移动到这一行的最前面字符处 (常用)** |
| $ 或功能键[End] | **移动到这一行的最后面字符处(常用)** |
| H | 光标移动到这个屏幕的最上方那一行的第一个字符 |
| M | 光标移动到这个屏幕的中央那一行的第一个字符 |
| L | 光标移动到这个屏幕的最下方那一行的第一个字符 |
| G | **移动到这个档案的最后一行(常用)** |
| nG | **n 为数字。移动到这个档案的第 n 行。例如 20G 则会移动到这个档案的第 20 行(可配合 :set nu) **|
| gg | **移动到这个档案的第一行，相当于 1G 啊！ (常用)** |
| n<Enter> | **n 为数字。光标向下移动 n 行(常用)** |
| 搜索替换 |
| /word | 向光标之下寻找一个名称为 word 的字符串。例如要在档案内搜寻 vbird 这个字符串，就输入 /vbird 即可！ (常用) |
| ?word | 向光标之上寻找一个字符串名称为 word 的字符串。 |
| n | 这个 n 是英文按键。代表重复前一个搜寻的动作。举例来说， 如果刚刚我们执行 /vbird 去向下搜寻 vbird 这个字符串，则按下 n 后，会向下继续搜寻下一个名称为 vbird 的字符串。如果是执行 ?vbird 的话，那么按下 n 则会向上继续搜寻名称为 vbird 的字符串！ |
| N | 这个 N 是英文按键。与 n 刚好相反，为『反向』进行前一个搜寻动作。 例如 /vbird 后，按下 N 则表示『向上』搜寻 vbird 。 |
| 使用 /word 配合 n 及 N 是非常有帮助的！可以让你重复的找到一些你搜寻的关键词！ |
| :n1,n2s/word1/word2/g | n1 与 n2 为数字。在第 n1 与 n2 行之间寻找 word1 这个字符串，并将该字符串取代为 word2 ！举例来说，在 100 到 200 行之间搜寻 vbird 并取代为 VBIRD 则：
『:100,200s/vbird/VBIRD/g』。(常用) |
| :1,$s/word1/word2/g | 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！(常用) |
| :1,$s/word1/word2/gc | 从第一行到最后一行寻找 word1 字符串，并将该字符串取代为 word2 ！且在取代前显示提示字符给用户确认 (confirm) 是否需要取代！(常用) |
| 删除、复制与贴上 |
| x, X | **在一行字当中，x 为向后删除一个字符 (相当于 [del] 按键)， X 为向前删除一个字符(相当于 [backspace] 亦即是退格键) (常用)** |
| nx | n 为数字，连续向后删除 n 个字符。举例来说，我要连续删除 10 个字符， 『10x』。 |
| dd | **删除游标所在的那一整行(常用)** |
| ndd | **n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行 (常用)** |
| d1G | 删除光标所在到第一行的所有数据 |
| dG | 删除光标所在到最后一行的所有数据 |
| d$ | **删除游标所在处，到该行的最后一个字符** |
| d0 |**那个是数字的 0 ，删除游标所在处，到该行的最前面一个字符** |
| yy | **复制游标所在的那一行(常用)** |
| nyy | **n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行(常用)** |
| y1G | 复制游标所在行到第一行的所有数据 |
| yG | 复制游标所在行到最后一行的所有数据 |
| y0 | 复制光标所在的那个字符到该行行首的所有数据 |
| y$ | 复制光标所在的那个字符到该行行尾的所有数据 |
| p, P | p 为将已复制的数据在光标下一行贴上，P 则为贴在游标上一行！ 举例来说，我目前光标在第 20 行，且已经复制了 10 行数据。则按下 p 后， 那 10 行数据会贴在原本的 20 行之后，亦即由 21 行开始贴。但如果是按下 P 呢？ 那么原本的第 20 行会被推到变成 30 行。 (常用) |
| J | 将光标所在行与下一行的数据结合成同一行 |
| c | 重复删除多个数据，例如向下删除 10 行，[ 10cj ] |
| u | **复原前一个动作。(相当于undo,常用) **  |
| [Ctrl]+r | **重做上一个动作。(常用)** |
| 这个 u 与 [Ctrl]+r 是很常用的指令！一个是复原，另一个则是重做一次～ 利用这两个ii功能按键，你的编辑，嘿嘿！很快乐的啦！ |
| . | **不要怀疑！这就是小数点！意思是重复前一个动作的意思。 如果你想要重复删除、重复贴上等等动作，按下小数点『.』就好了！ (常用)** |

### 第二部份：一般模式切换到编辑模式的可用的按钮说明

| 进入输入或取代的编辑模式 | 说明 |
| --- | --- |
| i, I | 进入输入模式(Insert mode)：
i 为『从目前光标所在处输入』， I 为『在目前所在行的第一个非空格符处开始输入』。 (常用) |
| a, A | 进入输入模式(Insert mode)：
a 为『从目前光标所在的下一个字符处开始输入』， A 为『从光标所在行的最后一个字符处开始输入』。(常用) |
| o, O | **进入输入模式(Insert mode)：
这是英文字母 o 的大小写。o 为『在目前光标所在的下一行处输入新的一行』； O 为在目前光标所在处的上一行输入新的一行！(常用)** |
| r, R | 进入取代模式(Replace mode)：
**r 只会取代光标所在的那一个字符一次；R会一直取代光标所在的文字，直到按下 ESC 为止；(常用)** |
| 上面这些按键中，在 vi 画面的左下角处会出现『--INSERT--』或『--REPLACE--』的字样。 由名称就知道该动作了吧！！特别注意的是，我们上面也提过了，你想要在档案里面输入字符时， 一定要在左下角处看到 INSERT 或 REPLACE 才能输入喔！ |
| [Esc] | 退出编辑模式，回到一般模式中(常用) |

### 第三部份：一般模式切换到指令行模式的可用的按钮说明

| 指令行的储存、离开等指令 | 说明 |
| --- | --- |
| :w | 将编辑的数据写入硬盘档案中(常用) |
| :w! | 若文件属性为『只读』时，强制写入该档案。不过，到底能不能写入， 还是跟你对该档案的档案权限有关啊！ |
| :q | 离开 vi (常用) |
| :q! | 若曾修改过档案，又不想储存，使用 ! 为强制离开不储存档案。 |
| 注意一下啊，那个惊叹号 (!) 在 vi 当中，常常具有『强制』的意思～ |
| :wq | 储存后离开，若为 :wq! 则为强制储存后离开 (常用) |
| ZZ | **这是大写的 Z 喔！若档案没有更动，则不储存离开，若档案已经被更动过，则储存后离开！** |
| :w [filename] | 将编辑的数据储存成另一个档案（类似另存新档） |
| :r [filename] | 在编辑的数据中，读入另一个档案的数据。亦即将 『filename』 这个档案内容加到游标所在行后面 |
| :n1,n2 w [filename] | 将 n1 到 n2 的内容储存成 filename 这个档案。 |
| :! command | 暂时离开 vi 到指令行模式下执行 command 的显示结果！例如
『:! ls /home』即可在 vi 当中察看 /home 底下以 ls 输出的档案信息！ |
| vim 环境的变更 |
| :set nu | 显示行号，设定之后，会在每一行的前缀显示该行的行号 |
| :set nonu | 与 set nu 相反，为取消行号！ |

特别注意，在 vi/vim 中，数字是很有意义的！数字通常代表重复做几次的意思！ 也有可能是代表去到第几个什么什么的意思。

举例来说，要删除 50 行，则是用 『50dd』 对吧！ 数字加在动作之前，如我要向下移动 20 行呢？那就是『20j』或者是『20↓』即可。

## 其他

* 命令行模式下输入（n为指定的行号）：
    * （1）ngg / nG
    * （2）:n
    * （3）vim +n filename（注意这里要输入 + 号）

## 常用

* `h、j、k、l`上下左右, 配合[行数]`h、j、k、l`
* `w、b`移动单词
* 配合数字表示重复次数
* 配合[motion]
* `行号 + G` 跳转到制定的行
* `: + 行号`跳转到制定的行
* u表示撤销上一次修改（undo）
* U表示撤销对整行的修改（undo）
* Ctrl + r 恢复所撤销的内容（redo）
* 按下`%`跳转到另一半的括号
* `>>`向右边👉缩进，`<<`向左边👈缩进
* 搜索🔍，使用`/`进行查询,使用`n`,`N`切换结果. 搜索替换`:s/SEARCH_STRING/REPLACE_STRING`; 
* `:s/SEARCH_STRING/REPLACE_STRING/g`整行替换
* `%s/SEARCH_STRING/REPLACE_STRING/g`表示全部都进行替换
* `:[数字1],[数字2]s/SEARCH_STRING/REPLACE_STRING/gc`表示制定行范围内，每次询问替换操作`replace with O (y/n/a/q/l/E/~Y) ?`，(g是表示global,但c表示continue?)/
* :nohl取消屏幕所有高亮
* `:!`表示进入命令模式
* `:w + newFileName`表示当前路径下另存为新文件
* `r + FileName`表示将FileName合并
 * `v`进入可视模式


## Motion

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15311967218523.jpg)
数字 + [motion] = 重复多个[motion]


## 删除命令

d + [motion]
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15311968436967.jpg)

d + [数字] + [motion] = 删除多个[motion]范围

所有的“删除”操作并不是真的删除，它们事实上是存放在VIM的一个缓冲区中，相当于Windows的剪切功能
d20j, 删除到第20行。

## 拷贝

y + [数字] + [motion] 

## 黏贴

配合之前删除的“dd”
* p: 将最后一次删除的内容黏贴到光标之前
* P: 将最后一次删除的内容黏贴到光标之后
* 如果你需要粘贴的是整行为单位，那么p命令将在光标的下一行开始粘贴;
* 如果你拷贝的是非整行的局部字符串，那么p命令将在光标后开始粘贴。

### iterm2黏贴到系统

[mac os x copy terminal (does work) vs iterm2 (does not work) · Issue #3702 · neovim/neovim](https://github.com/neovim/neovim/issues/3702)

```
@hansrodtang just enlightened me on what is going on here. This is actually a feature of iTerm2.
Go to Settings->General, and enable Applications in terminal may access clipboard.

When I enabled that option, I could copy from and paste to iTerm2 as one would expect.
There is still something strange here, though. @hansrodtang gets expected behaviour with the option off.

Anyway, hope this helps, @ephes. :)

EDIT: Sorry for all the noise here. Especially since this has nothing to do with Neovim.
I reinstalled the latest nightly from iTerm2, and then, everything was allright. It turned out that I in fact couldn't copy from iTerm whether the option I mentioned was enabled or not. After reinstallation, the option does not seem to have any effect.
```

```
I also had similar problem with iTerm. For me, turning on Application in terminal may access clipboard didn't help.
What actually worked for me is: Profile -> Text -> Blinking Cusror (mark it checked)
Weird !!
```

## 搜索

1.普通搜索，输入：
/关键字  
向下找（左斜杠+关键字）

向下查找if，按回车后提示已查找到文件结尾

?关键字 
 # 向上找（逆向搜索）（问号+关键字）

向上查找if，按回车后提示已查找到文件开头

2.匹配搜索，输入：

/关键字\>   
 #匹配末尾（右斜杠+大于号）

搜索以_HOME结尾的字符串

/\<关键字    
匹配开头（右斜杠+小于号）

搜索以HOST开头的字符串

/\<关键字\> 
 #匹配全部（匹配开头和结尾的符号加起来）

以整个字符串为单位进行搜索

3.不区分大小写
:set ignorecase    

:set noignorecase  

输入忽略大小写配置命令+回车+普通搜索

4.高亮搜索
:set hlsearch    

输入高亮配置命令+回车，之前或之后的搜索都高亮显示

5.递进搜索
（每输入一个字符，搜索一次）
:set incsearch   

## 替换模式

* r命令用于替换光标所在的字符，做法是先将光标移动到需要替换的字符处，按一下r键，然后输入新的字符。

* 在键入r命令前输入数字,表示从光标处开始，将多个字符统一替换为新字符
* abc ——>  aaa
* R命令让你一步到位进入替换模式
* Backspace可以退回替换前的模式

## 修改模式

Vim用C命令实现修改: C [数字] motion
![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15311987911491.jpg)
修改 == 删除 十 进入插入模式

## 文件信息

```linux
Ctrl + g
```

## 1.4 Vi练习题

> 在用户主目录下，执行vi程序，编辑文件install.log；移动光标到第10行，第五个字符；按大写字母G，达到文件末尾；不存盘退出；

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295535450600.jpg)

> 在用户主目录下，执行vi程序，编辑文件install.log；用/命令查找字符串sudo，复制包含字符串sudo的行

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295536089358.jpg)


> 在用户主目录下，执行vi程序，编辑文件install.log；进入命令模式，设置显示行号；用？命令查找字符串openssh，用命令n查找下一个

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295536218243.jpg)

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295536294515.jpg)


## vi/vim 使用实例

## Recording⏺

使用vim时无意间触碰到q键，左下角出现“recording”这个标识，觉得好奇，遂在网上查了一下，然后这是vim的一个强大功能。他可以录制一个宏（Macro)，在开始记录后，会记录你所有的键盘输入，包括在insert模式下的输入、正常模式下使用的各种命令等。
具体使用：
* 第一步：在正常模式下（非insert模式、非visual模式）按下q键盘
* 第二步：选择a-z或0-9中任意一个作为缓冲器的名字，准备开始录制宏
* 第三步：正常的操作，此次所有的操作都会被记录在上一步中定义的缓冲器中
* 第四步：在非insert模式下输入q停止宏的录制
* 第五步：使用@ + 第二步中定义的缓冲器的名字即可。

![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190712142247.png)

观察可以发现他们的规律，在每行文字的开头添加“System.out.println(”，结尾添加“);”就变成下面的信息了。下面简单介绍一下如何使用recording来完成这样的操作。

* 首先把光标移动line1上，
* 输入qt，准备开始录制，
* **缓冲器的名字为t**，
* 录制的动作为：shift + ^ 回到行首、按下i键进入insert模式、输入“System.out.println(”、按下esc键回到正常模式、shift + $ 回到行尾部、按下i键进入insert模式、输入“);”
* 按下esc键回到正常模式，按下q停止录制。
* 然后把光标移动到下面一行的任意位置输入 @ + t 即可。

* recording还可以和查询结合起来使用，例如想把一个文件中含有特定字符串的行注释，可以通过这样的宏来实现。在正常模式下输入/search string + enter、shift + ^、i、#、esc、shift + $。
* 让定制的宏自动执行多次的方法是先输入一个数字，然后在输入@ + 缓冲器的名字。 例如 100@t，表示执行100次。

### 使用 vi/vim 进入一般模式

如果你想要使用 vi 来建立一个名为 test.txt 的文件时，你可以这样做：

$ vi runoob.txt

直接输入** vi 文件名 **就能够进入 vi 的一般模式了。请注意，记得 vi 后面一定要加文件名，不管该文件存在与否！

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295559313018.jpg)

### 按下 i 进入输入模式(也称为编辑模式)，开始编辑文字

在一般模式之中，只要按下 i, o, a 等字符就可以进入输入模式了！

在编辑模式当中，你可以发现在左下角状态栏中会出现 –INSERT- 的字样，那就是可以输入任意字符的提示。

这个时候，键盘上除了 **Esc** 这个按键之外，其他的按键都可以视作为一般的输入按钮了，所以你可以进行任何的编辑。

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295559394282.jpg)

### 按下 ESC 按钮回到一般模式

好了，假设我已经按照上面的样式给他编辑完毕了，那么应该要如何退出呢？是的！没错！就是给他按下 **Esc** 这个按钮即可！马上你就会发现画面左下角的 – INSERT – 不见了！

### 在一般模式中按下 **:wq** 储存后离开 vi

OK，我们要存档了，存盘并离开的指令很简单，输入 **:wq** 即可保存离开！

![](http://pic-mike.oss-cn-hongkong.aliyuncs.com/qiniu/15295559471425.jpg)

OK! 这样我们就成功创建了一个 runoob.txt 的文件。

## Plugins

* 🌿 Another elegant statusline for vim
    * [liuchengxu/eleline.vim: Another elegant statusline for vim](https://github.com/liuchengxu/eleline.vim)
    * Plug 'liuchengxu/eleline.vim'
    * ![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190712152343.png)
* Vim for markdown
    * [suan/vim-instant-markdown: Instant Markdown previews from VIm!](https://github.com/suan/vim-instant-markdown)
* NERDTree
    * [scrooloose/nerdtree: A tree explorer plugin for vim.](https://github.com/scrooloose/nerdtree)
* ctrlp.vim
    * 好用的文件搜索<C-p>，Plugin 'kien/ctrlp.vim'[ctrlp.vim ÷ home](http://kien.github.io/ctrlp.vim/#installation)
* undoTree [mbbill/undotree: The undo history visualizer for VIM](https://github.com/mbbill/undotree)
![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190713033813.png)
* easymotion，搜索结果的快速跳转[easymotion/vim-easymotion: Vim motions on speed!](https://github.com/easymotion/vim-easymotion)
* Fzf
    * 使用Ag [PATTERN]模糊搜索字符串
    * 使用Files [PATH]模糊搜索目录
* MattesGroeger/vim-bookmarks[MattesGroeger/vim-bookmarks: Vim bookmark plugin](https://github.com/MattesGroeger/vim-bookmarks)
    * ![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190713105519.gif)

| Action | Shortcut | Command |
| --- | --- | --- |
| Add/remove bookmark at current line | `mm` | `:BookmarkToggle` |
| Add/edit/remove annotation at current line | `mi` | `:BookmarkAnnotate <TEXT>` |
| Jump to next bookmark in buffer | `mn` | `:BookmarkNext` |
| Jump to previous bookmark in buffer | `mp` | `:BookmarkPrev` |
| Show all bookmarks (toggle) | `ma` | `:BookmarkShowAll` |
| Clear bookmarks in current buffer only | `mc` | `:BookmarkClear` |
| Clear bookmarks in all buffers | `mx` | `:BookmarkClearAll` |
| Move up bookmark at current line | `[count]mkk` | `:BookmarkMoveUp [<COUNT>]` |
| Move down bookmark at current line | `[count]mjj` | `:BookmarkMoveDown [<COUNT>]` |
| Move bookmark at current line to another line | `[count]mg` | `:BookmarkMoveToLine <LINE>` |
| Save all bookmarks to a file |  | `:BookmarkSave <FILE_PATH>` |
| Load bookmarks from a file |  | `:BookmarkLoad <FILE_PATH>` |


## Neovim

[neovim/neovim: Vim-fork focused on extensibility and usability](https://github.com/neovim/neovim)

```linux
brew install --HEAD neovim
```

官方推荐，neovim的配置文件vimrc位于的
```linux
~/.config/nvim/init.vim
```
![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190713014909.png)


## Space-Vim

> 这些感觉都是vim的快捷键的很多修改，高度使用Vim进行Code,但目前还未有这个需求，仅供参考。

![](https://pic-mike.oss-cn-hongkong.aliyuncs.com/Blog/20190713134019.png)

* [超漂亮 vim 配置：space-vim - 简书](https://www.jianshu.com/p/6bf206d68163)
* [liuchengxu/space-vim: Lean & mean spacemacs-ish Vim distribution](https://github.com/liuchengxu/space-vim)

### SpaceVim

* [使用文档 | SpaceVim](https://spacevim.org/cn/documentation/)
* [SpaceVim Tutorial On Mac - Zeech's Tech Blog](https://zcheng.ren/2018/07/27/spacevimtutorial/)
* [Quick start guide | SpaceVim](https://spacevim.org/quick-start-guide/)
* [Home | SpaceVim](https://spacevim.org/)


## 我的Vim配置

### 参考配置

* [theniceboy/vimrc-example](https://github.com/theniceboy/vimrc-example)
* [spf13/spf13-vim: The ultimate vim distribution](https://github.com/spf13/spf13-vim)

### `.vimrc`文件

```linux
"==========================================
" vim-bundles插件
"==========================================

if filereadable(expand("~/.vimrc.bundles"))
  source ~/.vimrc.bundles
endif

" vundle 环境设置
filetype off
set rtp+=~/.vim/bundle/Vundle.vim
" vundle 管理的插件列表必须位于 vundle#begin() 和 vundle#end() 之间
call vundle#begin()
"Plugin 'scrooloose/nerdtree'
"Plugin 'Shougo/deoplete.nvim'
Plugin 'VundleVim/Vundle.vim'
Plugin 'junegunn/fzf.vim'
Plugin 'junegunn/gv.vim'
Plugin 'tpope/vim-fugitive'
Plugin 'airblade/vim-gitgutter'
Plugin 'edkolev/tmuxline.vim'
Plugin 'majutsushi/tagbar'
Plugin 'roxma/nvim-yarp'
Plugin 'roxma/vim-hug-neovim-rpc'
Plugin 'tomasr/molokai'
Plugin 'vim-scripts/phd'
Plugin 'vim-airline/vim-airline'
Plugin 'octol/vim-cpp-enhanced-highlight'
Plugin 'kien/ctrlp.vim'
Plugin 'mhinz/vim-startify'
Plugin 'easymotion/vim-easymotion'
Plugin 'MattesGroeger/vim-bookmarks'
Plugin 'suan/vim-instant-markdown'
Plugin 'altercation/vim-colors-solarized'
" 插件列表结束
call vundle#end()
filetype plugin indent on


" ==
" == NERDTree-git
" ==
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ "Unknown"   : "?"
    \ }

"==========================================
"General
"==========================================
" history存储长度。
set history=1000
" 检测文件类型
filetype on
" 针对不同的文件类型采用不同的缩进格式
filetype indent on
" 允许插件
filetype plugin on
" 启动自动补全
filetype plugin indent on
" 兼容vi模式。去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限
set nocompatible
set autoread          " 文件修改之后自动载入。
set shortmess=atI       " 启动的时候不显示那个援助索马里儿童的提示
set wildmenu       	" 自动补全菜单
set scrolljump=5       	" 光标自动滚动
set scrolloff=3       	" 光标自动滚动

"==========================================
" show and format
"==========================================
" 显示行号：
set number
set relativenumber
set nowrap                    " 取消换行。
" 为方便复制，用<F6>开启/关闭行号显示:
nnoremap <F6> :set nonumber!<CR>:set foldcolumn=0<CR>

" 括号配对情况
set showmatch
" How many tenths of a second to blink when matching brackets
set mat=2

" 设置文内智能搜索提示
" 高亮search命中的文本。
set hlsearch
" 搜索时忽略大小写
set ignorecase
" 随着键入即时搜索
set incsearch
" 有一个或以上大写字母时仍大小写敏感
set smartcase

" 代码折叠
set foldenable
" 折叠方法
" manual    手工折叠
" indent    使用缩进表示折叠
" expr      使用表达式定义折叠
" syntax    使用语法定义折叠
" diff      对没有更改的文本进行折叠
" marker    使用标记进行折叠, 默认标记是 {{{ 和 }}}
set foldmethod=syntax
" 在左侧显示折叠的层次
" set foldcolumn=4
" 基于缩进或语法进行代码折叠
"set foldmethod=indent
set foldmethod=syntax
" 启动 vim 时关闭折叠代码
set nofoldenable

set tabstop=4                " 设置Tab键的宽度        [等同的空格个数]
set shiftwidth=4
set expandtab                " 将Tab自动转化成空格    [需要输入真正的Tab键时，使用 Ctrl+V + Tab]
" 按退格键时可以一次删掉 4 个空格
set softtabstop=4

set ai "Auto indent
set si "Smart indent

" 开启语法高亮功能
syntax enable
" 允许用指定语法高亮配色方案替换默认方案
syntax on


" 禁止光标闪烁
set gcr=a:block-blinkon0
" 禁止显示滚动条
set guioptions-=l
set guioptions-=L
set guioptions-=r
set guioptions-=R
" 禁止显示菜单和工具条
set guioptions-=m
set guioptions-=T

" 总是显示状态栏
set laststatus=2
" 显示光标当前位置
set ruler
" 开启行号显示
set number
" 高亮显示当前行/列
set cursorline
" 高亮显示搜索结果
set hlsearch
" 禁止折行
set nowrap

" 设置状态栏主题风格
let g:Powerline_colorscheme='solarized256'
" 搜索替换
let g:ackprg = 'ag --nogroup --nocolor --column'


" NERDTree config  自动打开
" open a NERDTree automatically when vim starts up
"autocmd vimenter * NERDTree
"open a NERDTree automatically when vim starts up if no files were specified
"autocmd StdinReadPre * let s:std_in=1
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
"open NERDTree automatically when vim starts up on opening a directory
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
"map tt to open NERDTree
map tt :NERDTreeToggle<CR>

"Tagbar
nmap pp :TagbarToggle<CR>

"bookmark_sign
highlight BookmarkSign ctermbg=NONE ctermfg=160
highlight BookmarkLine ctermbg=194 ctermfg=NONE
let g:bookmark_sign = '♥'
let g:bookmark_highlight_lines = 1

"Common Shortcuts
"map S to save files
map S :w<CR>
"map Q to exit normol model
map Q :q<CR>
"map R to exit normol model
map M :source $MYVIMRC<CR>
noremap U 5j
noremap E 5k

"close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Use deoplete.
let g:deoplete#enable_at_startup = 1

" Use easymotion.
nmap ss <Plug>(easymotion-s2)

" fzf If installed using Homebrew
set rtp+=/usr/local/opt/fzf
" If installed using git
set rtp+=~/.fzf"
```

### `init.vim`文件

```linux
"==========================================
" vim-plug插件
"==========================================
" vim-plug 环境设置
" - For Neovim: ~/.local/share/nvim/plugged
call plug#begin('~/.vim/plugged')

Plug 'scrooloose/nerdtree'
"Plug 'Shougo/deoplete.nvim'
Plug 'junegunn/fzf.vim'
Plug 'junegunn/gv.vim'
Plug 'tpope/vim-fugitive'
Plug 'airblade/vim-gitgutter'
Plug 'edkolev/tmuxline.vim'
Plug 'majutsushi/tagbar'
Plug 'roxma/nvim-yarp'
Plug 'roxma/vim-hug-neovim-rpc'
Plug 'tomasr/molokai'
Plug 'vim-scripts/phd'
Plug 'vim-airline/vim-airline'
Plug 'octol/vim-cpp-enhanced-highlight'
Plug 'kien/ctrlp.vim'
Plug 'mhinz/vim-startify'
Plug 'easymotion/vim-easymotion'
Plug 'MattesGroeger/vim-bookmarks'
Plug 'suan/vim-instant-markdown'
Plug 'altercation/vim-colors-solarized'

" 插件列表结束
call plug#end()
filetype plugin indent on


" ==
" == NERDTree-git
" ==
let g:NERDTreeIndicatorMapCustom = {
    \ "Modified"  : "✹",
    \ "Staged"    : "✚",
    \ "Untracked" : "✭",
    \ "Renamed"   : "➜",
    \ "Unmerged"  : "═",
    \ "Deleted"   : "✖",
    \ "Dirty"     : "✗",
    \ "Clean"     : "✔︎",
    \ "Unknown"   : "?"
    \ }

"==========================================
"General
"==========================================
" history存储长度。
set history=1000
" 检测文件类型
filetype on
" 针对不同的文件类型采用不同的缩进格式
filetype indent on
" 允许插件
filetype plugin on
" 启动自动补全
filetype plugin indent on
" 兼容vi模式。去掉讨厌的有关vi一致性模式，避免以前版本的一些bug和局限
set nocompatible
set autoread          " 文件修改之后自动载入。
set shortmess=atI       " 启动的时候不显示那个援助索马里儿童的提示
set wildmenu       	" 自动补全菜单
set scrolljump=5       	" 光标自动滚动
set scrolloff=3       	" 光标自动滚动

"==========================================
" show and format
"==========================================
" 显示行号：
set number
set relativenumber
set nowrap                    " 取消换行。
" 为方便复制，用<F6>开启/关闭行号显示:
nnoremap <F6> :set nonumber!<CR>:set foldcolumn=0<CR>

" 括号配对情况
set showmatch
" How many tenths of a second to blink when matching brackets
set mat=2

" 设置文内智能搜索提示
" 高亮search命中的文本。
set hlsearch
" 搜索时忽略大小写
set ignorecase
" 随着键入即时搜索
set incsearch
" 有一个或以上大写字母时仍大小写敏感
set smartcase

" 代码折叠
set foldenable
" 折叠方法
" manual    手工折叠
" indent    使用缩进表示折叠
" expr      使用表达式定义折叠
" syntax    使用语法定义折叠
" diff      对没有更改的文本进行折叠
" marker    使用标记进行折叠, 默认标记是 {{{ 和 }}}
set foldmethod=syntax
" 在左侧显示折叠的层次
" set foldcolumn=4
" 基于缩进或语法进行代码折叠
"set foldmethod=indent
set foldmethod=syntax
" 启动 vim 时关闭折叠代码
set nofoldenable

set tabstop=4                " 设置Tab键的宽度        [等同的空格个数]
set shiftwidth=4
set expandtab                " 将Tab自动转化成空格    [需要输入真正的Tab键时，使用 Ctrl+V + Tab]
" 按退格键时可以一次删掉 4 个空格
set softtabstop=4

set ai "Auto indent
set si "Smart indent

" 开启语法高亮功能
syntax enable
" 允许用指定语法高亮配色方案替换默认方案
syntax on


" 禁止光标闪烁
set gcr=a:block-blinkon0
" 禁止显示滚动条
set guioptions-=l
set guioptions-=L
set guioptions-=r
set guioptions-=R
" 禁止显示菜单和工具条
set guioptions-=m
set guioptions-=T

" 总是显示状态栏
set laststatus=2
" 显示光标当前位置
set ruler
" 开启行号显示
set number
" 高亮显示当前行/列
set cursorline
" 高亮显示搜索结果
set hlsearch
" 禁止折行
set nowrap

" 设置状态栏主题风格
let g:Powerline_colorscheme='solarized256'
" 搜索替换
let g:ackprg = 'ag --nogroup --nocolor --column'


" NERDTree config  自动打开
" open a NERDTree automatically when vim starts up
"autocmd vimenter * NERDTree
"open a NERDTree automatically when vim starts up if no files were specified
"autocmd StdinReadPre * let s:std_in=1
"autocmd VimEnter * if argc() == 0 && !exists("s:std_in") | NERDTree | endif
"open NERDTree automatically when vim starts up on opening a directory
autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | endif
"map tt to open NERDTree
map tt :NERDTreeToggle<CR>

"Tagbar
nmap pp :TagbarToggle<CR>

"bookmark_sign
highlight BookmarkSign ctermbg=NONE ctermfg=160
highlight BookmarkLine ctermbg=194 ctermfg=NONE
let g:bookmark_sign = '♥'
let g:bookmark_highlight_lines = 1

"Common Shortcuts
"map S to save files
map S :w<CR>
"map Q to exit normol model
map Q :q<CR>
"map R to exit normol model
map M :source $MYVIMRC<CR>
noremap U 5j
noremap E 5k

"close vim if the only window left open is a NERDTree
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif

" Use deoplete.
let g:deoplete#enable_at_startup = 1

" Use easymotion.
nmap ss <Plug>(easymotion-s2)

" fzf If installed using Homebrew
set rtp+=/usr/local/opt/fzf
" If installed using git
set rtp+=~/.fzf
```




## 参考

1. [简明 Vim 练级攻略 | | 酷 壳 - CoolShell](https://coolshell.cn/articles/5426.html)
2. [看完这篇Linux基本的操作就会了 - 简书](https://www.jianshu.com/p/a182a0be4b8a#%E5%9B%9B%E3%80%81VI%E7%BC%96%E8%BE%91%E5%99%A8)
3. [Linux vi/vim | 菜鸟教程](http://www.runoob.com/linux/linux-vim.html)
4. [PacVim](https://zhuanlan.zhihu.com/p/37988604)
5. [程序员内功系列--Vim篇 | iTimothy](https://xiaozhou.net/learn-the-command-line-vim-2018-08-08.html)
