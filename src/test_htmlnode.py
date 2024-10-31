# test_HTMLNode.py

import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node1 = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node1.__repr__(),
            "HTMLNode(p, What a strange world, None, {'class': 'primary'})",
        )

    def test_to_html_props(self):
        node1 = HTMLNode(
            "div",
            "Hello, World",
            None,
            {
                "class": "greeting",
                "href": "https://boot.dev",
            },
        )
        self.assertEqual(
            node1.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_NotImplemented(self):
        node1 = HTMLNode(
            "a",
            "test",
            None,
            None,
        )
        self.assertRaises(NotImplementedError, node1.to_html)


class TestLeafNode(unittest.TestCase):
    def test_to_html(self):
        node1 = LeafNode(
            "p",
            "What a strange world",
        )
        self.assertEqual("<p>What a strange world</p>", node1.to_html())

    #        print(node1.to_html())

    def test_to_html2(self):
        node2 = LeafNode(
            "p",
            "This one has props",
            {"class": "greeting"},
        )
        self.assertEqual('<p class="greeting">This one has props</p>', node2.to_html())

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")

    def test_to_html_with_children(self):
        child_node = LeafNode("span", "child")
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(parent_node.to_html(), "<div><span>child</span></div>")

    def test_to_html_with_grandchildren(self):
        grandchild_node = LeafNode("b", "grandchild")
        child_node = ParentNode("span", [grandchild_node])
        parent_node = ParentNode("div", [child_node])
        self.assertEqual(
            parent_node.to_html(),
            "<div><span><b>grandchild</b></span></div>",
        )

    def test_to_html_many_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>",
        )

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )
