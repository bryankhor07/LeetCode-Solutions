# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs an inorder traversal (Left, Root, Right) of a binary tree.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: A list of node values in inorder sequence.
        """
        res = []  # List to store the inorder traversal result
        
        def inorder(root):
            """Recursive helper function to perform inorder traversal."""
            if not root:  # Base case: If the node is None, return
                return
            inorder(root.left)  # Traverse the left subtree
            res.append(root.val)  # Visit the root node
            inorder(root.right)  # Traverse the right subtree
        
        inorder(root)  # Start the traversal from the root node
        return res  # Return the final inorder traversal list
    
# Time complexity: O(N), where N is the number of nodes in the binary tree.
# Space complexity: O(H), where H is the height of the binary tree. In the worst case, the recursion stack can go as deep as the height of the tree.