from binarytree import Node
from back.config import bot


# Binary tree filling
def binary_init():
    b_tree = Node(1)
    b_tree.left = Node(2)
    b_tree.right = Node(3)
    b_tree.left.left = Node(3)
    b_tree.left.left.left = Node(4)
    b_tree.left.right = Node(3)
    b_tree.right.left = Node(2)
    b_tree.right.right = Node(2)
    b_tree.right.right.right = Node(3)
    b_tree.right.left.left = Node(5)
    b_tree.left.right.right = Node(5)
    return tree


# Enum getattr
class Colors_enum(tuple):
    __getattr__ = tuple.index


# Colors_enum init
Colors = Colors_enum(['pink', 'yellow', 'lightblue', 'blue', 'red'])

# Binary tree init
tree = binary_init()


@bot.callback_query_handler(func=lambda call: True)
def tree_helper_init(call):
    moved_tree = Node(0)

    if call.message:
        if call.data == "First":
            moved_tree = tree.left
        elif call.data == "Second":
            moved_tree = tree.right
            bot.send_message(call.message.chat.id, "Do you like it?")
            img = open("resources/" + Colors[tree.value] + ".png", 'rb')
            bot.send_photo(call.message.chat.id, img)


def main(call):
    bot.send_message(call.message.chat.id, "Privet Ya Tebe pomogu)")

