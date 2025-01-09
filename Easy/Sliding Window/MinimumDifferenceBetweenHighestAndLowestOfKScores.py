def minimumDifference(self, nums: List[int], k: int) -> int:
    # Sort the input list in ascending order to facilitate comparison of k elements
    nums.sort()

    # Initialize the minimum possible difference to infinity
    # This will track the smallest difference between the largest and smallest values in any k-sized subarray
    minPossibleDiff = float('inf')

    # Set up two pointers: `l` (left) at the start of the window and `r` (right) at the k-th position - 1
    l, r = 0, k - 1

    # Slide the window of size k across the sorted array
    while r < len(nums):
        # Update the minimum difference using the difference between the largest (nums[r]) 
        # and smallest (nums[l]) elements in the current window
        minPossibleDiff = min(minPossibleDiff, nums[r] - nums[l])

        # Move the window to the right by incrementing both `l` and `r`
        l += 1
        r += 1

    # Return the smallest difference found
    return minPossibleDiff

# Time Complexity: O(nlogn) due to the sorting operation
# Space Complexity: O(1) since we are using a constant amount of space