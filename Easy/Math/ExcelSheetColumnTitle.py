def convertToTitle(self, columnNumber: int) -> str:
    res = []
    while columnNumber > 0:
        n = (columnNumber - 1) % 26  # Adjust for 1-based indexing
        char = chr(n + ord('A'))  # Map to 'A'-'Z'
        res.append(char)
        columnNumber = (columnNumber - 1) // 26  # Adjust columnNumber

    return "".join(res[::-1])  # Reverse the result to get the correct order

# Time Complexity: O(log(columnNumber)), where columnNumber is the input number.
# We divide the columnNumber by 26 in each iteration.
# Space Complexity: O(log(columnNumber)). We use a list to store the result. The length of the list is log(columnNumber) + 1.