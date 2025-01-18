def runningSum(self, nums: List[int]) -> List[int]:
    # Calculate the running sum of the input list nums
    # by adding the current element to the previous element
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list once to calculate the running sum.
# Space Complexity: O(1). We do not use any extra space other than the input list.