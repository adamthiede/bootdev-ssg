import unittest

from block_formatting import markdown_to_blocks


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

if __name__ == "__main__":
    unittest.main()
