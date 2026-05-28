import json
import os

class DataParser:
    """
    动态数据解析器
    职责：读取不同格式的物理文件，返回统一标准的内存数据树结构
    """
    def __init__(self):
        # 注册支持的解析策略
        self._strategies = {
            '.json': self._parse_json,
            # 如果以后需要支持 yaml，在这里取消注释即可，并实现对应方法
            # '.yaml': self._parse_yaml, 
        }

    def scan_directory(self, dir_path, default_file=None):
        """扫描目录，返回目标文件路径。包含路径有效性校验。"""
        # 1. 确保目录存在
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)
            return None

        # 2. 优先匹配默认文件 (例如：example_landscape.json)
        if default_file:
            target_path = os.path.join(dir_path, default_file)
            if os.path.exists(target_path):
                return target_path

        # 3. 容错回退：如果没有找到默认文件，就随便找一个 .json 文件返回
        for file in os.listdir(dir_path):
            if file.endswith('.json'):
                return os.path.join(dir_path, file)
                
        return None

    def parse(self, filepath):
        """统一解析入口"""
        if not filepath or not os.path.exists(filepath):
            raise FileNotFoundError(f"在 data 目录下没有找到任何词库配置文件。")

        ext = os.path.splitext(filepath)[-1].lower()
        
        # 动态路由到对应的解析函数
        if ext in self._strategies:
            raw_data = self._strategies[ext](filepath)
            # 无论何种格式，最终进入标准化清洗流程
            return self._normalize_data(raw_data)
        else:
            raise ValueError(f"不支持的文件扩展名: {ext}")

    def _parse_json(self, filepath):
        """真正的 JSON 读取逻辑"""
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def _normalize_data(self, raw_dict):
        """
        数据清洗与标准化转换
        因为我们现在写的 example_landscape.json 格式已经非常完美地契合了 UI 的需求，
        所以目前直接返回即可。未来如果加入 XML，才需要在这里做复杂的树结构抹平。
        """
        return raw_dict