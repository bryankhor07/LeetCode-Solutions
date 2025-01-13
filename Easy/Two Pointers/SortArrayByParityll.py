def sortArrayByParityII(self, nums: List[int]) -> List[int]:
    # Two pointers: one for even indices, one for odd indices
    even, odd = 0, 1
    n = len(nums)

    while even < n and odd < n:
        # If the number at the even index is even, it's correct
        if nums[even] % 2 == 0:
            even += 2
        # If the number at the odd index is odd, it's correct
        elif nums[odd] % 2 != 0:
            odd += 2
        # If both are incorrect, swap them
        else:
            nums[even], nums[odd] = nums[odd], nums[even]
            even += 2
            odd += 2

    return nums

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers even, odd, and the temporary variable temp.