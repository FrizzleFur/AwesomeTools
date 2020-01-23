# AppCode

## Inspections
快捷方式和设置

要点
AppCode它致力于完美的代码，并帮助您找到需要改善的地方。所以这里是 Code Inspection mechanism的一小部分。

即时Inspections工作并突出显示潜在问题：


要浏览突出显示的问题，请使用F2（到下一个）和↑F2（到前一个）。 此外，该机制suggests针对问题快速修复（将光标放到有问题的代码后按⌥⏎可以看到它）：


设置
如果您认为此问题可能出现在项目的另一个范围内，您可以对其进行Inspections，甚至可以立即修复此类问题。所有这些inspection settings 都可在context menu部分中找到：


如果您不认为这是一个问题或者不希望IDE在这种情况下打扰您，您可以将其限制为有限的 limited scope - file，method，statement - so，以便它仍然可以在此选择范围之外工作但不会打扰您：

1.突出显示问题（⌘F1）


2.打开Inspections context menu（⌥⏎）


3.选择禁止Inspections所需范围，例如语句：


您可以通过“Remove suppression”意图操作（⌥⏎）轻松删除 suppression：


当然，你可以为整个项目禁用它。如果您选择Edit inspection... AppCode将显示特定Inspections的首选项，您可以在其中阅读说明，管理severity （choose from Typo, Server problem, Weak warning, Info, Warning, Error)），甚至在某些情况下配置Inspections参数以更准确地反映您的需求。您可以为Simplifiable statement执行此操作，例如：


AppCode中的所有Inspections都分为几组：Objective-C，C ++，Swift，General，CSS，XML，JavaScript等。有些是基于编译警告，而有些则是将您带到下一个级别。完整的Inspections清单包括100多种可能性。转到Preferences | Inspections。此外，还可以将各种配置保存为命名配置文件，并在一个项目内的不同项目或范围内单独使用它们。

Try in action
这是一个缺失switch的案例问题。

1.AppCode在您键入时突出显示特定问题（用⌘F1查看说明）。例如，suggests在switch case中缺少某些枚举值，或者省略默认分支：


2.然后你可以使用快速修复（⌥⏎），如添加默认分支：


3.接受后：


4.或者从context menu中选择操作（⌥⏎）：


运行单一inspection
如果需要调用某些特定 inspection，请使用“ Run Inspection by name”操作：


开始输入名称，AppCode可以帮助您完成其余的工作。通过调用Code | Inspect Code，可以获得项目suggested问题的完整列表。

在那里你会发现你想要Inspections的文件范围的几种可能性：

整个项目;
未提交的文件（如果有的话）;
最近查看过的文件;
pre-configured的范围。

运行时，AppCode会显示在所选范围中找到的完整 inspections列表：


您可以浏览此列表，按目录或Severity对问题进行分组，应用快速修复（对一个或多个错误）和编辑设置。


单击ac InspTutorial hector 状态栏上的Hector图标或按⌥⇧⌘H，您将能够：

1.配置突出显示级别：将滑块移动到三个可用位置之一：

None：关闭编辑器中突出显示的问题;
Syntax：仅突出显示语法问题;
Inspections:(默认）突出显示语法问题和Inspections问题。
2.配置Inspections。

3.打开/关闭省电模式（同样可以在File | Power Save Mode中完成） - 但此模式会关闭动态代码Inspections。





## 搜索和导航


导航视图
快捷方式和设置



AppCode中有很多导航视图。知道在给定情况下调用哪一个将有助于您更有效地使用IDE。

所述项目视图（⌘1）是类似于Xcode中的项目导航仪。它显示特定工作空间中包含的所有项目以及其中的所有文件和组：


默认情况下，AppCode中的“ Project”视图以相同顺序显示文件和文件夹，他们存储在文件系统中。您可以通过在选项菜单中选择Manual order来更改它（如果您在设置AppCode时选择了Xcode行为，则会自动启用此选项）：


还有 Autoscroll from source和Autoscroll to source。前者允许您在选择文件时自动打开文件代码，而后者在编辑器区域处于焦点时自动将焦点设置在项目视图中的文件名上：


Files view是AppCode Project view的另一个模式。它显示.xcworkspace或.xcproject所在目录中的所有文件。使用此视图，您可以轻松打开任何未包含在项目中的文件并进行查看。由于AppCode具有许多针对各种文件类型的插件集成，因此它可能会有所帮助，例如，当您需要README.md在项目中编辑时 ：


Structure view （⌘7）和Structure popup（⌥F12）显示特定文件的结构以及代码中的所有// TODO，// FIXME和#pragma mark或// MARK注释。 它们的工作方式与Xcode中的Symbol导航器类似：


The Imports hierarchy （⌥⇧H）和Call hierarchy视图（⌃⌥H）允许您查看特定文件中的hierarchy of imports，或者在Objective-C和C ++中调用特定方法或函数：


The Find in Path（⇧⌘F）对话框提供与Xcode中的Find navigator相同的功能。用它来进行全文搜索：


在搜索代码使用（变量，方法，类名等的用法）时，建议使用 Find Usages。它不是仅搜索文本，而且显示特定代码符号的实际用法：


The Build messages工具窗口（⌘0）显示编译器输出，并可以过滤按类型建立的消息：


The Run tool window （⌘4）显示控制台，您可以在其中查看应用程序的输出（如果运行Test Run Configuration，则显示Tests运行器）。

The Debug tool window（⌘5）类似于Xcode中的Debug navigator。 它显示了右侧的所有watches，局部变量以及左侧的线程列表：


The Breakpoints dialog（⇧⌘F8）与Xcode中的Breakpoint navigator具有相同的功能 - 它显示项目中所有断点的列表：


TODO工具窗口在单独的窗口中显示代码中的所有// TODO和// FIXME注释标记：


请注意，您还可以使用左侧的“ Filter TODO Items ”按钮为自定义标记创建自定义过滤器 ：


The Bookmarks对话框 显示代码中的书签：


在AppCode中，只需按F3即可为代码中的任何位置或Project工具窗口中的任何文件添加书签。 通过Edit编辑说明以给出书签摘要。

VCS工具窗口（⌘9）提供了使用版本控制系统所需的一切，包括更改视图，VCS日志等：


the Favorites tool window （⌘2）聚合书签，断点和收藏夹：


在工具窗口中搜索和过滤内容
几乎所有AppCode中的工具窗口和对话框（具有专用搜索字段的工具窗口和对话框）都允许您通过键入一些文本来搜索和过滤其内容。如果您不记得整个名称，请尝试使用模糊匹配，只需键入要搜索的实体的一部分：


代码内导航
快捷方式和设置


Go to...
处理项目时，通常需要打开并编辑特定的类或文件。最快的方法是分别使用Go to Class（⌘O）或Go to File（⇧⌘O）：


Go to Symbol （⌥⌘O）可以直接导航到代码中的符号 - 使用模糊匹配只输入名称的一部分：


Go to ...系列的另一个重要动作是Go to definition。只需将插入符号放在任何符号（变量或方法）上，然后按⌘B 即可跳转到其定义。


Go to super definition（⌘U）将导航到父类声明。使用Go to related symbol（⌃⌘↑）在标题和实现之间跳转。

快速定义和文档
要在代码中查看符号的快速定义，只需按⌘Y：


F1显示插入符号下符号的 Quick documentation。

Gutter navigation
gutter区域中的小图标是浏览代码的另一种方式。它们可用于浏览类层次结构：


只需单击一下这些小图标就可以导航到方法的定义或声明，super方法，重写方法，实现或超类等等。

最近的文件和Switcher
最近的文件（⌘E）显示项目中最近打开的文件列表:


Switcher视图（⌃⇥）显示相同的窗口，与macOS上的窗口切换器相同。

搜索
使用Find Usages（⌥F7）搜索任何代码构造（类，变量，方法等）：

使用Find in Path（⇧⌘F）在项目或目录中执行常规全文搜索。
使用Find和（↑/ ↓)在单个文件中搜索并在匹配中向后/向前导航。注意，您可以使用正则表达式进行搜索
使用⇧⇧Search Everywhere（即使在IDE设置中）：

按下⇧⌘A以查找IDE中的任何操作或您需要的任何首选项，并直接跳转到所需位置：


## 参考

* [AppCode使用技巧（四）——搜索和导航](https://www.evget.com/article/2018/8/10/28315.html)