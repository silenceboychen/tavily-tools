# Tavily Tools

> 🚀 强大的Tavily搜索结果格式化工具包 - 提供智能搜索和多格式输出功能

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

## 🌟 功能特性

- 🎨 **多种输出格式**: 控制台美化输出、JSON结构化保存、HTML报告生成
- 📊 **搜索质量分析**: 自动分析搜索结果质量和评分分布  
- ⚡ **快速格式化**: 一键完成搜索和格式化操作
- 🔄 **批量处理**: 支持批量搜索和结果处理
- 🎯 **交互式搜索**: 用户友好的交互式界面
- 💾 **智能保存**: 自动生成时间戳文件名和目录管理
- 🛠️ **CLI工具**: 完整的命令行接口支持
- 📚 **搜索历史**: 搜索历史管理和导出功能
- 🌐 **中文优化**: 专门优化的中文界面和输出

## 📁 项目结构

```
tavily-tools/
├── src/tavily_tools/           # 主包目录 (src-layout)
│   ├── __init__.py            # 包初始化和主要导出
│   ├── core/                  # 核心业务逻辑
│   │   ├── __init__.py       
│   │   ├── formatter.py       # 搜索结果格式化器
│   │   └── search.py          # 搜索客户端封装
│   ├── config/                # 配置管理
│   │   ├── __init__.py       
│   │   └── settings.py        # 环境变量和配置管理
│   ├── utils/                 # 工具函数
│   │   ├── __init__.py       
│   │   └── helpers.py         # 通用辅助函数
│   └── cli/                   # 命令行接口
│       ├── __init__.py       
│       └── main.py            # CLI主程序
├── examples/                   # 使用示例
│   ├── __init__.py           
│   └── usage_examples.py      # 详细使用示例
├── tests/                     # 测试套件
│   ├── __init__.py           
│   └── test_formatter.py      # 格式化器测试
├── results/                   # 结果输出目录
├── env.template               # 环境变量模板
├── pyproject.toml             # 项目配置和依赖管理
├── requirements.txt           # 基础依赖（兼容性）
├── README.md                  # 项目文档
├── LICENSE                    # MIT许可证
└── .gitignore                 # Git忽略文件
```

## 🛠️ 安装与配置

### 方式一：开发安装（推荐）

```bash
# 克隆项目
git clone https://github.com/your-org/tavily-tools.git
cd tavily-tools

# 创建虚拟环境
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# 开发模式安装
pip install -e .

# 或安装完整开发依赖
pip install -e ".[dev]"
```

### 方式二：直接安装

```bash
# 安装基础版本
pip install tavily-tools

# 安装完整版本（包含开发工具）
pip install "tavily-tools[dev]"
```

### 配置API密钥

1. **复制环境变量模板**:
```bash
cp env.template .env
```

2. **编辑.env文件**:
```bash
# 必需配置
TAVILY_API_KEY=your_tavily_api_key_here

# 可选配置
DEFAULT_SEARCH_QUERY=deepseek
RESULTS_SAVE_PATH=./results/
MAX_SEARCH_RESULTS=10
```

3. **获取API密钥**:
   - 访问 [Tavily官网](https://tavily.com/)
   - 注册账户并获取API密钥
   - 将密钥填入.env文件

## 🚀 快速开始

### 命令行使用

```bash
# 交互式搜索（推荐）
tavily-tools

# 快速搜索
tavily-tools -q "Python机器学习"

# 批量搜索并保存结果
tavily-tools -b "AI发展" "量子计算" "区块链" --save-json --save-html

# 显示配置信息
tavily-tools --config

# 验证环境配置
tavily-tools --validate-env
```

### Python编程使用

#### 基础使用

```python
from tavily_tools import TavilyFormatter, SearchClient

# 创建搜索客户端
client = SearchClient()

# 执行搜索
response = client.search("人工智能最新发展")

# 格式化输出
formatter = TavilyFormatter(response)
formatter.print_full()

# 保存结果
formatter.save_json()
formatter.save_html()
```

#### 高级功能

```python
from tavily_tools import quick_format, batch_search, interactive_search

# 快速格式化（一键完成）
quick_format(
    response, 
    save_json=True, 
    save_html=True, 
    print_output=True
)

# 批量搜索
topics = ["机器学习", "深度学习", "神经网络"]
formatters = batch_search(topics, save_json=True)

# 交互式搜索
interactive_search()
```

#### 搜索质量分析

```python
# 详细质量分析
quality = formatter.analyze_quality()
print(f"平均评分: {quality['平均评分']:.3f}")
print(f"高质量结果: {quality['评分分布']['高质量(>0.7)']}条")

# 搜索历史管理
client = SearchClient()
client.search("查询1")
client.search("查询2")

# 查看搜索历史
history = client.get_search_history()
for item in history:
    print(f"{item['query']}: {item['results_count']}条结果")

# 导出搜索历史
client.export_history("my_search_history.json")
```

## 📚 详细文档

### 核心类和函数

#### TavilyFormatter

搜索结果格式化器，提供多种输出格式。

```python
formatter = TavilyFormatter(response, save_path="./results/")

# 打印方法
formatter.print_summary()      # 打印搜索摘要
formatter.print_results()      # 打印搜索结果
formatter.print_full()         # 打印完整信息

# 数据转换
data = formatter.to_dict()     # 转换为结构化字典

# 文件输出
formatter.save_json()          # 保存为JSON文件
formatter.save_html()          # 生成HTML报告

# 质量分析
quality = formatter.analyze_quality()
```

#### SearchClient

搜索客户端封装，提供统一的搜索接口。

```python
client = SearchClient(api_key="your_key")  # 可选，默认从配置读取

# 基础搜索
response = client.search("查询关键词")

# 搜索并格式化
formatter = client.search_and_format(
    query="查询关键词",
    save_json=True,
    save_html=True
)

# 搜索历史管理
history = client.get_search_history()
client.export_history("history.json")
client.clear_history()
```

#### 配置管理

```python
from tavily_tools.config import get_config, get_tavily_client

# 获取配置
config = get_config()
config.show_config()

# 获取预配置的客户端
client = get_tavily_client()
```

### 命令行选项

```bash
# 基本操作
tavily-tools -q "查询"                    # 单次搜索
tavily-tools -b "查询1" "查询2"           # 批量搜索
tavily-tools -i                          # 交互式模式

# 输出选项
tavily-tools -q "查询" --save-json        # 保存JSON
tavily-tools -q "查询" --save-html        # 生成HTML报告
tavily-tools -q "查询" --no-print         # 不打印到控制台

# 配置和信息
tavily-tools --config                    # 显示配置
tavily-tools --validate-env              # 验证环境
tavily-tools --version                   # 显示版本

# 调试选项
tavily-tools -q "查询" --verbose          # 详细输出
tavily-tools -q "查询" --quiet            # 安静模式
```

## 🔧 开发指南

### 环境设置

```bash
# 克隆项目
git clone https://github.com/your-org/tavily-tools.git
cd tavily-tools

# 安装开发依赖
pip install -e ".[dev]"

# 安装pre-commit钩子
pre-commit install
```

### 代码质量工具

```bash
# 代码格式化
black src/ tests/ examples/
isort src/ tests/ examples/

# 静态检查
flake8 src/ tests/ examples/
mypy src/

# 运行测试
pytest tests/ --cov=src/tavily_tools
```

### 构建和发布

```bash
# 构建包
python -m build

# 本地安装测试
pip install dist/tavily_tools-0.1.0-py3-none-any.whl

# 发布到PyPI（需要配置token）
twine upload dist/*
```

## 📊 使用示例

### 示例1：基础搜索和格式化

```python
from tavily_tools import SearchClient, TavilyFormatter

# 执行搜索
client = SearchClient()
response = client.search("Python机器学习库推荐")

# 创建格式化器
formatter = TavilyFormatter(response)

# 显示搜索摘要
formatter.print_summary()
# 输出：
# ============================================================
# 🔍 查询: Python机器学习库推荐
# ⏱️  用时: 1.234秒
# 📊 结果: 10条
# ============================================================

# 保存结果
json_file = formatter.save_json()
html_file = formatter.save_html()
```

### 示例2：批量搜索和质量分析

```python
from tavily_tools import batch_search

# 定义搜索主题
topics = [
    "人工智能最新突破",
    "量子计算发展现状", 
    "区块链技术应用"
]

# 批量搜索
formatters = batch_search(
    topics=topics,
    save_json=True,
    save_html=False,
    print_progress=True
)

# 分析结果质量
for i, formatter in enumerate(formatters):
    quality = formatter.analyze_quality()
    print(f"{topics[i]}:")
    print(f"  结果数: {quality['结果总数']}")
    print(f"  平均评分: {quality['平均评分']:.3f}")
    print(f"  高质量结果: {quality['评分分布']['高质量(>0.7)']}条")
```

### 示例3：自定义配置和高级功能

```python
from tavily_tools import SearchClient, TavilyFormatter
from tavily_tools.config import get_config

# 显示当前配置
config = get_config()
config.show_config()

# 创建客户端并执行多次搜索
client = SearchClient()

queries = ["深度学习", "计算机视觉", "自然语言处理"]
for query in queries:
    print(f"\n🔍 搜索: {query}")
    
    # 执行搜索
    response = client.search(query)
    
    # 快速分析
    formatter = TavilyFormatter(response)
    quality = formatter.analyze_quality()
    
    print(f"✅ 完成 | 结果: {quality['结果总数']}条 | 评分: {quality['平均评分']:.3f}")

# 查看搜索历史
print("\n📚 搜索历史:")
history = client.get_search_history()
for i, item in enumerate(history, 1):
    print(f"  {i}. {item['query']} - {item['results_count']}条结果")

# 导出历史
history_file = client.export_history()
print(f"\n📁 搜索历史已导出: {history_file}")
```

## 🤝 贡献指南

我们欢迎任何形式的贡献！请查看以下指南：

1. **Fork** 项目
2. 创建功能分支: `git checkout -b feature/amazing-feature`
3. 提交更改: `git commit -m 'Add amazing feature'`
4. 推送分支: `git push origin feature/amazing-feature`
5. 开启 **Pull Request**

### 贡献类型

- 🐛 Bug修复
- ✨ 新功能开发
- 📚 文档改进
- 🎨 界面优化
- ⚡ 性能优化
- 🧪 测试覆盖

## 📝 更新日志

### [0.1.0] - 2024-12-03

#### 新增
- 🎉 初始版本发布
- 🔍 完整的搜索功能封装
- 🎨 多格式输出支持（控制台、JSON、HTML）
- 📊 搜索质量分析功能
- 🛠️ 完整的CLI工具
- 📚 批量搜索和搜索历史管理
- 🧪 完善的测试套件
- 📖 详细的文档和示例

## 🆘 问题排查

### 常见问题

**Q: 报错"未找到TAVILY_API_KEY环境变量"**
```bash
# 解决方案：
1. 复制环境变量模板：cp env.template .env
2. 编辑.env文件，填入真实的API密钥
3. 确保.env文件在项目根目录
```

**Q: 模块导入错误**
```bash
# 解决方案：
1. 确保已安装项目：pip install -e .
2. 检查Python路径：python -c "import tavily_tools; print('OK')"
3. 激活正确的虚拟环境
```

**Q: 搜索结果为空**
```bash
# 解决方案：
1. 检查网络连接
2. 验证API密钥有效性：tavily-tools --validate-env
3. 尝试简化搜索查询
```

### 调试模式

```bash
# 启用详细输出
tavily-tools -q "查询" --verbose

# 查看配置信息
tavily-tools --config --verbose

# 验证环境
tavily-tools --validate-env
```

## 📄 许可证

本项目基于 [MIT许可证](LICENSE) 开源。

## 🔗 相关链接

- [Tavily官网](https://tavily.com/) - 获取API密钥
- [项目主页](https://github.com/your-org/tavily-tools)
- [问题反馈](https://github.com/your-org/tavily-tools/issues)
- [文档站点](https://tavily-tools.readthedocs.io)

## 💡 致谢

感谢以下项目和技术：

- [Tavily](https://tavily.com/) - 提供强大的AI搜索API
- [Python](https://python.org) - 优秀的编程语言
- [Click](https://click.palletsprojects.com/) - 命令行界面框架
- [Rich](https://rich.readthedocs.io/) - 终端美化库（计划集成）

---

<div align="center">

**⭐ 如果这个项目对您有帮助，请给我们一个Star！ ⭐**

Made with ❤️ by AI工具链研发团队

</div> 