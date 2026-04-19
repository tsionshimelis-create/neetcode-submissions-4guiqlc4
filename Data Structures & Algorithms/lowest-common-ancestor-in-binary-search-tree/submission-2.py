# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        self.common = 0
        def find(root):
            if not root:
                return 
            if q.val >= root.val and p.val <= root.val or p.val >= root.val and q.val <= root.val:
                self.common = root
                return
            if q.val < root.val and p.val < root.val:
                find(root.left)
            else:
                find(root.right)

        find(root)
        return self.common

