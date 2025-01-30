# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a preorder traversal (Root, Left, Right) of a binary tree iteratively.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: A list of node values in preorder sequence.
        """
        if not root:
            return []  # If the tree is empty, return an empty list
        
        stack = [root]  # Use a stack to manage nodes to visit
        res = []  # List to store the preorder traversal result

        while stack:
            node = stack.pop()  # Retrieve the last inserted node
            if node is not None:
                res.append(node.val)  # Visit the root node
                # Push right child first so that left child is processed first
                stack.append(node.right)
                stack.append(node.left)

        return res  # Return the final preorder traversal list

# Time complexity: O(N), where N is the number of nodes in the binary tree.
# Space complexity: O(N), where N is the number of nodes in the binary tree. In the worst case, the stack can contain all the nodes of the tree.