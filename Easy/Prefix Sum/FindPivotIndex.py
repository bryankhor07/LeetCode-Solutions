def pivotIndex(self, nums: List[int]) -> int:
    leftSum = list(nums)
    rightSum = list(nums)
    n = len(nums)

    # Calculate the prefix sum for the nums array
    for i in range(1, n):
        leftSum[i] += leftSum[i - 1]

    # Calculate the postfix sum for the nums array
    for i in range(n - 2, -1, -1):
        rightSum[i] += rightSum[i + 1]
    
    # Find the index where both prefix and postfix sums are equal
    for i in range(n):
        if leftSum[i] == rightSum[i]:
            return i

    return -1

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list twice to calculate the prefix and postfix sums.
# Space Complexity: O(n). We use two lists of size n to store the prefix and postfix sums