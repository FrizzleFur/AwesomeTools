# 云与 DevOps 工具

## 目录

- [云平台](#云平台)
- [容器化](#容器化)
- [编排工具](#编排工具)
- [基础设施即代码](#基础设施即代码)
- [CI/CD](#cicd)
- [监控与日志](#监控与日志)
- [配置管理](#配置管理)
- [选择指南](#选择指南)
- [学习资源](#学习资源)
- [更新日志](#更新日志)

## 云平台

| 平台 | 描述 | 免费套餐 | 特点 |
|------|------|----------|------|
| [AWS](https://aws.amazon.com/) | 亚马逊云服务 | 12个月免费 | 服务最全面 |
| [Google Cloud](https://cloud.google.com/) | 谷歌云平台 | 300美元信用 | 数据分析和机器学习 |
| [Azure](https://azure.microsoft.com/) | 微软云服务 | 200美元信用 | 企业集成 |
| [Alibaba Cloud](https://www.alibabacloud.com/) | 阿里云 | 免费试用 | 亚洲市场覆盖 |

## 容器化

| 工具 | 描述 | 类型 | 开源 |
|------|------|------|------|
| [Docker](https://www.docker.com/) | 容器平台 | 容器引擎 | 是 |
| [Podman](https://podman.io/) | 无守护进程容器引擎 | 容器引擎 | 是 |
| [Containerd](https://containerd.io/) | 行业标准容器运行时 | 容器运行时 | 是 |
| [Buildah](https://buildah.io/) | 构建 OCI 镜像 | 镜像构建 | 是 |

## 编排工具

| 工具 | 描述 | 云集成 | 开源 |
|------|------|--------|------|
| [Kubernetes](https://kubernetes.io/) | 容器编排 | 多平台 | 是 |
| [Docker Swarm](https://docs.docker.com/engine/swarm/) | Docker 原生编排 | Docker | 是 |
| [Nomad](https://www.nomadproject.io/) | 简单灵活的编排器 | 多平台 | 是 |
| [OpenShift](https://www.redhat.com/en/technologies/cloud-computing/openshift) | 企业级 Kubernetes | 多平台 | 是 |

## 基础设施即代码

| 工具 | 描述 | 语言 | 状态管理 |
|------|------|------|----------|
| [Terraform](https://www.terraform.io/) | 多云基础设施 | HCL | 有状态 |
| [Pulumi](https://www.pulumi.com/) | 使用通用语言 | 多语言 | 有状态 |
| [Ansible](https://www.ansible.com/) | 配置管理 | YAML | 无状态 |
| [Crossplane](https://crossplane.io/) | 云原生控制平面 | YAML | 有状态 |

## CI/CD

| 工具 | 描述 | 自托管 | 云服务 |
|------|------|--------|--------|
| [Jenkins](https://www.jenkins.io/) | 自动化服务器 | 是 | 是 |
| [GitHub Actions](https://github.com/features/actions) | GitHub 原生 CI/CD | 否 | 是 |
| [GitLab CI/CD](https://docs.gitlab.com/ee/ci/) | GitLab 内置 | 是 | 是 |
| [Argo CD](https://argoproj.github.io/cd/) | 声明式 GitOps 工具 | 是 | 是 |

## 监控与日志

| 工具 | 类型 | 开源 | 特点 |
|------|------|------|------|
| [Prometheus](https://prometheus.io/) | 监控 | 是 | 指标收集 |
| [Grafana](https://grafana.com/) | 可视化 | 是 | 仪表板 |
| [ELK Stack](https://www.elastic.co/what-is/elk-stack) | 日志管理 | 是 | 日志分析 |
| [New Relic](https://newrelic.com/) | APM | 否 | 全栈可观测性 |

## 配置管理

| 工具 | 描述 | 语言 | 代理 |
|------|------|------|------|
| [Ansible](https://www.ansible.com/) | 自动化工具 | YAML | 无 |
| [Chef](https://www.chef.io/) | 配置管理 | Ruby | 有 |
| [Puppet](https://puppet.com/) | 自动化交付 | Puppet | 有 |
| [SaltStack](https://www.saltstack.com/) | 事件驱动自动化 | Python | 有 |

## 选择指南

### 初创公司
- **GitHub Actions** - 简单易用的 CI/CD
- **Docker + Kubernetes** - 容器化部署
- **Prometheus + Grafana** - 监控方案

### 企业级
- **OpenShift** - 企业级 K8s
- **Terraform** - 多云基础设施
- **Argo CD** - GitOps 工作流

## 学习资源

### 在线课程
- [Kubernetes 官方教程](https://kubernetes.io/docs/tutorials/)
- [Terraform 学习](https://learn.hashicorp.com/terraform)
- [AWS 培训](https://aws.amazon.com/training/)

### 博客与社区
- [DevOps.com](https://devops.com/)
- [The New Stack](https://thenewstack.io/)
- [Kubernetes Blog](https://kubernetes.io/blog/)

## 更新日志

### 2023-10-18
- 新增云与 DevOps 工具分类文档
- 添加常用云与 DevOps 工具
- 完善文档结构和内容

### 2023-10-01
- 初始版本创建
