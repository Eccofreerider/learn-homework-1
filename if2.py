"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
first_input = input("Введите строку 1: ")
second_input = input("Введите строку 2: ")

def main(string_one, string_two):
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    if not isinstance(string_one, str) or not isinstance(string_two, str):
        # print('0')
        return 0
    elif string_one == string_two:
        # print('1')
        return 1
    elif string_one != string_two and len(string_one) > len(string_two) and not "learn" in string_two.lower():
        # print('2')
        return 2
    elif string_one != string_two and "learn" in string_two.lower():
        # print('3')
        return 3
    else:
        print('Ошибка')


if __name__ == "__main__":
    print(main(first_input, second_input))
