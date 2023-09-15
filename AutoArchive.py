import os
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel


class FolderCreator(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Folder Creator")
        self.layout = QVBoxLayout()
        self.label = QLabel("点击按钮创建文件夹结构")
        self.button = QPushButton("创建文件夹")
        self.button.clicked.connect(self.create_folders)

        self.layout.addWidget(self.label)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

    def create_folders(self):
        root_folder = "./新建文件夹"
        folders = ["bg", "mit24", "midk", "yssj"]
        subfolders = {
            "mit24": ["data", "map"],
            "midk": ["data", "map"]
        }

        try:
            # 创建根文件夹
            os.makedirs(root_folder)

            # 创建子文件夹
            for folder in folders:
                folder_path = os.path.join(root_folder, folder)
                os.makedirs(folder_path)

                # 创建子文件夹
                if folder in subfolders:
                    for subfolder in subfolders[folder]:
                        subfolder_path = os.path.join(folder_path, subfolder)
                        os.makedirs(subfolder_path)

            self.label.setText("文件夹结构创建成功！")
        except OSError as e:
            self.label.setText(f"创建文件夹结构时出现错误：{e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = FolderCreator()
    window.show()
    sys.exit(app.exec_())