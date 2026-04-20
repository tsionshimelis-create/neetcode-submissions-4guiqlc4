# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(root, minVal, maxVal):
            if not root:
                return True

            if minVal >= root.val or root.val >= maxVal:
                return False
            
            return (validate(root.left, minVal, root.val) and 
            validate(root.right, root.val, maxVal))
            
        return validate(root, float('-inf'), float('inf'))




