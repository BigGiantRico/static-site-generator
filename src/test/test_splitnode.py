import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from splitnode import *
from textnode import *


class TestSplitNode(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        self.maxDiff = None
        # Test case 1: Basic text with bold delimiter
        input_nodes = [TextNode("This is **bold** text", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(" text", TextType.TEXT)
        ]
        actual = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        print(f"\nTest Case 1 - Basic bold text:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 2: Text with code delimiter
        input_nodes = [TextNode("This is `code` text", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" text", TextType.TEXT)
        ]
        actual = split_nodes_delimiter(input_nodes, "`", TextType.CODE)
        print(f"\nTest Case 2 - Code text:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 3: Text with italic delimiter
        input_nodes = [TextNode("This is *italic* text", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" text", TextType.TEXT)
        ]
        actual = split_nodes_delimiter(input_nodes, "*", TextType.ITALIC)
        print(f"\nTest Case 3 - Italic text:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 4: Non-text node should remain unchanged
        input_nodes = [TextNode("This is bold text", TextType.BOLD)]
        expected = [TextNode("This is bold text", TextType.BOLD)]
        actual = split_nodes_delimiter(input_nodes, "**", TextType.BOLD)
        print(f"\nTest Case 4 - Non-text node:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

    def test_split_nodes_image(self):
        self.maxDiff = None
        # Test case 1: Text with single image
        input_nodes = [TextNode("This is ![alt text](https://example.com/image.png) text", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("alt text", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(" text", TextType.TEXT)
        ]
        actual = split_nodes_image(input_nodes)
        print(f"\nTest Case 1 - Single image:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 2: Text with multiple images
        input_nodes = [TextNode("![first](https://example.com/1.png) and ![second](https://example.com/2.png)", TextType.TEXT)]
        expected = [
            TextNode("first", TextType.IMAGE, "https://example.com/1.png"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.IMAGE, "https://example.com/2.png")
        ]
        actual = split_nodes_image(input_nodes)
        print(f"\nTest Case 2 - Multiple images:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 3: Text with no images
        input_nodes = [TextNode("This is plain text", TextType.TEXT)]
        expected = [TextNode("This is plain text", TextType.TEXT)]
        actual = split_nodes_image(input_nodes)
        print(f"\nTest Case 3 - No images:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

    def test_split_nodes_link(self):
        self.maxDiff = None
        # Test case 1: Text with single link
        input_nodes = [TextNode("This is [link text](https://example.com) text", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("link text", TextType.LINK, "https://example.com"),
            TextNode(" text", TextType.TEXT)
        ]
        actual = split_nodes_link(input_nodes)
        print(f"\nTest Case 1 - Single link:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 2: Text with multiple links
        input_nodes = [TextNode("[first](https://example.com/1) and [second](https://example.com/2)", TextType.TEXT)]
        expected = [
            TextNode("first", TextType.LINK, "https://example.com/1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("second", TextType.LINK, "https://example.com/2"),
        ]
        actual = split_nodes_link(input_nodes)
        print(f"\nTest Case 2 - Multiple links:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 3: Text with no links
        input_nodes = [TextNode("This is plain text", TextType.TEXT)]
        expected = [TextNode("This is plain text", TextType.TEXT)]
        actual = split_nodes_link(input_nodes)
        print(f"\nTest Case 3 - No links:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

    def test_text_to_textnodes(self):
        self.maxDiff = None 
        # Test case 1: Text with all types of markdown
        input_nodes = [TextNode("This is **bold**, _italic_, `code`, ![image](https://example.com/image.png), and [link](https://example.com)", TextType.TEXT)]
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold", TextType.BOLD),
            TextNode(", ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(", ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(", ", TextType.TEXT),
            TextNode("image", TextType.IMAGE, "https://example.com/image.png"),
            TextNode(", and ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://example.com")
        ]
        actual = text_to_textnodes(input_nodes)
        print(f"\nTest Case 1 - All markdown types:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)

        # Test case 2: Plain text
        input_nodes = [TextNode("This is plain text", TextType.TEXT)]
        expected = [TextNode("This is plain text", TextType.TEXT)]
        actual = text_to_textnodes(input_nodes)
        print(f"\nTest Case 2 - Plain text:")
        print(f"Input: {input_nodes}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        print("----------------------------")
        self.assertEqual(actual, expected)    


if __name__ == "__main__":
    unittest.main()