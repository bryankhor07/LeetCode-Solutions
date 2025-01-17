# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        ret = dummy

        while head and head.next:
            firstNode = head
            secondNode = head.next

            # swapping 2 nodes
            prev.next = secondNode
            nextTemp = secondNode.next
            secondNode.next = firstNode
            firstNode.next = nextTemp

            # update prev
            prev = firstNode

            # move pointer
            head = firstNode.next


        return ret.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# Space Complexity: O(1). The space complexity is constant as we use only a few pointers to store the nodes.