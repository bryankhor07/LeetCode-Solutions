def targetIndices(self, nums: List[int], target: int) -> List[int]:
    # Sort the input list in ascending order
    # Sorting ensures that all occurrences of the target appear consecutively
    nums.sort()

    # Initialize an empty list to store the indices where the target is found
    res = []

    # Iterate through the sorted list to find the target
    for i in range(len(nums)):
        # If the current element equals the target, append its index to the result list
        if nums[i] == target:
            res.append(i)
    
    # Return the list of indices where the target is found
    return res

# Time Complexity: O(nlogn) due to the sorting operation
# Space Complexity: O(n) to store the indices where the target is found