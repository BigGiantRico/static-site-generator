import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
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
        d = {
            "href": "bongie",
            "target": "shifter",
            "rel": "stylesheet"
        }

        node1 = HTMLNode("p", "bababooo", {}, d)
        node2 = HTMLNode("h1", "pewpew", {}, d)
        node3 = HTMLNode("a", "bangbang", {}, d)

    def test_parent_node_with_children(self):
        child1 = LeafNode("p", "First paragraph")
        child2 = LeafNode("p", "Second paragraph")
        parent = ParentNode("div", [child1, child2])
        expected = "<div><p>First paragraph</p><p>Second paragraph</p></div>"
        actual = parent.to_html()
        
        self.print_test_info(
            f"Parent: div\nChildren: [p: 'First paragraph', p: 'Second paragraph']",
            expected,
            actual
        )
        self.assertEqual(actual, expected)

    def test_parent_node_with_grandchildren(self):
        grandchild1 = LeafNode("p", "First paragraph")
        grandchild2 = LeafNode("p", "Second paragraph")
        child1 = ParentNode("div", [grandchild1, grandchild2])
        parent = ParentNode("div", [child1])
        expected = "<div><div><p>First paragraph</p><p>Second paragraph</p></div></div>"
        self.assertEqual(parent.to_html(), expected)
    
    def test_parent_node_with_props(self):
        child = LeafNode("p", "Hello")
        parent = ParentNode("div", [child], {"class": "greeting"})
        expected = '<div class="greeting"><p>Hello</p></div>'
        actual = parent.to_html()
        
        self.print_test_info(
            f"Parent: div with props={{'class': 'greeting'}}\nChild: p: 'Hello'",
            expected,
            actual
        )
        self.assertEqual(actual, expected)

    def test_parent_node_with_grandchildren_and_props(self):
        grandchild1 = LeafNode("p", "First paragraph")
        grandchild2 = LeafNode("p", "Second paragraph")
        child1 = ParentNode("div", [grandchild1, grandchild2])
        parent = ParentNode("div", [child1], {"class": "greeting"}) 
        expected = '<div class="greeting"><div><p>First paragraph</p><p>Second paragraph</p></div></div>'
        self.assertEqual(parent.to_html(), expected)
    
    def test_parent_node_no_children(self):
        with self.assertRaises(ValueError):
            parent = ParentNode("div", None)
            self.print_test_info(
                "Parent: div with no children",
                "ValueError: ParentNode: Missing Children!!",
                "Testing for ValueError..."
            )
            parent.to_html()
    
    def test_parent_node_no_tag(self):
        child = LeafNode("p", "Hello")
        with self.assertRaises(ValueError):
            parent = ParentNode(None, [child])
            self.print_test_info(
                "Parent: no tag with child p: 'Hello'",
                "ValueError: ParentNode: Missing Tag!!",
                "Testing for ValueError..."
            )
            parent.to_html()


if __name__ == "__main__":
    unittest.main()