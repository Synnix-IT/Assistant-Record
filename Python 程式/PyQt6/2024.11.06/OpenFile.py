import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget
from mainform import Ui_MainWindow


class MainForm(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainForm, self).__init__(parent)
        self.setupUi(self)

        #self.button_close.clicked.connect(self.testSlot)      # 連接按鈕的點擊信號到自訂函式 testSlot

    #def testSlot(self):
    #    print("這是一個自訂函式，你成功了!")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MainForm()
    myWin.show()
    sys.exit(app.exec())