# Emmet

## 简介
Emmet是一个HTML/CSS代码快速编写工具，可以大幅提高前端开发效率。

## 主要功能
- 快速生成HTML结构
- 支持CSS缩写
- 支持多种编辑器集成
- 提供代码片段功能

## 安装方法
通过npm安装：
```bash
npm install -g emmet
```

## 使用示例
输入：
```html
ul>li*5>a{Item $}
```
输出：
```html
<ul>
  <li><a href="">Item 1</a></li>
  <li><a href="">Item 2</a></li>
  <li><a href="">Item 3</a></li>
  <li><a href="">Item 4</a></li>
  <li><a href="">Item 5</a></li>
</ul>
```

## 参考链接
[Emmet GitHub仓库](https://github.com/sergeche/emmet-sublime)
