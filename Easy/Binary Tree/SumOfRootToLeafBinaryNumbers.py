# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        # Initialize stack for preorder traversal with the root node and its value as a string
        stack = [(root, str(root.val))]
        # Variable to store the sum of root-to-leaf binary numbers
        total_sum = 0

        # Iterate until the stack is empty
        while stack:
            # Pop the current node and its accumulated string value
            node, val = stack.pop()

            # If the current node is a leaf, add its binary value to the total sum
            if not node.left and not node.right:
                total_sum += int(val, 2)

            # If the current node has a right child, add it to the stack with updated string value
            if node.right:
                stack.append((node.right, val + str(node.right.val)))
            # If the current node has a left child, add it to the stack with updated string value
            if node.left:
                stack.append((node.left, val + str(node.left.val)))

        # Return the total sum of all root-to-leaf binary numbers
        return total_sum
    
# Time complexity: O(N)
# Space complexity: O(H), where H is the height of the binary tree. In the worst case, the stack can go as deep as the height of