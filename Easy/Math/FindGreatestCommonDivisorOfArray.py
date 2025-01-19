def findGCD(self, nums: List[int]) -> int:
    largestNum = max(nums)
    smallestNum = min(nums)
    # Find the greatest common divisor of the smallest and largest numbers
    for i in range(smallestNum, 0, -1):
        # If the current number is a common divisor of the smallest and largest numbers, return it
        if smallestNum % i == 0 and largestNum % i == 0:
            return i

# Time Complexity: O(n), where n is the length of the input list nums.
# We iterate through the list once to find the smallest and largest numbers.
# Space Complexity: O(1). We use a constant amount of extra space.