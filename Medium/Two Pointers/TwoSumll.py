def twoSum(self, numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1

    # Two pointers to find the two numbers that sum up to the target
    # If the sum is greater than the target, move the right pointer to the left
    # If the sum is less than the target, move the left pointer to the right
    # If the sum is equal to the target, return the indices of the two numbers
    while l < r:
        if numbers[l] + numbers[r] == target:
            return [l + 1, r + 1]
        elif numbers[l] + numbers[r] > target:
            r -= 1
        else:
            l += 1

# Time Complexity: O(n), where n is the length of the input list numbers.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l and r.