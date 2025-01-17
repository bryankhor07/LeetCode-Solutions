# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def reverseEvenLengthGroups(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = []
        curr = head
        res = ListNode(0)
        r = res

        # Convert the linked list into an array
        while curr:
            arr.append(curr.val)
            curr = curr.next

        i = 0
        group = 1

        while i < len(arr):
            # Determine the current group's size
            group_size = min(group, len(arr) - i)

            # Reverse the group if its size is even
            if group_size % 2 == 0:
                j, k = i, i + group_size - 1
                while j < k:
                    arr[j], arr[k] = arr[k], arr[j]
                    j += 1
                    k -= 1

            # Move to the next group
            i += group_size
            group += 1

        # Reconstruct the linked list from the modified array
        for val in arr:
            r.next = ListNode(val)
            r = r.next

        return res.next
    
# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once to convert it into an array.
# We then iterate through the array to reverse the even-length groups.
# Finally, we iterate through the array again to reconstruct the linked list.
# Thus, the overall time complexity is O(n).
# Space Complexity: O(n). We store the values of the linked list in an array, which takes O(n) space.