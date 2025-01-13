def backspaceCompare(self, s: str, t: str) -> bool:
    stackS = []
    stackT = []

    # Iterate through the string s and t and store the characters in stackS and stackT
    # Pop the top character from the stack if the current character is '#'
    # Compare the two stacks at the end
    for i in range(len(s)):
        if s[i] == '#' and stackS:
            stackS.pop()
        elif s[i] != '#':
            stackS.append(s[i])
    for i in range(len(t)):
        if t[i] == '#' and stackT:
            stackT.pop()
        elif t[i] != '#':
            stackT.append(t[i])
    return stackS == stackT

# Time Complexity: O(n + m), where n is the length of the input string s and m is the length of the input string t.
# Space Complexity: O(n + m), where n is the length of the input string s and m is the length of the input string t. The space complexity is due to the stack used to store the characters of the strings s and t.