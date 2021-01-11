import random as rand
import sqlite3
from binarytree import Node
from back.config import bot
from back.config import ch_keyboard


# Binary tree filling
def binary_init():
    b_tree = Node(0)
    b_tree.left = Node(1)
    b_tree.right = Node(2)
    b_tree.left.left = Node(2)
    b_tree.left.right = Node(2)
    b_tree.right.left = Node(1)
    b_tree.right.right = Node(1)
    b_tree.left.left.left = Node(3)
    b_tree.right.left.left = Node(4)
    b_tree.left.left.right = Node(4)
    b_tree.left.right.left = Node(3)
    b_tree.left.right.right = Node(4)
    b_tree.right.right.left = Node(4)
    b_tree.right.left.right = Node(2)
    b_tree.right.right.right = Node(2)
    return b_tree


# Enum getattr
class colors_enum(tuple):
    __getattr__ = tuple.index


# Make_types_enum init
make_types = colors_enum(['svad', 'nude', 'even', 'cock', 'creative'])

# Binary tree init
tree = binary_init()


# @bot.callback_query_handler(func=lambda call: True)
def tree_helper_init(call):
    global tree

    if call.message:
        print(tree)
        if tree.left is None or tree.right is None:
            bot.send_message(call.message.chat.id, "Vash vibor: " + make_types[tree.value])
        else:
            if call.data == "First":
                print("First")
                tree = tree.left
            elif call.data == "Second":
                print("Second")
                tree = tree.right
            bot.send_message(call.message.chat.id, "Do you like it?")
            print(make_types[tree.value])
            img = open("resources/" + make_types[tree.value] + str(rand.randint(0, 2)) + ".jpeg", 'rb')
            bot.send_photo(call.message.chat.id, img, reply_markup=ch_keyboard)
            # print(tree.value)
            # print(tree)


# def db_connect():


def main(call):
    print(tree)
    bot.send_message(call.chat.id, "Privet Ya Tebe pomogu)")
    img = open("resources/pink.png", 'rb')
    bot.send_message(call.chat.id, "Do you like it?")
    bot.send_photo(call.chat.id, img, reply_markup=ch_keyboard)
