import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from blocktype import Blocktype, block_to_block_type

class TestBlockType(unittest.TestCase):
    def test_heading(self):
        input_text = "# Heading 1"
        expected = Blocktype.HEADING
        actual = block_to_block_type(input_text)
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)
        print("------------")

    def test_code(self):
        input_text = "```print('Hello')```"
        expected = Blocktype.CODE
        actual = block_to_block_type(input_text)
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)
        print("------------")

    def test_quote(self):
        input_text = "> This is a quote"
        expected = Blocktype.QUOTE
        actual = block_to_block_type(input_text)
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)
        print("------------")

    def test_unordered_list(self):
        input_text = "- List item"
        expected = Blocktype.UNORDERED_LIST
        actual = block_to_block_type(input_text)
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)
        print("------------")

    def test_ordered_list(self):
        input_text = "1. First item"
        expected = Blocktype.ORDERED_LIST
        actual = block_to_block_type(input_text)
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)
        print("------------")

    def test_paragraph(self):
        input_text = "This is a regular paragraph"
        expected = Blocktype.PARAGRAPH
        actual = block_to_block_type(input_text)
        print(f"Input: {input_text}")
        print(f"Expected: {expected}")
        print(f"Actual: {actual}")
        self.assertEqual(expected, actual)
        print("------------")

if __name__ == "__main__":
    unittest.main()
