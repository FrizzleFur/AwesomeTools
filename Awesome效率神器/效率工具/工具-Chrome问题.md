## Chrome问题

[](https://www.google.com.hk/search?newwindow=1&safe=strict&biw=1396&bih=798&ei=8mOgW5O8GKjN0PEPh8aT4A8&q=chrome+%E6%AF%8F%E6%AC%A1+%E7%99%BB%E5%BD%95&oq=chrome+%E6%AF%8F%E6%AC%A1+%E7%99%BB%E5%BD%95&gs_l=psy-ab.12...41934.42488.0.43296.3.3.0.0.0.0.283.283.2-1.1.0....0...1c.1.64.psy-ab..2.0.0....0.PvOqVOMkjUU)

昨天遇到了这个问题，每次用 Command+Q 完全退出 chrome 后，下次再打开 chrome 之前登录的账号就自动给退出了，又要重新登录特别麻烦；
下面是我的解决办法，亲测有效：

完全卸载后再重装 chrome ；

完全卸载：
在 application 里把 chrome 拖到废纸篓后，再去 finder 的这三个路径下完全删除 Chrome 相关的文件：


```
/Users/XXX/Library/Application Support/Google/Chrome
/Users/XXX/Library/Caches/Google/Chrome
/Library/Google/
```