def generateKey(self, num1: int, num2: int, num3: int) -> int:
    key = 0
    multiplier = 1  # To construct the key from the least significant to most significant digit

    for _ in range(4):
        # Extract the least significant digit of each number (or 0 if the number is exhausted)
        d1 = num1 % 10 if num1 > 0 else 0
        d2 = num2 % 10 if num2 > 0 else 0
        d3 = num3 % 10 if num3 > 0 else 0

        # Find the smallest digit at this position
        smallest_digit = min(d1, d2, d3)

        # Add this smallest digit to the key
        key += smallest_digit * multiplier
        multiplier *= 10

        # Remove the least significant digit from the numbers
        num1 //= 10
        num2 //= 10
        num3 //= 10

    return key  # Convert key to an integer to remove leading zeros

# Time Complexity: O(1)
# Space Complexity: O(1)