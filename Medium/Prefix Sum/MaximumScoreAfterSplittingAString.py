def maxScore(self, s: str) -> int:
    ones = 0
    zeros = 0
    best = float('-inf')

    for i in range(len(s) - 1):
        if s[i] == "1":
            ones += 1
        else:
            zeros += 1
        
        best = max(best, zeros - ones)
        
    if s[-1] == "1":
        ones += 1
    
    return best + ones

# Time Complexity: O(n), where n is the length of the input string `s`.
# We iterate through the string `s` once to calculate the maximum score.
# Space Complexity: O(1). The space complexity is constant as we use only a few variables to store the counts.