#  Контейнерные типы данных (коллекции)
#    0    1     2     3
a = [23, "ok", True, 3.14]  # список list()
#               -2    -1
b = (23, "ok", True, 3.14)  # кортеж (неизменяемый список) tuple()

c = {"name": "Максим", "age": 15, "street": "25 октября", "apartment": 12}  # словарь dict()
d = {3, "ok", 23, 3, "hello", 'ok'}  # множество (содержит только уникальные элементы) set()

print(c["street"])
print(d)

for k, v in c.items():
    print(k, v)

