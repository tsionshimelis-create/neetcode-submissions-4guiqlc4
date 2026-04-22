# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        self.string = []
        def dfs(root):
            if not root:
                self.string.append("N")
                self.string.append(":")
                return
            self.string.append(str(root.val))
            self.string.append(":")
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return "".join(self.string)
        
        
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = data.split(':')
        self.i = 0
        def dfs():
            if self.i > len(val) or val[self.i] == "N":
                self.i += 1
                return 

            root = TreeNode(val[self.i])
            self.i += 1

            root.left = dfs()
            root.right = dfs()

            return root
        return dfs()
