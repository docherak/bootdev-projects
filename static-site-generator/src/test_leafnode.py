import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_leafnode(self):
        node = LeafNode("div", "Lorem Ipsum", {"class": "bold"})
        self.assertEqual(str(node), "LeafNode(div, Lorem Ipsum, {'class': 'bold'})")

if __name__ == "__main__":
    unittest.main()