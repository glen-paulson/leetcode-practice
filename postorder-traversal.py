class Node:
    def __init__(self, v):
        self.data = v
        self.left = None
        self.right = None


def postOrder(node, res):
    if node is None:
        return
    postOrder(node.left, res)
    postOrder(node.right, res)
    res.append(node.data)
