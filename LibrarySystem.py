from PyQt5.QtWidgets import QMainWindow, QDialog
from mainGUI import Ui_MainWindow
from addBook import Add_Dialog

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addBook.clicked.connect(self.add_book)

    def add_book(self):
        dialog = QDialog()
        ui = Add_Dialog()

        ui.setupUi(dialog)
        dialog.exec()