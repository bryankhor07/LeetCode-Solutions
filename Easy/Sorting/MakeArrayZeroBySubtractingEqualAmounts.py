def minimumOperations(self, nums: List[int]) -> int:
    # Step 1: Sort the array in ascending order
    nums.sort()
    i = 0  # Pointer to track the current index in numsSorted
    minNumOfOperations = 0  # Counter for the number of operations

    # Step 2: Continue the process while the largest number is greater than 0
    while nums[-1] > 0:
        # If the current number is 0, skip it and move the pointer
        if nums[i] == 0:
            i += 1
        else:
            # Subtract the smallest non-zero element from all elements
            x = nums[i]
            for j in range(i, len(nums)):
                nums[j] -= x
            # Increment the operation count
            minNumOfOperations += 1
            # Move to the next number
            i += 1

    return minNumOfOperations

# Time complexity: O(n log n)
# Space complexity: O(1) since we are not using any extra space