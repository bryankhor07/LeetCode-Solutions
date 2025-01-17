def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    prev, curr = None, head 

    # Traverse through the linked list and reverse the pointers
    while curr:
        nxtNode = curr.next # Store the next node in a variable
        curr.next = prev # Reverse the pointer
        prev = curr # Move the previous node to the current node
        curr = nxtNode # Move to the next node
    return prev

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.