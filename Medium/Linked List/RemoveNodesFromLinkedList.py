# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Reverse the linked list
        prev, curr = None, head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev now points to the head of the reversed list
        reversed_head = prev
        currMaxVal = float('-inf')

        # Step 2: Remove nodes
        dummy = ListNode(0, reversed_head)
        prev = dummy
        curr = reversed_head
        while curr:
            if curr.val >= currMaxVal:
                currMaxVal = curr.val
                prev = curr
            else:
                prev.next = curr.next
            curr = curr.next

        # Step 3: Reverse the list back to its original order
        prev, curr = None, dummy.next
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        # prev now points to the new head of the correctly modified list
        return prev
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.