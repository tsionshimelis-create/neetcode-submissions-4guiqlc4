# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        if not root:
            return True
        queue = deque()
        queue.append([root, float('-inf'), float('inf')])

        while queue:
            node, leftBound, rightBound = queue.popleft()

            if node.val <= leftBound or node.val >= rightBound:
                return False
            
            if node.left:
                queue.append([node.left, leftBound, node.val])
            if node.right:
                queue.append([node.right, node.val, rightBound])

        return True




