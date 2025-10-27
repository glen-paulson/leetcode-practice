class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def insertAtFront(head, data):
    newNode = Node(data)
    newNode.next = head
    return newNode


def insertAtEnd(head, data):
    newNode = Node(data)

    if head is None:
        return newNode

    lastPointer = head
    while lastPointer.next is not None:
        lastPointer = lastPointer.next

    lastPointer.next = newNode

    return head


def insertAtPos(head, data, pos):
    if pos < 1:
        return head

    if pos == 1:
        newNode = Node(data)
        newNode.next = head
        return newNode

    curr = head

    for i in range(1, pos-1):
        if curr is None:
            return head
        curr = curr.next

    if curr is None:
        return head

    newNode = Node(data)
    newNode.next = curr.next
    curr.next = newNode

    return head
