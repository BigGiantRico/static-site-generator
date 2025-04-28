import unittest

def markdown_to_blocks(markdown):
    mark = markdown.split("\n\n")
    mark = [m.strip("\n").strip(" ") for m in mark]
    mark = [m for m in mark if m]
    return mark