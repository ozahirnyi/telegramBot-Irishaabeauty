import random as rand
from binarytree import Node
from db import Db
from back.config import bot, ch_keyboard


# Binary tree filling
def binary_init():
    b_tree = Node(0)
    b_tree.left = Node(51)
    b_tree.right = Node(52)
    b_tree.left.left = Node(611)
    b_tree.left.right = Node(712)
    b_tree.right.left = Node(712)
    b_tree.right.right = Node(422)
    b_tree.left.left.left = Node(8111)
    b_tree.left.left.right = Node(9211)
    b_tree.right.right.left = Node(-8122)
    b_tree.right.right.right = Node(-9222)
    return b_tree


# Enum getattr
class colors_enum(tuple):
    __getattr__ = tuple.index


# Make_types_enum init
make_types = colors_enum(['typeOfEvent', 'weddingQuestion', 'dayEvent', 'weddingTrue',
                          'eveningEvent', 'day', 'cocktail', 'evening', 'creative'])


def get_position(current_position, tree):
    sign = 1 if current_position > 0 else -1
    value_n_position = []

    while current_position < 0 or current_position > 9:
        if current_position % (10 * sign) == 1:
            tree = tree.left
            current_position /= 10
        elif current_position % (10 * sign) == 2:
            tree = tree.right
            current_position /= 10
    print("Current position: %s" % current_position)
    print("Tree: %s" % tree)
    value_n_position.append(current_position)
    value_n_position.append(tree)
    return value_n_position


@bot.callback_query_handler(func=lambda call: True)
def tree_helper_init(call):
    if call.message:
        tree = binary_init()

        print(tree)
        data_base = Db()
        data_base.create_table()
        data_base.print_db()
        position_value = data_base.get_data(call.message.chat.id)

        if 3 <= position_value <= 9:
            bot.send_message(call.message.chat.id, "Your answer is: %s" % position_value)
        else:
            value_n_position = get_position(position_value, tree)
            print("Value_n_position: %s" % value_n_position)
            if call.data == "First":
                print("First")
                bot.send_message(call.message.chat.id, "Your value is: %s" % value_n_position[0])
                data_base.insert_data(call.message.chat.id, int(value_n_position[1].left.value))
                data_base.print_db()
            elif call.data == "Second":
                print("Second")
                bot.send_message(call.message.chat.id, "Your value is: %s" % value_n_position[0])
                data_base.insert_data(call.message.chat.id, value_n_position[1].right.value)
                data_base.print_db()


def main(call):
    # data_base = Db()
    # data_base.create_table()
    # data_base.print_db()
    # print(call)
    bot.send_message(call.chat.id, "Privet Ya Tebe pomogu)")
    img = open("../resources/pink.png", 'rb')
    bot.send_message(call.chat.id, "Do you like it?")
    bot.send_photo(call.chat.id, img, reply_markup=ch_keyboard)
