def isPalindrome(self, s: str) -> bool:
    # Initialize two pointers
    l = 0
    r = len(s) - 1

    while l <= r:
        # Skip non-alphanumeric characters on the left
        while l < r and not self.alphaNum(s[l]):
            l += 1
        # Skip non-alphanumeric characters on the right
        while r > l and not self.alphaNum(s[r]):
            r -= 1
        # Check if characters are equal (case insensitive)
        if s[l].lower() != s[r].lower():
            return False
        # Move pointers closer
        l += 1
        r -= 1
    return True

# Helper function to check if a character is alphanumeric
def alphaNum(self, s):
    return (ord('A') <= ord(s) <= ord('Z') or
            ord('a') <= ord(s) <= ord('z') or
            ord('0') <= ord(s) <= ord('9'))

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(1).