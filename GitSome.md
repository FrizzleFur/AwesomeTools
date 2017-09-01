# Gitsome

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


### 命令

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


