# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ctrl_Dia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QDialog, QWidget


class Ui_ctrl_win(object):
    def setupUi(self, ctrl_win):
        ctrl_win.setObjectName("ctrl_win")
        ctrl_win.resize(400, 243)
        self.label = QtWidgets.QLabel(ctrl_win)
        self.label.setGeometry(QtCore.QRect(30, 10, 181, 61))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.splitter = QtWidgets.QSplitter(ctrl_win)
        self.splitter.setGeometry(QtCore.QRect(171, 71, 138, 151))
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.label_2 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.splitter)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(14)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.splitter_2 = QtWidgets.QSplitter(ctrl_win)
        self.splitter_2.setGeometry(QtCore.QRect(330, 70, 51, 151))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.pushButton_1 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_1.setText("")
        self.pushButton_1.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_2.setText("")
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.splitter_2)
        self.pushButton_3.setText("")
        self.pushButton_3.setObjectName("pushButton_3")

        self.retranslateUi(ctrl_win)
        self.pushButton_1.clicked.connect(self.but_click)
        self.pushButton_2.clicked.connect(self.but2_click)
        self.pushButton_3.clicked.connect(self.but3_click)
        QtCore.QMetaObject.connectSlotsByName(ctrl_win)

    def retranslateUi(self, ctrl_win):
        _translate = QtCore.QCoreApplication.translate
        ctrl_win.setWindowTitle(_translate("Hello!", "Hello!"))
        self.label.setText(_translate("ctrl_win", "您要的是？"))
        self.label_2.setText(_translate("ctrl_win", "打个卡就成"))
        self.label_3.setText(_translate("ctrl_win", "看看谁迟到了"))
        self.label_4.setText(_translate("ctrl_win", "今天开除谁呢"))

    def but_click(self):
        msgBox1 = QMessageBox()
        msgBox1.setStyleSheet("QLabel{"
                              # "min-width: 200px;"
                              # "min-height: 70px; "
                              "font:18px"
                              "}")
        msgBox1.setWindowTitle("开工！")
        msgBox1.setText("打卡成功！")
        msgBox1.exec()

    def but2_click(self):
        msgBox = QMessageBox()
        msgBox.setStyleSheet("QLabel{"
                              # "min-width: 200px;"
                              # "min-height: 80px; "
                              "font:18px"
                              "}")
        msgBox.setWindowTitle("注意")
        msgBox.setText('输入的格式应类似于：\n\n2022-10-11 12:34:56')
        msgBox.exec()

        from .search_time import Ui_Dialog
        time_Dia = QDialog()
        time_win = Ui_Dialog()
        time_win.setupUi(time_Dia)
        time_Dia.exec()

    def but3_click(self):
        from .add_del import Ui_Dialog
        add_del_Dia = QDialog()
        add_del_win = Ui_Dialog()
        add_del_win.setupUi(add_del_Dia)
        add_del_Dia.exec()