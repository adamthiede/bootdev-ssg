import re
from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

from textnode import split_nodes_delimiter, text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image, text_to_textnodes

def markdown_to_blocks(markdown):
    new_lines=[]
    for line in markdown.split('\n\n'):
        to_add=line.strip()
        if to_add!=(''):
            new_lines.append(to_add)
    return new_lines

def block_to_block_type(block):
    bsplit=block.split()
    lsplit=block.split('\n')
    # Heading
    if re.search("^[#]{1,6} ",block):
        return "heading"
    elif bsplit[0]=='```' and bsplit[len(bsplit)-1]=='```':
        return "code"
    elif all(n.startswith("> ") for n in lsplit):
        return "quote"
    elif all(n.startswith("- ") for n in lsplit) or all(n.startswith("* ") for n in lsplit):
        return "unordered_list"
    elif all(lsplit[x].startswith(f"{x+1}. ") for x in range(0,len(lsplit))):
        return "ordered_list"
    else:
        return "paragraph"

def markdown_to_html_node(markdown):
    top_children=[]
    blocks=markdown.split('\n\n')
    for block in blocks:
        bt=block_to_block_type(block)
        if bt=="heading":
            headnum=len(block.split(" ")[0])
            top_children.append(LeafNode(f"h{headnum}",block,None))
        elif bt=="code":
            code_lines=block.split('\n')
            code_text="\n".join(code_lines[1:len(code_lines)-1])
            codeblock=LeafNode("code",code_text,None)
            top_children.append(ParentNode("pre",[codeblock]))
        elif bt=="quote":
            top_children.append(LeafNode("blockquote",block.replace("\n> ","\n"),None))
        elif bt=="paragraph":
            top_children.append(LeafNode("p",block,None))
        elif bt=="unordered_list":
            ul=[]
            for l in block.split("\n"):
                ul.append(LeafNode("li",l[2:],None))
            top_children.append(ParentNode("ul",ul))
        elif bt=="ordered_list":
            ol=[]
            for l in block.split("\n"):
                ol.append(LeafNode("li",l[3:],None))
            top_children.append(ParentNode("ol",ol))

    toplevel=HTMLNode("div", None, top_children)
    return toplevel

