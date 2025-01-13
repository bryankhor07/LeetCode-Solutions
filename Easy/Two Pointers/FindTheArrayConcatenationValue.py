def findTheArrayConcVal(self, nums: List[int]) -> int:
    l, r = 0, len(nums) - 1  # Initialize pointers
    res = 0  # Initialize result

    while l < r:
        # Concatenate the numbers at l and r, convert to integer, and add to res
        temp = str(nums[l]) + str(nums[r])
        res += int(temp)
        l += 1  # Move left pointer
        r -= 1  # Move right pointer

    # If there's a single middle element, add it to res
    if l == r:
        res += nums[l]

    return res

# Time Complexity: O(n), where n is the length of the input list nums.
# Space Complexity: O(1).