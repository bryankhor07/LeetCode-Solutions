def minStartValue(self, nums: List[int]) -> int:
    minPrefixSum = float("infinity")
    prefix_sum = [0] * (len(nums) + 1)

    # Calculate the prefix sum and the mininum of the prefix sum
    for i in range(1, len(prefix_sum)):
        prefix_sum[i] = nums[i - 1] + prefix_sum[i - 1]
        minPrefixSum = min(minPrefixSum,  prefix_sum[i])
    
    # Return 1 if the mininum prefix sum is positive
    if minPrefixSum > 0:
        return 1
    return abs(minPrefixSum) + 1

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list once to calculate the prefix sum.
# Space Complexity: O(n). We use a list of size n to store the prefix sum.