# test_main

import unittest

from main import extract_title


class TestMain(unittest.TestCase):
    def test_extract_title(self):
        sample_markdown = """

        # This is a heading

        This is a paragraph of text. It has some **bold** and *italic* words inside it.

* This is the first list item in a list block
* This is another list item
* This is the last *list* item"""
        sample_title = extract_title(sample_markdown)

        self.assertEqual(
            sample_title,
            "This is a heading",
        )


if __name__ == "__main__":
    unittest.main()
