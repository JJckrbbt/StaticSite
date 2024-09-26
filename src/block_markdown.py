# block_markdown


def markdown_to_blocks(markdown):
    trimmed_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            trimmed_blocks.append(block.strip())
    print(trimmed_blocks)


sample_markdown = """   # This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.






     * This is the first list item in a list block
* This is a list item
* This is another list item     """

markdown_to_blocks(sample_markdown)
