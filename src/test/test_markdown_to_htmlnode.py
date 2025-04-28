import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from markdown_to_htmlnode import markdown_to_html
from htmlnode import ParentNode, LeafNode

class TestMarkdownToHTMLNode(unittest.TestCase):
    def test_paragraph(self):
        print("\nTesting paragraph conversion:")
        print("Input: This is a paragraph")
        md = "This is a paragraph"
        node = markdown_to_html(md)
        print("Expected output: <div><p>This is a paragraph</p></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This is a paragraph")
                ])
            ]).to_html()
        )

    def test_heading(self):
        print("\nTesting heading conversion:")
        print("Input: # Heading 1")
        md = "# Heading 1"
        node = markdown_to_html(md)
        print("Expected output: <div><h1>Heading 1</h1></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("h1", [
                    LeafNode(None, "Heading 1")
                ])
            ]).to_html()
        )
        

    def test_bold(self):
        print("\nTesting bold text conversion:")
        print("Input: This is **bold** text")
        md = "This is **bold** text"
        node = markdown_to_html(md)
        print("Expected output: <div><p>This is <b>bold</b> text</p></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This is "),
                    LeafNode("b", "bold"),
                    LeafNode(None, " text")
                ])
            ]).to_html()
        )
        

    def test_italic(self):
        print("\nTesting italic text conversion:")
        print("Input: This is _italic_ text")
        md = "This is _italic_ text"
        node = markdown_to_html(md)
        print("Expected output: <div><p>This is <i>italic</i> text</p></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This is "),
                    LeafNode("i", "italic"),
                    LeafNode(None, " text")
                ])
            ]).to_html()
        )
        

    def test_code(self):
        print("\nTesting code block conversion:")
        print("Input: This is `code` text")
        md = "This is `code` text"
        node = markdown_to_html(md)
        print("Expected output: <div><p>This is <code>code</code> text</p></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This is "),
                    LeafNode("code", "code"),
                    LeafNode(None, " text")
                ])
            ]).to_html()
        )
        

    def test_link(self):
        print("\nTesting link conversion:")
        print("Input: This is a [link](https://example.com)")
        md = "This is a [link](https://example.com)"
        node = markdown_to_html(md)
        print("Expected output: <div><p>This is a <a href=\"https://example.com\">link</a></p></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This is a ", None),
                    LeafNode("a", "link", {"href": "https://example.com"})
                ])
            ]).to_html()
        )
        

    def test_image(self):
        print("\nTesting image conversion:")
        print("Input: This is an ![image](https://example.com/image.jpg)")
        md = "This is an ![image](https://example.com/image.jpg)"
        node = markdown_to_html(md)
        print("Expected output: <div><p>This is an <img src=\"https://example.com/image.jpg\" alt=\"image\"/></p></div>")
        print("Actual output:", node)
        print("--------------")
        self.assertEqual(
            node,
            ParentNode("div", [
                ParentNode("p", [
                    LeafNode(None, "This is an "),
                    LeafNode("img", "", {"src": "https://example.com/image.jpg", "alt": "image"}),
                ])
            ]).to_html()
        )

        

if __name__ == "__main__":
    unittest.main()