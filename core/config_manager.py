import json
import os

class ConfigManager:
    """配置中心：处理多语言、全局设置"""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._init()
        return cls._instance

    def _init(self):
        self.language_map = {}
        self.current_lang = "en"
        self.assets_dir = "" # 记录资源文件夹绝对路径

    def set_assets_dir(self, path: str):
        self.assets_dir = path

    def load_language(self, lang: str = "en"):
        self.current_lang = lang
        filepath = os.path.join(self.assets_dir, f'i18n_{lang}.json')
        if os.path.exists(filepath):
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    self.language_map = json.load(f)
            except json.JSONDecodeError:
                print(f"⚠️ 警告: 语言文件 {filepath} 格式错误。")
                self.language_map = {}
        else:
            print(f"⚠️ 警告: 找不到语言文件 {filepath}")

    def get_text(self, key: str) -> str:
        return self.language_map.get(key, key)