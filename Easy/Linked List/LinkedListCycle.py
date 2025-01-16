# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hashmap = {}
        curr = head

        while curr:
           # Check if the current node is already in the hashmap
            if curr in hashmap:
                return True
            
            # Store the current node in the hashmap
            hashmap[curr] = 1
            curr = curr.next
        return False

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once.
# Space Complexity: O(n). The space complexity is linear as we store the nodes in the hashmap.

        # Floyd's Tortoise and Hare algorithm
        # slow, fast, = head, head

        # while fast and fast.next:
        #    slow = slow.next
        #    fast = fast.next.next
        #    if slow == fast:
        #        return True
        # return False
