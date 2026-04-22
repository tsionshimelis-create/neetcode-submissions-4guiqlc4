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
        print(data)
        def dfs(i):
            if i >= len(data) or data[i] == "N":
                return
            root = TreeNode(data[i])
            root.left = TreeNode(data[i + 2])
            root.right = TreeNode(data[i + 3])

            dfs(i + 2)
        dfs(0)
        return root
