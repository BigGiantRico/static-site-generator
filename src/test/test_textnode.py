import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from textnode import TextNode, TextType
from htmlnode import LeafNode


class TestTextNode(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None  # Show full diffs
    
    def print_test_info(self, input_desc, expected, actual):
        print("\nInput:")
        print(input_desc)
        print("\nExpected:")
        print(expected)
        print("\n-----------------")
        print("\nActual:")
        print(actual)
        print("\n")

    def test_eq(self):
        node1 = TextNode("This is a text node", TextType.LINK, "https")
        node2 = TextNode("This is a bang node", TextType.BOLD)
        node3 = TextNode("This is a text node", TextType.LINK, "https")
        
        self.assertEqual(node1, node3)
    
    def test_text_type_text_to_html_node(self):
        text_node = TextNode("Just plain text", TextType.TEXT)
        expected = LeafNode(None, "Just plain text")
        actual = text_node.text_node_to_html_node()
        
        self.print_test_info(
            f"TextNode(text='Just plain text', text_type=TextType.TEXT)",
            expected.to_html(),
            actual.to_html()
        )
        self.assertEqual(actual.to_html(), expected.to_html())
    
    def test_text_type_bold_to_html_node(self):
        text_node = TextNode("Bold text", TextType.BOLD)
        expected = LeafNode("b", "Bold text")
        actual = text_node.text_node_to_html_node()
        
        self.print_test_info(
            f"TextNode(text='Bold text', text_type=TextType.BOLD)",
            expected.to_html(),
            actual.to_html()
        )
        self.assertEqual(actual.to_html(), expected.to_html())
    
    def test_text_type_italic_to_html_node(self):
        text_node = TextNode("Italic text", TextType.ITALIC)
        expected = LeafNode("i", "Italic text")
        actual = text_node.text_node_to_html_node()
        
        self.print_test_info(
            f"TextNode(text='Italic text', text_type=TextType.ITALIC)",
            expected.to_html(),
            actual.to_html()
        )
        self.assertEqual(actual.to_html(), expected.to_html())
    
    def test_text_type_code_to_html_node(self):
        text_node = TextNode("Code text", TextType.CODE)
        expected = LeafNode("code", "Code text")
        actual = text_node.text_node_to_html_node()
        
        self.print_test_info(
            f"TextNode(text='Code text', text_type=TextType.CODE)",
            expected.to_html(),
            actual.to_html()
        )
        self.assertEqual(actual.to_html(), expected.to_html())
    
    def test_text_type_link_to_html_node(self):
        text_node = TextNode("Click me", TextType.LINK, "https://www.google.com")
        expected = LeafNode("a", "Click me", {"href": "https://www.google.com"})
        actual = text_node.text_node_to_html_node()
        
        self.print_test_info(
            f"TextNode(text='Click me', text_type=TextType.LINK, url='https://www.google.com')",
            expected.to_html(),
            actual.to_html()
        )
        self.assertEqual(actual.to_html(), expected.to_html())
    
    def test_text_type_image_to_html_node(self):
        text_node = TextNode("Alt text", TextType.IMAGE, "image.png")
        expected = LeafNode("img", "", {"src": "image.png", "alt": "Alt text"})
        actual = text_node.text_node_to_html_node()
        
        self.print_test_info(
            f"TextNode(text='Alt text', text_type=TextType.IMAGE, url='image.png')",
            expected.to_html(),
            actual.to_html()
        )
        self.assertEqual(actual.to_html(), expected.to_html())


if __name__ == "__main__":
    unittest.main()