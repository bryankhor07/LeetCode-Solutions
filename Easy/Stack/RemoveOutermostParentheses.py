def removeOuterParentheses(self, s: str) -> str:
    val = 0 
    ans = []
    idx = 0 
    # Group the primitive decomposition in a list
    for i in range(0, len(s)):
        if (i == 0):
            val += 1 
            continue 
        elif (s[i] == "("):
            val += 1 
        else: 
            val -= 1 
        if (val == 0):
            ans.append(s[idx:i+1])
            idx = i + 1 

    t = ""
    # Remove the outermost parentheses of each primitive decomposition
    for par in ans:
        n = len(par)
        t += par[1:n-1]

    return t

# Time Complexity: O(n), where n is the length of the input string `s`. We iterate through the string once.
# Space Complexity: O(n). The space complexity is due to the list `ans` used to store the primitive decompositions.