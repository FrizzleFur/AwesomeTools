# AwesomeTools清单重构计划

## 🎯 重构目标

将文档从当前的混乱结构重组为清晰的用户友好结构：

**当前问题**：
- ❌ Resource/Pool 在开头，阻碍用户快速找到工具
- ❌ Graph 独立为二级标题，与平台分类混乱
- ❌ PC/Windows 分散，非主流平台占用显眼位置
- ❌ 缺少"推荐工具"引导新用户
- ❌ Contents 目录无分组，难以导航

## 📐 新结构设计

```markdown
# AwesomeTools清单

## 📥 Inbox

## ⭐ 推荐工具（新增）
### 🖥️ Mac 必备
### 📱 Phone 必备
### 👨‍💻 开发必备

## 📑 Contents（改进）
### 🚀 快速导航
### 💻 平台工具
### 🛠️ 功能专题
### 📚 参考资料

## 💻 Mac 工具（主要平台）
### 🛠️ Mac Helper
### ⚙️ 系统工具
### 🧹 系统清理与优化
### ☁️ Cloud
### 💾 Backup
### ✅ GTD
### 📧 Email
### 💬 IM
### 📝 Writing
### 📊 统计相关
### 🛠️ 效率工具
### 👁️ QuickLook
### 💻 终端工具
### 🔧 开发工具
   - Git 工具
   - Xcode 工具
   - API 测试
   - Linux 工具
   - 开发辅助

## 📱 Phone 手机工具
### ⚡ Productivity
### 📦 JSBox
### 🎤 Siri ShortCut
### 📚 Reading
### 💾 Data
### 🧘 Relax
### 📸 收集创作
### 🔐 VPN

## 🌐 Web 工具
### 🌐 Chrome Extension
### 🌐 WebSite
### 🌐 Web Helper
### 🌐 Productivity
### 🌐 Career
### 🌐 Developing
### 🌐 RSS Tool
### 🌐 entertainment
### 🌐 WallPaper

## 💻 其他平台
### 🖥️ PC 工具
### 🪟 Windows 工具

## 🛠️ 功能专题（跨平台）
### 📊 图表工具
### ✅ GTD（如果需要独立）
### 💪 BodyBuilding
### 🛒 Shopping

## 📚 Resources 参考资料（原 Resource + Pool）
### 📖 学习资源
   - Resource（原内容）
   - RSS Resource
   - pan资源
### 🌐 工具池
   - Pool（原内容）
   - 逆向Pool
   - Tools Pool
   - Tool Guide
   - Tool Shop
   - Pool 资源
### 🔧 开发资源
   - Alfred Workflow Pool
   - Developing（原内容）

## 📖 附录
### 🔧 HardWare 硬件
### 🍎 Apple 专属
```

## 📋 执行步骤

### Phase 1: 备份和准备 ✅
- [x] 读取完整文档
- [x] 创建重构计划

### Phase 2: 创建新文件头（进行中）
- [ ] 添加推荐工具章节
- [ ] 改进 Contents 目录

### Phase 3: 重组 Mac 章节
- [ ] 保持原有内容，调整标题级别

### Phase 4: 重组 Phone 章节
- [ ] 保持原有内容，调整标题级别

### Phase 5: 重组 Web 章节
- [ ] 保持原有内容，调整标题级别

### Phase 6: 合并 PC/Windows
- [ ] 合并为"其他平台"

### Phase 7: 重组 Resources
- [ ] 合并 Resource + Pool
- [ ] 移到文档末尾

### Phase 8: 附录部分
- [ ] HardWare + Apple

### Phase 9: 验证和提交
- [ ] 检查链接
- [ ] Git commit

---

**状态**: 🚧 进行中
**当前步骤**: Phase 2
**开始时间**: 2025-02-18
