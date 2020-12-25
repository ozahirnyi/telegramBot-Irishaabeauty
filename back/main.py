import telebot as tb

bot = tb.TeleBot('1481133710:AAHc6yyPa3bQJcV86C2HQ9xBmpxNPh-h1hk')

# Main keyboard
keyboard1 = tb.types.ReplyKeyboardMarkup(True)
keyboard1.row('Price', 'Contacts', 'Help')
help_str = "*Price:* Типы макиажа.\n          Цены.\n\n" \
           "*Contacts:* телега - ...\n" \
           "                инста - ...\n" \
           "                номер - ...\n"
# Start keyboard
s_key_b1 = tb.types.InlineKeyboardButton(text="Заказать", callback_data="Zakazat")
s_key_b2 = tb.types.InlineKeyboardButton(text="Подобрать", callback_data="Vibrat")
start_keyboard = tb.types.InlineKeyboardMarkup()
start_keyboard.add(s_key_b2, s_key_b1)


# Start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Это телеграм-бот @irishaa_antonova, чем могу помочь?',
                     reply_markup=start_keyboard)


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


bot.polling()
