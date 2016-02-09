"""
These classes solve the problem of the context menu appearing everywhere in the
main window
"""
from PySide.QtCore import *
from PySide.QtGui import *
import databaseManagement


class CartTable(QTableWidget):
    """
    this class implements a QTableWidget with custom context menu
    for the cart table
    """
    def __init__(self, *args, **kwargs):
        super(CartTable, self).__init__(*args, **kwargs)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self, SIGNAL('customContextMenuRequested(const QPoint &)'), self.context_menu)

    def context_menu(self):
        menu = QMenu(self)
        delete_action = menu.addAction('Delete')
        self.connect(delete_action, SIGNAL('triggered()'), self.remove_from_cart)
        menu.exec_(QCursor.pos())

    def remove_from_cart(self):
        self.removeRow(self.currentRow())


class SearchTable(QTableWidget):
    """
    this class implements a QTableWidget with custom context menu
    for the cart table
    """
    def __init__(self, *args, **kwargs):
        super(SearchTable, self).__init__(*args, **kwargs)
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.connect(self, SIGNAL('customContextMenuRequested(const QPoint &)'), self.context_menu)

    def context_menu(self):
        menu = QMenu(self)
        edit_action = menu.addAction('Edit')
        restock_action = menu.addAction('Add Stock')
        delete_action = menu.addAction('Delete')
        self.connect(edit_action, SIGNAL('triggered()'), self.edit_item)
        self.connect(delete_action, SIGNAL('triggered()'), self.delete_item)
        self.connect(restock_action, SIGNAL('triggered()'), self.add_stock)
        menu.exec_(QCursor.pos())

    def delete_item(self):
        print 'raise message box delete item'
        """first confirm"""
        confirm_box = QMessageBox(self)
        confirm_box.setText("This item will be deleted.")
        confirm_box.setInformativeText("Once the item is deleted, it can not be recovered.")
        confirm_box.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        confirm_box.setDefaultButton(QMessageBox.Cancel)
        ret = confirm_box.exec_()
        if ret == QMessageBox.Ok:
            item_id = self.selectedItems()[0].text()
            self.removeRow(self.currentRow())
            databaseManagement.delete_item(item_id)
            # print 'Item Deleted ', item_id
        else:
            pass

    def edit_item(self):
        item_id = str(self.selectedItems()[0].text())
        edit_item_dlg = EditItemDialog(item_id, self)
        edit_item_dlg.open()

    def add_stock(self):
        print "add stock"
        item_id = 1  # str(self.selectedItems()[0].text())
        add_stock_dlg = AddStockDialog(item_id, self)
        add_stock_dlg.show()


class AddStockDialog(QDialog):
    def __init__(self, item_id, parent=None):
        super(AddStockDialog, self).__init__(parent)
        self.item_id = item_id
        self.setWindowTitle('Add Stock')
        self.grid = QGridLayout()
        self.spinbox_label = QLabel('Stock:')
        self.stock_spinbox = QSpinBox()
        self.stock_spinbox.setRange(0, 1000000)

        self.button_box = QDialogButtonBox()
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        QObject.connect(self.button_box, SIGNAL("accepted()"), self.accept)
        QObject.connect(self.button_box, SIGNAL("rejected()"), self.reject)

        self.font = QFont()
        self.font.setPointSize(14)
        self.font.setWeight(75)
        self.font.setBold(True)
        self.title_label = QLabel('Add Stock')
        self.title_label.setFont(self.font)

        self.grid.addWidget(self.spinbox_label, 0, 0)
        self.grid.addWidget(self.stock_spinbox, 0, 1)

        self.vertical_layout = QVBoxLayout()
        self.vertical_layout.addWidget(self.title_label)
        self.vertical_layout.addLayout(self.grid)
        self.vertical_layout.addWidget(self.button_box)
        self.setLayout(self.vertical_layout)

        self.connect(self.button_box, SIGNAL('accepted()'), self.add_stock)

    def add_stock(self):
        restock_value = self.stock_spinbox.value()
        print 'Stock of %d added' % restock_value


class EditItemDialog(QDialog):
    def __init__(self, item_id, parent=None):
        super(EditItemDialog, self).__init__(parent)
        self.item_id = item_id
        self.setWindowTitle('Edit Item')
        self.grid = QGridLayout()
        self.font = QFont()
        self.font.setPointSize(14)
        self.font.setWeight(75)
        self.font.setBold(True)
        self.vertical_layout = QVBoxLayout()
        self.name_line_edit = QLineEdit()
        self.desc_text_edit = QTextEdit()
        self.unit_price_spinbox = QSpinBox()
        self.unit_price_spinbox.setRange(100, 100000000)
        self.button_box = QDialogButtonBox()
        self.button_box.setStandardButtons(QDialogButtonBox.Cancel | QDialogButtonBox.Ok)
        QObject.connect(self.button_box, SIGNAL("accepted()"), self.accept)
        QObject.connect(self.button_box, SIGNAL("rejected()"), self.reject)
        self.name_label = QLabel("Name:")
        self.desc_label = QLabel("Description:")
        self.unit_price_label = QLabel("Unit Price:")

        self.grid.addWidget(self.name_label, 0, 0)
        self.grid.addWidget(self.desc_label, 1, 0)
        self.grid.addWidget(self.unit_price_label, 2, 0)

        self.grid.addWidget(self.name_line_edit, 0, 1)
        self.grid.addWidget(self.desc_text_edit, 1, 1)
        self.grid.addWidget(self.unit_price_spinbox, 2, 1)
        self.grid.addWidget(self.button_box, 3, 1)

        self.top_label = QLabel("Edit Item")
        self.top_label.setFont(self.font)
        self.vertical_layout.addWidget(self.top_label)
        self.vertical_layout.addLayout(self.grid)
        self.setLayout(self.vertical_layout)
        _, name, desc = databaseManagement.get_item_details(self.item_id)
        self.name_line_edit.setText(name)
        self.desc_text_edit.setText(desc)
        self.connect(self.button_box, SIGNAL('accepted()'), self.update_db)

    def update_db(self):
        name = self.name_line_edit.text()
        desc = self.desc_text_edit.toPlainText()
        databaseManagement.update(self.item_id, name, desc)
        print 'Updated'






















