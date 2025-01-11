def countElements(self, nums: List[int]) -> int:
    # Sort the list to arrange elements in ascending order.
    numsSorted = sorted(nums)
    count = 0  # Initialize the count of valid elements.

    # Iterate over the middle elements, skipping the smallest and largest.
    for i in range(1, len(numsSorted) - 1):
        # Check if the current element is strictly between the smallest and largest.
        if numsSorted[i] > numsSorted[0] and numsSorted[i] < numsSorted[-1]:
            count += 1  # Increment the count if the condition is met.

    return count  # Return the final count.

# Time complexity: O(nlogn), where n is the length of the input list nums.
# The time complexity is dominated by the sorting operation.
# Space complexity: O(n), where n is the length of the input list nums.