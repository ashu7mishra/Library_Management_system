# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'member.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import mysql.connector as mc


class Member_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 427)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit_memberID = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_memberID.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_memberID.setFont(font)
        self.lineEdit_memberID.setObjectName("lineEdit_memberID")
        self.verticalLayout.addWidget(self.lineEdit_memberID)
        self.lineEdit_memberName = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_memberName.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_memberName.setFont(font)
        self.lineEdit_memberName.setObjectName("lineEdit_memberName")
        self.verticalLayout.addWidget(self.lineEdit_memberName)
        self.lineEdit_memberMobile = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_memberMobile.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_memberMobile.setFont(font)
        self.lineEdit_memberMobile.setObjectName("lineEdit_memberMobile")
        self.verticalLayout.addWidget(self.lineEdit_memberMobile)
        self.lineEdit_memberEmail = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_memberEmail.setMaximumSize(QtCore.QSize(16777215, 40))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_memberEmail.setFont(font)
        self.lineEdit_memberEmail.setObjectName("lineEdit_memberEmail")
        self.verticalLayout.addWidget(self.lineEdit_memberEmail)
        self.pushButton_save = QtWidgets.QPushButton(Dialog)
        self.pushButton_save.setMaximumSize(QtCore.QSize(16777215, 40))
        self.pushButton_save.clicked.connect(self.insert_member)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton_save.setFont(font)
        self.pushButton_save.setStyleSheet("QPushButton{\n"
"\n"
"background-color:grey\n"
"\n"
"}")
        self.pushButton_save.setObjectName("pushButton_save")
        self.verticalLayout.addWidget(self.pushButton_save)
        self.label_result = QtWidgets.QLabel(Dialog)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setText("")
        self.label_result.setObjectName("label_result")
        self.verticalLayout.addWidget(self.label_result)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def insert_member(self):
        try:
            mydb = mc.connect(
                host="localhost",
                user="root",
                password="",
                database="library"
            )
            name = self.lineEdit_memberName.text()
            id = self.lineEdit_memberID.text()
            mobile = self.lineEdit_memberMobile.text()
            email = self.lineEdit_memberEmail.text()

            if name == "" or id == "" or mobile == "" or email == "":
                self.label.setText("Please add all fields")
                self.label.setStyleSheet("color:red")
                return

            mycursor = mydb.cursor()
            query = "INSERT INTO member (idmember, name, mobile, email) VALUES (%s, %s, %s, %s)"
            value = (id, name, mobile, email)
            mycursor.execute(query, value)
            mydb.commit()
            self.label_result.setText("Data added successfully")
            self.label_result.setStyleSheet("color:green")

            self.lineEdit_memberName.setText("")
            self.lineEdit_memberID.setText("")
            self.lineEdit_memberMobile.setText("")
            self.lineEdit_memberEmail.setText("")

        except mc.Error as e:
            self.label_result.setText("Failed to add Member")
            self.label_result.setStyleSheet("color:red")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Insert Member"))
        self.lineEdit_memberID.setPlaceholderText(_translate("Dialog", "Please Enter Member ID"))
        self.lineEdit_memberName.setPlaceholderText(_translate("Dialog", "Please Enter Member Name"))
        self.lineEdit_memberMobile.setPlaceholderText(_translate("Dialog", "Please Enter Member Mobile Number"))
        self.lineEdit_memberEmail.setPlaceholderText(_translate("Dialog", "Please Enter Member Email"))
        self.pushButton_save.setText(_translate("Dialog", "Insert Member"))

