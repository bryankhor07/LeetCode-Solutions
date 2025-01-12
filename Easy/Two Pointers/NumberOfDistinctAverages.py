def distinctAverages(self, nums: List[int]) -> int:
    # Step 1: Initialize a set to store unique average values
    uniqueAvgVal = set()

    # Step 2: Sort the input list in ascending order
    numsSorted = sorted(nums)

    # Step 3: Use two pointers to calculate averages
    l, r = 0, len(numsSorted) - 1  # l points to the start, r points to the end

    # Step 4: Iterate until the two pointers meet
    while l < r:
        # Calculate the average of the smallest and largest remaining elements
        avgVal = (numsSorted[l] + numsSorted[r]) / 2
        
        # Add the average to the set (ensures only unique averages are stored)
        uniqueAvgVal.add(avgVal)
        
        # Move the pointers inward
        l += 1
        r -= 1

    # Step 5: Return the count of unique averages
    return len(uniqueAvgVal)

# Time Complexity Analysis
# The time complexity of this approach is O(nlogn), where n is the length of the input list nums.
# The dominant factor in the time complexity is the sorting operation, which has a time complexity of O(nlogn).
# The two-pointer traversal takes linear time O(n), as the pointers move towards each other.
# Thus, the overall time complexity is O(nlogn) due to the sorting operation.

# Space Complexity Analysis
# The space complexity of this approach is O(n), where n is the length of the input list nums.
# The space complexity is determined by the set uniqueAvgVal, which stores unique average values.
# In the worst case, all the averages are unique, leading to a set of size n.
# Therefore, the space complexity is O(n) in this case.