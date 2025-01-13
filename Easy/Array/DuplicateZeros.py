def duplicateZeros(self, arr: List[int]) -> None:
    """
    Do not return anything, modify arr in-place instead.
    """
    i = 0
    while i < len(arr):
        if arr[i] == 0:
            arr.insert(i + 1, 0)  # Insert zero at the next position
            arr.pop()  # Remove the last element to maintain length
            i += 1  # Skip the newly added zero
        i += 1

# Time Complexity: O(n^2), where n is the length of the input list arr.
# Space Complexity: O(1).