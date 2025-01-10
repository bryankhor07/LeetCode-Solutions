def findTheDifference(self, s: str, t: str) -> str:
    # Dictionaries to store the frequency of each character in s and t
    hashmapS = {}
    hashmapT = {}

    # Count the frequency of each character in string s
    for i in range(len(s)):
        hashmapS[s[i]] = 1 + hashmapS.get(s[i], 0)

    # Count the frequency of each character in string t
    for i in range(len(t)):
        hashmapT[t[i]] = 1 + hashmapT.get(t[i], 0)

    # Compare the frequencies in hashmapT with those in hashmapS
    for key, val in hashmapT.items():
        # If a character in t is not present in s, return it
        if key not in hashmapS:
            return key
        # If the frequency of a character in t is greater than in s, return it
        elif key in hashmapS and val != hashmapS[key]:
            return key
        
# Time complexity: O(n)
# Space complexity: O(n) where n is the length of the longer string