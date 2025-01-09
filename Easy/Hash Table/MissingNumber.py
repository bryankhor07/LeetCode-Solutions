def missingNumber(self, nums: List[int]) -> int:
    # Use a set for O(1) lookups
    numsSet = set(nums)

    # If a number from 0 to len(nums) + 1 is not in the set, return it
    for i in range(len(nums) + 1):
        if i not in numsSet:
            return i
        
# Time Complexity: O(n) where n is the number of elements in the input list
# Space Complexity: O(n) since we store all the elements in the input list in a set