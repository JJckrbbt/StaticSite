# test_HTMLNode.py

import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode(
            "p",
            "What a strange world",
            {"class": "primary"},
            None,
        )
        self.assertEqual(
            node1.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_props(self):
        node1 = HTMLNode(
            "div",
            "Hello, World",
            {
                "class": "greeting",
                "href": "https://boot.dev",
            },
            None,
        )
        self.assertEqual(
            node1.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_NotImplemented(self):
        node1 = HTMLNode(
            "a",
            "test",
            "None",
            "None",
        )
        self.assertRaises(NotImplementedError, node1.to_html)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode(
            "What a strange world",
            "p",
        )
        self.assertEqual("<p>What a strange world</p>", node1.to_html())

        print(node1.to_html())

    def test_to_html2(self):
        node2 = LeafNode(
            "This one has props",
            "p",
            {"class": "greeting"},
        )
        self.assertEqual('<p class="greeting">This one has props</p>', node2.to_html())
