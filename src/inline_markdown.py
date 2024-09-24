# inline_markdown

import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link,
)


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != text_type_text:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], text_type_text))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    images = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return images


def extract_markdown_links(text):
    links = re.findall(r"(?<!!)\[(.*?)\]\((.*?)\)", text)
    return links


def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        while original_text:
            images = extract_markdown_images(original_text)
            if not images:
                new_nodes.append(TextNode(original_text, text_type_text))
                break

            image_text, image_url = images[0]
            sections = original_text.split(f"![{image_text}]({image_url})", 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], text_type_text))

            new_nodes.append(TextNode(image_text, text_type_image, image_url))

            original_text = sections[1] if len(sections) > 1 else ""

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        original_text = old_node.text
        while original_text:
            links = extract_markdown_links(original_text)
            if not links:
                new_nodes.append(TextNode(original_text, text_type_text))
                break

            link_text, link_url = links[0]
            sections = original_text.split(f"[{link_text}]({link_url})", 1)

            if sections[0]:
                new_nodes.append(TextNode(sections[0], text_type_text))

            new_nodes.append(TextNode(link_text, text_type_link, link_url))

            original_text = sections[1] if len(sections) > 1 else ""

    return new_nodes


node1 = TextNode(
    "This is text with a ![image](https://image.com/pic.gif) and ![kitty](https://cat.gov/zazzy.gif)",
    text_type_text,
)


node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    text_type_text,
)

print(split_nodes_image([node1]))

print(split_nodes_link([node]))


# new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", text_type_text),
#     TextNode("to boot dev", text_type_link, "https://www.boot.dev"),
#     TextNode(" and ", text_type_text),
#     TextNode(
#         "to youtube", text_type_link, "https://www.youtube.com/@bootdotdev"
#     ),
# ]

# node = TextNode("This is a text with a `code block` word", text_type_text)
# new_nodes = split_nodes_delimiter([node], "`", text_type_code)

# text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
# print(extract_markdown_images(text))


# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]


# text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
# print(extract_markdown_links(text))

# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

# print(new_nodes)
