def maxDepth(self, s: str) -> int:
    stack = [] # Stack to store parentheses
    count = 0 # Maximum nesting depth of the parentheses

    # Iterate through the string to find the maximum nesting depth
    for i in range(len(s)):
        # If the current character is '(', push it onto the stack
        if s[i] == '(':
            stack.append('(')
        # If the current character is ')', pop the top element from the stack
        elif s[i] == ')':
            stack.pop()
        # Update the maximum nesting depth
        count = max(count, len(stack))
    return count

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the parentheses in the input string `s`.