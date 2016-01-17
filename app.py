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
import editItemDlg
from generate_ean import getnumber


class LoginDlg(QDialog, loginDlg.Ui_loginDlg):
    def __init__(self, parent=None):
        super(LoginDlg, self).__init__(parent)
        self.setupUi(self)
        self.userComboBox.clear()
        self.userComboBox.addItems(databaseManagement.get_users())
        self.connect(self.loginBtn, SIGNAL('clicked()'), self.login)

    def login(self):
        uname = self.userComboBox.currentText()
        pwd = self.loginPwdLineEdit.text()
        if uname == 'Admin':
            if pwd == databaseManagement.retrievepassword(uname):
                adminMain = AdminMainWindow(self)
                self.hide()
                adminMain.show()
            else:
                messageBox = QMessageBox()
                messageBox.setText("Incorrect Login Credentials")
                messageBox.show()
                messageBox.exec_()
                self.loginPwdLineEdit.clear()
        else:
            if pwd == databaseManagement.retrievepassword(uname):
                userMain = UserMainWindow(self)
                self.hide()
                userMain.show()

            else:
                messageBox = QMessageBox()
                messageBox.setText("Incorrect Login Credentials")
                messageBox.show()
                messageBox.exec_()
                self.loginPwdLineEdit.clear()


class UserMainWindow(QMainWindow, userMainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(UserMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.connect(self.userSales, SIGNAL('clicked()'), self.switch2sales)
        self.connect(self.userSettings, SIGNAL('clicked()'), self.switch2settings)
        self.connect(self.notificationsBtn, SIGNAL('clicked()'), self.switch2notifactions)

    def logout(self):
        """update the database with the logout time"""
        sys.exit(1)

    def switch2sales(self):
        self.stackedWidget.setCurrentWidget(self.salesStackPage)

    def switch2settings(self):
        self.stackedWidget.setCurrentWidget(self.settingsStackPage)

    def switch2notifactions(self):
        self.stackedWidget.setCurrentWidget(self.notificationsPage)

        # def change_password(self):


class AdminMainWindow(QMainWindow, adminMainWindow.Ui_MainWindow):
    def __init__(self, parent=None):
        super(AdminMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.tabWidget.setCurrentWidget(self.reportsTab)
        self.userComboBox.clear()
        self.userComboBox.addItems(databaseManagement.get_users())
        self.connect(self.inventoryBtn, SIGNAL('clicked()'),
                     self.inventoryBtnSignal)
        self.connect(self.reportsBtn, SIGNAL('clicked()'),
                     self.reportsBtnSignal)
        self.connect(self.logoutBtn, SIGNAL('clicked()'), self.logout)
        self.connect(self.addUserBtn, SIGNAL('clicked()'), self.add_user)
        self.connect(self.deleteUserBtn, SIGNAL('clicked()'), self.delete_user)
        self.setWindowTitle("Point of Sale System")
        self.connect(self.inventoryAddItemBtn, SIGNAL('clicked()'), self.add_new_item)
        self.connect(self.searchBtn, SIGNAL('clicked()'), self.search_inventory)


    def inventoryBtnSignal(self):
        self.tabWidget.setCurrentWidget(self.inventoryTab)

    def reportsBtnSignal(self):
        self.tabWidget.setCurrentWidget(self.reportsTab)

    def logout(self):
        """update the database with the logout time"""
        sys.exit(1)

    def add_user(self):
        if self.addUserUnameEdit.isModified() == True and self.addUserPwdEdit.isModified() == True and \
                        self.addUserRptPwdEdit.isModified() == True:
            if self.addUserPwdEdit.text() == self.addUserRptPwdEdit.text():
                uname = self.addUserUnameEdit.text()
                pwd = self.addUserPwdEdit.text()
                databaseManagement.create_user(uname, pwd)
                self.addUserUnameEdit.clear()
                self.addUserPwdEdit.clear()
                self.addUserRptPwdEdit.clear()
                msgBox = QMessageBox(self)
                msgBox.setText('New user Added!!!!')
                msgBox.show()
                msgBox.exec_()
                self.userComboBox.clear()
                self.userComboBox.addItems(databaseManagement.get_users())

            else:
                msgBox = QMessageBox(self)
                msgBox.setText('The passwords do not match')
                msgBox.show()
                msgBox.exec_()
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
        confirmBox = QMessageBox(self)
        confirmBox.setText("This user will be deleted.")
        confirmBox.setInformativeText("Once the user is deleted, they can not be recovered.")
        confirmBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirmBox.setDefaultButton(QMessageBox.Cancel)
        ret = confirmBox.exec_()
        if ret == QMessageBox.Ok:
            databaseManagement.delete_user(user_del)
            self.userComboBox.clear()
            self.userComboBox.addItems(databaseManagement.get_users())
        else:
            pass

    def add_new_item(self):
        addItem = AddNewItemDialog(self)
        addItem.show()

    def search_inventory(self):
        self.tableWidget.setContextMenuPolicy(Qt.ActionsContextMenu)
        self.tableWidget.clear()
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setHorizontalHeaderLabels(['ID', 'Item', 'Description'])
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionBehavior(QTableWidget.SelectRows)
        self.tableWidget.setSelectionMode(QTableWidget.SingleSelection)
        text = self.inventorySeachEdit.text()
        if text != '':
            result = databaseManagement.search(text)
            self.tableWidget.setRowCount(len(result))
            for row in range(len(result)):
                for i in range(3):
                    item = QTableWidgetItem(result[row][i])
                    self.tableWidget.setItem(row, i, item)
            self.tableWidget.resizeColumnsToContents()
            self.tableWidget.customContextMenuRequested.connect(self.contextMenuEvent)
            # self.tableWidget.itemSelectionChanged.connect(self.getContextMenu)

        else:
            pass

    def contextMenuEvent(self, event):
        menu = QMenu()
        editAction = menu.addAction('Edit')
        deleteAction = menu.addAction('Delete')
        self.connect(editAction, SIGNAL('triggered()'), self.edit_item)
        self.connect(deleteAction, SIGNAL('triggered()'), self.delete_item)
        menu.exec_(event.globalPos())

    def delete_item(self):
        print 'raise message box delete item'
        """first confirm"""
        confirmBox = QMessageBox(self)
        confirmBox.setText("This item will be deleted.")
        confirmBox.setInformativeText("Once the item is deleted, it can not be recovered.")
        confirmBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirmBox.setDefaultButton(QMessageBox.Cancel)
        ret = confirmBox.exec_()
        if ret == QMessageBox.Ok:
            item_id = self.tableWidget.selectedItems()[0].text()
            self.tableWidget.removeRow(self.tableWidget.currentRow())
            databaseManagement.delete_item(item_id)
            # print 'Item Deleted ', item_id
        else:
            pass

    def edit_item(self):
        item_id = self.tableWidget.selectedItems()[0].text()
        editItem = EditItemDialog(self)
        editItem.show()


class AddNewItemDialog(QDialog, addNewItemDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super(AddNewItemDialog, self).__init__(parent)
        self.setupUi(self)
        self.ean = None
        self.connect(self.generateBarcodeBtn, SIGNAL('clicked()'), self.generate_barcode)
        self.connect(self.addItemBtnBox, SIGNAL('accepted()'), self.writeToDb)

    def generate_barcode(self):
        self.ean = getnumber()
        self.eanDisplayLbl.setText(self.ean)

    def print_barcode(self):
        bar = barcode.get('ean13', self.ean, writer=ImageWriter())
        # filename = bar.save('ean13')

    def writeToDb(self):
        ean = self.ean
        name = self.nameLE.text()
        description = self.descriptionTE.toPlainText()
        price = self.priceLE.text()
        quantity = self.quantityLE.text()
        # add item into the db
        print "Written to db"


class EditItemDialog(QDialog, editItemDlg.Ui_Dialog):
    def __init__(self, parent=None):
        super(EditItemDialog, self).__init__(parent)
        self.setupUi(self)
        self.item_id = 1
        _, name, desc = databaseManagement.get_item_details(self.item_id)
        self.nameLineEdit.setText(name)
        self.descTextEdit.setText(desc)
        self.connect(self.editItemBtnBox, SIGNAL('accepted()'), self.update_db)

    def update_db(self):
        name = self.nameLineEdit.text()
        desc = self.descTextEdit.toPlainText()
        databaseManagement.update(self.item_id, name, desc)


app = QApplication(sys.argv)
lgn = LoginDlg()
lgn.show()
app.exec_()