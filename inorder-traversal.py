class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None


def inOrder(node, res):
    if node is None:
        return
    inOrder(node.left, res)
    res.append(node.data)
    inOrder(node.right, res)
