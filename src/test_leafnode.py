import unittest

from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_value_none(self):
        self.assertRaises(Exception, LeafNode, "a")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Test Text")
        self.assertEqual('Test Text', node.to_html())

    def test_to_html_no_props(self):
        node = LeafNode("p", "This is a test sentance.")
        self.assertEqual('<p>This is a test sentance.</p>', node.to_html())

    def test_to_html(self):
        node = LeafNode("a", "Website", {"href": "https://www.test.com", "target": "_blank"})
        self.assertEqual('<a href="https://www.test.com" target="_blank">Website</a>', node.to_html())

if __name__ == "__main__":
    unittest.main()