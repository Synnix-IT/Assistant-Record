import sys
import os
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QFileDialog
from PyQt6.QtCore import QCoreApplication
from mainform import Ui_MainWindow

class MainWinMenuToolbar(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWinMenuToolbar, self).__init__(parent)
        self.setupUi(self)
        self.close_action.triggered.connect(self.close)
        self.open_action.triggered.connect(self.OpenFile)
        self.open_calc_action.triggered.connect(lambda : os.system("calc"))
        self.open_notepad_action.triggered.connect(lambda : os.system("notepad"))

    def OpenFile(self):
        filename = QFileDialog.getOpenFileName(self, "開啟檔案", os.getcwd())
        self.statusbar.showMessage(filename)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWinMenuToolbar()
    main.show()
    sys.exit(app.exec())
        

