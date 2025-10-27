class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseLl(head):
    if head is None:
        print()
        return

    print(head.data, end="")

    if head.next is not None:
        print("->", end="")

    traverseLl(head.next)
