def isPrefixString(self, s: str, words: List[str]) -> bool:
    temp = ""
    for word in words:
        temp += word
        # Early termination if temp exceeds s
        if len(temp) > len(s):
            return False
        if temp == s:
            return True
    return False

# Time Complexity: O(n * m), where n is the number of words in the list words and m is the average length of the words.
# Space Complexity: O(m), where m is the length of the input string s. The space complexity is due to the creation of the temp string.