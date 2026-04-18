# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        self.Truth = True
        def same(p, q):
            if not q and not p:
                return
            if p and not q or q and not p:
                self.Truth = False
                return
            if p and q:
                if p.val != q.val:
                    self.Truth = False
                    return 
            same(p.left, q.left)
            same(p.right, q.right)

        

        same(p, q)
        return self.Truth
            
