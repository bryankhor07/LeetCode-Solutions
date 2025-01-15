def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    # Initialize an empty stack to keep track of elements in nums2
    stack = []
    # A dictionary to map each element in nums2 to its next greater element
    map = {}
    # The result array to store the next greater elements for nums1
    res = []

    # Traverse nums2 in reverse order
    for i in range(len(nums2) - 1, -1, -1):
        # Maintain a decreasing stack:
        # Remove elements from the stack that are less than or equal to the current element
        while stack and stack[-1] <= nums2[i]:
            stack.pop()

        # If the stack is not empty, the top of the stack is the next greater element for nums2[i]
        if stack:
            map[nums2[i]] = stack[-1]

        # Push the current element onto the stack for future comparisons
        stack.append(nums2[i])

    # Traverse nums1 to build the result array
    for num in nums1:
        # Use the map to find the next greater element for each element in nums1
        # If an element is not in the map, it means there is no greater element in nums2, so append -1
        res.append(map.get(num, -1))

    # Return the result array containing next greater elements for nums1
    return res

# Time Complexity: O(n + m), where n is the length of nums1 and m is the length of nums2.
# The algorithm traverses nums2 twice: once to build the map and once to build the result array.
# Space Complexity: O(n + m), where n is the length of nums1 and m is the length of nums2.