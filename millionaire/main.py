#! /usr/bin/env python
# -*- coding: utf-8 -*-

from json import load
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QDialog
from PySide6 import QtCore
# импортируем связанный py файл с нашим ui файлом
from millionaire import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
		# вызовем метод родительского класса
        super(MainWindow, self).__init__()

        # создадим объект
        self.ui = Ui_MainWindow()
        # инициализируем нашу форму
        self.ui.setupUi(self)

        # Соединим сигналы со слотами
        self.ui.get_question_button.clicked.connect(self.get_new_question)

        with open("millionaire/questions.json", 'r') as file:
            self.questions = load(file)
            self.questions = self.questions["games"][0]["questions"]


    # функция при нажатии на кнопку
    def get_new_question(self):
        print(self.questions)
        question = self.questions.pop()
        self.ui.question.setText(question['question'])
        counter = 0
        for answer in question['content']:
            counter += 1
            exec(f"self.ui.answer_{counter}.setText('{answer}')")

        

if __name__ == "__main__":
    # Создадим Qt Application
    app = QApplication(sys.argv)
    # Создадим и покажем главное окно
    window = MainWindow()
    # Показываем окно
    window.show()
    # Запустим приложение
    sys.exit(app.exec_())

