import socket
import json
from MyThread import Thread
from PyQt5.QtCore import Qt, QThread,pyqtSignal
import time
s = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#设置可以广播
s.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)

s.bind(("172.20.10.5", 6666))

cli_list = []
send_data = {
    "type": "",
    "addr": "",
    "data": ""
}
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
            send_data["type"] = "test"
            send_data["addr"] = ""
            send_data["data"] = "!!!!!!!!!"
            cli_list.clear()
            s.sendto(bytes(json.dumps(send_data), encoding='utf8'), ("<broadcast>", 8888))
            self.my_signal.emit()  # 释放信号

thread = Thread()
thread.start()  # 运行线程



while True:
    data, addr = s.recvfrom(1024)
    send_data["data"] = data.decode()
    send_data["addr"] = addr
    if addr in cli_list:
        send_data["type"] = "old"
    else:
        send_data["type"] = "new"
        cli_list.append(addr)
    if send_data["data"] == "/test":
        send_data["type"] = "set"
    s.sendto(bytes(json.dumps(send_data), encoding='utf8'), ("<broadcast>", 8888))
