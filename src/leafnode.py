# LeafNode.py

from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, value, tag="None", props="None"):
        super().__init__(value, tag, props)
