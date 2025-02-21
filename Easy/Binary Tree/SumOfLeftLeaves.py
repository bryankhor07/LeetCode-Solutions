# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        # Stack to hold nodes and a marker for whether they are left or right children
        stack = [(root, "root")]
        sum = 0

        while stack:
            node, type = stack.pop()
            # Skip null nodes
            if not node:
                continue
            if node:
                # Add right child to stack and mark it as 'right'
                stack.append((node.right, "right"))
                # Add left child to stack and mark it as 'left'
                stack.append((node.left, "left"))
            # Check if it's a leaf node and if it's a left child
            if not node.right and not node.left and type == "left":
                sum += node.val
        return sum
    
# Time Complexity: O(N)
# Space Complexity: O(N) due to the stack used for iterative traversal