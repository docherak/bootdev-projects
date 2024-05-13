import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_htmlnode(self):
        node = HTMLNode("div", "Lorem Ipsum", None, {"class": "bold"})
        self.assertEqual(str(node), "HTMLNode(div, Lorem Ipsum, children: None, {'class': 'bold'})")

    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )
                                                     
if __name__ == "__main__":
    unittest.main()