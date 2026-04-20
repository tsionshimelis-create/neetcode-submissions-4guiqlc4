# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        order = []
        self.k = k
        def dfs(root):
            nonlocal order
            if not root:
                return
            if self.k == 0:
                return 

            dfs(root.left)
            order.append(root.val)
            self.k -= 1
            dfs(root.right)
        dfs(root)
        return order[self.k - 1]