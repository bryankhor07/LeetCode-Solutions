def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
    # Initialize two pointers
    left = right = 0

    # Traverse both arrays as long as neither pointer exceeds its respective array
    while left < len(nums1) and right < len(nums2):
        # If the current elements match, return the common element
        if nums1[left] == nums2[right]:
            return nums1[left]
        # If nums1's element is smaller, move the left pointer
        elif nums1[left] < nums2[right]:
            left += 1
        # Otherwise, move the right pointer
        else:
            right += 1

    # If no common element is found, return -1
    return -1

# Time complexity: O(n + m)
# Space complexity: O(1)