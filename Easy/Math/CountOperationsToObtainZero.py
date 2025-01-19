def countOperations(self, num1: int, num2: int) -> int:
    count = 0 # Initialize the count of operations

    # Continue the loop until one of the numbers becomes 0
    while num1 != 0 and num2 != 0:
        # If num1 is greater than or equal to num2, subtract num2 from num1
        # Otherwise, subtract num1 from num2
        if num1 >= num2:
            num1 -= num2
        else:
            num2 -= num1
        count += 1
    return count

# Time Complexity: O(max(num1, num2))
# The function performs a constant number of operations in each iteration of the while loop.
# The number of iterations is proportional to the maximum of num1 and num2.
# Space Complexity: O(1)