# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        arr = []
        res = [None] * k  # Initialize a result list of length k with None values
        curr = head

        # Convert the linked list to a Python list of values (arr)
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # Determine the number of elements in each part
        if len(arr) < k:
            for i in range(len(arr)):
                res[i] = ListNode(arr[i])  # Create a ListNode from arr[i]
        else:
            extraOnes = len(arr) % k
            size = len(arr) // k
            z = 0
            for i in range(k):
                if z < len(arr):
                    res[i] = ListNode(arr[z])
                    temp = res[i]
                    z += 1
                    for j in range(size - 1):  # Link remaining nodes for this part
                        temp.next = ListNode(arr[z])
                        temp = temp.next
                        z += 1
                    if extraOnes > 0:  # Distribute extra elements
                        temp.next = ListNode(arr[z])
                        temp = temp.next
                        z += 1
                        extraOnes -= 1
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once to convert it to a Python list.
# Space Complexity: O(n). We store the values of the linked list in an array. The space complexity of the result list is O(k).