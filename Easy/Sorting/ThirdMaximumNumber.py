def thirdMax(self, nums: List[int]) -> int:
    # Step 1: Sort the list in ascending order
    numsSorted = sorted(nums)
    
    # Step 2: Initialize variables for the first, second, and third distinct maximums
    fdm = numsSorted[-1]  # First distinct maximum is the largest element
    sdm = None  # Second distinct maximum, initially None
    tdm = None  # Third distinct maximum, initially None

    # Step 3: Iterate through the sorted list in reverse (from second-to-last to the start)
    for i in range(len(numsSorted) - 2, -1, -1):
        # Check for the second distinct maximum
        if sdm is None and numsSorted[i] < fdm:  
            sdm = numsSorted[i]
        # Check for the third distinct maximum
        elif tdm is None and sdm is not None and numsSorted[i] < sdm:  
            tdm = numsSorted[i]
            break  # Exit the loop once the third maximum is found

    # Step 4: Return the appropriate result
    if tdm is None:  # If there is no third distinct maximum
        return fdm  # Return the first distinct maximum
    return tdm  # Otherwise, return the third distinct maximum

# Time complexity: O(nlogn), where n is the length of the input list nums.
# The time complexity is dominated by the sorting operation.
# Space complexity: O(1) since we use a constant amount of extra space.