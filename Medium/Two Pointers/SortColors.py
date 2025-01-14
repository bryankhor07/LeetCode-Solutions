def sortColors(self, nums: List[int]) -> None:
    l, r, i = 0, len(nums) - 1, 0 # Initialize the left pointer l, right pointer r, and current pointer i

    # If the current element is 0, swap it with the left pointer and increment the left pointer
    # If the current element is 2, swap it with the right pointer and decrement the right pointer
    # If the current element is 1, increment the current pointer
    while i <= r:
        if nums[i] == 0:
            nums[l], nums[i] = nums[i], nums[l]
            l += 1
        if nums[i] == 2:
            nums[r], nums[i] = nums[i], nums[r]
            r -= 1
        else:
            i += 1

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, i, and the temporary variable temp.