# test_textnode.py

import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode("Text", text_type_text)
        node2 = TextNode("Text", text_type_text)
        self.assertEqual(node1, node2, f"node1: {node1}, node2: {node2}")

    def test_ep_false(self):
        node1 = TextNode("Text", text_type_text)
        node2 = TextNode("Text", text_type_bold)
        self.assertNotEqual(node1, node2, f"node1: {node1}, node2: {node2}")

    def test_ep_false2(self):
        node1 = TextNode("Text", text_type_text)
        node2 = TextNode("Text node", text_type_text)
        self.assertNotEqual(node1, node2, f"node1: {node1}, node2: {node2}")

    def test_eq_url(self):
        node1 = TextNode("This is a TextNode", text_type_italic, "https://www.boot.dev")
        node2 = TextNode("This is a TextNode", text_type_italic, "https://www.boot.dev")
        self.assertEqual(node1, node2)

    def test_repr(self):
        node1 = TextNode("Text", text_type_text, "google.com")
        self.assertEqual("TextNode(Text, text, google.com)", node1.__repr__())


if __name__ == "__main__":
    unittest.main()
