def diStringMatch(self, s: str) -> List[int]:
    l, r = 0, len(s)
    perm = []

    # If the character is "I", append the left pointer and increment it
    # If the character is "D", append the right pointer and decrement it
    for i in range(len(s)):
        if s[i] == "I":
            perm.append(l)
            l += 1
        elif s[i] == "D":
            perm.append(r)
            r -= 1
    perm.append(l)
    
    return perm

# Time Complexity: O(n), where n is the length of the input string s.
# Space Complexity: O(n). The space complexity is due to the list perm, which stores the permutation of integers. The length of perm is n+1, where n is the length of the input string s.