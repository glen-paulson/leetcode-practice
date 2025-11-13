# class Node:
#     def __init__(self, data):
#     self.data = data
#     self.children = []

def dfs(root):
    if root is None:
        return
    stack = []
    stack.append(root)

    while len(stack) > 0:
        print(stack[-1].data)
        cur_node = stack.pop(-1)

        for item in cur_node.children:
            stack.append(item)
