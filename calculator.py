#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6 import QtCore
# импортируем связанный py файл с нашим ui файлом
from design_calculator import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
		# вызовем метод родительского класса
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        self.ui.b1.clicked.connect(self.pushed_button)
        self.ui.b2.clicked.connect(self.pushed_button)
        self.ui.b3.clicked.connect(self.pushed_button)
        self.ui.b4.clicked.connect(self.pushed_button)
        self.ui.b5.clicked.connect(self.pushed_button)
        self.ui.b6.clicked.connect(self.pushed_button)
        self.ui.b7.clicked.connect(self.pushed_button)
        self.ui.b8.clicked.connect(self.pushed_button)




    # функция при нажатии на кнопку
    def pushed_button(self):
        self.button = self.sender()
        self.ui.screen.setText(self.button.text())


if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
