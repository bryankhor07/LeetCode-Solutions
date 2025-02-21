# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Initialize a list with one element to store the maximum diameter found
        res = [0]

        def dfs(root):
            # Base case: if the current node is null, return -1
            if not root:
                return -1
            
            # Recursively calculate the depth of the left subtree
            left = dfs(root.left)
            # Recursively calculate the depth of the right subtree
            right = dfs(root.right)
            
            # Calculate the diameter at the current node
            # Diameter is the number of nodes on the longest path between two leaves in the tree
            # This is calculated as 2 + left + right (path through the current node)
            res[0] = max(res[0], 2 + left + right)

            # Return the depth of the tree rooted at the current node
            # Depth is 1 + max depth of either subtree (left or right)
            return 1 + max(left, right)

        # Call the dfs function starting from the root
        dfs(root)
        # The result is stored in res[0], which is the maximum diameter found
        return res[0]
    
# Time Complexity: O(N)
# Space Complexity : O(N) due to the recursive calls on the stack. The space complexity can be reduced to O(1) by using an iterative approach.