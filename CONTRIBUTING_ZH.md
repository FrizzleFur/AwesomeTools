# 贡献指南

感谢您对 Awesome Tools 项目的关注！我们欢迎各种形式的贡献，包括但不限于：

- 添加新工具
- 更新现有工具信息
- 修复错误
- 改进文档
- 翻译
- 提出建议和反馈

## 开始之前

1. 在开始之前，请确保您已阅读并同意我们的[行为准则](CODE_OF_CONDUCT_ZH.md)
2. 查看[问题跟踪器](https://github.com/FrizzleFur/AwesomeTools/issues)以查找要处理的问题或功能请求
3. 如果您想添加新工具或功能，请先创建一个问题讨论

## 工作流程

1. Fork 本仓库
2. 创建您的功能分支 (`git checkout -b feature/amazing-feature`)
3. 提交您的更改 (`git commit -m 'Add some amazing feature'`)
4. 推送到分支 (`git push origin feature/amazing-feature`)
5. 打开一个 Pull Request

## 添加新工具

### 1. 创建工具文档

1. 在 `docs/tools/` 下创建适当的目录结构
2. 使用[工具模板](docs/templates/tool_template_zh.md)创建新工具的文档
3. 确保包含以下部分：
   - 工具名称和简短描述
   - 基本信息（版本、许可证、平台等）
   - 安装说明
   - 使用示例
   - 配置选项
   - 常见问题解答

### 2. 更新分类文档

1. 导航到相关的分类文档（如 `docs/categories/development.md`）
2. 在适当的章节下添加新工具的链接
3. 确保工具按字母顺序排列
4. 提供简短的描述（1-2句话）

### 3. 提交更改

1. 添加并提交您的更改：
   ```bash
   git add .
   git commit -m "docs: add [工具名称] to [分类]"
   ```
2. 推送到您的分支：
   ```bash
   git push origin your-branch-name
   ```
3. 创建 Pull Request

## 文档规范

### 文件命名

- 使用小写字母和连字符（kebab-case）
- 例如：`visual-studio-code.md`

### 图片和资源

- 将图片放在 `docs/assets/images/` 目录下
- 使用有意义的文件名，例如：`vscode-interface.png`
- 图片大小应适当优化，建议宽度不超过 1200px

### Markdown 格式

- 使用 ATX 风格的标题（`## 标题`）
- 列表项后添加空行
- 代码块指定语言
- 链接使用引用样式：`[链接文本][ref]`

## 代码风格

### Shell 脚本

- 使用 2 空格缩进
- 引用所有变量：`"$variable"`
- 使用 `[[` 而不是 `[` 进行条件测试
- 使用 `set -euo pipefail` 使脚本更健壮

### Python 脚本

- 遵循 [PEP 8](https://www.python.org/dev/peps/pep-0008/) 风格指南
- 使用 4 空格缩进
- 导入顺序：标准库、第三方库、本地应用/库

## 提交信息规范

提交信息应遵循 [Conventional Commits](https://www.conventionalcommits.org/) 规范：

```
<类型>[可选的作用域]: <描述>

[可选的正文]

[可选的脚注]
```

### 提交类型

- `feat`: 新功能
- `fix`: 修复 bug
- `docs`: 文档更新
- `style`: 代码格式（不影响代码运行的变动）
- `refactor`: 重构（既不增加新功能，也不是修复 bug）
- `perf`: 性能优化
- `test`: 增加测试
- `chore`: 构建过程或辅助工具的变动

### 示例

```
feat: 添加 Visual Studio Code 工具文档

docs: 更新 README 中的安装说明

fix: 修复 Python 脚本中的语法错误
```

## 代码审查

- 所有提交都需要通过代码审查
- 至少需要一个维护者批准才能合并
- 保持建设性的反馈
- 及时响应审阅意见

## 报告问题

如果您发现错误或有功能建议，请[创建新问题](https://github.com/FrizzleFur/AwesomeTools/issues/new/choose)。

### 错误报告

请提供：

1. 重现步骤
2. 预期行为
3. 实际行为
4. 环境信息（操作系统、版本等）
5. 相关日志或截图

### 功能请求

请描述：

1. 您想要什么功能？
2. 为什么需要这个功能？
3. 您认为应该如何实现？

## 许可证

通过向本项目提交贡献，您同意您的贡献将采用 [MIT 许可证](LICENSE) 授权。

## 致谢

感谢所有为这个项目做出贡献的人！

[![Contributors](https://contrib.rocks/image?repo=FrizzleFur/AwesomeTools)](https://github.com/FrizzleFur/AwesomeTools/graphs/contributors)
