def findFinalValue(self, nums: List[int], original: int) -> int:
    # Convert the input list to a set for O(1) lookup time
    nums_set = set(nums)

    # Loop until the `original` value is not found in the set
    while original in nums_set:
        # If `original` is in the set, multiply it by 2
        original *= 2

    # Return the final value of `original` after the loop
    return original

# Time Complexity: O(n) where n is the number of elements in the input list
# Space Complexity: O(n) since we store all the elements in the input list in a set