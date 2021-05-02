# тип фигуры: 
# прямоугольник, стороны a, b  | s = a*b
# треугольник, стороны a, b, c  | s = Vp*(p-a)*(p-b)*(p-c), где p=(a+b+c)/2, V81 = 81**0.5
# круг радиус r | s = P*R**2
# вывести площадь s
while  True:
    t = int(input('''Введите тип фигуры
    1 - прямоугольник
    2 - треугольник
    3 - круг
    '''))

    if t == 1:
        a = int(input('Введите первую сторону\n'))
        b = int(input('Введите вторую сторону\n'))
        s = a * b
    elif t == 2:
        a = int(input('Введите первую сторону\n'))
        b = int(input('Введите вторую сторону\n'))
        c = int(input('Введите третью сторону\n'))
        p = (a + b + c)/2
        s = p**0.5*(p-a)*(p-b)*(p-c)
    elif t == 3:
        a = int(input('Введите радиус\n')) 
        s = a**2*3.14
    print(f'Площадь равна: {s}')