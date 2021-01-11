from back.config import bot, contact_keyboard


def needToKnow(message):
    img = open("resources/need_to_know.png", 'rb')
    bot.send_photo(message.chat.id, img)


def myWorks(message):
    caption = "<a href='https://instagram.com/irishaa_beauty?igshid=1hxkt1nbk45w3'>irishaa_beauty</a>"

    bot.send_message(message.chat.id, "С моими работами Вы можете ознакомиться в Инстаграм: "
                     + caption, parse_mode='HTML')


def contacts(message):
    bot.send_message(message.chat.id, "Звоните/пишите – с удовольствием отвечу на все "
                                      "интересующие Вас вопросы)", reply_markup=contact_keyboard)


def offers(message):
    img = open("resources/offers.png", 'rb')
    bot.send_photo(message.chat.id, img)
