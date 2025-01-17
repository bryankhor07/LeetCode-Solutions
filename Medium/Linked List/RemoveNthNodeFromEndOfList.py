# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
    dummy = ListNode(0, head)
    left = dummy
    right = head

    # Shift the right ptr n times
    while n > 0 and right:
        right = right.next
        n -= 1

    # Shift both left and right ptr until the right ptr reaches the end
    while right:
        left = left.next
        right = right.next
    
    # Remove the nth node from end of list
    left.next = left.next.next
    return dummy.next

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1). The space complexity is constant as we use only two pointers to traverse the linked list.