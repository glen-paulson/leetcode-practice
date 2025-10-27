class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def minVal(root):
    if root is None:
        return -1

    curr_pointer = root

    while curr_pointer.left is not None:
        curr_pointer = curr_pointer.left

    return curr_pointer.data
