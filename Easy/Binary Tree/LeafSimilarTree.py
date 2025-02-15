# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        # Initialize stacks for iterative DFS traversal of both trees
        stack = [root1]
        stack2 = [root2]

        # Lists to store leaf sequences of both trees
        seq1 = []
        seq2 = []

        # Traverse the first tree
        while stack:
            node = stack.pop()
            if not node:
                continue
            if node:
                # Add right child to stack 
                stack.append(node.right)
                # Add left child to stack
                stack.append(node.left)
            # If it's a leaf node, add its value to seq1
            if not node.right and not node.left:
                seq1.append(node.val)

        # Traverse the second tree
        while stack2:
            node = stack2.pop()
            if not node:
                continue
            if node:
                # Add right child to stack 
                stack2.append(node.right)
                # Add left child to stack
                stack2.append(node.left)
            # If it's a leaf node, add its value to seq2
            if not node.right and not node.left:
                seq2.append(node.val)

        return seq1 == seq2
    
# Time complexity: O(n)
# Space complexity: O(n)