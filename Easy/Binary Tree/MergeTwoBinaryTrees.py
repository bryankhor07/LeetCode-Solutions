# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # If one of the roots is None, return the other root
        if not root1:
            return root2
        if not root2:
            return root1
        # Create two stacks to store the nodes of the two trees
        stack1 = [root1]
        stack2 = [root2]

        # While there are nodes in both stacks
        while stack1 and stack2:
            node1 = stack1.pop()
            node2 = stack2.pop()
            # If one of the nodes is None, continue to the next iteration
            if not node1 or not node2:
                continue
            # Add the values of the nodes
            node1.val += node2.val
            # If the right child of the first tree is None, set it to the right child of the second tree
            # Otherwise, add the right children to the stacks
            if not node1.right:
                node1.right = node2.right
            else:
                stack1.append(node1.right)
                stack2.append(node2.right)
            
            # If the left child of the first tree is None, set it to the left child of the second tree
            # Otherwise, add the left children to the stacks
            if not node1.left:
                node1.left = node2.left
            else:
                stack1.append(node1.left)
                stack2.append(node2.left)
            
        return root1
    
# Time complexity: O(n)
# Space complexity: O(n)