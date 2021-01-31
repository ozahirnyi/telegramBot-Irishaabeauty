from back.config import bot, main_keyboard
import back.binary as binary
import back.callback as callback
from back.config import smiles


# Start
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет!\nЭто телеграм-бот @irishaa_antonova, чем могу помочь?'
                     + smiles[6], reply_markup=main_keyboard)


# Main button pressed
@bot.message_handler(content_types=['text'])
def parse_input_message(message):
    if message.text.lower() == smiles[5] + ' мои работы':
        callback.myWorks(message)
    elif message.text.lower() == '📝 как записаться':
        callback.offers(message)
    elif message.text.lower() == '💬 важно знать':
        callback.needToKnow(message)
    elif message.text.lower() == '📞 контакты':
        callback.contacts(message)
    elif message.text.lower() == smiles[1] + ' прайс':
        callback.price(message)
    elif message.text.lower() == smiles[4] + ' подобрать образ':
        binary.main(message)
    else:
        bot.send_message(message.chat.id, "Oops something wrong!", reply_markup=main_keyboard)


# Inline button pressed
@bot.callback_query_handler(func=lambda call: True)
def help_handler(call):
    if call.message:
        if call.data == "First" or call.data == "Second":
            binary.tree_helper_init(call)
        elif call.data == "Start Choose":
            binary.tree_helper_init_start(call)
        elif call.data == "phone":
            callback.phone(call)
        else:
            bot.send_message(call.message.chat.id, "Oops, something wrong!", main_keyboard)


bot.polling()
