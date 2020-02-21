"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""
import logging
import settings
import ephem
import datetime

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log'
)


def body(bot, update):

    # bodies_match = [item[-1] for item in ephem._libastro.builtin_planets()]
    text = update.message.text
    body_name = text.split()[-1]
    current_date = datetime.date.today().strftime("%Y/%m/%d")
    try:
        calc_data = getattr(ephem, body_name)(current_date)
        final = ephem.constellation(calc_data)
        update.message.reply_text(f"Планета находится в созвездии {final}")
    except AttributeError:
        update.message.reply_text("Повторите название планеты.")
        # for planet in bodies_match:
        #     if planet.replace("'", "") == body_name:
        #         update.message.reply_text(f"Планета находится в созвездии {final}")
        #         return False





def greet_user(bot, update):
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def talk_to_me(bot, update):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)
 

def main():
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", body))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    
    mybot.start_polling()
    mybot.idle()
       

if __name__ == "__main__":
    main()
