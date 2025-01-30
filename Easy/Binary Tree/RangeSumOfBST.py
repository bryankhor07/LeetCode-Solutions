# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        res = [0] # Store the sum of nodes within the range
       
        # Helper function to perform DFS traversal
        def DFS(tree):
            if tree is not None:
                # If the current node value is within the range, add it to the sum
                if (tree.val >= low and tree.val <= high):
                    res[0] += tree.val
                # Traverse the left and right subtrees
                DFS(tree.left)
                DFS(tree.right)
        
        DFS(root)
        return res[0]