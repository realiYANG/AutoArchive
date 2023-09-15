# coding=utf-8
import os
import random
import shutil
import socket
import sys
import threading
import time
from datetime import datetime, timedelta

import numpy as np
import openpyxl
import pandas as pd
import xlrd
import xlwings as xw
import xlwt
from xlutils.copy import copy
from docx import Document
from docx.enum.table import WD_CELL_VERTICAL_ALIGNMENT
from docx.enum.text import WD_PARAGRAPH_ALIGNMENT
from docx.enum.text import WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.shared import Cm, Inches, Pt, RGBColor
from openpyxl import load_workbook
from PIL import Image
from PyQt5.Qt import QPoint, QPropertyAnimation, QEasingCurve, QAbstractAnimation
from PyQt5 import QtCore, QtGui, QtWidgets, QtNetwork
from PyQt5.QtCore import QDate, QTime, QBasicTimer, QDateTime, Qt, QTimer, QCoreApplication
from PyQt5.QtPrintSupport import QPageSetupDialog, QPrintDialog, QPrinter
from PyQt5.QtWidgets import (QApplication, QColorDialog, QDialog, QFileDialog,
                             QFontDialog, QLabel, QLineEdit, QMainWindow,
                             QMessageBox, QPushButton, QRadioButton,
                             QTableWidgetItem, QTextEdit, QWidget, QStyleFactory)
from CLASSES.Ui_AutoArchiveUI import Ui_MainWindow

class Main_window(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(Main_window, self).__init__()
        self.setupUi(self)
        self.statusBar().showMessage('Ready')
        # self.setWindowOpacity(1.0)
        self.setObjectName("mainWindow")
        # qss = "QMainWindow#mainWindow{background-color:black;}"
        self.main_initialization()

    def main_initialization(self):
        # 防止上传不能保存空文件夹的bug
        dir1_path = '.\\WorkSpace\\bg'
        dir2_path = '.\\WorkSpace\\mit24'
        dir3_path = '.\\WorkSpace\\报告生成工区\\储层表'
        dir4_path = '.\\WorkSpace\\报告生成工区\\储层图'
        dir5_path = '.\\WorkSpace\\报告生成工区\\胶结差图'
        dir6_path = '.\\WorkSpace\\分层和成果表工区'
        dir7_path = '.\\WorkSpace\\合并统计工区'
        dir8_path = '.\\WorkSpace'
        dir_paths = [dir1_path, dir2_path, dir3_path, dir4_path, dir5_path, dir6_path, dir7_path, dir8_path]
        for item in dir_paths:
            if not os.path.exists(item):
                os.makedirs(item)
                print(item, ' 已创建。')

        # 水泥胶结评价模块初始化
        ###################################################
        self.pushButton.clicked.connect(self.read_raw_info_docx)
        self.pushButton.setToolTip('请确保原始记录登记表格式正确')
        self.pushButton_53.clicked.connect(self.automate_table_helper)  # 智能补充解释评价顶底深度
        self.pushButton_53.setToolTip('成果表放置后该按钮才有用')
        self.pushButton_3.clicked.connect(self.generate_txt_file)
        self.pushButton_3.setToolTip('生成可导入LEAD4.0的TXT井信息文件')
        self.pushButton_67.clicked.connect(self.result_table_process_in_report_module)  # 成果表规范化