# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head # Initialize the current node to the head node.

        # Iterate through the linked list.
        while curr and curr.next:
            # If the current node's value is the same as the next node's value,
            # update the current node's next pointer to skip the next node.
            # Otherwise, move to the next node.
            nxtNode = curr.next
            if nxtNode.val == curr.val:
                curr.next = nxtNode.next
            else:
                curr = curr.next
        return head
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.