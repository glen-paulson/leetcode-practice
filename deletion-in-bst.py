# getting the inorder successor - which is the smallest in the right sub tree
def getSuccessor(curr):
    curr = curr.right
    while curr is not None and curr.left is not None:
        curr = curr.left
    return curr


def delNode(root, x):
    if root is None:
        return root

    if root.data > x:
        root.left = delNode(root.left, x)
    elif root.data > x:
        root.right = delNode(root.right, x)
    else:
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        successor = getSuccessor(root)
        root.data = successor.data
        root.right = delNode(root.right, successor.data)

    return root
