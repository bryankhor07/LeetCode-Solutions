def repeatedCharacter(self, s: str) -> str:
    # Use a hashmap to get the frequency of each letter
    hashmap = {}
    
    # Store the frequency of each letter in hashmap and return the first letter to appear twice
    for i in range(len(s)):
        hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
        if hashmap[s[i]] == 2:
            return s[i]
        
# Time Complexity: O(n) where n is the length of the input string
# Space Complexity: O(1) since the hashmap contains at most 26 characters