def longestPalindrome(self, s: str) -> int:
    # Initialize a hashmap to store the frequency of each character
    hashmap = {}
    # Variable to track the length of the longest palindrome
    length = 0

    # Iterate through the string to populate the hashmap with character counts
    for i in range(len(s)):
        # Update the count of the current character
        hashmap[s[i]] = 1 + hashmap.get(s[i], 0)
        # If the character's count is even, it can contribute to a symmetric palindrome
        if hashmap[s[i]] % 2 == 0:
            length += 2

    # Check if there is any character with an odd count
    # We can use one odd-count character as the center of the palindrome
    for value in hashmap.values():
        if value % 2 != 0:
            length += 1
            break  # We only need one odd-count character

    # Return the calculated length of the longest palindrome
    return length

# Time complexity: O(n)
# Space complexity: O(n) where n is the length of the input string s