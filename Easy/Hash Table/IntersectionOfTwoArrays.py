def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Initialize a set to store unique elements from nums1
    s = set()
    # Initialize a set to store the result of intersection
    res = set()

    # Add each element from nums1 to the set s
    for i in range(len(nums1)):
        s.add(nums1[i])

    # Check each element in nums2
    for i in range(len(nums2)):
        # If the element is in the set s, add it to the result set res
        if nums2[i] in s:
            res.add(nums2[i])
    
    # Return the result set containing the intersection
    return res

# Time Complexity: O(n + m) where n is the number of elements in nums1 and m is the number of elements in nums2
# Space Complexity: O(n) where n is the number of elements in nums1 since we store all elements in nums1 in a set