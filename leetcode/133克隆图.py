'''





"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""

# BFS
class Solution:

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        queue = [node]
        visited = {node: Node(node.val)}

        while queue:
            vertex = queue.pop(0)

            for w in vertex.neighbors:
                if w not in visited:
                    queue.append(w)
                    visited[w] = Node(w.val)
                visited[vertex].neighbors.append(visited[w])

        return visited[node]

# DFS
class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        self.visited[node] = Node(node.val)

        for w in node.neighbors:
            if w not in self.visited:
                self.visited[w] = self.cloneGraph(w)

            self.visited[node].neighbors.append(self.visited[w])

        return self.visited[node]


# 标准DFS
class Solution:

    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return None

        if node in self.visited:
            return self.visited[node]

        clone_node = Node(node.val)
        self.visited[node] = clone_node

        for w in node.neighbors:
            clone_node.neighbors.append(self.cloneGraph(w))

        return clone_node
'''