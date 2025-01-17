def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
    arr = []
    curr = head
    res = ListNode(0)
    currRes = res

    # Retrieve the values of the linked list
    while curr:
        arr.append(curr.val)
        curr = curr.next
    
    # Swap the kth node from the beginning with the kth node from the end
    temp = arr[k - 1]
    arr[k - 1] = arr[-k]
    arr[-k] = temp

    # Create a new linked list with the swapped values
    for i in range(len(arr)):
        newNode = ListNode(arr[i])
        currRes.next = newNode
        currRes = currRes.next

    return res.next

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(n). We store the values of the linked list in an array.