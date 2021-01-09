from back.config import bot, main_keyboard, start_keyboard
import back.binary as binary
import back.callback as callback


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
    elif message.text.lower() == 'мои работы':
        callback.myWorks(message)
    elif message.text.lower() == '📝 как записаться':
        callback.offers(message)
    elif message.text.lower() == '👸🏼 подобрать образ':
        print('qwe')
        binary.main(message)
    elif message.text.lower() == 'price':
        img = open("resources/test_screen.png", 'rb')
        bot.send_message(message.chat.id, "Улыбка на Миллион! : 327 гривень")
        bot.send_photo(message.chat.id, img)
    elif message.text.lower() == 'contacts':
        bot.send_message(message.chat.id, "instagram: @irisha_beauty"
                                          "\n\ntelegram: @irishaa_antonova"
                                          "\n\nphone: +380952180492")
    else:
        bot.send_message(message.chat.id, "Oops something wrong!", reply_markup=main_keyboard)


# Inline button pressed
@bot.callback_query_handler(func=lambda call: True)
def help_handler(call):
    if call.message:
        if call.data == "First" or call.data == "Second":
            binary.tree_helper_init(call)
        else:
            bot.send_message(call.message.chat.id, "Oops, something wrong!", main_keyboard)


bot.polling()
