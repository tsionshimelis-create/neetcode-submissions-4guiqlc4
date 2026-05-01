# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        queue = deque()
        queue.append(root)
# queue = []  
# p = 1, q = 2
# 3 < 5 < 4
        while queue:
            node = queue.popleft()
            if node.val == p.val or node.val == q.val:
                return node
            if p.val < node.val < q.val or q.val < node.val < p.val:
                return node

            for neigh in [node.left, node.right]:
                if neigh:
                    queue.append(neigh)
