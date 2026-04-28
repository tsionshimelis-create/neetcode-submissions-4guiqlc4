"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        hash_map = {}
        visited = set()
        def dfs(start):
            if start in hash_map:
                return hash_map[start]
            if not start:
                return None

            cloned = Node(start.val)
            hash_map[start] = cloned
            for neigh in start.neighbors:
                cloned.neighbors.append(dfs(neigh))

            return cloned

        return dfs(node)