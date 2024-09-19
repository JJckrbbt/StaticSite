# test_text_to_html

import unittest

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_link,
    text_type_image,
)


from htmlnode import LeafNode

from text_to_html import text_node_to_html_node


class TestTextToHTML(unittest.TestCase):
    def test_normal_text_to_html_node(self):
        node1 = TextNode(
            "Testing Normal Text",
            text_type_text,
            None,
        )
        node2 = LeafNode(None, "Testing Normal Text", None)
        #        result = text_node_to_html_node(node1)
        #        print(f"Type of result: {type(result)}")
        #        print(f"Attributes of result: {vars(result)}")
        #        print(f"Type of node2: {type(node2)}")
        #        print(f"Attributes of node2: {vars(node2)}")

        self.assertEqual(text_node_to_html_node(node1), node2)

    def test_bold_text_html_node(self):
        node1 = TextNode(
            "Testing Bold Text",
            text_type_bold,
            None,
        )
        node2 = LeafNode("b", "Testing Bold Text", None)
        self.assertEqual(text_node_to_html_node(node1), node2)

    def test_italic_text_html_node(self):
        node1 = TextNode(
            "Testing Italic Text",
            text_type_italic,
            None,
        )
        node2 = LeafNode("i", "Testing Italic Text", None)
        self.assertEqual(text_node_to_html_node(node1), node2)

    def test_code_text_html_node(self):
        node1 = TextNode(
            "Testing Code Text",
            text_type_code,
            None,
        )
        node2 = LeafNode("code", "Testing Code Text", None)
        self.assertEqual(text_node_to_html_node(node1), node2)

    def test_link_text_html_node(self):
        node1 = TextNode(
            "Testing Link Text",
            text_type_link,
            "gsa.gov",
        )
        node2 = LeafNode("a", "Testing Link Text", {"href": "gsa.gov"})
        self.assertEqual(text_node_to_html_node(node1), node2)

    def test_image_text_html_node(self):
        node1 = TextNode(
            "Testing Image Text",
            text_type_image,
            "gsa.gov",
        )
        node2 = LeafNode(
            "img",
            None,
            {"src": "gsa.gov", "alt": "Testing Image Text"},
        )
        self.assertEqual(text_node_to_html_node(node1), node2)


if __name__ == "__main__":
    unittest.main()
