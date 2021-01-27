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

# Main buttons | mkb = Main keyboard button
# mkb_myWorks = tb.types.InlineKeyboardButton(text=":art: мои работы", callback_data="My works")
# mkb_offers = tb.types.InlineKeyboardButton(text="📝 Как записаться", callback_data="Offers")
# mkb_binTree = tb.types.InlineKeyboardButton(text="👸🏼 Подобрать образ", callback_data="Bin tree")
# mkb_needToKnow = tb.types.InlineKeyboardButton(text="💬 Важно знать", callback_data="Need to know")
# mkb_contacts = tb.types.InlineKeyboardButton(text="📞 Контакты", callback_data="Contacts")
#
# # Main keyboard
# main_keyboard = tb.types.InlineKeyboardMarkup()
# main_keyboard.add(mkb_myWorks)
# main_keyboard.row(mkb_offers, mkb_binTree)
# main_keyboard.row(mkb_needToKnow, mkb_contacts)

# Start keyboard
s_key_b1 = tb.types.InlineKeyboardButton(text="Заказать", callback_data="Zakazat")
s_key_b2 = tb.types.InlineKeyboardButton(text="Подобрать", callback_data="Vibrat")
start_keyboard = tb.types.InlineKeyboardMarkup()
start_keyboard.add(s_key_b2, s_key_b1)

# Choose start keyboard
ch_key_start = tb.types.InlineKeyboardButton(text='Старт', callback_data="Start Choose")
ch_start_keyboard = tb.types.InlineKeyboardMarkup()
ch_start_keyboard.add(ch_key_start)

# Choose helper keyboard
ch_key_b1 = tb.types.InlineKeyboardButton(text="Первое", callback_data="First")
ch_key_b2 = tb.types.InlineKeyboardButton(text="Второе", callback_data="Second")
ch_keyboard = tb.types.InlineKeyboardMarkup()
ch_keyboard.add(ch_key_b1, ch_key_b2)


