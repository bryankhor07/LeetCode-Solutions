def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
    stack = [] # Stack to store the pushed elements
    j = 0 # Index to iterate through the popped list

    # Iterate through the pushed list
    for i in range(len(pushed)):
        # Append the current element to the stack
        stack.append(pushed[i])
        # Check if the top element of the stack is equal to the current element in the popped list
        # If it is, pop the element from the stack and increment the index for the popped list
        # Continue until the top element of the stack is not equal to the current element in the popped list
        while stack:
            if stack[-1] == popped[j]:
                stack.pop()
                j += 1
            else:
                break
    # If the stack is empty, return True, else return False
    if stack:
        return False
    return True

# Time Complexity: O(n), where n is the length of the input lists `pushed` and `popped`.
# We iterate through both lists once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the elements from the `pushed` list.