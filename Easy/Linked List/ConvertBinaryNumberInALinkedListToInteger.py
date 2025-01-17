# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        curr = head
        binary = ""
        res = 0

        # Retrieve the binary number from the linked list
        while curr:
            binary += str(curr.val)
            curr = curr.next

        multipleOfTwo = 1
        # Traverse the binary number and convert it to decimal
        for i in range(len(binary) - 1, -1, -1):
            res += (int(binary[i]) * multipleOfTwo)
            multipleOfTwo *= 2
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once to retrieve the binary number and once to convert it to decimal.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.