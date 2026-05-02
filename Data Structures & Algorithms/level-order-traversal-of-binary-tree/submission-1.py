# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        level = []

        while queue:
            n = len(queue)
            newLevel = []
            for i in range(n):
                node = queue.popleft()
                newLevel.append(node.val)
                for neigh in [node.left, node.right]:
                    if neigh:
                        queue.append(neigh)

            level.append(newLevel)

        return level