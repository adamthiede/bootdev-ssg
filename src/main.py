from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

from textnode import split_nodes_delimiter, text_node_to_html_node, extract_markdown_images, extract_markdown_links



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
    new_nodes = split_nodes_delimiter([node,node2], "`", "code")
    for node in new_nodes:
        print(node)
    text = "This is text with an ![image](https://i.imgur.com/zjjcJKZ.png) and ![another](https://i.imgur.com/dfsdkjfd.png)"
    print(extract_markdown_images(text))

    text2 = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
    print(extract_markdown_links(text2))


if __name__ == "__main__":
    main()
