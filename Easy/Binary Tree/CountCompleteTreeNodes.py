# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res = [0] # Initialize a list to store the number of nodes

        # Helper function to perform DFS traversal of the tree
        def dfs(root):
            if not root: # Base case: if the node is None,
                return 0

            res[0] += 1 # Increment the number of nodes
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        return res[0]