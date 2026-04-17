# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # recursion 
        # may be dfs
        # find the right and left swap them

        # 1 
        # left  = invert(2)
        # left = 5
        # right = 4
#    1

# null 2

        def invert(root):
            if not root: 
                return None
            
            
            left = invert(root.left)
            right = invert(root.right)

            root.left, root.right = right, left
            

            return root

        return invert(root)

            