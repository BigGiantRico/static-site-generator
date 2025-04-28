from blocktype import block_to_block_type, Blocktype
from htmlnode import HTMLNode, LeafNode, ParentNode
from splitblocks import markdown_to_blocks
from splitnode import text_to_textnodes
from textnode import TextNode, TextType
import re

def heading_node(block):
    h, tags = 0, block.split(" ")[0]
    text = block.split(f"{tags} ")[1]
    for tag in tags:
        h += 1
    children = text_to_children(text)
    return ParentNode(f"h{h}", children)

def code_node(block):
    text = block.split("```")[1]
    children = text_to_children(text)
    return ParentNode("pre", [ParentNode("code", children)])

def quote_node(block):
    text = block.split("> ")[1]
    children = text_to_children(text)
    return ParentNode("blockquote", children)

def ordered_list_node(block):
    list_items = [item.strip() for item in re.split(r"\d+\.\s+", block) if item.strip()]
    print(list_items)
    temp = []
    for item in list_items:
        temp.append(ParentNode("li", text_to_children(item)))
    return ParentNode("ol", temp)

def unordered_list_node(block):
    list_items = [item.strip() for item in re.split(r"-\s+", block) if item.strip()]
    print(list_items)
    temp = []
    for item in list_items:
        temp.append(ParentNode("li", text_to_children(item)))
    return ParentNode("ul", temp)

def paragraph_node(block):
    text = block
    children = text_to_children(text)
    return ParentNode("p", children)


def text_to_children(text):
    textnodes = text_to_textnodes([TextNode(text, TextType.TEXT)])
    return [textnode.text_node_to_html_node() for textnode in textnodes]
    

def markdown_to_html(markdown):
    blocks = markdown_to_blocks(markdown)
    nodes = []
    for block in blocks:
        btype = block_to_block_type(block)
        if btype == Blocktype.HEADING:
            nodes.append(heading_node(block))
        elif btype == Blocktype.CODE:
            nodes.append(code_node(block))
        elif btype == Blocktype.QUOTE:
            nodes.append(quote_node(block))
        elif btype == Blocktype.ORDERED_LIST:
            nodes.append(ordered_list_node(block))
        elif btype == Blocktype.UNORDERED_LIST:
            nodes.append(unordered_list_node(block))
        elif btype == Blocktype.PARAGRAPH:
            nodes.append(paragraph_node(block))
        else:
            raise Exception("Invalid Markdown!!!")

    return ParentNode("div", nodes).to_html()