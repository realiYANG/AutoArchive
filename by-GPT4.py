import sys
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QSplitter, QListView, QPushButton, QFileDialog, QLineEdit, QGroupBox
from PyQt5.QtCore import QStringListModel

class FileOrganizer(QWidget):
    def __init__(self):
        super().__init__()

        # 设置主窗口属性
        self.setWindowTitle('File Organizer')
        self.setGeometry(300, 300, 800, 600)

        # 创建左右半屏
        left_half = QWidget()
        right_half = QWidget()

        # 设置左半屏
        left_layout = QVBoxLayout()
        left_half.setLayout(left_layout)

        # 文件列表
        self.file_list = QListView()
        self.file_model = QStringListModel()
        self.file_list.setModel(self.file_model)
        left_layout.addWidget(self.file_list)

        # 添加文件按钮
        add_file_button = QPushButton('添加文件')
        add_file_button.clicked.connect(self.add_file)
        left_layout.addWidget(add_file_button)

        # 设置右半屏
        right_layout = QVBoxLayout()
        right_half.setLayout(right_layout)

        # 右半屏内的四个区域
        self.bg_folder = self.create_folder_area('BG')
        self.pdf_folder = self.create_folder_area('PDF')
        self.data_folder = self.create_folder_area('Data')
        self.yssj_folder = self.create_folder_area('YSSJ')

        right_layout.addWidget(self.bg_folder)
        right_layout.addWidget(self.pdf_folder)
        right_layout.addWidget(self.data_folder)
        right_layout.addWidget(self.yssj_folder)

        # 创建并设置分隔器
        splitter = QSplitter()
        splitter.addWidget(left_half)
        splitter.addWidget(right_half)

        main_layout = QHBoxLayout()
        main_layout.addWidget(splitter)
        self.setLayout(main_layout)

    def create_folder_area(self, label):
        group_box = QGroupBox(label)

        layout = QVBoxLayout()

        rename_edit = QLineEdit()
        layout.addWidget(rename_edit)

        move_button = QPushButton(f'移动到 {label}')
        move_button.clicked.connect(lambda: self.move_file(rename_edit.text(), label))
        layout.addWidget(move_button)

        group_box.setLayout(layout)

        return group_box

    def add_file(self):
        file_name, _ = QFileDialog.getOpenFileName(self, '选择文件')
        if file_name:
            self.file_model.setStringList(self.file_model.stringList() + [file_name])

    def move_file(self, new_name, folder):
        current_index = self.file_list.currentIndex()
        if not current_index.isValid():
            return

        old_path = self.file_model.data(current_index)
        new_folder = os.path.join(os.path.dirname(old_path), folder)
        os.makedirs(new_folder, exist_ok=True)

        new_file_name = os.path.splitext(os.path.basename(old_path))[0] + new_name + os.path.splitext(old_path)[1]
        new_path = os.path.join(new_folder, new_file_name)

        os.rename(old_path, new_path)

        # 更新文件列表
        files = self.file_model.stringList()
        files.remove(old_path)
        self.file_model.setStringList(files)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileOrganizer()
    ex.show()
    sys.exit(app.exec_())