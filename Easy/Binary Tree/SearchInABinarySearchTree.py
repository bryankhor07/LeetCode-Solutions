# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        stack = [] # Initialize a stack to store nodes
        stack.append(root) # Add the root node to the stack

        # While the stack is not empty
        while len(stack) > 0:
            # Pop the top node from the stack
            node = stack.pop()
            # If the node is not None 
            # Add the right and left children to the stack
            if node is not None:
                stack.append(node.right)
                stack.append(node.left)
                # If the value of the node is equal to the target value, return the node
                if node.val == val:
                    return node
        return None
    
# Time complexity: O(n)
# Space complexity: O(n)