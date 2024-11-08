# Form implementation generated from reading ui file 'LayoutWin2.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_LayoutWin2(object):
    def setupUi(self, LayoutWin2):
        LayoutWin2.setObjectName("LayoutWin2")
        LayoutWin2.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(parent=LayoutWin2)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(parent=self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 120, 461, 121))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_income = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_income.sizePolicy().hasHeightForWidth())
        self.label_income.setSizePolicy(sizePolicy)
        self.label_income.setObjectName("label_income")
        self.verticalLayout.addWidget(self.label_income)
        self.label_drawdown = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(3)
        sizePolicy.setHeightForWidth(self.label_drawdown.sizePolicy().hasHeightForWidth())
        self.label_drawdown.setSizePolicy(sizePolicy)
        self.label_drawdown.setObjectName("label_drawdown")
        self.verticalLayout.addWidget(self.label_drawdown)
        self.label_sharp = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_sharp.sizePolicy().hasHeightForWidth())
        self.label_sharp.setSizePolicy(sizePolicy)
        self.label_sharp.setObjectName("label_sharp")
        self.verticalLayout.addWidget(self.label_sharp)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.formLayout.setObjectName("formLayout")
        self.label_min = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_min.setObjectName("label_min")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.LabelRole, self.label_min)
        self.label_max = QtWidgets.QLabel(parent=self.horizontalLayoutWidget)
        self.label_max.setObjectName("label_max")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.ItemRole.FieldRole, self.label_max)
        self.spin_income_min = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.spin_income_min.setObjectName("spin_income_min")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.LabelRole, self.spin_income_min)
        self.spin_income_max = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.spin_income_max.setObjectName("spin_income_max")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spin_income_max)
        self.spin_drawdown_min = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.spin_drawdown_min.setObjectName("spin_drawdown_min")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.LabelRole, self.spin_drawdown_min)
        self.spin_drawdown_max = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.spin_drawdown_max.setObjectName("spin_drawdown_max")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spin_drawdown_max)
        self.spin_sharp_min = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.spin_sharp_min.setObjectName("spin_sharp_min")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.LabelRole, self.spin_sharp_min)
        self.spin_sharp_max = QtWidgets.QDoubleSpinBox(parent=self.horizontalLayoutWidget)
        self.spin_sharp_max.setObjectName("spin_sharp_max")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.ItemRole.FieldRole, self.spin_sharp_max)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(200, 20, QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(parent=self.horizontalLayoutWidget)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        self.button_start = QtWidgets.QPushButton(parent=self.horizontalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.button_start.sizePolicy().hasHeightForWidth())
        self.button_start.setSizePolicy(sizePolicy)
        self.button_start.setMinimumSize(QtCore.QSize(100, 100))
        self.button_start.setMaximumSize(QtCore.QSize(300, 300))
        self.button_start.setObjectName("button_start")
        self.horizontalLayout.addWidget(self.button_start)
        LayoutWin2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=LayoutWin2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        LayoutWin2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent=LayoutWin2)
        self.statusbar.setObjectName("statusbar")
        LayoutWin2.setStatusBar(self.statusbar)
        self.label_income.setBuddy(self.spin_income_min)
        self.label_drawdown.setBuddy(self.spin_drawdown_min)
        self.label_sharp.setBuddy(self.spin_sharp_min)

        self.retranslateUi(LayoutWin2)
        QtCore.QMetaObject.connectSlotsByName(LayoutWin2)

    def retranslateUi(self, LayoutWin2):
        _translate = QtCore.QCoreApplication.translate
        LayoutWin2.setWindowTitle(_translate("LayoutWin2", "MainWindow"))
        self.label_income.setText(_translate("LayoutWin2", "&收益"))
        self.label_drawdown.setText(_translate("LayoutWin2", "&最大回撤"))
        self.label_sharp.setText(_translate("LayoutWin2", "&Sharp比"))
        self.label_min.setText(_translate("LayoutWin2", "最小值"))
        self.label_max.setText(_translate("LayoutWin2", "最大值"))
        self.button_start.setText(_translate("LayoutWin2", "開始"))
