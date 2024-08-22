# test_textnode.py

import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node1 = TextNode('Text', 'bold')
        node2 = TextNode('Text', 'bold')
        self.assertEqual(node1, node2, f"node1: {node1}, node2: {node2}")


if __name__ == "__main__":
    unittest.main()
