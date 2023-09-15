import os
import shutil
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QTableWidgetItem, QLabel, QLineEdit, QPushButton, QFileDialog, QMessageBox


class FileRenamer(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('File Renamer')
        self.setGeometry(100, 100, 800, 400)

        # Layouts
        main_layout = QVBoxLayout()
        table_layout = QHBoxLayout()
        action_layout = QHBoxLayout()

        # File table
        self.file_table = QTableWidget()
        self.file_table.setColumnCount(4)
        self.file_table.setHorizontalHeaderLabels(['Name', 'Size', 'Type', 'Modified'])
        self.file_table.setColumnWidth(0, 300)
        self.file_table.setColumnWidth(1, 100)
        self.file_table.setColumnWidth(2, 100)
        self.file_table.setColumnWidth(3, 200)

        # Name editor
        name_label = QLabel('New name:')
        self.name_editor = QLineEdit()

        # Move editor
        move_label = QLabel('Move to:')
        self.move_editor = QLineEdit()

        # Buttons
        self.rename_button = QPushButton('Rename')
        self.move_button = QPushButton('Move')
        self.undo_button = QPushButton('Undo')

        self.rename_button.clicked.connect(self.rename_file)
        self.move_button.clicked.connect(self.move_file)
        self.undo_button.clicked.connect(self.undo_action)

        table_layout.addWidget(self.file_table)
        action_layout.addWidget(name_label)
        action_layout.addWidget(self.name_editor)
        action_layout.addWidget(move_label)
        action_layout.addWidget(self.move_editor)
        action_layout.addWidget(self.rename_button)
        action_layout.addWidget(self.move_button)
        action_layout.addWidget(self.undo_button)

        main_layout.addLayout(table_layout)
        main_layout.addLayout(action_layout)

        self.setLayout(main_layout)

        self.show()

    def load_files(self, path):
        files = os.listdir(path)
        self.file_table.setRowCount(len(files))

        for row, file_name in enumerate(files):
            file_path = os.path.join(path, file_name)
            file_info = os.stat(file_path)

            self.file_table.setItem(row, 0, QTableWidgetItem(file_name))
            self.file_table.setItem(row, 1, QTableWidgetItem(str(file_info.st_size)))
            self.file_table.setItem(row, 2, QTableWidgetItem(file_path.split('.')[-1]))
            self.file_table.setItem(row, 3, QTableWidgetItem(str(file_info.st_mtime)))

    def rename_file(self):
        # TODO: Add your rename logic here
        QMessageBox.information(self, 'Info', 'Rename is not implemented yet.')

    def move_file(self):
        # TODO: Add your move logic here
        QMessageBox.information(self, 'Info', 'Move is not implemented yet.')

    def undo_action(self):
        # TODO: Add your undo logic here
        QMessageBox.information(self, 'Info', 'Undo is not implemented yet.')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file_renamer = FileRenamer()
    folder_path = QFileDialog.getExistingDirectory(file_renamer, 'Select Folder')
    if folder_path:
        file_renamer.load_files(folder_path)
    else:
        sys.exit()
    sys.exit(app.exec_())
