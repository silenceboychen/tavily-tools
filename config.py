"""
配置管理模块
用于安全地加载和管理环境变量配置
"""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv

class Config:
    """配置管理类"""
    
    def __init__(self):
        """初始化配置，自动加载.env文件"""
        self._load_environment()
        self._validate_config()
    
    def _load_environment(self):
        """加载环境变量"""
        # 查找.env文件的路径
        env_path = Path(__file__).parent / '.env'
        
        # 如果.env文件存在，则加载它
        if env_path.exists():
            load_dotenv(env_path)
            print(f"✅ 已加载环境变量文件: {env_path}")
        else:
            print(f"⚠️  未找到.env文件: {env_path}")
            print("请根据env_template.txt创建.env文件并配置API密钥")
    
    def _validate_config(self):
        """验证必要的配置项"""
        if not self.tavily_api_key:
            print("❌ 错误: 未找到TAVILY_API_KEY环境变量")
            print("📝 请按以下步骤配置:")
            print("1. 复制 env_template.txt 为 .env")
            print("2. 编辑 .env 文件，填入您的Tavily API密钥")
            print("3. 重新运行程序")
            sys.exit(1)
        elif self.tavily_api_key == "your_tavily_api_key_here":
            print("❌ 错误: 请在.env文件中设置真实的API密钥")
            print("当前API密钥仍为模板默认值")
            sys.exit(1)
    
    @property
    def tavily_api_key(self) -> str:
        """获取Tavily API密钥"""
        return os.getenv('TAVILY_API_KEY', '')
    
    @property
    def default_search_query(self) -> str:
        """获取默认搜索查询"""
        return os.getenv('DEFAULT_SEARCH_QUERY', 'deepseek')
    
    @property
    def results_save_path(self) -> str:
        """获取结果保存路径"""
        return os.getenv('RESULTS_SAVE_PATH', './')
    
    @property
    def log_level(self) -> str:
        """获取日志级别"""
        return os.getenv('LOG_LEVEL', 'INFO')
    
    def show_config(self):
        """显示当前配置（隐藏敏感信息）"""
        print("📋 当前配置:")
        print(f"   API密钥: {'*' * 8}...{self.tavily_api_key[-4:] if len(self.tavily_api_key) > 4 else '****'}")
        print(f"   默认搜索: {self.default_search_query}")
        print(f"   保存路径: {self.results_save_path}")
        print(f"   日志级别: {self.log_level}")


def get_tavily_client():
    """
    获取配置好的Tavily客户端
    
    Returns:
        TavilyClient: 已配置API密钥的客户端实例
    """
    from tavily import TavilyClient
    
    try:
        config = Config()
        client = TavilyClient(config.tavily_api_key)
        print(f"🔑 Tavily客户端初始化成功")
        return client
    except Exception as e:
        print(f"❌ Tavily客户端初始化失败: {e}")
        print("请检查您的API密钥配置")
        sys.exit(1)


def get_config():
    """
    获取配置实例
    
    Returns:
        Config: 配置实例
    """
    return Config()


# 全局配置实例（可选使用）
config = None

def init_config():
    """初始化全局配置"""
    global config
    if config is None:
        config = Config()
    return config 