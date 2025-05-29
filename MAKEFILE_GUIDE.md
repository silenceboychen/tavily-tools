# Makefile 使用指南

## 🎯 概述

本项目提供了一个功能完整的 Makefile，包含了开发、测试、代码质量检查、构建和部署等所有常用命令。通过 `make` 命令可以快速执行各种开发任务。

## 🚀 快速开始

### 查看所有可用命令
```bash
make help
# 或者直接运行
make
```

### 新用户推荐设置流程
```bash
# 1. 完整项目设置（推荐）
make setup

# 2. 运行测试验证
make test

# 3. 检查代码质量
make quality

# 4. 运行项目
make run
```

## 📦 安装和环境设置

| 命令 | 功能 | 使用场景 |
|------|------|----------|
| `make install` | 安装基础依赖 | 生产环境或简单使用 |
| `make install-dev` | 安装开发依赖 | 开发环境（包含测试、格式化工具等） |
| `make setup-env` | 设置环境变量文件 | 首次配置项目 |
| `make setup` | 完整项目设置 | **新用户推荐**，一键完成所有设置 |

### 详细说明

#### `make setup` - 完整项目设置
这是新用户的推荐命令，会自动执行：
1. 安装所有开发依赖
2. 创建 `.env` 环境变量文件
3. 提供后续步骤指导

```bash
make setup
# 输出示例:
# 🎉 项目设置完成！
# 📝 下一步: 编辑 .env 文件并填入您的 Tavily API 密钥
# 🧪 测试: make test
# 🎯 运行: make run
```

## 🧪 测试相关

| 命令 | 功能 | 适用场景 |
|------|------|----------|
| `make test` | 运行测试套件 | 标准测试 |
| `make test-verbose` | 详细测试输出 | 调试测试问题 |
| `make test-cov` | 测试覆盖率报告 | 代码质量分析 |
| `make test-fast` | 快速测试（跳过慢速测试） | 快速验证 |
| `make test-watch` | 监视文件变化自动测试 | 开发中持续测试 |

### 测试覆盖率
```bash
make test-cov
# 生成 HTML 覆盖率报告：htmlcov/index.html
```

## 🔧 代码质量检查

| 命令 | 功能 | 说明 |
|------|------|------|
| `make format` | 代码格式化 | 自动修复格式问题（black + isort） |
| `make format-check` | 检查代码格式 | 只检查，不修改文件 |
| `make lint` | 静态代码分析 | flake8 代码规范检查 |
| `make mypy` | 类型检查 | mypy 静态类型检查 |
| `make check` | 运行所有静态检查 | lint + mypy |
| `make quality` | 完整代码质量检查 | format-check + lint + mypy |
| `make quality-fix` | 修复代码质量问题 | 自动格式化 + 静态检查 |

### 代码质量工作流
```bash
# 开发中修复代码质量问题
make quality-fix

# 提交前检查（不修改代码）
make quality
```

## 🏗️ 构建和部署

| 命令 | 功能 | 用途 |
|------|------|------|
| `make build` | 构建分发包 | 生成 wheel 和 tar.gz 包 |
| `make build-check` | 构建并检查包 | 验证包的完整性 |
| `make publish-test` | 发布到测试 PyPI | 测试发布流程 |
| `make publish` | 发布到正式 PyPI | 正式发布（需要确认） |

### 发布流程
```bash
# 1. 构建并检查
make build-check

# 2. 测试发布
make publish-test

# 3. 正式发布（需要手动确认）
make publish
```

## 🎯 运行和使用

| 命令 | 功能 | 说明 |
|------|------|------|
| `make run` | 启动交互式CLI | 运行 Tavily Tools |
| `make run-help` | 显示CLI帮助 | 查看命令行选项 |
| `make run-config` | 显示当前配置 | 查看配置信息 |
| `make validate` | 验证环境配置 | 检查API密钥等配置 |
| `make run-example` | 运行使用示例 | 执行示例代码 |
| `make demo` | 运行演示 | 快速演示搜索功能 |

### 运行示例
```bash
# 交互式搜索
make run

# 查看帮助信息
make run-help

# 验证配置
make validate

# 运行演示
make demo
```

## 🧹 清理和维护

| 命令 | 功能 | 清理内容 |
|------|------|----------|
| `make clean` | 清理构建文件 | 构建缓存、临时文件 |
| `make clean-all` | 深度清理 | 包括虚拟环境 |
| `make reset` | 重置项目 | 清理后重新设置 |

## 🤖 CI/CD 和自动化

| 命令 | 功能 | 用途 |
|------|------|------|
| `make ci` | 完整 CI/CD 检查 | 5步完整检查流程 |
| `make pre-commit` | 提交前检查 | 快速检查（格式+静态分析+快速测试） |
| `make all` | 运行所有主要任务 | 质量检查+测试+构建 |

### CI/CD 流程
```bash
# 完整 CI/CD 检查（推荐用于 CI 环境）
make ci
# 执行：格式检查 → 静态分析 → 类型检查 → 测试覆盖率 → 构建检查

# 快速提交前检查
make pre-commit
# 执行：格式检查 → 静态分析 → 快速测试
```

## 🔍 调试和信息

| 命令 | 功能 | 获取信息 |
|------|------|----------|
| `make info` | 显示项目信息 | Python版本、Git信息等 |
| `make deps` | 显示依赖信息 | 已安装的相关包 |
| `make version` | 显示版本信息 | 项目版本号 |

## 📊 使用场景和工作流

### 🆕 新开发者入门
```bash
git clone <repository>
cd tavily-tools
make setup           # 一键设置
# 编辑 .env 文件
make test           # 验证环境
make run            # 开始使用
```

### 👨‍💻 日常开发流程
```bash
# 1. 开发代码
# 2. 自动修复代码质量
make quality-fix

# 3. 运行测试
make test

# 4. 提交前检查
make pre-commit
```

### 🚀 发布流程
```bash
# 1. 完整检查
make ci

# 2. 构建和发布
make build-check
make publish-test    # 可选：先发布到测试环境
make publish         # 正式发布
```

### 🐛 问题排查
```bash
# 查看项目信息
make info

# 查看依赖状态
make deps

# 验证环境
make validate

# 详细测试输出
make test-verbose
```

## ⚡ 效率提升技巧

### 常用组合命令
```bash
# 开发中的完整检查
make quality-fix && make test

# 快速验证
make format && make test-fast

# 完整质量保证
make ci
```

### 文件监视（需要安装 pytest-watch）
```bash
# 自动测试（文件变化时自动运行测试）
make test-watch
```

### 查看构建产物
```bash
make build
ls -la dist/
# 输出：
# tavily_tools-0.1.0-py3-none-any.whl
# tavily_tools-0.1.0.tar.gz
```

## 🎨 自定义和扩展

### 修改 Makefile
Makefile 文件结构清晰，您可以根据需要添加自定义命令：

```makefile
# 添加自定义命令示例
my-custom-task: ## 🔧 我的自定义任务
	@echo "执行自定义任务..."
	# 添加您的命令
```

### 环境变量配置
某些命令支持环境变量配置：
- `PYTHON`: 指定 Python 解释器（默认: python3）
- `PIP`: 指定 pip 命令（默认: pip3）

## 📋 命令速查表

| 分类 | 常用命令 | 快速说明 |
|------|----------|----------|
| **入门** | `make setup` | 新用户完整设置 |
| **开发** | `make quality-fix` | 修复代码质量问题 |
| **测试** | `make test-cov` | 测试覆盖率 |
| **检查** | `make pre-commit` | 提交前快速检查 |
| **构建** | `make build` | 构建分发包 |
| **运行** | `make run` | 启动程序 |
| **清理** | `make clean` | 清理临时文件 |

---

💡 **提示**: 
- 使用 `make help` 查看最新的完整命令列表
- 所有命令都有彩色输出和进度提示
- 支持并行执行多个独立任务
- 错误时会提供详细的诊断信息 