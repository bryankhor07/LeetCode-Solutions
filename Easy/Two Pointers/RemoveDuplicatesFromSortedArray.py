def removeDuplicates(self, nums: List[int]) -> int:
    # If the list has only one element, no duplicates are possible.
    if len(nums) == 1:
        return 1

    # Initialize the left pointer `l` to track the position of unique elements.
    l = 0

    # Loop through the list starting from the second element (right pointer `r`).
    for r in range(1, len(nums)):
        # If the current element is the same as the last unique element, skip it.
        if nums[l] == nums[r]:
            continue
        else:
            # If a new unique element is found, move the left pointer forward,
            # and update its position with the value of the current element.
            nums[l + 1] = nums[r]
            l += 1

    # The length of the array with unique elements is `l + 1`.
    return l + 1

# Time Complexity: O(n), where n is the length of the input list `nums`.
# Space Complexity: O(1). The algorithm uses a constant amount of extra space.