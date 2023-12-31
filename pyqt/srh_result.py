# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'srh_result.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
import csv
import json
import winreg

import requests
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox


class Ui_Dialog(object):
    def setupUi(self, Dialog, inf):
        self.inf = inf

        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 293)
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setGeometry(QtCore.QRect(10, 50, 381, 231))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(12)
        self.listWidget.setFont(font)
        self.listWidget.setObjectName("listWidget")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 10, 131, 31))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(290, 10, 71, 31))
        font = QtGui.QFont()
        font.setFamily("Cascadia Code")
        font.setPointSize(11)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.save_but)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "search_result"))
        self.label.setText(_translate("Dialog", "查询结果："))
        self.pushButton.setText(_translate("Dialog", "保存"))

        self.inf = json.loads(self.inf)
        for key, value in self.inf.items():
            self.listWidget.addItem(key + '\t' + value)
        self.listWidget.show()

    def save_but(self):
        import pandas as pd
        import os
        path = winreg.QueryValueEx(winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                         r'Software\\Microsoft\\Windows\\CurrentVersion\\Explorer\\Shell Folders'),"Desktop")[0]
        with open(os.path.join(path + '\\checkin_inf.csv'), 'w', newline='', encoding='utf-8-sig') as f:
            writer = csv.writer(f)
            writer.writerow(['time', 'name'])
            for key, value in self.inf.items():
                writer.writerow([key, value])
        msgBox = QMessageBox()
        msgBox.setStyleSheet("QLabel{"
                             "min-width: 200px;"
                             "min-height: 80px; "
                             "font:18px"
                             "}")
        msgBox.setWindowTitle("成功！")
        msgBox.setText('csv文件已保存到桌面！')
        msgBox.exec()
