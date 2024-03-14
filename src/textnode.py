import re

class TextNode:
    text, text_type, url = None, None, None
    def __init__(self, text, text_type, url=None):
        self.text=text
        self.text_type=text_type
        self.url=url
    def __eq__(self, textnode):
        if self.text==textnode.text and self.text_type==textnode.text_type and self.url==textnode.url:
            return True
        return False

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"

def text_node_to_html_node(text_node):
    valid_types=["text","bold","italic","code","link","image"]
    match text_node.text_type:
        case "text":
            return LeafNode(None, text_node.text)
        case "bold":
            return LeafNode("b", text_node.text)
        case "italic":
            return LeafNode("i", text_node.text)
        case "code":
            return LeafNode("code", text_node.text)
        case "link":
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case "image":
            return LeafNode("img", None, {"alt": text_node.text, "src": text_node.url})
        case _:
            raise Exception(ValueError(f"{text_node.text_type} not in valid_types: {valid_types}"))

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    nodes=[]
    for node in old_nodes:
        if isinstance(node,TextNode):
            if node.text.count(delimiter)%2!=0:
                raise Exception(SyntaxError(f"Odd number of delimiters: '{delimiter}'"))
            n_split=node.text.split(delimiter)
            format=False
            if node.text.startswith(delimiter):
                format=True
                n_split.pop(0)
            for n in n_split:
                if format:
                    nodes.append(TextNode(n,text_type))
                else:
                    nodes.append(TextNode(n,"text"))
                format=not format
        else:
            nodes.append(node)
    return nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)",text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)",text)
