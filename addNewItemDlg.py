# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewItem.ui'
#
# Created: Tue Jan  5 15:54:13 2016
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(367, 471)
        self.addItemBtnBox = QtGui.QDialogButtonBox(Dialog)
        self.addItemBtnBox.setGeometry(QtCore.QRect(0, 430, 341, 32))
        self.addItemBtnBox.setOrientation(QtCore.Qt.Horizontal)
        self.addItemBtnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel | QtGui.QDialogButtonBox.Ok)
        self.addItemBtnBox.setObjectName("addItemBtnBox")
        self.generateBarcodeBtn = QtGui.QPushButton(Dialog)
        self.generateBarcodeBtn.setGeometry(QtCore.QRect(90, 380, 131, 24))
        self.generateBarcodeBtn.setObjectName("generateBarcodeBtn")
        self.layoutWidget = QtGui.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(10, 30, 335, 341))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.nameLbl = QtGui.QLabel(self.layoutWidget)
        self.nameLbl.setObjectName("nameLbl")
        self.gridLayout.addWidget(self.nameLbl, 0, 0, 1, 1)
        self.nameLE = QtGui.QLineEdit(self.layoutWidget)
        self.nameLE.setObjectName("nameLE")
        self.gridLayout.addWidget(self.nameLE, 0, 1, 1, 1)
        self.descriptionLbl = QtGui.QLabel(self.layoutWidget)
        self.descriptionLbl.setObjectName("descriptionLbl")
        self.gridLayout.addWidget(self.descriptionLbl, 1, 0, 1, 1)
        self.descriptionTE = QtGui.QTextEdit(self.layoutWidget)
        self.descriptionTE.setObjectName("descriptionTE")
        self.gridLayout.addWidget(self.descriptionTE, 1, 1, 1, 1)
        self.priceLbl = QtGui.QLabel(self.layoutWidget)
        self.priceLbl.setObjectName("priceLbl")
        self.gridLayout.addWidget(self.priceLbl, 2, 0, 1, 1)
        self.priceLE = QtGui.QLineEdit(self.layoutWidget)
        self.priceLE.setObjectName("priceLE")
        self.gridLayout.addWidget(self.priceLE, 2, 1, 1, 1)
        self.quantityLbl = QtGui.QLabel(self.layoutWidget)
        self.quantityLbl.setObjectName("quantityLbl")
        self.gridLayout.addWidget(self.quantityLbl, 3, 0, 1, 1)
        self.quantityLE = QtGui.QLineEdit(self.layoutWidget)
        self.quantityLE.setObjectName("quantityLE")
        self.gridLayout.addWidget(self.quantityLE, 3, 1, 1, 1)
        self.barcodeLbl = QtGui.QLabel(self.layoutWidget)
        self.barcodeLbl.setObjectName("barcodeLbl")
        self.gridLayout.addWidget(self.barcodeLbl, 4, 0, 1, 1)
        self.eanDisplayLbl = QtGui.QLabel(self.layoutWidget)
        self.eanDisplayLbl.setText("")
        self.eanDisplayLbl.setObjectName("eanDisplayLbl")
        self.gridLayout.addWidget(self.eanDisplayLbl, 4, 1, 1, 1)
        self.printBarcodeBtn = QtGui.QPushButton(Dialog)
        self.printBarcodeBtn.setGeometry(QtCore.QRect(250, 380, 95, 24))
        self.printBarcodeBtn.setObjectName("printBarcodeBtn")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.addItemBtnBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.addItemBtnBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(
            QtGui.QApplication.translate("Dialog", "Add New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.generateBarcodeBtn.setText(
            QtGui.QApplication.translate("Dialog", "Generate Barcode", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLbl.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLbl.setText(
            QtGui.QApplication.translate("Dialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.priceLbl.setText(QtGui.QApplication.translate("Dialog", "Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.quantityLbl.setText(
            QtGui.QApplication.translate("Dialog", "Quantity:", None, QtGui.QApplication.UnicodeUTF8))
        self.barcodeLbl.setText(
            QtGui.QApplication.translate("Dialog", "Barcode:", None, QtGui.QApplication.UnicodeUTF8))
        self.printBarcodeBtn.setText(
            QtGui.QApplication.translate("Dialog", "Print", None, QtGui.QApplication.UnicodeUTF8))
