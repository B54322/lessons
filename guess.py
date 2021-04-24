from random import randint

name = input("Как вас зовут?\n")

play = "да"

# запустим программу в цикле
while play == "да":
    # Попросим ввести число
    user_number = int(input(f"{name}, до скольки загадать мне число?\n"))
    # Загадаем число
    guessed_number = randint(1, user_number)
    # Количество попыток
    attempts = 4

    ok = False


    print(f"Хорошо, {name}, я загадал число от 1 до {user_number}")

    for i in range(attempts):
        answer = int(input(f"Попытка {i+1}:\n"))
        if answer > guessed_number:
            print("Слишком много!")
        elif answer < guessed_number:
            print("Слишком мало!")
        else:
            print("Угадал")
            ok = True
            break
    if ok == False:
        print(f"Я загадал число {guessed_number}")
        
    play = input('Еще попытаешь удачу? (да/нет)\n')
