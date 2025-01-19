import math

def titleToNumber(self, columnTitle: str) -> int:
    sum = 0
    n = len(columnTitle)

    # Calculate the column number.
    # The column number is the sum of 26^(n-i-1) * (ord(ch) - ord('A') + 1) for each character ch in the column title.
    for i in range(n):
        ch = columnTitle[i]
        p = ord(ch) - ord('A') + 1
        sum += int(math.pow(26, n - i - 1) * p)
    
    return sum

# Time Complexity: O(n), where n is the length of the input string columnTitle.
# We iterate through the string once.
# Space Complexity: O(1). We use a constant amount of extra space.