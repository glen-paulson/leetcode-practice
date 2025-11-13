def bfs(root):
    if root is None:
        return
    queue = []
    queue.append(root)

    while len(queue) > 0:
        print(queue[0].data)
        cur_node = queue.pop(0)

        for item in cur_node.children:
            queue.append(item)
