# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res = 0

        def diameter(root):
            nonlocal res
            if not root:
                return 0
            left = 1 + diameter(root.left)
            right = 1 + diameter(root.right)

            left_edge = left - 1
            right_edge = right - 1

            res = max(res, left_edge + right_edge)

            return max(left, right)
        diameter(root)
        return res