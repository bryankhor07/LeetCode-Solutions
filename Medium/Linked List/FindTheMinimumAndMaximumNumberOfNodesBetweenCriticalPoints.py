# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        maxDistance = float("-inf")  # The maximum distance between critical points
        minDistance = float("inf")   # The minimum distance between critical points
        criticalPoints = []  # Store the index of the node that is a critical point
        i = 1  # Start the index at 1 (since we're checking local minima/maxima at index 1)
        prev = head
        curr = head.next
        next_node = head.next.next

        while next_node:
            # Check if the current node is a local maxima or minima
            if (prev.val < curr.val and curr.val > next_node.val) or (prev.val > curr.val and curr.val < next_node.val):
                criticalPoints.append(i)
                if len(criticalPoints) > 1:
                    # Update the minimum distance when we find a new critical point
                    minDistance = min(minDistance, criticalPoints[-1] - criticalPoints[-2])
            
            # Move to the next node
            prev = prev.next
            curr = curr.next
            next_node = next_node.next
            i += 1
        
        # If there are less than 2 critical points, return [-1, -1]
        if len(criticalPoints) < 2:
            return [-1, -1]
        
        # Calculate the maximum distance between the first and last critical points
        maxDistance = criticalPoints[-1] - criticalPoints[0]

        return [minDistance, maxDistance]
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once to find the critical points.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.