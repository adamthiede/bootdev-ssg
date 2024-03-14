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
    tn=TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(tn)
    print(text_node_to_html_node(tn).to_html())

def main():
    node = TextNode("This is text with a `code block` word", "text")
    node2 = TextNode("`Code block` begins the thing", "text")
    node3 = TextNode("`Code block`  but wrong `  begins the thing", "text")
    new_nodes = split_nodes_delimiter([node,node2,node3], "`", "code")
    for node in new_nodes:
        print(node)
    print(isinstance(node,TextNode))


if __name__ == "__main__":
    main()
