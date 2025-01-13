def countPairs(self, nums: List[int], target: int) -> int:
    nums.sort()

    l = 0
    r = len(nums) - 1
    pairs = 0
    # Count pairs whose sum is less than target
    while l != r:
        # If the sum of the numbers at l and r is less than target then all the pairs from l to r will be less than target
        if nums[l] + nums[r] < target:
            pairs += r - l
            l += 1
        else:
            r -= 1
    return pairs

# Time Complexity: O(n log n), where n is the length of the input list nums. The time complexity is due to the sorting of the input list.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and pairs.