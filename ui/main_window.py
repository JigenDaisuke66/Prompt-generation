from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QScrollArea, QPushButton, QTextEdit, QLabel)
from ui.components import TagWidget, ModuleGroupWidget

class MainWindow(QMainWindow):
    def __init__(self, data_tree):
        super().__init__()
        self.setWindowTitle(data_tree.get("项目名称", "Prompt-generation"))
        self.resize(1200, 800)
        self.data_tree = data_tree
        self.setup_ui()
        self._bind_events()

    def setup_ui(self):
        # 主容器
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        # 上半部分：提示词配置区（带滚动条）
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName("scroll_content")
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area, stretch=3)

        # 动态渲染数据树
        self._render_modules(self.data_tree.get("模块组", []))
        self.scroll_layout.addStretch()
        
        output_container = QWidget()
        output_layout = QHBoxLayout(output_container)
        output_layout.setContentsMargins(0, 0, 0, 0) # 去除边缘留白

        # 左栏：本地语言预览
        left_layout = QVBoxLayout()
        left_label = QLabel("🌐 本地语言预览")
        left_label.setObjectName("output_label")
        self.output_text_local = QTextEdit()
        self.output_text_local.setPlaceholderText("母语提示词将显示在这里...")
        left_layout.addWidget(left_label)
        left_layout.addWidget(self.output_text_local)

        # 右栏：英文提示词输出
        right_layout = QVBoxLayout()
        right_label = QLabel("📄 英文提示词 (用于复制给 AI)")
        right_label.setObjectName("output_label")
        self.output_text_en = QTextEdit()
        self.output_text_en.setPlaceholderText("生成的英文提示词将显示在这里...")
        right_layout.addWidget(right_label)
        right_layout.addWidget(self.output_text_en)

        output_layout.addLayout(left_layout)
        output_layout.addLayout(right_layout)
        
        main_layout.addWidget(output_container, stretch=1)
        # =======================================================
        
        # 底部按钮栏
        bottom_layout = QHBoxLayout()
        
        self.global_random_btn = QPushButton("🎲 全局一键随机")
        self.global_random_btn.setObjectName("global_random_btn")
        self.global_random_btn.setMinimumHeight(45)
        
        self.generate_btn = QPushButton("🚀 生成提示词")
        self.generate_btn.setObjectName("generate_btn")
        self.generate_btn.setMinimumHeight(45)

        bottom_layout.addWidget(self.global_random_btn, stretch=1)
        bottom_layout.addWidget(self.generate_btn, stretch=2)
        
        main_layout.addLayout(bottom_layout)

    def _bind_events(self):
        """集中绑定全局事件"""
        self.generate_btn.clicked.connect(self.generate_prompt)
        # 新增：绑定全局随机事件
        self.global_random_btn.clicked.connect(self.trigger_global_random)

    def trigger_global_random(self):
        """触发所有可见模块组的随机抽取"""
        all_groups = self.scroll_content.findChildren(ModuleGroupWidget)
        for group in all_groups:
            # 加入一个人性化的小逻辑：如果用户手动把某个模块折叠（隐藏）了，就不参与全局随机
            if group.content_widget.isVisible():
                group.random_select()        

    def generate_prompt(self):
        """扫描全局 UI，收集被选中的标签并生成最终 Prompt"""
        selected_tags = []
        
        # 利用 findChildren 查找所有自定义的 TagWidget 组合组件
        all_tag_widgets = self.scroll_content.findChildren(TagWidget)
        
        for widget in all_tag_widgets:
            if widget.isChecked():
                selected_tags.append(widget.get_formatted_tag())
        
        if selected_tags:
            final_prompt = ", ".join(selected_tags)
            self.output_text.setText(final_prompt)
        else:
            self.output_text.setText("⚠️ 未选择任何标签。")

    def _render_modules(self, module_groups):
        """递归渲染模块，解析 JSON 数据生成 UI"""
        for group in module_groups:
            group_widget = ModuleGroupWidget(group["模块名"], group.get("开启状态", True))
            
            # 渲染子模块和标签
            for sub_module in group.get("子模块", []):
                sub_name = sub_module.get("子模块名", "默认分类")
                tags = sub_module.get("标签列表", {})
                
                for display_name, tag_value in tags.items():
                    # 实例化 TagWidget 并传入 category，供随机抽选算法使用
                    btn = TagWidget(display_name, tag_value, category=sub_name)
                    group_widget.add_tag(btn)
                    
            self.scroll_layout.addWidget(group_widget)