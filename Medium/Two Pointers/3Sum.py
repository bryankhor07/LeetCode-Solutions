def threeSum(self, nums: List[int]) -> List[List[int]]:
    res = []
    nums.sort()

    # Iterate through the list of numbers
    for i, a in enumerate(nums):
        # Skip duplicates 
        if i > 0 and a == nums[i - 1]:
            continue
        # Two pointers to find the other two numbers
        l, r = i + 1, len(nums) - 1
        while l < r:
            # Check if the sum of the three numbers is zero
            threeSum = a + nums[l] + nums[r]
            if threeSum > 0:
                r -= 1
            elif threeSum < 0:
                l += 1
            else:
                res.append([a, nums[l], nums[r]])
                l += 1
                while nums[l] == nums[l-1] and l < r:
                    l += 1
    return res

# Time Complexity: O(n^2), where n is the length of the input list nums. The time complexity is due to the nested loops and the sorting of the input list.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the temporary variable threeSum.