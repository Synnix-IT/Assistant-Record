# Form implementation generated from reading ui file 'LayoutFirst.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LayoutFirst(object):
    def setupUi(self, LayoutFirst):
        LayoutFirst.setObjectName("LayoutFirst")
        LayoutFirst.resize(800, 600)
        LayoutFirst.setMinimumSize(QtCore.QSize(0, 0))
        LayoutFirst.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.horizontalLayout = QtWidgets.QHBoxLayout(LayoutFirst)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.line_hi = QtWidgets.QLineEdit(parent=LayoutFirst)
        self.line_hi.setEnabled(True)
        font = QtGui.QFont()
        font.setFamily("標楷體")
        font.setPointSize(15)
        font.setKerning(False)
        self.line_hi.setFont(font)
        self.line_hi.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.line_hi.setObjectName("line_hi")
        self.verticalLayout.addWidget(self.line_hi)
        self.pushButton = QtWidgets.QPushButton(parent=LayoutFirst)
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.button_1 = QtWidgets.QPushButton(parent=LayoutFirst)
        font = QtGui.QFont()
        font.setFamily("新細明體")
        font.setPointSize(12)
        font.setBold(True)
        self.button_1.setFont(font)
        self.button_1.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.button_1.setObjectName("button_1")
        self.verticalLayout.addWidget(self.button_1)
        self.horizontalLayout.addLayout(self.verticalLayout)

        self.retranslateUi(LayoutFirst)
        QtCore.QMetaObject.connectSlotsByName(LayoutFirst)

    def retranslateUi(self, LayoutFirst):
        _translate = QtCore.QCoreApplication.translate
        LayoutFirst.setWindowTitle(_translate("LayoutFirst", "Form"))
        self.line_hi.setText(_translate("LayoutFirst", "嗨你好"))
        self.pushButton.setText(_translate("LayoutFirst", "PushButton"))
        self.button_1.setText(_translate("LayoutFirst", "我是按鈕"))
