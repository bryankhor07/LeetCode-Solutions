def maximizeGreatness(self, nums: List[int]) -> int:
    nums.sort(reverse=True)
    l, r = 0, 1
    count = 0

    # Count the number of times the left pointer is greater than the right pointer
    while r < len(nums):
        # If the left pointer is greater than the right pointer, increment the count and move both pointers to the right
        if nums[l] > nums[r]:
            count += 1
            l += 1
            r += 1
        # If the left pointer is equal to the right pointer, move the right pointer to the right
        elif nums[l] == nums[r]:
            r += 1
    return count

# Time Complexity: O(n log n), where n is the length of the input list nums. The time complexity is due to the sorting of the input list.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the variable count.