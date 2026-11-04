---
title: "Kilobat CLI 使用指南"
category: "网络"
platforms: ["mac"]
tags: ["network", "dns", "cli", "mcp"]
created: "2026-11-01"
updated: "2026-11-01"
---

# Kilobat CLI

## 简介

[Kilobat CLI](https://github.com/seifip/kilobat-cli) 是 macOS 上的开源网络诊断工具，可以从终端检查 DNS、延迟、网络接口和代理路由。它支持 JSON 输出、终端仪表盘以及本地 stdio MCP 服务。

CLI 采用 GPL-3.0-only 许可证；Kilobat 的菜单栏 App 是单独的专有产品。本页介绍公开的 CLI，不把菜单栏 App 列为开源软件。

## 功能特点

- 将连接到某个主机或 API 的检查结果整理为 JSON，便于脚本读取。
- 使用终端仪表盘查看网络状态。
- 通过 `kilobat mcp` 为兼容的 MCP 客户端提供本机网络诊断工具。

## 安装指南

### 系统要求

- macOS 14 或更新版本。
- Homebrew。
- Xcode 16 或更新版本：Homebrew 配方会从源码构建 CLI。

### Mac

```sh
brew install seifip/kilobat/kilobat
```

## 快速开始

先查看可用命令，再检查一个公开主机：

```sh
kilobat --help
kilobat why example.com --json
```

需要终端仪表盘时运行 `kilobat`。需要 MCP 时，让客户端以 stdio 方式启动 `kilobat mcp`；这不是公开的远程 HTTP 服务。

## 使用场景

- 浏览器可以上网，但某个 API 连不上时，检查 DNS、代理路由和连接链路。
- 开发脚本需要结构化网络检查结果。
- 编码代理需要读取当前 Mac 的诊断信息，而不是让用户逐条复制命令输出。

## 使用技巧与限制

- 读取 Wi-Fi 名称需要运行配套 App，并授予定位权限；CLI 不会绕过 macOS 权限限制。
- 诊断会访问目标主机或测量服务，不是离线检测。
- 未测量、跳过或缺失的结果不等于通过；应查看各检查项的状态。
- App 记录的历史及网络过滤依赖相应 App 功能，不能仅凭安装 CLI 就假定它们已启用。

## 相关资源

- [公开 CLI 源码与 README](https://github.com/seifip/kilobat-cli)
- [v0.20.0 已发布源码](https://github.com/seifip/kilobat-cli/tree/v0.20.0)
- [Homebrew 配方](https://github.com/seifip/homebrew-kilobat/blob/main/Formula/kilobat.rb)
