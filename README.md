# Tavily搜索结果格式化工具

一个功能强大的Tavily搜索结果格式化和分析工具，提供多种输出格式和质量分析功能。

## 🚀 功能特性

- **🎨 多种输出格式**: 支持控制台输出、JSON、HTML报告
- **📊 质量分析**: 自动分析搜索结果质量和评分分布
- **⚡ 快速格式化**: 一键完成所有格式化操作
- **🔄 批量处理**: 支持批量搜索和结果处理
- **🎯 自定义显示**: 灵活的结果筛选和显示选项
- **💾 智能保存**: 自动生成时间戳文件名
- **🌐 国际化**: 支持中文界面和输出

## 📁 文件结构

```
tavily/
├── tavily_search.py         # 增强版主程序，支持交互式操作
├── tavily_formatter.py     # 核心格式化工具类
├── example_usage.py        # 详细使用示例
├── config.py               # 配置管理模块（环境变量）
├── env_template.txt        # 环境变量模板文件
├── requirements.txt        # 依赖管理（传统方式）
├── README.md              # 项目文档
├── LICENSE                # MIT许可证
└── .gitignore             # Git忽略文件
```

## 🛠️ 安装与配置

### 1. 环境管理（推荐使用uv）

#### 方法一：使用uv（推荐）

[uv](https://github.com/astral-sh/uv) 是一个极速的Python包管理器，比pip快10-100倍。

```bash
# 安装uv（如果尚未安装）
curl -LsSf https://astral.sh/uv/install.sh | sh

# 或者使用pip安装
pip install uv

# 使用uv初始化项目（创建虚拟环境）
uv venv --python=3.12.4

# 激活虚拟环境
# Linux/macOS:
source .venv/bin/activate
# Windows:
.venv\Scripts\activate

# 安装项目依赖
uv pip install -r requirements.txt
```

#### 方法二：使用传统pip + venv

```bash
# 创建虚拟环境
python -m venv venv

# 激活虚拟环境
# Linux/macOS:
source venv/bin/activate
# Windows:
venv\Scripts\activate

# 安装依赖
pip install -r requirements.txt
```

### 2. 配置API密钥

#### 方法一：使用.env文件（推荐）

1. 复制环境变量模板：
```bash
cp env_template.txt .env
```

2. 编辑.env文件，填入您的真实API密钥：
```bash
# 编辑.env文件
TAVILY_API_KEY=your_actual_api_key_here
DEFAULT_SEARCH_QUERY=deepseek
```

#### 方法二：直接设置环境变量

```bash
# Linux/macOS
export TAVILY_API_KEY="your_actual_api_key_here"

# Windows
set TAVILY_API_KEY=your_actual_api_key_here
```

### 3. 获取API密钥

1. 访问 [Tavily官网](https://tavily.com/)
2. 注册账户并登录
3. 在控制台获取您的API密钥
4. 将密钥添加到.env文件中

## 📖 快速开始

### 方法一：使用uv（推荐）

```bash
# 使用uv安装并运行
uv run tavily_search.py

# 运行示例
uv run python example_usage.py
```

### 方法二：传统方式

```bash
# 激活虚拟环境后运行主程序
python3 tavily_search.py
```

### 基础使用

```python
# 方法一：使用配置管理模块（推荐）
from config import get_tavily_client
from tavily_formatter import TavilyFormatter

# 自动加载环境变量并初始化客户端
client = get_tavily_client()

# 执行搜索
response = client.search(query="人工智能发展趋势")

# 格式化输出
formatter = TavilyFormatter().load_response(response)
formatter.print_full()
```

```python
# 方法二：手动使用环境变量
import os
from dotenv import load_dotenv
from tavily import TavilyClient
from tavily_formatter import TavilyFormatter

# 加载环境变量
load_dotenv()

# 初始化客户端
client = TavilyClient(os.getenv('TAVILY_API_KEY'))

# 执行搜索和格式化
response = client.search(query="人工智能发展趋势")
formatter = TavilyFormatter().load_response(response)
formatter.print_full()
```

### 一键格式化

```python
from tavily_formatter import quick_format

# 一键格式化并保存所有格式
formatter = quick_format(
    response, 
    save_json=True, 
    save_html=True
)
```

## 🔧 API 参考

### TavilyFormatter 类

#### 核心方法

| 方法 | 描述 | 参数 | 返回值 |
|------|------|------|--------|
| `load_response(response)` | 加载搜索响应数据 | `response`: Tavily搜索响应 | `TavilyFormatter`: 支持链式调用 |
| `print_summary()` | 打印搜索摘要信息 | 无 | `None` |
| `print_results(max_content_length)` | 打印搜索结果 | `max_content_length`: 内容摘要最大长度 | `None` |
| `print_full(max_content_length)` | 打印完整格式化结果 | `max_content_length`: 内容摘要最大长度 | `None` |

#### 数据转换方法

| 方法 | 描述 | 参数 | 返回值 |
|------|------|------|--------|
| `to_dict()` | 转换为结构化字典 | 无 | `Dict`: 格式化后的字典数据 |
| `to_json(filename, formatted)` | 保存为JSON文件 | `filename`: 文件名<br>`formatted`: 是否使用格式化数据 | `str`: 保存的文件名 |
| `to_html(filename, title)` | 生成HTML报告 | `filename`: 文件名<br>`title`: 报告标题 | `str`: 保存的文件名 |

#### 分析方法

| 方法 | 描述 | 参数 | 返回值 |
|------|------|------|--------|
| `analyze_quality()` | 分析搜索结果质量 | 无 | `Dict`: 质量分析报告 |

### 便捷函数

| 函数 | 描述 | 参数 | 返回值 |
|------|------|------|--------|
| `quick_format(response, save_json, save_html)` | 快速格式化搜索结果 | `response`: 搜索响应<br>`save_json`: 是否保存JSON<br>`save_html`: 是否保存HTML | `TavilyFormatter`: 格式化器实例 |

## 📊 输出格式示例

### 1. 控制台输出

```
================================================================================
🔍 搜索查询: deepseek
⏱️  响应时间: 1.77 秒
📊 结果数量: 5
================================================================================

📄 结果 1:
   标题: DeepSeek explained: Everything you need to know - TechTarget
   链接: https://www.techtarget.com/WhatIs/feature/DeepSeek-explained-Everything-you-need-to-know
   评分: 0.8875
   摘要: What is DeepSeek? DeepSeek DeepSeek, a Chinese AI firm, is disrupting the industry with its low-cost, open source large language models...
----------------------------------------

📈 搜索质量分析:
   结果总数: 5
   平均评分: 0.691
   高质量结果: 2条
   中等质量结果: 3条
   低质量结果: 0条
```

### 2. JSON输出格式

```json
{
  "搜索信息": {
    "查询": "deepseek",
    "响应时间": 1.77,
    "结果数量": 5
  },
  "AI答案": null,
  "搜索结果": [
    {
      "序号": 1,
      "标题": "DeepSeek explained: Everything you need to know",
      "链接": "https://www.techtarget.com/...",
      "评分": 0.8875,
      "内容摘要": "What is DeepSeek? DeepSeek..."
    }
  ],
  "跟进问题": []
}
```

### 3. HTML报告

生成美观的HTML报告，包含：
- 响应式设计，支持移动端
- 搜索摘要信息面板
- 结构化的搜索结果展示
- 可点击的链接
- 时间戳和质量评估

## 💡 使用场景

### 1. 研究和分析
```python
# 学术研究场景
response = client.search(query="机器学习最新论文 2024")
formatter = TavilyFormatter().load_response(response)

# 只显示高质量结果
quality = formatter.analyze_quality()
print(f"高质量结果: {quality['评分分布']['高质量(>0.7)']}条")

# 生成研究报告
formatter.to_html(title="机器学习研究报告")
```

### 2. 内容整理
```python
# 批量搜索不同主题
topics = ["AI安全", "自动驾驶", "量子计算"]

for topic in topics:
    response = client.search(query=topic)
    formatter = TavilyFormatter().load_response(response)
    formatter.to_json(filename=f"research_{topic}.json")
```

### 3. 质量监控
```python
# 搜索质量监控
response = client.search(query="某个查询")
quality = TavilyFormatter().load_response(response).analyze_quality()

if quality['平均评分'] < 0.5:
    print("⚠️ 搜索质量较低，建议调整查询词")
```

## ⚙️ 配置选项

### 内容长度控制
```python
# 控制内容摘要长度
formatter.print_results(max_content_length=200)  # 默认150字符
```

### 文件命名自定义
```python
# 自定义文件名
formatter.to_json(filename="custom_search_results.json")
formatter.to_html(filename="report.html", title="自定义标题")
```

### 质量分析阈值
```python
# 质量分析基于以下阈值:
# - 高质量: score > 0.7
# - 中等质量: 0.4 <= score <= 0.7  
# - 低质量: score < 0.4
```

## 🔍 高级功能

### 1. uv高级用法

```bash
# 开发模式安装（包含开发依赖）
uv sync --dev

# 添加新的依赖
uv add requests beautifulsoup4

# 添加开发依赖
uv add --dev pytest black

# 创建生产环境的锁定文件
uv lock

# 使用特定Python版本
uv venv --python 3.11

# 运行脚本（无需激活虚拟环境）
uv run python tavily_search.py

# 运行测试（如果有）
uv run pytest

# 代码格式化
uv run black .

# 类型检查
uv run mypy .
```

### 2. 自定义结果筛选
```python
# 筛选高质量结果
results = response.get('results', [])
high_quality = [r for r in results if r.get('score', 0) > 0.8]

# 按评分排序
sorted_results = sorted(results, key=lambda x: x.get('score', 0), reverse=True)
```

### 3. 批量质量分析
```python
# 批量分析多个搜索的质量
def analyze_multiple_searches(queries):
    quality_reports = []
    for query in queries:
        response = client.search(query=query)
        quality = TavilyFormatter().load_response(response).analyze_quality()
        quality_reports.append({
            'query': query,
            'quality': quality
        })
    return quality_reports
```

### 4. 结果去重
```python
# 基于URL去重
def deduplicate_results(response):
    seen_urls = set()
    unique_results = []
    
    for result in response.get('results', []):
        url = result.get('url', '')
        if url not in seen_urls:
            seen_urls.add(url)
            unique_results.append(result)
    
    response['results'] = unique_results
    return response
```

## 🐛 错误处理

工具内置了完善的错误处理机制：

```python
try:
    formatter = TavilyFormatter().load_response(response)
    formatter.print_full()
except Exception as e:
    print(f"❌ 格式化出错: {e}")
    # 程序会继续运行，不会崩溃
```

常见错误和解决方案：

| 错误类型 | 原因 | 解决方案 |
|----------|------|----------|
| `❌ 没有搜索数据` | 未加载response数据 | 先调用`load_response()` |
| `❌ 保存失败` | 文件权限或路径问题 | 检查文件路径和权限 |
| `❌ API调用失败` | 网络或API key问题 | 检查网络连接和API key |

## 📈 性能优化

### 1. 大量结果处理
```python
# 对于大量搜索结果，建议分页处理
formatter.print_results(max_content_length=100)  # 减少内容长度
```

### 2. 内存使用优化
```python
# 处理完成后释放内存
formatter.response = None
```

### 3. 文件大小控制
```python
# 生成压缩的JSON
import json
data = formatter.to_dict()
with open('compressed.json', 'w') as f:
    json.dump(data, f, separators=(',', ':'))  # 去除空格
```

## 📄 许可证

本项目采用 MIT 许可证 - 查看 [LICENSE](LICENSE) 文件了解详情。

---

**🎯 让搜索结果更清晰，让信息处理更高效！** 