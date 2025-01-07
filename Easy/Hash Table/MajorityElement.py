def majorityElement(self, nums: List[int]) -> int:
    freq = {}
    n = len(nums)

    # Store the frequency of each element
    for num in nums:
        freq[num] = 1 + freq.get(num, 0)
    
    # Return the key that appears more thhan n // 2 times
    for key, value in freq.items():
        if value > n // 2:
            return key

# Time complexity: O(n)
# Space complexity: O(n)