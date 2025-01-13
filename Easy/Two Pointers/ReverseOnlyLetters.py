def reverseOnlyLetters(self, s: str) -> str:
    l, r = 0, len(s) - 1
    sList = list(s)

    # Swap letters from the start and end of the string
    while l < r:
        # If character at l is not a letter, move l to the right
        if not sList[l].isalpha():
            l += 1
        # If character at r is not a letter, move r to the left
        if not sList[r].isalpha():
            r -= 1
        # If both characters at l and r are letters, swap them
        if sList[l].isalpha() and sList[r].isalpha():
            temp = sList[l]
            sList[l] = sList[r]
            sList[r] = temp
            l += 1
            r -= 1
    return "".join(sList)

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n). The space complexity is due to the list sList.