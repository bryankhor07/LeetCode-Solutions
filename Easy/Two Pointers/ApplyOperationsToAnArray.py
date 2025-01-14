def applyOperations(self, nums: List[int]) -> List[int]:
    i = 0
    # Multiply nums[i] by 2 if it equal to it adjacent value
    while i < len(nums) - 1:
        if nums[i] == nums[i+1]:
            nums[i] *= 2
            nums[i + 1] = 0
            i += 2
        else:
            i += 1
    
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
    return nums

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers i, l, r, and the temporary variable temp.