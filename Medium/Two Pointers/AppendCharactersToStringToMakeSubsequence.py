def appendCharacters(self, s: str, t: str) -> int:
    l = 0

    # If the character in s is equal to the character in t, increment the left pointer
    # If the left pointer reaches the end of t, return 0
    for r in range(len(s)):
        if l >= len(t):
            return 0
        if s[r] == t[l]:
            l += 1

    # If the left pointer is at the end of t, return the length of t
    if l == 0:
        return len(t)
    # Otherwise, return the difference between the length of t and the left pointer
    return len(t) - l

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the variable count.