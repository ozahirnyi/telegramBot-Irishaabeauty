import telebot as tb
from back.bot_token import irishaToken

# Bot init
bot = tb.TeleBot(irishaToken)

# Main keyboard
main_keyboard = tb.types.ReplyKeyboardMarkup(True)
main_keyboard.add(":disappointed: Мои работы")
main_keyboard.row("📝 Как записаться", "👸🏼 Подобрать образ")
main_keyboard.row("💬 Важно знать", "📞 Контакты")
main_keyboard.add("🤑 Прайс")

# Contact keyboard
contact_keyboard = tb.types.InlineKeyboardMarkup()
contact_instagram_button = tb.types.InlineKeyboardButton(text='Instagram',
                                                         url='https://instagram.com/irishaa_beauty?'
                                                             'igshid=1hxkt1nbk45w3')
contact_telegram_button = tb.types.InlineKeyboardButton(text='Telegram', url='t.me/irishaa_antonova')
contact_number_button = tb.types.InlineKeyboardButton(text='Phone', callback_data="phone")
contact_keyboard.add(contact_number_button)
contact_keyboard.add(contact_telegram_button)
contact_keyboard.add(contact_instagram_button)

# Start keyboard
s_key_b1 = tb.types.InlineKeyboardButton(text="Заказать", callback_data="Zakazat")
s_key_b2 = tb.types.InlineKeyboardButton(text="Подобрать", callback_data="Vibrat")
start_keyboard = tb.types.InlineKeyboardMarkup()
start_keyboard.add(s_key_b2, s_key_b1)

# Choose start keyboard
ch_key_start = tb.types.InlineKeyboardButton(text='Старт', callback_data="Start Choose")
ch_start_keyboard = tb.types.InlineKeyboardMarkup()
ch_start_keyboard.add(ch_key_start)

# Choose helper keyboards
ch_key_b00 = tb.types.InlineKeyboardButton(text="Да, я невеста!", callback_data="First")
ch_key_b01 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_key_b10 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_key_b11 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_key_b20 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_key_b21 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_key_b30 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_key_b31 = tb.types.InlineKeyboardButton(text="Нет", callback_data="Second")
ch_keyboard0 = tb.types.InlineKeyboardMarkup()
ch_keyboard1 = tb.types.InlineKeyboardMarkup()
ch_keyboard2 = tb.types.InlineKeyboardMarkup()
ch_keyboard3 = tb.types.InlineKeyboardMarkup()
ch_keyboard0.add(ch_key_b00, ch_key_b01)
ch_keyboard0.add(ch_key_b10, ch_key_b11)
ch_keyboard0.add(ch_key_b20, ch_key_b21)
ch_keyboard0.add(ch_key_b30, ch_key_b31)
