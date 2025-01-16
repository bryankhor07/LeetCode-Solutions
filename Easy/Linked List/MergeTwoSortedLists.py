def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0) # dummy node to start the merged list
    tail = dummy # tail node to keep track of the merged list

    # iterate through both linked lists
    while list1 and list2:
        # if the value of the first linked list is less than the value of the second linked list
        # add the first linked list node to the merged list
        if list1.val < list2.val:
            tail.next = list1
            list1 = list1.next # move to the next node in the first linked list
        # if the value of the second linked list is less than the value of the first linked list
        # add the second linked list node to the merged list
        elif list2.val < list1.val:
            tail.next = list2
            list2 = list2.next
        # if the values of the two linked lists are equal
        # add either one to the merged list
        else:
            tail.next = list1
            list1 = list1.next
        tail = tail.next
    # add the remaining nodes of the first linked list to the merged list
    # if there are any left
    # otherwise, add the remaining nodes of the second linked list
    if list1:
        tail.next = list1
    else:
        tail.next = list2

    return dummy.next

# Time Complexity: O(n + m), where n is the number of nodes in the first linked list and m is the number of nodes in the second linked list.
# We iterate through both linked lists once.
# Space Complexity: O(1). The space complexity is constant as we only use a few pointers to store the merged linked list.