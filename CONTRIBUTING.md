# 贡献指南

感谢您有兴趣为 Awesome Tools 项目做出贡献！本指南将帮助您了解如何参与贡献。

## 如何贡献

### 报告问题

如果您发现任何错误或有改进建议，请先查看 [问题跟踪器](https://github.com/FrizzleFur/AwesomeTools/issues) 是否已存在类似问题。如果不存在，请创建一个新问题。

### 提交 Pull Request

1. Fork 本仓库并创建您的功能分支 (`git checkout -b feature/AmazingFeature`)
2. 提交您的更改 (`git commit -m 'Add some AmazingFeature'`)
3. 推送到分支 (`git push origin feature/AmazingFeature`)
4. 打开一个 Pull Request

## 文档规范

### 工具文档

每个工具应该有一个独立的 Markdown 文件，位于 `docs/tools/[tool-name]/README.md`。请参考 [工具文档模板](docs/templates/tool_template.md) 了解详细格式要求。

### 分类文档

分类文档位于 `docs/categories/` 目录下，用于组织相关工具。请参考 [分类文档模板](docs/templates/category_template.md) 了解详细格式要求。

## 提交信息规范

请遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范提交信息：

```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

### 提交类型

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式调整（不影响代码运行的变动）
- `refactor`: 代码重构
- `perf`: 性能优化
- `test`: 测试相关
- `chore`: 构建过程或辅助工具的变动

## 行为准则

请遵守 [贡献者公约](CODE_OF_CONDUCT.md) 中定义的行为准则。

## 许可证

通过提交 Pull Request，您同意根据 MIT 许可证授权您的贡献。

## 开始贡献

1. 确保您有 [Git](https://git-scm.com/) 和 [Node.js](https://nodejs.org/) 环境
2. Fork 并克隆仓库：
   ```bash
   git clone https://github.com/your-username/AwesomeTools.git
   cd AwesomeTools
   ```
3. 安装依赖：
   ```bash
   npm install
   ```
4. 创建一个新分支：
   ```bash
   git checkout -b feature/your-feature
   ```
5. 进行更改并提交
6. 推送到您的分支并创建 Pull Request

## 需要帮助？

如果您有任何问题，请随时在 [问题跟踪器](https://github.com/FrizzleFur/AwesomeTools/issues) 中提问。
