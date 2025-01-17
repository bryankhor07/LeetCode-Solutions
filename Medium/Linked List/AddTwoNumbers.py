# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        str1 = str2 = ""

        dummy = ListNode()
        current = dummy  # Create a separate pointer to traverse the list

        currl1 = l1
        currl2 = l2

        while currl1:
            str1 += str(currl1.val)
            currl1 = currl1.next

        while currl2:
            str2 += str(currl2.val)
            currl2 = currl2.next

        str1 = self.reverseStr(str1)
        str2 = self.reverseStr(str2)
        sum = int(str1) + int(str2)

        if sum == 0:  # Handle the case when both numbers are zero
            return ListNode(0)

        while sum > 0:
            current.next = ListNode(sum % 10)
            current = current.next
            sum = sum // 10
        return dummy.next

    def reverseStr(self, s):
        res = ""
        for i in range(len(s) - 1, -1, -1):
            res += s[i]
        return res
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.