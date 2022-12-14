# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog, client):
        Dialog.setObjectName("Dialog")
        Dialog.resize(625, 393)
        self.client = client
        self.btn_login = QtWidgets.QPushButton(Dialog)
        self.btn_login.setGeometry(QtCore.QRect(200, 240, 75, 23))
        self.btn_login.setObjectName("btn_login")
        self.btn_register = QtWidgets.QPushButton(Dialog)
        self.btn_register.setGeometry(QtCore.QRect(340, 240, 75, 23))
        self.btn_register.setObjectName("btn_register")
        self.line_edit_password = QtWidgets.QLineEdit(Dialog)
        self.line_edit_password.setGeometry(QtCore.QRect(260, 190, 151, 31))
        self.line_edit_password.setObjectName("line_edit_password")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(210, 200, 41, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(210, 160, 41, 16))
        self.label_2.setObjectName("label_2")
        self.line_edit_username = QtWidgets.QLineEdit(Dialog)
        self.line_edit_username.setGeometry(QtCore.QRect(260, 150, 151, 31))
        self.line_edit_username.setObjectName("line_edit_username")

        self.btn_login.clicked.connect(self.login)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def login(self):
        self.client.show()

    def print_log(self):
        print("clicked")

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.btn_login.setText(_translate("Dialog", "登录"))
        self.btn_register.setText(_translate("Dialog", "注册"))
        self.label.setText(_translate("Dialog", "密码"))
        self.label_2.setText(_translate("Dialog", "用户名"))
