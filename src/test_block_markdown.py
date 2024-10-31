# test block markdown

import unittest

from block_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    markdown_to_html_node,
)
from htmlnode import LeafNode, ParentNode


class TestBlockMarkdown(unittest.TestCase):
    def test_blocks(self):
        sample_markdown = """

        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside it.

* This is the first list item in a list block
* This is another list item
* This is the last *list* item"""
        new_blocks = markdown_to_blocks(sample_markdown)
        self.assertListEqual(
            [
                "# This is a heading",
                "This is a paragraph of text. It has some **bold** and *italic* words inside it.",
                "* This is the first list item in a list block\n* This is another list item\n* This is the last *list* item",
            ],
            new_blocks,
        )

    def test_block_types(self):
        sample_markdown = """

        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside it.

* This is the first list item in a list block
* This is another list item
* This is the last *list* item"""
        block_types = map(block_to_block_type, markdown_to_blocks(sample_markdown))
        self.assertListEqual(
            [
                "heading",
                "paragraph",
                "unordered_list",
            ],
            list(block_types),
        )

    def test_markdown_to_html_node(self):
        sample_markdown = """   # This is a heading!

This is a paragraph of text. It has some **bold** and *italic* words inside of it.


>Quotes are here
>and here

```plus = we have some code
and some more code```

* This is the **first list item** in a list block
* This is a *list item*
* This is another list item

1 This is an ordered list
2 This is second item of ordered list

This is another paragraph.

##### This is a closing heading, I think?

"""
        html_nodes = markdown_to_html_node(sample_markdown)
        self.assertEqual(
            ParentNode(
                "div",
                [
                    ParentNode(
                        "h1", [LeafNode(None, "This is a heading!", None)], None
                    ),
                    ParentNode(
                        "p",
                        [
                            LeafNode(
                                None, "This is a paragraph of text. It has some ", None
                            ),
                            LeafNode("b", "bold", None),
                            LeafNode(None, " and ", None),
                            LeafNode("i", "italic", None),
                            LeafNode(None, " words inside of it.", None),
                        ],
                        None,
                    ),
                    ParentNode(
                        "blockquote",
                        [LeafNode(None, "Quotes are here\nand here", None)],
                        None,
                    ),
                    ParentNode(
                        "pre",
                        [
                            LeafNode(
                                "code",
                                "plus = we have some code\nand some more code",
                                None,
                            )
                        ],
                        None,
                    ),
                    ParentNode(
                        "ul",
                        [
                            ParentNode(
                                "li",
                                [
                                    LeafNode(None, "This is the ", None),
                                    LeafNode("b", "first list item", None),
                                    LeafNode(None, " in a list block", None),
                                ],
                                None,
                            ),
                            ParentNode(
                                "li",
                                [
                                    LeafNode(None, "This is a ", None),
                                    LeafNode("i", "list item", None),
                                ],
                                None,
                            ),
                            ParentNode(
                                "li",
                                [LeafNode(None, "This is another list item", None)],
                                None,
                            ),
                        ],
                        None,
                    ),
                    ParentNode(
                        "ol",
                        [
                            ParentNode(
                                "li",
                                [LeafNode(None, "This is an ordered list", None)],
                                None,
                            ),
                            ParentNode(
                                "li",
                                [
                                    LeafNode(
                                        None,
                                        "This is second item of ordered list",
                                        None,
                                    )
                                ],
                                None,
                            ),
                        ],
                        None,
                    ),
                    ParentNode(
                        "p", [LeafNode(None, "This is another paragraph.", None)], None
                    ),
                    ParentNode(
                        "h5",
                        [LeafNode(None, "This is a closing heading, I think?", None)],
                        None,
                    ),
                ],
                None,
            ),
            html_nodes,
        )


if __name__ == "__main__":
    unittest.main()
