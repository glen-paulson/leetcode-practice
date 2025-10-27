class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder(root, sortedArr):
    if root is None:
        return

    inorder(root.left, sortedArr)
    sortedArr.append(root.data)
    inorder(root.right, sortedArr)


def maxValue(root):
    if root is None:
        return -1
    sortedArr = []
    inorder(root, sortedArr)

    return sortedArr[-1]
