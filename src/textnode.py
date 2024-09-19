# textnode.py


text_type_text = "text"
text_type_bold = "bold"
text_type_italic = "italic"
text_type_code = "code"
text_type_link = "link"
text_type_image = "image"


class TextNode:
    def __init__(self, text, text_type, url="None"):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(Node1, Node2):
        return (
            Node1.text == Node2.text
            and Node1.text_type == Node2.text_type
            and Node1.url == Node2.url
        )

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"


# node1 = TextNode("Node1", None, "google.com")

# print(node1)
# print(node1)
