import unittest

from htmlnode import HTMLNode
from htmlnode import LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_value_none(self):
        self.assertRaises(Exception, LeafNode, "a")

    def test_to_html_1(self):
        node = LeafNode(value="Test Text")
        self.assertEqual('Test Text', node.to_html())

    def test_to_html_2(self):
        node = LeafNode("p", "This is a test sentance.")
        self.assertEqual('<p>This is a test sentance.</p>', node.to_html())

    def test_to_html_3(self):
        node = LeafNode("a", "Website", {"href": "https://www.test.com", "target": "_blank"})
        self.assertEqual('<a href="https://www.test.com" target="_blank">Website</a>', node.to_html())

if __name__ == "__main__":
    unittest.main()