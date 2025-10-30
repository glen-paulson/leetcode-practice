def searchBST(root, key):
    if root is None:
        return None

    if root.key == key:
        return root
    elif root.key > key:
        return searchBST(root.left, key)
    elif root.key < key:
        return searchBST(root.right, key)
