"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return

        prev_copy = {node: Node(node.val)}
        queue = deque([node])
       
        while queue:
            curr = queue.popleft()

            for neigh in curr.neighbors:
                if neigh not in prev_copy:
                    prev_copy[neigh] = Node(neigh.val)
                    queue.append(neigh)
                prev_copy[curr].neighbors.append(prev_copy[neigh])
        return prev_copy[node]

