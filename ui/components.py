import random
from collections import defaultdict
from PyQt6.QtWidgets import (QPushButton, QWidget, QVBoxLayout, QHBoxLayout, 
                             QLabel, QDoubleSpinBox)
from PyQt6.QtCore import Qt, pyqtSignal
from ui.flow_layout import FlowLayout
from core.config_manager import ConfigManager

class WeightPopup(QWidget):
    """悬浮的权重调节面板：支持手动输入和快捷重置"""
    weight_changed = pyqtSignal(float)

    def __init__(self, current_weight=1.0, parent=None):
        super().__init__(parent)
        self.setWindowFlags(Qt.WindowType.Popup | Qt.WindowType.FramelessWindowHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)

        config = ConfigManager()
        
        # 内部主容器（用于应用 QSS 样式）
        self.container = QWidget(self)
        self.container.setObjectName("weight_popup_container")
        layout = QVBoxLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(self.container)

        # 面板内部布局
        vbox = QVBoxLayout(self.container)
        vbox.setContentsMargins(10, 10, 10, 10)

        # 标题与输入框
        vbox.addWidget(QLabel(config.get_text("lbl_manual_weight")))
        self.spin_box = QDoubleSpinBox()
        self.spin_box.setRange(0.1, 5.0)
        self.spin_box.setSingleStep(0.05)
        self.spin_box.setValue(current_weight)
        vbox.addWidget(self.spin_box)

        # 重置按钮
        reset_btn = QPushButton(config.get_text("btn_reset_weight"))
        reset_btn.clicked.connect(lambda: self.spin_box.setValue(1.0))
        vbox.addWidget(reset_btn)

        # 当输入框的值改变时，向外发送信号
        self.spin_box.valueChanged.connect(self._on_value_changed)

    def _on_value_changed(self, value):
        self.weight_changed.emit(value)


class TagWidget(QWidget):
    """组合标签组件：包含主按钮和权重设置小按钮"""
    def __init__(self, display_name, tag_value, category=""):
        super().__init__()
        self.display_name = display_name
        self.tag_value = tag_value
        self.category = category
        self.weight = 1.0

        # 组件布局：去掉所有边距，让两个按钮贴合在一起
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        # 1. 主标签按钮
        self.main_btn = QPushButton(self.display_name)
        self.main_btn.setCheckable(True)
        self.main_btn.setObjectName("tag_main_btn")
        
        # 2. 调节权重小按钮
        self.edit_btn = QPushButton("⚙")
        self.edit_btn.setObjectName("tag_edit_btn")
        self.edit_btn.setFixedWidth(24)
        
        self.layout.addWidget(self.main_btn)
        self.layout.addWidget(self.edit_btn)

        self.edit_btn.clicked.connect(self.show_weight_popup)
        
    def show_weight_popup(self):
        self.popup = WeightPopup(self.weight, self)
        self.popup.weight_changed.connect(self.update_weight)
        
        # 计算全局坐标：让弹窗准确出现在 edit_btn 的左下角，并向左微调
        pos = self.edit_btn.mapToGlobal(self.edit_btn.rect().bottomLeft())
        pos.setX(pos.x() - 100) 
        self.popup.move(pos)
        self.popup.show()

    def update_weight(self, new_weight):
        self.weight = round(new_weight, 2)
        if self.weight == 1.0:
            self.main_btn.setText(self.display_name)
        else:
            self.main_btn.setText(f"{self.display_name} ({self.weight})")

    # 保持向后兼容，让 MainWindow 可以像操作普通 Button 一样操作它
    def isChecked(self):
        return self.main_btn.isChecked()

    def setChecked(self, checked):
        self.main_btn.setChecked(checked)

    def get_formatted_tag(self):
        if self.weight == 1.0:
            return self.tag_value
        return f"({self.tag_value}:{self.weight})"
    
    def get_formatted_display(self):
        if self.weight == 1.0:
            return self.display_name
        return f"({self.display_name}:{self.weight})"


class ModuleGroupWidget(QWidget):
    """模块组容器：包含全局开关、随机按钮和流式布局容器"""
    def __init__(self, title, is_open=True):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 10)
        config = ConfigManager()

        # 头部控制栏
        self.header_layout = QHBoxLayout()
        self.toggle_btn = QPushButton("▼" if is_open else "▶")
        self.toggle_btn.setFixedSize(30, 30)
        self.toggle_btn.clicked.connect(self.toggle_content)
        
        self.title_label = QLabel(title)
        self.random_btn = QPushButton(config.get_text("btn_random_group"))
        self.random_btn.setObjectName("btn_random_group")
        self.random_btn.clicked.connect(self.random_select)
        
        self.header_layout.addWidget(self.toggle_btn)
        self.header_layout.addWidget(self.title_label)
        self.header_layout.addStretch()
        self.header_layout.addWidget(self.random_btn)
        self.layout.addLayout(self.header_layout)

        # 内容区（使用流式布局）
        self.content_widget = QWidget()
        self.content_layout = FlowLayout(self.content_widget)
        self.layout.addWidget(self.content_widget)
        
        self.content_widget.setVisible(is_open)

    def toggle_content(self):
        is_visible = not self.content_widget.isVisible()
        self.content_widget.setVisible(is_visible)
        self.toggle_btn.setText("▼" if is_visible else "▶")
        # --- 新增：折叠时自动清空内部所有选中状态 ---
        if not is_visible:
            all_tags = self.content_widget.findChildren(TagWidget)
            for btn in all_tags:
                btn.setChecked(False)
        
    def add_tag(self, tag_widget: TagWidget):
        self.content_layout.addWidget(tag_widget)

    def random_select(self):
        """优化后的随机算法：按子模块分组，每组只抽 1 个"""
        # 注意：这里已经更新为查找 TagWidget
        all_tags = self.content_widget.findChildren(TagWidget)
        if not all_tags:
            return

        # 1. 先清空当前组内所有按钮的选中状态
        for btn in all_tags:
            btn.setChecked(False)

        # 2. 按 category 对标签进行分组
        grouped_tags = defaultdict(list)
        for btn in all_tags:
            grouped_tags[btn.category].append(btn)

        # 3. 遍历每一个子模块，随机抽取 1 个标签激活
        for category, btns in grouped_tags.items():
            picked_btn = random.choice(btns)
            picked_btn.setChecked(True)