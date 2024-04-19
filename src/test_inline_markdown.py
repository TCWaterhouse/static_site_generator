import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code
)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_one_type(self):
        node = TextNode("This is text with a `code block` word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word", text_type_text),
            ],
            new_nodes
        )

    def test_split_nodes_two_types(self):
        node = TextNode("This is text with a `code block` word as well as a **bold** word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "`", text_type_code)
        newer_nodes = split_nodes_delimiter(new_nodes, "**", text_type_bold)
        self.assertEqual(
            [
                TextNode("This is text with a ", text_type_text),
                TextNode("code block", text_type_code),
                TextNode(" word as well as a ", text_type_text),
                TextNode("bold", text_type_bold),
                TextNode(" word", text_type_text)
            ],
            newer_nodes
        )

    def test_split_nodes_one_type_double(self):
        node = TextNode("This is text with an *italic and fancy* word with another *italic* word", text_type_text)
        new_nodes = split_nodes_delimiter([node], "*", text_type_italic)
        self.assertEqual(
            [
                TextNode("This is text with an ", text_type_text),
                TextNode("italic and fancy", text_type_italic),
                TextNode(" word with another ", text_type_text),
                TextNode("italic", text_type_italic),
                TextNode(" word", text_type_text)
            ],
            new_nodes
        )

    def test_split_nodes_error(self):
        node = TextNode("This is text with a `code block word", text_type_text)
        self.assertRaises(ValueError, split_nodes_delimiter, [node], "`", text_type_code)

    def test_extract_images(self):
        text = "This is text with an ![image](www.test.com) and ![another](www.anothertest.com)"
        self.assertEqual(
            [("image", "www.test.com"), ("another", "www.anothertest.com")],
            extract_markdown_images(text)
        )

    def test_extract_links(self):
        text = "This is text with an [link](www.test.com) and [another](www.anothertest.com)"
        self.assertEqual(
            [("link", "www.test.com"), ("another", "www.anothertest.com")],
            extract_markdown_links(text)
        )

    def test_extract_both(self):
        text = "This is text with an ![image](www.test.com) and [link](www.link.com)"
        self.assertEqual(
            [("link", "www.link.com")],
            extract_markdown_links(text)
        )

if __name__ == "__main__":
    unittest.main()