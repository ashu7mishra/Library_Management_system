from PyQt5.QtWidgets import QMainWindow, QDialog
from mainGUI import Ui_MainWindow
from addBook import Add_Dialog
from AddMember import Member_Dialog
from ViewBook import View_Dialog

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addBook.clicked.connect(self.add_book)
        self.toolButton_addMember.clicked.connect(self.add_member)
        self.toolButton_viewBook.clicked.connect(self.view_books)

    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def add_member(self):
        dialog = QDialog()
        ui = Member_Dialog()

        ui.setupUi(dialog)
        dialog.exec()

    def view_books(self):
        dialog = QDialog()
        ui = View_Dialog()

        ui.setupUi(dialog)
        dialog.exec()