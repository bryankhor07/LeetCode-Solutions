def judgeSquareSum(self, c: int) -> bool:
    # Initialize two pointers:
    # `l` starts at 0 (the smallest possible square root),
    # `r` starts at the integer square root of `c`.
    l, r = 0, int(math.sqrt(c))

    # Use a two-pointer approach to find the sum of two squares.
    while l <= r:
        # Calculate the sum of the squares of the two pointers.
        current_sum = (l ** 2) + (r ** 2)

        if current_sum == c:
            # If the sum equals `c`, return True as the condition is satisfied.
            return True
        elif current_sum > c:
            # If the sum is greater than `c`, decrease `r` to reduce the sum.
            r -= 1
        else:
            # If the sum is less than `c`, increase `l` to increase the sum.
            l += 1

    # If no combination of `l` and `r` satisfies the condition, return False.
    return False

# Time Complexity: O(sqrt(c)), where c is the input integer. The two-pointer approach runs in O(sqrt(c)) time.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers `l` and `r`.