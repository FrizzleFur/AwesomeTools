# 任务计划：工具文档优化

## 📋 任务概述

**目标**: 优化 AwesomeTools 项目中的工具文档组织结构，改善分类、序号和可读性

**范围**:
- 工具-VSCode.md 的工具分类和序号优化
- AwesomeTools清单.md 的 Inbox 区域重构
- 其他工具文档的格式统一（可选）

---

## 🎯 执行阶段

### Phase 1: 分析与准备 ✅
- [x] 分析现有文档结构
- [x] 识别主要问题点
- [x] 创建本规划文件
- [x] 创建 findings.md 记录发现
- [x] 创建 progress.md 记录进度

**关键发现**:
- 工具-VSCode.md 包含 16+ 个工具，混合排列无分类
- AwesomeTools清单.md 的 Inbox 区域缺少分类
- Markdown 相关工具新增 4 个，需要合理组织

---

### Phase 2: 工具-VSCode.md 优化 🚧

#### 2.1 工具分类设计
**目标**: 按功能对 VSCode 扩展进行分类

**分类方案**:
1. **Markdown 编辑工具** (6个)
   - Markdown All in One
   - Markdown Preview Enhanced
   - markdown-markmap
   - markmap-vscode
   - vscode-markmap-universe
   - Instant Markdown

2. **代码编辑增强** (3个)
   - CSS Peek
   - Better Align
   - Paste JSON as Code

3. **项目管理与导航** (3个)
   - Bookmarks
   - Todo Tree
   - Reference Search View

4. **开发者工具** (3个)
   - Dash
   - Visual Studio IntelliCode
   - (其他开发工具)

5. **中文社区工具** (4个)
   - 掘金
   - 韭菜盒子
   - 前端盒子
   - LeetCode

#### 2.2 添加序号系统
- 采用层级序号：1.1, 1.2, 2.1, 2.2...
- 每个工具保留链接和描述

#### 2.3 格式统一
- 所有工具名称添加链接（如果缺失）
- 统一描述格式
- 保留所有现有内容

---

### Phase 3: AwesomeTools清单.md 优化 📝

#### 3.1 Inbox 区域重构
**目标**: 按类型分组，添加图标

**新结构**:
```markdown
## Inbox

### 📝 Markdown 工具
1. [vscode-markdown-markmap] - 思维导图预览
2. [markmap-vscode] - 官方扩展
3. [vscode-markmap-universe] - 增强版
4. [vscode-markdown-preview-enhanced] - 综合预览

### 🔧 开发工具
5. [uv] - Python 环境管理器
```

#### 3.2 添加分类说明
- 每个分类添加简短说明
- 保持工具数量序号连续

---

### Phase 4: 验证与调整 ✅ (待执行)

- [ ] 检查所有链接有效
- [ ] 确认格式一致性
- [ ] 跨文件引用更新
- [ ] 提交变更

---

## 📊 进度追踪

| 阶段 | 状态 | 完成时间 | 备注 |
|------|------|----------|------|
| Phase 1 | ✅ 完成 | 2025-02-18 15:20 | 分析完成 |
| Phase 2 | ✅ 完成 | 2025-02-18 15:30 | 工具-VSCode.md 重构完成 |
| Phase 3 | ✅ 完成 | 2025-02-18 15:30 | 清单文件优化完成 |
| Phase 4 | ✅ 完成 | 2025-02-18 15:35 | 验证和提交完成 |

---

## 🔄 决策日志

### 2025-02-18: 决定采用渐进式优化策略
**理由**: 避免一次性大规模变更带来的风险
**决策**:
- 先优化工具-VSCode.md
- 再优化清单文件
- 最后考虑其他文档

### 2025-02-18: 确认工具分类标准
**理由**: 按功能分类比按字母序更实用
**分类维度**: 功能类别（Markdown、代码编辑、项目管理等）

---

## 📝 待办事项

- [ ] 完成 Phase 2: 工具-VSCode.md 重构
- [ ] 完成 Phase 3: 清单文件优化
- [ ] 验证所有链接
- [ ] 创建 Git commit

---

## 🔗 相关文件

- `/Users/mac/Documents/Develop/GitRepo/AwesomeTools/Awesome效率神器/开发工具/工具-VSCode.md`
- `/Users/mac/Documents/Develop/GitRepo/AwesomeTools/AwesomeTools清单.md`
- `/Users/mac/Documents/Develop/GitRepo/AwesomeTools/findings.md`
- `/Users/mac/Documents/Develop/GitRepo/AwesomeTools/progress.md`
