import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode
from htmlnode import ParentNode


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        chld=HTMLNode("tr", "table", None, "bold")
        node = HTMLNode("p","This is a paragraph node", children=chld, props="bold")
        node2 = HTMLNode("p","This is a paragraph node", children=chld, props="bold")
        self.assertEqual(node, node2)
    def test_print(self):
        chld=HTMLNode("tr", "table", None, "bold")
        node = HTMLNode("p","This is a paragraph node", children=chld, props="bold")
        node2 = HTMLNode("p","This is a paragraph node", children=chld, props="bold")
        self.assertEqual(node, node2)
    def test_neq(self):
        chld=HTMLNode("tr", "table", None, "bold")
        node = HTMLNode("p","This is a paragraph node", None, "bold")
        self.assertNotEqual(chld, node)
    def test_parent_node(self):
        leaf1=LeafNode("b","strong!")
        leaf2=LeafNode("i","italic!")
        parent=ParentNode("p", [leaf1, leaf2])
        self.assertNotEqual(leaf1,leaf2)
        self.assertEqual(parent.children,[leaf1,leaf2])

if __name__ == "__main__":
    unittest.main()
