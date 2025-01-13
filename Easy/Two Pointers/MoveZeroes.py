def moveZeroes(self, nums: List[int]) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """
    l = 0
    r = 1

    while r < len(nums):
        if nums[l] == 0 and nums[r] != 0:
            # Swap zero with non-zero
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
        elif nums[l] != 0:
            # Move left pointer if current element is non-zero
            l += 1
        # Always move right pointer
        r += 1

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1).