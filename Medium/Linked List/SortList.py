# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        dummy = ListNode(0)
        d = dummy

        # Traverse the linked list and add the values to arr
        while curr:
            arr.append(curr.val)
            curr = curr.next
        
        # Sort the arr
        arr.sort()

        # Add the sorted values to a new linked list
        for i in range(len(arr)):
            d.next = ListNode(arr[i])
            d = d.next
        return dummy.next
    
# Time Complexity: O(nlogn), where n is the number of nodes in the linked list.
# We traverse the linked list once to create the array, which takes O(n) time.
# Sorting the array takes O(nlogn) time.
# Creating the new linked list takes O(n) time.
# Thus, the overall time complexity is O(nlogn).
# Space Complexity: O(n). We store the values of the linked list in an array, which takes O(n) space.