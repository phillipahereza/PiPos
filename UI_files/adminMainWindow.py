# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created: Sat Jan 16 19:32:12 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(735, 551)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/window.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(7, 90, 771, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName("line")
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 120, 691, 381))
        self.tabWidget.setObjectName("tabWidget")
        self.reportsTab = QtGui.QWidget()
        self.reportsTab.setObjectName("reportsTab")
        self.layoutWidget = QtGui.QWidget(self.reportsTab)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 10, 576, 317))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.layoutWidget)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.verticalLayout_5 = QtGui.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtGui.QLabel(self.layoutWidget)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.graphicsView = QtGui.QGraphicsView(self.layoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.verticalLayout_5.addWidget(self.graphicsView)
        self.horizontalLayout_4.addLayout(self.verticalLayout_5)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem)
        self.verticalLayout_4 = QtGui.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_9 = QtGui.QLabel(self.layoutWidget)
        self.label_9.setObjectName("label_9")
        self.verticalLayout_4.addWidget(self.label_9)
        self.todaysSalesLCD = QtGui.QLCDNumber(self.layoutWidget)
        self.todaysSalesLCD.setObjectName("todaysSalesLCD")
        self.verticalLayout_4.addWidget(self.todaysSalesLCD)
        self.calendarWidget = QtGui.QCalendarWidget(self.layoutWidget)
        self.calendarWidget.setObjectName("calendarWidget")
        self.verticalLayout_4.addWidget(self.calendarWidget)
        self.horizontalLayout_4.addLayout(self.verticalLayout_4)
        self.verticalLayout_6.addLayout(self.horizontalLayout_4)
        spacerItem1 = QtGui.QSpacerItem(20, 28, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_6.addItem(spacerItem1)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtGui.QLabel(self.layoutWidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.label_11 = QtGui.QLabel(self.layoutWidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 1, 0, 1, 1)
        self.label_12 = QtGui.QLabel(self.layoutWidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout_3.addWidget(self.label_12, 1, 1, 1, 1)
        self.reportDateFromEdit = QtGui.QDateEdit(self.layoutWidget)
        self.reportDateFromEdit.setDate(QtCore.QDate(2016, 1, 1))
        self.reportDateFromEdit.setObjectName("reportDateFromEdit")
        self.gridLayout_3.addWidget(self.reportDateFromEdit, 2, 0, 1, 1)
        self.reportDateToEdit = QtGui.QDateEdit(self.layoutWidget)
        self.reportDateToEdit.setDate(QtCore.QDate(2016, 1, 1))
        self.reportDateToEdit.setObjectName("reportDateToEdit")
        self.gridLayout_3.addWidget(self.reportDateToEdit, 2, 1, 1, 1)
        self.viewReportsBtn = QtGui.QPushButton(self.layoutWidget)
        self.viewReportsBtn.setObjectName("viewReportsBtn")
        self.gridLayout_3.addWidget(self.viewReportsBtn, 2, 2, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.tabWidget.addTab(self.reportsTab, "")
        self.manageUsersTab = QtGui.QWidget()
        self.manageUsersTab.setObjectName("manageUsersTab")
        self.layoutWidget1 = QtGui.QWidget(self.manageUsersTab)
        self.layoutWidget1.setGeometry(QtCore.QRect(10, 20, 598, 147))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout_5 = QtGui.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtGui.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtGui.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 1)
        self.addUserUnameEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.addUserUnameEdit.setObjectName("addUserUnameEdit")
        self.gridLayout.addWidget(self.addUserUnameEdit, 0, 1, 1, 1)
        self.label_3 = QtGui.QLabel(self.layoutWidget1)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 1, 0, 1, 1)
        self.addUserPwdEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.addUserPwdEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.addUserPwdEdit.setObjectName("addUserPwdEdit")
        self.gridLayout.addWidget(self.addUserPwdEdit, 1, 1, 1, 1)
        self.label_4 = QtGui.QLabel(self.layoutWidget1)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 2, 0, 1, 1)
        self.addUserRptPwdEdit = QtGui.QLineEdit(self.layoutWidget1)
        self.addUserRptPwdEdit.setEchoMode(QtGui.QLineEdit.Password)
        self.addUserRptPwdEdit.setObjectName("addUserRptPwdEdit")
        self.gridLayout.addWidget(self.addUserRptPwdEdit, 2, 1, 1, 1)
        self.addUserBtn = QtGui.QPushButton(self.layoutWidget1)
        self.addUserBtn.setObjectName("addUserBtn")
        self.gridLayout.addWidget(self.addUserBtn, 3, 1, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.horizontalLayout_5.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(58, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.line_2 = QtGui.QFrame(self.layoutWidget1)
        self.line_2.setFrameShape(QtGui.QFrame.VLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.horizontalLayout_5.addWidget(self.line_2)
        spacerItem3 = QtGui.QSpacerItem(118, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem3)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_5 = QtGui.QLabel(self.layoutWidget1)
        self.label_5.setObjectName("label_5")
        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)
        self.label_6 = QtGui.QLabel(self.layoutWidget1)
        self.label_6.setObjectName("label_6")
        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)
        self.userComboBox = QtGui.QComboBox(self.layoutWidget1)
        self.userComboBox.setObjectName("userComboBox")
        self.gridLayout_2.addWidget(self.userComboBox, 1, 1, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(20, 38, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.gridLayout_2.addItem(spacerItem4, 2, 1, 1, 1)
        self.deleteUserBtn = QtGui.QPushButton(self.layoutWidget1)
        self.deleteUserBtn.setObjectName("deleteUserBtn")
        self.gridLayout_2.addWidget(self.deleteUserBtn, 3, 1, 1, 1)
        self.horizontalLayout_5.addLayout(self.gridLayout_2)
        self.tabWidget.addTab(self.manageUsersTab, "")
        self.inventoryTab = QtGui.QWidget()
        self.inventoryTab.setObjectName("inventoryTab")
        self.layoutWidget2 = QtGui.QWidget(self.inventoryTab)
        self.layoutWidget2.setGeometry(QtCore.QRect(20, 30, 635, 283))
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.gridLayout_5 = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_7 = QtGui.QLabel(self.layoutWidget2)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_2.addWidget(self.label_7)
        self.inventorySearchEdit = QtGui.QLineEdit(self.layoutWidget2)
        self.inventorySearchEdit.setObjectName("inventorySearchEdit")
        self.horizontalLayout_2.addWidget(self.inventorySearchEdit)
        self.searchBtn = QtGui.QPushButton(self.layoutWidget2)
        self.searchBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.searchBtn.setIcon(icon1)
        self.searchBtn.setObjectName("searchBtn")
        self.horizontalLayout_2.addWidget(self.searchBtn)
        self.gridLayout_5.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)
        spacerItem5 = QtGui.QSpacerItem(498, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_5.addItem(spacerItem5, 2, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.inventoryAddItemBtn = QtGui.QPushButton(self.layoutWidget2)
        self.inventoryAddItemBtn.setObjectName("inventoryAddItemBtn")
        self.gridLayout_4.addWidget(self.inventoryAddItemBtn, 0, 0, 1, 2)
        self.inventorySaveBtn = QtGui.QPushButton(self.layoutWidget2)
        self.inventorySaveBtn.setObjectName("inventorySaveBtn")
        self.gridLayout_4.addWidget(self.inventorySaveBtn, 1, 0, 1, 1)
        self.inventoryCancelBtn = QtGui.QPushButton(self.layoutWidget2)
        self.inventoryCancelBtn.setObjectName("inventoryCancelBtn")
        self.gridLayout_4.addWidget(self.inventoryCancelBtn, 1, 1, 1, 1)
        self.gridLayout_5.addLayout(self.gridLayout_4, 2, 1, 1, 1)
        self.tableWidget = QtGui.QTableWidget(self.layoutWidget2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.gridLayout_5.addWidget(self.tableWidget, 1, 0, 1, 2)
        self.tabWidget.addTab(self.inventoryTab, "")
        self.layoutWidget3 = QtGui.QWidget(self.centralwidget)
        self.layoutWidget3.setGeometry(QtCore.QRect(20, 20, 708, 70))
        self.layoutWidget3.setObjectName("layoutWidget3")
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.reportsBtn = QtGui.QPushButton(self.layoutWidget3)
        self.reportsBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/statistics.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.reportsBtn.setIcon(icon2)
        self.reportsBtn.setIconSize(QtCore.QSize(54, 54))
        self.reportsBtn.setObjectName("reportsBtn")
        self.horizontalLayout.addWidget(self.reportsBtn)
        self.inventoryBtn = QtGui.QPushButton(self.layoutWidget3)
        self.inventoryBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/images/restock.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.inventoryBtn.setIcon(icon3)
        self.inventoryBtn.setIconSize(QtCore.QSize(54, 54))
        self.inventoryBtn.setObjectName("inventoryBtn")
        self.horizontalLayout.addWidget(self.inventoryBtn)
        spacerItem6 = QtGui.QSpacerItem(438, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.logoutBtn = QtGui.QPushButton(self.layoutWidget3)
        self.logoutBtn.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/images/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.logoutBtn.setIcon(icon4)
        self.logoutBtn.setIconSize(QtCore.QSize(58, 58))
        self.logoutBtn.setObjectName("logoutBtn")
        self.horizontalLayout.addWidget(self.logoutBtn)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 735, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("MainWindow", "Weekly Sales", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("MainWindow", "Today\'s Sales", None, QtGui.QApplication.UnicodeUTF8))
        self.label_10.setText(QtGui.QApplication.translate("MainWindow", "View Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.label_11.setText(QtGui.QApplication.translate("MainWindow", "From", None, QtGui.QApplication.UnicodeUTF8))
        self.label_12.setText(QtGui.QApplication.translate("MainWindow", "To", None, QtGui.QApplication.UnicodeUTF8))
        self.viewReportsBtn.setText(QtGui.QApplication.translate("MainWindow", "View", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.reportsTab), QtGui.QApplication.translate("MainWindow", "Reports", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Add User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("MainWindow", "Password", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("MainWindow", "Repeat Password:", None, QtGui.QApplication.UnicodeUTF8))
        self.addUserBtn.setText(QtGui.QApplication.translate("MainWindow", "Add User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("MainWindow", "Remove User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("MainWindow", "Username:", None, QtGui.QApplication.UnicodeUTF8))
        self.deleteUserBtn.setText(QtGui.QApplication.translate("MainWindow", "Delete", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.manageUsersTab), QtGui.QApplication.translate("MainWindow", "Manage Users", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("MainWindow", "Search:", None, QtGui.QApplication.UnicodeUTF8))
        self.inventoryAddItemBtn.setText(QtGui.QApplication.translate("MainWindow", "Add Item", None, QtGui.QApplication.UnicodeUTF8))
        self.inventorySaveBtn.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.inventoryCancelBtn.setText(QtGui.QApplication.translate("MainWindow", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.inventoryTab), QtGui.QApplication.translate("MainWindow", "Inventory", None, QtGui.QApplication.UnicodeUTF8))

import qrc_resources
