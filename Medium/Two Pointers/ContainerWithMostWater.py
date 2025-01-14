def maxArea(self, height: List[int]) -> int:
    l = 0
    r = len(height) - 1
    maxArea = 0
    
    # Two pointers: one for the leftmost height, one for the rightmost height
    while l < r:
        # Calculate the area between the two heights
        currentArea = min(height[l], height[r]) * (r - l)
        # Update the maximum area if the current area is greater
        if currentArea > maxArea:
            maxArea = currentArea
        # Move the pointer with the smaller height
        if height[l] < height[r]:
            l += 1
        elif height[l] > height[r]:
            r -= 1
        # If the heights are equal, move the left pointer to the right
        else:
            l += 1
    return maxArea

# Time Complexity: O(n), where n is the length of the input list height.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the variable maxArea.