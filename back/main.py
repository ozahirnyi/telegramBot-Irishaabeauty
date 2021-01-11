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
    bot.send_message(message.chat.id, 'yo sobaki')
    if message.text.lower() == 'мои работы':
        callback.myWorks(message)
    elif message.text.lower() == '📝 как записаться':
        callback.offers(message)
    elif message.text.lower() == '💬 важно знать':
        callback.needToKnow(message)
    elif message.text.lower() == '📞 контакты':
        callback.contacts(message)
    elif message.text.lower() == '👸🏼 подобрать образ':
        binary.main(message)
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