from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

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

def test_some_nodes():
    ln=LeafNode('a', 'this is a link', {"href":'https://www.boot.dev'})
    ln2=LeafNode("p", "This is a paragraph of text.")
    print(ln)
    print(ln2)
    print(ln.to_html())
    print(ln2.to_html())
    hn=HTMLNode('p', 'This is a text node', ln, None )
    print(hn)
    leaf1=LeafNode("b","strong!")
    leaf2=LeafNode("i","italic!")
    print(leaf1)
    print(leaf2)
    parent=ParentNode("p", [leaf1, leaf2])
    parent2=ParentNode("p", None)
    print(parent.to_html())


def main():
    tn=TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(tn)
    print(text_node_to_html_node(tn).to_html())

if __name__ == "__main__":
    main()
