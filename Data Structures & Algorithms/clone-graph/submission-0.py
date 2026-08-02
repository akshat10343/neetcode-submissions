"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if node is None:
            return None

        d = {}

        def dfs(node):
            if node in d:
                return
            d[node] = Node(node.val)
            for nb in node.neighbors:  # or graph[node]
                dfs(nb)
        dfs(node)
        head = d[node]
        for orig, copy in d.items():
            for nb in orig.neighbors:
                copy.neighbors.append(d[nb])
        return head

