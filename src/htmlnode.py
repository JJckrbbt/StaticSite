# htmlnode.py


class HTMLNode:
    def __init__(self, tag=None, value=None, props=None, children=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implmented")

    def props_to_html(self):
        if self.props is None:
            return ""
        else:
            props_html = ""
            for prop in self.props:
                props_html += f' {prop}="{self.props[prop]}"'
            return props_html

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})"


node1 = HTMLNode(
    "p",
    "this is a node",
    "None",
    {
        "href": "https://www.google.com",
        "target": "_blank",
    },
)

# print(node1)

# print(node1.props_to_html())


class LeafNode(HTMLNode):
    def __init__(self, value, tag=None, props=None):
        super().__init__(tag, value, props)

    def to_html(self):
        if self.value:
            if self.tag is None:
                return f"{self.value}"
            else:
                html_props = self.props_to_html()
                print(html_props)
                return f"<{self.tag}{html_props}>{self.value}</{self.tag}>"
        else:
            raise ValueError("has no value")


node1 = LeafNode("Testing", "p", None)
print(node1.tag, node1.value, node1.props)
print(node1.to_html())

node2 = LeafNode("Testing", "p", {"class": "greeting"})
print(node2)
print(node2.to_html())
