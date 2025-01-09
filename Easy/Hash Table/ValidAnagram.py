def isAnagram(self, s: str, t: str) -> bool:
    # Summary: Use a hashmap to store the count of occurrences of each 
    #          character in the two strings. Compare their counts and 
    #          return False if any of the counts differ.
    if (len(s) != len(t)):
        return False
    
    countS, countT = {}, {}

    for i in range(len(s)):
        countS[s[i]] = 1 + countS.get(s[i], 0)
        countT[t[i]] = 1 + countT.get(t[i], 0)

    for i in countS:
        if countS[i] != countT.get(i, 0):
            return False
    return True

# Time Complexity: O(n) where n is the length of the input strings
# Space Complexity: O(n) since we store the counts of characters in the strings