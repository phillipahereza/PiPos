import sys

import barcode
from PySide.QtCore import *
from PySide.QtGui import *
from barcode.writer import ImageWriter

import addNewItemDlg
import adminMainWindow
import databaseManagement
import loginDlg
import userMainWindow

from generate_ean import getnumber


class LoginDlg(QDialog, loginDlg.Ui_loginDlg):
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)
        self.setupUi(self)
        self.userComboBox.clear()
        self.userComboBox.addItems(databaseManagement.get_users())
        self.connect(self.loginBtn, SIGNAL('clicked()'), self.login)

    def login(self):
        u_name = self.userComboBox.currentText()
        pwd = self.loginPwdLineEdit.text()
        if u_name == 'Admin':
            if pwd == databaseManagement.retrieve_password(u_name):
                admin_mainwindow = AdminMainWindow(self)
                self.hide()
                admin_mainwindow.show()
            else:
                message_box = QMessageBox()
                message_box.setText("Incorrect Login Credentials")
                message_box.show()
                message_box.exec_()
                self.loginPwdLineEdit.clear()
        else:
            if pwd == databaseManagement.retrieve_password(u_name):
                user_mainwindow = UserMainWindow(self)
                self.hide()
                user_mainwindow.show()

            else:
                message_box = QMessageBox()
                message_box.setText("Incorrect Login Credentials")
                message_box.show()
                message_box.exec_()
                self.loginPwdLineEdit.clear()


class UserMainWindow(QMainWindow, userMainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UserMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.currentCart = []
        self.connect(self.userSales, SIGNAL('clicked()'), self.switch_to_sales_tab)
        self.connect(self.userSettings, SIGNAL('clicked()'), self.switch_to_settings_tab)
        self.connect(self.notificationsBtn, SIGNAL('clicked()'), self.switch_to_notifications_tab)
        self.connect(self.searchButton, SIGNAL('clicked()'), self.search_inventory)
        self.connect(self.searchTableWidget, SIGNAL('itemSelectionChanged()'), self.add_to_cart)
        self.searchTableWidget.setAlternatingRowColors(True)
        self.searchTableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.searchTableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.searchTableWidget.setSelectionMode(QTableWidget.SingleSelection)
        self.cartTableWidget.clear()
        self.cartTableWidget.setColumnCount(3)
        self.cartTableWidget.setHorizontalHeaderLabels(['Item', 'Quantity', 'Price'])
        self.cartTableWidget.setAlternatingRowColors(True)
        self.connect(self.cashLineEdit, SIGNAL('returnPressed()'), self.return_balance)
        self.connect(self.finishBtn, SIGNAL('clicked()'), self.on_finish)
        self.connect(self.checkoutButton, SIGNAL('clicked()'), self.checkout)
        self.connect(self.searchLineEdit, SIGNAL('returnPressed()'), self.search_inventory)

    def logout(self):
        """update the database with the logout time"""
        sys.exit(1)

    def switch_to_sales_tab(self):
        self.stackedWidget.setCurrentWidget(self.salesStackPage)

    def switch_to_settings_tab(self):
        self.stackedWidget.setCurrentWidget(self.settingsStackPage)

    def switch_to_notifications_tab(self):
        self.stackedWidget.setCurrentWidget(self.notificationsPage)

    # def change_password(self):

    def search_inventory(self):
        self.searchTableWidget.clear()
        self.searchTableWidget.setColumnCount(3)
        self.searchTableWidget.setHorizontalHeaderLabels(['Item', 'Desc', 'Cost'])
        text = self.searchLineEdit.text()
        if text != '':
            result = databaseManagement.search(text)
            # result = [['1', 'Book', '3000'], ['2', 'Pencil', '300'], ['5', 'Ruler', '1000']]
            self.searchTableWidget.setRowCount(len(result))
            for row in range(len(result)):
                for i in range(3):
                    item = QTableWidgetItem(result[row][i])
                    self.searchTableWidget.setItem(row, i, item)
            # self.searchTableWidget.resizeColumnsToContents()
        else:
            pass

    def add_to_cart(self):
        quantity, result = QInputDialog.getInt(self, "Quantity", "Enter quantity to buy: ")
        if quantity > 0:
            # print 'Quantity is %s' % quantity
            item = self.searchTableWidget.selectedItems()[1].text()
            px = self.searchTableWidget.selectedItems()[2].text()
            result = [item, str(quantity), str(int(px) * int(quantity))]
            self.currentCart.append(result)
            self.cartTableWidget.setRowCount(len(self.currentCart))
            for row in range(len(self.currentCart)):
                for i in range(3):
                    item = QTableWidgetItem(self.currentCart[row][i])
                    self.cartTableWidget.setItem(row, i, item)

        else:
            pass
        self.searchTableWidget.clearSelection()

    def checkout(self):
        prices = []
        for row in range(self.cartTableWidget.rowCount()):
            item = self.cartTableWidget.item(row, 2)
            prices.append(int(item.text()))
        self.totalDisplay.setText(str(sum(prices)))

        # databaseManagement.make_sale(sum(prices))

        # self.cartTableWidget.clear()
        # self.cartTableWidget.setColumnCount(3)
        # self.cartTableWidget.setHorizontalHeaderLabels(['Item', 'Quantity', 'Price'])
        # self.currentCart = []

    def return_balance(self):
        cash = int(self.cashLineEdit.text())
        if int(self.totalDisplay.text()) > 1:
            balance = cash - int(self.totalDisplay.text())
            self.balanceDisplayLbl.setText(str(balance))
        else:
            confirm_box = QMessageBox(self)
            confirm_box.setText("This user will be deleted.")
            confirm_box.setInformativeText("Once the user is deleted, they can not be recovered.")
            confirm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            confirm_box.setDefaultButton(QMessageBox.Cancel)

    def on_finish(self):
        self.balanceDisplayLbl.setText("")
        self.cashLineEdit.setText("")
        self.totalDisplay.setText("")
        self.cartTableWidget.clear()
        self.currentCart = []
        self.cartTableWidget.setColumnCount(3)
        self.cartTableWidget.setHorizontalHeaderLabels(['Item', 'Quantity', 'Price'])
        # self.searchTableWidget.clear()


class AdminMainWindow(QMainWindow, adminMainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AdminMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.reportsTab)
        self.userComboBox.clear()
        self.userComboBox.addItems(databaseManagement.get_users())
        self.connect(self.inventoryBtn, SIGNAL('clicked()'),
                     self.inventory_btn_signal)
        self.connect(self.reportsBtn, SIGNAL('clicked()'),
                     self.reports_btn_signal)
        self.connect(self.logoutBtn, SIGNAL('clicked()'), self.logout)
        self.connect(self.addUserBtn, SIGNAL('clicked()'), self.add_user)
        self.connect(self.deleteUserBtn, SIGNAL('clicked()'), self.delete_user)
        self.setWindowTitle("Point of Sale System")
        self.connect(self.inventoryAddItemBtn, SIGNAL('clicked()'), self.add_new_item)
        self.connect(self.searchBtn, SIGNAL('clicked()'), self.search_inventory)
        self.connect(self.inventorySeachEdit, SIGNAL('returnPressed()'), self.search_inventory)

    def inventory_btn_signal(self):
        self.tabWidget.setCurrentWidget(self.inventoryTab)

    def reports_btn_signal(self):
        self.tabWidget.setCurrentWidget(self.reportsTab)

    def logout(self):
        """update the database with the logout time"""
        sys.exit(1)

    def add_user(self):
        if self.addUserUnameEdit.isModified() == True and self.addUserPwdEdit.isModified() == True and \
                        self.addUserRptPwdEdit.isModified() == True:
            if self.addUserPwdEdit.text() == self.addUserRptPwdEdit.text():
                u_name = self.addUserUnameEdit.text()
                pwd = self.addUserPwdEdit.text()
                databaseManagement.create_user(u_name, pwd)
                self.addUserUnameEdit.clear()
                self.addUserPwdEdit.clear()
                self.addUserRptPwdEdit.clear()
                msg_box = QMessageBox(self)
                msg_box.setText('New user Added!!!!')
                msg_box.show()
                msg_box.exec_()
                self.userComboBox.clear()
                self.userComboBox.addItems(databaseManagement.get_users())

            else:
                msg_box = QMessageBox(self)
                msg_box.setText('The passwords do not match')
                msg_box.show()
                msg_box.exec_()
                self.addUserUnameEdit.clear()
                self.addUserPwdEdit.clear()
                self.addUserRptPwdEdit.clear()
        else:
            mBox = QMessageBox(self)
            mBox.setText('Make sure you fill all the spaces')
            mBox.show()
            mBox.exec_()
            self.addUserUnameEdit.clear()
            self.addUserPwdEdit.clear()
            self.addUserRptPwdEdit.clear()

    def delete_user(self):
        user_del = self.userComboBox.currentText()
        """first confirm"""
        confirm_box = QMessageBox(self)
        confirm_box.setText("This user will be deleted.")
        confirm_box.setInformativeText("Once the user is deleted, they can not be recovered.")
        confirm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirm_box.setDefaultButton(QMessageBox.Cancel)
        ret = confirm_box.exec_()
        if ret == QMessageBox.Ok:
            databaseManagement.delete_user(user_del)
            self.userComboBox.clear()
            self.userComboBox.addItems(databaseManagement.get_users())
        else:
            pass

    def add_new_item(self):
        add_item_dlg = AddNewItemDialog(self)
        add_item_dlg.show()

    def search_inventory(self):
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Item', 'Description', 'Stock Left', 'Price', 'barcode'])
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        text = self.inventorySeachEdit.text()
        if text != '':
            result = databaseManagement.search_inventory(text)
            self.tableWidget.setRowCount(len(result))
            # print len(result)
            for row in range(len(result)):
                for i in range(5):
                    item = QTableWidgetItem(result[row][i])
                    self.tableWidget.setItem(row, i, item)
            self.tableWidget.resizeColumnsToContents()

        else:
            pass


class AddNewItemDialog(QDialog, addNewItemDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super(AddNewItemDialog, self).__init__(parent)
        self.setupUi(self)
        self.ean = None
        self.connect(self.generateBarcodeBtn, SIGNAL('clicked()'), self.generate_barcode)
        self.connect(self.addItemBtnBox, SIGNAL('accepted()'), self.write_to_db)
        self.scanned_ean = ''
        self.scannedLineEdit.blockSignals(True)
        self.scanned_ean = self.scannedLineEdit.text()

    def generate_barcode(self):
        self.ean = getnumber()
        self.eanDisplayLbl.setText(self.ean)

    def print_barcode(self):
        bar = barcode.get('ean13', self.ean, writer=ImageWriter())
        # filename = bar.save('ean13')

    def write_to_db(self):
        if self.scanned_ean == '':
            ean = self.ean
        else:
            ean = self.generate_barcode
        name = self.nameLE.text()
        description = self.descriptionTE.toPlainText()
        price = self.priceLE.text()
        quantity = self.quantityLE.text()
        # add item into the db
        databaseManagement.add_new_item(name, quantity, price, description, ean)
        print "Written to db"


app = QApplication(sys.argv)
lgn = LoginDlg()
lgn.show()
app.exec_()

"""
add stock - getInputDialog
add barcode scanner functionality
legit database
"""