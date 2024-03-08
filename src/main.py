from textnode import TextNode
from htmlnode import HTMLNode
from htmlnode import LeafNode

def main():
    tn=TextNode('This is a text node', 'bold', 'https://www.boot.dev')
    print(tn)
    ln=LeafNode('a', 'this is a link', {"href":'https://www.boot.dev'})
    ln2=LeafNode("p", "This is a paragraph of text.")
    print(ln)
    print(ln2)
    print(ln.to_html())
    print(ln2.to_html())
    hn=HTMLNode('p', 'This is a text node', ln, None )
    print(hn)


if __name__ == "__main__":
    main()
