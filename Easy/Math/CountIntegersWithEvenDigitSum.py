def countEven(self, num: int) -> int:
    count = 0
    # Continue the loop until num becomes 0
    while num > 0:
        numCopy = num
        sum = 0
        # Calculate the sum of the digits of num
        while numCopy > 0:
            digit = numCopy % 10
            sum += digit
            numCopy = numCopy // 10
        # If the sum is even, increment the count
        if sum % 2 == 0:
            count += 1
        num -= 1
    return count

# Time Complexity: O(n * m), where n is the input number num and m is the number of digits in num.
# The outer loop runs n times, and the inner loop runs m times for each iteration of the outer loop.
# Space Complexity: O(1)