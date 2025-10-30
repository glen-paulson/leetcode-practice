def rightRotation(node):
    if node is None or node.left is None:
        return node

    new_root = node.left
    temp_subTree = new_root.right
    new_root.right = node
    node.left = temp_subTree

    return new_root


def leftRotation(node):
    if node is None or node.right is None:
        return node

    new_root = node.right
    temp_subTree = new_root.left
    new_root.left = node
    node.right = temp_subTree

    return new_root
