# Берем полученное сообщение и переводим его
  translated_text = translator.translate(message.text, src=src, dest=dest).text

  # Отправляем переведенное сообщение
  bot.send_message(message.chat.id, translated_text)

# Запускаем бота
bot.polling(none_stop=True)