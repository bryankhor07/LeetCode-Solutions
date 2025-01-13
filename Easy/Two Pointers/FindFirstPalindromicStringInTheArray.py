def firstPalindrome(self, words: List[str]) -> str:
    for i in range(len(words)):
        if self.isPalindrome(words[i]):
            return words[i]
    return ""

def isPalindrome(self, s):
    l = 0
    r = len(s) - 1

    while l <= r:
        if s[l] != s[r]:
            return False
        l += 1
        r -= 1
    return True

# Time Complexity: O(n * m), where n is the number of words in the list words and m is the average length of the words.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l and r.