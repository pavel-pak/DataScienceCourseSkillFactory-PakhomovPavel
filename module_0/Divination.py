import numpy as np

def gadalka(number):
    upper = 100  # верхняя граница интервала
    lower = 0  # нижняя граница интервала
    Start_number = 50  # стартовое число
    count = 0  # счетчик
    while number != Start_number:  # цикл пока не найду нужное число
        count += 1  # add count
        if number > Start_number:  # если число больше стартового
            if number == upper: # проверка на крайнее значение
                count += 1
                Start_number = number
            else:
                lower = Start_number  # корректирую нижнюю границу
                Start_number += round((upper - lower) / 2)  # новое стартовое числа
        elif number < Start_number:  # если число меньше стартового
            if number == lower: # проверка на крайнее значение
                count += 1
                Start_number = lower
            else:
                upper = Start_number  # корректирую верхнюю границу
                Start_number -= round((upper - lower) / 2)  # новое стартовое число
    return count


"""

test programme 

"""


def Test_programm():
    m =0
    for i in range(1, 101):
        number = np.random.randint(1, 101)
        try:
           n = gadalka(number)

        except:
            print(number)

        print(f"<{i}> Задананое число |{number}|")
        print(f"Гадание выполнено за ***|{n}|***")
        m += n
    print(f" средние кол-во шагов для разгадки - {round(m/100)}")


# запуск стартовой программы
Test_programm()

