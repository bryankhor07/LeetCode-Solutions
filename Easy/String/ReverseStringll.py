def reverseStr(self, s: str, k: int) -> str:
    sList = list(s)  # Convert the string to a list for in-place modification
    n = len(s)       # Get the length of the string

    for i in range(0, n, 2 * k):  # Iterate over the string in chunks of 2 * k
        # Reverse the first k characters in the current chunk
        sList[i:i + k] = reversed(sList[i:i + k])
    
    return "".join(sList)  # Convert the list back to a string and return it

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n), where n is the length of the input string s. The space complexity is due to the list conversion.