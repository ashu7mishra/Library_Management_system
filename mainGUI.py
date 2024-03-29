# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'File_Management_System.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(911, 551)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.tabWidget.setFont(font)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalWidget = QtWidgets.QWidget(self.tab_2)
        self.horizontalWidget.setStyleSheet("QWidget{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.horizontalWidget.setObjectName("horizontalWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalWidget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_BookID = QtWidgets.QLineEdit(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_BookID.setFont(font)
        self.lineEdit_BookID.setObjectName("lineEdit_BookID")
        self.horizontalLayout_2.addWidget(self.lineEdit_BookID)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_BookName = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_BookName.setFont(font)
        self.label_BookName.setObjectName("label_BookName")
        self.verticalLayout_2.addWidget(self.label_BookName)
        self.label_BookAuthor = QtWidgets.QLabel(self.horizontalWidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_BookAuthor.setFont(font)
        self.label_BookAuthor.setObjectName("label_BookAuthor")
        self.verticalLayout_2.addWidget(self.label_BookAuthor)
        self.horizontalLayout_2.addLayout(self.verticalLayout_2)
        self.verticalLayout_4.addWidget(self.horizontalWidget)
        self.horizontalWidget_2 = QtWidgets.QWidget(self.tab_2)
        self.horizontalWidget_2.setStyleSheet("QWidget{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.horizontalWidget_2.setObjectName("horizontalWidget_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalWidget_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit_MemberID = QtWidgets.QLineEdit(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_MemberID.setFont(font)
        self.lineEdit_MemberID.setObjectName("lineEdit_MemberID")
        self.horizontalLayout_3.addWidget(self.lineEdit_MemberID)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_MemberName = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_MemberName.setFont(font)
        self.label_MemberName.setObjectName("label_MemberName")
        self.verticalLayout_3.addWidget(self.label_MemberName)
        self.label_ContactInfo = QtWidgets.QLabel(self.horizontalWidget_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_ContactInfo.setFont(font)
        self.label_ContactInfo.setObjectName("label_ContactInfo")
        self.verticalLayout_3.addWidget(self.label_ContactInfo)
        self.horizontalLayout_3.addLayout(self.verticalLayout_3)
        self.verticalLayout_4.addWidget(self.horizontalWidget_2)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem2)
        self.toolButton_issueBook = QtWidgets.QToolButton(self.tab_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_issueBook.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("images/issuebook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_issueBook.setIcon(icon)
        self.toolButton_issueBook.setIconSize(QtCore.QSize(78, 78))
        self.toolButton_issueBook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_issueBook.setObjectName("toolButton_issueBook")
        self.horizontalLayout_4.addWidget(self.toolButton_issueBook)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_4)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_submission = QtWidgets.QLineEdit(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.lineEdit_submission.setFont(font)
        self.lineEdit_submission.setStyleSheet("QLineEdit{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.lineEdit_submission.setObjectName("lineEdit_submission")
        self.verticalLayout_5.addWidget(self.lineEdit_submission)
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        self.tableWidget.setStyleSheet("QWidget{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(180)
        self.verticalLayout_5.addWidget(self.tableWidget)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem4)
        self.pushButton_renew = QtWidgets.QPushButton(self.tab)
        self.pushButton_renew.setStyleSheet("QPushButton{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("images/renew.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_renew.setIcon(icon1)
        self.pushButton_renew.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_renew.setObjectName("pushButton_renew")
        self.horizontalLayout_5.addWidget(self.pushButton_renew)
        self.pushButton_Submission = QtWidgets.QPushButton(self.tab)
        self.pushButton_Submission.setStyleSheet("QPushButton{\n"
"\n"
"background-color:rgb(218,218,218)\n"
"\n"
"}")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("images/submission.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_Submission.setIcon(icon2)
        self.pushButton_Submission.setIconSize(QtCore.QSize(40, 40))
        self.pushButton_Submission.setObjectName("pushButton_Submission")
        self.horizontalLayout_5.addWidget(self.pushButton_Submission)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.verticalLayout_5.addLayout(self.horizontalLayout_5)
        self.tabWidget.addTab(self.tab, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.toolButton_addBook = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_addBook.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_addBook.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("images/addbook.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_addBook.setIcon(icon3)
        self.toolButton_addBook.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_addBook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_addBook.setObjectName("toolButton_addBook")
        self.verticalLayout.addWidget(self.toolButton_addBook)
        self.toolButton_addMember = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_addMember.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_addMember.setFont(font)
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap("images/addmember.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_addMember.setIcon(icon4)
        self.toolButton_addMember.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_addMember.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_addMember.setObjectName("toolButton_addMember")
        self.verticalLayout.addWidget(self.toolButton_addMember)
        self.toolButton_viewBook = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_viewBook.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_viewBook.setFont(font)
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap("images/viewbook .png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_viewBook.setIcon(icon5)
        self.toolButton_viewBook.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_viewBook.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_viewBook.setObjectName("toolButton_viewBook")
        self.verticalLayout.addWidget(self.toolButton_viewBook)
        self.toolButton_viewMember = QtWidgets.QToolButton(self.centralwidget)
        self.toolButton_viewMember.setMaximumSize(QtCore.QSize(160, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.toolButton_viewMember.setFont(font)
        icon6 = QtGui.QIcon()
        icon6.addPixmap(QtGui.QPixmap("images/viewmembers.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.toolButton_viewMember.setIcon(icon6)
        self.toolButton_viewMember.setIconSize(QtCore.QSize(68, 68))
        self.toolButton_viewMember.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolButton_viewMember.setObjectName("toolButton_viewMember")
        self.verticalLayout.addWidget(self.toolButton_viewMember)
        self.horizontalLayout.addLayout(self.verticalLayout)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Library Management System"))
        self.lineEdit_BookID.setPlaceholderText(_translate("MainWindow", "Please Enter Book ID"))
        self.label_BookName.setText(_translate("MainWindow", "Book Name"))
        self.label_BookAuthor.setText(_translate("MainWindow", "Book Author"))
        self.lineEdit_MemberID.setPlaceholderText(_translate("MainWindow", "Please Enter Member ID"))
        self.label_MemberName.setText(_translate("MainWindow", "Member Name"))
        self.label_ContactInfo.setText(_translate("MainWindow", "Contact Info"))
        self.toolButton_issueBook.setText(_translate("MainWindow", "Issue Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Issue Book"))
        self.lineEdit_submission.setPlaceholderText(_translate("MainWindow", "Please Enter Book ID"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Book ID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Member ID"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "New Column"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Renew Count"))
        self.pushButton_renew.setText(_translate("MainWindow", "Renew Book"))
        self.pushButton_Submission.setText(_translate("MainWindow", "Submit Book"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Renew/Submission Book"))
        self.toolButton_addBook.setText(_translate("MainWindow", "Add Book"))
        self.toolButton_addMember.setText(_translate("MainWindow", "Add Member"))
        self.toolButton_viewBook.setText(_translate("MainWindow", "View Book"))
        self.toolButton_viewMember.setText(_translate("MainWindow", "View Member"))

