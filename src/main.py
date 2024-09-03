# main.py

from textnode import TextNode


def main():
    node1 = TextNode("some text", "txt", "gmail.com")

    node1.__repr__()

    print(node1)
