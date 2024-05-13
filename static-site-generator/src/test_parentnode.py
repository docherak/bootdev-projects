import unittest

from htmlnode import ParentNode

class TestParentNode(unittest.TestCase):
    def test_parentnode(self):
        node = ParentNode("div", ["Lorem Ipsum"], {"class": "bold"})
        self.assertEqual(str(node), "ParentNode(div, children: ['Lorem Ipsum'], {'class': 'bold'})")

if __name__ == "__main__":
    unittest.main()