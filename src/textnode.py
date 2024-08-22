# textnode.py
class TextNode:
    def __init__(self, text, text_type, url ="None"):
        self.text = text
        self.text_type =  text_type
        self.url = url

    def __eq__(Node1, Node2):
        if Node1.text == Node2.text and Node1.text_type == Node2.text_type and Node1.url == Node2.url:
            return True
        else:
            return False


    def __repr__(self):
        return f'TextNode({self.text}, {self.text_type}, {self.url})'

