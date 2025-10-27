class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def search(root, key):
        present = False

        while root is not None:
            if root.data == key:
                present = True
                break
            elif key > root.data:
                root = root.right
            else:
                root = root.left

        return present
