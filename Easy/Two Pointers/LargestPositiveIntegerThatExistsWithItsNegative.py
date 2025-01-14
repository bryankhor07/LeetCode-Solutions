def findMaxK(self, nums: List[int]) -> int:
    numsSorted = sorted(nums)

    l, r = 0, len(numsSorted) - 1

    # Two pointers: one for the leftmost negative number, one for the rightmost positive number
    # If the absolute value of the leftmost negative number is equal to the rightmost positive number, return the rightmost positive number
    # If the rightmost positive number is greater than the absolute value of the leftmost negative number, move the right pointer to the left
    # If the rightmost positive number is less than the absolute value of the leftmost negative number, move the left pointer to the right
    while l < r:
        if numsSorted[l] < 0 and abs(numsSorted[l]) == numsSorted[r]:
            return numsSorted[r]
        elif numsSorted[r] > abs(numsSorted[l]):
            r -= 1
        else:
            l += 1
    return -1

# Time Complexity: O(n log n), where n is the length of the input list nums. The time complexity is due to the sorting of the input list.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, and the sorted list numsSorted.