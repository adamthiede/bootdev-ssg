import unittest

from textnode import TextNode
from textnode import split_nodes_delimiter, text_node_to_html_node, extract_markdown_images, extract_markdown_links


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(node, node2)
    def test_print(self):
        node = TextNode("This is a text node", "bold")
        node2 = TextNode("This is a text node", "bold")
        self.assertEqual(print(node), print(node2))
    def test_neq(self):
        node = TextNode("This is a text node", "bold", "http://url.com")
        node2 = TextNode("This is a text node", "bold")
        self.assertNotEqual(node, node2)
    def test_link(self):
        text = "This is text with a [link](https://www.example.com) and [another](https://www.example.com/another)"
        links=extract_markdown_links(text)
        self.assertEqual(2,len(links))


if __name__ == "__main__":
    unittest.main()
