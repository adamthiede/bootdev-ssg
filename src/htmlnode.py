class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag=tag
        self.value=value
        self.children=children
        self.props=props

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"

    def __eq__(self, hnode):
        return (
                self.tag==hnode.tag and
                self.value==hnode.value and
                self.children==hnode.children and
                self.props==hnode.props
                )

    def to_html(self):
        raise Exception(NotImplementedError(f"{__name__} is not implemented"))

    def props_to_html(self):
        if self.props is None:
            return ""
        props_html = ""
        for prop in self.props:
            props_html += f' {prop}="{self.props[prop]}"'
        return props_html

    def props_to_html(self):
        if self.props is None:
            return ""
        rv=""
        for prop in self.props:
            rv+=f' {prop}="{self.props[prop]}"'
        return rv

class LeafNode(HTMLNode):
    def __init__(self, tag=None, value=None, props=None):
        super().__init__(tag=tag, value=value, children=None, props=props)

    def to_html(self):
        if self.value is None:
            raise Exception(ValueError("Provide a value to the leaf node"))
        if self.tag is None:
            return self.value
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, children=children, props=props)

    def __repr__(self):
        return f"ParentNode({self.tag}, {self.children}, {self.props})"

    def to_html(self):
        if self.tag is None:
            raise Exception(ValueError("No tag for ParentNode"))
        elif self.children is None:
            raise Exception(ValueError("No children for ParentNode"))
        else:
            html=f"<{self.tag}>"
            for node in self.children:
                if node.value is None:
                    raise Exception(ValueError("Child node does not have a value"))
                html+=node.to_html()
            html+=f"</{self.tag}>"
            return html

