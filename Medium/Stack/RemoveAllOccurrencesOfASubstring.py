def removeOccurrences(self, s: str, part: str) -> str:
    stack = [] # Stack to store characters
    part_len = len(part)

    # Iterate through the string to remove the occurrences of the substring `part`
    for char in s:
        stack.append(char)
        # Check the last part of the stack directly
        if len(stack) >= part_len and "".join(stack[-part_len:]) == part:
            del stack[-part_len:]  # Remove `part` from the stack

    return "".join(stack)

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the stack used to store the characters of the input string `s`.