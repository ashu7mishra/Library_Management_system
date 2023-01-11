from PyQt5.QtWidgets import QMainWindow, QDialog, QMessageBox
from mainGUI import Ui_MainWindow
from addBook import Add_Dialog
from AddMember import Member_Dialog
from ViewBook import View_Dialog
from view_members import Member_Ui
import mysql.connector as mc
from PyQt5.QtWidgets import QTableWidgetItem

class LibrarySystem(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.show()

        self.toolButton_addBook.clicked.connect(self.add_book)
        self.toolButton_addMember.clicked.connect(self.add_member)
        self.toolButton_viewBook.clicked.connect(self.view_books)
        self.toolButton_viewMember.clicked.connect(self.view_member)
        self.lineEdit_BookID.returnPressed.connect(self.book_id)
        self.lineEdit_MemberID.returnPressed.connect(self.member_id)
        self.toolButton_issueBook.clicked.connect(self.issue_book)
        self.lineEdit_submission.returnPressed.connect(self.load_issue)

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

    def view_member(self):
        dialog = QDialog()
        ui = Member_Ui()

        ui.setupUi(dialog)
        dialog.exec()

    def book_id(self):
        id = self.lineEdit_BookID.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
            mycursor = mydb.cursor()
            query = "SELECT * FROM book WHERE id = '" + id + "'"

            mycursor.execute(query)

            result = mycursor.fetchall()

            for row in result:
                self.label_BookName.setText("Book Name: " + row[1])
                self.label_BookAuthor.setText("Book Author: " + row[2])

        except mc.Error as e:
            print("Error")

    def member_id(self):
        id = self.lineEdit_MemberID.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
            mycursor = mydb.cursor()
            query = "SELECT * FROM member WHERE idmember = '" + id + "'"

            mycursor.execute(query)

            result = mycursor.fetchall()

            for row in result:
                self.label_MemberName.setText("Member Name: " + row[1])
                self.label_ContactInfo.setText("Contact Info: " + row[3])

        except mc.Error as e:
            print("Error")

    def issue_book(self):
        b_id = self.lineEdit_BookID.text()
        m_id = self.lineEdit_MemberID.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
            mycursor = mydb.cursor()
            query1 = "INSERT INTO tbl_issue (bookID, memberID) VALUES (%s, %s)"
            query2 = "UPDATE book SET available = False where id = '" + b_id + "'"
            value = (b_id, m_id)
            mycursor.execute(query1, value)
            mycursor.execute(query2)

            result = mycursor.fetchall()

            QMessageBox.about(self, "Issue Book", "Book Issued Successfully")

        except mc.Error as e:
            print("Error")

    def load_issue(self):
        issue_id = self.lineEdit_submission.text()

        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
            mycursor = mydb.cursor()
            query = "SELECT * FROM tbl_issue WHERE bookID = ' " + issue_id + " ' "

            mycursor.execute(query)

            result = mycursor.fetchall()

            self.tabWidget.setRowCount(0)

            for row_num, row_data in enumerate(result):
                self.tabWidget.insertRow(row_num)
                for col_num, data in enumerate(row_data):
                    self.tabWidget.setItem(row_num, col_num, QTableWidgetItem(str(data)))

        except mc.Error as e:
            print("Error")



