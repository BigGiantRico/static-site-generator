from enum import Enum
import re


class Blocktype(Enum):
    PARAGRAPH = "paragraph"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST = "ordered_list"

def block_to_block_type(markdown):
    if re.match(r'#{1,6} ', markdown):
        return Blocktype.HEADING
    if re.match(r'^`{3}.*`{3}$', markdown, re.DOTALL):
        return Blocktype.CODE
    if re.match(r'^>\s', markdown):
        return Blocktype.QUOTE
    if re.match(r'^-\s', markdown):
        return Blocktype.UNORDERED_LIST
    if re.match(r'^\d+\.\s', markdown):
        return Blocktype.ORDERED_LIST
    return Blocktype.PARAGRAPH