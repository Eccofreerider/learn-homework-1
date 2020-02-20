"""

Домашнее задание №1

Цикл while: ask_user со словарём

* Создайте словарь типа "вопрос": "ответ", например: 
  {"Как дела": "Хорошо!", "Что делаешь?": "Программирую"} и так далее
* Напишите функцию ask_user_dict() которая с помощью input() просит 
  пользователя ввести вопрос, а затем, если вопрос есть в словаре, 
  программа давала ему соотвествующий ответ. Например:

    Пользователь: Что делаешь?
    Программа: Программирую
    
"""
phrases = {"Как дела?":"Отлично!",
           "Что делаешь?":"Решаю задачи по python",
           "Что нового?":"Записался на курс по python",
           "Сколько тебе лет?":"32",
           "Привет!":"Салют!"}


def ask_user():
    """
    Замените pass на ваш код
    """
    while True:
        ask_question = input("Задай вопрос: ")
        for n in phrases:
            if n == ask_question:
                print(phrases.get(ask_question))
            else:
                print("Задайте вопрос из списка.")

if __name__ == "__main__":
    ask_user()
