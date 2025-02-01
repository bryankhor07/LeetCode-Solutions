# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        stack = [] # Create a stack to store the nodes of the tree

        # Inorder traversal of the tree
        def inorder(root):
            if not root:
                return
            inorder(root.left)
            stack.append(root.val)
            inorder(root.right)
        
        inorder(root)

        # Create a dummy node and a current node
        dummy = TreeNode()
        current = dummy
        # Create a new tree with the nodes in the stack
        for val in stack:
            current.right = TreeNode(val)
            current = current.right
        
        return dummy.right
    
# Time complexity: O(n)
# Space complexity: O(n)