def trap(self, height: List[int]) -> int:
    # If the input list is empty or null, no water can be trapped.
    if not height:
        return 0

    # Initialize two pointers:
    # 'l' starts from the leftmost index, and 'r' starts from the rightmost index.
    l, r = 0, len(height) - 1

    # Variables to keep track of the maximum height seen so far from the left and the right.
    leftMax, rightMax = height[l], height[r]

    # Variable to store the total amount of trapped water.
    res = 0

    # Loop until the two pointers meet.
    while l < r:
        # Compare the maximum heights from the left and right.
        if leftMax < rightMax:
            # Move the left pointer to the right.
            l += 1
            # Update the maximum height seen from the left.
            leftMax = max(leftMax, height[l])
            # Add trapped water above the current bar (if any).
            res += leftMax - height[l]
        else:
            # Move the right pointer to the left.
            r -= 1
            # Update the maximum height seen from the right.
            rightMax = max(rightMax, height[r])
            # Add trapped water above the current bar (if any).
            res += rightMax - height[r]

    # Return the total trapped water.
    return res

# Time Complexity: O(n), where n is the length of the input list height.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the variables leftMax, rightMax, and res.