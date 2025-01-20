# Gitsome

## 简介
Gitsome 是一个Git命令行增强工具，提供了GitHub集成命令和自动补全功能，可以更方便地使用Git和GitHub。

## 主要功能
- GitHub集成命令
- 自动补全
- 查看GitHub趋势项目
- 搜索GitHub仓库
- 查看GitHub通知

## 安装方法
1. 使用Homebrew安装：
```bash
brew install gitsome
```

2. 安装完成后，在终端输入`gh`即可使用

## 常用命令
### 搜索仓库
```bash
gh search-repos "created:>=2015-01-01 stars:>=1000 language:python" --sort stars -p
```

### 查看趋势项目
```bash
gh trending [language] [-w/--weekly] [-m/--monthly] [-d/--devs] [-b/--browser]
```

### 查看搜索结果
```bash
gh view [#] [-b/--browser]
```

### GitHub集成命令列表
```bash
configure            # 配置gitsome
create-comment       # 在issue上创建评论
create-issue         # 创建issue
create-repo          # 创建仓库
emojis               # 列出GitHub支持的emoji
feed                 # 查看用户或仓库的活动
followers            # 查看关注者
following            # 查看关注的人
gitignore-template   # 输出指定语言的.gitignore模板
gitignore-templates  # 输出所有支持的.gitignore模板
issue                # 查看issue详情
issues               # 列出匹配的issues
license              # 输出指定license的模板
licenses             # 输出所有支持的license模板
me                   # 查看当前登录用户信息
notifications        # 查看通知
octo                 # 输出Octocat消息
pull-request         # 查看pull request详情
pull-requests        # 列出pull requests
rate-limit           # 查看API速率限制
repo                 # 查看仓库详情
repos                # 列出匹配的仓库
search-issues        # 搜索issues
search-repos         # 搜索仓库
starred              # 查看starred仓库
trending             # 查看趋势项目
user                 # 查看用户信息
view                 # 在终端或浏览器中查看内容
```

## 参考
[Gitsome GitHub仓库](https://github.com/donnemartin/gitsome)
