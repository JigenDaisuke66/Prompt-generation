import sys
import os
from PyQt6.QtWidgets import QApplication
from core.config_manager import ConfigManager
from core.parser import DataParser
from ui.main_window import MainWindow

def get_base_path():
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def main():
    app = QApplication(sys.argv)
    
    base_dir = get_base_path()
    assets_dir = os.path.join(base_dir, 'assets')
    data_dir = os.path.join(base_dir, 'data')
    
    config = ConfigManager()
    config.set_assets_dir(assets_dir)
    config.load_language("en")
    
    parser = DataParser()
    default_data_file = parser.scan_directory(data_dir, default_file="example_landscape.json")
    
    try:
        data_tree = parser.parse(default_data_file)
    except Exception as e:
        print(f"数据解析失败: {e}")
        sys.exit(1)
        
    window = MainWindow(data_tree)
    # 【已删除硬编码加载 QSS 的代码，交由 MainWindow 统一处理】
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()