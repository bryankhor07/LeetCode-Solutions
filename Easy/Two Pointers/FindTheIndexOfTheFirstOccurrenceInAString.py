def strStr(self, haystack: str, needle: str) -> int:
    if not needle:  # Handle the edge case where needle is an empty string
        return 0

    l = 0
    needleIndex = 0

    while l + needleIndex < len(haystack):
        if haystack[l + needleIndex] == needle[needleIndex]:
            needleIndex += 1
            if needleIndex == len(needle):
                return l
        else:
            l += 1
            needleIndex = 0  # Reset needleIndex for the new starting position
    return -1

# Time Complexity: O((n - m) * m), where n is the length of the haystack and m is the length of the needle.
# Space Complexity: O(1). The algorithm uses a constant amount of extra space.