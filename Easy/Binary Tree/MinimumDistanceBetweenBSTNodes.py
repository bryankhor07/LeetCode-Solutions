# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        # This list will hold the values of nodes in inorder traversal order
        res = [] 

        # Helper function to perform inorder traversal
        def inorder(root):
            if not root:
                return 0
            inorder(root.left)
            res.append(root.val)
            inorder(root.right)

        # Perform the inorder traversal starting from the root
        inorder(root)
        # Initialize the minimum difference to a very large number
        min_diff = float('inf')

        # Iterate through the sorted values to find the minimum difference
        for i in range(1, len(res)):
            # Compare the current difference with the previous minimum difference
            min_diff = min(min_diff, res[i] - res[i - 1])
        return min_diff
    
# Time Complexity: O(N)
# Space Complexity: O(N) due to the list used to store node values