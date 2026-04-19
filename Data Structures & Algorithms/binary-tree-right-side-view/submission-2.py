# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        res = []
        q = collections.deque()
        q.append(root)

        while q:
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                rightSide = node
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)

            res.append(rightSide.val)

        return res
