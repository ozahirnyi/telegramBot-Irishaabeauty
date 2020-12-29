from binarytree import Node
from back.config import bot
from back.config import ch_keyboard


# Binary tree filling
def binary_init():
    b_tree = Node(0)
    b_tree.left = Node(1)
    b_tree.right = Node(2)
    b_tree.left.left = Node(2)
    b_tree.left.left.left = Node(3)
    b_tree.left.right = Node(2)
    b_tree.right.left = Node(1)
    b_tree.right.right = Node(1)
    b_tree.right.right.right = Node(2)
    b_tree.right.left.left = Node(4)
    b_tree.left.right.right = Node(4)
    return b_tree


# Enum getattr
class Colors_enum(tuple):
    __getattr__ = tuple.index


# Colors_enum init
Colors = Colors_enum(['pink', 'yellow', 'lightblue', 'blue', 'red'])

# Binary tree init
tree = binary_init()


@bot.callback_query_handler(func=lambda call: True)
def tree_helper_init(call):
    global tree

    if call.message:
        if tree is not None:
            print(tree.value)
            print(tree)
        else:
            bot.send_message(call.message.chat.id, "This is your choice)")
        if call.data == "First":
            print("First")
            tree = tree.left
        elif call.data == "Second":
            print("Second")
            tree = tree.right
        bot.send_message(call.message.chat.id, "Do you like it?")
        img = open("resources/" + Colors[tree.value] + ".png", 'rb')
        bot.send_photo(call.message.chat.id, img, reply_markup=ch_keyboard)


def main(call):

    print(tree)
    bot.send_message(call.message.chat.id, "Privet Ya Tebe pomogu)")
    img = open("resources/pink.png", 'rb')
    bot.send_message(call.message.chat.id, "Do you like it?")
    bot.send_photo(call.message.chat.id, img, reply_markup=ch_keyboard)


