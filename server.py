import socket
import json
from MyThread import Thread
from PyQt5.QtCore import Qt, QThread,pyqtSignal
import time
import db.user

s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#设置可以广播
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("172.20.10.5", 6666))

cli_list = []

# def heartbeat():
#     print("------------------------")
#     send_data["type"] = "test"
#     send_data["addr"] = ""
#     send_data["data"] = "!!!!!!!!!"
#     print("begin heart")
#     s.sendto(bytes(json.dumps(send_data), encoding='utf8'), ("<broadcast>", 8888))
#
# timer = QTimer()  # 初始化定时器
# timer.timeout.connect(heartbeat)
# timer.start(1000)  # 设置计时间隔并启动



class Thread(QThread):
    my_signal = pyqtSignal()
    def __init__(self):
        super().__init__()

    def run(self):
        while True:
            time.sleep(1)
            data = {"type": "test"}
            s.sendto(bytes(json.dumps(data), encoding='utf8'), ("<broadcast>", 8888))
            self.my_signal.emit()  # 释放信号

thread = Thread()
thread.start()  # 运行线程

def login(recv_data):
    data = json.loads(recv_data)
    result = db.user.get_user(data["name"])
    if len(result) != 1 or result[0].password != data["password"]:
        send_data["status"] = 0
        return
    send_data["status"] = 1
    send_data["name"] = data["name"]
    return send_data


def register_login(recv_data, addr):
    data = json.loads(recv_data)
    user = db.user.User()
    user.name = data["name"]
    user.password = data["password"]
    user.age = data["age"]
    user.gender = data["gender"]
    user.address = data["address"]
    user.net_address = addr[0] + ":" + str(addr[1])
    db.user.add_user(user)
    send_data["name"] = data["name"]
    send_data["status"] = 1
    return send_data


while True:
    data, addr = s.recvfrom(1024)
    send_data = json.loads(data.decode())
    print(send_data)
    if addr in cli_list:
        pass
    else:
        if send_data["type"] == "login":
            send_data = login(send_data["data"])
        elif send_data["type"] == "register_login":
            send_data = register_login(send_data["data"], addr)
        cli_list.append(addr)
    if send_data["type"] == "/test":
        send_data["type"] = "set"
    s.sendto(bytes(json.dumps(send_data), encoding='utf8'), ("<broadcast>", 8888))
