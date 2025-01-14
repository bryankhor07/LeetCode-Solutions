def sortedSquares(self, nums: List[int]) -> List[int]:
    # Result array to store squared elements
    res = [0] * len(nums)
    
    # Two pointers
    left, right = 0, len(nums) - 1
    index = len(nums) - 1  # Start filling from the end of result array

    while left <= right:
        # Square the elements at both pointers
        left_square = nums[left] ** 2
        right_square = nums[right] ** 2
        
        # Place the larger square at the current index in the result array
        if left_square > right_square:
            res[index] = left_square
            left += 1
        else:
            res[index] = right_square
            right -= 1
        
        index -= 1  # Move the index for the next largest square

    return res

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(n). The space complexity is due to the result array res, which stores the squared elements of the input list nums. The length of res is n, where n is the length of the input list nums.