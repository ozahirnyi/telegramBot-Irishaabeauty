from binarytree import Node
from back.config import bot
import enum


# Enum of colors init
class Colors(enum.Enum):
    Pink = 1
    Yellow = 2
    LBlue = 3
    Blue = 4
    Red = 5


# Binary tree init
def binary_init():
    tree = Node(1)
    tree.left = Node(2)
    tree.right = Node(3)
    tree.left.left = Node(3)
    tree.left.left.left = Node(4)
    tree.left.right = Node(3)
    tree.right.left = Node(2)
    tree.right.right = Node(2)
    tree.right.right.right = Node(3)
    tree.right.left.left = Node(5)
    tree.left.right.right = Node(5)
    return tree


def main(call):
    tree = binary_init()

    bot.send_message(call.message.chat.id, "Privet Ya Tebe pomogu)")

    print(tree.value)
    print(tree)
