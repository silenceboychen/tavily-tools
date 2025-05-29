"""
Tavily搜索结果格式化工具
提供多种格式化输出选项，包括控制台输出、JSON保存、HTML报告等
"""

import json
import html
import os
from datetime import datetime
from pathlib import Path
from typing import Dict, List, Optional, Any


class TavilyFormatter:
    """Tavily搜索结果格式化器"""
    
    def __init__(self, save_path: Optional[str] = None):
        """
        初始化格式化器
        
        Args:
            save_path: 保存路径，默认使用配置中的路径
        """
        self.response = None
        self.save_path = save_path or self._get_default_save_path()
        
        # 确保保存目录存在
        Path(self.save_path).mkdir(parents=True, exist_ok=True)
    
    def _get_default_save_path(self) -> str:
        """获取默认保存路径"""
        try:
            from config import get_config
            config = get_config()
            return config.results_save_path
        except ImportError:
            # 如果无法导入config，使用默认路径
            return './results/'
    
    def load_response(self, response: Dict[str, Any]) -> 'TavilyFormatter':
        """
        加载搜索响应数据
        
        Args:
            response: Tavily搜索响应
            
        Returns:
            self: 支持链式调用
        """
        self.response = response
        return self
    
    def print_summary(self) -> None:
        """打印搜索摘要信息"""
        if not self.response:
            print("❌ 没有搜索数据")
            return
            
        print("=" * 60)
        print(f"🔍 查询: {self.response.get('query', 'N/A')}")
        print(f"⏱️  用时: {self.response.get('response_time', 'N/A')}秒")
        print(f"📊 结果: {len(self.response.get('results', []))}条")
        print("=" * 60)
    
    def print_results(self, max_content_length: int = 150) -> None:
        """
        打印搜索结果
        
        Args:
            max_content_length: 内容摘要的最大长度
        """
        if not self.response:
            print("❌ 没有搜索数据")
            return
            
        results = self.response.get('results', [])
        
        for i, result in enumerate(results, 1):
            print(f"\n📄 [{i}] {result.get('title', '无标题')}")
            print(f"   🔗 {result.get('url', 'N/A')}")
            print(f"   ⭐ 评分: {result.get('score', 0):.3f}")
            
            content = result.get('content', '')
            if content:
                if len(content) > max_content_length:
                    content = content[:max_content_length] + "..."
                print(f"   📝 {content}")
            print("-" * 50)
    
    def print_full(self, max_content_length: int = 150) -> None:
        """
        打印完整的格式化结果
        
        Args:
            max_content_length: 内容摘要的最大长度
        """
        self.print_summary()
        
        # AI答案
        if self.response and self.response.get('answer'):
            print(f"\n💡 AI答案:")
            print(f"{self.response['answer']}")
            print("-" * 50)
        
        # 搜索结果
        self.print_results(max_content_length)
        
        # 跟进问题
        if self.response and self.response.get('follow_up_questions'):
            print(f"\n❓ 相关问题:")
            for i, question in enumerate(self.response['follow_up_questions'], 1):
                print(f"   {i}. {question}")
    
    def to_dict(self) -> Optional[Dict[str, Any]]:
        """
        转换为结构化字典
        
        Returns:
            格式化后的字典数据
        """
        if not self.response:
            return None
            
        formatted = {
            "搜索信息": {
                "查询": self.response.get('query'),
                "响应时间": self.response.get('response_time'),
                "结果数量": len(self.response.get('results', []))
            },
            "AI答案": self.response.get('answer'),
            "搜索结果": [],
            "跟进问题": self.response.get('follow_up_questions', [])
        }
        
        for i, result in enumerate(self.response.get('results', []), 1):
            formatted["搜索结果"].append({
                "序号": i,
                "标题": result.get('title'),
                "链接": result.get('url'),
                "评分": result.get('score'),
                "内容摘要": result.get('content')
            })
        
        return formatted
    
    def to_json(self, filename: Optional[str] = None, 
                formatted: bool = True) -> Optional[str]:
        """
        保存为JSON文件
        
        Args:
            filename: 文件名，默认自动生成
            formatted: 是否使用格式化数据
            
        Returns:
            保存的文件名
        """
        if not self.response:
            print("❌ 没有搜索数据")
            return None
            
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            query = self.response.get('query', 'search').replace(' ', '_')
            # 清理查询字符串，移除特殊字符
            query = "".join(c for c in query if c.isalnum() or c in ('_', '-'))[:50]
            filename = f"tavily_{query}_{timestamp}.json"
        
        # 确保文件名不包含路径，然后拼接保存路径
        filename = Path(filename).name  # 只取文件名部分
        filepath = Path(self.save_path) / filename
        
        try:
            data = self.to_dict() if formatted else self.response
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            
            print(f"💾 已保存到: {filepath}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ 保存失败: {e}")
            return None
    
    def to_html(self, filename: Optional[str] = None, 
                title: Optional[str] = None) -> Optional[str]:
        """
        生成HTML报告
        
        Args:
            filename: 文件名，默认自动生成
            title: 报告标题
            
        Returns:
            保存的文件名
        """
        if not self.response:
            print("❌ 没有搜索数据")
            return None
            
        if not filename:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            query = self.response.get('query', 'search').replace(' ', '_')
            # 清理查询字符串，移除特殊字符
            query = "".join(c for c in query if c.isalnum() or c in ('_', '-'))[:50]
            filename = f"tavily_report_{query}_{timestamp}.html"
        
        # 确保文件名不包含路径，然后拼接保存路径
        filename = Path(filename).name  # 只取文件名部分
        filepath = Path(self.save_path) / filename
        
        if not title:
            title = f"Tavily搜索报告 - {self.response.get('query', '搜索结果')}"
        
        try:
            html_content = self._generate_html_content(title)
            
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(html_content)
            
            print(f"📄 HTML报告已保存到: {filepath}")
            return str(filepath)
            
        except Exception as e:
            print(f"❌ 生成HTML报告失败: {e}")
            return None
    
    def _generate_html_content(self, title: str) -> str:
        """生成HTML内容"""
        results_html = ""
        for i, result in enumerate(self.response.get('results', []), 1):
            content = html.escape(result.get('content', ''))
            results_html += f"""
            <div class="result">
                <h3>{i}. {html.escape(result.get('title', '无标题'))}</h3>
                <p><strong>链接:</strong> <a href="{result.get('url', '#')}" target="_blank">{result.get('url', 'N/A')}</a></p>
                <p><strong>评分:</strong> {result.get('score', 0):.3f}</p>
                <p><strong>内容:</strong> {content}</p>
            </div>
            """
        
        answer_html = ""
        if self.response.get('answer'):
            answer_html = f"""
            <div class="answer">
                <h2>💡 AI答案</h2>
                <p>{html.escape(self.response['answer'])}</p>
            </div>
            """
        
        questions_html = ""
        if self.response.get('follow_up_questions'):
            questions_list = ""
            for q in self.response['follow_up_questions']:
                questions_list += f"<li>{html.escape(q)}</li>"
            
            questions_html = f"""
            <div class="questions">
                <h2>❓ 相关问题</h2>
                <ul>{questions_list}</ul>
            </div>
            """
        
        return f"""
        <!DOCTYPE html>
        <html lang="zh-CN">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{html.escape(title)}</title>
            <style>
                body {{ font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; 
                       line-height: 1.6; margin: 40px; background-color: #f5f5f5; }}
                .container {{ max-width: 1000px; margin: 0 auto; background: white; 
                             padding: 30px; border-radius: 10px; box-shadow: 0 2px 10px rgba(0,0,0,0.1); }}
                h1 {{ color: #333; border-bottom: 3px solid #007acc; padding-bottom: 10px; }}
                .summary {{ background: #e8f4f8; padding: 20px; border-radius: 8px; margin: 20px 0; }}
                .summary p {{ margin: 5px 0; }}
                .result {{ border: 1px solid #ddd; padding: 20px; margin: 15px 0; 
                          border-radius: 8px; background: #fafafa; }}
                .result h3 {{ color: #007acc; margin-top: 0; }}
                .answer {{ background: #e8f5e8; padding: 20px; border-radius: 8px; margin: 20px 0; }}
                .questions {{ background: #fff4e8; padding: 20px; border-radius: 8px; margin: 20px 0; }}
                a {{ color: #007acc; text-decoration: none; }}
                a:hover {{ text-decoration: underline; }}
                .timestamp {{ color: #666; font-size: 12px; text-align: right; margin-top: 30px; }}
            </style>
        </head>
        <body>
            <div class="container">
                <h1>{html.escape(title)}</h1>
                
                <div class="summary">
                    <p><strong>🔍 搜索查询:</strong> {html.escape(self.response.get('query', 'N/A'))}</p>
                    <p><strong>⏱️ 响应时间:</strong> {self.response.get('response_time', 'N/A')} 秒</p>
                    <p><strong>📊 结果数量:</strong> {len(self.response.get('results', []))} 条</p>
                </div>
                
                {answer_html}
                
                <h2>📄 搜索结果</h2>
                {results_html}
                
                {questions_html}
                
                <div class="timestamp">
                    报告生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
                </div>
            </div>
        </body>
        </html>
        """
    
    def analyze_quality(self) -> Dict[str, Any]:
        """
        分析搜索结果质量
        
        Returns:
            质量分析报告
        """
        if not self.response:
            return {"错误": "没有搜索数据"}
            
        results = self.response.get('results', [])
        
        if not results:
            return {"状态": "无结果"}
        
        # 评分统计
        scores = [result.get('score', 0) for result in results]
        avg_score = sum(scores) / len(scores)
        
        # 质量分级
        high_quality = len([s for s in scores if s > 0.7])
        medium_quality = len([s for s in scores if 0.4 <= s <= 0.7])
        low_quality = len([s for s in scores if s < 0.4])
        
        # 内容长度统计
        content_lengths = [len(result.get('content', '')) for result in results]
        avg_content_length = sum(content_lengths) / len(content_lengths) if content_lengths else 0
        
        return {
            "结果总数": len(results),
            "平均评分": round(avg_score, 3),
            "评分分布": {
                "高质量(>0.7)": high_quality,
                "中等质量(0.4-0.7)": medium_quality,
                "低质量(<0.4)": low_quality
            },
            "内容统计": {
                "平均内容长度": round(avg_content_length),
                "最长内容": max(content_lengths) if content_lengths else 0,
                "最短内容": min(content_lengths) if content_lengths else 0
            },
            "响应时间": self.response.get('response_time', 'N/A'),
            "质量评估": "优秀" if avg_score > 0.7 else "良好" if avg_score > 0.5 else "一般"
        }


# 使用示例和便捷函数
def quick_format(response: Dict[str, Any], save_json: bool = False, 
                save_html: bool = False) -> TavilyFormatter:
    """
    快速格式化Tavily搜索结果
    
    Args:
        response: Tavily搜索响应
        save_json: 是否保存JSON文件
        save_html: 是否保存HTML报告
        
    Returns:
        格式化器实例
    """
    formatter = TavilyFormatter().load_response(response)
    
    # 打印格式化结果
    formatter.print_full()
    
    # 打印质量分析
    quality = formatter.analyze_quality()
    print(f"\n📈 质量分析:")
    print(f"   总体评估: {quality.get('质量评估', 'N/A')}")
    print(f"   平均评分: {quality.get('平均评分', 'N/A')}")
    print(f"   高质量结果: {quality.get('评分分布', {}).get('高质量(>0.7)', 0)}条")
    
    # 可选保存
    if save_json:
        formatter.to_json()
    
    if save_html:
        formatter.to_html()
    
    return formatter


if __name__ == "__main__":
    # 测试示例
    sample_response = {
        "query": "deepseek AI模型",
        "response_time": 1.5,
        "answer": "DeepSeek是一家中国AI公司开发的开源大语言模型...",
        "results": [
            {
                "title": "DeepSeek官网",
                "url": "https://www.deepseek.com",
                "content": "DeepSeek是一家专注于AI研究的公司...",
                "score": 0.85
            }
        ],
        "follow_up_questions": ["DeepSeek的技术优势是什么？", "如何使用DeepSeek API？"]
    }
    
    # 快速格式化示例
    formatter = quick_format(sample_response, save_json=True, save_html=True) 