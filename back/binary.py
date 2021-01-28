from binarytree import Node
from db import Db
from back.config import bot, ch_keyboard, ch_start_keyboard


# Binary tree filling
def binary_init():
    b_tree = Node(0)
    b_tree.left = Node(1)
    b_tree.right = Node(2)
    b_tree.left.left = Node(3)
    b_tree.left.left.left = Node(5)
    b_tree.left.left.right = Node(6)
    b_tree.left.right = Node(4)
    b_tree.left.right.left = Node(7)
    b_tree.left.right.right = Node(8)
    return b_tree


# Enum getattr
class colors_enum(tuple):
    __getattr__ = tuple.index


# Make_types_enum init
make_types = colors_enum(['weddingQuestion', 'eventTime', 'weddingTrue',
                          'dayEvent', 'nightEvent', 'day', 'cocktail', 'evening', 'creative'])


def get_response(result):
    value = make_types[result]

    if value == 'typeOfEvent':
        return ''
    elif value == 'weddingQuestion':
        return 'Возможно Вы невеста?'
    elif value == 'dayEvent':
        return ''
    elif value == 'weddingTrue':
        return ''
    elif value == 'eveningEvent':
        return ''
    elif value == 'day':
        return ''
    elif value == 'cocktail':
        return ''
    elif value == 'evening':
        return ''
    elif value == 'creative':
        return ''
    else:
        return "Oops, something wrong..("


# Get value by moving in binary tree to left(if we get '1') and right(if we get '2')
def get_value(current_position, tree):
    if tree is None:
        return -1

    while current_position:
        if current_position == 1 or current_position % 10 == 1:
            tree = tree.left
            current_position //= 10
        elif current_position == 2 or current_position % 10 == 2:
            tree = tree.right
            current_position //= 10
    print("Tree: %s" % tree)
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
    buf.sort(reverse=True)
    for i in buf:
        res = res * 10 + i
    return res


# Init binary_tree for find current value by requesting data from DB(path - for move in tree)
# First - move left in bin_tree | Second - move right in bin_tree | by adding 1 or 2 in path
# 5, 6, 7, 8, 2 - its a final positions in bit_tree
# if someone send wrong data from DB we will get -1, print error and give that id '0' value
def tree_helper_init(call):
    if call.message:
        tree = binary_init()
        data_base = Db()
        data_base.create_table()
        data_base.print_db()
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
        elif 5 <= value <= 8 or value == 2:
            bot.send_message(call.message.chat.id, "Your answer is: %s" % value)
            data_base.insert_data(call.message.chat.id, 0)
        else:
            bot.send_message(call.message.chat.id, "Your value is: %s" % value, reply_markup=ch_keyboard)


def tree_helper_init_start(call):
    data_base = Db()
    data_base.create_table()
    data_base.insert_data(call.message.chat.id, 0)
    tree_helper_init(call)


def main(call):
    bot.send_message(call.chat.id, "Привет, давай подберем макияж твоей мечты вместе!", reply_markup=ch_start_keyboard)
