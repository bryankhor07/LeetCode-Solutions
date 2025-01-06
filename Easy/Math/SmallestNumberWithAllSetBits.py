def smallestNumber(self, n: int) -> int:
    # Loop indefinitely to find the smallest number meeting the condition
    while True:
        # Convert the current number n to its binary representation as a string
        # bin(n) returns a string like '0b101', so [2:] removes the '0b' prefix
        binaryN = str(bin(n)[2:])
        
        # Check if the binary representation has no '0's
        # binaryN.count('0') counts the number of '0's in the binary string
        if binaryN.count('0') == 0:
            # If there are no '0's, return the current number n
            return n
        
        # If the condition isn't met, increment n and repeat the process
        n += 1

# Time Complexity: O(n)
# Space Complexity: O(1)
