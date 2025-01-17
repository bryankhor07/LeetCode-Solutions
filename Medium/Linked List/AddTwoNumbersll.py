# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize pointers for traversing the lists
        curr1 = l1
        curr2 = l2
        dummy = ListNode(0)  # Dummy node to build the result list
        str1 = ""
        str2 = ""

        # Collect numbers from the first linked list
        while curr1:
            str1 += str(curr1.val)
            curr1 = curr1.next

        # Collect numbers from the second linked list
        while curr2:
            str2 += str(curr2.val)
            curr2 = curr2.next

        # Convert collected strings to integers and compute the sum
        total_sum = int(str1) + int(str2)
        
        # If the sum is 0, return a single node with value 0
        if total_sum == 0:
            return ListNode(0)

        # Create the resulting linked list from the digits of total_sum
        new_curr = dummy
        for digit in str(total_sum):
            new_curr.next = ListNode(int(digit))
            new_curr = new_curr.next

        return dummy.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.