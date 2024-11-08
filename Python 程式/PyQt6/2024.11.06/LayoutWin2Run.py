from PyQt6.QtCore import pyqtSlot
from PyQt6.QtWidgets import QApplication, QMainWindow

from layoutwin2 import Ui_LayoutWin2

class LayoutWin2(QMainWindow, Ui_LayoutWin2):

    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(LayoutWin2, self).__init__(parent)
        self.setupUi(self)

    @pyqtSlot()
    def on_button_start_clicked(self):
        """
        Slot documentation goes here.
        """
        print("收益_min:", self.spin_income_min.value())
        print("收益_max:", self.spin_income_max.value())

        print("最大回撤_min:", self.spin_drawdown_min.value())
        print("最大回撤_max:", self.spin_drawdown_max.value())

        print("Sharp比_min:", self.spin_sharp_min.value())
        print("Sharp比_max:", self.spin_sharp_max.value())

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = LayoutWin2()
    ui.show()
    sys.exit(app.exec())