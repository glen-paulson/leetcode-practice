def height(root):
    if root is None:
        return -1

    left_ht = height(root.left)
    right_ht = height(root.right)

    if left_ht > right_ht:
        return 1 + left_ht
    else:
        return 1 + right_ht
