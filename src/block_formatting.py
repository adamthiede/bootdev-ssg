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
