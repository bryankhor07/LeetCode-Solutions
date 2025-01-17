def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
    slowPtr = head
    fastPtr = head

    while fastPtr and fastPtr.next:
        slowPtr = slowPtr.next
        fastPtr = fastPtr.next.next
        
    return slowPtr

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We traverse the linked list once.
# Space Complexity: O(1). The space complexity is constant as we use only two pointers to traverse the linked list.