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
