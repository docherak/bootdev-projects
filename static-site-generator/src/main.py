from textnode import TextNode
from htmlnode import HTMLNode, LeafNode, ParentNode

def main():
    dummy = TextNode("Lorem Ipsum", "bold")
    print(dummy)

    test = dummy.to_html_node()
    print(test)

    dummy = HTMLNode("div", "Lorem Ipsum", None, {"class": "bold"})
    print(dummy)

    dummy = LeafNode("p", "Lorem Ipsum", {"class": "bold"})
    print(dummy)
    dummy = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
    print(dummy)

    node = ParentNode(
        "p",
        [
            LeafNode("b", "Bold text"),
            LeafNode(None, "Normal text"),
            LeafNode("i", "italic text"),
            LeafNode(None, "Normal text"),
        ],
    )

    print(node.to_html())


main()
