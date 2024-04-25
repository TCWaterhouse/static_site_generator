import unittest

from inline_markdown import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link
)

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
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

    def test_split_images_none(self):
        node = TextNode("This text has no *images*", text_type_text)
        self.assertEqual(
            [TextNode("This text has no *images*", text_type_text)],
            split_nodes_image([node])
        )

    def test_split_images_multiple(self):
        node = TextNode("This text has an ![image](www.test.com) with ![another](www.example.com) and some text after", text_type_text)
        self.assertEqual(
            [
                TextNode("This text has an ", text_type_text),
                TextNode("image", text_type_image, "www.test.com"),
                TextNode(" with ", text_type_text),
                TextNode("another", text_type_image, "www.example.com"),
                TextNode(" and some text after", text_type_text)
            ],
            split_nodes_image([node])
        )

    def test_split_images_both_types(self):
        node = TextNode("This text has an ![image](www.test.com) and a [link](www.link.com)", text_type_text)
        self.assertEqual(
            [
                TextNode("This text has an ", text_type_text),
                TextNode("image", text_type_image, "www.test.com"),
                TextNode(" and a [link](www.link.com)", text_type_text)
            ],
            split_nodes_image([node])
        )
    
    def test_split_images_multiple_nodes(self):
        nodes = [
            TextNode("An ![image](www.test.com)", text_type_text),
            TextNode("Another sentance with an ![image](www.example.com) and a word", text_type_text)
        ]
        self.assertEqual(
            [
                TextNode("An ", text_type_text),
                TextNode("image", text_type_image, "www.test.com"),
                TextNode("Another sentance with an ", text_type_text),
                TextNode("image", text_type_image, "www.example.com"),
                TextNode(" and a word", text_type_text)
            ],
            split_nodes_image(nodes)
        )

    def test_split_links_multiple(self):
        node = TextNode("This text has an [link](www.test.com) with [another](www.example.com) and some text after", text_type_text)
        self.assertEqual(
            [
                TextNode("This text has an ", text_type_text),
                TextNode("link", text_type_link, "www.test.com"),
                TextNode(" with ", text_type_text),
                TextNode("another", text_type_link, "www.example.com"),
                TextNode(" and some text after", text_type_text)
            ],
            split_nodes_link([node])
        )

if __name__ == "__main__":
    unittest.main()