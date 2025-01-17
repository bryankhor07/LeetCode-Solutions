import math

def isPalindrome(self, head: Optional[ListNode]) -> bool:
    stack = [] # Stack to store the values of the linked list
    curr = head # Pointer to traverse through the linked list

    # Push the values of the linked list into the stack
    while curr:
        stack.append(curr.val)
        curr = curr.next
    
    # Compare the values of the linked list with the values in the stack
    curr2 = head
    n = math.ceil(len(stack) / 2)
    for _ in range(n):
        # If the values are not equal, return False
        if curr2.val != stack.pop():
            return False
        # Move to the next node
        curr2 = curr2.next
    return True

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list twice, once to push the values into the stack and once to compare the values.
# Space Complexity: O(n). We store all the values of the linked list in the stack. The space complexity is linear.