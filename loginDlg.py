# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'loginDlg.ui'
#
# Created: Tue Dec 29 17:57:46 2015
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_loginDlg(object):
    def setupUi(self, loginDlg):
        loginDlg.setObjectName("loginDlg")
        loginDlg.resize(272, 148)
        self.layoutWidget = QtGui.QWidget(loginDlg)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 20, 251, 110))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_3 = QtGui.QLabel(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setWeight(75)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.loginPwdLineEdit = QtGui.QLineEdit(self.layoutWidget)
        self.loginPwdLineEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.loginPwdLineEdit.setObjectName("loginPwdLineEdit")
        self.gridLayout.addWidget(self.loginPwdLineEdit, 1, 2, 1, 1)
        self.label = QtGui.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.loginBtn = QtGui.QPushButton(self.layoutWidget)
        self.loginBtn.setObjectName("loginBtn")
        self.gridLayout.addWidget(self.loginBtn, 2, 2, 1, 1)
        self.userComboBox = QtGui.QComboBox(self.layoutWidget)
        self.userComboBox.setObjectName("userComboBox")
        self.gridLayout.addWidget(self.userComboBox, 0, 1, 1, 2)
        self.label_2 = QtGui.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 2)
        self.verticalLayout.addLayout(self.gridLayout)

        self.retranslateUi(loginDlg)
        QtCore.QMetaObject.connectSlotsByName(loginDlg)

    def retranslateUi(self, loginDlg):
        loginDlg.setWindowTitle(QtGui.QApplication.translate("loginDlg", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("loginDlg", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("loginDlg", "User:", None, QtGui.QApplication.UnicodeUTF8))
        self.loginBtn.setText(QtGui.QApplication.translate("loginDlg", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(
            QtGui.QApplication.translate("loginDlg", "Password:", None, QtGui.QApplication.UnicodeUTF8))
