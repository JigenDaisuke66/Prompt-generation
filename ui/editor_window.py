import os
import json
from PyQt6.QtWidgets import (QDialog, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, 
                             QTreeWidget, QTreeWidgetItem, QTableWidget, 
                             QTableWidgetItem, QPushButton, QMessageBox, QAbstractItemView,
                             QFileDialog)
from PyQt6.QtCore import Qt
from core.config_manager import ConfigManager

class LibraryEditor(QDialog):
    def __init__(self, data_tree, parent=None):
        super().__init__(parent)
        self.config = ConfigManager()
        self.data_tree = data_tree
        self.setWindowTitle(self.config.get_text("editor_title"))
        self.resize(800, 500)
        
        self.setup_ui()
        self.load_data_to_tree()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)
        
        splitter = QSplitter(Qt.Orientation.Horizontal)
        
        # === 左侧：树状分类 ===
        left_widget = QWidget()
        left_layout = QVBoxLayout(left_widget)
        left_layout.setContentsMargins(0,0,0,0)
        
        self.tree = QTreeWidget()
        self.tree.setHeaderHidden(True)
        self.tree.itemSelectionChanged.connect(self.on_tree_select)
        
        tree_btn_layout = QHBoxLayout()
        self.btn_add_group = QPushButton(self.config.get_text("btn_add_group"))
        self.btn_add_sub = QPushButton(self.config.get_text("btn_add_sub"))
        self.btn_del_node = QPushButton(self.config.get_text("btn_del_node"))
        
        self.btn_add_group.clicked.connect(self.add_group)
        self.btn_add_sub.clicked.connect(self.add_sub)
        self.btn_del_node.clicked.connect(self.del_node)
        
        tree_btn_layout.addWidget(self.btn_add_group)
        tree_btn_layout.addWidget(self.btn_add_sub)
        tree_btn_layout.addWidget(self.btn_del_node)
        
        left_layout.addWidget(self.tree)
        left_layout.addLayout(tree_btn_layout)
        
        # === 右侧：表格编辑 ===
        right_widget = QWidget()
        right_layout = QVBoxLayout(right_widget)
        right_layout.setContentsMargins(0,0,0,0)
        
        self.table = QTableWidget(0, 2)
        self.table.setHorizontalHeaderLabels([self.config.get_text("header_display"), self.config.get_text("header_value")])
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.setSelectionBehavior(QAbstractItemView.SelectionBehavior.SelectRows)
        self.table.cellChanged.connect(self.on_cell_changed)
        
        table_btn_layout = QHBoxLayout()
        self.btn_add_tag = QPushButton(self.config.get_text("btn_add_tag"))
        self.btn_del_tag = QPushButton(self.config.get_text("btn_del_tag"))
        
        self.btn_add_tag.clicked.connect(self.add_tag)
        self.btn_del_tag.clicked.connect(self.del_tag)
        
        table_btn_layout.addStretch()
        table_btn_layout.addWidget(self.btn_add_tag)
        table_btn_layout.addWidget(self.btn_del_tag)
        
        right_layout.addWidget(self.table)
        right_layout.addLayout(table_btn_layout)
        
        splitter.addWidget(left_widget)
        splitter.addWidget(right_widget)
        splitter.setSizes([300, 500])
        main_layout.addWidget(splitter)
        
        # === 底部保存按钮 ===
        self.btn_save = QPushButton(self.config.get_text("btn_save_apply"))
        self.btn_save.setObjectName("generate_btn") # 复用蓝色大按钮样式
        self.btn_save.setMinimumHeight(40)
        self.btn_save.clicked.connect(self.save_and_apply)
        main_layout.addWidget(self.btn_save)

    def load_data_to_tree(self):
        self.tree.blockSignals(True)
        self.tree.clear()
        groups = self.data_tree.get("module_groups", [])
        for g in groups:
            g_item = QTreeWidgetItem(self.tree, [g.get("module_name", "New Module")])
            g_item.setFlags(g_item.flags() | Qt.ItemFlag.ItemIsEditable)
            for s in g.get("sub_modules", []):
                s_item = QTreeWidgetItem(g_item, [s.get("sub_module_name", "New Sub")])
                s_item.setFlags(s_item.flags() | Qt.ItemFlag.ItemIsEditable)
                # 将 tags 数据绑定在子节点上
                s_item.setData(0, Qt.ItemDataRole.UserRole, s.get("tags", {}).copy())
        self.tree.expandAll()
        self.tree.blockSignals(False)

    def on_tree_select(self):
        self.table.blockSignals(True)
        self.table.setRowCount(0)
        item = self.tree.currentItem()
        
        # 只有选中的是第二层（子模块），才显示表格
        if item and item.parent():
            tags = item.data(0, Qt.ItemDataRole.UserRole)
            if not tags: tags = {}
            for display, val in tags.items():
                self.add_table_row(display, val)
                
        self.table.blockSignals(False)

    def add_table_row(self, display="", val=""):
        row = self.table.rowCount()
        self.table.insertRow(row)
        self.table.setItem(row, 0, QTableWidgetItem(display))
        self.table.setItem(row, 1, QTableWidgetItem(val))

    def on_cell_changed(self, row, col):
        """核心魔法：解决英文用户需要输入两次的痛点，以及实时保存数据到节点"""
        # 1. 自动填充逻辑
        if col == 0:
            display_item = self.table.item(row, 0)
            val_item = self.table.item(row, 1)
            # 如果第一列有字，但第二列为空，自动复制过去
            if display_item and display_item.text().strip():
                if not val_item or not val_item.text().strip():
                    self.table.blockSignals(True)
                    self.table.setItem(row, 1, QTableWidgetItem(display_item.text().strip()))
                    self.table.blockSignals(False)
                    
        # 2. 实时保存回树节点
        item = self.tree.currentItem()
        if item and item.parent():
            new_tags = {}
            for r in range(self.table.rowCount()):
                d_item = self.table.item(r, 0)
                v_item = self.table.item(r, 1)
                if d_item and v_item and d_item.text().strip():
                    new_tags[d_item.text().strip()] = v_item.text().strip()
            item.setData(0, Qt.ItemDataRole.UserRole, new_tags)

    def add_group(self):
        item = QTreeWidgetItem(self.tree, ["New Module"])
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        self.tree.editItem(item)

    def add_sub(self):
        curr = self.tree.currentItem()
        parent = curr if curr and not curr.parent() else (curr.parent() if curr else None)
        if not parent:
            return QMessageBox.warning(self, "Warning", "Please select a Module first.")
        item = QTreeWidgetItem(parent, ["New Sub-category"])
        item.setFlags(item.flags() | Qt.ItemFlag.ItemIsEditable)
        item.setData(0, Qt.ItemDataRole.UserRole, {})
        parent.setExpanded(True)
        self.tree.editItem(item)

    def del_node(self):
        curr = self.tree.currentItem()
        if curr:
            (curr.parent() or self.tree.invisibleRootItem()).removeChild(curr)

    def add_tag(self):
        curr = self.tree.currentItem()
        if curr and curr.parent():
            self.table.blockSignals(True)
            self.add_table_row("New Tag", "new_tag")
            self.table.blockSignals(False)
            self.on_cell_changed(self.table.rowCount()-1, 0) # 触发保存

    def del_tag(self):
        rows = sorted([r.row() for r in self.table.selectedItems()])
        if rows:
            for r in reversed(rows):
                self.table.removeRow(r)
            self.on_cell_changed(0, 0)

    def save_and_apply(self):
        # 1. 将树重新组装为 JSON 格式
        new_groups = []
        for i in range(self.tree.topLevelItemCount()):
            g_item = self.tree.topLevelItem(i)
            subs = []
            for j in range(g_item.childCount()):
                s_item = g_item.child(j)
                subs.append({
                    "sub_module_name": s_item.text(0),
                    "tags": s_item.data(0, Qt.ItemDataRole.UserRole)
                })
            new_groups.append({
                "module_name": g_item.text(0),
                "is_open": True,
                "sub_modules": subs
            })
            
        self.data_tree["module_groups"] = new_groups
        # 如果是新建的空模板，这里可以顺便给个默认项目名
        project_name = self.data_tree.get("project_name", "My_Custom_Library")
        self.data_tree["project_name"] = project_name
        
        # 2. 弹出系统的“另存为”对话框，让用户自己定名字
        default_dir = self.config.assets_dir.replace("assets", "data")
        if not os.path.exists(default_dir):
            default_dir = ""
            
        # 默认文件名会自动带上项目名称
        default_save_path = os.path.join(default_dir, f"{project_name}.json")
        
        save_path, _ = QFileDialog.getSaveFileName(
            self,
            self.config.get_text("title_save_as"),
            default_save_path,
            "JSON Files (*.json)"
        )

        # 3. 用户选择了保存路径后执行写入
        if save_path:
            try:
                with open(save_path, 'w', encoding='utf-8') as f:
                    json.dump(self.data_tree, f, ensure_ascii=False, indent=2)
                self.saved_path = save_path # 记录最终保存的路径传给主窗口
                self.accept()
            except Exception as e:
                QMessageBox.critical(self, "Error", f"Save Failed: {str(e)}")