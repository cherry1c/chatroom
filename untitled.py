# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
from MyThread import Thread
import json


ip = "172.20.10.5"
port = 6666
selfPort = 8888

send_data = {
    "type": "",
    "name": "",
    "status": 0,
    "data": ""
}


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(845, 619)
        font = QtGui.QFont()
        font.setPointSize(14)
        Dialog.setFont(font)
        self.Dialog = Dialog
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(40, 30, 491, 451))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(580, 30, 231, 451))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(40, 490, 491, 71))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(580, 490, 111, 71))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(Dialog)
        self.lineEdit.setGeometry(QtCore.QRect(40, 570, 221, 41))
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(290, 580, 91, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.lineEdit.hide()
        self.pushButton_2.hide()

        self.s_name = ""
        self.retranslateUi(Dialog)
        self.pushButton.clicked.connect(self.sendData)
        # self.pushButton_2.clicked.connect(self.login)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def socket_init(self):
        ip = self.lineEdit.text()
        s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
        s.bind((ip, selfPort))
        print("bind success. addr ", ip, selfPort)
        return s


    def login(self, user):
        send_data["type"] = "login"
        send_data["data"] = json.dumps(user)
        send_data["name"] = user["name"]
        self.s = self.socket_init()
        self.thread_init()

    def register_login(self, user):
        print("register_login")
        send_data["type"] = "register_login"
        send_data["data"] = json.dumps(user)
        send_data["name"] = user["name"]
        self.s = self.socket_init()
        self.thread_init()
        self.Dialog.show()

    def thread_init(self):
        self.s_name = send_data["name"]
        self.thread = Thread(self.s, json.dumps(send_data))
        # 如果子线程发射了信号，则执行show_cli_data函数
        self.thread.my_signal.connect(self.show_cli_data)
        self.thread.start()  # 运行线程

    def show_cli_data(self, recv_data):
        print(recv_data)
        if recv_data["type"] == "login" or recv_data["type"] == "register_login":
            print(recv_data["name"])
            print(self.s_name)
            if recv_data["name"] == self.s_name:
                self.s_status = recv_data["status"]
                if recv_data["status"] == 0:
                    print("login failed")
                    return
                else:
                    print("login success")
                    self.s_name = recv_data["name"]
            if recv_data["status"] == 0:
                return
            self.textEdit_2.insertPlainText(str(recv_data["name"]) + " 已上线")
            return
        elif recv_data["type"] == "test":
            data = {"type": "/test"}
            data["name"] = self.s_name
            self.s.sendto(bytes(json.dumps(data), encoding="utf8"), (ip, port))
            self.textEdit_2.setText("")
            return
        elif recv_data["type"] == "set":
            self.textEdit_2.insertPlainText(str(recv_data["name"]))
            return
        self.textEdit.insertPlainText(str(recv_data["name"]) + ": " + recv_data["data"] + "\n")

    def sendData(self):
        send_data = dict()
        if self.s_status == 0:
            return
        send_data["type"] = "msg"
        send_data["name"] = self.s_name
        send_data["data"] = self.textEdit_3.toPlainText()
        self.textEdit_3.clear()
        self.s.sendto(bytes(json.dumps(send_data), encoding="utf8"), (ip, port))


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "发送"))
        # self.pushButton_2.setText(_translate("Dialog", "登录"))
