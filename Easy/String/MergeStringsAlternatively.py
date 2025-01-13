def mergeAlternately(self, word1: str, word2: str) -> str:
    n1 = len(word1)
    n2 = len(word2)
    res = ""

    i = 0
    
    # Merge the strings alternatively until one of the strings is exhausted
    while i < n1 and i < n2:
        res += word1[i] + word2[i]
        i += 1
    
    # Append the remaining characters from the longer string
    if i < n1:
        res += word1[i:]
    elif i < n2:
        res += word2[i:]
    return res

# Time Complexity: O(n), where n is the length of the longer of the two input strings word1 and word2.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers i and the result string res.