import random
import os
from collections import defaultdict
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                             QScrollArea, QPushButton, QTextEdit, QLabel, QApplication,
                             QFileDialog, QMessageBox)
from PyQt6.QtGui import QAction, QActionGroup
from ui.components import TagWidget, ModuleGroupWidget
from core.config_manager import ConfigManager
from core.parser import DataParser
from PyQt6.QtWidgets import QLineEdit  # 引入输入框组件
from ui.editor_window import LibraryEditor # 引入我们刚写的编辑器

class MainWindow(QMainWindow):
    def __init__(self, data_tree):
        super().__init__()
        self.config = ConfigManager()
        self.setWindowTitle(data_tree.get("project_name", "Prompt-generation"))
        self.resize(1200, 800)
        self.data_tree = data_tree
        self.switch_theme("dark") # 默认加载暗黑科技风
        
        # 新增：用于临时存储后台随机抽到的标签组件对象
        self.last_inspired_widgets = []
        
        self._create_menu_bar()
        self.setup_ui()
        self._bind_events()
        self.retranslate_ui()
        
        self.statusBar().showMessage("Ready.")

    def _create_menu_bar(self):
        self.menu_bar = self.menuBar()
        self.menu_bar.setObjectName("main_menu_bar")

        self.file_menu = self.menu_bar.addMenu("")
        
        # === 1. 新建词库 ===
        self.new_action = QAction("", self)
        self.new_action.setShortcut("Ctrl+N")
        self.new_action.triggered.connect(self.new_library)
        self.file_menu.addAction(self.new_action)
        
        self.file_menu.addSeparator()

        # === 2. 加载/加载并编辑 ===
        self.open_action = QAction("", self)
        self.open_action.setShortcut("Ctrl+O")
        self.open_action.triggered.connect(self.load_new_dict) 
        self.file_menu.addAction(self.open_action)
        
        self.edit_other_action = QAction("", self)
        self.edit_other_action.triggered.connect(self.edit_other) 
        self.file_menu.addAction(self.edit_other_action)
        
        self.file_menu.addSeparator()
        
        # === 3. 编辑当前词库 ===
        self.edit_current_action = QAction("", self)
        self.edit_current_action.setShortcut("Ctrl+E")
        self.edit_current_action.triggered.connect(self.edit_current)
        self.file_menu.addAction(self.edit_current_action)

        self.file_menu.addSeparator()
        self.exit_action = QAction("", self)
        self.exit_action.setShortcut("Ctrl+Q")
        self.exit_action.triggered.connect(self.close)
        self.file_menu.addAction(self.exit_action)
        

        # 2. 主题菜单
        self.theme_menu = self.menu_bar.addMenu("")
        theme_group = QActionGroup(self)
        
        self.action_theme_dark = QAction("", self, checkable=True)
        self.action_theme_dark.setChecked(True)
        self.action_theme_dark.triggered.connect(lambda: self.switch_theme("dark"))
        theme_group.addAction(self.action_theme_dark)
        
        self.action_theme_light = QAction("", self, checkable=True)
        self.action_theme_light.triggered.connect(lambda: self.switch_theme("light"))
        theme_group.addAction(self.action_theme_light)

        self.action_theme_dracula = QAction("", self, checkable=True)
        self.action_theme_dracula.triggered.connect(lambda: self.switch_theme("dracula"))
        theme_group.addAction(self.action_theme_dracula)

        self.theme_menu.addAction(self.action_theme_dark)
        self.theme_menu.addAction(self.action_theme_light)
        self.theme_menu.addAction(self.action_theme_dracula)

        # 3. 设置菜单 (包含语言)
        self.settings_menu = self.menu_bar.addMenu("")
        self.lang_menu = self.settings_menu.addMenu("")
        lang_group = QActionGroup(self)
        
        # 简体中文
        self.action_cn = QAction(self.config.get_text("menu_lang_cn"), self, checkable=True)
        self.action_cn.setChecked(self.config.current_lang == "cn")
        self.action_cn.triggered.connect(lambda: self.switch_language("cn"))
        lang_group.addAction(self.action_cn)
        
        # 英文
        self.action_en = QAction(self.config.get_text("menu_lang_en"), self, checkable=True)
        self.action_en.setChecked(self.config.current_lang == "en")
        self.action_en.triggered.connect(lambda: self.switch_language("en"))
        lang_group.addAction(self.action_en)
        
        # 日文
        self.action_ja = QAction(self.config.get_text("menu_lang_ja"), self, checkable=True)
        self.action_ja.setChecked(self.config.current_lang == "ja")
        self.action_ja.triggered.connect(lambda: self.switch_language("ja"))
        lang_group.addAction(self.action_ja)

        # === 新增：繁体中文 ===
        self.action_tw = QAction(self.config.get_text("menu_lang_tw"), self, checkable=True)
        self.action_tw.setChecked(self.config.current_lang == "tw")
        self.action_tw.triggered.connect(lambda: self.switch_language("tw"))
        lang_group.addAction(self.action_tw)

        # === 新增：德语 ===
        self.action_de = QAction(self.config.get_text("menu_lang_de"), self, checkable=True)
        self.action_de.setChecked(self.config.current_lang == "de")
        self.action_de.triggered.connect(lambda: self.switch_language("de"))
        lang_group.addAction(self.action_de)
        # ======================

        # === 新增：俄语 ===
        self.action_ru = QAction(self.config.get_text("menu_lang_ru"), self, checkable=True)
        self.action_ru.setChecked(self.config.current_lang == "ru")
        self.action_ru.triggered.connect(lambda: self.switch_language("ru"))
        lang_group.addAction(self.action_ru)
        
        # === 新增：韩语 ===
        self.action_ko = QAction(self.config.get_text("menu_lang_ko"), self, checkable=True)
        self.action_ko.setChecked(self.config.current_lang == "ko")
        self.action_ko.triggered.connect(lambda: self.switch_language("ko"))
        lang_group.addAction(self.action_ko)
        
        # === 新增：西班牙语 ===
        self.action_es = QAction(self.config.get_text("menu_lang_es"), self, checkable=True)
        self.action_es.setChecked(self.config.current_lang == "es")
        self.action_es.triggered.connect(lambda: self.switch_language("es"))
        lang_group.addAction(self.action_es)

        # 将所有的 Action 按照顺序添加到菜单栏
        self.lang_menu.addAction(self.action_en) # 英语
        self.lang_menu.addAction(self.action_ru) # 俄语
        self.lang_menu.addAction(self.action_de) # 德语
        self.lang_menu.addAction(self.action_ja) # 日语
        self.lang_menu.addAction(self.action_ko) # 韩语
        self.lang_menu.addAction(self.action_es) # 西班牙语
        self.lang_menu.addAction(self.action_cn) # 简体
        self.lang_menu.addAction(self.action_tw) # 繁体放到简体旁边
      

        # 4. 帮助菜单
        self.help_menu = self.menu_bar.addMenu("")
        self.about_action = QAction("", self)
        self.help_menu.addAction(self.about_action)

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_content = QWidget()
        self.scroll_content.setObjectName("scroll_content")
        self.scroll_layout = QVBoxLayout(self.scroll_content)
        self.scroll_area.setWidget(self.scroll_content)
        main_layout.addWidget(self.scroll_area, stretch=3)

        self._render_modules(self.data_tree.get("module_groups", []))
        self.scroll_layout.addStretch()

        # ====== 1. 修改：灵感提示区域加入“应用”按钮 ======
        insp_layout = QVBoxLayout()
        insp_header_layout = QHBoxLayout()
        
        self.insp_label = QLabel()
        self.insp_label.setObjectName("output_label")
        
        self.apply_insp_btn = QPushButton()
        self.apply_insp_btn.setObjectName("apply_insp_btn")
        self.apply_insp_btn.setVisible(False) # 默认隐藏，只有生成了灵感才显示
        
        insp_header_layout.addWidget(self.insp_label)
        insp_header_layout.addWidget(self.apply_insp_btn)
        insp_header_layout.addStretch() # 把标签和按钮挤到左边
        
        self.insp_text = QTextEdit()
        self.insp_text.setObjectName("insp_text")
        self.insp_text.setMaximumHeight(65)
        self.insp_text.setReadOnly(True)
        
        insp_layout.addLayout(insp_header_layout)
        insp_layout.addWidget(self.insp_text)
        main_layout.addLayout(insp_layout)
        # =================================================


        # ====== 新增：自由补充提示词输入框 ======
        custom_prompt_layout = QVBoxLayout()
        self.custom_prompt_label = QLabel()
        self.custom_prompt_label.setObjectName("output_label")
        self.custom_prompt_input = QLineEdit()
        self.custom_prompt_input.setPlaceholderText("masterpiece, best quality, 1girl, ...")
        custom_prompt_layout.addWidget(self.custom_prompt_label)
        custom_prompt_layout.addWidget(self.custom_prompt_input)
        main_layout.addLayout(custom_prompt_layout)
        # =======================================

        # 2. 原有的双栏输出框
        output_container = QWidget()
        output_layout = QHBoxLayout(output_container)
        output_layout.setContentsMargins(0, 0, 0, 0)

        left_layout = QVBoxLayout()
        self.left_label = QLabel()
        self.left_label.setObjectName("output_label")
        self.output_text_local = QTextEdit()
        left_layout.addWidget(self.left_label)
        left_layout.addWidget(self.output_text_local)

        right_layout = QVBoxLayout()
        self.right_label = QLabel()
        self.right_label.setObjectName("output_label")
        self.output_text_en = QTextEdit()
        right_layout.addWidget(self.right_label)
        right_layout.addWidget(self.output_text_en)

        output_layout.addLayout(left_layout)
        output_layout.addLayout(right_layout)
        main_layout.addWidget(output_container, stretch=1)
        
        # 3. 底部大按钮
        bottom_layout = QHBoxLayout()
        self.global_random_btn = QPushButton()
        self.global_random_btn.setObjectName("global_random_btn")
        self.global_random_btn.setMinimumHeight(45)
        
        self.generate_btn = QPushButton()
        self.generate_btn.setObjectName("generate_btn")
        self.generate_btn.setMinimumHeight(45)

        self.copy_btn = QPushButton()
        self.copy_btn.setObjectName("copy_btn")
        self.copy_btn.setMinimumHeight(45)

        bottom_layout.addWidget(self.global_random_btn, stretch=15)
        bottom_layout.addWidget(self.generate_btn, stretch=20)
        bottom_layout.addWidget(self.copy_btn, stretch=10)
        
        main_layout.addLayout(bottom_layout)

    def _bind_events(self):
        self.generate_btn.clicked.connect(self.generate_prompt)
        self.global_random_btn.clicked.connect(self.trigger_global_random)
        self.copy_btn.clicked.connect(self.copy_to_clipboard)
        self.apply_insp_btn.clicked.connect(self.apply_inspiration) # 新增绑定
    
    def switch_theme(self, theme_name):
        import os
        filepath = os.path.join(self.config.assets_dir, f'theme_{theme_name}.qss')
        if os.path.exists(filepath):
            with open(filepath, 'r', encoding='utf-8') as f:
                self.setStyleSheet(f.read())

    def switch_language(self, lang_code):
        self.config.load_language(lang_code)
        self.retranslate_ui()

    def retranslate_ui(self):
        # 新增的菜单翻译
        self.new_action.setText(self.config.get_text("menu_new"))
        self.edit_current_action.setText(self.config.get_text("menu_edit_current"))
        self.edit_other_action.setText(self.config.get_text("menu_edit_other"))
        self.custom_prompt_label.setText(self.config.get_text("lbl_custom_prompt"))

        self.file_menu.setTitle(self.config.get_text("menu_file"))
        # 新增主题相关的翻译
        self.theme_menu.setTitle(self.config.get_text("menu_theme"))
        self.action_theme_dark.setText(self.config.get_text("theme_dark"))
        self.action_theme_light.setText(self.config.get_text("theme_light"))
        self.action_theme_dracula.setText(self.config.get_text("theme_dracula"))

        self.open_action.setText(self.config.get_text("menu_load"))
        self.exit_action.setText(self.config.get_text("menu_exit"))
        
        self.settings_menu.setTitle(self.config.get_text("menu_settings"))
        self.lang_menu.setTitle(self.config.get_text("menu_lang"))
        
        self.help_menu.setTitle(self.config.get_text("menu_help"))
        self.about_action.setText(self.config.get_text("menu_about"))

        self.left_label.setText(self.config.get_text("lbl_local_preview"))
        self.right_label.setText(self.config.get_text("lbl_en_prompt"))
        self.output_text_local.setPlaceholderText(self.config.get_text("msg_placeholder_local"))
        self.output_text_en.setPlaceholderText(self.config.get_text("msg_placeholder_en"))
        
        self.global_random_btn.setText(self.config.get_text("btn_global_random"))
        self.generate_btn.setText(self.config.get_text("btn_generate"))
        self.copy_btn.setText(self.config.get_text("btn_copy"))

        self.insp_label.setText(self.config.get_text("lbl_inspiration"))
        self.insp_text.setPlaceholderText(self.config.get_text("msg_placeholder_insp"))
        self.apply_insp_btn.setText(self.config.get_text("btn_apply_insp")) # 翻译应用按钮

        for btn in self.scroll_content.findChildren(QPushButton, "btn_random_group"):
            btn.setText(self.config.get_text("btn_random_group"))
            
        if self.output_text_en.toPlainText().startswith("⚠️"):
            self.output_text_en.setText(self.config.get_text("msg_no_tags"))
            self.output_text_local.setText(self.config.get_text("msg_no_tags"))

    def trigger_global_random(self):
        inspiration_en = []
        inspiration_local = []
        self.last_inspired_widgets.clear() # 清空上一次记录
        
        all_groups = self.scroll_content.findChildren(ModuleGroupWidget)
        for group in all_groups:
            if group.content_widget.isVisible():
                all_tags = group.content_widget.findChildren(TagWidget)
                if not all_tags:
                    continue
                
                grouped_tags = defaultdict(list)
                for btn in all_tags:
                    grouped_tags[btn.category].append(btn)
                
                for category, btns in grouped_tags.items():
                    picked_btn = random.choice(btns)
                    # 记录被选中的对象，备用
                    self.last_inspired_widgets.append(picked_btn) 
                    inspiration_en.append(picked_btn.get_formatted_tag())
                    inspiration_local.append(picked_btn.get_formatted_display())
        
        if inspiration_en:
            insp_str = f"🌐 {', '.join(inspiration_local)}\n📄 {', '.join(inspiration_en)}"
            self.insp_text.setText(insp_str)
            self.apply_insp_btn.setVisible(True) # 显示应用按钮
            self.statusBar().showMessage(self.config.get_text("msg_random_done"), 3000)

    def apply_inspiration(self):
        """核心：将灵感标签强制应用到界面状态中"""
        if not self.last_inspired_widgets:
            return
            
        # 1. 一键清空当前主界面所有的选中状态
        all_tag_widgets = self.scroll_content.findChildren(TagWidget)
        for widget in all_tag_widgets:
            widget.setChecked(False)
            
        # 2. 将之前后台记录的标签设为选中状态
        for widget in self.last_inspired_widgets:
            widget.setChecked(True)
            
        # 3. 自动触发一次生成，更新底部的结果框
        self.generate_prompt()
        self.statusBar().showMessage(self.config.get_text("msg_insp_applied"), 3000)

    def generate_prompt(self):
        selected_tags_en = []
        selected_tags_local = []
        
        # 1. 抓取自由补充框的内容 (核心拼接逻辑)
        custom_text = self.custom_prompt_input.text().strip()
        if custom_text:
            selected_tags_en.append(custom_text)
            selected_tags_local.append(custom_text)
            
        # 2. 收集按钮标签
        all_tag_widgets = self.scroll_content.findChildren(TagWidget)
        for widget in all_tag_widgets:
            if widget.isChecked():
                selected_tags_en.append(widget.get_formatted_tag())
                selected_tags_local.append(widget.get_formatted_display())
                
        # 3. 输出
        if selected_tags_en:
            self.output_text_en.setText(", ".join(selected_tags_en))
            self.output_text_local.setText(", ".join(selected_tags_local))
        else:
            self.output_text_en.setText(self.config.get_text("msg_no_tags"))
            self.output_text_local.setText(self.config.get_text("msg_no_tags"))

    def copy_to_clipboard(self):
        text_to_copy = self.output_text_en.toPlainText()
        if text_to_copy and not text_to_copy.startswith("⚠️"):
            clipboard = QApplication.clipboard()
            clipboard.setText(text_to_copy)
            self.statusBar().showMessage(self.config.get_text("msg_copied"), 4000)

    def _render_modules(self, module_groups):
        for group in module_groups:
            group_widget = ModuleGroupWidget(group["module_name"], group.get("is_open", True))
            for sub_module in group.get("sub_modules", []):
                sub_name = sub_module.get("sub_module_name", "默认分类")
                tags = sub_module.get("tags", {})
                for display_name, tag_value in tags.items():
                    btn = TagWidget(display_name, tag_value, category=sub_name)
                    group_widget.add_tag(btn)
            self.scroll_layout.addWidget(group_widget)
    
    def _clear_modules(self):
        """清空当前滚动区域内的所有旧模块和占位弹簧"""
        # 倒序遍历并删除布局中的所有元素，防止正序删除导致的索引偏移
        for i in reversed(range(self.scroll_layout.count())):
            item = self.scroll_layout.itemAt(i)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater() # 安全销毁组件
            else:
                self.scroll_layout.removeItem(item)

    def load_new_dict(self, file_path=None):
        # 如果没有传 file_path，就弹出对话框让用户选
        if not file_path:
            default_dir = self.config.assets_dir.replace("assets", "data")
            if not os.path.exists(default_dir): default_dir = ""
            file_path, _ = QFileDialog.getOpenFileName(
                self, self.config.get_text("menu_load"), default_dir, "JSON Files (*.json);;All Files (*)")

        if file_path:
            try:
                parser = DataParser()
                self.data_tree = parser.parse(file_path)
                self.setWindowTitle(self.data_tree.get("project_name", "Prompt-generation"))
                self._clear_modules()
                self._render_modules(self.data_tree.get("module_groups", []))
                self.scroll_layout.addStretch()
                self.output_text_local.clear()
                self.output_text_en.clear()
                self.insp_text.clear()
                self.apply_insp_btn.setVisible(False)
                self.last_inspired_widgets.clear()
                filename = os.path.basename(file_path)
                self.statusBar().showMessage(f"✅ Loaded: {filename}", 4000)
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load library file:\n{str(e)}")
    
    def new_library(self):
        """新建词库：传入一个干净的空字典"""
        empty_data = {"project_name": "New_Library", "module_groups": []}
        editor = LibraryEditor(empty_data, self)
        if editor.exec():
            self.load_new_dict(editor.saved_path)

    def edit_current(self):
        """编辑当前：直接传入内存中正在使用的词库数据"""
        editor = LibraryEditor(self.data_tree, self)
        if editor.exec():
            self.load_new_dict(editor.saved_path)

    def edit_other(self):
        """选文件编辑：先弹出选择框，解析后直接喂给编辑器，不污染当前主界面"""
        default_dir = self.config.assets_dir.replace("assets", "data")
        if not os.path.exists(default_dir): default_dir = ""
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.config.get_text("menu_edit_other"), default_dir, "JSON Files (*.json);;All Files (*)")
        
        if file_path:
            try:
                from core.parser import DataParser # 确保能解析
                parser = DataParser()
                target_data = parser.parse(file_path)
                
                # 把解析出的新数据扔进编辑器
                editor = LibraryEditor(target_data, self)
                if editor.exec():
                    self.load_new_dict(editor.saved_path) # 如果保存了，主界面就同步加载它
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Failed to load file for editing:\n{str(e)}")