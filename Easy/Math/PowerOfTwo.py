import math

def isPowerOfTwo(self, n: int) -> bool:
    def recursion(exponent):
        if math.pow(2, exponent) == n:
            return True
        elif math.pow(2, exponent) > n:
            return False
        return recursion(exponent + 1)
    return recursion(0)

# Time Complexity: O(log n)
# The function performs a binary search to find the exponent of 2 that equals n.
# The number of iterations is proportional to log n.
# Space Complexity: O(log n)