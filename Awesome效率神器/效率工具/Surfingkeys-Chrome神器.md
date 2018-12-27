## Surfingkeys

> [Surfingkeys](https://chrome.google.com/webstore/detail/surfingkeys/gfbliohnnapiefjpjlpjnehglfpaknnc)是Chrome上的一个神器，开发者将Chrome上常用的操作封装成快捷键，使用后，感觉比[Vimium](https://chrome.google.com/webstore/detail/vimium/dbepggeogbaibhgnhhndojpepiihcmeb?hl=en)还要好用。
> Map your keys for web surfing, expand your browser with javascript and keyboard.

文档：[Surfingkeys/README_CN.md at master · brookhong/Surfingkeys](https://github.com/brookhong/Surfingkeys/blob/master/README_CN.md)

Surfingkeys有三种模式：normal，visual和insert。

* Normal mode，默认模式,当你打开一个页面时，自动进入该模式。通过函数mapkey添加的所有按键都只在这种模式下有用。
* Visual mode，用于选中文本，以及各种针对选中文本的操作
* Insert mode，当输入焦点定位到各类输入框时（无论你是通过i或f选择定位还是鼠标点击定位的），就进入该模式。 通过函数imapkey添加的所有按键都只在这种模式下有用。

### 可视模式

可视模式步骤：

1. 通过`v`进入可视模式,确认你能看到`Caret`提示和光标
2. 选择切入文本, 使用`j` `k` `h` `l` `b` `w``0` `$`试试移动光标。
3. 通过`v`进行选择文本
4. 其实选择文本可以通过`ymv`进行多个文本的复制

*   `zz` 让光标位于窗口中间行。
*   `f` 往前查找下一个字符。
*   `F` 往后查找下一个字符。
*   `;` 重复最后的`f`/`F`操作。
*   `,` 反向重复最后的`f`/`F`操作。


 名称 | 快捷键 
  :-: | :-: 
进入可视模式，并全选指定文本 |  zv
选择复制多个指定文本 | ymv
选择复制指定文本 | yv
切换可视模式 | v
恢复可视模式 | V
跳到行首 | 0
前进一个字符 | l
后退一个字符 | h
下一行 | j
上一行 | k
前进一个单词 | w
前进一个单词 | e
后退一个单词 | b
前进一个句子 | )
后退一个句子 | (
前进一个段落 | }
后退一个段落 | {
跳到行尾 | $
跳到页面结尾 | G
跳到页面开头 | gg
跳到页面结尾 |  o
点击光标下的元素 | <'Enter'>
把光标所在的位置放在屏幕中间 | zz
选中一个单词(w)／行(l)／句子(s)／段落(p) | V
复制一个单词(w)／行(l)／句子(s)／段落(p) | y
往上20行 | <'Ctrl-u'>
向下20行 | <'Ctrl-d'>
| **查找** |  |
在当前页查找 | /
在当前页查找选中文本 | *
下一处 | n
上一处 | N
查找光标下的单词 | *
重复相应的f/F | ;
往前查找字符 | f
往后查找字符 | F
反向重复相应的f/F | ,
| **其他** |  |
电脑语音阅读选中文本 | gr
翻译光标下的单词 | q

### 插入模式

 名称 | 快捷键 
  :-: | :-: 
把光标放到行尾 | <Ctrl-e>
把光标放到行首 | <Ctrl-f>
删除光标前的所有字符 | <Ctrl-u>
把光标往后移一个单词 | <Alt-b>
把光标往前移一个单词 | <Alt-f>
删除光标前一个单词 | <Alt-w>
删除光标后一个单词 | <Alt-d>
退出插入模式 | <Esc>
输入字符表情: | <Ctrl-'>
给当前输入加双引号 | <Ctrl-'>
打开VIM编辑器编辑当前输入 | <Ctrl-i>
给当前输入加双引号 | <Ctrl-'>

### 普通模式

| 名称 | 快捷键 |
| :-: | :-: |
| **打开连接** |  |
| 在新标签页后台打开链接 | gf |
| 在新标签页打开多个链接 | cf |
| 在新标签页打开链接 | af |
| 打开链接，如果拨号键有重叠按SHIFT | f |
|  打开文字中的超级链接  | O |
| 打开选中的网址或系统剪贴板里的网址 | cc |
| 复制链接 | ya |
| 复制当前页标题 | yl |
| 选择复制制定文本 | yv|
| 复制当前地址 | yy |
| 当前页后退 | S | 
| 当前页前进 | D | 
| 刷新当前页 | r | 
| 跳到当前地址的根路径 | gU |
| **标签页** |  |
| 跳到最早的那个标签页 | gT |
| 跳到最新的那个标签页 | gt |
| 选择标签页 | T |
| 复制当前标签页 | yt |
| 打开新标签 | on |
| 把当前标签页移入新窗口 | W |
|  往左移动当前标签页 | << |
| 往右移动当前标签页 |  >> |
| **搜索** |  | 
| 打开网页 | t | 
| 打开搜索栏查找当前标签页访问过的所有网址 | H | 
|  跳到第一个输入框 | gi |
| **文本** |  |
| 用stackoverflow搜索选中文本 | ss |
| 用百度搜索选中文本 | sb |
| 用谷歌搜索选中文本 | sg |
| **滚动** |  |
| 切换滚动目标 |  |
| 滚到最上边 | gg |
| 滚到最下边 | G |
| **其他** |  |
| 用谷歌翻译选中文本 | ;t |
|  电脑语音阅读选中文本或剪贴板里的文本  | gr |
| 删除30天前的所有访问历史记录  | ;dh | 
| 截屏 | yg | 
| 截长屏 | yG | 
| 退出Chrome | ZQ |
| 保存会话并退出 | ZZ |
| 恢复最近一次会话 | ZR |
| 显示最近一次操作 | sql |
| 重复最近一次操作 | . |
| **Chrome内置功能** |  |
| 打开收藏夹 | gb |
| 打开下载 | gd |
| 打开历史记录 |  gh |
打开扩展 | ge |

非常高效有木有，心里禁不住为作者喝彩，感谢作者~
还有可视模式，和插入模式，还没有深入的使用

### 打开连接

默认的拨号键有asdfgqwertzxcvb，如果按了一个非拨号键，会自动退出拨号。下面的设置可以改成右手习惯：

```
Hints.characters = 'yuiophjklnm'; // for right hand

```

**当拨号盘有重叠上，可以按Shift翻转重叠的拨号盘。按住空格键可隐藏拨号盘，松开恢复。**


### vim编辑器

用vim编辑器编辑textarea


