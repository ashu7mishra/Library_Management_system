import sys
from PyQt5.QtWidgets import QApplication
from LibrarySystem import LibrarySystem

app = QApplication(sys.argv)

library = LibrarySystem()

sys.exit(app.exec_())
