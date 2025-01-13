def isSubsequence(self, s: str, t: str) -> bool:
    if len(t) < len(s):
        return False
    if len(s) == 0:
        return True

    index = 0

    # Check if the characters in s are present in t
    for i in range(len(t)):
        # Increment the index if the characters match
        if index < len(s):
            if s[index] == t[i]:
                index += 1
    # Return True if all characters in s are found in t
    return len(s) == index

# Time Complexity: O(n), where n is the length of the input string t.
# Space Complexity: O(1). The space complexity is due to the constant space used by the index variable.