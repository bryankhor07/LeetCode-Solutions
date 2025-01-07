def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
    hashmap = {}
    # Use set data structure for all three arrays to remove duplicate values
    nums1Set = set(nums1)
    nums2Set = set(nums2)
    nums3Set = set(nums3)
    result = []

    # Iterate through all three sets and the get the frequency of the integers
    for n in nums1Set:
        hashmap[n] = 1 + hashmap.get(n, 0)
    for n in nums2Set:
        hashmap[n] = 1 + hashmap.get(n, 0)
    for n in nums3Set:
        hashmap[n] = 1 + hashmap.get(n, 0)

    # Check all the values in the hashmap and add it to the result if it occurs more than twice
    for key, value in hashmap.items():
        if value >= 2:
            result.append(key)
    return result

# Time complexity: O(n)
# Space complexity: O(n)