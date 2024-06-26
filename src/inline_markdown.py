import re

from textnode import (
    TextNode,
    text_type_text,
    text_type_bold,
    text_type_italic,
    text_type_code,
    text_type_image,
    text_type_link
)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        split_nodes = []
        segments = node.text.split(delimiter)
        if len(segments) % 2 == 0:
            raise ValueError("Invalid Markdown: Formatted section not closed")
        for i in range(len(segments)):
            if segments[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(segments[i], text_type_text))
            else:
                split_nodes.append(TextNode(segments[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        image_tups = extract_markdown_images(node.text)
        if len(image_tups) == 0:
            new_nodes.append(node)
            continue
        split_nodes = []
        original_text = node.text
        for image_tup in image_tups:
            segments = original_text.split(f"![{image_tup[0]}]({image_tup[1]})", 1)
            if image_tup == image_tups[-1]:
                if segments[0] != "":
                    split_nodes.append(TextNode(segments[0], text_type_text))
                split_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
                if segments[1] != "":
                    split_nodes.append(TextNode(segments[1], text_type_text))
            else:
                if segments[0] != "":
                    split_nodes.append(TextNode(segments[0], text_type_text))
                split_nodes.append(TextNode(image_tup[0], text_type_image, image_tup[1]))
                original_text = segments[1]
        new_nodes.extend(split_nodes)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != text_type_text:
            new_nodes.append(node)
            continue
        link_tups = extract_markdown_links(node.text)
        if len(link_tups) == 0:
            new_nodes.append(node)
            continue
        split_nodes = []
        original_text = node.text
        for link_tup in link_tups:
            segments = original_text.split(f"[{link_tup[0]}]({link_tup[1]})", 1)
            if link_tup == link_tups[-1]:
                if segments[0] != "":
                    split_nodes.append(TextNode(segments[0], text_type_text))
                split_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
                if segments[1] != "":
                    split_nodes.append(TextNode(segments[1], text_type_text))
            else:
                if segments[0] != "":
                    split_nodes.append(TextNode(segments[0], text_type_text))
                split_nodes.append(TextNode(link_tup[0], text_type_link, link_tup[1]))
                original_text = segments[1]
        new_nodes.extend(split_nodes)
    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, text_type_text)]
    nodes = split_nodes_delimiter(nodes, "**", text_type_bold)
    nodes = split_nodes_delimiter(nodes, "*", text_type_italic)
    nodes = split_nodes_delimiter(nodes, "`", text_type_code)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes