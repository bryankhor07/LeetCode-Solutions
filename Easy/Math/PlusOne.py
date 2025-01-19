def plusOne(self, digits: List[int]) -> List[int]:
    n = len(digits)

    # Iterate through the list in reverse order.
    for i in range(n-1, -1, -1):
        # If the current digit is less than 9, increment it by 1 and return the list.
        if digits[i] < 9:
            digits[i] += 1
            return digits
        # If the current digit is 9, set it to 0 and continue to the next digit.
        digits[i] = 0

    # If all digits are 9, create a new list with an additional digit 1 at the beginning.
    newNum = [0] * (n + 1)
    newNum[0] = 1
    return newNum

# Time Complexity: O(n), where n is the length of the input list digits.
# We iterate through the list once to find the first digit that is less than 9.
# Space Complexity: O(n). We use a list of size n to store the new number.