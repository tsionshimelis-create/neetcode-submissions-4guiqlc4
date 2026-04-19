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

        q = deque()
        q.append(root)

        res = []

        while q:
            new_level = []
            n = len(q)
            for _ in range(n):
                node = q.popleft()
                new_level.append(node.val)
                for child in [node.left, node.right]:
                    if child != None:
                        q.append(child)
            res.append(new_level)

        return res

            
