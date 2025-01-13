def reverseVowels(self, s: str) -> str:
    res = list(s)
    l, r = 0, len(s) - 1
    vowels = set('aeiouAEIOU')

    # Swap vowels from the start and end of the string
    while l < r:
        # If both characters at l and r are vowels, swap them
        if res[l] in vowels and res[r] in vowels:
            temp = res[l]
            res[l] = res[r]
            res[r] = temp
            l += 1
            r -= 1
        # If character at l is not a vowel, move l to the right
        elif res[l] in vowels and res[r] not in vowels:
            r -= 1
        # If character at r is not a vowel, move r to the left
        elif res[l] not in vowels and res[r] in vowels:
            l += 1
        else:
            l += 1
            r -= 1
    return ''.join(res)

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n). The space complexity is due to the list res