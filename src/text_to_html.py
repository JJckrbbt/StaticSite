# text_to_html.py

from textnode import TextNode

from htmlnode import LeafNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text, None)
        case "bold":
            return LeafNode("b", text_node.text, None)
        case "italic":
            return LeafNode("i", text_node.text, None)
        case "code":
            return LeafNode("code", text_node.text, None)
        case "image":
            return LeafNode(
                "img",
                None,
                {
                    "src": text_node.url,
                    "alt": text_node.text,
                },
            )
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})

        case _:
            raise ValueError("Invalid Text Type")


def text_switch(text_type):
    match text_type:
        case "text":
            return None
        case "bold":
            return "b"
        case "italic":
            return "i"
        case "code":
            return "code"
        case "image":
            return "img"
        case "link":
            return "a"
