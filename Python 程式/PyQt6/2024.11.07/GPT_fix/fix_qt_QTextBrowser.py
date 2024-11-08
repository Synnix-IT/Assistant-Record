import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QMainWindow,
                             QLineEdit, QTextBrowser, QPushButton,
                             QVBoxLayout, QHBoxLayout, QFrame, QLabel)
from PyQt6.QtCore import QUrl
from PyQt6.QtGui import QTextCursor
from urllib.parse import unquote  # 匯入 unquote 函數
import os

os.chdir(os.path.dirname(__file__))

class TextBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.lineEdit = QLineEdit()
        self.lineEdit.setPlaceholderText("在这里添加你想要的数据，回车确认")
        self.lineEdit.returnPressed.connect(self.append_text)

        self.textBrowser = QTextBrowser()
        self.textBrowser.setAcceptRichText(True)
        self.textBrowser.setOpenExternalLinks(True)
        
        # 使用 setHtml() 方法載入本地 HTML 檔案的內容
        with open(r'.\support\\textBrowser.html', 'r', encoding='utf-8') as f:
            self.textBrowser.setHtml(f.read())

        # 使用 unquote 來解碼 URL
        self.textBrowser.anchorClicked.connect(lambda url: self.statusBar().showMessage(
            '你点击了url ' + unquote(url.toString()), 3000))
        self.textBrowser.backwardAvailable.connect(self.update_navigation_buttons)
        self.textBrowser.forwardAvailable.connect(self.update_navigation_buttons)

        self.back_btn = QPushButton('Back')
        self.forward_btn = QPushButton('Forward')
        self.home_btn = QPushButton('Home')
        self.clear_btn = QPushButton('Clear')

        self.back_btn.pressed.connect(self.textBrowser.backward)
        self.forward_btn.pressed.connect(self.textBrowser.forward)
        self.clear_btn.pressed.connect(self.clear_text)
        self.home_btn.pressed.connect(lambda: self.textBrowser.setHtml(self.initial_html_content))

        layout = QVBoxLayout()
        layout.addWidget(self.lineEdit)
        layout.addWidget(self.textBrowser)
        frame = QFrame()
        layout.addWidget(frame)

        self.text_show = QTextBrowser()
        self.text_show.setMaximumHeight(70)
        layout.addWidget(self.text_show)

        layout_frame = QHBoxLayout()
        layout_frame.addWidget(self.back_btn)
        layout_frame.addWidget(self.forward_btn)
        layout_frame.addWidget(self.home_btn)
        layout_frame.addWidget(self.clear_btn)
        frame.setLayout(layout_frame)

        widget = QWidget()
        self.setCentralWidget(widget)
        widget.setLayout(layout)

        # 初始化頁面 HTML 內容
        self.initial_html_content = self.textBrowser.toHtml()

        self.setWindowTitle('QTextBrowser 案例')
        self.setGeometry(300, 300, 400, 400)
        self.show()

    def append_text(self):
        text = self.lineEdit.text()
        self.textBrowser.append(text)
        self.lineEdit.clear()

    def update_navigation_buttons(self):
        self.back_btn.setEnabled(self.textBrowser.isBackwardAvailable())
        self.forward_btn.setEnabled(self.textBrowser.isForwardAvailable())
        self.update_history_status()

    def update_history_status(self):
        back = "无" if not self.textBrowser.isBackwardAvailable() else "可用"
        now = "当前页面"
        forward = "无" if not self.textBrowser.isForwardAvailable() else "可用"
        _str = f'上一个url: {back},<br>当前url: {now},<br>下一个url: {forward}'
        self.text_show.setText(_str)

    def clear_text(self):
        self.textBrowser.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = TextBrowser()
    sys.exit(app.exec())
