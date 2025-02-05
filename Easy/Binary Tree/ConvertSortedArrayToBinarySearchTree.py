# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        # Base case: if the list is empty, return None (no tree to build)
        if not nums:
            return None
        
        # Find the middle index of the list
        mid = len(nums) // 2
        
        # The middle element becomes the root of the BST
        root = TreeNode(nums[mid])
        
        # Recursively build the left subtree with the left half of the list
        root.left = self.sortedArrayToBST(nums[:mid])
        
        # Recursively build the right subtree with the right half of the list
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        # Return the root of the BST
        return root
    
# Time complexity: O(n)
# Space complexity: O(n)