def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Create hashmaps to store the frequency of each element in nums1 and nums2
    freq_map1 = {}
    freq_map2 = {}
    result = []

    # Count occurrences of each number in nums1
    for num in nums1:
        freq_map1[num] = 1 + freq_map1.get(num, 0)

    # Count occurrences of each number in nums2
    for num in nums2:
        freq_map2[num] = 1 + freq_map2.get(num, 0)

    # Find the intersection by comparing frequencies in both hashmaps
    for num, count1 in freq_map1.items():
        if num in freq_map2:  # Check if the number exists in both arrays
            # Determine the minimum count of the number in both arrays
            intersect_count = min(count1, freq_map2[num])
            # Append the number to the result the appropriate number of times
            result.extend([num] * intersect_count)

    return result

# Time Complexity: O(n + m) where n is the number of elements in nums1 and m is the number of elements in nums2
# Space Complexity: O(n + m) where n is the number of unique elements in nums1 and m is the number of unique elements in nums2