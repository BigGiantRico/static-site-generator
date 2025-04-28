import re
from textnode import TextNode, TextType
from extractmarkdown import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, t):
    new_nodes = []
    pattern = re.compile(rf"{re.escape(delimiter)}(.*?){re.escape(delimiter)}")

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        temp = node.text
        last_end = 0

        for match in pattern.finditer(temp):
            start, end = match.span()
            content = match.group(1)

            if start > last_end:
                new_nodes.append(TextNode(temp[last_end:start], TextType.TEXT))

            new_nodes.append(TextNode(content, t))
            last_end = end

        if last_end < len(temp):
            new_nodes.append(TextNode(temp[last_end:], TextType.TEXT))

    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        alt_text = [img[0] for img in extract_markdown_images(node.text)]
        url = [img[1] for img in extract_markdown_images(node.text)]
        temp = node.text

        for alt, rl in zip(alt_text, url):
            before, mid, after = temp.partition(f"![{alt}]({rl})")
            temp = after

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.IMAGE, rl))

        if temp:
            new_nodes.append(TextNode(temp, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue

        alt_text = [img[0] for img in extract_markdown_links(node.text)]
        url = [img[1] for img in extract_markdown_links(node.text)]
        temp = node.text

        for alt, rl in zip(alt_text, url):
            before, mid, after = temp.partition(f"[{alt}]({rl})")
            temp = after

            if before:
                new_nodes.append(TextNode(before, TextType.TEXT))
            new_nodes.append(TextNode(alt, TextType.LINK, rl))

        if temp:
            new_nodes.append(TextNode(temp, TextType.TEXT))

    return new_nodes

def text_to_textnodes(old_nodes):
    nodes = split_nodes_image(old_nodes)
    nodes = split_nodes_link(nodes)
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    return nodes