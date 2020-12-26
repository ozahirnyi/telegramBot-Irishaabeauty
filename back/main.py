import telebot as tb

bot = tb.TeleBot('1481133710:AAHc6yyPa3bQJcV86C2HQ9xBmpxNPh-h1hk')

# Main keyboard
main_keyboard = tb.types.ReplyKeyboardMarkup(True)
main_keyboard.row('Price', 'Contacts', 'Help')

# Start keyboard
s_key_b1 = tb.types.InlineKeyboardButton(text="Заказать", callback_data="Zakazat")
s_key_b2 = tb.types.InlineKeyboardButton(text="Подобрать", callback_data="Vibrat")
start_keyboard = tb.types.InlineKeyboardMarkup()
start_keyboard.add(s_key_b2, s_key_b1)


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
        bot.send_message(message.chat.id, "instagram: @irisha_abeauty"
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


bot.polling()
