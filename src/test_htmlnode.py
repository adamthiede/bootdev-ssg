import unittest

from htmlnode import HTMLNode


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
        self.assertEqual(print(node), print(node2))
    def test_neq(self):
        chld=HTMLNode("tr", "table", None, "bold")
        node = HTMLNode("p","This is a paragraph node", None, "bold")
        self.assertNotEqual(chld, node)


if __name__ == "__main__":
    unittest.main()
