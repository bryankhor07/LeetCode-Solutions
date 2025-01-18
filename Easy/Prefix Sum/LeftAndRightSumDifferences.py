def leftRightDifference(self, nums: List[int]) -> List[int]:
    leftSum = [0] * len(nums)
    rightSum = [0] * len(nums)
    answer = [0] * len(nums)

    # Populate leftSum
    for i in range(1, len(nums)):
        leftSum[i] = nums[i - 1] + leftSum[i - 1]
    
    # Populate rightSum
    for i in range(len(nums) - 2, -1, -1):
        rightSum[i] = nums[i + 1] + rightSum[i + 1]
    
    # Find the difference between left and right sum
    for i in range(len(nums)):
        answer[i] = abs(leftSum[i] - rightSum[i])
    
    return answer

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list twice to calculate the prefix sums.
# Space Complexity: O(n). We use two lists of size n to store the prefix sums.