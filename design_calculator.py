# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculator.ui'
##
## Created by: Qt User Interface Compiler version 6.0.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(374, 377)
        icon = QIcon()
        icon.addFile(u"img/icon.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet(u"QMainWindow\n"
"{\n"
"	background-color: rgb(0, 85, 127);\n"
"}\n"
"\n"
"QPushButton\n"
"{\n"
"	font: 700 24pt \"Script MT Bold\";\n"
"	background-color: rgb(0, 255, 0);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 80, 351, 281))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.b8 = QPushButton(self.layoutWidget)
        self.b8.setObjectName(u"b8")

        self.gridLayout.addWidget(self.b8, 3, 1, 1, 1)

        self.b6 = QPushButton(self.layoutWidget)
        self.b6.setObjectName(u"b6")

        self.gridLayout.addWidget(self.b6, 2, 2, 1, 1)

        self.minus = QPushButton(self.layoutWidget)
        self.minus.setObjectName(u"minus")

        self.gridLayout.addWidget(self.minus, 1, 3, 1, 1)

        self.b5 = QPushButton(self.layoutWidget)
        self.b5.setObjectName(u"b5")

        self.gridLayout.addWidget(self.b5, 2, 1, 1, 1)

        self.b1 = QPushButton(self.layoutWidget)
        self.b1.setObjectName(u"b1")

        self.gridLayout.addWidget(self.b1, 1, 0, 1, 1)

        self.plus = QPushButton(self.layoutWidget)
        self.plus.setObjectName(u"plus")

        self.gridLayout.addWidget(self.plus, 0, 3, 1, 1)

        self.b9 = QPushButton(self.layoutWidget)
        self.b9.setObjectName(u"b9")

        self.gridLayout.addWidget(self.b9, 3, 2, 1, 1)

        self.plus_minus = QPushButton(self.layoutWidget)
        self.plus_minus.setObjectName(u"plus_minus")

        self.gridLayout.addWidget(self.plus_minus, 4, 0, 1, 1)

        self.backspace = QPushButton(self.layoutWidget)
        self.backspace.setObjectName(u"backspace")

        self.gridLayout.addWidget(self.backspace, 0, 2, 1, 1)

        self.point = QPushButton(self.layoutWidget)
        self.point.setObjectName(u"point")

        self.gridLayout.addWidget(self.point, 4, 2, 1, 1)

        self.b3 = QPushButton(self.layoutWidget)
        self.b3.setObjectName(u"b3")

        self.gridLayout.addWidget(self.b3, 1, 2, 1, 1)

        self.b4 = QPushButton(self.layoutWidget)
        self.b4.setObjectName(u"b4")

        self.gridLayout.addWidget(self.b4, 2, 0, 1, 1)

        self.b7 = QPushButton(self.layoutWidget)
        self.b7.setObjectName(u"b7")

        self.gridLayout.addWidget(self.b7, 3, 0, 1, 1)

        self.b2 = QPushButton(self.layoutWidget)
        self.b2.setObjectName(u"b2")

        self.gridLayout.addWidget(self.b2, 1, 1, 1, 1)

        self.b0 = QPushButton(self.layoutWidget)
        self.b0.setObjectName(u"b0")

        self.gridLayout.addWidget(self.b0, 4, 1, 1, 1)

        self.multiplication = QPushButton(self.layoutWidget)
        self.multiplication.setObjectName(u"multiplication")

        self.gridLayout.addWidget(self.multiplication, 2, 3, 1, 1)

        self.division = QPushButton(self.layoutWidget)
        self.division.setObjectName(u"division")

        self.gridLayout.addWidget(self.division, 3, 3, 1, 1)

        self.equal = QPushButton(self.layoutWidget)
        self.equal.setObjectName(u"equal")

        self.gridLayout.addWidget(self.equal, 4, 3, 1, 1)

        self.sqrt = QPushButton(self.layoutWidget)
        self.sqrt.setObjectName(u"sqrt")

        self.gridLayout.addWidget(self.sqrt, 0, 0, 1, 1)

        self.clear = QPushButton(self.layoutWidget)
        self.clear.setObjectName(u"clear")

        self.gridLayout.addWidget(self.clear, 0, 1, 1, 1)

        self.screen = QLabel(self.centralwidget)
        self.screen.setObjectName(u"screen")
        self.screen.setGeometry(QRect(10, 10, 351, 61))
        self.screen.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"font: 700 60pt \"Script MT Bold\";\n"
"")
        self.screen.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u041a\u0410\u041b\u042c\u041a\u0423\u041b\u042f\u0422\u041e\u0420", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.plus_minus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.backspace.setText(QCoreApplication.translate("MainWindow", u"\u232b", None))
        self.point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.multiplication.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
        self.sqrt.setText(QCoreApplication.translate("MainWindow", u"\u221a", None))
        self.clear.setText(QCoreApplication.translate("MainWindow", u"\u00a9", None))
        self.screen.setText(QCoreApplication.translate("MainWindow", u"0", None))
    # retranslateUi

