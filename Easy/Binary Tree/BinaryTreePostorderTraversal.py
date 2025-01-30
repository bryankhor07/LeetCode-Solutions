# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """
        Performs a postorder traversal (Left, Right, Root) of a binary tree iteratively.

        Args:
        root (Optional[TreeNode]): The root node of the binary tree.

        Returns:
        List[int]: A list of node values in postorder sequence.
        """
        if not root:
            return []  # If the tree is empty, return an empty list
        
        stack = [root]  # Use a stack to manage nodes to visit
        res = []  # List to store the traversal result

        while stack:
            node = stack.pop()  # Retrieve the last inserted node
            if node is not None:
                res.append(node.val)  # Append the node's value to the result list
                # Push left child first so that right child is processed first
                stack.append(node.left)
                stack.append(node.right)
                
        return res[::-1]  # Reverse the result to achieve postorder (Left, Right, Root)