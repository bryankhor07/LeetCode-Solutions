def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
    n = len(nums)
    prefix_sum = [0] * (n + 1)
    
    # Compute the prefix sum
    for i in range(n):
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Find the minimum sum subarray of lengths l to r
    min_sum = float('inf')
    for length in range(l, r + 1):
        for start in range(n - length + 1):
            # Calculate the sum of the subarray [start, start + length - 1]
            curr_sum = prefix_sum[start + length] - prefix_sum[start]
            if curr_sum > 0:
                min_sum = min(min_sum, curr_sum)
    
    return min_sum if min_sum != float('inf') else -1

# Time Complexity: O(n * (r - l + 1)), where n is the length of the input list nums, and r and l are the given integers.
# We iterate through the list nums for each subarray length between l and r.
# Space Complexity: O(n). We use an additional list of size n to store the prefix sum.