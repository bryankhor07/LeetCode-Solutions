def longestPalindrome(self, s: str) -> str:
    if len(s) <= 1:
        return s  # A single character or empty string is always a palindrome

    def expandAroundCenter(left: int, right: int) -> str:
        # Expand around the center as long as it's a palindrome
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]  # Return the valid palindrome substring

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome (single character center)
        odd_palindrome = expandAroundCenter(i, i)
        # Even-length palindrome (two-character center)
        even_palindrome = expandAroundCenter(i, i + 1)

        # Update the longest palindrome if a longer one is found
        longest = max(longest, odd_palindrome, even_palindrome, key=len)

    return longest

# Time Complexity: O(n^2), where n is the length of the input string s. The expandAroundCenter function is called for each character in the string, and each call takes O(n) time in the worst case.
# Space Complexity: O(1). The space complexity is constant because we only use a few variables to store the indices of the palindrome substring.