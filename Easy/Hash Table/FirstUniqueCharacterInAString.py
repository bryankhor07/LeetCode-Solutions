def firstUniqChar(self, s: str) -> int:
    # Create a dictionary to store the frequency of each character in the string
    hashmap = {}

    # First pass: Count the occurrences of each character
    for i in range(len(s)):
        hashmap[s[i]] = 1 + hashmap.get(s[i], 0)

    # Second pass: Find the first character with a frequency of 1
    for i in range(len(s)):
        if hashmap[s[i]] == 1:
            return i  # Return the index of the first unique character

    # If no unique character is found, return -1
    return -1

# Time complexity: O(n)
# Space complexity: O(n) where n is the length of the input string