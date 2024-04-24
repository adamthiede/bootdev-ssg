from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil

from textnode import split_nodes_delimiter, text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image, text_to_textnodes

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
    text3 = "starting text [zzzzzz](ftp://1.1.3.51/asdf.doc) and [qqq](gopher://hole) ending text"
    t3=TextNode(text3,"text")
    ll=split_nodes_link([t3])
    for link in ll:
        print(link)
    print("---")

    text2 = "starting text ![zzzzzz](ftp://1.1.3.51/asdf.doc) and ![qqq](gopher://hole) ending text"
    t2=TextNode(text2,"text")
    l2=split_nodes_image([t2])
    for link in l2:
        print(link)
    text = "This is **boldy guy** with an *slanty guy* word and a `monospaced guy` and an ![pee en gee](https://i.imgur.com/zjjcJKZ.png) and a [hyper textlink](https://boot.dev)"
    nodes=text_to_textnodes(text)
    for node in nodes:
        print("---")
        print(node)

def dir_copy(from_dir,to_dir):
    project_dir="/".join(__file__.split('/')[0:-2])
    my_file=__file__

    full_src=f"{project_dir}/{from_dir}"
    full_dst=f"{project_dir}/{to_dir}"
    print(full_src)
    print(full_dst)

    src_list=os.listdir(full_src)
    for src_item in src_list:
        item_path=f"{full_src}/{src_item}"
        if os.path.isfile(item_path):
            shutil.copy(item_path, f"{full_dst}/{src_item}")
            print(f"copied file {item_path}")
        elif os.path.isdir(item_path):
            if not os.path.isdir(f"{full_dst}/{src_item}"):
                os.mkdir(f"{full_dst}/{src_item}")
                print(f"mk'd dir {item_path}")
            # recurse here
            print(f"recursing on {from_dir}/{src_item} and {to_dir}/{src_item}")
            dir_copy(f"{from_dir}/{src_item}", f"{to_dir}/{src_item}")

def main():
    dir_copy("static", "public")

if __name__ == "__main__":
    main()
