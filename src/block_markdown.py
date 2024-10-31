# block_markdown
import re
from htmlnode import ParentNode, LeafNode
from text_to_html import text_node_to_html
from inline_markdown import text_to_textnodes


def markdown_to_blocks(markdown):
    trimmed_blocks = []
    blocks = markdown.split("\n\n")
    for block in blocks:
        if block != "":
            trimmed_blocks.append(block.strip())
    return trimmed_blocks


def block_to_block_type(string):
    if string.startswith("#"):
        return "heading"
    elif string.startswith("```"):
        return "code"
    elif string.startswith(">"):
        return "quote"
    elif string.startswith("* "):
        return "unordered_list"
    elif string.startswith("- "):
        return "unordered_list"
    elif string.startswith("+ "):
        return "unordered_list"
    elif string[:1].isdigit():
        return "ordered_list"
    elif string.startswith("!["):
        return "image"
    else:
        return "paragraph"


def markdown_to_html_node(markdown):
    child_nodes = []
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        html_nodes = []
        block_type = block_to_block_type(block)
        tag = block_tag(block_type, block)
        if block_type == "heading":
            block = block.lstrip("# ")
        if block_type == "quote":
            block = strip_carrots(block)
        if block_type == "code":
            block = block.lstrip("```")
            block = block.rstrip("```")
        if (
            block_type == "heading"
            or block_type == "paragraph"
            or block_type == "quote"
        ):
            block = block.lstrip()
            html_nodes.extend(text_to_children(block))
            parent_node = create_parent(tag, html_nodes)
            child_nodes.append(parent_node)
        elif block_type == "code":
            code_leaf = LeafNode("code", block)
            parent_node = create_parent("pre", [code_leaf])
            child_nodes.append(parent_node)
        elif block_type == "unordered_list" or block_type == "ordered_list":
            tag = ""
            list_items = create_list(block, "li")
            if block_type == "unordered_list":
                tag = "ul"
            if block_type == "ordered_list":
                tag = "ol"
            parent_node = create_parent(tag, list_items)
            child_nodes.append(parent_node)
        elif block_type == "image":
            html_nodes.extend(text_to_children(block))
            parent_node = create_parent(tag, html_nodes)
            child_nodes.append(parent_node)

        else:
            raise ValueError("Invalid Markdown: Can not parse")

    block_parent = ParentNode("div", child_nodes)

    return block_parent


def create_parent(tag, children, props=None):
    return ParentNode(tag, children, props)


def create_list(block, tag):
    parent_nodes = []
    lines = block.split("\n")
    for line in lines:
        line = re.sub(r"^\s*[-*+\d.]+\s*", "", line)

        list_nodes = text_to_children(line)
        parent_nodes.append(create_parent(tag, list_nodes))
    return parent_nodes


def strip_carrots(text):
    lines = text.split("\n")
    new_lines = []
    for line in lines:
        line = line.lstrip(">")
        new_lines.append(line)
    new_text = "\n".join(new_lines)
    return new_text


def text_to_children(text):
    nodes = text_to_textnodes(text)
    html_nodes = []
    for node in nodes:
        html_nodes.append(text_node_to_html(node))
    return html_nodes


def block_tag(block_type, block):
    if block_type == "paragraph":
        return "p"
    elif block_type == "quote":
        return "blockquote"
    elif block_type == "code":
        return "code"
    elif block_type == "heading":
        return heading_block_tag(block)
    elif block_type == "image":
        return "div"
    elif block_type == "unordered_list":
        return "ul"
    elif block_type == "ordered_list":
        return "ol"


#    for node in nodes:
#        text_node_to_html(node)


def heading_block_tag(block):
    if block.startswith("######"):
        return "h6"
    elif block.startswith("#####"):
        return "h5"
    elif block.startswith("####"):
        return "h4"
    elif block.startswith("###"):
        return "h3"
    elif block.startswith("##"):
        return "h2"
    elif block.startswith("#"):
        return "h1"


# def block_to_htmlnode(block, block_type):


sample_markdown = """   # This is a heading!

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

>Quotes are here
>and here

```plus = we have some code
and some more code```

This is text with a ![image](https://image.com/pic.gif) and ![kitty](https://cat.gov/zazzy.gif)

This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)

![image](https://image.com/pic.gif) and ![kitty](https://cat.gov/zazzy.gif)


* This is the **first list item** in a list block
* This is a *list item*
* This is another list item

1 This is an ordered list
2 This is second item of ordered list

This is another paragraph.

##### This is a closing heading, I think?

"""


# print(markdown_to_blocks(sample_markdown))
# print(type(markdown_to_blocks(sample_markdown)) is list)

# block_types = map(block_to_block_type, markdown_to_blocks(sample_markdown))
# print(list(block_types))

print(markdown_to_html_node(sample_markdown))
