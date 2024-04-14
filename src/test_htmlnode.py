import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode

class TestHTMLNode(unittest.TestCase):
    def test_repr(self):
        node = HTMLNode("p", "Test Text", None, {"href": "https://www.test.com"})
        self.assertEqual(
            "HTMLNode(p, Test Text, children: None, {'href': 'https://www.test.com'})", repr(node)
        )

    def test_to_html(self):
        node = HTMLNode("p", "Test Text", None, {"href": "https://www.test.com"})
        self.assertRaises(Exception, node.to_html)

    def test_props_to_html(self):
        node1 = HTMLNode("p", "Test Text", None, {"href": "tel:+447000112233"})
        node2 = HTMLNode("p", "Test Text", None, {"href": "https://www.test.com", "target": "_blank"})
        self.assertEqual(
            ' href="tel:+447000112233"', node1.props_to_html()
        )
        self.assertEqual(
            ' href="https://www.test.com" target="_blank"', node2.props_to_html()
        )

    def test_props_to_html_def(self):
        node = HTMLNode("a")
        self.assertEqual("", node.props_to_html())

class TestLeafNode(unittest.TestCase):
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

class TestParentNode(unittest.TestCase):
    def test_to_html_no_tag(self):
        node = ParentNode(None, [LeafNode("b", "Bold text")])
        self.assertRaises(ValueError, node.to_html)

    def test_to_html_no_children(self):
        node = ParentNode("p", None)
        self.assertRaises(ValueError, node.to_html)

    def test_to_html(self):
        node1 = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )

        node2 = ParentNode(
            "p",
            [
                node1,
                LeafNode("b", "Test Text")
            ],
        )

        node3 = ParentNode(
            "div",
            [
                LeafNode("a", "Test Nested"),
                node2
            ],
        )

        self.assertEqual(
            "<div><a>Test Nested</a><p><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p><b>Test Text</b></p></div>",
            node3.to_html()
        )

if __name__ == "__main__":
    unittest.main()