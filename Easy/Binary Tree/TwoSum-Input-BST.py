# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        stack = [root]
        nodeValues = []

        # Perform iterative traversal of the tree
        while stack:
            node = stack.pop()
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            nodeValues.append(node.val)

        hashmap = {} # val : index

        # i is the index, n is the value
        for i, n in enumerate(nodeValues):
            remainder = k - n # remainder is the value needed to reach k
            if remainder in hashmap: # if the remainder is in the hashmap, return True
                return True
            hashmap[n] = i # store the value and its index in the hashmap
        return False
    
# Time Complexity: O(N)
# Space Complexity: O(N) due to the stack used for iterative traversal and the hashmap used to store node values