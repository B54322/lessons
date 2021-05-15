def kassa(money, col):
    price = 150
    tickets = col * price
    change = money - tickets
    if change < 0:
        print('К оплате ещё: ', change)
    else:
        print('Сдача: ', change)
    print('Стоимость: ', tickets)
    

kassa(350, 5)
kassa(1000, 4)