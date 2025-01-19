def isThree(self, n: int) -> bool:
    count = 0
    k = n

    # Check if n has exactly three divisors.
    while k > 0:
        # If n is divisible by k, increment the count.
        if n % k == 0:
            count += 1
        # If the count is greater than 3, return False.
        if count > 3:
            return False
        k -= 1
    # Return True if the count is exactly 3.
    return count == 3