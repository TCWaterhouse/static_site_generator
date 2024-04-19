from textnode import (
    TextNode, 
    text_type_text, 
    text_type_bold, 
    text_type_italic, 
    text_type_code
)

from htmlnode import (
    HTMLNode, 
    LeafNode, 
    ParentNode
)

from inline_markdown import split_nodes_delimiter

def main():
    node = TextNode("This is text with a `code block` word", text_type_text)
    new_nodes = split_nodes_delimiter([node], "`", text_type_code)
    print(len(new_nodes))
    
if __name__ == "__main__":
    main()