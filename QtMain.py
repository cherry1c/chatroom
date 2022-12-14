import sys
from login.ui import login
import untitled
from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == '__main__':
    myapp = QApplication(sys.argv)

    myDlg = QDialog()
    myUI = untitled.Ui_Dialog()
    myUI.setupUi(myDlg)
    myDlg.hide()
    loginDlg = QDialog()
    loginUI = login.Ui_Dialog()

    loginUI.setupUi(loginDlg, myUI)
    loginDlg.show()

    sys.exit(myapp.exec_())



