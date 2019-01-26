## Node-Npm脚本安装

现在：NPM包的路径

```
/usr/local/lib/node_modules/
```

[01 - npm 是什么？ | npm 中文文档](https://www.npmjs.cn/getting-started/what-is-npm/)


### Npm脚本安装权限问题

```
╰─ npm install -g weex-toolkit
npm WARN checkPermissions Missing write access to /usr/local/lib/node_modules
npm ERR! path /usr/local/lib/node_modules
npm ERR! code EACCES
npm ERR! errno -13
npm ERR! syscall access
npm ERR! Error: EACCES: permission denied, access '/usr/local/lib/node_modules'
npm ERR!  { Error: EACCES: permission denied, access '/usr/local/lib/node_modules'
npm ERR!   stack: 'Error: EACCES: permission denied, access \'/usr/local/lib/node_modules\'',
npm ERR!   errno: -13,
npm ERR!   code: 'EACCES',
npm ERR!   syscall: 'access',
npm ERR!   path: '/usr/local/lib/node_modules' }
npm ERR!
npm ERR! Please try running this command again as root/Administrator.

```

[修复权限 | npm](https://wohugb.gitbooks.io/npm/content/getting_started/fixing_npm_permissions.html)

### 解决

可能是路径错了，尽量不要使用sudo

```
sudo chown -R $USER /usr/local
```


[Cannot install reason on mac os x · Issue #1888 · facebook/reason](https://github.com/facebook/reason/issues/1888)

solution [#2](https://github.com/facebook/reason/issues/2) worked for me. For future reference here is what I did (taken for the link : [https://docs.npmjs.com/getting-started/fixing-npm-permissions](https://docs.npmjs.com/getting-started/fixing-npm-permissions))



Make a directory for global installations:

`mkdir ~/.npm-global`

Configure npm to use the new directory path:

`npm config set prefix '~/.npm-global'`

Open or create a ~/.profile file and add this line:

`export PATH=~/.npm-global/bin:$PATH`

Back on the command line, update your system variables:

`source ~/.profile`

And then finally:

`npm install -g bs-platform`



