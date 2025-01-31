# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        # If the root is a leaf node, return the value of the node
        if root.val <= 1:
            return root.val
        # If the root is an OR node, return the OR of the left and right children
        elif root.val == 2:
            return self.evaluateTree(root.left) or self.evaluateTree(root.right)
        # If the root is an AND node, return the AND of the left and right children
        else:
            return self.evaluateTree(root.left) and self.evaluateTree(root.right)
        
# Time complexity: O(n)
# Space complexity: O(1)