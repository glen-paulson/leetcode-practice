class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def insert(root, key):
        tempNode = Node(key)

        curr = root
        while curr is not None:
            if curr.data > key and curr.right is not None:
                curr = curr.right
            elif curr.data < key and curr.left is not None:
                curr = curr.left
            else:
                break

        if curr.data > key:
            curr.left = tempNode
        else:
            curr.right = tempNode

        return root
