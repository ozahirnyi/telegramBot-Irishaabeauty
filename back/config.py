import telebot as tb
from back.bot_token import irishaToken

# Bot init
bot = tb.TeleBot(irishaToken)

# Smiles
information_desk_person = "\N{INFORMATION DESK PERSON}"
money_with_wings = "\N{MONEY WITH WINGS}"
winking_face = "\N{WINKING FACE}"
telephone_receiver = "\N{TELEPHONE RECEIVER}"
princess = "\N{PRINCESS}"
artist_palette = "\N{ARTIST PALETTE}"
smiling_face_with_smiling_eyes = "\N{SMILING FACE WITH SMILING EYES}"
sparkles = "\N{SPARKLES}"
incoming_envelope = "\N{INCOMING ENVELOPE}"
mobile_phone_with_rightwards_arrow_at_left = "\N{MOBILE PHONE WITH RIGHTWARDS ARROW AT LEFT}"
smiles = [information_desk_person, money_with_wings, winking_face, telephone_receiver,
          princess, artist_palette, smiling_face_with_smiling_eyes]

# Main keyboard
main_keyboard = tb.types.ReplyKeyboardMarkup(True)
main_keyboard.add(artist_palette + " Мои работы")
main_keyboard.row("📝 Как записаться", princess + " Подобрать образ")
main_keyboard.row("💬 Важно знать", "📞 Контакты")
main_keyboard.add(money_with_wings + " Прайс")

# Contact keyboard
contact_keyboard = tb.types.InlineKeyboardMarkup()
contact_instagram_button = tb.types.InlineKeyboardButton(text=mobile_phone_with_rightwards_arrow_at_left + ' Instagram',
                                                         url='https://instagram.com/irishaa_beauty?'
                                                             'igshid=1hxkt1nbk45w3')
contact_telegram_button = tb.types.InlineKeyboardButton(text=incoming_envelope + ' Telegram', url='t.me/irishaa_antonova')
contact_number_button = tb.types.InlineKeyboardButton(text=telephone_receiver + ' Phone', callback_data="phone")
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
ch_key_b20 = tb.types.InlineKeyboardButton(text="Днём", callback_data="First")
ch_key_b21 = tb.types.InlineKeyboardButton(text="Вечером", callback_data="Second")
ch_key_b30 = tb.types.InlineKeyboardButton(text="Спокойный", callback_data="First")
ch_key_b31 = tb.types.InlineKeyboardButton(text="Коктейльный", callback_data="Second")
ch_key_b40 = tb.types.InlineKeyboardButton(text="Вечерний", callback_data="First")
ch_key_b41 = tb.types.InlineKeyboardButton(text="Креативный", callback_data="Second")
ch_keyboard0 = tb.types.InlineKeyboardMarkup()
ch_keyboard2 = tb.types.InlineKeyboardMarkup()
ch_keyboard3 = tb.types.InlineKeyboardMarkup()
ch_keyboard4 = tb.types.InlineKeyboardMarkup()
ch_keyboard0.add(ch_key_b00, ch_key_b01)
ch_keyboard2.add(ch_key_b20, ch_key_b21)
ch_keyboard3.add(ch_key_b30, ch_key_b31)
ch_keyboard4.add(ch_key_b40, ch_key_b41)
ch_keyboard = [ch_keyboard0, None, ch_keyboard2, ch_keyboard3, ch_keyboard4]
