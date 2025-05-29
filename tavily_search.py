"""
Tavily搜索结果格式化工具 - 主程序
支持交互式搜索和多种格式化输出
"""

import json
from datetime import datetime
from tavily_formatter import TavilyFormatter, quick_format
from config import get_tavily_client, get_config

def interactive_search():
    """
    交互式搜索功能
    提供用户友好的搜索体验和结果展示
    """
    try:
        # 获取配置和客户端
        config = get_config()
        client = get_tavily_client()
        
        # 显示配置信息
        config.show_config()
        
        # 获取搜索查询
        search_query = input(f"\n🔍 请输入搜索关键词 (默认: {config.default_search_query}): ").strip()
        if not search_query:
            search_query = config.default_search_query
        
        print(f"🚀 正在搜索...")
        
        # 执行搜索
        response = client.search(query=search_query)
        
        # 格式化输出
        formatter = TavilyFormatter().load_response(response)
        formatter.print_full()
        
        # 分析质量
        quality = formatter.analyze_quality()
        print(f"\n📈 搜索质量分析:")
        print(f"   结果总数: {quality['结果总数']}")
        print(f"   平均评分: {quality['平均评分']:.3f}")
        print(f"   高质量结果: {quality['评分分布']['高质量(>0.7)']}")
        print(f"   中等质量结果: {quality['评分分布']['中等质量(0.4-0.7)']}")
        print(f"   低质量结果: {quality['评分分布']['低质量(<0.4)']}")
        print(f"   响应时间: {quality['响应时间']}")
        
        # 询问是否保存结果
        save_json = input(f"\n💾 是否保存搜索结果到JSON文件？(y/n): ").lower().strip()
        if save_json in ['y', 'yes', '是']:
            filename = formatter.to_json()
            print(f"\n💾 搜索结果已保存到: {filename}")
            print("✅ 结果已成功保存!")
        
        # 询问是否显示原始响应
        show_raw = input(f"\n📋 是否显示原始JSON响应？(y/n): ").lower().strip()
        if show_raw in ['y', 'yes', '是']:
            print(f"\n{'='*80}")
            print("📋 原始JSON响应:")
            print('='*80)
            print(json.dumps(response, ensure_ascii=False, indent=2))
        
        # 询问是否生成HTML报告
        save_html = input(f"\n📄 是否生成HTML报告？(y/n): ").lower().strip()
        if save_html in ['y', 'yes', '是']:
            html_filename = formatter.to_html(title=f"Tavily搜索报告 - {search_query}")
            print(f"\n📄 HTML报告已生成: {html_filename}")
            print("✅ 报告已成功保存!")
        
    except KeyboardInterrupt:
        print(f"\n\n🛑 搜索已被用户中断")
    except Exception as e:
        print(f"\n❌ 搜索过程中发生错误: {e}")
        print("请检查网络连接和API密钥配置")

def batch_search_example():
    """
    批量搜索示例
    展示如何进行多个主题的批量搜索
    """
    try:
        client = get_tavily_client()
        config = get_config()
        
        # 定义搜索主题
        topics = [
            "人工智能最新发展",
            "量子计算突破",
            "自动驾驶技术"
        ]
        
        print("🔄 开始批量搜索...")
        
        for i, topic in enumerate(topics, 1):
            print(f"\n📍 正在搜索第{i}个主题: {topic}")
            
            # 执行搜索
            response = client.search(query=topic)
            
            # 快速格式化并保存
            formatter = quick_format(response, save_json=True, save_html=False)
            
            # 显示质量摘要
            quality = formatter.analyze_quality()
            print(f"   ✅ 完成 | 结果数: {quality['结果总数']} | 平均评分: {quality['平均评分']:.3f}")
        
        print(f"\n🎉 批量搜索完成！共处理 {len(topics)} 个主题")
        
    except Exception as e:
        print(f"❌ 批量搜索失败: {e}")

def main():
    """主函数"""
    print("🌟 欢迎使用 Tavily 搜索结果格式化工具!")
    print("="*60)
    
    try:
        # 显示菜单
        print("请选择操作模式:")
        print("1. 交互式搜索 (推荐)")
        print("2. 批量搜索示例")
        print("3. 退出")
        
        choice = input("\n请输入选项 (1-3): ").strip()
        
        if choice == '1':
            interactive_search()
        elif choice == '2':
            batch_search_example()
        elif choice == '3':
            print("👋 感谢使用，再见!")
        else:
            print("❌ 无效选项，请重新运行程序")
            
    except Exception as e:
        print(f"❌ 程序运行出错: {e}")

if __name__ == "__main__":
    main()