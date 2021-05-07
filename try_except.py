# print(eval(input()))
while True:
    try:
        n1 = float(input('введите первое число\n'))
        sign = input('введите знак\n')
        n2 = float(input('введите второе число\n'))

        if sign == '+':
            s = n1 + n2
        elif sign == '-':
            s = n1 - n2
        elif sign == '*':
            s = n1 * n2
        elif sign == '/':
            s = n1 / n2
        
        s = str(s)

        if s[-2:] == '.0':
            s = s[:-2]

        print(f'Ответ: {s}')

    except ValueError:
        print("До скорых встреч!")
        break
    except ZeroDivisionError:
        print('Чувак, делить на ноль нельзя :) !!!')    