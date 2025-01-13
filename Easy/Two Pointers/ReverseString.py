def reverseString(self, s: List[str]) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    l = 0
    r = len(s) - 1
    
    # Swap elements from the start and end of the list
    while l < r:
        temp = s[l]
        s[l] = s[r]
        s[r] = temp
        l += 1
        r -= 1

# Time Complexity: O(n), where n is the length of the input list s.
# Space Complexity: O(1). The space complexity is due to the constant space used by the pointers l and r.