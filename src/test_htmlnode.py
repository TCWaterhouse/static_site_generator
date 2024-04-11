import unittest

from htmlnode import HTMLNode

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

if __name__ == "__main__":
    unittest.main()