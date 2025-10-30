class Node:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.key)


def createListFromTree(root, listNodes):
    if root is None:
        return

    createListFromTree(root.left, listNodes)
    listNodes.append(root.key)
    createListFromTree(root.right, listNodes)


def buildBSTRecursive(listNodes, start, end):
    if start > end:
        return None

    mid = (start+end) // 2
    node = Node(listNodes[mid])
    node.left = buildBSTRecursive(listNodes, start, mid-1)
    node.right = buildBSTRecursive(listNodes, mid + 1, end)

    return node


def buildBST(root):
    listNodes = []
    createListFromTree(root, listNodes)
    listNodes.sort()
    n = len(listNodes)
    if n == 0:
        return None

    return buildBSTRecursive(listNodes, 0, n-1)
