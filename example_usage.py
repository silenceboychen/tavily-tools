"""
Tavily搜索结果格式化工具使用示例
演示如何使用TavilyFormatter类进行结构化输出
"""

from tavily_formatter import TavilyFormatter, quick_format
from config import get_tavily_client, get_config


def example_basic_formatting():
    """基础格式化示例"""
    print("🔥 示例1: 基础格式化输出")
    print("="*50)
    
    # 使用配置管理获取客户端
    client = get_tavily_client()
    
    # 执行搜索
    response = client.search(query="Python机器学习库")
    
    # 使用格式化工具
    formatter = TavilyFormatter()
    formatter.load_response(response)
    
    # 打印摘要
    formatter.print_summary()
    
    # 打印结果
    formatter.print_results(max_content_length=100)


def example_full_formatting():
    """完整格式化示例"""
    print("\n\n🚀 示例2: 完整格式化输出")
    print("="*50)
    
    client = get_tavily_client()
    response = client.search(query="Claude AI助手功能")
    
    # 完整格式化输出
    formatter = TavilyFormatter().load_response(response)
    formatter.print_full()


def example_quality_analysis():
    """质量分析示例"""
    print("\n\n📊 示例3: 搜索质量分析")
    print("="*50)
    
    client = get_tavily_client()
    response = client.search(query="量子计算最新突破")
    
    formatter = TavilyFormatter().load_response(response)
    
    # 分析搜索质量
    quality = formatter.analyze_quality()
    
    print("📈 详细质量分析:")
    print(f"   🔢 结果总数: {quality['结果总数']}")
    print(f"   ⭐ 平均评分: {quality['平均评分']:.4f}")
    print(f"   🎯 响应时间: {quality['响应时间']}秒")
    
    # 评分分布
    print(f"\n📊 评分分布:")
    for level, count in quality['评分分布'].items():
        print(f"   {level}: {count}条")


def example_data_conversion():
    """数据转换示例"""
    print("\n\n🔄 示例4: 数据格式转换")
    print("="*50)
    
    client = get_tavily_client()
    response = client.search(query="人工智能伦理")
    
    formatter = TavilyFormatter().load_response(response)
    
    # 转换为结构化字典
    structured_data = formatter.to_dict()
    print(f"✅ 已转换为结构化字典，包含 {len(structured_data)} 个主要字段")
    
    # 保存为JSON
    json_file = formatter.to_json(filename="ai_ethics_search.json")
    print(f"💾 JSON文件已保存: {json_file}")
    
    # 生成HTML报告
    html_file = formatter.to_html(filename="ai_ethics_report.html", title="AI伦理搜索报告")
    print(f"📄 HTML报告已生成: {html_file}")


def example_quick_format():
    """快速格式化示例"""
    print("\n\n⚡ 示例5: 一键快速格式化")
    print("="*50)
    
    client = get_tavily_client()
    response = client.search(query="区块链技术应用")
    
    # 一键格式化，同时保存JSON和HTML
    formatter = quick_format(
        response, 
        save_json=True, 
        save_html=True
    )
    
    print("✅ 快速格式化完成！已自动保存所有格式")


def example_batch_processing():
    """批量处理示例"""
    print("\n\n🔄 示例6: 批量搜索处理")
    print("="*50)
    
    client = get_tavily_client()
    
    # 定义多个搜索主题
    search_topics = [
        "自然语言处理发展",
        "计算机视觉新技术", 
        "强化学习应用"
    ]
    
    results_summary = []
    
    for i, topic in enumerate(search_topics, 1):
        print(f"\n🔍 搜索 {i}/{len(search_topics)}: {topic}")
        
        try:
            # 执行搜索
            response = client.search(query=topic)
            
            # 快速处理
            formatter = TavilyFormatter().load_response(response)
            quality = formatter.analyze_quality()
            
            # 保存结果
            json_file = formatter.to_json(formatted=True)
            
            # 记录摘要
            summary = {
                "主题": topic,
                "结果数": quality["结果总数"],
                "平均评分": quality["平均评分"],
                "文件": json_file
            }
            results_summary.append(summary)
            
            print(f"   ✅ 完成 | 结果: {quality['结果总数']}条 | 评分: {quality['平均评分']:.3f}")
            
        except Exception as e:
            print(f"   ❌ 失败: {e}")
    
    # 显示批量处理总结
    print(f"\n📋 批量处理总结:")
    print("-" * 60)
    for summary in results_summary:
        print(f"   {summary['主题']}: {summary['结果数']}条结果，评分{summary['平均评分']:.3f}")
    
    print(f"\n🎉 批量处理完成！共处理 {len(results_summary)} 个主题")


def run_all_examples():
    """运行所有示例"""
    print("🌟 Tavily格式化工具完整示例演示")
    print("="*60)
    
    try:
        # 显示配置信息
        config = get_config()
        config.show_config()
        
        # 运行所有示例
        example_basic_formatting()
        example_full_formatting() 
        example_quality_analysis()
        example_data_conversion()
        example_quick_format()
        example_batch_processing()
        
        print(f"\n🎊 所有示例运行完成！")
        print("💡 提示：您可以查看生成的JSON和HTML文件")
        
    except Exception as e:
        print(f"❌ 示例运行出错: {e}")


if __name__ == "__main__":
    # 询问用户要运行哪个示例
    print("🎮 请选择要运行的示例:")
    print("1. 基础格式化")
    print("2. 完整格式化")
    print("3. 质量分析")
    print("4. 数据转换")
    print("5. 快速格式化")
    print("6. 批量处理")
    print("7. 运行所有示例")
    
    choice = input("\n请输入选项 (1-7): ").strip()
    
    examples = {
        '1': example_basic_formatting,
        '2': example_full_formatting,
        '3': example_quality_analysis,
        '4': example_data_conversion,
        '5': example_quick_format,
        '6': example_batch_processing,
        '7': run_all_examples
    }
    
    if choice in examples:
        examples[choice]()
    else:
        print("❌ 无效选项")
        run_all_examples() 