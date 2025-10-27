# using inorder traversal

def inorder(root, sortedArr):
    if root is None:
        return

    inorder(root.left, sortedArr)

    sortedArr.append(root.data)

    inorder(root.right, sortedArr)


def minValue(root):
    if root is None:
        return
    sortedArr = []
    inorder(root, sortedArr)

    return sortedArr[0]
