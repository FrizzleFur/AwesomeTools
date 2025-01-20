# Quicktype

## 简介
Quicktype是一个在线代码生成工具，可以根据JSON数据自动生成对应的类型定义和序列化代码。

## 主要功能
- 支持多种编程语言
- 根据JSON生成类型定义
- 自动生成序列化/反序列化代码
- 支持TypeScript、Swift、Go等语言

## 使用示例
输入JSON：
```json
{
  "name": "John",
  "age": 30,
  "isMarried": false
}
```

生成TypeScript代码：
```typescript
interface Person {
  name: string;
  age: number;
  isMarried: boolean;
}
```

## 在线工具
[Quicktype在线工具](https://app.quicktype.io/)

## 参考图片
![Quicktype示例](https://i.loli.net/2018/11/02/5bdbea2317a77.jpg)
