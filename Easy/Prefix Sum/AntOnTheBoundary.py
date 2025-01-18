def returnToBoundaryCount(self, nums: List[int]) -> int:
    count = 0 # The number of times the ant returns to the boundary

    # Calculate the prefix sum of nums array
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
        # Increment count if the ant returns to the boundary
        if nums[i] == 0:
            count += 1
    return count

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list once to calculate the prefix sum.
# Space Complexity: O(1). We do not use any extra space other than the input list
