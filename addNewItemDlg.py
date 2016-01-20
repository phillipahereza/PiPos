# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addNewItem.ui'
#
# Created: Wed Jan 20 21:35:26 2016
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
        self.addItemBtnBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.addItemBtnBox.setObjectName("addItemBtnBox")
        self.generateBarcodeBtn = QtGui.QPushButton(Dialog)
        self.generateBarcodeBtn.setGeometry(QtCore.QRect(90, 380, 131, 24))
        self.generateBarcodeBtn.setObjectName("generateBarcodeBtn")
        self.printBarcodeBtn = QtGui.QPushButton(Dialog)
        self.printBarcodeBtn.setGeometry(QtCore.QRect(250, 380, 95, 24))
        self.printBarcodeBtn.setObjectName("printBarcodeBtn")
        self.barcodeLbl_2 = QtGui.QLabel(Dialog)
        self.barcodeLbl_2.setGeometry(QtCore.QRect(11, 344, 65, 16))
        self.barcodeLbl_2.setObjectName("barcodeLbl_2")
        self.scannedLineEdit = QtGui.QLineEdit(Dialog)
        self.scannedLineEdit.setGeometry(QtCore.QRect(89, 344, 129, 25))
        self.scannedLineEdit.setObjectName("scannedLineEdit")
        self.descriptionLbl = QtGui.QLabel(Dialog)
        self.descriptionLbl.setGeometry(QtCore.QRect(11, 63, 72, 16))
        self.descriptionLbl.setObjectName("descriptionLbl")
        self.quantityLE = QtGui.QLineEdit(Dialog)
        self.quantityLE.setGeometry(QtCore.QRect(89, 292, 129, 25))
        self.quantityLE.setObjectName("quantityLE")
        self.nameLE = QtGui.QLineEdit(Dialog)
        self.nameLE.setGeometry(QtCore.QRect(89, 32, 129, 25))
        self.nameLE.setObjectName("nameLE")
        self.eanDisplayLbl = QtGui.QLabel(Dialog)
        self.eanDisplayLbl.setGeometry(QtCore.QRect(89, 323, 16, 16))
        self.eanDisplayLbl.setText("")
        self.eanDisplayLbl.setObjectName("eanDisplayLbl")
        self.quantityLbl = QtGui.QLabel(Dialog)
        self.quantityLbl.setGeometry(QtCore.QRect(11, 292, 56, 16))
        self.quantityLbl.setObjectName("quantityLbl")
        self.priceLbl = QtGui.QLabel(Dialog)
        self.priceLbl.setGeometry(QtCore.QRect(11, 261, 34, 16))
        self.priceLbl.setObjectName("priceLbl")
        self.nameLbl = QtGui.QLabel(Dialog)
        self.nameLbl.setGeometry(QtCore.QRect(11, 32, 39, 16))
        self.nameLbl.setObjectName("nameLbl")
        self.barcodeLbl = QtGui.QLabel(Dialog)
        self.barcodeLbl.setGeometry(QtCore.QRect(11, 323, 53, 16))
        self.barcodeLbl.setObjectName("barcodeLbl")
        self.priceLE = QtGui.QLineEdit(Dialog)
        self.priceLE.setGeometry(QtCore.QRect(89, 261, 129, 25))
        self.priceLE.setObjectName("priceLE")
        self.descriptionTE = QtGui.QTextEdit(Dialog)
        self.descriptionTE.setGeometry(QtCore.QRect(89, 63, 256, 192))
        self.descriptionTE.setObjectName("descriptionTE")

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.addItemBtnBox, QtCore.SIGNAL("accepted()"), Dialog.accept)
        QtCore.QObject.connect(self.addItemBtnBox, QtCore.SIGNAL("rejected()"), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Add New Item", None, QtGui.QApplication.UnicodeUTF8))
        self.generateBarcodeBtn.setText(QtGui.QApplication.translate("Dialog", "Generate Barcode", None, QtGui.QApplication.UnicodeUTF8))
        self.printBarcodeBtn.setText(QtGui.QApplication.translate("Dialog", "Print", None, QtGui.QApplication.UnicodeUTF8))
        self.barcodeLbl_2.setText(QtGui.QApplication.translate("Dialog", "Scan Code:", None, QtGui.QApplication.UnicodeUTF8))
        self.descriptionLbl.setText(QtGui.QApplication.translate("Dialog", "Description:", None, QtGui.QApplication.UnicodeUTF8))
        self.quantityLbl.setText(QtGui.QApplication.translate("Dialog", "Quantity:", None, QtGui.QApplication.UnicodeUTF8))
        self.priceLbl.setText(QtGui.QApplication.translate("Dialog", "Price:", None, QtGui.QApplication.UnicodeUTF8))
        self.nameLbl.setText(QtGui.QApplication.translate("Dialog", "Name:", None, QtGui.QApplication.UnicodeUTF8))
        self.barcodeLbl.setText(QtGui.QApplication.translate("Dialog", "Barcode:", None, QtGui.QApplication.UnicodeUTF8))

