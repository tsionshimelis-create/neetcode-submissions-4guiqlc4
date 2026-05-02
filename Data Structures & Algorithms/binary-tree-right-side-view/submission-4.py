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

        rightSide = []
        queue = deque()
        queue.append(root)

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                level.append(node.val)
                for neigh in [node.left, node.right]:
                    if neigh:
                        queue.append(neigh)
            if level:
                rightSide.append(level[-1])   

        return rightSide
            