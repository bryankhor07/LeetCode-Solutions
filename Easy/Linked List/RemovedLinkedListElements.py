# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(-1, head)
        curr = dummy

        # Traverse through the linked list and set the pointer of the current node
        # to the next next node if the next node is equal to val
        while curr and curr.next:
            nxtNode = curr.next
            if nxtNode.val == val:
                curr.next = nxtNode.next
            else:
                curr = curr.next
        return dummy.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.