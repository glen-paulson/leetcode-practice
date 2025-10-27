class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def maxValue(root):
    if root is None:
        return -1

    curr_pointer = root
    while curr_pointer.right is not None:
        curr_pointer = curr_pointer.right

    return curr_pointer.data
