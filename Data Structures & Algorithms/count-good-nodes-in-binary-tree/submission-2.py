# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        q = deque()
        q.append([root, root.val])
        self.count = 0

        while q:
            node, maxVal = q.popleft()

            if node.val >= maxVal:
                self.count += 1
                maxVal = node.val
            
            for child in [node.left, node.right]:
                if child:
                    q.append([child, maxVal])
        return self.count

        
        

            