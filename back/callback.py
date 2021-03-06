from back.config import bot, contact_keyboard, smiles
insta_link = "<a href='https://instagram.com/irishaa_beauty?igshid=1hxkt1nbk45w3'>irishaa_beauty</a>"


def needToKnow(message):
    img = open("resources/need_to_know.png", 'rb')
    bot.send_photo(message.chat.id, img)


def myWorks(message):
    bot.send_message(message.chat.id, "С моими работами Вы можете ознакомиться в Инстаграм: "
                     + insta_link + ' ' + smiles[2], parse_mode='HTML')


def price(message):
    img = open("resources/price.png", 'rb')
    bot.send_photo(message.chat.id, img)


def contacts(message):
    bot.send_message(message.chat.id, "Звоните/пишите – с удовольствием отвечу на все "
                                      "интересующие Вас вопросы)", reply_markup=contact_keyboard)


def offers(message):
    img = open("resources/offers.png", 'rb')
    bot.send_photo(message.chat.id, img)


def phone(call):
    bot.send_message(call.message.chat.id, "Ирина: +380952180492")
