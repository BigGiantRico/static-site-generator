import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from extractmarkdown import extract_markdown_images, extract_markdown_links

class TestExtractMarkdown(unittest.TestCase):
    def setUp(self):
        self.maxDiff = None  # Show full diffs
    
    def print_test_info(self, test_num, input_desc, expected, actual):
        print(f"\nTest {test_num}.")
        print("Input:")
        print(input_desc)
        print("\nExpected:")
        print(expected)
        print("\nActual:")
        print(actual)
        print("\n------")

    def test_extract_markdown_images(self):
        # Test 1: Single image
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png)"
        expected = [("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png")]
        actual = extract_markdown_images(text)
        self.print_test_info(1, text, expected, actual)
        self.assertEqual(actual, expected)

        # Test 2: Multiple images
        text = "This is text with an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and another ![second image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png)"
        expected = [
            ("image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png"),
            ("second image", "https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/3elNhQu.png")
        ]
        actual = extract_markdown_images(text)
        self.print_test_info(2, text, expected, actual)
        self.assertEqual(actual, expected)

        # Test 3: No images
        text = "This is text with no images"
        expected = []
        actual = extract_markdown_images(text)
        self.print_test_info(3, text, expected, actual)
        self.assertEqual(actual, expected)

    def test_extract_markdown_links(self):
        # Test 1: Single link
        text = "This is text with a [link](https://www.example.com)"
        expected = [("link", "https://www.example.com")]
        actual = extract_markdown_links(text)
        self.print_test_info(1, text, expected, actual)
        self.assertEqual(actual, expected)

        # Test 2: Multiple links
        text = "This is text with a [link](https://www.example.com) and another [second link](https://www.example2.com)"
        expected = [
            ("link", "https://www.example.com"),
            ("second link", "https://www.example2.com")
        ]
        actual = extract_markdown_links(text)
        self.print_test_info(2, text, expected, actual)
        self.assertEqual(actual, expected)

        # Test 3: No links
        text = "This is text with no links"
        expected = []
        actual = extract_markdown_links(text)
        self.print_test_info(3, text, expected, actual)
        self.assertEqual(actual, expected)

if __name__ == "__main__":
    unittest.main()