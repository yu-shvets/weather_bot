import telebot
from telebot import types
from forecast import day_forecast


token = '398499334:AAEAaTVquTv_pju9C9bxMUIhv_21RgleLmA'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start', 'help'])
def start_message(message):
    bot.reply_to(message, 'Hello! Welcome to TodayWeather. Please, enter city name:')


@bot.message_handler(content_types=['text'])
def today_forecast(message):
    weather = day_forecast(message.text)
    bot.send_message(message.chat.id, weather)


if __name__ == '__main__':
    bot.polling(none_stop=True)
