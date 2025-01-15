def minRemoveToMakeValid(self, s: str) -> str:
    s = list(s)
    stack = [] # Stack to store the indices of the parentheses

    # Iterate through the string to remove invalid parentheses
    for i, char in enumerate(s):
        # If an opening parenthesis is encountered, add its index to the stack
        if char == '(':
            stack.append(i)
        # If a closing parenthesis is encountered, remove the corresponding opening parenthesis
        elif char == ')':
            if stack:
                stack.pop()
            else:
                s[i] = ''
    # Remove any unmatched opening parentheses from the string
    while stack:
        s[stack.pop()] = ''
    return ''.join(s)

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the indices of the parentheses in the input string `s`.