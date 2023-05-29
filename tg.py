import telebot
from googletrans import Translator
from langdetect import detect

# Создаем переводчик
translator = Translator()
bot = telebot.TeleBot('5970069277:AAEGlfiW4MF4F4wJgO8pr1qVx_GZczvpGoA')
# Определяем функцию для обработки сообщений
@bot.message_handler(func=lambda m: True)
def translate_message(message):
  # Определяем язык исходного текста
  src = detect(message.text)

  # Задаем целевой язык
  dest = 'ru'