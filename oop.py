# Класс (чертёж)
class House:
    # метод build (функция)
    def build(self, wl, dr, wn): 
        self.walls = wl  # свойство/параметр
        self.doors = dr
        self.windows = wn

    def get_info(self):
        print(f'''
        ИНФОРМАЦИЯ О ДОМЕ:
        Стены: {self.walls}
        Двери: {self.doors}
        Количество окон: {self.windows}
        ''')

# Создадим объекты
max_house = House()
ivan_house = House()

max_house.build("кирпич", "дерево", 4)
max_house.get_info()

ivan_house.build("бетон", "железо", 5)
ivan_house.get_info()
