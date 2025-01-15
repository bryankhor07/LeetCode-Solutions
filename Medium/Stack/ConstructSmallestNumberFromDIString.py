def smallestNumber(self, pattern: str) -> str:
    stack = [] # Stack to store numbers
    ans = [] # List to store the final answer

    # Iterate through the pattern and push numbers to the stack
    for i in range(len(pattern) + 1):
        stack.append(i + 1)
        # If the current character is 'I' or the end of the pattern is reached, pop the numbers from the stack
        if i == len(pattern) or pattern[i] == 'I':
            while stack:
                ans.append(str(stack.pop()))

    return ''.join(ans)

# Time Complexity: O(n), where n is the length of the input string `pattern`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the numbers and the final answer