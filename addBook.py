# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\addBook.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Add_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 427)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_title = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_title.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_title.setFont(font)
        self.lineEdit_title.setObjectName("lineEdit_title")
        self.verticalLayout.addWidget(self.lineEdit_title)
        self.lineEdit_ID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_ID.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_ID.setFont(font)
        self.lineEdit_ID.setObjectName("lineEdit_ID")
        self.verticalLayout.addWidget(self.lineEdit_ID)
        self.lineEdit_author = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_author.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_author.setFont(font)

        self.lineEdit_author.setObjectName("lineEdit_author")
        self.verticalLayout.addWidget(self.lineEdit_author)
        self.lineEdit_publisher = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_publisher.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_publisher.setFont(font)
        self.lineEdit_publisher.setObjectName("lineEdit_publisher")
        self.verticalLayout.addWidget(self.lineEdit_publisher)
        self.pushButton_addBook = QtWidgets.QPushButton(Dialog)
        self.pushButton_addBook.clicked.connect(self.insert_book)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_addBook.setFont(font)
        self.pushButton_addBook.setStyleSheet("QPushButton{\n"
"\n"
"background-color:grey\n"
"\n"
"}")
        self.pushButton_addBook.setObjectName("pushButton_addBook")
        self.verticalLayout.addWidget(self.pushButton_addBook)
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setText("")
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def insert_book(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
            title = self.lineEdit_title.text()
            id = self.lineEdit_ID.text()
            author = self.lineEdit_author.text()
            publisher = self.lineEdit_publisher.text()

            if title == "" or id == "" or author == "" or publisher == "":
                self.label.setText("Please add all fields")
                self.label.setStyleSheet("color:red")
                return

            mycursor = mydb.cursor()
            query = "INSERT INTO book (id, title, author, publisher) VALUES (%s, %s, %s, %s)"
            value = (id, title, author, publisher)
            mycursor.execute(query, value)
            mydb.commit()
            self.label.setText("Data added successfully")
            self.label.setStyleSheet("color:green")

            self.lineEdit_title.setText("")
            self.lineEdit_ID.setText("")
            self.lineEdit_author.setText("")
            self.lineEdit_publisher.setText("")

        except mc.Error as e:
            self.label.setText("Failed to add Book")
            self.label.setStyleSheet("color:red")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert Book"))
        self.lineEdit_title.setPlaceholderText(_translate("Dialog", "Please Enter Title"))
        self.lineEdit_ID.setPlaceholderText(_translate("Dialog", "Please Enter ID"))
        self.lineEdit_author.setPlaceholderText(_translate("Dialog", "Please Enter Author"))
        self.lineEdit_publisher.setPlaceholderText(_translate("Dialog", "Please Enter Publisher"))
        self.pushButton_addBook.setText(_translate("Dialog", "Insert Book"))
