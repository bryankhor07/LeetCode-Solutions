# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # Helper function to perform depth-first search
        def dfs(root):
            # Base case: If the node is None, it's balanced with height 0
            if not root:
                return [True, 0]

            # Recursively check the left and right subtrees
            left = dfs(root.left)
            right = dfs(root.right)

            # A tree is balanced if:
            # 1. The left subtree is balanced
            # 2. The right subtree is balanced
            # 3. The height difference between the left and right subtree is no more than 1
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1)

            # The height of the current tree is the maximum height of its subtrees plus 1
            return [balanced, 1 + max(left[1], right[1])]
        
        # Start the DFS from the root and check if the whole tree is balanced
        return dfs(root)[0]
    
# Time complexity: O(N)
# Space complexity: O(H), where H is the height of the binary tree. In the worst case, the recursion stack can go as deep as the height of the tree.