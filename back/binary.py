from binarytree import Node
from telebot.apihelper import ApiException

from db import Db
from back.config import bot, ch_keyboard, ch_start_keyboard, information_desk_person, sparkles
from callback import insta_link


# Binary tree filling
def binary_init():
    b_tree = Node(0)
    b_tree.left = Node(1)
    b_tree.right = Node(2)
    b_tree.right.left = Node(3)
    b_tree.right.left.left = Node(5)
    b_tree.right.left.right = Node(6)
    b_tree.right.right = Node(4)
    b_tree.right.right.left = Node(7)
    b_tree.right.right.right = Node(8)
    return b_tree


# Enum getattr
class colors_enum(tuple):
    __getattr__ = tuple.index


# Make_types_enum init
make_types = colors_enum(['weddingQuestion', 'weddingTrue', 'eventTime',
                          'dayEvent', 'nightEvent', 'day', 'cocktail', 'evening', 'creative'])


def get_response(result):
    value = make_types[result]

    if value == 'weddingQuestion':
        return 'Возможно Вы невеста?'
    elif value == 'eventTime':
        return 'Ваше мероприятие будет проходить вечером или днём?'
    elif value == 'dayEvent':
        return 'Отлично! Вы желаете более спокойный макияж или, быть может, коктейльный?'
    elif value == 'nightEvent':
        return 'Отлично! Возможно Вашему мероприятию подойдет креативный макияж?'
    elif value == 'weddingTrue':
        return 'Прекрасно! Тогда Вам подойте Свадебный макиякж' \
               + sparkles + \
               '\nС примерами можете ознакомится в моем инстаграмме ' \
               + information_desk_person + ": "
    elif value == 'day':
        return 'Чудесно! Вам идельно подойдет Нюдовый макияж' \
               + sparkles + \
               '\nС примерами можете ознакомится в моем инстаграмме ' \
               + information_desk_person + ": "
    elif value == 'cocktail':
        return 'Чудесно! Вам идельно подойдет Коктейльный макияж' \
               + sparkles + \
               '\nС примерами можете ознакомится в моем инстаграмме ' \
               + information_desk_person + ": "
    elif value == 'evening':
        return 'Чудесно! Вам идельно подойдет Вечерний макияж' \
               + sparkles + \
               '\nС примерами можете ознакомится в моем инстаграмме ' \
               + information_desk_person + ": "
    elif value == 'creative':
        return 'Чудесно! Вам идельно подойдет Креативный макияж' \
               + sparkles + \
               '\nС примерами можете ознакомится в моем инстаграмме ' \
               + information_desk_person + ": "
    else:
        return "Oops, something wrong..("


# Get value by moving in binary tree to left(if we get '1') and right(if we get '2')
def get_value(current_position, tree):
    while current_position:
        if tree is None:
            return -1
        if current_position == 1 or current_position % 10 == 1:
            tree = tree.left
            current_position //= 10
        elif current_position == 2 or current_position % 10 == 2:
            tree = tree.right
            current_position //= 10
    if tree is None:
        return -1
    return tree.value


# Prepare tree_path(reverse and adding value)
def path_update(direction, current_path):
    res = direction
    buf = []

    while current_path:
        buf.append(current_path % 10)
        current_path //= 10
    buf.reverse()
    for i in buf:
        res = res * 10 + i
    return res


# Init binary_tree for find current value by requesting data from DB(path - for move in tree)
# First - move left in bin_tree | Second - move right in bin_tree | by adding 1 or 2 in path
# 5, 6, 7, 8, 1 - its a final positions in bit_tree
# if someone send wrong data from DB we will get -1, print error and give that id '0' value in DB
def tree_helper_init(call):
    if call.message:
        tree = binary_init()
        data_base = Db()
        tree_path = data_base.get_data(call.message.chat.id)

        if call.data == "First":
            tree_path = path_update(1, tree_path)
            data_base.insert_data(call.message.chat.id, tree_path)
        elif call.data == "Second":
            tree_path = path_update(2, tree_path)
            data_base.insert_data(call.message.chat.id, tree_path)
        # Get value for make_types and give a response
        value = get_value(tree_path, tree)
        if value == -1:
            bot.send_message(call.message.chat.id, "Oops, something wrong..(")
            data_base.insert_data(call.message.chat.id, 0)
        elif 5 <= value <= 8 or value == 1:
            bot.send_message(call.message.chat.id, get_response(value) + insta_link, parse_mode='HTML')
            for i in range(0, 3):
                img = open("resources/makeups/" + make_types[value] + str(i) + ".png", "rb")
                bot.send_photo(call.message.chat.id, img)
            data_base.insert_data(call.message.chat.id, 0)
        else:
            bot.send_message(call.message.chat.id, get_response(value), reply_markup=ch_keyboard[value])
        if value != 0:
            try:
                bot.edit_message_reply_markup(call.message.chat.id, message_id=call.message.message_id, reply_markup=None)
            except ApiException:
                data_base.insert_data(call.message.chat.id, 0)


def tree_helper_init_start(call):
    data_base = Db(create_table=True)
    data_base.insert_data(call.message.chat.id, 0)
    tree_helper_init(call)


def main(call):
    bot.send_message(call.chat.id, "Привет, давай подберем макияж твоей мечты вместе!", reply_markup=ch_start_keyboard)
