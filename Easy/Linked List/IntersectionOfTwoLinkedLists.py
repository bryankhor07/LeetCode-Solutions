# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        currA = headA
        currB = headB

        listA = []
        listB = []

        while currA:
            listA.append(currA)
            currA = currA.next
        
        while currB:
            listB.append(currB)
            currB = currB.next

        lenA = len(listA)
        lenB = len(listB)

        indexA = lenA - 1
        indexB = lenB - 1

        # Find the first node from the end where they differ
        while indexA >= 0 and indexB >= 0 and listA[indexA] == listB[indexB]:
            indexA -= 1
            indexB -= 1

        # If there was an intersection, return the node right after the last common node
        if indexA != lenA - 1:
            return listA[indexA + 1]

        return None
    
# Time Complexity: O(m + n), where m is the number of nodes in the linked list A and n is the number of nodes in the linked list B.
# We iterate through both linked lists to find the intersection node.
# Space Complexity: O(m + n). We store the nodes of both linked lists in two separate lists. The space complexity is linear with respect to the number of nodes in the linked lists.