class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def preOrder(node, res):
    if not node:
        return
    res.append(node.data)
    preOrder(node.left, res)
    preOrder(node.right, res)
