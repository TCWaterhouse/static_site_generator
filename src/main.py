from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    node = ParentNode(
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
            node,
            LeafNode("b", "Test Text")
        ],
    )

    string = node2.to_html()

    

main()