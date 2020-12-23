import telebot as tb

bot = tb.TeleBot('1481133710:AAHc6yyPa3bQJcV86C2HQ9xBmpxNPh-h1hk')
keyboard1 = tb.types.ReplyKeyboardMarkup(True)
keyboard1.row('Price', 'Contacts', 'Help')


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Это телеграм-бот @irishaa_antonova, чем могу помочь?',
                     reply_markup=keyboard1)


@bot.message_handler(content_types=['text'])
def parse_input_message(message):
    if message.text.lower() == 'help':
        bot.send_message(message.chat.id, 'helped help\n\n\n')
    elif message.text.lower() == 'price':
        img = open("/Users/ozahirnyi/PycharmProjects/tgBot/images/test_screen.png", 'rb')
        bot.send_message(message.chat.id, "Улыбка на Миллион! : 327 гривень")
        bot.send_photo(message.chat.id, img)


bot.polling()
