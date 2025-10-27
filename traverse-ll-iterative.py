class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def traverseLl(head):
    while head is not None:
        print(head.data, end="")
        if head.next is not None:
            print("->", end="")
        head = head.next
