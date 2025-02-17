# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        stack = [(root, str(root.val))] # Initialize a stack with the root node and its value

        res = []

        # Perform DFS traversal of the tree
        while stack:
            node, path = stack.pop() # Pop the node and its path from the stack

            # If the node is None, continue to the next iteration
            if not node:
                continue
            
            # If the node is a leaf node, append the path to the result list
            if not node.left and not node.right: 
                res.append(path)

            # If the node has a left or right child, append the child node and its path to the stack
            if node.right:
                stack.append((node.right, path + "->" + str(node.right.val)))
            if node.left:
                stack.append((node.left, path + "->" + str(node.left.val)))

        return res