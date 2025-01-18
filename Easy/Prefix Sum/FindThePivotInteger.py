def pivotInteger(self, n: int) -> int:
    if n == 1:
        return 1
    
    # Create two lists to store the prefix sums
    leftSum = [i for i in range(1, n + 1)]
    rightSum = [i for i in range(1, n + 1)]

    # Calculate the prefix sums for the left and right lists
    for i in range(1, n):
        leftSum[i] += leftSum[i - 1]

    for i in range(n - 2, -1, -1):
        rightSum[i] += rightSum[i + 1]
        # Check if the prefix sums are equal
        # If they are, return the index
        if rightSum[i] == leftSum[i]:
            return i + 1
    return -1

# Time Complexity: O(n), where n is the input integer n.
# We iterate through the input integer n twice to calculate the prefix sums.
# Space Complexity: O(n). We use two lists of size n to store the prefix sums.