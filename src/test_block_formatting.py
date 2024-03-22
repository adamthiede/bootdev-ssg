import unittest

from block_formatting import markdown_to_blocks, block_to_block_type


class TestHTMLNode(unittest.TestCase):
    def test_to_blocks(self):
        text="""
  This is **bolded** paragraph    

This is another paragraph with *italic* text and `code` here
 This is the same paragraph on a new line

* This is a list
* with items

        """
        manual_blocks = [
        "This is **bolded** paragraph",
        "This is another paragraph with *italic* text and `code` here\n This is the same paragraph on a new line",
        "* This is a list\n* with items"
        ]
        blocks=markdown_to_blocks(text)
        self.assertEqual(len(blocks),len(manual_blocks))
        self.assertEqual(blocks,manual_blocks)
    def test_block_types(self):
        ol="1. one\n2. two\n3. three\n4. four"
        self.assertEqual(block_to_block_type(ol),"ordered_list")

        quote="> quote\n> quote2\n> quote3"
        self.assertEqual(block_to_block_type(quote),"quote")

        head="## This is a heading"
        self.assertEqual(block_to_block_type(head),"heading")
        nohead="####### This is not a heading, too many"
        self.assertEqual(block_to_block_type(nohead),"paragraph")

if __name__ == "__main__":
    unittest.main()
