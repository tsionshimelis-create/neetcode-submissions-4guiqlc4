# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder, inorder):
        # map value -> index in inorder
        self.idx_map = {val:i for i, val in enumerate(inorder)}
        self.idx = 0
        def build(l, r):
            
            if l > r:
                return 

            root = TreeNode(preorder[self.idx])
            self.idx += 1
            mid = self.idx_map[root.val]

            root.left = build(l, mid - 1)
            root.right = build(mid + 1, r)

            return root


        
        return build(0, len(preorder) - 1)




