from back.config import bot, main_keyboard, start_keyboard
import back.binary as bin_tree


# Start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Это телеграм-бот @irishaa_antonova, чем могу помочь?',
                     reply_markup=main_keyboard)


# Main button pressed
@bot.message_handler(content_types=['text'])
def parse_input_message(message):
    if message.text.lower() == 'help':
        bot.send_message(message.chat.id, "Подобрать макияж онлайн      Тупа сразу заказать.",
                         reply_markup=start_keyboard)
    elif message.text.lower() == 'price':
        img = open("resources/test_screen.png", 'rb')
        bot.send_message(message.chat.id, "Улыбка на Миллион! : 327 гривень")
        bot.send_photo(message.chat.id, img)
    elif message.text.lower() == 'contacts':
        bot.send_message(message.chat.id, "instagram: @irisha_beauty"
                                          "\n\ntelegram: @irishaa_antonova"
                                          "\n\nphone: +380952180492")


@bot.callback_query_handler(func=lambda call: True)
def help_handler(call):
    if call.message:
        if call.data == "Zakazat":
            for i in range(0, 5):
                img = open("resources/test_screen.png", 'rb')
                bot.send_message(call.message.chat.id, "Rabota #" + str(i))
                bot.send_photo(call.message.chat.id, img)
        elif call.data == "Vibrat":
            bot.send_message(call.message.chat.id, "tut buted binary tree)")
            bin_tree.main(call)


bot.polling()
