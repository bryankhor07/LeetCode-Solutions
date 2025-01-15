def makeGood(self, s: str) -> str:
    stack = [] # Stack to store characters

    # Iterate through the string to remove adjacent duplicates
    for i in range(len(s)):
        # If the stack is not empty and the current character is the same as the top of the stack but in different cases, pop the top element
        if stack:
            if ord(s[i]) + 32 == ord(stack[-1]):
                stack.pop()
            elif ord(s[i]) - 32 == ord(stack[-1]):
                stack.pop()
            else:
                stack.append(s[i])
        # Otherwise, add the current character to the stack
        else:
            stack.append(s[i])
    return "".join(stack)

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the characters of the input string `s`.