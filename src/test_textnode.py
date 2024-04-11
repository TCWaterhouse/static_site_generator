import unittest

from textnode import TextNode


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", "bold", "www.test.com")
        node2 = TextNode("This is a text node", "bold", "www.test.com")
        self.assertEqual(node, node2)

    def test_neq_1(self):
        node = TextNode("This is a test", "italic", "www.test.com")
        node2 = TextNode("This is not a test", "italic", "www.test.com")
        self.assertNotEqual(node, node2)

    def test_neq_2(self):
        node = TextNode("This is a test", "italic", "www.test.com")
        node2 = TextNode("This is a test", "bold", "www.test.com")
        self.assertNotEqual(node, node2)

    def test_neq_3(self):
        node = TextNode("This is a test", "italic", "www.test.com")
        node2 = TextNode("This is a test", "italic", "www.test.co.uk")
        self.assertNotEqual(node, node2)

    def test_default_url(self):
        node = TextNode("No URL", "bold")
        self.assertIsNone(node.url)

    def test_repr(self):
        node = TextNode("This is a test", "italic", "www.test.com")
        self.assertEqual(
            "TextNode(This is a test, italic, www.test.com)", repr(node)
        )


if __name__ == "__main__":
    unittest.main()
