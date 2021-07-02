# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'millionaire.ui'
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
        MainWindow.resize(664, 604)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.question = QLabel(self.centralwidget)
        self.question.setObjectName(u"question")
        self.question.setGeometry(QRect(20, 30, 611, 81))
        self.get_question_button = QPushButton(self.centralwidget)
        self.get_question_button.setObjectName(u"get_question_button")
        self.get_question_button.setGeometry(QRect(10, 310, 141, 51))
        self.answer_1 = QRadioButton(self.centralwidget)
        self.answer_1.setObjectName(u"answer_1")
        self.answer_1.setGeometry(QRect(20, 140, 611, 31))
        self.answer_2 = QRadioButton(self.centralwidget)
        self.answer_2.setObjectName(u"answer_2")
        self.answer_2.setGeometry(QRect(20, 190, 611, 31))
        self.answer_3 = QRadioButton(self.centralwidget)
        self.answer_3.setObjectName(u"answer_3")
        self.answer_3.setGeometry(QRect(20, 240, 611, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.question.setText("")
        self.get_question_button.setText(QCoreApplication.translate("MainWindow", u"\u041d\u043e\u0432\u044b\u0439 \u0432\u043e\u043f\u0440\u043e\u0441", None))
        self.answer_1.setText("")
        self.answer_2.setText("")
        self.answer_3.setText("")
    # retranslateUi

