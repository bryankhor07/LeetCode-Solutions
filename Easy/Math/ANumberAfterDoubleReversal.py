def isSameAfterReversals(self, num: int) -> bool:
    # If the number is 0, it is the same after any number of reversals
    if num == 0:
        return True
    # If the number does not end in 0, it will be the same after reversals
    if num % 10 != 0:
        return True
    # If the number ends in 0, it won't be the same after reversals
    return False

# Time Complexity: O(1)
# The function performs a constant number of operations to determine if the number is the same after reversals.
# Space Complexity: O(1)