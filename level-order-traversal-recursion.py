class Node:
    def __init__(self, value):
        self.data = value
        self.left = None
        self.right = None


def level_order_rec(root, level, res):
    if root is None:
        return

    if len(res) <= level:
        res.append([])
    res[level].append(root.data)

    level_order_rec(root.left, level + 1, res)
    level_order_rec(root.right, level + 1, res)


def levelOrder(root):
    res = []
    level_order_rec(root, 0, res)
    return res
