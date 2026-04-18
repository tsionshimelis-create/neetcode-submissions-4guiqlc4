# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        stack = []
        last = None
        node = root
        depth = defaultdict(int)

        while stack or node:
            if node:
                stack.append(node)
                node = node.left
            else:
                node = stack[-1]
                if node.right == None or last == node.right:
                    stack.pop()
                    left = depth[node.left]
                    right = depth[node.right]

                    if abs(left - right) > 1:
                        return False
                    depth[node] = 1 + max(left, right)
                    last = node
                    node = None
                else:
                    node = node.right
        return True


