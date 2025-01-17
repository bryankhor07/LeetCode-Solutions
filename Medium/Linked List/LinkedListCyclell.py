# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        hashmap = {} # Store the nodes in the linked list
        curr = head
        i = 0

        # Iterate through the linked list
        while curr:
            # Check if the current node is already in the hashmap
            # If it is, return the node
            if hashmap and curr in hashmap:
                return curr
            hashmap[curr] = i
            i += 1
            # Move to the next node
            curr = curr.next
        return None
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once.
# Space Complexity: O(n). The space complexity is linear as we store the nodes in the hashmap.