class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def inorder(root, prev):
    if root is None:
        return True

    if not inorder(root.left, prev):
        return False

    if prev[0] >= root.data:
        return False

    prev[0] = root.data

    return inorder(root.right, prev)


def isBST(root):
    prev = [float('-inf')]
    return inorder(root, prev)
