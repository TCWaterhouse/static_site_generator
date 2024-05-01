import unittest

from blocks_markdown import (
    markdown_to_blocks,
    block_to_block_type,
    block_type_paragraph,
    block_type_heading,
    block_type_code,
    block_type_quote,
    block_type_unordered_list,
    block_type_ordered_list
)

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = """
This is **bolded** paragraph

The first paragraph


This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line



* This is a list
* with items
"""
        self.assertEqual(
            [
                "This is **bolded** paragraph",
                "The first paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items"
            ],
            markdown_to_blocks(markdown)
        )

    def test_blocktype_heading_correct(self):
        block_heading = "### Big Title"
        self.assertEqual(block_type_heading, block_to_block_type(block_heading))

    def test_blocktype_heading_incorrect(self):
        block_heading = "#####Big Title"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_heading))

    def test_blocktype_code_correct(self):
        block_code = "```\nx + y = 5\ncode\n```"
        self.assertEqual(block_type_code, block_to_block_type(block_code))

    def test_blocktype_code_incorrect_end(self):
        block_code = "```\nx + y = 5\ncode\n"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_code))

    def test_blocktype_code_incorrect_lines(self):
        block_code = "```x + y = 5```n"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_code))

    def test_blocktype_quote_correct(self):
        block_quote = ">bla bla bla\n>more bla"
        self.assertEqual(block_type_quote, block_to_block_type(block_quote))

    def test_blocktype_quote_incorrect(self):
        block_quote = ">bla bla bla\nmore bla"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_quote))

    def test_blocktype_ul_correct(self):
        block_unordered_list_ast = "* a list\n* another line in a list"
        block_unordered_list_dash = "- 1st item in a\n- list of things"
        self.assertEqual(block_type_unordered_list, block_to_block_type(block_unordered_list_ast))
        self.assertEqual(block_type_unordered_list, block_to_block_type(block_unordered_list_dash))

    def test_blocktype_ul_incorrect(self):
        block_unordered_list_ast = "*a list\n* another line in a list"
        block_unordered_list_dash = "- 1st item in a\n* list of things"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_unordered_list_ast))
        self.assertEqual(block_type_paragraph, block_to_block_type(block_unordered_list_dash))

    def test_blocktype_ol_correct(self):
        block_ordered_list = "1. First item\n2. Second item\n3. Third Item"
        self.assertEqual(block_type_ordered_list, block_to_block_type(block_ordered_list))

    def test_blocktype_ol_incorrect(self):
        block_ordered_list = "1. First item\n4. Second item\n3. Third Item"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_ordered_list))

    def test_blocktype_paragraph(self):
        block_paragraph = "A bunch of normal text\non another line as well"
        self.assertEqual(block_type_paragraph, block_to_block_type(block_paragraph))

if __name__ == "__main__":
    unittest.main()