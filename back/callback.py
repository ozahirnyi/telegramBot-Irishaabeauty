from back.config import bot, main_keyboard


def myWorks(message):
    caption = "<a href='https://instagram.com/irishaa_beauty?igshid=1hxkt1nbk45w3'>irishaa_beauty</a>"

    bot.send_message(message.chat.id, "С моими работами Вы можете ознакомиться в Инстаграм: "
                     + caption, parse_mode='HTML')


def offers(message):
    img = open("resources/offers.png", 'rb')
    bot.send_photo(message.chat.id, img)
