# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        # Initialize queue for level-order traversal
        queue = [root]
        # List to store the average of each level
        res = []

        # Iterate until the queue is empty
        while queue:
            # Get the number of nodes at the current level
            qSize = len(queue)
            # Variable to accumulate the sum of values at the current level
            avgLevel = 0
            
            # Iterate over all nodes at the current level
            for i in range(qSize):
                # Pop the first node in the queue
                node = queue.pop(0)
                # If the left child exists, add it to the queue
                if node.left:
                    queue.append(node.left)
                # If the right child exists, add it to the queue
                if node.right:
                    queue.append(node.right)
                # Add the node's value to the level sum
                avgLevel += node.val
            
            # Calculate the average value for the current level
            avgLevel /= qSize
            # Append the average value to the result list
            res.append(avgLevel)

        # Return the list of averages for each level
        return res
    
# Time complexity: O(n)
# Space complexity: O(n)