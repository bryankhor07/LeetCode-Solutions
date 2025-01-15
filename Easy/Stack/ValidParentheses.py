def isValid(self, s: str) -> bool:
    stack = [] # Initialize a stack to store the opening brackets.

    # Iterate through the input string.
    for char in s:
        # If the character is an opening bracket, push it onto the stack.
        if char == '(' or char == '{' or char == '[':
            stack.append(char)
        # If the character is a closing bracket, check if it matches the top of the stack.
        # If it does, pop the top element from the stack.
        # If it doesn't, return False as the brackets are not valid.
        else:
            if not stack:
                return False
            if char == ')' and stack[-1] == '(':
                stack.pop()
            elif char == '}' and stack[-1] == '{':
                stack.pop()
            elif char == ']' and stack[-1] == '[':
                stack.pop()
            else:
                return False
    return not stack

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the opening brackets.