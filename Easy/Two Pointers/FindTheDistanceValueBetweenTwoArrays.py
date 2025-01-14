def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
    arr2.sort()
    count = len(arr1)

    # Iterate through the first array
    for num in arr1:
        l, r = 0, len(arr2) - 1
        # Binary search to find the closest number in the second array
        while l <= r:
            m = (l + r) // 2
            if abs(num - arr2[m]) <= d:  # If within distance, decrement count and break
                count -= 1
                break
            elif arr2[m] > num:  # Adjust binary search bounds
                r = m - 1
            else:
                l = m + 1
    return count

# Time Complexity: O(n log n + m log m), where n is the length of the first array arr1 and m is the length of the second array arr2. The time complexity is due to the sorting of both arrays and the binary search for each element in arr1.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l, r, m, and the variable count.