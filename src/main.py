from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode
import os
import shutil
import time

from textnode import split_nodes_delimiter, text_node_to_html_node, extract_markdown_images, extract_markdown_links, split_nodes_link, split_nodes_image, text_to_textnodes
from block_formatting import markdown_to_html_node

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

def extract_title(markdown):
    text=open(markdown)
    lines=text.readlines()
    title=""
    for line in lines:
        if line.startswith("# "):
            title=line[1:].strip()
            break
    if title=="":
        raise exception("Posts must have a title.")
    return title

def generate_page(from_path, template_path, dest_path):
    ## Print a message to the console that says something like "Generating page from from_path to dest_path using template_path".
    ## Read the markdown file at from_path and store the contents in a variable.
    ## Read the template file at template_path and store the contents in a variable.
    ## Use your markdown_to_html_node function and .to_html() method to convert the markdown file to HTML.
    ## Use the extract_title function to grab the title of the page.
    ## Replace the {{ Title }} and {{ Content }} placeholders in the template with the HTML and title you generated.
    ## Write the new HTML to a file at dest_path. Be sure to create any necessary directories if they don't exist.
    print(f"Generating page {from_path} with template {template_path} to {dest_path}")

    text=open(from_path)
    md_lines=text.read()
    text.close()

    template_text=open(template_path)
    template_lines=template_text.read()
    template_text.close()

    html_lines=markdown_to_html_node(md_lines)

    md_title=extract_title(from_path)

    #elif all(lsplit[x].startswith(f"{x+1}. ") for x in range(0,len(lsplit))):

    html_t=""
    for x in html_lines.children:
        html_t+=x.to_html()
    print(html_t)

    template_lines=template_lines.replace("{{ Title }}", md_title)
    template_lines=template_lines.replace("{{ Content }}", html_t)
    print(template_lines)

    content_list=[item for sublist in template_lines for item in sublist]

    dest_file=open(dest_path, mode='w')
    for line in content_list:
        dest_file.write(line)
    dest_file.flush()
    dest_file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    # generate pages
    project_dir="/".join(__file__.split('/')[0:-2])

    full_src=f"{project_dir}/{dir_path_content}"
    full_dst=f"{project_dir}/{dest_dir_path}"
    print(full_src)
    print(full_dst)

    src_list=os.listdir(full_src)
    for src_item in src_list:
        item_path=f"{full_src}/{src_item}"
        dst_item=f"{src_item.split('.')[0]}.html"
        if os.path.isfile(item_path):
            generate_page(item_path, template_path, f"{dest_dir_path}/{dst_item}")
            print(f"generated {item_path}")
        elif os.path.isdir(item_path):
            if not os.path.isdir(f"{full_dst}/{src_item}"):
                os.mkdir(f"{full_dst}/{src_item}")
                print(f"mk'd dir {item_path}")
            # recurse here
            print(f"recursing on {dir_path_content}/{src_item} and {dest_dir_path}/{src_item}")
            generate_pages_recursive(f"{dir_path_content}/{src_item}", template_path, f"{dest_dir_path}/{src_item}")

def main():
    dir_copy("static", "public")
    title=extract_title('content/index.md')
    generate_pages_recursive("content", "template.html", "public")

if __name__ == "__main__":
    main()
