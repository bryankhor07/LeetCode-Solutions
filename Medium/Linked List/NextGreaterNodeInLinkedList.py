class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
    values = []
    while head:
        values.append(head.val)
        head = head.next
    
    answer = [0] * len(values)
    stack = []
    
    for i, value in enumerate(values):
        while stack and values[stack[-1]] < value:
            smaller = stack.pop()
            answer[smaller] = value
        stack.append(i)
    
    return answer

# Time Complexity: O(n), where n is the number of nodes in the linked list.
# We iterate through the linked list once to retrieve the values and once to find the next greater node.
# Space Complexity: O(n). We use a stack to store the indices of the nodes, which can have at most n elements.