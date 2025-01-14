def findLongestWord(self, s: str, dictionary: List[str]) -> str:
    # Sort the dictionary by length and then lexographical order
    dictionary.sort(key= lambda x: (-len(x),x))

    for d in dictionary:   
        count = 0
        i = j = 0
        while j < len(d) and i < len(s):
            # Start counting whenever a character matches 
            if s[i] == d[j]:
                j += 1
                count += 1
            i += 1
        # Return as soon as you find all the characters from dictionary word in s
        if count == len(d):
            return d
        
    return ''

# Time Complexity: O(n * m * log(m)), where n is the number of words in the dictionary and m is the length of the longest word in the dictionary. The sort operation takes O(n * log(n)) time, and for each word in the dictionary, we iterate through the characters of the input string s, which takes O(m) time.
# Space Complexity: O(n), where n is the number of words in the dictionary. The space complexity is due to the space used by the sorted dictionary.