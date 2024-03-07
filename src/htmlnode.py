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
            rv+=f'{prop}="{self.props[prop]}" '
        return rv.strip()

