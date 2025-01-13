def reversePrefix(self, word: str, ch: str) -> str:
    # Stack to store characters for reversing the prefix
    stack = []
    # Pointer to track the current position in the string
    i = 0

    # Traverse the string to find the prefix ending with the first occurrence of `ch`
    while i < len(word):
        stack.append(word[i])  # Add characters to the stack
        if word[i] == ch:  # Stop at the first occurrence of `ch`
            break
        i += 1

    # If `ch` is not found, return the original word
    if i == len(word):
        return word

    # Reverse the prefix by popping from the stack
    res = []
    for _ in range(len(stack)):
        res.append(stack.pop())

    # Join the reversed prefix with the remaining part of the word
    resString = "".join(res)
    return resString + word[i+1:]

# Time Complexity: O(n), where n is the length of the input string word.
# Space Complexity: O(n), where n is the length of the input string word. The space complexity is due to the stack used to store the characters of the prefix.