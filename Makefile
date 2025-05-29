# =================================================================
# Tavily Tools - Makefile
# 提供开发、测试、代码质量检查等常用命令的快速执行脚本
# =================================================================

.PHONY: help install install-dev clean test test-verbose test-cov
.PHONY: format check lint mypy quality pre-commit
.PHONY: build publish build-check docs serve-docs
.PHONY: run run-interactive validate setup-env
.PHONY: all ci

# 默认目标
.DEFAULT_GOAL := help

# 颜色定义
RED := \033[31m
GREEN := \033[32m
YELLOW := \033[33m
BLUE := \033[34m
MAGENTA := \033[35m
CYAN := \033[36m
WHITE := \033[37m
RESET := \033[0m

# 项目信息
PROJECT_NAME := tavily-tools
PYTHON := python3
PIP := pip3
SRC_DIR := src
TEST_DIR := tests
EXAMPLES_DIR := examples

# =================================================================
# 帮助信息
# =================================================================

help: ## 📚 显示所有可用命令
	@echo "$(CYAN)$(PROJECT_NAME) - Makefile 命令$(RESET)"
	@echo "$(CYAN)================================$(RESET)"
	@echo ""
	@echo "$(YELLOW)🚀 快速开始:$(RESET)"
	@echo "  $(GREEN)make setup$(RESET)          - 完整项目设置（推荐新用户）"
	@echo "  $(GREEN)make install-dev$(RESET)     - 安装开发依赖"
	@echo "  $(GREEN)make test$(RESET)            - 运行测试套件"
	@echo "  $(GREEN)make quality$(RESET)         - 运行所有代码质量检查"
	@echo ""
	@echo "$(YELLOW)📦 安装和环境:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## .*📦/ {printf "  $(GREEN)%-16s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)🧪 测试相关:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## .*🧪/ {printf "  $(GREEN)%-16s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)🔧 代码质量:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## .*🔧/ {printf "  $(GREEN)%-16s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)🏗️  构建和部署:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## .*🏗️/ {printf "  $(GREEN)%-16s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)🎯 运行和使用:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## .*🎯/ {printf "  $(GREEN)%-16s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(YELLOW)🧹 清理和维护:$(RESET)"
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## .*🧹/ {printf "  $(GREEN)%-16s$(RESET) %s\n", $$1, $$2}' $(MAKEFILE_LIST)
	@echo ""
	@echo "$(BLUE)💡 提示: 使用 'make <命令>' 来执行对应操作$(RESET)"

# =================================================================
# 安装和环境设置
# =================================================================

install: ## 📦 安装基础依赖
	@echo "$(YELLOW)📦 安装基础依赖...$(RESET)"
	$(PIP) install -e .
	@echo "$(GREEN)✅ 基础依赖安装完成$(RESET)"

install-dev: ## 📦 安装开发依赖（包含测试、格式化等工具）
	@echo "$(YELLOW)📦 安装开发依赖...$(RESET)"
	$(PIP) install -e ".[dev]"
	@echo "$(GREEN)✅ 开发依赖安装完成$(RESET)"

setup-env: ## 📦 设置环境变量文件
	@echo "$(YELLOW)📦 设置环境变量...$(RESET)"
	@if [ ! -f .env ]; then \
		cp env.template .env; \
		echo "$(GREEN)✅ 已创建 .env 文件，请编辑并填入您的 API 密钥$(RESET)"; \
		echo "$(CYAN)📝 编辑命令: nano .env$(RESET)"; \
	else \
		echo "$(BLUE)ℹ️  .env 文件已存在$(RESET)"; \
	fi

setup: install-dev setup-env ## 📦 完整项目设置（新用户推荐）
	@echo "$(GREEN)🎉 项目设置完成！$(RESET)"
	@echo "$(CYAN)📝 下一步: 编辑 .env 文件并填入您的 Tavily API 密钥$(RESET)"
	@echo "$(CYAN)🧪 测试: make test$(RESET)"
	@echo "$(CYAN)🎯 运行: make run$(RESET)"

# =================================================================
# 测试相关
# =================================================================

test: ## 🧪 运行测试套件
	@echo "$(YELLOW)🧪 运行测试套件...$(RESET)"
	$(PYTHON) -m pytest $(TEST_DIR)/ -v
	@echo "$(GREEN)✅ 测试完成$(RESET)"

test-verbose: ## 🧪 运行详细测试（显示更多信息）
	@echo "$(YELLOW)🧪 运行详细测试...$(RESET)"
	$(PYTHON) -m pytest $(TEST_DIR)/ -v -s --tb=long
	@echo "$(GREEN)✅ 详细测试完成$(RESET)"

test-cov: ## 🧪 运行测试并生成覆盖率报告
	@echo "$(YELLOW)🧪 运行测试覆盖率分析...$(RESET)"
	$(PYTHON) -m pytest $(TEST_DIR)/ --cov=$(SRC_DIR)/tavily_tools --cov-report=term-missing --cov-report=html:htmlcov
	@echo "$(GREEN)✅ 测试覆盖率报告生成完成$(RESET)"
	@echo "$(CYAN)📊 HTML报告: htmlcov/index.html$(RESET)"

test-fast: ## 🧪 快速测试（跳过慢速测试）
	@echo "$(YELLOW)🧪 运行快速测试...$(RESET)"
	$(PYTHON) -m pytest $(TEST_DIR)/ -v -m "not slow"
	@echo "$(GREEN)✅ 快速测试完成$(RESET)"

test-watch: ## 🧪 监视文件变化并自动运行测试
	@echo "$(YELLOW)🧪 启动测试监视模式...$(RESET)"
	$(PYTHON) -m pytest-watch $(TEST_DIR)/ --clear

# =================================================================
# 代码质量检查
# =================================================================

format: ## 🔧 代码格式化（black + isort）
	@echo "$(YELLOW)🔧 格式化代码...$(RESET)"
	@echo "$(CYAN)📝 Black 格式化...$(RESET)"
	$(PYTHON) -m black $(SRC_DIR)/ $(TEST_DIR)/ $(EXAMPLES_DIR)/
	@echo "$(CYAN)📝 isort 导入排序...$(RESET)"
	$(PYTHON) -m isort $(SRC_DIR)/ $(TEST_DIR)/ $(EXAMPLES_DIR)/
	@echo "$(GREEN)✅ 代码格式化完成$(RESET)"

format-check: ## 🔧 检查代码格式（不修改文件）
	@echo "$(YELLOW)🔧 检查代码格式...$(RESET)"
	$(PYTHON) -m black --check $(SRC_DIR)/ $(TEST_DIR)/ $(EXAMPLES_DIR)/
	$(PYTHON) -m isort --check-only $(SRC_DIR)/ $(TEST_DIR)/ $(EXAMPLES_DIR)/
	@echo "$(GREEN)✅ 代码格式检查完成$(RESET)"

lint: ## 🔧 代码静态分析（flake8）
	@echo "$(YELLOW)🔧 运行 flake8 静态分析...$(RESET)"
	$(PYTHON) -m flake8 $(SRC_DIR)/ $(TEST_DIR)/ $(EXAMPLES_DIR)/
	@echo "$(GREEN)✅ 静态分析完成$(RESET)"

mypy: ## 🔧 类型检查（mypy）
	@echo "$(YELLOW)🔧 运行 mypy 类型检查...$(RESET)"
	$(PYTHON) -m mypy $(SRC_DIR)/tavily_tools/
	@echo "$(GREEN)✅ 类型检查完成$(RESET)"

check: lint mypy ## 🔧 运行所有静态检查（不包含格式化）
	@echo "$(GREEN)✅ 所有静态检查完成$(RESET)"

quality: format-check lint mypy ## 🔧 运行所有代码质量检查
	@echo "$(GREEN)🎉 所有代码质量检查通过！$(RESET)"

quality-fix: format lint mypy ## 🔧 修复代码质量问题（自动格式化）
	@echo "$(GREEN)🎉 代码质量问题修复完成！$(RESET)"

# =================================================================
# 构建和部署
# =================================================================

build: clean ## 🏗️ 构建分发包
	@echo "$(YELLOW)🏗️ 构建分发包...$(RESET)"
	$(PYTHON) -m build
	@echo "$(GREEN)✅ 构建完成$(RESET)"
	@echo "$(CYAN)📦 输出目录: dist/$(RESET)"

build-check: build ## 🏗️ 构建并检查包
	@echo "$(YELLOW)🏗️ 检查构建包...$(RESET)"
	$(PYTHON) -m twine check dist/*
	@echo "$(GREEN)✅ 包检查完成$(RESET)"

publish-test: build-check ## 🏗️ 发布到测试PyPI
	@echo "$(YELLOW)🏗️ 发布到测试PyPI...$(RESET)"
	$(PYTHON) -m twine upload --repository testpypi dist/*
	@echo "$(GREEN)✅ 测试发布完成$(RESET)"

publish: build-check ## 🏗️ 发布到正式PyPI
	@echo "$(RED)⚠️  准备发布到正式PyPI，请确认版本号正确！$(RESET)"
	@read -p "确认发布？(y/N): " confirm && [ "$$confirm" = "y" ]
	$(PYTHON) -m twine upload dist/*
	@echo "$(GREEN)🎉 正式发布完成$(RESET)"

# =================================================================
# 运行和使用
# =================================================================

run: ## 🎯 运行CLI工具（交互模式）
	@echo "$(YELLOW)🎯 启动 Tavily Tools...$(RESET)"
	$(PYTHON) -m $(SRC_DIR).tavily_tools.cli.main

run-help: ## 🎯 显示CLI帮助信息
	@echo "$(YELLOW)🎯 CLI 帮助信息:$(RESET)"
	$(PYTHON) -m $(SRC_DIR).tavily_tools.cli.main --help

run-config: ## 🎯 显示当前配置
	@echo "$(YELLOW)🎯 当前配置:$(RESET)"
	$(PYTHON) -m $(SRC_DIR).tavily_tools.cli.main --config

validate: ## 🎯 验证环境配置
	@echo "$(YELLOW)🎯 验证环境配置...$(RESET)"
	$(PYTHON) -m $(SRC_DIR).tavily_tools.cli.main --validate-env
	@echo "$(GREEN)✅ 环境验证完成$(RESET)"

run-example: ## 🎯 运行使用示例
	@echo "$(YELLOW)🎯 运行使用示例...$(RESET)"
	$(PYTHON) $(EXAMPLES_DIR)/usage_examples.py

# =================================================================
# 文档相关
# =================================================================

docs: ## 📚 生成文档（如果配置了Sphinx）
	@echo "$(YELLOW)📚 生成文档...$(RESET)"
	@if [ -d "docs" ]; then \
		cd docs && make html; \
		echo "$(GREEN)✅ 文档生成完成$(RESET)"; \
	else \
		echo "$(BLUE)ℹ️  docs目录不存在，跳过文档生成$(RESET)"; \
	fi

serve-docs: docs ## 📚 启动文档服务器
	@echo "$(YELLOW)📚 启动文档服务器...$(RESET)"
	@if [ -d "docs/_build/html" ]; then \
		cd docs/_build/html && $(PYTHON) -m http.server 8000; \
	else \
		echo "$(RED)❌ 未找到文档，请先运行 make docs$(RESET)"; \
	fi

# =================================================================
# 清理和维护
# =================================================================

clean: ## 🧹 清理构建文件和缓存
	@echo "$(YELLOW)🧹 清理构建文件...$(RESET)"
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info/
	rm -rf .pytest_cache/
	rm -rf htmlcov/
	rm -rf .coverage
	rm -rf .mypy_cache/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	@echo "$(GREEN)✅ 清理完成$(RESET)"

clean-all: clean ## 🧹 深度清理（包括虚拟环境相关）
	@echo "$(YELLOW)🧹 深度清理...$(RESET)"
	rm -rf .venv/
	rm -rf .tox/
	rm -rf .coverage.*
	@echo "$(GREEN)✅ 深度清理完成$(RESET)"

reset: clean-all setup ## 🧹 重置项目（清理后重新设置）
	@echo "$(GREEN)🎉 项目重置完成$(RESET)"

# =================================================================
# CI/CD 相关
# =================================================================

ci: ## 🤖 CI/CD 完整检查流程
	@echo "$(YELLOW)🤖 开始 CI/CD 检查流程...$(RESET)"
	@echo "$(CYAN)1/5 代码格式检查...$(RESET)"
	@$(MAKE) format-check
	@echo "$(CYAN)2/5 静态分析...$(RESET)"
	@$(MAKE) lint
	@echo "$(CYAN)3/5 类型检查...$(RESET)"
	@$(MAKE) mypy
	@echo "$(CYAN)4/5 运行测试...$(RESET)"
	@$(MAKE) test-cov
	@echo "$(CYAN)5/5 构建检查...$(RESET)"
	@$(MAKE) build-check
	@echo "$(GREEN)🎉 CI/CD 检查全部通过！$(RESET)"

pre-commit: ## 🤖 提交前检查（快速版本）
	@echo "$(YELLOW)🤖 提交前检查...$(RESET)"
	@$(MAKE) format-check
	@$(MAKE) lint
	@$(MAKE) test-fast
	@echo "$(GREEN)✅ 提交前检查通过$(RESET)"

all: quality test build ## 🤖 运行所有主要任务
	@echo "$(GREEN)🎉 所有任务完成！$(RESET)"

# =================================================================
# 调试和开发辅助
# =================================================================

info: ## 🔍 显示项目信息
	@echo "$(CYAN)项目信息:$(RESET)"
	@echo "  名称: $(PROJECT_NAME)"
	@echo "  Python: $(shell $(PYTHON) --version)"
	@echo "  Pip: $(shell $(PIP) --version)"
	@echo "  工作目录: $(shell pwd)"
	@echo "  源码目录: $(SRC_DIR)"
	@echo "  测试目录: $(TEST_DIR)"
	@echo ""
	@echo "$(CYAN)Git 信息:$(RESET)"
	@git branch --show-current 2>/dev/null || echo "  未初始化 Git 仓库"
	@git log --oneline -5 2>/dev/null || echo "  无提交历史"

deps: ## 🔍 显示依赖信息
	@echo "$(CYAN)已安装包:$(RESET)"
	$(PIP) list | grep -E "(tavily|black|pytest|mypy|flake8|isort)"

version: ## 🔍 显示版本信息
	@echo "$(CYAN)版本信息:$(RESET)"
	@$(PYTHON) -c "import sys; sys.path.insert(0, '$(SRC_DIR)'); import tavily_tools; print(f'tavily-tools: {tavily_tools.__version__}')" 2>/dev/null || echo "tavily-tools: 未安装"

# =================================================================
# 自定义目标示例
# =================================================================

demo: ## 🎭 运行演示（示例搜索）
	@echo "$(YELLOW)🎭 运行演示...$(RESET)"
	@echo "$(CYAN)执行示例搜索: 'Python机器学习'$(RESET)"
	$(PYTHON) -m $(SRC_DIR).tavily_tools.cli.main -q "Python机器学习" --save-json
	@echo "$(GREEN)✅ 演示完成，结果已保存$(RESET)"

benchmark: ## 📊 运行性能基准测试
	@echo "$(YELLOW)📊 运行性能基准测试...$(RESET)"
	@echo "$(BLUE)注意: 这是一个示例命令，需要实现具体的基准测试$(RESET)"
	# 这里可以添加具体的性能测试代码
	@echo "$(GREEN)✅ 基准测试完成$(RESET)" 