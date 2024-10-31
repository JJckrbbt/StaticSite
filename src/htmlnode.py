# htmlnode.py


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
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
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, HTMLNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )


# node1 = HTMLNode(
#    "p",
#    "this is a node",
#    None,
#    {
#        "href": "https://www.google.com",
#        "target": "_blank",
#    },
# )

# print(node1)

# print(node1.props_to_html())


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        SELF_CLOSING_TAGS = ["img", "br", "hr", "input"]
        if self.tag in SELF_CLOSING_TAGS:
            return f"<{self.tag}{self.props_to_html()}/>"
        if self.value is None:
            raise ValueError("Invalid HTML: no value")
        if self.tag is None:
            return self.value
        return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"


# node1 = LeafNode("p", "Testing", None)
# print(node1.tag, node1.value, node1.props)
# print(node1.to_html())

# node2 = LeafNode("p", "Testing", {"class": "greeting"})
# print(node2)
# print(node2.to_html())


class ParentNode(HTMLNode):
    def __init__(self, children, tag=None, props=None):
        super().__init__(children, None, tag, props)

    def to_html(self):
        if self.tag is None:
            raise ValueError("Invalid HTML: no tag")
        if self.children is None:
            raise ValueError("Invalid Entry: no children")
        children_html = ""
        for child in self.children:
            children_html += child.to_html()
        return f"<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>"

    #        leaves = self._generate_leaves(self.children)
    #        return f"<{self.tag}>{leaves}</{self.tag}>"
    #
    #    def _generate_leaves(self, children):
    #        if not isinstance(children, list):
    #            return f"<{self.tag}>{self.value}</{self.tag}"
    #        leaves = ""
    #        for child in children:
    #            leaves += self._generate_leaves(child)
    #        return leaves

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def __eq__(self, other):
        if not isinstance(other, ParentNode):
            return False
        return (
            self.tag == other.tag
            and self.value == other.value
            and self.children == other.children
            and self.props == other.props
        )


# node = ParentNode(
#    "p",
#    [
#        LeafNode("b", "Bold Text"),
#        LeafNode(None, "Normal Text"),
#        LeafNode("i", "italic text"),
#        LeafNode(None, "Normal Text"),
#    ],
# )

# print(f"tag: {node.tag} | children: {node.children}")

# node.to_html()
