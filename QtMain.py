import sys
import untitled
from PyQt5.QtWidgets import QApplication, QDialog

if __name__ == '__main__':
    myapp = QApplication(sys.argv)
    myDlg = QDialog()
    myUI = untitled.Ui_Dialog()
    myUI.setupUi(myDlg)
    myDlg.show()

    sys.exit(myapp.exec_())


