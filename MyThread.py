from PyQt5.QtCore import Qt, QThread,pyqtSignal
import socket
import json

class Thread(QThread):
    my_signal = pyqtSignal(dict)  # 自定义信号对象。参数dict就代表这个信号可以传一个字典

    def __init__(self, server):
        super().__init__()
        self.server = server

    def run(self):
        #接收服务器广播的数据
        while True:
            data, addr = self.server.recvfrom(1024)
            data = json.loads(data.decode())
            if len(data):
                #将数据显示在 接收窗口 难道我们还在线程内操作界面吗？
                #可以将数据传输给主线程
                self.my_signal.emit(data)  # 释放信号