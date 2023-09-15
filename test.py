"""

setCellWidget:将控件放到单元格
setItem: 将文本放到单元格
setStyleSheet: 设置控件的样式(QSS)
在单元格中放置控件
"""

from PyQt5 import QtGui, QtWidgets, QtPrintSupport
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import *
from PyQt5.QtPrintSupport import *
import sys

class PlaceControlInCell(QWidget):
    def __init__(self):
        super(PlaceControlInCell, self).__init__()
        self.printer = QPrinter()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("在单元格中放置控件")
        self.resize(430, 300)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)

        layout.addWidget(tableWidget)

        tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重(KG)'])
        textItem = QTableWidgetItem("小明")
        tableWidget.setItem(0, 0, textItem)

        #构造下拉框
        combox = QComboBox()
        #下拉框添加内容
        combox.addItem("男")
        combox.addItem("女")
        # QSS Qt StyleSheet
        #设置下拉框的样式即边距为3
        combox.setStyleSheet('QComboBox(margin:3px)')
        #在表格中放入下拉框控件
        tableWidget.setCellWidget(0, 1, combox)

        modifyButton = QPushButton('修改')
        modifyButton.setDown(True)
        #设置按钮的样式即边距为3
        modifyButton.setStyleSheet("QPushButton(margin:3px)")
        #在表格中放入按钮的控件
        tableWidget.setCellWidget(0, 2, modifyButton)

        self.setLayout(layout)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    main = PlaceControlInCell()
    main.show()

    sys.exit(app.exec_())