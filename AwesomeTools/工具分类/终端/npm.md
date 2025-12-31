
# NPM



1. 切换 npm 镜像源
默认的 npm 源在国内可能不稳定，切换到国内镜像（如淘宝源）：


```
npm config set registry https://registry.npmmirror.com
```

恢复

```
npm config set registry https://registry.npmjs.org/
```