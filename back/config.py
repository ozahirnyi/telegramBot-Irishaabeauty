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

# Choose helper keyboard
ch_key_b1 = tb.types.InlineKeyboardButton(text="Да", callback_data="Da")
ch_key_b2 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Net")
ch_keyboard = tb.types.InlineKeyboardMarkup()
ch_keyboard.add(ch_key_b1, ch_key_b2)