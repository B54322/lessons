# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'calculatorEYBmwt.ui'
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
        MainWindow.resize(521, 564)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(19, 20, 481, 521))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.screen = QLabel(self.verticalLayoutWidget)
        self.screen.setObjectName(u"screen")

        self.verticalLayout.addWidget(self.screen)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.plus_minus = QPushButton(self.verticalLayoutWidget)
        self.plus_minus.setObjectName(u"plus_minus")

        self.gridLayout.addWidget(self.plus_minus, 3, 0, 1, 1)

        self.multiplication = QPushButton(self.verticalLayoutWidget)
        self.multiplication.setObjectName(u"multiplication")

        self.gridLayout.addWidget(self.multiplication, 2, 3, 1, 1)

        self.b1 = QPushButton(self.verticalLayoutWidget)
        self.b1.setObjectName(u"b1")

        self.gridLayout.addWidget(self.b1, 0, 0, 1, 1)

        self.b5 = QPushButton(self.verticalLayoutWidget)
        self.b5.setObjectName(u"b5")

        self.gridLayout.addWidget(self.b5, 1, 1, 1, 1)

        self.minus = QPushButton(self.verticalLayoutWidget)
        self.minus.setObjectName(u"minus")

        self.gridLayout.addWidget(self.minus, 1, 3, 1, 1)

        self.division = QPushButton(self.verticalLayoutWidget)
        self.division.setObjectName(u"division")

        self.gridLayout.addWidget(self.division, 3, 3, 1, 1)

        self.b4 = QPushButton(self.verticalLayoutWidget)
        self.b4.setObjectName(u"b4")

        self.gridLayout.addWidget(self.b4, 1, 0, 1, 1)

        self.b8 = QPushButton(self.verticalLayoutWidget)
        self.b8.setObjectName(u"b8")

        self.gridLayout.addWidget(self.b8, 2, 1, 1, 1)

        self.b7 = QPushButton(self.verticalLayoutWidget)
        self.b7.setObjectName(u"b7")

        self.gridLayout.addWidget(self.b7, 2, 0, 1, 1)

        self.b6 = QPushButton(self.verticalLayoutWidget)
        self.b6.setObjectName(u"b6")

        self.gridLayout.addWidget(self.b6, 1, 2, 1, 1)

        self.b9 = QPushButton(self.verticalLayoutWidget)
        self.b9.setObjectName(u"b9")

        self.gridLayout.addWidget(self.b9, 2, 2, 1, 1)

        self.b2 = QPushButton(self.verticalLayoutWidget)
        self.b2.setObjectName(u"b2")

        self.gridLayout.addWidget(self.b2, 0, 1, 1, 1)

        self.plus = QPushButton(self.verticalLayoutWidget)
        self.plus.setObjectName(u"plus")

        self.gridLayout.addWidget(self.plus, 0, 3, 1, 1)

        self.point = QPushButton(self.verticalLayoutWidget)
        self.point.setObjectName(u"point")

        self.gridLayout.addWidget(self.point, 3, 2, 1, 1)

        self.b0 = QPushButton(self.verticalLayoutWidget)
        self.b0.setObjectName(u"b0")

        self.gridLayout.addWidget(self.b0, 3, 1, 1, 1)

        self.b3 = QPushButton(self.verticalLayoutWidget)
        self.b3.setObjectName(u"b3")

        self.gridLayout.addWidget(self.b3, 0, 2, 1, 1)

        self.equal = QPushButton(self.verticalLayoutWidget)
        self.equal.setObjectName(u"equal")

        self.gridLayout.addWidget(self.equal, 4, 3, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.screen.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.plus_minus.setText(QCoreApplication.translate("MainWindow", u"+/-", None))
        self.multiplication.setText(QCoreApplication.translate("MainWindow", u"*", None))
        self.b1.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.b5.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.minus.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.division.setText(QCoreApplication.translate("MainWindow", u"/", None))
        self.b4.setText(QCoreApplication.translate("MainWindow", u"4", None))
        self.b8.setText(QCoreApplication.translate("MainWindow", u"8", None))
        self.b7.setText(QCoreApplication.translate("MainWindow", u"7", None))
        self.b6.setText(QCoreApplication.translate("MainWindow", u"6", None))
        self.b9.setText(QCoreApplication.translate("MainWindow", u"9", None))
        self.b2.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.plus.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.point.setText(QCoreApplication.translate("MainWindow", u".", None))
        self.b0.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.b3.setText(QCoreApplication.translate("MainWindow", u"3", None))
        self.equal.setText(QCoreApplication.translate("MainWindow", u"=", None))
    # retranslateUi

