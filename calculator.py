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
        self.ui.b9.clicked.connect(self.pushed_button)
        self.ui.b0.clicked.connect(self.pushed_button)

        self.ui.plus.clicked.connect(self.pushed_button)
        self.ui.minus.clicked.connect(self.pushed_button)
        self.ui.multiplication.clicked.connect(self.pushed_button)
        self.ui.division.clicked.connect(self.pushed_button)
        self.ui.equal.clicked.connect(self.equal)

        self.ui.clear.clicked.connect(self.clear)
        self.ui.backspace.clicked.connect(self.backspace)
        self.ui.sqrt.clicked.connect(self.sqrt)
        self.ui.plus_minus.clicked.connect(self.minus_plus)
        self.ui.point.clicked.connect(self.pushed_button)
        # значение экрана
        self.screen = ''
        self.minus = False

    # функция при нажатии на кнопку
    def pushed_button(self):
        self.button = self.sender()
        self.screen += self.button.text()
        self.ui.screen.setText(self.screen)

    def equal(self):
        self.screen = str(eval(self.screen))
        print(self.screen)
        position = self.screen.find('.')
        if position != -1:
            if len(self.screen[position+1:])>3:
                rounded = self.screen[position+1:position+4]
                self.screen = f'{self.screen[:position+1]}{rounded}'
                print(self.screen)
                self.ui.screen.setText(self.screen)

        else:
            self.ui.screen.setText(self.screen)
        self.ui.screen.setText(self.screen)

    def clear(self):
        self.screen = ''
        self.ui.screen.setText('0')
        self.minus = False

    def backspace(self):
        self.screen = self.screen[:-1]
        self.ui.screen.setText(self.screen)

    def sqrt(self):
        self.screen = str(int(self.screen)**0.5)
        self.ui.screen.setText(self.screen)
    
    def minus_plus(self):
        if not self.minus:
            self.screen = f'-{self.screen}'
            self.minus = True
        else:
            self.screen = self.screen[1:]
            self.minus = False
        
        self.ui.screen.setText(self.screen)

if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())
