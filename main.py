# main.py 启动逻辑框架

import sys
import os
from PyQt6.QtWidgets import QApplication
from core.config_manager import ConfigManager
from core.parser import DataParser
from ui.main_window import MainWindow

def get_base_path():
    """
    处理绝对路径：兼容开发环境与单文件打包环境（如 PyInstaller 的 _MEIPASS）
    确保 assets/ 和 data/ 目录在任何环境下都能被正确读取
    """
    if hasattr(sys, '_MEIPASS'):
        return sys._MEIPASS
    return os.path.dirname(os.path.abspath(__file__))

def main():
    # 1. 初始化 Qt 应用上下文
    app = QApplication(sys.argv)
    
    # 2. 获取根路径
    base_dir = get_base_path()
    assets_dir = os.path.join(base_dir, 'assets')
    data_dir = os.path.join(base_dir, 'data')
    
    # 3. 初始化全局配置中心 (单例模式)
    config = ConfigManager()
    config.load_i18n(os.path.join(assets_dir, 'i18n_cn.json'))
    
    # 4. 执行数据解析
    parser = DataParser()
    # 自动扫描 data 目录，寻找默认的配置文件 (支持容错与格式回退)
    default_data_file = parser.scan_directory(data_dir, default_file="example_landscape.json")
    
    try:
        # data_tree 是一棵高度标准化的字典树，屏蔽了底层 XML/JSON/YAML 的差异
        data_tree = parser.parse(default_data_file)
    except Exception as e:
        # 抛出致命错误，可接入 Logging 或弹窗报错
        print(f"数据解析失败: {e}")
        sys.exit(1)
        
    # 5. 初始化主窗口，注入解析好的数据树和样式
    window = MainWindow(data_tree)
    
    # 加载全局 QSS 皮肤
    with open(os.path.join(assets_dir, 'styles.qss'), 'r', encoding='utf-8') as f:
        window.setStyleSheet(f.read())
        
    # 6. 显示窗口并挂起主循环
    window.show()
    sys.exit(app.exec())

if __name__ == "__main__":
    main()