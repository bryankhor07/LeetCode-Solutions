def containsDuplicate(self, nums: List[int]) -> bool:
    # Summary: Use a set data structure to store the nums in the array.
    #          Loop through the array and return True if the current
    #          num is in the set. Return False at the end
    hashset = set()

    for i in range(len(nums)):
        if (nums[i] in hashset):
            return True
        hashset.add(nums[i])
    return False

# Time Complexity: O(n) since we loop through the array once
# Space Complexity: O(n) since we store all the nums in the array in the set